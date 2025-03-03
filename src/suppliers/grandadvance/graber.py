## \file /src/suppliers/grandadvance/graber.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.grandadvance 
	:platform: Windows, Unix
	:synopsis: Класс собирает значение полей на странице  товара `grandadvanse.co.il`. 
    Для каждого поля страницы товара сделана функция обработки поля в родительском классе.
    Если нужна нестандертная обработка, функция перегружается в этом классе.
    ------------------
    Перед отправкой запроса к вебдрайверу можно совершить предварительные действия через декоратор. 
    Декоратор по умолчанию находится в родительском классе. Для того, чтобы декоратор сработал надо передать значение 
    в `Context.locator`, Если надо реализовать свой декоратор - раскоментируйте строки с декоратором и переопределите его поведение


"""


from typing import Any
import header
from header import __root__
from src import gs
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from types import SimpleNamespace
from src.logger.logger import logger

#############################################################

ENDPOINT = 'grandadvance'

#############################################################

class Graber(Grbr):
    """Класс населедутет Graber. 
    все поля 
    товара устана
   вливвв модуле `src.supplier."""

    def __init__(self, driver: Driver, lang_index:int):
        config:SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / ENDPOINT / f'{ENDPOINT}.json')
        locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / ENDPOINT / 'locators' / 'product.json')
        super().__init__(supplier_prefix=ENDPOINT, driver=driver, lang_index=lang_index)
        Context.locator_for_decorator = locator.click_to_specifications # <- if locator not definded decorator 

