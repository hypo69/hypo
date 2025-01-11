### Анализ кода модуля `executor`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код разбит на функции, что улучшает читаемость и поддерживает модульность.
    - Используется `dataclass` для `ExecuteLocator`, что упрощает создание экземпляров и управление атрибутами.
    - Присутствует асинхронность, что позволяет выполнять неблокирующие операции.
    - Присутствует документация для функций, хоть и требует доработки.
    - Использование `SimpleNamespace` для хранения данных локаторов.
- **Минусы**:
    - Смешанное использование одинарных и двойных кавычек.
    - Отсутствует подробная RST-документация в некоторых местах.
    - Чрезмерное использование `try-except` блоков с `...`.
    - Смешанное использование `logger.error` и `logger.debug` без явного разграничения по уровню критичности ошибки.
    - Некоторые функции имеют слишком много параметров.
    - Непоследовательное использование `asyncio.to_thread`.
    - В некоторых местах отсутствует обработка ошибок.
    - Не все функции имеют docstring.

**Рекомендации по улучшению**:
1.  **Форматирование**:
    - Применить одинарные кавычки для всех строковых литералов в коде, кроме `print`, `input` и логгирования.
2.  **Документация**:
    - Добавить подробные RST-комментарии для всех функций, методов и классов.
    - Улучшить существующие комментарии, сделав их более информативными и точными.
3.  **Обработка ошибок**:
    - Избегать использования `...` в блоках `except`. Вместо этого, явно обрабатывать исключения через `logger.error` и возвращать `None` или `False` в случае ошибки.
    - Уточнить, какие исключения могут возникать в каждом блоке `try-except` и обрабатывать их соответствующим образом.
    - Использовать `logger.error` для критических ошибок, `logger.debug` для информационных сообщений, и `logger.info` для отслеживания хода выполнения.
4.  **Импорты**:
    -  Импортировать `logger` из `src.logger.logger`.
5.  **Структура кода**:
    - Переименовать локальную переменную `locator` в `loc` внутри функции `_parse_locator`, для избежания коллизии имен.
    - Упростить логику в `_parse_elements_list` и сделать её более читаемой.
    - Избегать дублирования кода (например, в блоке `if web_element:` в `get_attribute_by_locator`).
6. **Рефакторинг**:
    - Рассмотреть возможность объединения некоторых функций, чтобы уменьшить количество параметров и сложность (например `get_webelement_by_locator` и `_parse_elements_list`).
    - Оптимизировать использование асинхронных операций и `asyncio.to_thread`, использовать их там, где это действительно необходимо.
    - Упростить логику `send_message`, убрав лишние уровни вложенности и вызовы `self.actions.perform()`.
7.  **Улучшения**:
    - Добавить проверку на наличие `locator.by` и `locator.selector` перед использованием.
    - Использовать `logger.info` для информационных сообщений, таких как начало и конец выполнения функции.
    - Добавить описание `__post_init__` метода.

**Оптимизированный код**:
```python
## \file /src/webdriver/executor.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для выполнения действий с веб-элементами
==============================================

Модуль `executor` предназначен для выполнения действий с веб-элементами на основе предоставленных конфигураций,
известных как "локаторы". Эти конфигурации (или "локаторы") представляют собой словари, содержащие информацию о том,
как находить и взаимодействовать с элементами на веб-странице. Модуль предоставляет следующие возможности:

1. **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что обеспечивает
   гибкое манипулирование данными локаторов.

2. **Взаимодействие с веб-элементами**: В зависимости от предоставленных данных, модуль может выполнять различные действия,
   такие как клики, отправка сообщений, выполнение событий и извлечение атрибутов из веб-элементов.

3. **Обработка ошибок**: Модуль поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы,
   которые могут иметь нестабильные элементы или требовать особого подхода.

4. **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, что позволяет
   идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

Модуль обеспечивает гибкость и универсальность в работе с веб-элементами, позволяя автоматизировать сложные сценарии
взаимодействия с веб-страницами.
"""

import asyncio
import re
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import BinaryIO, ByteString, Dict, List, Optional, Union

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    JavascriptException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import header
from src import gs
from src.logger.logger import logger
from src.logger.exceptions import (
    DefaultSettingsException,
    ExecuteLocatorException,
    WebDriverException,
)

from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint
from src.utils.image import save_image


@dataclass
class ExecuteLocator:
    """
    Класс для управления локаторами веб-элементов с использованием Selenium.

    :param driver: Опциональный объект веб-драйвера Selenium.
    :type driver: Optional[object]
    :param actions: Объект ActionChains для выполнения сложных действий с элементами.
    :type actions: ActionChains
    :param by_mapping: Словарь, связывающий строковые идентификаторы с методами поиска элементов Selenium.
    :type by_mapping: dict
    :param mode: Режим работы (например, 'debug').
    :type mode: str
    """
    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(default_factory=lambda: {
        'XPATH': By.XPATH,
        'ID': By.ID,
        'TAG_NAME': By.TAG_NAME,
        'CSS_SELECTOR': By.CSS_SELECTOR,
        'NAME': By.NAME,
        'LINK_TEXT': By.LINK_TEXT,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'CLASS_NAME': By.CLASS_NAME,
    })
    mode: str = 'debug'

    def __post_init__(self):
        """
        Инициализирует объект ActionChains после создания экземпляра класса,
        если передан драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)


    async def execute_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: Optional[float] = 0,
        continue_on_error: Optional[bool] = True,
    ) -> str | list | dict | WebElement | bool:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        :param locator: Данные локатора (словарь, SimpleNamespace или Locator).
        :type locator: dict | SimpleNamespace
        :param timeout: Время ожидания для поиска элемента.
        :type timeout: Optional[float], optional
        :param timeout_for_event: Условие ожидания ('presence_of_element_located', 'element_to_be_clickable').
        :type timeout_for_event: Optional[str], optional
        :param message: Опциональное сообщение для отправки.
        :type message: Optional[str], optional
        :param typing_speed: Скорость набора текста для событий send_keys.
        :type typing_speed: Optional[float], optional
        :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение при ошибке.
        :type continue_on_error: Optional[bool], optional
        :return: Результат выполнения на основе инструкций локатора.
        :rtype: str | list | dict | WebElement | bool

        ```mermaid
                graph TD
            A[Начало] --> B[Проверка типа локатора]\
            B --> C{Локатор SimpleNamespace?}\
            C -->|Да| D[Использовать локатор]\
            C -->|Нет| E[Преобразовать словарь в SimpleNamespace]\
            E --> D\
            D --> F[Определение _parse_locator]\
            F --> G[Проверка наличия event, attribute, mandatory]\
            G -->|Нет| H[Возврат None]\
            G -->|Да| I[Попытка сопоставить by и вычислить атрибут]\
            I --> J[Перехват исключений и лог]\
            J --> K{Локатор имеет event?}\
            K -->|Да| L[Выполнение события]\
            K -->|Нет| M{Локатор имеет attribute?}\
            M -->|Да| N[Получение атрибута по локатору]\
            M -->|Нет| O[Получение веб-элемента по локатору]\
            L --> P[Возврат результата события]\
            N --> P[Возврат результата атрибута]\
            O --> P[Возврат веб-элемента]\
            P --> Q[Возврат результата _parse_locator]\
            Q --> R[Возврат результата execute_locator]\
            R --> S[Конец]
        ```
        """
        loc = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        if not loc.attribute and not loc.selector: # проверка наличия аттрибута или селектора
            return None # если ни того, ни другого нет, то это заглушка

        async def _parse_locator(
            loc: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """
            Разбирает и выполняет инструкции локатора.

            :param loc: Данные локатора.
            :type loc: Union[dict, SimpleNamespace]
            :param message: Сообщение для отправки, если применимо.
            :type message: Optional[str], optional
            :return: Результат выполнения.
            :rtype: Union[str, list, dict, WebElement, bool]
            """
            loc = (
                loc if isinstance(loc, SimpleNamespace) else SimpleNamespace(**loc) # приводим к SimpleNamespace
            )
            if all([loc.event, loc.attribute, loc.mandatory]) is None: # если нет event, attribute или mandatory
                return # возвращаем None

            try: # оборачиваем в try/except
                loc.by = self.by_mapping.get(loc.by.upper(), loc.by) # получаем значение по ключу, если такого ключа нет - возвращаем исходное
                if loc.attribute: # если есть атрибут
                    loc.attribute = await self.evaluate_locator(loc.attribute) # вычисляем его
                    if loc.by == 'VALUE': # если значение = VALUE, то сразу отдаём его
                        return loc.attribute # возвращаем значение
            except Exception as ex: # перехват ошибки
                logger.debug(f"Ошибка локатора: {loc=}", exc_info=True) # логгируем ошибку
                return # возвращаем None

            if loc.event: # если есть событие
                return await self.execute_event(loc, timeout, timeout_for_event, message, typing_speed) # запускаем событие
            if loc.attribute: # если есть атрибут
                return await self.get_attribute_by_locator(loc) # возвращаем атрибут
            return await self.get_webelement_by_locator(loc, timeout, timeout_for_event) # возвращаем элемент

        return await _parse_locator(loc, message) # возвращаем результат работы


    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Вычисляет и обрабатывает атрибуты локатора.

        :param attribute: Атрибуты для вычисления.
        :type attribute: Union[str, List[str], dict]
        :return: Вычисленные атрибуты.
        :rtype: Optional[str | List[str] | dict]

        ```mermaid
                graph TD
            A[Начало] --> B[Проверка списка атрибутов]\
            B -->|Да| C[Перебор каждого атрибута в списке]\
            C --> D[Вызов _evaluate для каждого атрибута]\
            D --> E[Возврат результатов asyncio.gather]\
            B -->|Нет| F[Вызов _evaluate для одного атрибута]\
            F --> G[Возврат результата _evaluate]\
            G --> H[Конец]\
            E --> H
            ```
        """
        async def _evaluate(attr: str) -> Optional[str]:
            """
            Вычисляет одиночный атрибут.
            
            :param attr: Атрибут для вычисления.
            :type attr: str
            :return: Вычисленный атрибут.
            :rtype: Optional[str]
            """
            if re.match(r"^%\\w+%", attr): # проверяем на наличие макроса
                match = re.findall(r"%(\\w+)%", attr)[0] # извлекаем его
                return getattr(Keys, match, None) # получаем значение из Keys или None
            return attr # если не макрос, возвращаем как есть

        if isinstance(attribute, list): # если это список
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute]) # возвращаем список вычисленных значений
        return await _evaluate(str(attribute)) # возвращаем вычисленное значение


    async def get_attribute_by_locator(
        self,
        locator: SimpleNamespace | dict,
        timeout: Optional[float] = 0,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
    ) ->  WebElement | list[WebElement] | None:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания появления элемента.
        :type timeout: float, optional
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str, optional
        :return: Значение атрибута(ов) или словарь с атрибутами.
        :rtype:  WebElement | list[WebElement] | None

        ```mermaid
                graph TD
            A[Начало] --> B[Проверка типа локатора]\
            B -->|Да| C[Преобразование в SimpleNamespace]\
            C --> D[Вызов get_webelement_by_locator]\
            D --> E[Проверка наличия элемента]\
            E -->|Нет| F[Лог и возврат]\
            E -->|Да| G[Проверка атрибута на словарь]\
            G -->|Да| H[Разбор атрибута в словарь]\
            H --> I[Проверка, является ли элемент списком]\
            I -->|Да| J[Получение атрибутов для каждого элемента]\
            J --> K[Возврат списка атрибутов]\
            I -->|Нет| L[Получение атрибута для одного элемента]\
            L --> K\
            G -->|Нет| M[Проверка, является ли элемент списком]\
            M -->|Да| N[Получение атрибутов для каждого элемента]\
            N --> O[Возврат списка атрибутов или атрибута]\
            M -->|Нет| P[Получение атрибута для одного элемента]\
            P --> O\
            O --> Q[Конец]\
            F --> Q
        ```
        """
        loc = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        web_element = await self.get_webelement_by_locator(loc, timeout, timeout_for_event) # получаем веб-элемент по локатору
        if not web_element: # если элемента нет
            logger.debug(f'Элемент не найден: {loc=}') # лог
            return # выходим

        def _parse_dict_string(attr_string: str) -> dict | None:
            """
            Преобразует строку вида '{attr1:attr2}' в словарь.

            :param attr_string: Строка, представляющая структуру, похожую на словарь.
            :type attr_string: str
            :return: Разобранный словарь или None, если разбор не удался.
            :rtype: dict | None
            """
            try: # оборачиваем в try/except
                return {
                    k.strip(): v.strip() # удаляем пробелы и возвращаем словарь
                    for k, v in (pair.split(':') for pair in attr_string.strip('{}').split(',')) # парсим строку
                }
            except ValueError as ex: # ловим ошибку
                logger.error(f'Неверный формат строки атрибута: {pprint(attr_string, text_color="WHITE", bg_color="RED")}', exc_info=True) # логгируем ошибку
                return # выходим

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """
            Извлекает значения атрибутов для каждого ключа в заданном словаре.

            :param web_element: Веб-элемент, из которого нужно получить атрибуты.
            :type web_element: WebElement
            :param attr_dict: Словарь, где ключи и значения - это названия атрибутов.
            :type attr_dict: dict
            :return: Словарь с атрибутами и их значениями.
            :rtype: dict
            """
            result = {} # инициализируем результирующий словарь
            for key, value in attr_dict.items(): # проходим по атрибутам
                try: # оборачиваем в try/except
                    attr_key = web_element.get_attribute(key) # получаем атрибут по ключу
                    attr_value = web_element.get_attribute(value) # получаем атрибут по значению
                    result[attr_key] = attr_value # записываем в словарь
                except Exception as ex: # ловим ошибку
                    logger.error(f"Ошибка при извлечении атрибутов '{key}' или '{value}' из элемента.", exc_info=True) # логгируем ошибку
                    return # выходим
            return result # возвращаем результат

        if web_element: # если элемент найден
            if isinstance(loc.attribute, str) and loc.attribute.startswith('{'): # если это строка, и она начинается с {
                attr_dict = _parse_dict_string(loc.attribute) # парсим строку в словарь

                if isinstance(web_element, list): # если это список
                    return [_get_attributes_from_dict(el, attr_dict) for el in web_element] # проходим по каждому элементу и получаем атрибуты
                return _get_attributes_from_dict(web_element, attr_dict) # если не список, получаем атрибуты

            if isinstance(web_element, list): # если это список элементов
                ret: list = [] # создаем пустой список
                try: # оборачиваем в try/except
                    for e in web_element: # проходим по элементам
                        ret.append(f'{e.get_attribute(loc.attribute)}') # записываем атрибут в список
                    return ret if len(ret) > 1 else ret[0] # возвращаем список или один элемент
                except Exception as ex: # ловим ошибку
                    logger.error(f'Ошибка в get_attribute(): {pprint(loc, text_color="YELLOW", bg_color="BLACK")}', exc_info=True) # логгируем ошибку
                    return # выходим
            return web_element.get_attribute(loc.attribute) # если не список, возвращаем атрибут
        return # если нет элемента - возвращаем None


    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located'
    ) -> WebElement | List[WebElement] | None:
        """
        Извлекает веб-элемент или список элементов по указанному локатору.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Время ожидания элемента.
        :type timeout: Optional[float], optional
        :param timeout_for_event: Условие ожидания элемента.
        :type timeout_for_event: Optional[str], optional
        :return: Веб-элемент или список элементов или None, если элемент не найден.
        :rtype: WebElement | List[WebElement] | None
        """
        timeout = timeout if timeout > 0 else locator.timeout # присваиваем timeout, если он больше 0

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрует список веб-элементов на основе условия в `locator.if_list`.

            :param web_elements: Веб-элемент или список веб-элементов.
            :type web_elements: WebElement | List[WebElement]
            :param locator: SimpleNamespace с данными локатора.
            :type locator: SimpleNamespace
            :return: Отфильтрованный веб-элемент или список веб-элементов.
            :rtype: WebElement | List[WebElement]
            """
            if not isinstance(web_elements, list): # если это не список
                return web_elements # возвращаем как есть

            if_list = locator.if_list # получаем значение if_list

            if if_list == 'all': # возвращаем все элементы
                return web_elements
            elif if_list == 'first': # возвращаем первый элемент
                return web_elements[0]
            elif if_list == 'last': # возвращаем последний элемент
                return web_elements[-1]
            elif if_list == 'even': # возвращаем четные элементы
                return [web_elements[i] for i in range(0, len(web_elements), 2)]
            elif if_list == 'odd': # возвращаем нечетные элементы
                return [web_elements[i] for i in range(1, len(web_elements), 2)]
            elif isinstance(if_list, list): # возвращаем элементы по индексам
                return [web_elements[i] for i in if_list]
            elif isinstance(if_list, int): # возвращаем один элемент по индексу
                return web_elements[if_list - 1]

            return web_elements # возвращаем все элементы, если if_list не подходит


        driver = self.driver # получаем драйвер
        loc = (
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        ) # приводим к SimpleNamespace, если это словарь

        if not loc: # проверка на наличие loc
            logger.error('Локатор не передан') # лог
            raise ValueError('Некорректный локатор.') # выкидываем ошибку

        web_elements = None # инициализируем переменную web_elements
        try: # оборачиваем в try/except
            if timeout == 0: # если timeout = 0
                web_elements = await asyncio.to_thread( # выполняем в потоке
                    driver.find_elements, loc.by, loc.selector # ищем элементы
                )
            else: # если timeout > 0
                condition = (
                    EC.presence_of_all_elements_located
                    if timeout_for_event == 'presence_of_all_elements_located'
                    else EC.visibility_of_all_elements_located # выбираем условие
                )

                web_elements = await asyncio.to_thread( # выполняем в потоке
                    WebDriverWait(driver, timeout).until, # ждем пока элементы появятся
                    condition((loc.by, loc.selector)) # условие поиска
                )

            return await _parse_elements_list(web_elements, loc) # фильтруем и возвращаем список элементов
        except TimeoutException as ex: # ловим timeout
            logger.error(f'Таймаут при поиске локатора: {loc}', exc_info=True) # логгируем
            return None # возвращаем None
        except Exception as ex: # ловим ошибку
            logger.error(f'Ошибка при поиске локатора: {loc}', exc_info=True) # логгируем
            return None # возвращаем None

    async def get_webelement_as_screenshot(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
        webelement: Optional[WebElement] = None
    ) -> BinaryIO | None:
        """
        Делает скриншот найденного веб-элемента.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания появления элемента.
        :type timeout: float, optional
        :param timeout_for_event: Тип условия ожидания элемента.
        :type timeout_for_event: str, optional
        :param message: Сообщение для отправки.
        :type message: Optional[str], optional
        :param typing_speed: Скорость набора текста.
        :type typing_speed: float, optional
        :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение при ошибке.
        :type continue_on_error: bool, optional
        :param webelement: Предварительно полученный веб-элемент.
        :type webelement: Optional[WebElement], optional
        :return: Бинарный поток скриншота или None, если произошла ошибка.
        :rtype: BinaryIO | None
        """
        loc = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        if not webelement: # если элемента нет
            webelement = await self.get_webelement_by_locator(locator = loc, timeout = timeout, timeout_for_event = timeout_for_event) # получаем элемент

        if not webelement: # если элемента нет
            return # возвращаем None

        try: # оборачиваем в try/except
            screenshot_stream = webelement.screenshot_as_png # делаем скриншот
            return screenshot_stream # возвращаем
        except Exception as ex: # ловим ошибку
            logger.error('Не удалось захватить скриншот', exc_info=True) # логгируем ошибку
            return # возвращаем None


    async def execute_event(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: str = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
    ) -> str | list[str] | bytes | list[bytes] | bool:
        """
        Выполняет события, связанные с локатором.

        :param locator: Локатор, определяющий элемент и событие для выполнения.
        :type locator: SimpleNamespace | dict
        :param timeout: Время ожидания поиска элемента.
        :type timeout: float, optional
        :param timeout_for_event: Время ожидания события.
        :type timeout_for_event: str, optional
        :param message: Сообщение для отправки с событием.
        :type message: Optional[str], optional
        :param typing_speed: Скорость набора текста для событий send_keys.
        :type typing_speed: int, optional
        :return: True, если событие выполнено успешно, False в противном случае.
        :rtype: str | list[str] | bytes | list[bytes] | bool
        """
        loc = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )
        events = str(loc.event).split(';') # получаем список событий
        result: list = [] # инициализируем список результатов

        web_element = await self.get_webelement_by_locator( # получаем элемент
            loc,
            timeout,
            timeout_for_event
        )
        if not web_element: # если элемента нет
            return False # возвращаем False
        web_element = web_element[0] if isinstance(web_element, list) else web_element # получаем элемент из списка, если он есть

        for event in events: # проходимся по событиям
            if event == 'click()': # если это click()
                try: # оборачиваем в try/except
                    web_element.click() # выполняем клик
                    continue # переходим к следующему событию
                except ElementClickInterceptedException as ex: # ловим ошибку
                    logger.error(f'Перехват клика элемента: {loc=}', exc_info=True) # логгируем
                    return # возвращаем None
                except Exception as ex: # ловим ошибку
                    logger.error(f'Ошибка при клике элемента: {loc=}', exc_info=True) # логгируем
                    return # возвращаем None

            elif event.startswith('pause('): # если это пауза
                match = re.match(r'pause\\((\\d+)\\)', event) # извлекаем время паузы
                if match: # если совпадение есть
                    pause_duration = int(match.group(1)) # получаем время паузы
                    await asyncio.sleep(pause_duration) # ждем
                    result.append(True) # записываем результат
                    continue # переходим к следующему событию
                logger.debug(f'Должна быть пауза, но что-то не срослось: {loc=}') # лог
                return False # возвращаем False

            elif event == 'upload_media()': # если это загрузка файла
                if not message: # если нет сообщения
                    logger.debug(f'Сообщение обязательно для события upload_media. Сообщение: {pprint(message, text_color="WHITE",bg_color="RED")}') # лог
                    return False # возвращаем False
                try: # оборачиваем в try/except
                    await asyncio.to_thread(web_element.send_keys, message) # отправляем путь к файлу
                    result.append(True) # записываем результат
                    continue # переходим к следующему событию
                except Exception as ex: # ловим ошибку
                    logger.error(f'Ошибка загрузки медиа: {message=}', exc_info=True) # логгируем
                    return False # возвращаем False

            elif event == 'screenshot()': # если это скриншот
                try: # оборачиваем в try/except
                    result.append(await self.get_webelement_as_screenshot(loc, webelement=web_element)) # делаем скриншот
                except Exception as ex: # ловим ошибку
                    logger.error(f'Ошибка при создании скриншота: {loc=}', exc_info=True) # логгируем
                    return False # возвращаем False

            elif event == 'clear()': # если это очистка поля
                try: # оборачиваем в try/except
                   await asyncio.to_thread(web_element.clear)  # очищаем поле
                except Exception as ex: # ловим ошибку
                    logger.error(f'Ошибка при очистке элемента: {loc=}', exc_info=True) # логгируем
                    return False # возвращаем False

            elif event.startswith('send_keys('): # если это отправка клавиш
                keys_to_send = event.replace('send_keys(', '').replace(')', '').split('+') # извлекаем клавиши
                try: # оборачиваем в try/except
                    actions = ActionChains(self.driver) # создаем цепочку действий
                    for key in keys_to_send: # проходимся по клавишам
                        key = key.strip().strip('\'') # очищаем клавишу от пробелов и кавычек
                        if hasattr(Keys, key): # если есть клавиша в Keys
                            key_to_send = getattr(Keys, key) # получаем значение клавиши
                            actions.send_keys(key_to_send) # отправляем клавишу
                    await asyncio.to_thread(actions.perform) # выполняем действия
                except Exception as ex: # ловим ошибку
                    logger.error(f'Ошибка при отправке клавиш: {loc=}', exc_info=True) # логгируем
                    return False # возвращаем False

            elif event.startswith('type('): # если это ввод текста
                message = event.replace('type(', '').replace(')', '') # получаем текст
                if typing_speed: # если есть скорость печати
                    for character in message: # проходимся по символам
                        await asyncio.to_thread(web_element.send_keys, character) # отправляем символ
                        await asyncio.sleep(typing_speed) # ждем