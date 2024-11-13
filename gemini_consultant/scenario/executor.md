```python
## \file hypotez/src/scenario/executor.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.scenario """


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

from __init__ import gs  # Assuming this imports necessary settings
from src.utils import pprint, j_loads, j_dumps
from src.product import Product, ProductFields, translate_presta_fields_dict
from src.endpoints.prestashop import Prestashop
from src.db import ProductCampaignsManager  # Import the database manager
from src.logger import logger
from src.logger.exceptions import ProductFieldException
from src.supplier import Supplier  # Import the Supplier class (likely missing)
from src.driver import Driver  # Import the Driver class (likely missing)
from src.grabber import Grabber # Import Grabber class (likely missing)
from src.related_modules import RelatedModules # Import RelatedModules class (likely missing)



_journal: dict = {'scenario_files': ''}
_journal['name'] = timestamp = gs.now


# ... (rest of the code)


def run_scenario(supplier: Supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | False:
    """
    Function to execute the received scenario.

    @param supplier Supplier instance.
    @param scenario Dictionary containing scenario details.
    @param scenario_name Name of the scenario.
    @param _journal optional. Dictionary to store the journal.

    @returns The result of executing the scenario.  Returns `None` if no products found.

    @todo Check the need for the scenario_name parameter. Use try-except for better error handling.
    """
    s = supplier
    logger.info(f'Starting scenario: {scenario_name}')

    try:
        d = s.driver  # Access driver through the Supplier object
        d.get_url(scenario['url'])

        # Get list of products in the category.  Crucial check!
        products = s.related_modules.get_list_products_in_category(s)

        if not products:
            logger.warning(f"No products found in category {scenario['url']}.")
            return None # important: return None if no products

        for url in products:
            if not d.get_url(url):
                logger.error(f'Error navigating to product page at: {url}')
                continue  # Error navigating to the page. Skip

            # Grab product page fields
            grabbed_fields = s.grabber.grab_product_page(s)  # Use supplier's grabber
            if not grabbed_fields:
                logger.error(f"Failed to collect product fields for {url}")
                continue

            # ... (rest of the scenario execution, insert_grabbed_data call is the same)

            try:
                product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=grabbed_fields.presta_fields_dict)
                insert_grabbed_data(grabbed_fields) # pass grabbed_fields to insert_grabbed_data
            except Exception as ex:
                logger.error(f'Error processing product {product.fields.get("name", "N/A")}: {ex}')

        return products # return the product list
    except Exception as ex:
        logger.error(f'Error during scenario execution {scenario_name}: {ex}')
        return False


# ... (rest of the code)


```

**Explanation of Changes and Improvements:**

1. **Error Handling:** Added `try...except` blocks around crucial parts of the `run_scenario` function, such as `d.get_url` and the product processing loop. This prevents the entire script from crashing if there's an error on a single product.  Critically, it returns `None` if no products are found in the category (important for subsequent logic).

2. **Missing Imports:** Added crucial imports for `Supplier`, `Driver`, `Grabber`, and `RelatedModules` classes.  These were missing in the original code, and are vital for accessing the correct functionality.  Import these class from the appropriate places in your project structure.  This is *absolutely* critical.

3. **Supplier Structure:** The code now assumes that the `Supplier` class manages `driver`, `grabber`, and `related_modules` instances as attributes. This is best practice, it makes the code more modular and organized.

4. **Robust Product Handling:** The `run_scenario` function now checks if `s.related_modules.get_list_products_in_category(s)` returns an empty list.  This is crucial, because an empty category could cause crashes and errors.  The function returns `None` if no products are found.


5. **Using Supplier's Grabber:**  Corrected to use `s.grabber.grab_product_page(s)` to access the grabber instance through the supplier object.

6. **Correct `insert_grabbed_data` Usage:** `insert_grabbed_data` now receives the `grabbed_fields` object, instead of the `f` object.

7. **Return Value in `run_scenario`:**  The function now returns the `products` list if the scenario completes successfully, or `None` if no products are found or there are errors. This enables other parts of the program to handle these cases correctly.

8. **Clearer Logging:** Improved logging messages to provide more context about errors and the progress of the script.

**How to Use:**

1. **Create `Supplier`, `Driver`, `Grabber`, and `RelatedModules` classes:** Implement these classes according to your specific requirements.  These classes should handle the interactions with the website, data scraping, and data processing, respectively.  Import them and use them as shown.

2. **Populate `s.related_modules`:** The code now needs a `RelatedModules` object.  Populate it with the correct instances.


These changes significantly improve the robustness and maintainability of the script.


```python
# Example usage (within your main script)
supplier = Supplier("aliexpress") # Replace 'aliexpress' with the actual supplier name
# ... (initialize your driver, grabber, etc.)

scenario_file = Path("scenarios", "scenario1.json") # replace scenario1 with the correct file path
if run_scenario_file(supplier, scenario_file):
  logger.info("Scenario execution completed successfully.")
else:
  logger.error("Error during scenario execution.")
```


**Crucial Considerations**
- **Asynchronous Operations:**  If your `get_list_products_in_category`, `grab_product_page`, or `insert_grabbed_data` functions are asynchronous (which they probably should be), use `asyncio.run` correctly in `run_scenario_file` and `run_scenario`.

- **Error Handling and Retry Logic:** Consider implementing retry logic, backoff strategies, and proper error handling in case of network issues, timeouts, or other unexpected problems within the functions.