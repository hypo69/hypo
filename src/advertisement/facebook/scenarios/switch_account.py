""" Переключение на аккунт. 
Если есть кнопка `Переключить` - нажимаю её """

## \file ../src/advertisement/facebook/scenarios/switch_account.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

...
from pathlib import Path

from src import gs
from src.webdriver import Driver
from src.utils import j_loads_ns

locator = j_loads_ns(Path(gs.path.src,'advertisement','facebook','locators','switch_account.json'))

def switch_account(driver: Driver):
    driver.execute_locator(locator.switch_to_account_button)