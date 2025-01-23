## \file /src/suppliers/_experiments/Supplier/test_absolute_paths.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers._experiments.Supplier 
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
  
""" module: src.suppliers._experiments.Supplier """


import unittest
from pathlib import Path
from src.suppliers import Supplier

class TestSetAbsolutePaths(unittest.TestCase):
    def setUp(self):
        self.supplier_abs_path = '/path/to/supplier'
        self.function = Supplier().set_absolute_paths

    def test_single_filename_with_prefix_as_string(self):
        prefix = 'subfolder'
        related_filenames = 'file.txt'
        expected_result = Path(self.supplier_abs_path, prefix, related_filenames)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)

    def test_single_filename_with_prefix_as_list(self):
        prefix = ['subfolder', 'subsubfolder']
        related_filenames = 'file.txt'
        expected_result = Path(self.supplier_abs_path, *prefix, related_filenames)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)

    def test_multiple_filenames_with_prefix_as_string(self):
        prefix = 'subfolder'
        related_filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        expected_result = [
            Path(self.supplier_abs_path, prefix, filename)
            for filename in related_filenames
        ]

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)

    def test_multiple_filenames_with_prefix_as_list(self):
        prefix = ['subfolder', 'subsubfolder']
        related_filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        expected_result = [
            Path(self.supplier_abs_path, *prefix, filename)
            for filename in related_filenames
        ]

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)

    def test_no_related_filenames_with_prefix_as_string(self):
        prefix = 'subfolder'
        related_filenames = None
        expected_result = Path(self.supplier_abs_path, prefix)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)

    def test_no_related_filenames_with_prefix_as_list(self):
        prefix = ['subfolder', 'subsubfolder']
        related_filenames = None
        expected_result = Path(self.supplier_abs_path, *prefix)

        result = self.function(prefix, related_filenames)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

