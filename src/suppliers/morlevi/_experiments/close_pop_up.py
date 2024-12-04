## \file /src/suppliers/morlevi/_experiments/close_pop_up.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.suppliers.morlevi._experiments.close_pop_up
	:platform: Windows, Unix
	:synopsis: Проверка локатора закрытия поп-ап окна
   """
MODE = 'dev'
import header
from src import gs
from src.webdriver.driver import Driver
#from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.utils.jjson import j_loads_ns

driver = Driver(Firefox)
graber = MorleviGraber(driver)
...