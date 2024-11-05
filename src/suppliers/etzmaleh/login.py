#! /usr/bin/python
﻿## \file src/suppliers/etzmaleh/login.py
"""   Интерфейс авторизации. Реализация для вебдрайвера

@image html login.png
"""
## \file /src/suppliers/etzmaleh/login.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

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