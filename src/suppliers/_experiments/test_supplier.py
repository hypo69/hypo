## \file /src/suppliers/_experiments/test_supplier.py
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
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier


class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.supplier_prefix = 'test_supplier'
        self.lang = 'en'
        self.method = 'web'
        self.supplier_settings = {
            'supplier_id': '123',
            'price_rule': '*1.2',
            'if_login': True,
            'login_url': 'http://example.com/login',
            'start_url': 'http://example.com/start',
            'parcing method [webdriver|api]': 'webdriver',
            'scenarios': [
                {'name': 'scenario1', 'file': 'scenario1.json'},
                {'name': 'scenario2', 'file': 'scenario2.json'},
            ]
        }
        self.locators = {
            'search_box': {'xpath': '//*[@id="search-box"]'},
            'search_button': {'xpath': '//*[@id="search-button"]'},
            'product_name': {'xpath': '//*[@id="product-name"]'},
            'product_price': {'xpath': '//*[@id="product-price"]'},
        }
        self.supplier = Supplier('example_supplier')
        self.settings_file = Path(__file__).parent / 'data/example_supplier/example_supplier.json'
        self.locators_file = Path(__file__).parent / 'data/example_supplier/locators.json'
    

    @patch('mymodule.supplier.gs.j_loads')
    @patch('mymodule.supplier.Driver')
    def test_init_webdriver(self, mock_driver, mock_j_loads):
        mock_j_loads.return_value = self.supplier_settings
        mock_driver.return_value = MagicMock()
        supplier = Supplier(self.supplier_prefix, self.lang, self.method)
        self.assertEqual(supplier.supplier_prefix, self.supplier_prefix)
        self.assertEqual(supplier.lang, self.lang)
        self.assertEqual(supplier.scrapping_method, self.method)
        self.assertEqual(supplier.supplier_id, self.supplier_settings['supplier_id'])
        self.assertEqual(supplier.price_rule, self.supplier_settings['price_rule'])
        self.assertEqual(supplier.login_data['if_login'], self.supplier_settings['if_login'])
        self.assertEqual(supplier.login_data['login_url'], self.supplier_settings['login_url'])
        self.assertEqual(supplier.start_url, self.supplier_settings['start_url'])
        self.assertEqual(supplier.scenarios, self.supplier_settings['scenarios'])
        mock_j_loads.assert_called_once_with(Path('suppliers', self.supplier_prefix, f'''{self.supplier_prefix}.json'''))
        mock_driver.assert_called_once()

    @patch('mymodule.supplier.gs.j_loads')
    def test_init_api(self, mock_j_loads):
        self.method = 'api'
        mock_j_loads.return_value = self.supplier_settings
        supplier = Supplier(self.supplier_prefix, self.lang, self.method)
        self.assertEqual(supplier.supplier_prefix, self.supplier_prefix)
        self.assertEqual(supplier.lang, self.lang)
        self.assertEqual(supplier.scrapping_method, self.method)
        self.assertEqual(supplier.supplier_id, self.supplier_settings['supplier_id'])
        self.assertEqual(supplier.price_rule, self.supplier_settings['price_rule'])
        self.assertEqual(supplier.login_data['if_login'], self.supplier_settings['if_login'])
        self.assertEqual(supplier.login_data['login_url'], self.supplier_settings['login_url'])
        self.assertEqual(supplier.start_url, self.supplier_settings['start_url'])
        self.assertEqual(supplier.scenarios, self.supplier_settings['scenarios'])
        mock_j_loads.assert_called_once_with(Path('suppliers', self.supplier_prefix, f'''{self.supplier_prefix}.json'''))

    def test_supplier_load_settings_success():
        supplier = Supplier(supplier_prefix='dummy')
        assert supplier.supplier_id == 'dummy'
        assert supplier.price_rule == 'dummy'
        assert supplier.login_data == {
            'if_login': None,
            'login_url': None,
            'user': None,
            'password': None,
        }
        assert supplier.start_url == 'dummy'
        assert supplier.scrapping_method == 'web'
        assert supplier.scenarios == []

    def test_supplier_load_settings_failure():
        supplier = Supplier(supplier_prefix='nonexistent')
        assert supplier.supplier_id == None
        assert supplier.price_rule == None
        assert supplier.login_data == {
            'if_login': None,
            'login_url': None,
            'user': None,
            'password': None,
        }
        assert supplier.start_url == None
        assert supplier.scrapping_method == ''
    
    def test_load_settings(supplier):
        assert supplier.supplier_prefix == 'example_supplier'
        assert supplier.lang == 'en'
        assert supplier.scrapping_method == 'web'
        assert supplier.supplier_id == '1234'
        assert supplier.price_rule == 'example_price_rule'
        assert supplier.login_data == {'if_login': True, 'login_url': 'https://example.com/login', 'user': None, 'password': None}
        assert supplier.start_url == 'https://example.com/start'
        assert supplier.scenarios == [{'name': 'scenario1', 'steps': [{'type': 'click', 'locator': 'example_locator'}]}]
        assert supplier.locators == {'example_locator': '//html/body/div'}


    def test_load_settings_invalid_path(supplier, caplog):
        supplier._load_settings()
        assert 'Error reading suppliers/example_supplier/example_supplier.json' in caplog.text


    def test_load_settings_invalid_locators_path(supplier, caplog):
        supplier.scrapping_method = 'api'
        supplier._load_settings()
        assert 'Error reading suppliers/example_supplier/locators.json' in caplog.text


    def test_load_settings_api(supplier):
        supplier.scrapping_method = 'api'
        assert supplier.locators is None
        assert supplier.driver is None


    def test_load_related_functions(supplier):
        assert hasattr(supplier, 'related_modules')
        assert hasattr(supplier.related_modules, 'example_function')


    def test_init(supplier):
        assert supplier.driver is not None
        assert isinstance(supplier.p, list)
        assert isinstance(supplier.c, list)
        assert supplier.current_scenario_filename is None
        assert supplier.current_scenario is None

 
    def test_load_settings_success(self):
        with patch('builtins.open', return_value=MagicMock(spec=open, read=lambda: json.dumps({'supplier_id': 123}))) as mock_open:
            result = self.supplier._load_settings()
            self.assertTrue(result)
            self.assertEqual(self.supplier.supplier_id, 123)

    def test_load_settings_failure(self):
        with patch('builtins.open', side_effect=Exception):
            result = self.supplier._load_settings()
            self.assertFalse(result)
    
    def test_run_api(self):
        with patch('my_module.supplier.importlib.import_module') as mock_import:
            mock_module = MagicMock()
            mock_module.run_api.return_value = True
            mock_import.return_value = mock_module
            result = self.supplier.run()
            self.assertTrue(result)
    
    def test_run_scenario_files_success(self):
        with patch.object(self.supplier, 'login', return_value=True):
            self.supplier._load_settings()
            scenario_file = Path(__file__).parent / 'data/example_supplier/scenario.json'
            result = self.supplier.run_scenario_files(str(scenario_file))
            self.assertTrue(result)

    def test_run_scenario_files_failure(self):
        with patch.object(self.supplier, 'login', return_value=True):
            self.supplier._load_settings()
            scenario_file = Path(__file__).parent / 'data/example_supplier/invalid_scenario.json'
            result = self.supplier.run_scenario_files(str(scenario_file))
            self.assertFalse(result)
    
    def test_run_with_login(self):
        with patch.object(self.supplier, 'login', return_value=True) as mock_login:
            self.supplier._load_settings()
            result = self.supplier.run()
            self.assertTrue(mock_login.called)
            self.assertTrue(result)
    
    def test_run_without_login(self):
        self.supplier.login['if_login'] = False
        with patch.object(self.supplier, 'run_scenario_files', return_value=True) as mock_run_scenario_files:
            self.supplier._load_settings()
            result = self.supplier.run()
            self.assertFalse(mock_run_scenario_files.called_with())
            self.assertTrue(result)

