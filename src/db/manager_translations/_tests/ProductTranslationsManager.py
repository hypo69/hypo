## \file /src/db/manager_translations/_tests/ProductTranslationsManager.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.db.manager_translations._tests 
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
  
""" module: src.db.manager_translations._tests """


""" @namespace src.db.manager_translations._tests """
import unittest
from unittest.mock import MagicMock, patch
from ..product_translations import ProductTranslationsManager

class TestProductTranslationsManager(unittest.TestCase):

    def setUp(self):
        # Initialize the ProductTranslationsManager with a mocked session
        self.manager = ProductTranslationsManager()
        self.manager.session = MagicMock()

    def test_insert_record(self):
        # Test inserting a record
        fields = {'product_reference': 'reference_product_value', 'locale': 'en', 'name': 'Product Name'}
        self.manager.insert_record(fields)
        self.manager.session.add.assert_called_once()

    def test_select_record(self):
        # Test selecting a record
        # Mock the query and return some dummy records
        dummy_records = [MagicMock(), MagicMock()]
        self.manager.session.query.return_value.filter.return_value.all.return_value = dummy_records

        # Call the method
        records = self.manager.select_record(product_reference='reference_product_value')

        # Check if the query was called with the correct filters
        self.manager.session.query.assert_called_once_with(self.manager.ProductTranslation)
        self.manager.session.query.return_value.filter.assert_called_once_with(self.manager.ProductTranslation.product_reference == 'reference_product_value')

        # Check if the returned records match the dummy records
        self.assertEqual(records, dummy_records)

    def test_update_record(self):
        # Test updating a record
        # Mock the query to return a dummy record
        dummy_record = MagicMock()
        self.manager.session.query.return_value.filter_by.return_value.first.return_value = dummy_record

        # Call the method to update the record
        self.manager.update_record('reference_product_value', 'en', name='Updated Name')

        # Check if the record attributes were updated and committed
        self.assertEqual(dummy_record.name, 'Updated Name')
        self.manager.session.commit.assert_called_once()

    def test_delete_record(self):
        # Test deleting a record
        # Mock the query to return a dummy record
        dummy_record = MagicMock()
        self.manager.session.query.return_value.filter_by.return_value.first.return_value = dummy_record

        # Call the method to delete the record
        self.manager.delete_record('reference_product_value', 'en')

        # Check if the record was deleted and committed
        self.manager.session.delete.assert_called_once_with(dummy_record)
        self.manager.session.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()