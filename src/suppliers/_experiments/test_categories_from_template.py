## \file /src/suppliers/_experiments/test_categories_from_template.py
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


""" класс проверки создания шаблонов категорий.
@deprecated Это какая-то старая версия. Сейчас в файле сценария записана дефолтная категория
собираемого товара. От нее строится дерево вверх. при необходимости в сценарии можно
прописать и дополнительные категории и при желании восстановиуть их иеархию """

import unittest
import tempfile
import os


class TestBuildtemplates(unittest.TestCase):
    def test_build_templates_with_existing_directory(self):
        # Create a temporary directory and add some JSON files
        with tempfile.TemporaryDirectory() as tmpdir:
            json_data = '{"category1": {"template1": "some content"}, "category2": {"template2": "some content"}}'
            file1_path = os.path.join(tmpdir, 'file1.json')
            with open(file1_path, 'w') as f:
                f.write(json_data)
            file2_path = os.path.join(tmpdir, 'subdir', 'file2.json')
            os.makedirs(os.path.dirname(file2_path))
            with open(file2_path, 'w') as f:
                f.write(json_data)

            # Call the function and check the output
            expected_output = {"category1": {
                "template1": "some content"}, "category2": {"template2": "some content"}}
            self.assertEqual(buid_templates(tmpdir), expected_output)

    def test_build_templates_with_non_existing_directory(self):
        # Call the function with a non-existing directory and check that it raises an exception
        with self.assertRaises(FileNotFoundError):
            buid_templates('/non/existing/path/')

