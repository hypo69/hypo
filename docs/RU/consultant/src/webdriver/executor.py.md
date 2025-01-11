## Анализ кода модуля `executor`

**Качество кода**
6
-  Плюсы
    - Код хорошо структурирован и разбит на функции.
    - Присутствует базовая документация для функций и классов.
    - Используются `dataclass` для хранения данных, что упрощает код.
    - Применяются асинхронные операции, что делает код более производительным.
    - Есть обработка исключений с использованием `logger`.
    - Присутствуют импорты необходимых библиотек.
-  Минусы
    - Не везде используется `j_loads` или `j_loads_ns`.
    - Некоторые docstring требуют доработки в формате reStructuredText (RST).
    - Есть избыточное использование `try-except` блоков.
    - Не все переменные и функции имеют подробные docstring.
    - Использование `...` в коде является нежелательным.
    - Есть повторения кода, которые можно вынести в отдельные функции.
    - Некоторые комментарии не совсем информативны.
    - Не хватает более подробного описания модуля в начале файла.

**Рекомендации по улучшению**

1.  **Использование `j_loads`:** Заменить все `json.load` на `j_loads` или `j_loads_ns` для чтения файлов.
2.  **Формат документации:** Привести docstring к формату RST для совместимости со Sphinx.
3.  **Обработка ошибок:** Заменить избыточные `try-except` на использование `logger.error` и `return`.
4.  **Улучшение комментариев:** Сделать комментарии более информативными и конкретными.
5.  **Удалить `...`:** Заменить все `...` на конкретную обработку или логирование.
6.  **Добавить недостающие импорты:** Убедиться, что все необходимые библиотеки импортированы.
7.  **Рефакторинг:** Вынести повторяющийся код в отдельные функции для переиспользования.
8.  **Описание модуля:** Добавить подробное описание модуля в начале файла.
9.  **Документация функций и методов:** Добавить документацию ко всем функциям, методам и переменным.
10. **Именование переменных и функций:** Привести в соответствие с ранее обработанными файлами.
11. **Унифицировать кавычки:** Использовать одинарные кавычки `'` в коде Python, двойные кавычки `" ` только в операциях вывода.
12. **Проверка типа `locator`:** Добавить проверку типа `locator` для предотвращения ошибок.
13. **Обработка `if_list`:** Сделать более гибкую обработку `if_list`.
14. **Консистентность параметров:** Привести в соответствие параметры в функциях.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для взаимодействия с веб-элементами с использованием Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`ExecuteLocator`, который используется для выполнения различных действий
с веб-элементами на основе предоставленных локаторов. Локаторы представляют собой словари или объекты SimpleNamespace,
содержащие информацию о том, как найти и взаимодействовать с элементами на веб-странице.

Модуль включает в себя следующие возможности:

1. **Обработка локаторов:** Преобразует словари в объекты SimpleNamespace для удобства работы с данными локаторов.

2. **Взаимодействие с элементами:** Выполняет действия, такие как клики, ввод текста, выполнение JavaScript, получение атрибутов.

3. **Обработка ошибок:** Позволяет продолжить выполнение скрипта при возникновении ошибок с возможностью логирования.

4. **Поддержка разных типов локаторов:** Позволяет работать как с единичными, так и со множественными веб-элементами.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from src.logger.logger import logger
    from pathlib import Path

    driver = webdriver.Chrome()  # Замените на ваш драйвер
    executor = ExecuteLocator(driver=driver, mode='debug')

    async def main():
        locator = {'by': 'ID', 'selector': 'some_element_id'}
        element = await executor.execute_locator(locator)

        if element:
            print(f'Элемент найден: {element}')
        else:
            print('Элемент не найден')

        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())
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
    Класс для управления веб-элементами с использованием Selenium.

    Attributes:
        driver (Optional[object]): Экземпляр веб-драйвера Selenium.
        actions (ActionChains): Экземпляр ActionChains для выполнения цепочек действий.
        by_mapping (dict): Словарь соответствия строковых значений By.*.
        mode (str): Режим работы.
    """

    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(
        default_factory=lambda: {
            'XPATH': By.XPATH,
            'ID': By.ID,
            'TAG_NAME': By.TAG_NAME,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'NAME': By.NAME,
            'LINK_TEXT': By.LINK_TEXT,
            'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
            'CLASS_NAME': By.CLASS_NAME,
        }
    )
    mode: str = 'debug'

    def __post_init__(self):
        """Инициализирует ActionChains, если передан драйвер."""
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
        Выполняет действие с веб-элементом на основе предоставленного локатора.

        Args:
            locator (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
            timeout (float, optional): Время ожидания элемента. По умолчанию 0.
            timeout_for_event (str, optional): Тип ожидаемого события.
              ('presence_of_element_located', 'element_to_be_clickable'). По умолчанию 'presence_of_element_located'.
            message (str, optional): Сообщение для отправки, если применимо. По умолчанию None.
            typing_speed (float, optional): Скорость набора текста для событий send_keys. По умолчанию 0.
            continue_on_error (bool, optional): Флаг для продолжения выполнения при ошибке. По умолчанию True.

        Returns:
            str | list | dict | WebElement | bool: Результат выполнения, основанный на инструкциях локатора.

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
        # Проверка типа и преобразование локатора
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )
        if not locator or (not locator.attribute and not locator.selector):
            return None  # Если локатор не задан или не содержит атрибутов или селектора

        async def _parse_locator(
            locator: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """
            Разбирает и выполняет инструкции локатора.

            Args:
                locator (Union[dict, SimpleNamespace]): Данные локатора.
                message (Optional[str]): Сообщение для отправки, если применимо.

            Returns:
                str | list | dict | WebElement | bool: Результат выполнения.
            """
            locator = (
                locator
                if isinstance(locator, SimpleNamespace)
                else SimpleNamespace(**locator)
            )
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return

            try:
                # Получение значения By из словаря
                locator.by = self.by_mapping.get(locator.by.upper(), locator.by)
                if locator.attribute:
                    locator.attribute = await self.evaluate_locator(
                        locator.attribute
                    )
                    # Если by == 'VALUE', возвращаем значение атрибута
                    if locator.by == 'VALUE':
                        return locator.attribute

            except Exception as ex:
                logger.debug(f'Locator Error: {locator=}', ex, False)
                return

            if locator.event:
                return await self.execute_event(
                    locator, timeout, timeout_for_event, message, typing_speed
                )
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            return await self.get_webelement_by_locator(
                locator, timeout, timeout_for_event
            )

        return await _parse_locator(locator, message)

    async def evaluate_locator(
        self, attribute: str | List[str] | dict
    ) -> Optional[str | List[str] | dict]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        Args:
            attribute (str | List[str] | dict): Атрибуты для оценки.

        Returns:
            str | List[str] | dict | None: Оцененные атрибуты или None.

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
            Оценивает значение атрибута.

            Args:
                attr (str): Атрибут для оценки.

            Returns:
                 Optional[str]: Оцененный атрибут или None
            """
            match = re.match(r'^%(\w+)%', attr)
            if match:
                key = match.group(1)
                return getattr(Keys, key, None)
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
        Получает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        Args:
            locator (dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.
            timeout (float, optional): Максимальное время ожидания появления элемента. По умолчанию 0.
            timeout_for_event (str, optional): Тип условия ожидания. По умолчанию 'presence_of_element_located'.

        Returns:
            Union[str, list, dict, WebElement | list[WebElement] | None]: Значение(я) атрибута или словарь с атрибутами.
            Возвращает None, если веб-элемент не найден.

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
        # Проверка типа и преобразование локатора
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )
        if not locator:
            logger.debug(f'Локатор не задан', None, False)
            return None


        web_element: WebElement = await self.get_webelement_by_locator(
            locator, timeout, timeout_for_event
        )
        if not web_element:
            logger.debug(f'Не найден: {locator=}', None, False)
            return None

        def _parse_dict_string(attr_string: str) -> dict | None:
            """
            Разбирает строку вида '{attr1:attr2}' в словарь.

            Args:
                attr_string (str): Строка, представляющая структуру, похожую на словарь.

            Returns:
                dict | None: Разобранный словарь или None, если разбор не удался.
            """
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (
                        pair.split(':') for pair in attr_string.strip('{}').split(',')
                    )
                }
            except ValueError as ex:
                logger.debug(
                    f'Неверный формат атрибута: {pprint(attr_string, text_color=\'WHITE\', bg_color=\'RED\')}',
                    ex,
                    False,
                )
                return None

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """
            Получает значения атрибутов для каждого ключа в словаре.

            Args:
                web_element (WebElement): Веб-элемент для получения атрибутов.
                attr_dict (dict): Словарь, где ключи представляют имена атрибутов.

            Returns:
                dict: Словарь с атрибутами и их значениями.
            """
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = web_element.get_attribute(key)
                    attr_value = web_element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    logger.debug(
                        f'Ошибка получения атрибута {key} или {value} из элемента.',
                        ex,
                        False,
                    )
                    return {}
            return result

        if web_element:
            if (
                isinstance(locator.attribute, str)
                and locator.attribute.startswith('{')
            ):
                attr_dict = _parse_dict_string(locator.attribute)

                if isinstance(web_element, list):
                    return [
                        _get_attributes_from_dict(el, attr_dict) for el in web_element
                    ]
                return _get_attributes_from_dict(web_element, attr_dict)

            if isinstance(web_element, list):
                ret: list = []
                try:
                    for e in web_element:
                        ret.append(f'{e.get_attribute(locator.attribute)}')
                    return ret if len(ret) > 1 else ret[0]
                except Exception as ex:
                    logger.debug(
                        f'Ошибка в get_attribute(): {pprint(locator, text_color=\'YELLOW\', bg_color=\'BLACK\')}',
                        ex,
                        False,
                    )
                    return None

            return web_element.get_attribute(locator.attribute)
        return None

    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
    ) -> WebElement | List[WebElement] | None:
        """
        Получает веб-элемент или список элементов по указанному локатору.

        Args:
            locator (dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.
            timeout (float, optional): Максимальное время ожидания элемента. По умолчанию 0.
            timeout_for_event (str, optional): Тип условия ожидания. По умолчанию 'presence_of_element_located'.

        Returns:
            WebElement | List[WebElement] | None: Веб-элемент или список элементов, или None, если элемент не найден.
        """
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace,
        ) -> WebElement | List[WebElement]:
            """
            Фильтрует список веб-элементов на основе правила, заданного в `locator.if_list`.

            Args:
                web_elements (WebElement | List[WebElement]): Веб-элемент или список элементов.
                locator (SimpleNamespace): Локатор.

            Returns:
                 WebElement | List[WebElement]: Отфильтрованный веб-элемент или список элементов.
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
        # Проверка типа и преобразование локатора
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
                web_elements = await asyncio.to_thread(
                    driver.find_elements, locator.by, locator.selector
                )
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
                    condition((locator.by, locator.selector)),
                )
            return await _parse_elements_list(web_elements, locator)

        except TimeoutException as ex:
            logger.error(f'Таймаут для локатора: {locator}', ex, False)
            return None
        except Exception as ex:
            logger.error(f'Ошибка локатора: {locator}', ex, False)
            return None

    async def get_webelement_as_screenshot(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
        webelement: Optional[WebElement] = None,
    ) -> BinaryIO | None:
        """
        Делает скриншот найденного веб-элемента.

        Args:
            locator (dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.
            timeout (float, optional): Максимальное время ожидания появления элемента. По умолчанию 5.
            timeout_for_event (str, optional): Тип условия ожидания. По умолчанию 'presence_of_element_located'.
            message (str, optional): Сообщение для отправки. По умолчанию None.
            typing_speed (float, optional): Скорость набора текста, если необходимо. По умолчанию 0.
            continue_on_error (bool, optional): Флаг для продолжения при ошибке. По умолчанию True.
            webelement (WebElement, optional): Уже найденный веб-элемент. По умолчанию None.

        Returns:
            BinaryIO | None: Бинарный поток изображения или None, если произошла ошибка.
        """
        # Проверка типа и преобразование локатора
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )
        if not locator:
            logger.debug(f'Локатор не задан', None, False)
            return None

        if not webelement:
            webelement = await self.get_webelement_by_locator(
                locator=locator, timeout=timeout, timeout_for_event=timeout_for_event
            )
        if not webelement:
            return None

        try:
            screenshot_stream = webelement.screenshot_as_png
            return screenshot_stream
        except Exception as ex:
            logger.error(f'Не удалось захватить скриншот', ex, False)
            return None

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

        Args:
            locator (SimpleNamespace | dict): Локатор, определяющий элемент и событие.
            timeout (float, optional): Время ожидания элемента. По умолчанию 5.
            timeout_for_event (str, optional): Время ожидания события. По умолчанию 'presence_of_element_located'.
            message (str, optional): Сообщение для отправки с событием, если применимо. По умолчанию None.
            typing_speed (float, optional): Скорость набора текста для событий send_keys. По умолчанию 0.

        Returns:
            str | list[str] | bytes | list[bytes] | bool: Результат выполнения события.
        """
        # Проверка типа и преобразование локатора
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )
        if not locator:
            logger.debug(f'Локатор не задан', None, False)
            return False

        events = str(locator.event).split(';')
        result: list = []
        # Получение веб-элемента на основе локатора
        webelement = await self.get_webelement_by_locator(
            locator, timeout, timeout_for_event
        )

        if not webelement:
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement

        for event in events:
            if event == 'click()':
                try:
                    webelement.click()
                    continue
                except ElementClickInterceptedException as ex:
                    logger.error(f'Клик перехвачен элементом: {locator=}', ex, False)
                    return False
                except Exception as ex:
                    logger.error(f'Ошибка при клике на элемент: {locator=}', ex, False)
                    return False

            elif event.startswith('pause('):
                match = re.match(r'pause\((\d+)\)', event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                logger.debug(f'Не удалось сделать паузу: {locator=}')
                return False

            elif event == 'upload_media()':
                if not message:
                    logger.debug(
                        f'Требуется сообщение для upload_media события. Сообщение: {pprint(message, text_color=\'WHITE\',bg_color=\'RED\')}',
                        None,
                        False,
                    )
                    return False
                try:
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    logger.debug(f'Ошибка загрузки медиа: {message=}', ex, False)
                    return False

            elif event == 'screenshot()':
                try:
                    result.append(
                        await self.get_webelement_as_screenshot(
                            locator, webelement=webelement
                        )
                    )
                except Exception as ex:
                    logger.error(f'Ошибка при создании скриншота: {locator=}', ex, False)
                    return False

            elif event == 'clear()':
                try:
                    await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                    logger.error(f'Ошибка при очистке элемента: {locator=}', ex, False)
                    return False

            elif event.startswith('send_keys('):
                keys_to_send = event.replace('send_keys(', '').replace(')', '').split('+')
                try:
                    actions = ActionChains(self.driver)
                    for key in keys_to_send:
                        key = key.strip().strip("'")
                        if hasattr(Keys, key):
                            key_to_send = getattr(Keys, key)
                            actions.send_keys(key_to_send)
                    await asyncio.to_thread(actions.perform)
                except Exception as ex:
                    logger.error(f'Ошибка при отправке клавиш: {locator=}', ex, False)
                    return False

            elif event.startswith('type('):
                message = event.replace('type(', '').replace(')', '')
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

        Args:
            locator (dict | SimpleNamespace): Информация о местоположении элемента на странице.
            timeout (float, optional): Максимальное время ожидания появления элемента. По умолчанию 5.
            timeout_for_event (str, optional): Тип условия ожидания. По умолчанию 'presence_of_element_located'.
            message (str, optional): Сообщение для отправки веб-элементу. По умолчанию None.
            typing_speed (float, optional): Скорость набора сообщения в секундах. По умолчанию 0.

        Returns:
            bool: Возвращает True, если сообщение было успешно отправлено, False в противном случае.

        Example:
            >>> driver = Driver()
            >>> driver.send_message(locator={'id': 'messageBox'}, message='Hello World', typing_speed=0.1)
            True
        """
        # Проверка типа и преобразование локатора
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(locator)
        )
        if not locator:
            logger.debug(f'Локатор не задан', None, False)
            return False

        def type_message(
            el: WebElement,
            message: str,
            replace_dict: dict = {';': 'SHIFT+ENTER'},
            typing_speed: float = typing_speed,
        ) -> bool:
            """
            Набирает сообщение в веб-элемент с указанной скоростью.

            Args:
                el (WebElement): Веб-элемент, в который набирается сообщение.
                message (str): Сообщение для набора.
                replace_dict (dict, optional): Словарь для замены символов в сообщении. По умолчанию {';': 'SHIFT+ENTER'}.
                typing_speed (float, optional): Скорость набора сообщения в секундах. По умолчанию 0.

            Returns:
                bool: Возвращает True, если сообщение было успешно набрано, False в противном случае.
            """
            message = message.split(' ')

            for word in message:
                word += ' '
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
                    logger.error(
                        f'Ошибка при наборе сообщения\\n{message=}\\n{word=}\\n{letter=}',
                        ex,
                        False
                    )
                    continue
            return True

        webelement = await self.get_webelement_by_locator(
            locator=locator, timeout=timeout, timeout_for_event=timeout_for_event
        )
        if not webelement or (isinstance(webelement, list) and len(webelement) == 0):
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement
        self.actions.move_to_element(webelement)
        type_message(
            el=webelement,
            message=message,
            replace_dict={';': 'SHIFT+ENTER'},
            typing_speed=typing_speed,
        )
        return True