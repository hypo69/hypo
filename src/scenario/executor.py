
"""
Script Executor
@details Executor functions:
- `run_scenario_files()` - Accepts a list of scenario files, parses the list, and hands it over to the file executor.
- `run_scenario_file()` - Parses the scenario file into a list of scenarios and hands each over to the executor `run_scenario()`.
- `run_scenario()` - Executes the scenario. A typical scenario contains information about one category of goods. The driver translates the URL to the category page, retrieves links to products in the category, follows each of them, and hands it over to the specific supplier's grabber to collect information from the product page fields. After receiving the fields, the function passes them to the PrestaShop handler.
- `run_scenarios()` - Adds flexibility: I can collect a list of scenarios from different files.

Executor functions:
- `run_scenario_files()` - Accepts a list of scenario files, parses the list, and hands it over to the file executor.
- `run_scenario_file()` - Parses the scenario file into a list of scenarios and hands each over to the executor `run_scenario()`.
- `run_scenario()` - Executes the scenario. A typical scenario contains information about one category of goods. The driver translates the URL to the category page, retrieves links to products in the category, follows each of them, and hands it over to the specific supplier's grabber to collect information from the product page fields. After receiving the fields, the function passes them to the PrestaShop handler.
- `run_scenarios()` - Adds flexibility: I can collect a list of scenarios from different files.


Исполняется такая логика:
<pre>
   +-----------+
   |  Scenario |
   +-----------+
        |
        | Defines
        |
        v
  +-----------+
  | Executor  |
  +-----------+
        |
        | Uses
        |
        v
  +-----------+        +-----------+
  |  Supplier | <----> |  Driver   |
  +-----------+        +-----------+
        |                      |
        | Provides Data        | Provides Interface
        |                      |
        v                      v
  +-----------+        +-----------------+
  |  Prestashop        | Other Suppliers |
  +-----------+        +-----------------+
</pre>
@code
s = Suppler('aliexpress)

run_scenario_files(s,'file1')


scenario_files = ['file1',...]
run_scenario_files(s,scenario_files)


scenario1 = {'key':'value'}
run_scenarios(s,scenario1)


list_of_scenarios = [scenario1,...]
run_scenarios(s,list_of_scenarios)

@endcode
Пример файла сценария:
@code
{
  "scenarios": {

    "feet-hand-treatment": {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
      "name": "טיפוח כפות ידיים ורגליים",
      "condition": "new",
      "presta_categories": {
        "default_category": 11259,
        "additional_categories": []
      }
    },



    "creams-butters-serums-for-body": {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/creams-butters-serums-for-body/",
      "name": "קרמים, חמאות וסרומים לגוף",
      "condition": "new",
      "presta_categories": {
        "default_category": 11260,
        "additional_categories": []
      }
    }
}
@endcode

Подробно о словаре сценариев читать здесь: ...


Когда программа запускается через main() происходит такая последовательность исполнения:
@code
s = Supplier('aliexpress')


s.run()


s.run('file1')


scenario_files = ['file1',...]
s.run(scenario_files)


scenario1 = {'key':'value'}
s.run(scenario1)


list_of_scenarios = [scenario1,...]
s.run(list_of_scenarios)

@endcode

@image html executor.png
"""


import os
import sys
import requests
import asyncio
import time
import tempfile
from datetime import datetime
from math import log, prod
from pathlib import Path
from typing import Dict, List

import header
from src import gs
from src.utils import pprint, j_loads, j_dumps
from src.product import Product, ProductFields, translate_presta_fields_dict
from src.endpoints.prestashop import Prestashop
from src.db import ProductCampaignsManager
from src.logger import logger
from src.logger.exceptions import ProductFieldException


_journal: dict = {'scenario_files': ''}
_journal['name'] = timestamp = gs.now


def dump_journal(s, journal: dict):
    """
    Journaling the process of executing the scenario.
    @param journal `dict`: Dictionary storing the state of scenario execution.
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)


def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """ 
    Function to run a list of scenario files one after another.

    @param s Supplier instance.
    @param scenario_files_list List of file paths for the JSON scenario files.
    @returns True if all scenarios were executed successfully, else False.

    @details The set of scenarios can be passed via scenario_files_list. If the list of scenarios is not passed, it is taken from the default settings of the supplier. For each scenario in the list, the function run_scenario_file() will be called, which loads the scenario file in JSON format and executes each scenario using the run_scenario() function.

    @todo 1. Make logging more detailed.
          2. Implement logic for gathering scenarios after a crash.
          3. If an empty value is allowed in scenario_files_list - execute all scenarios by default.
    """
    scenario_files_list = [scenario_files_list] if isinstance(scenario_files_list, str) else s.scenario_files
    _journal['scenario_files']: dict = {}
    for scenario_file in scenario_files_list:
        _journal['scenario_files'].update({'scenario_file': scenario_file.name})
        dump_journal(s, _journal)
        if run_scenario_file(s, scenario_file):
            _journal['scenario_files'][scenario_file]['message'] = f"{scenario_file} completed successfully!"
            dump_journal(s, _journal)
            logger.success(f'Scenario {scenario_file} completed successfully!')
        else:
            _journal['scenario_files'][scenario_file]['message'] = f"{scenario_file} FAILED!"
            dump_journal(s, _journal)
            logger.error(f'Scenario {scenario_file} failed to execute!')

    return True


def run_scenario_file(s, scenario_file: Path | str) -> bool:
    """
    Loads the scenario from a file.

    @param s Supplier instance.
    @param scenario_file Path to the scenario file.
    @returns True if the scenario was executed successfully, False otherwise.
    @code
    from pathlib import Path

    # Path to the scenario file
    file_path = Path("scenarios", "scenario1.json")

    # Running the scenario
    result = run_scenario_file(supplier_instance, file_path)

    # Checking the result
    if result:
        print("Scenario executed successfully.")
    else:
        print("An error occurred while executing the scenario.")
    @endcode
    """
    logger.info(f'Starting scenario file {str(Path(scenario_file).name)}')

    scenarios_dict = j_loads(scenario_file)['scenarios']
    _journal['scenario_files'][Path(scenario_file).name]: dict = {}

    for scenario_name, scenario in scenarios_dict.items():
        s.current_scenario = scenario
        _journal['scenario_files'][Path(scenario_file).name]: dict = {}

        if run_scenario(s, scenario, scenario_name, _journal):
            _journal['scenario_files'][Path(scenario_file).name].update({scenario_name: 'success'})
            dump_journal(s, _journal)
            s.supplier_settings['runned_scenario'].append(scenario_name)
            logger.success(f'Last executed scenario: {scenario_name}')
        else:
            _journal['scenario_files'][Path(scenario_file).name].update({scenario_name: 'failed'})
            dump_journal(s, _journal)
            logger.critical(f"""
            Scenario {scenario} 
            {str(Path(scenario_file).name)}
            interrupted with an error
            """)

    return True


def run_scenarios(s, scenarios: List[dict] | dict = None, _journal=None) -> List | dict | False:
    """
    Function to execute a list of scenarios (NOT FILES).

    @param s Supplier instance.
    @param scenarios Accepts a list of scenarios or a single scenario as a dictionary. The run_scenario(s, scenario) function is called to execute scenarios.
    @returns The result of executing the scenarios as a list or dictionary, depending on the input data type, or False in case of an error.

    @todo Check the option when no scenarios are specified from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
    """
    if not scenarios:
        scenarios = [s.current_scenario]
        """
        If no scenarios are specified, take them from s.current_scenario.
        @todo Check this option from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
        """

    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res = run_scenario(s, scenario)
        _journal['scenario_files'][-1][scenario] = str(res)
        dump_journal(s, _journal)
    return res


def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | False:
    """
    Function to execute the received scenario.

    @param supplier Supplier instance.
    @param scenario Dictionary containing scenario details.
    @param scenario_name Name of the scenario.

    @returns The result of executing the scenario.

    @todo Check the need for the scenario_name parameter.
    """
    s = supplier
    logger.info(f'Starting scenario: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    d.get_url(scenario['url'])

    # Get list of products in the category
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # No products in the category (or they haven't loaded yet)
    if not list_products_in_category:
        logger.warning('No product list collected from the category page. Possibly an empty category - ', d.current_url)
        return

    for url in list_products_in_category:
        if not d.get_url(url):
            logger.error(f'Error navigating to product page at: {url}')
            continue  # <- Error navigating to the page. Skip

        # Grab product page fields
        grabbed_fields = s.related_modules.grab_product_page(s)
        f: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not f:
            logger.error(f"Failed to collect product fields")
            continue

        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(f)
        except Exception as ex:
            logger.error(f'Product {product.fields["name"][1]} could not be saved', ex)
            continue

    return list_products_in_category


def insert_grabbed_data(product_fields: ProductFields):
    """
    Insert grabbed product data into PrestaShop.

    @todo Move this logic to another file. In PrestaShop class.
    """
    asyncio.run(execute_prestashop_insert(product_fields))


async def execute_prestashop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    await execute_prestashop_insert(f, coupon_code, start_date, end_date)


def execute_prestashop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool:
    """
    Insert the product into PrestaShop.

    @param f ProductFields instance containing the product information.
    @param coupon_code Optional coupon code.
    @param start_date Optional start date for the promotion.
    @param end_date Optional end date for the promotion.

    @returns True if the insertion was successful, False otherwise.
    """
    try:
        presta = Prestashop()
        presta.post_product_data(
            product_id=f.product_id,
            product_name=f.product_name,
            product_category=f.product_category,
            product_price=f.product_price,
            description=f.description,
            coupon_code=coupon_code,
            start_date=start_date,
            end_date=end_date
        )
        return True
    except Exception as ex:
        logger.error(f'Failed to insert product data into PrestaShop: {ex}', ex)
        return False
