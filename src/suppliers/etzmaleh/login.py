## \file hypotez/src/suppliers/etzmaleh/login.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.etzmaleh """
"""   Интерфейс авторизации. Реализация для вебдрайвера

@image html login.png
"""


from src.logger import logger
def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
  
    logger.info(f'''Залогинился ... ''')
    return Truee