## \file /src/suppliers/wallashop/graber.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.wallashop 
	:platform: Windows, Unix
	:synopsis: Класс собирает значение полей на странице  товара `wallashop.co.il`. 
    Для каждого поля страницы товара сделана функция обработки поля в родительском классе.
    Если нужна нестандертная обработка, функция перегружается в этом классе.
    ------------------
    Перед отправкой запроса к вебдрайверу можно совершить предварительные действия через декоратор. 
    Декоратор по умолчанию находится в родительском классе. Для того, чтобы декоратор сработал надо передать значение 
    в `Context.locator`, Если надо реализовать свой декоратор - раскоментируйте строки с декоратором и переопределите его поведение


"""


from typing import Any
import header
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up
from src.webdriver.driver import Driver
from src.logger.logger import logger



class Graber(Grbr):
    """Класс для операций захвата Wallashop."""
    supplier_prefix: str

    def __init__(self, driver: Driver, lang_index:int):
        """Инициализация класса сбора полей товара."""
        self.supplier_prefix = 'wallashop'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

        # Закрыватель поп ап `@close_pop_up`
        Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`

        
