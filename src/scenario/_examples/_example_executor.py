## \file /src/scenario/_examples/_example_executor.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.scenario._examples 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.scenario._examples """



...
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

import asyncio
from pathlib import Path
from src.scenario.executor import run_scenario_files, run_scenario_file, run_scenarios, run_scenario, insert_grabbed_data, execute_PrestaShop_insert, execute_PrestaShop_insert_async, add_coupon
from src.utils.jjson import j_loads_ns
from src.endpoints.prestashop.product_fields import ProductFields
from src.endpoints.PrestaShop import PrestaShop

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

    async def grab_page(self, s):
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
async def example_execute_PrestaShop_insert_async():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    await execute_PrestaShop_insert_async(product_fields)
    print("Product data inserted into PrestaShop asynchronously.")

# Example 7: Execute PrestaShop insert synchronously
def example_execute_PrestaShop_insert():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    result = execute_PrestaShop_insert(product_fields)
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
    asyncio.run(example_execute_PrestaShop_insert_async())
    example_execute_PrestaShop_insert()


