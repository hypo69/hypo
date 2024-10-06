## \file src/suppliers/grandadvance/__grandadvance__.py
"""   [File's Description]

@namespace src: src
 \package src.suppliers.grandadvance
\file __grandadvance__.py
 
 @section libs imports:
  - gs 
  - gs 
  - suppliers.Product 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""
## \file ../src/suppliers/grandadvance/__grandadvance__.py
# -*- coding: utf-8 -*-
#
# \package hypotez.suppliers.grandadvance

import settings 
from src.settings import StringFormatter
json_loads = settinsettings.json_loads
logger = settings.logger
from src.suppliers.Product import Product 

# Documentation for this module
def login(supplier):

    _s = supplier
    _l = supplier.locators['login']
    _d = supplier.driver

    _d.get_url(_s.settings['login_url'])
    logger.info(f"Залогиниваюсь")
    email = _l['email']
    password = _l['password']

    open_login_dialog_locator =_l['open_login_dialog_locator']
    email_locator = _l['email_selector']
    password_locator = _l['password_locator']
    loginbutton_locator =  _l['loginbutton_locator']


    elements = _d.execute_locator(open_login_dialog_locator)
    ''' получаю див с кнопками Логин и Регистер
    мне нужна первая'''
    elements[0].click()


    _d.execute_locator(email_locator).send_keys(email)
    _d.execute_locator(password_locator).send_keys(password)
    _d.wait(1)
    elements = _d.execute_locator(loginbutton_locator)
    ''' получаю див с кнопками Отмена и Войти
    мне нужна вторая'''
    elements[1].click()
    logger.info('Гранд logged in')
    return True


def update_categories_in_scenario_file(supplier,current_scenario_filename):
    return Truee