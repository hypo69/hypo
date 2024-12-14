## Анализ кода модуля `executor.py`

**Качество кода**
8
-  Плюсы
        - Код хорошо структурирован с использованием классов и функций.
        - Присутствует обработка исключений, что делает код более устойчивым.
        - Используются асинхронные операции, что повышает производительность.
        - Есть  документация в виде docstring для большинства методов и классов.
        - Код использует `logger` для логирования, что облегчает отладку.
        - Активно используется `SimpleNamespace` для работы с конфигурациями, что удобно.
-  Минусы
    -  Не все функции и методы имеют docstring, а некоторые требуют доработки.
    -  В некоторых местах используется `...` как заглушка, что нужно убрать или конкретизировать.
    -  Не везде используется `logger.error` для обработки исключений, иногда `try-except` без `logger`
    -  В некоторых местах код мог бы быть более читабельным, например, вынесением повторяющихся блоков в отдельные функции.
    -  Обработка ошибок не всегда последовательная, где-то логируется, а где-то просто пропускается.
    -  Не все комментарии соответствуют формату reStructuredText.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Заполнить отсутствующие docstring для всех функций, методов и классов, используя reStructuredText формат.
    -   Уточнить и дополнить существующие docstring, где это необходимо.

2.  **Импорты:**
    -   Убедиться, что все импорты используются, и добавить недостающие.

3.  **Обработка ошибок:**
    -   Заменить `try-except` блоки на использование `logger.error` для логирования ошибок и выхода из функций.
    -   Унифицировать обработку исключений для всех функций.

4.  **Рефакторинг:**
    -   Вынести повторяющиеся блоки кода в отдельные функции для повышения читаемости и уменьшения дублирования.
    -   Упростить сложные конструкции, где это возможно.
    -   Пересмотреть использование `...` и заменить на конкретные действия или комментарии.

5.  **Форматирование:**
    -   Привести в порядок все комментарии в соответствии с RST.
    -   Использовать консистентные имена переменных и функций.

6.  **Логирование:**
    -   Добавить более подробные логи, где это необходимо, включая контекст ошибки.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для выполнения действий с веб-элементами на основе конфигураций (локаторов).
=========================================================================================

Модуль `executor` предназначен для выполнения действий с веб-элементами, основываясь на предоставленных конфигурациях,
называемых "локаторами". Локаторы представляют собой словари, содержащие информацию о том, как находить и взаимодействовать
с элементами на веб-странице. Модуль обеспечивает следующие функциональные возможности:

1. **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`,
   что обеспечивает гибкость в управлении данными локаторов.

2. **Взаимодействие с веб-элементами**: В зависимости от предоставленных данных, модуль может выполнять различные действия,
   такие как клики, отправка сообщений, выполнение событий и получение атрибутов веб-элементов.

3. **Обработка ошибок**: Модуль поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы,
   которые могут иметь нестабильные элементы или требовать особого подхода.

4. **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, позволяя идентифицировать
   и взаимодействовать с одним или несколькими веб-элементами одновременно.

Этот модуль предоставляет гибкость и универсальность при работе с веб-элементами, позволяя автоматизировать сложные сценарии
взаимодействия с веб-страницами.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    driver = webdriver.Chrome(options=options)

    locator = {'by': 'ID', 'selector': 'myElementId'}

    executor = ExecuteLocator(driver=driver)
    element = await executor.execute_locator(locator)
    # Работаем с элементом
    driver.quit()

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
from src.utils.image import save_png



@dataclass
class ExecuteLocator:
    """
    Класс для обработки локаторов веб-элементов с использованием Selenium.

    :param driver: Опциональный экземпляр веб-драйвера Selenium.
    :type driver: Optional[object]
    :param actions: Объект для выполнения цепочки действий.
    :type actions: ActionChains
    :param by_mapping: Словарь соответствий для методов поиска элементов.
    :type by_mapping: dict
    :param mode: Режим работы (debug, dev и т.д.).
    :type mode: str

    :ivar driver: Экземпляр веб-драйвера Selenium.
    :ivar actions: Объект для выполнения цепочки действий.
    :ivar by_mapping: Словарь соответствий для методов поиска элементов.
    :ivar mode: Режим работы (debug, dev и т.д.).
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
        Инициализация объекта `ActionChains` после создания экземпляра класса.
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
        :type timeout: Optional[float]
        :param timeout_for_event: Условие ожидания ('presence_of_element_located', 'element_to_be_clickable').
        :type timeout_for_event: Optional[str]
        :param message: Опциональное сообщение для отправки.
        :type message: Optional[str]
        :param typing_speed: Скорость ввода текста для событий send_keys.
        :type typing_speed: Optional[float]
        :param continue_on_error: Флаг продолжения выполнения при ошибке.
        :type continue_on_error: Optional[bool]
        :return: Результат выполнения операции в зависимости от инструкций локатора.
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
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        if not locator or (not locator.attribute and not locator.selector):
            return None  # локатор-заглушка

        async def _parse_locator(
            locator: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """
            Разбирает и выполняет инструкции локатора.

            :param locator: Данные локатора.
            :type locator: Union[dict, SimpleNamespace]
            :param message: Сообщение для отправки, если необходимо.
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
                    #  устанавливает константное или формульное значение в атрибут локатора и возвращает его если `by == 'VALUE'`
                    if locator.by == 'VALUE':
                        return locator.attribute

            except Exception as ex:
                if MODE in ('dev', 'debug'):
                    logger.debug(f"Ошибка локатора: {locator=}", exc_info=True)
                return

            if locator.event:
                return await self.execute_event(locator, timeout, timeout_for_event, message, typing_speed)
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            return await self.get_webelement_by_locator(locator, timeout, timeout_for_event)

        return await _parse_locator(locator, message)


    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Вычисляет и обрабатывает атрибуты локатора.

        :param attribute: Атрибуты для вычисления.
        :type attribute: Union[str, List[str], dict]
        :return: Вычисленные атрибуты.
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
            Внутренняя функция для вычисления одного атрибута.

            :param attr: Атрибут для вычисления.
            :type attr: str
            :return: Вычисленный атрибут.
            :rtype: Optional[str]
            """
            match = re.match(r"^%(\w+)%", attr)
            if match:
                key_name = match.group(1)
                return getattr(Keys, key_name, None)
            return attr

        if isinstance(attribute, list):
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(str(attribute))

    async def get_attribute_by_locator(
        self,
        locator: SimpleNamespace | dict,
        timeout: Optional[float] = 0,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
    ) -> WebElement | list[WebElement] | None:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания появления элемента.
        :type timeout: Optional[float]
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str
        :return: Значение атрибута(ов) или словарь с атрибутами.
        :rtype: WebElement | list[WebElement] | None

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
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        web_element: WebElement = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            if MODE in ('dev', 'debug'):
                logger.debug(f"Элемент не найден: {locator=}")
            return

        def _parse_dict_string(attr_string: str) -> dict | None:
            """
            Разбирает строку вида '{attr1:attr2}' в словарь.

            :param attr_string: Строка, представляющая структуру, похожую на словарь.
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
                if MODE in ('dev', 'debug'):
                    logger.debug(f"Неверный формат строки атрибутов: {pprint(attr_string, text_color='WHITE', bg_color='RED')}", exc_info=True)
                return
            except Exception as ex:
                if MODE in ('dev', 'debug'):
                    logger.debug(f"Неверный формат строки атрибутов: {pprint(attr_string, text_color='WHITE', bg_color='RED')}", exc_info=True)
                return


        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """
            Извлекает значения атрибутов для каждого ключа в данном словаре.

            :param web_element: Веб-элемент для извлечения атрибутов.
            :type web_element: WebElement
            :param attr_dict: Словарь, где ключи/значения представляют имена атрибутов.
            :type attr_dict: dict
            :return: Словарь с атрибутами и их соответствующими значениями.
            :rtype: dict
            """
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = web_element.get_attribute(key)
                    attr_value = web_element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.debug(
                            f"Ошибка при извлечении атрибутов '{key}' или '{value}' из элемента.", exc_info=True)
                    return
            return result

        if web_element:
            # Проверка, является ли атрибут строкой, похожей на словарь
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
                    if MODE in ('dev', 'debug'):
                        logger.debug(f"Ошибка в get_attribute(): {pprint(locator, text_color='YELLOW', bg_color='BLACK')}", exc_info=True)
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

        :param locator: Данные локатора.
        :type locator: dict | SimpleNamespace
        :param timeout: Время ожидания для поиска элемента.
        :type timeout: Optional[float]
        :param timeout_for_event: Условие ожидания ('presence_of_element_located' и т.д.).
        :type timeout_for_event: Optional[str]
        :return: Веб-элемент или список веб-элементов.
        :rtype: WebElement | List[WebElement] | None
        """
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрует список веб-элементов по правилу, указанному в `locator.if_list`.

            :param web_elements: Веб-элемент или список веб-элементов.
            :type web_elements: WebElement | List[WebElement]
            :param locator: Локатор, содержащий правило фильтрации.
            :type locator: SimpleNamespace
            :return: Отфильтрованный веб-элемент или список веб-элементов.
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
            logger.error('Некорректный локатор.')
            return None

        web_elements = None
        try:
            # Если timeout = 0, попытаться найти элемент без ожидания
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
            return await _parse_elements_list(web_elements, locator)

        except TimeoutException as ex:
             if MODE in ('dev', 'debug'):
                logger.error(f'Таймаут для локатора: {locator}', exc_info=True)
             return None
        except Exception as ex:
             if MODE in ('dev', 'debug'):
                logger.error(f'Ошибка локатора: {locator}', exc_info=True)
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
        Делает скриншот расположенного веб-элемента.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания появления элемента.
        :type timeout: float
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str
        :param message: Сообщение для отправки элементу.
        :type message: Optional[str]
        :param typing_speed: Скорость ввода текста для send message событий.
        :type typing_speed: float
        :param continue_on_error: Флаг продолжения выполнения при ошибке.
        :type continue_on_error: bool
        :param webelement: Предварительно полученный веб-элемент.
        :type webelement: Optional[WebElement]
        :return: Бинарный поток скриншота или None, если не удалось.
        :rtype: BinaryIO | None
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event)

        if not webelement:
            return

        try:
            screenshot_stream = webelement.screenshot_as_png
            return screenshot_stream
        except Exception as ex:
             logger.error(f"Не удалось захватить скриншот", exc_info=True)
             return

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
        :param timeout: Время ожидания для поиска элемента.
        :type timeout: float
        :param timeout_for_event: Условие ожидания для события.
        :type timeout_for_event: str
        :param message: Сообщение для отправки с событием.
        :type message: Optional[str]
        :param typing_speed: Скорость ввода текста для событий send_keys.
        :type typing_speed: int
        :return: True, если выполнение события прошло успешно, False в противном случае.
        :rtype: str | list[str] | bytes | list[bytes] | bool
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )
        events = str(locator.event).split(";")
        result: list = []
        # Получить веб-элемент на основе локатора
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
                     if MODE in ('dev', 'debug'):
                        logger.error(f"Клик перехвачен: {locator=}", exc_info=True)
                     return
                except Exception as ex:
                     if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка клика: {locator=}", exc_info=True)
                     return

            elif event.startswith("pause("):
                match = re.match(r"pause\((\d+)\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                if MODE in ('dev', 'debug'):
                    logger.debug(f"Не удалось установить паузу: {locator=}")
                return False

            elif event == "upload_media()":
                if not message:
                    if MODE in ('dev', 'debug'):
                        logger.debug(f"Необходимо сообщение для события upload_media. Сообщение: {pprint(message, text_color='WHITE',bg_color='RED')}")
                    return False
                try:
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.debug(f"Ошибка загрузки медиа: {message=}", exc_info=True)
                    return False

            elif event == "screenshot()":
                try:
                    result.append(await self.get_webelement_as_screenshot(locator, webelement=webelement))
                except Exception as ex:
                     if MODE in ('dev', 'debug'):
                         logger.error(f"Ошибка при снятии скриншота: {locator=}", exc_info=True)
                     return False

            elif event == "clear()":
                try:
                    await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                     if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка очистки элемента: {locator=}", exc_info=True)
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
                     if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка при отправке клавиш: {locator=}", exc_info=True)
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



    async def send_message(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: str = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
    ) -> bool:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Информация о местоположении элемента на странице.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки веб-элементу.
        :type message: Optional[str]
        :param typing_speed: Скорость ввода сообщения в секундах.
        :type typing_speed: float
        :return: True, если сообщение было отправлено успешно, False в противном случае.
        :rtype: bool

        Пример:
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
            replace_dict: dict = {";": "SHIFT+ENTER"},
            typing_speed: float = typing_speed,
        ) -> bool:
            """
            Вводит сообщение в веб-элемент с заданной скоростью.

            :param el: Веб-элемент для ввода сообщения.
            :type el: WebElement
            :param message: Сообщение для ввода.
            :type message: str
            :param replace_dict: Словарь замен символов в сообщении.
            :type replace_dict: dict
            :param typing_speed: Скорость ввода сообщения в секундах.
            :type typing_speed: float
            :return: True, если сообщение было введено успешно, False в противном случае.
            :rtype: bool

            Пример:
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
                            #  TODO:
                            #  делать проверку в словаре подмен
                            # self.actions.perform()
                            # key = replace_dict[letter].split('+')
                            # self.actions.key_down(key[0])
                            # self.actions.send_keys(key[1])
                            # self.actions.key_up(key[0])
                            # self.actions.perform()
                        else:
                            self.actions.send_keys(letter)
                            self.actions.pause(typing_speed)
                            self.actions.perform()
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка ввода сообщения\n{message=}\n{word=}\n{letter=}", exc_info=True)
                    continue  # если была ошибка в передаче буквы - пока игнорую её
                    # TODO:
                    # Установить обработчик ошибок
            return True

        webelement = await self.get_webelement_by_locator(locator = locator, timeout =  timeout, timeout_for_event = timeout_for_event)
        if