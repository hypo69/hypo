Вот файл примеров для модуля `executor.py`, который иллюстрирует использование всех функций и методов, представленных в коде. В примерах показано, как можно использовать функции для выполнения сценариев, обработки файлов сценариев, работы с продуктами и взаимодействия с PrestaShop API.

```python
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

"""
Examples for the `executor` module from `src.scenario.executor`.

This file contains examples of how to use the functions provided in the `executor` module.
The examples demonstrate how to run scenarios, handle scenario files, and interact with PrestaShop API.

@details
- `Example 1` shows how to run a list of scenario files.
- `Example 2` demonstrates how to run a single scenario file.
- `Example 3` illustrates how to run a single scenario.
- `Example 4` provides an example of executing a product page scenario.
- `Example 5` shows how to add a coupon using PrestaShop API.

@image html executor.png
"""

from pathlib import Path
from src.scenario.executor import run_scenario_files, run_scenario_file, run_scenarios, run_scenario, insert_grabbed_data, execute_prestashop_insert, execute_prestashop_insert_async, add_coupon
from src.utils import j_loads
from src.product import ProductFields
from src.prestashop import Prestashop

# Assuming `Supplier` class is available and has necessary methods and attributes
class MockSupplier:
    def __init__(self):
        self.supplier_abs_path = Path('/path/to/scenarios')
        self.scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
        self.current_scenario = None
        self.supplier_settings = {'runned_scenario': []}
        self.related_modules = MockRelatedModules()
        self.driver = MockDriver()

class MockRelatedModules:
    def get_list_products_in_category(self, s):
        return ['http://example.com/product1', 'http://example.com/product2']

    def grab_product_page(self, s):
        return ProductFields(
            presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
            assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
        )

    async def async_grab_page(self, s):
        return self.grab_product_page(s)

class MockDriver:
    def get_url(self, url):
        return True

# Example 1: Run a list of scenario files
def example_run_scenario_files():
    supplier = MockSupplier()
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    result = run_scenario_files(supplier, scenario_files)
    if result:
        print("All scenarios executed successfully.")
    else:
        print("Some scenarios failed.")

# Example 2: Run a single scenario file
def example_run_scenario_file():
    supplier = MockSupplier()
    scenario_file = Path('scenarios/scenario1.json')
    result = run_scenario_file(supplier, scenario_file)
    if result:
        print("Scenario file executed successfully.")
    else:
        print("Failed to execute scenario file.")

# Example 3: Run a single scenario
def example_run_scenario():
    supplier = MockSupplier()
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    result = run_scenario(supplier, scenario)
    if result:
        print("Scenario executed successfully.")
    else:
        print("Failed to execute the scenario.")

# Example 4: Insert grabbed product data into PrestaShop
def example_insert_grabbed_data():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    insert_grabbed_data(product_fields)
    print("Product data inserted into PrestaShop.")

# Example 5: Add a coupon using PrestaShop API
def example_add_coupon():
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    add_coupon(credentials, reference, coupon_code, start_date, end_date)
    print("Coupon added successfully.")

# Example 6: Execute PrestaShop insert asynchronously
async def example_execute_prestashop_insert_async():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    await execute_prestashop_insert_async(product_fields)
    print("Product data inserted into PrestaShop asynchronously.")

# Example 7: Execute PrestaShop insert synchronously
def example_execute_prestashop_insert():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    result = execute_prestashop_insert(product_fields)
    if result:
        print("Product data inserted into PrestaShop.")
    else:
        print("Failed to insert product data into PrestaShop.")

# Running the examples
if __name__ == "__main__":
    example_run_scenario_files()
    example_run_scenario_file()
    example_run_scenario()
    example_insert_grabbed_data()
    example_add_coupon()
    asyncio.run(example_execute_prestashop_insert_async())
    example_execute_prestashop_insert()
```

### Пояснение к примерам

1. **Example 1: `run_scenario_files`**  
   Запускает список файлов сценариев и выполняет их один за другим.

2. **Example 2: `run_scenario_file`**  
   Запускает один файл сценария.

3. **Example 3: `run_scenario`**  
   Выполняет один сценарий.

4. **Example 4: `insert_grabbed_data`**  
   Вставляет данные о продукте в PrestaShop.

5. **Example 5: `add_coupon`**  
   Добавляет купон в базу данных PrestaShop.

6. **Example 6: `execute_prestashop_insert_async`**  
   Асинхронно выполняет вставку данных о продукте в PrestaShop.

7. **Example 7: `execute_prestashop_insert`**  
   Синхронно выполняет вставку данных о продукте в PrestaShop.

Эти примеры помогут вам понять, как можно использовать функции модуля `executor` для различных задач в вашем проекте.