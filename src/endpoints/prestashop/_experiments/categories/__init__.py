## \file hypotez/src/endpoints/prestashop/_experiments/categories/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.endpoints.prestashop._experiments.categories """
MODE = 'development'


"""   Модуль распределения категорий товара.  
@details Модуль переводит категории поставщика `Supplier` в категории `PrestaShop`
Изначально все категории строятся из гугл таблиц 
(https://drive.google.com/drive/folders/17qfLRWRt8X4SM-M54OJhZPTi4lIJX1pO?ths=true)
Там довольно сложная иерархия, надо исправлять
@todo Это надо переделывать СРОЧНО!


 @section libs imports:
  - src.category.category 

@file
"""


from .category import Category

