## \file /src/suppliers/_experiments/test_execute_scenaries.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers._experiments 
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
  
""" module: src.suppliers._experiments """


import unittest
from unittest.mock import MagicMock
from execute_scenarios import run_scenarios,run_scenario_file,run_scenario,grab_product_page

class TestRunListOfScenarioFiles(unittest.TestCase):
    
    def test_with_scenario_files_...ed(self):
        s = MagicMock()
        scenario_files = ["scenario1.json", "scenario2.json"]
        s.settings = {
            'check categories on site': False,
            'scenarios': ["default1.json", "default2.json"]
        }
        
        result = run_scenarios(s, scenario_files)
        
        self.assertTrue(result)
        s.related_modules.build_shop_categories.assert_not_called()
        self.assertEqual(s.current_scenario_filename, "scenario2.json")
        self.assertEqual(s.settings['last_runned_scenario'], "scenario2.json")
        
    def test_with_no_scenario_files_...ed(self):
        s = MagicMock()
        s.settings = {
            'check categories on site': True,
            'scenarios': ["default1.json", "default2.json"]
        }
        
        result = run_scenarios(s)
        
        self.assertTrue(result)
        s.related_modules.build_shop_categories.assert_called_once()
        self.assertEqual(s.current_scenario_filename, "default2.json")
        self.assertEqual(s.settings['last_runned_scenario'], "default2.json")


class TestRunScenarioFile(unittest.TestCase):

    def setUp(self):
        # Create a mock Supplier instance with the necessary attributes
        self.s = MagicMock()
        self.s.current_scenario_filename = "test_scenario.json"
        self.s.settings = {
            "parcing method [webdriver|api]": "webdriver"
        }
        self.s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
        self.s.scenarios = {
            "scenario1": {
                "url": "https://example.com",
                "steps": [
                    # steps for scenario1
                ]
            },
            "scenario2": {
                "url": None,
                "steps": [
                    # steps for scenario2
                ]
            }
        }

    def test_run_scenario_file_webdriver(self):
        with patch("your_module.j_loads") as mock_j_loads:
            mock_j_loads.return_value = {"scenarios": self.s.scenarios}
            with patch("your_module.run_scenario") as mock_run_scenario:
                run_scenario_file(self.s, "test_scenario.json")
                mock_j_loads.assert_called_once_with("/path/to/scenarios/test_scenario.json")
                mock_run_scenario.assert_any_call(self.s, self.s.scenarios["scenario1"])
                mock_run_scenario.assert_not_called_with(self.s, self.s.scenarios["scenario2"])

    def test_run_scenario_file_api(self):
        self.s.settings["parcing method [webdriver|api]"] = "api"
        with patch("your_module.related_modules.run_scenario_file_via_api") as mock_run_scenario_file_via_api:
            run_scenario_file(self.s, "test_scenario.json")
            mock_run_scenario_file_via_api.assert_called_once_with(self.s, "test_scenario.json")

    def test_run_scenario_file_no_scenarios(self):
        with patch("your_module.j_loads") as mock_j_loads:
            mock_j_loads.return_value = {"scenarios": None}
            with patch("your_module.logger.error") as mocklogger_console_error:
                self.assertFalse(run_scenario_file(self.s, "test_scenario.json"))
                mocklogger_console_error.assert_called_once_with("Возможно файл test_scenario.json не содержит сценариев")

                
class TestGrabProductPage(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects, like mock objects or the Supplier instance
        self.s = Supplier()

    def test_grab_product_page_succesStringFormatterul(self):
        # Test grabbing a product page when all necessary data is present
        self.s.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}
        result = grab_product_page(self.s)
        self.assertTrue(result)
        self.assertEqual(len(self.s.p), 1)
        self.assertEqual(self.s.p[0]['id'], '123')
        self.assertEqual(self.s.p[0]['price'], 19.99)
        self.assertEqual(self.s.p[0]['name'], 'Product Name')

    def test_grab_product_page_failure(self):
        # Test grabbing a product page when some necessary data is missing
        self.s.grab_product_page = lambda _: {'name': 'Product Name'}
        result = grab_product_page(self.s)
        self.assertFalse(result)
        self.assertEqual(len(self.s.p), 0)

        import unittest


class TestRunScenario(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier()
        self.supplier.settings['parcing method [webdriver|api]'] = 'webdriver'
        self.supplier.current_scenario_filename = 'test_scenario.json'
        self.supplier.export_file_name = 'test_export'
        self.supplier.dir_export_imagesECTORY_FOR_STORE = '/test/path'
        self.supplier.p = []

    def tearDown(self):
        ...

    def test_run_scenario_no_url(self):
        scenario = {'name': 'scenario1', 'url': None}
        self.supplier.scenarios = {'scenario1': scenario}
        self.supplier.get_list_products_in_category = MagicMock(return_value=[])
        self.assertFalse(self.supplier.run_scenario(scenario))

    def test_run_scenario_valid_url(self):
        scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}
        self.supplier.scenarios = {'scenario2': scenario}
        self.supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])
        self.supplier.grab_product_page = MagicMock(return_value=True)
        self.supplier.export_files = MagicMock()
        self.assertTrue(self.supplier.run_scenario(scenario))
        self.assertEqual(len(self.supplier.p), 2)
        self.supplier.export_files.assert_called_once_with(self.supplier, self.supplier.p, 'test_export-1', ['csv'])

    def test_run_scenario_export_empty_list(self):
        scenario = {'name': 'scenario3', 'url': 'https://example.com/products'}
        self.supplier.scenarios = {'scenario3': scenario}
        self.supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1'])
        self.supplier.grab_product_page = MagicMock(return_value=False)
        self.supplier.export_files = MagicMock()
        self.assertFalse(self.supplier.run_scenario(scenario))
        self.assertEqual(len(self.supplier.p), 0)
        self.supplier.export_files.assert_not_called()

if __name__ == '__main__':
    unittest.main()

