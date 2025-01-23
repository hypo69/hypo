## \file /src/endpoints/advertisement/facebook/scenarios/switch_account.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.advertisement.facebook.scenarios 
	:platform: Windows, Unix
	:synopsis: Переключение между аккаунатми
"""


from pathlib import Path
from types import SimpleNamespace
from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns

# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)

def switch_account(driver: Driver):
    """ Если есть кнопка `Переключить` - нажимаю её  """
    driver.execute_locator(locator.switch_to_account_button)