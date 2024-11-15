## \file hypotez/src/suppliers/aliexpress/scenarios/version.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress.scenarios """
MODE = 'debug'
""" module: src.suppliers.aliexpress.scenarios """
MODE = 'debug'

"""
- `__version__`: This variable holds the version of the module or package.
- `__name__`: Contains the name of the module. If the script is being run directly, the value will be `"__main__"`.
- `__doc__`: The module's documentation string.
- `__details__`: This variable likely contains additional details about the module, but the exact purpose depends on the specific module or package.
- `__annotations__`: Contains type annotations for variables and functions in the module.
- `__author__`: The name(s) of the author(s) of the module.
"""
__name__:str
__version__="3.12.0.0.0.4"
__doc__:str

__details__:str=f""" У меня есть несколько путей получения товаров:
       - `page by page` когда запускается сценарий на выполнение и програма обходит страницы сайта одну за другой
       - парсинг файла excel, который я собираю в личном кабинете affiliate trading
       - парсинг почтовой рассылки """

__annotations__

__author__='hypotez '

