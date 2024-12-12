# Анализ кода модуля `executor.py`

**Качество кода**

8

-   Плюсы
    *   Код хорошо структурирован и разделен на функции, что облегчает понимание и поддержку.
    *   Используются `dataclass` для определения структуры данных `ExecuteLocator`.
    *   Присутствует обработка основных исключений Selenium, таких как `TimeoutException`, `NoSuchElementException`, `ElementClickInterceptedException`, `StaleElementReferenceException`.
    *   Присутствуют проверки на тип данных и корректность входных параметров.
    *   Код содержит mermaid диаграммы для визуализации логики работы функций.
    *   Используется `logger` для записи ошибок и отладочной информации.
    *   Используются асинхронные операции, что способствует повышению производительности.
-   Минусы
    *   Не все функции имеют docstring в формате RST.
    *   Иногда используется `...` как заглушка, нужно рассмотреть их удаление или реализацию.
    *   Используется `MODE`, что может быть не лучшей практикой для конфигурации.
    *   В некоторых местах есть избыточные блоки `try-except` без конкретной обработки.
    *   Не везде используется `logger.error` для логирования ошибок.
    *   Не все комментарии после `#` соответствуют требуемому стандарту.

**Рекомендации по улучшению**

1.  **Документация**:
    *   Добавить docstring в формате RST ко всем функциям и методам.
    *   Уточнить docstring, где это необходимо, добавив примеры использования и описания параметров.
2.  **Обработка ошибок**:
    *   Заменить `...` на конкретную логику или удалить, если не нужно.
    *   Использовать `logger.error` для логирования ошибок вместо `try-except` без обработки.
    *   Убрать избыточные блоки `try-except` в тех местах, где это не требуется.
3.  **Рефакторинг**:
    *   Избегать дублирования кода, где это возможно.
    *   Пересмотреть использование `MODE` и возможно заменить на переменную среды.
    *   Переименовать локальные переменные для большей ясности.
4.  **Производительность**:
    *   Оптимизировать работу с `ActionChains`, где это возможно.
5.  **Комментарии**:
    *   Переписать все комментарии после `#` в соответствии с требованиями.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с веб-элементами через Selenium.
====================================================

Этот модуль предоставляет функциональность для взаимодействия с веб-элементами,
используя Selenium WebDriver. Он включает в себя функции для поиска элементов,
выполнения действий (клики, ввод текста), получения атрибутов и захвата скриншотов.
Модуль также обрабатывает ошибки и предоставляет гибкие настройки таймаутов.

Основные возможности:
    -   Парсинг и обработка локаторов.
    -   Взаимодействие с веб-элементами: клики, ввод текста, отправка сообщений и др.
    -   Обработка ошибок: продолжение выполнения в случае ошибок.
    -   Поддержка различных типов локаторов: XPath, ID, CSS и др.

"""

MODE = 'dev'

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

import header  # type: ignore
from src import gs # type: ignore
from src.logger.logger import logger
from src.logger.exceptions import (
    DefaultSettingsException,
    ExecuteLocatorException,
    WebDriverException,
)

from src.utils.jjson import j_dumps, j_loads, j_loads_ns # type: ignore
from src.utils.printer import pprint # type: ignore
from src.utils.image import save_png # type: ignore


@dataclass
class ExecuteLocator:
    """
    Обработчик локаторов для веб-элементов с использованием Selenium.
    ===============================================================

    Этот класс предоставляет методы для поиска и взаимодействия с веб-элементами,
    используя предоставленные локаторы и действия.
    """
    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(default_factory=lambda: {
        "XPATH": By.XPATH,
        "ID": By.ID,
        "TAG_NAME": By.TAG_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "CLASS_NAME": By.CLASS_NAME,
    })
    mode: str = 'debug'

    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если драйвер передан.
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
        Выполняет действия с веб-элементом на основе предоставленного локатора.
        ===================================================================

        :param locator: Данные локатора (dict, SimpleNamespace или Locator).
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания для поиска элемента.
        :type timeout: Optional[float]
        :param timeout_for_event: Тип ожидаемого события ('presence_of_element_located', 'element_to_be_clickable').
        :type timeout_for_event: Optional[str]
        :param message: Сообщение для отправки элементу (если применимо).
        :type message: Optional[str]
        :param typing_speed: Скорость ввода текста (если применимо).
        :type typing_speed: Optional[float]
        :param continue_on_error: Продолжать ли выполнение при ошибке.
        :type continue_on_error: Optional[bool]
        :raises ExecuteLocatorException: Если произошла ошибка при выполнении локатора.
        :return: Результат выполнения операции.
        :rtype: str | list | dict | WebElement | bool
        
        ```mermaid
                graph TD
            A[Start] --> B[Check if locator is SimpleNamespace or dict]
            B --> C{Is locator SimpleNamespace?}
            C -->|Yes| D[Use locator as is]
            C -->|No| E[Convert dict to SimpleNamespace]
            E --> D
            D --> F[Define async function _parse_locator]
            F --> G[Check if locator has event, attribute, or mandatory]
            G -->|No| H[Return None]
            G -->|Yes| I[Try to map by and evaluate attribute]
            I --> J[Catch exceptions and log if needed]
            J --> K{Does locator have event?}
            K -->|Yes| L[Execute event]
            K -->|No| M{Does locator have attribute?}
            M -->|Yes| N[Get attribute by locator]
            M -->|No| O[Get web element by locator]
            L --> P[Return result of event]
            N --> P[Return attribute result]
            O --> P[Return web element result]
            P --> Q[Return final result of _parse_locator]
            Q --> R[Return result of execute_locator]
            R --> S[End]

        ```
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not locator or (not locator.attribute and not locator.selector):
            return None # <- локатор - заглушка

        async def _parse_locator(
            locator: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """
            Разбирает и выполняет инструкции локатора.

            :param locator: Данные локатора.
            :type locator: Union[dict, SimpleNamespace]
            :param message: Сообщение для отправки (если применимо).
            :type message: Optional[str]
            :return: Результат выполнения.
            :rtype: str | list | dict | WebElement | bool
            """
            locator = (
                locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
            )
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return

            try:
                locator.by = self.by_mapping.get(locator.by.upper(), locator.by)
                if locator.attribute:
                    locator.attribute = await self.evaluate_locator(locator.attribute)
            except Exception as ex:
                if MODE in ('dev','debug'):
                    logger.debug(f"Locator Error: {locator=}")
                    
                return

            if locator.event:
                return await self.execute_event(locator, timeout, timeout_for_event, message, typing_speed)
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            return await self.get_webelement_by_locator(locator, timeout, timeout_for_event)

        return await _parse_locator(locator, message)

    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Оценивает и обрабатывает атрибуты локатора.
        ===========================================

        :param attribute: Атрибуты для оценки.
        :type attribute: Union[str, List[str], dict]
        :return: Оцененные атрибуты.
        :rtype: Optional[str | List[str] | dict]
        
        ```mermaid
                graph TD
            A[Start] --> B[Check if attribute is list]
            B -->|Yes| C[Iterate over each attribute in list]
            C --> D[Call _evaluate for each attribute]
            D --> E[Return gathered results from asyncio.gather]
            B -->|No| F[Call _evaluate for single attribute]
            F --> G[Return result of _evaluate]
            G --> H[End]
            E --> H
        ```
        """
        async def _evaluate(attr: str) -> Optional[str]:
            """
            Вспомогательная функция для оценки атрибута.
            
            :param attr: Атрибут для оценки
            :type attr: str
            :return: Оцененный атрибут.
            :rtype: Optional[str]
            """
            return getattr(Keys, re.findall(r"%(\\w+)%", attr)[0], None) if re.match(r"^%\\w+%", attr) else attr

        if isinstance(attribute, list):
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(attribute)

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
        Извлекает атрибуты из элемента или списка элементов.
        ==================================================

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания элемента.
        :type timeout: float, optional
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str, optional
        :return: Значения атрибутов или словарь с атрибутами.
        :rtype: Union[str, list, dict, WebElement | list[WebElement] | None]
        
        ```mermaid
                graph TD
            A[Start] --> B[Check if locator is SimpleNamespace or dict]
            B -->|Yes| C[Convert locator to SimpleNamespace if needed]
            C --> D[Call get_webelement_by_locator]
            D --> E[Check if web_element is found]
            E -->|No| F[Log debug message and return]
            E -->|Yes| G[Check if locator.attribute is a dictionary-like string]
            G -->|Yes| H[Parse locator.attribute string to dict]
            H --> I[Check if web_element is a list]
            I -->|Yes| J[Retrieve attributes for each element in list]
            J --> K[Return list of attributes]
            I -->|No| L[Retrieve attributes for a single web_element]
            L --> K
            G -->|No| M[Check if web_element is a list]
            M -->|Yes| N[Retrieve attributes for each element in list]
            N --> O[Return list of attributes or single attribute]
            M -->|No| P[Retrieve attribute for a single web_element]
            P --> O
            O --> Q[End]
            F --> Q
        ```
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        web_element: WebElement | List[WebElement] | None = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            if MODE in ('dev','debug'):
                logger.debug(f"Не нашелся : {locator=}\\n")
            
            return

        def _parse_dict_string(attr_string: str) -> dict | None:
            """
            Разбирает строку вида '{attr1:attr2}' в словарь.

            :param attr_string: Строка, представляющая структуру словаря.
            :type attr_string: str
            :return: Разобранный словарь или None, если разбор не удался.
            :rtype: dict | None
            """
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(":") for pair in attr_string.strip("{}").split(","))
                }
            except ValueError as ex:
                if MODE in ('dev','debug'):
                    logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}\\n", exc_info=ex)
                return
            except Exception as ex:
                if MODE in ('dev','debug'):
                     logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}\\n", exc_info=ex)
                return

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """
            Извлекает значения атрибутов для каждого ключа в словаре.

            :param element: Веб-элемент для извлечения атрибутов.
            :type element: WebElement
            :param attr_dict: Словарь с именами атрибутов.
            :type attr_dict: dict
            :return: Словарь с атрибутами и их значениями.
            :rtype: dict
            """
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = web_element.get_attribute(key)
                    attr_value = web_element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.debug(
                            f"Error retrieving attributes \'{key}\' or \'{value}\' from element.", exc_info=ex)
                    
                    return
            return result

        if web_element:
            # Check if the attribute is a dictionary-like string
            if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
                attr_dict = _parse_dict_string(locator.attribute)

                if isinstance(web_element, list):
                    return [_get_attributes_from_dict(el, attr_dict) for el in web_element]
                return _get_attributes_from_dict(web_element, attr_dict)

            if isinstance(web_element, list):
                ret: list = []
                try:
                    for e in web_element:
                        ret.append(f'{e.get_attribute(locator.attribute)}')
                    return ret if len(ret) > 1 else ret[0]
                except Exception as ex:
                    if MODE in ('dev','debug'):
                         logger.debug(f"Error in get_attribute(): {pprint(locator, text_color='YELLOW', bg_color='BLACK')}\\n", exc_info=ex)
                    return

            return web_element.get_attribute(locator.attribute)
        return

    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located'
    ) -> WebElement | List[WebElement] | None:
        """
        Извлекает веб-элемент или список элементов по указанному локатору.
        ===============================================================
        
        :param locator: Локатор элемента в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания элемента.
        :type timeout: Optional[float]
        :param timeout_for_event: Тип ожидаемого события.
        :type timeout_for_event: Optional[str]
        :raises ValueError: Если локатор некорректный.
        :return: Веб-элемент или список веб-элементов, или None, если не найден.
        :rtype: WebElement | List[WebElement] | None
        """
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрует список веб-элементов по правилу `if_list`.

            :param web_elements: Список веб-элементов.
            :type web_elements: WebElement | List[WebElement]
            :param locator: Локатор элемента.
            :type locator: SimpleNamespace
            :return: Отфильтрованный список веб-элементов или веб-элемент.
            :rtype: WebElement | List[WebElement]
            """
            if not isinstance(web_elements, list):
                return web_elements

            if_list = locator.if_list

            if if_list == 'all':
                return web_elements
            elif if_list == 'first':
                return web_elements[0]
            elif if_list == 'last':
                return web_elements[-1]
            elif if_list == 'even':
                return [web_elements[i] for i in range(0, len(web_elements), 2)]
            elif if_list == 'odd':
                return [web_elements[i] for i in range(1, len(web_elements), 2)]
            elif isinstance(if_list, list):
                return [web_elements[i] for i in if_list]
            elif isinstance(if_list, int):
                return web_elements[if_list - 1]

            return web_elements

        driver = self.driver
        locator = (
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        )

        if not locator:
            raise ValueError('Некорректный локатор.')
            

        web_elements = None
        try:
            # Если timeout = 0, сразу попытаться найти элемент без ожидания
            if timeout == 0:
                web_elements = driver.find_elements(locator.by, locator.selector)
            else:
                # Выбор условия ожидания
                condition = (
                    EC.presence_of_all_elements_located
                    if timeout_for_event == 'presence_of_all_elements_located'
                    else EC.visibility_of_all_elements_located
                )

                # Ожидание элементов через блокирующий вызов в асинхронном контексте
                web_elements = await asyncio.to_thread(
                    WebDriverWait(driver, timeout).until,
                    condition((locator.by, locator.selector))
                )
            if web_elements:
                return await _parse_elements_list(web_elements, locator)
            return None

        except TimeoutException as ex:
            if MODE in ('dev', 'debug'):
                 logger.error(f'Таймаут для локатора: {locator}', exc_info=ex)
            return None
        except Exception as ex:
            if MODE in ('dev', 'debug'):
                logger.error(f'Ошибка локатора: {locator}', exc_info=ex)
            return None


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
        Создает скриншот найденного веб-элемента.
        ======================================

        :param locator: Локатор элемента.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания элемента.
        :type timeout: float, optional
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str, optional
        :param message: Сообщение для отправки (если применимо).
        :type message: Optional[str], optional
        :param typing_speed: Скорость ввода текста.
        :type typing_speed: float, optional
        :param continue_on_error: Продолжать ли при ошибке.
        :type continue_on_error: bool, optional
        :param webelement: Предварительно полученный веб-элемент.
        :type webelement: Optional[WebElement], optional
        :return: Бинарный поток скриншота или None.
        :rtype: BinaryIO | None
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event)

        if not webelement:
            return

        try:
            screenshot_stream = webelement.screenshot_as_png
            return screenshot_stream
        except Exception as ex:
            logger.error(f"Не удалось захватить скриншот", exc_info=ex)
            return

    async def execute_event(self,
                             locator: SimpleNamespace | dict,
                             timeout: float = 5,
                             timeout_for_event: str = 'presence_of_element_located',
                             message: str = None,
                             typing_speed: float = 0,
                             continue_on_error: bool = True,
    ) -> str | list[str] | bytes | list[bytes] | bool:
        """
        Выполняет события, связанные с локатором.
        =======================================

        :param locator: Локатор, определяющий элемент и событие для выполнения.
        :type locator: SimpleNamespace | dict
        :param timeout: Максимальное время ожидания элемента.
        :type timeout: float
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str
        :param message: Сообщение для отправки (если применимо).
        :type message: Optional[str], optional
        :param typing_speed: Скорость ввода текста.
        :type typing_speed: int, optional
        :return: True, если событие выполнено успешно, иначе False.
        :rtype: bool
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        events = str(locator.event).split(";")
        result: list = []
        # Retrieve the web element based on the locator
        webelement = await self.get_webelement_by_locator(
            locator,
            timeout,
            timeout_for_event
        )

        if not webelement:
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement

        for event in events:
            if event == "click()":
                try:
                    webelement.click()
                    continue
                except ElementClickInterceptedException as ex:
                    if MODE in ('dev','debug'):
                         logger.error(f"Element click intercepted:  {locator=}\\n", exc_info=ex)
                    return False
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Element click intercepted: {locator=}\\n", exc_info=ex)
                    return False

            elif event.startswith("pause("):
                match = re.match(r"pause\\((\\d+)\\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                if MODE in ('dev','debug'):
                     logger.debug(f"Должна быть пауза, но что-то не срослось: {locator=}\\n")
                return False

            elif event == "upload_media()":
                if not message:
                    if MODE in ('dev','debug'):
                        logger.debug(f"Message is required for upload_media event. Message: {pprint(message, text_color='WHITE',bg_color='RED')}")
                    return False
                try:
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.debug(f"Error uploading media: {message=}", exc_info=ex)
                    return False

            elif event == "screenshot()":
                try:
                    result.append(await self.get_webelement_as_screenshot(locator, webelement=webelement))
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Error taking screenshot: {locator=}", exc_info=ex)
                    return False

            elif event == "clear()":
                try:
                    await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Error clearing element: {locator=}", exc_info=ex)
                    return False

            elif event.startswith("send_keys("):
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                    actions = ActionChains(self.driver)
                    for key in keys_to_send:
                        key = key.strip().strip("\'")
                        if hasattr(Keys, key):
                            key_to_send = getattr(Keys, key)
                            actions.send_keys(key_to_send)
                    await asyncio.to_thread(actions.perform)
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Error sending keys: {locator=}", exc_info=ex)
                    return False

            elif event.startswith("type("):
                message = event.replace("type(", "").replace(")", "")
                if typing_speed:
                    for character in message:
                        await asyncio.to_thread(webelement.send_keys, character)
                        await asyncio.sleep(typing_speed)
                else:
                    await asyncio.to_thread(webelement.send_keys, message)

        return result if result else True

    async def send_message(self,
                        locator: SimpleNamespace | dict,
                        timeout:float = 5 ,
                        timeout_for_event: str = 'presence_of_element_located',
                        message: str = None,
                        typing_speed: float = 0,
                        continue_on_error: bool = True,

    ) -> bool:
        """
        Отправляет сообщение веб-элементу.
        =================================
        
        :param locator: Локатор элемента.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания элемента.
        :type timeout: float, optional
        :param timeout_for_event: Тип ожидаемого события.
        :type timeout_for_event: str, optional
        :param message: Сообщение для отправки.
        :type message: Optional[str], optional
        :param typing_speed: Скорость ввода текста.
        :type typing_speed: float, optional
        :return: True, если сообщение отправлено успешно, иначе False.
        :rtype: bool
        
        Пример использования::
        
            >>> driver = Driver()
            >>> driver.send_message(locator={"id": "messageBox"}, message="Hello World", typing_speed=0.1)
            True
       
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(locator)
        )

        def type_message(
            el: WebElement,
            message: str,
            replace_dict: dict = {";":"SHIFT+ENTER"},
            typing_speed: float = typing_speed,
        ) -> bool:
            """
            Вводит сообщение в веб-элемент с заданной скоростью.

            :param el: Веб-элемент.
            :type el: WebElement
            :param message: Сообщение для ввода.
            :type message: str
            :param replace_dict: Словарь для замены символов.
            :type replace_dict: dict, optional
            :param typing_speed: Скорость ввода.
            :type typing_speed: float, optional
            :return: True, если сообщение введено успешно, иначе False.
            :rtype: bool
            
            Пример использования::

                >>> element = driver.get_element_by_id("messageBox")
                >>> driver.type_message(el=element, message="Hello World", typing_speed=0.1)
                True
            """
            message = message.split(" ")

            for word in message:
                word += " "
                try:
                    for letter in word:
                        if letter in replace_dict.keys():
                            self.actions.key_down(Keys.SHIFT).send_keys(
                                Keys.ENTER
                            ).key_up(Keys.SHIFT)
                        else:
                            self.actions.send_keys(letter)
                            self.actions.pause(typing_speed)
                            self.actions.perform()
                except Exception as ex:
                    if MODE in ('dev','debug'):
                         logger.error(f"Error typing message\\n{message=}\\n{word=}\\n{letter=}\\n", exc_info=ex)
                    continue  # <- если была ошибка в передаче буквы - пока игнорую ёё
            return True


        webelement = await self.get_webelement_by_locator(locator = locator, timeout =  timeout, timeout_for_event = timeout_for_event)
        if not webelement or (isinstance(webelement, list) and len(webelement) == 0):
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement
        self.actions.move_to_element(webelement)
        type_message(
            el=webelement,
            message=message,
            replace_dict={";":"SHIFT+ENTER"},
            typing_speed=typing_speed,
        )
        return True
```