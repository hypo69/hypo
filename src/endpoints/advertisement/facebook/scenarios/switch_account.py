## \file hypotez/src/endpoints/advertisement/facebook/scenarios/switch_account.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.advertisement.facebook.scenarios """
MODE = 'debug'
""" module: src.endpoints.advertisement.facebook.scenarios """
MODE = 'debug'
""" Переключение на аккунт. 
Если есть кнопка `Переключить` - нажимаю её """



...
from pathlib import Path

from src import gs
from src.webdriver import Driver
from src.utils import j_loads_ns

locator = j_loads_ns(Path(gs.path.src,'advertisement','facebook','locators','switch_account.json'))

def switch_account(driver: Driver):
    driver.execute_locator(locator.switch_to_account_button)