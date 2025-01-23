## \file /src/suppliers/kualastyle/login.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.kualastyle 
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
  
""" module: src.suppliers.kualastyle """



"""  Функции авторизации поставщика """

from src.logger.logger import logger

def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
    close_pop_up(s)
    return True 

def close_pop_up(s) -> bool:
    """ Функция логин
   @param
        s - Supplier
    @returns
        True if login else False

   """
    _d = s.driver
    _l : dict = s.locators['close_pop_up_locator']
    
    _d.get_url('https://www.kualastyle.com')
    _d.window_focus(_d)
    _d.wait(5)
    #_d.page_refresh()
    try:
        _d.execute_locator(_l)
    except Exception as e:
        logger.warning(f"Не закрыл попап")
    
    ...

