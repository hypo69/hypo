## Анализ кода модуля `executor.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован с использованием классов и функций.
    - Присутствуют обработки исключений с логированием ошибок.
    - Использованы асинхронные функции для неблокирующих операций.
    - Активно используется модуль `logger` для логирования.
- **Минусы**:
    - Некоторые участки кода требуют более подробной документации.
    - Встречаются смешанные стили кавычек (одинарные и двойные).
    - Не все функции и методы имеют docstring.
    - Некоторые переменные не имеют аннотации типов.
    - Есть места, где можно улучшить читаемость кода, добавив больше пробелов.

**Рекомендации по улучшению:**

1.  **Форматирование и стиль кода**:
    *   Привести все строки к использованию одинарных кавычек.
    *   Добавить пробелы вокруг операторов присваивания и других операторов.
    *   Удалить неиспользуемые импорты.
2.  **Документация**:
    *   Добавить docstring к каждой функции и методу, описывая параметры, возвращаемые значения и возможные исключения.
    *   В docstring добавить примеры использования.
    *   Улучшить существующие комментарии, сделав их более информативными и точными.
3.  **Обработка данных и логирование**:
    *   Убедиться, что все ошибки логируются с использованием `logger.error` с указанием `exc_info=True` для вывода трассировки.
4.  **Типизация**:
    *   Добавить аннотации типов для всех переменных, где это возможно.
5.  **Улучшение читаемости**:
    *   Разбить длинные функции на более мелкие, чтобы упростить их понимание и поддержку.

**Оптимизированный код:**

```python
## \file /src/webdriver/executor.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для взаимодействия с веб-элементами с использованием Selenium.
======================================================================

Этот модуль предоставляет функциональность для взаимодействия с веб-элементами,
используя Selenium, на основе предоставленных локаторов. Он обрабатывает
парсинг локаторов, взаимодействие с элементами и обработку ошибок.

Модуль является ключевым компонентом для автоматизированного взаимодействия
с веб-страницами. Он позволяет находить элементы на странице по различным
локаторам (например, id, class, xpath), выполнять с ними различные действия
(например, клик, ввод текста) и получать значения их атрибутов. Модуль также
включает механизмы ожидания появления элементов и обработки возможных ошибок,
таких как таймауты и перехваты кликов.

Пример использования:
--------------------

>>> executor = ExecuteLocator(driver)
>>> locator = {'by': 'id', 'selector': 'my_element', 'attribute': 'value'}
>>> result = await executor.execute_locator(locator)
"""

import asyncio
import re
from dataclasses import dataclass, field
from typing import BinaryIO, List, Optional
from types import SimpleNamespace
from itertools import zip_longest
from urllib.parse import urlparse, parse_qs

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.logger.logger import logger
from src.utils.printer import pprint as print


@dataclass
class ExecuteLocator:
    """
    Класс для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.
    """

    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    mode: str = 'debug'

    def __post_init__(self) -> None:
        """
        Инициализирует объект ActionChains с использованием драйвера, если он предоставлен.
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
    ) -> Optional[str | list | dict | WebElement | bool]:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        Args:
            locator (dict | SimpleNamespace): Данные локатора.
            timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию 0.
            timeout_for_event (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.
            message (Optional[str], optional): Сообщение для действий, таких как send_keys или type. По умолчанию None.
            typing_speed (Optional[float], optional): Скорость печати для событий send_keys (в секундах). По умолчанию 0.

        Returns:
            Optional[str | list | dict | WebElement | bool]: Результат операции, который может быть строкой, списком, словарем, WebElement, булевым значением или None.

        Example:
            >>> locator = {'by': 'id', 'selector': 'my_element', 'attribute': 'value'}
            >>> result = await self.execute_locator(locator)
            >>> print(result)
            None
        """
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)

        if not getattr(locator, 'attribute', None) and not getattr(locator, 'selector', None):
            logger.debug('Empty locator provided.', None, False)
            return None

        async def _parse_locator(
            locator: SimpleNamespace,
            message: Optional[str] = None,
            timeout: Optional[float] = 0,
            timeout_for_event: Optional[str] = 'presence_of_element_located',
            typing_speed: Optional[float] = 0,
        ) -> Optional[str | list | dict | WebElement | bool]:
            """
            Разбирает и выполняет инструкции локатора.

            Args:
                locator (SimpleNamespace):  Данные локатора.
                message (Optional[str], optional): Сообщение для действий, таких как send_keys или type. По умолчанию None.
                timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию 0.
                timeout_for_event (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.
                typing_speed (Optional[float], optional): Скорость печати для событий send_keys (в секундах). По умолчанию 0.

            Returns:
                Optional[str | list | dict | WebElement | bool]: Результат операции, который может быть строкой, списком, словарем, WebElement, булевым значением или None.
            """

            if locator.event and locator.attribute and locator.mandatory is None:
                logger.debug(
                    f'Locator with event and attribute but missing mandatory flag. Skipping. {print(locator.__dict__, text_color="yellow")} ',
                    None,
                    False,
                )
                return None

            if isinstance(locator.by, str):
                try:
                    locator.by = locator.by.lower()
                    if locator.attribute:
                        locator.attribute = self._evaluate_locator(locator.attribute)

                        if locator.by == 'value':
                            return locator.attribute

                        if locator.by == 'url':
                            if not locator.attribute:
                                logger.error(
                                    f'Attribute is missing for \'URL\' locator: {print(locator.__dict__, text_color="yellow")}'
                                )
                                return False

                            url = self.driver.current_url
                            parsed_url = urlparse(url)
                            query_params = parse_qs(parsed_url.query)
                            return query_params.get(locator.attribute, None)[0]

                except Exception as ex:
                    logger.error(
                        f'Error getting attribute by \'VALUE\': {print(locator.__dict__, text_color="yellow")}, error:',
                        ex,
                    )
                    return None

                if locator.event:
                    return await self.execute_event(locator, timeout, timeout_for_event, message, typing_speed)

                if locator.attribute:
                    return await self.get_attribute_by_locator(locator, timeout, timeout_for_event)

                return await self.get_webelement_by_locator(locator, timeout, timeout_for_event)

            elif isinstance(locator.selector, list) and isinstance(locator.by, list):
                if locator.sorted == 'pairs':
                    elements_pairs = []

                    # TODO: Fix logic
                    for n in range(len(locator.by)): # type: ignore

                        l = SimpleNamespace(
                            **{
                                'attribute': locator.attribute[n], # type: ignore
                                'by': locator.by[n], # type: ignore
                                'selector': locator.selector[n], # type: ignore
                                'if_list': locator.if_list if isinstance(locator.if_list, str) else locator.if_list[n], # type: ignore
                                'mandatory': locator.mandatory if isinstance(locator.mandatory, str) else locator.mandatory[n], # type: ignore
                                'event': locator.event if isinstance(locator.event, str) else locator.event[n], # type: ignore
                                'timeout': locator.timeout if isinstance(locator.timeout, str) else locator.timeout[n], # type: ignore
                                'timeout_for_event': locator.timeout_for_event
                                if isinstance(locator.timeout_for_event, str)
                                else locator.timeout_for_event[n], # type: ignore
                                'locator_description': locator.locator_description,
                            }
                        )
                        elements_pairs.append(
                            await _parse_locator(l, message, timeout, timeout_for_event, message, typing_speed)
                        )

                    zipped_pairs = list(zip_longest(*elements_pairs, fillvalue=None))
                    return zipped_pairs

            else:
                logger.warning('Locator does not contain \'selector\' and \'by\' lists or invalid \'sorted\' value.')

        return await _parse_locator(locator, message, timeout, timeout_for_event, typing_speed)

    def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        Args:
            attribute (str | List[str] | dict): Атрибут для оценки (может быть строкой, списком строк или словарем).

        Returns:
            Optional[str | List[str] | dict]: Оцененный атрибут, который может быть строкой, списком строк или словарем.
        """

        def _evaluate(attr: str) -> Optional[str]:
            """Оценивает строку отдельного атрибута."""
            return (
                getattr(Keys, re.findall(r'%(\\w+)%', attr)[0], None) if re.match(r'^%\\w+%', attr) else attr
            )

        if isinstance(attribute, list):
            return [_evaluate(attr) for attr in attribute]
        return _evaluate(str(attribute))

    async def get_attribute_by_locator(
        self,
        locator: SimpleNamespace | dict,
        timeout: Optional[float] = 0,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
    ) -> Optional[WebElement | list[WebElement]]:
        """
        Извлекает атрибуты из веб-элемента или списка веб-элементов.

        Args:
            locator (SimpleNamespace | dict): Данные локатора.
            timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию 0.
            timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.
            message (Optional[str], optional): Не используется в этой функции. По умолчанию None.
            typing_speed (float, optional): Не используется в этой функции. По умолчанию 0.

        Returns:
            Optional[WebElement | list[WebElement]]: Значение атрибута(ов) в виде WebElement, списка WebElements или None, если не найдено.
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        web_element: WebElement | list[WebElement] | None = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            if locator.mandatory:
                logger.debug(f'Element not found: {print(locator, text_color="yellow")}')
            return None

        def _parse_dict_string(attr_string: str) -> dict | None:
            """Разбирает строку типа '{attr1:attr2}' в словарь."""
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(':') for pair in attr_string.strip('{}').split(','))
                }
            except ValueError as ex:
                logger.debug(f'Invalid attribute string format: {attr_string!r}', ex)
                return None

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """Извлекает значения атрибутов из WebElement на основе словаря."""
            result = {}
            for key, value in attr_dict.items():
                try:
                    attr_key = web_element.get_attribute(key)
                    attr_value = web_element.get_attribute(value)
                    result[attr_key] = attr_value
                except Exception as ex:
                    logger.debug(f'Error retrieving attributes \'{key}\' or \'{value}\' from element.', ex)
                    return {}
            return result

        if web_element:
            if isinstance(locator.attribute, str) and locator.attribute.startswith('{'):
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
                    logger.debug(f'Error in get_attribute(): {locator=}', ex)
                    return None

            return web_element.get_attribute(locator.attribute)
        return None

    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
    ) -> Optional[WebElement | List[WebElement]]:
        """
        Извлекает веб-элемент или список элементов на основе предоставленного локатора.

        Args:
            locator (dict | SimpleNamespace): Данные локатора.
            timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию 0.
            timeout_for_event (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.

        Returns:
            Optional[WebElement | List[WebElement]]: WebElement, список WebElements или None, если не найдено.
        """
        timeout = timeout if timeout > 0 else getattr(locator, 'timeout', 0)

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement], locator: SimpleNamespace
        ) -> Optional[WebElement | List[WebElement]]:
            """Фильтрует список веб-элементов на основе атрибута if_list."""
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
        locator = SimpleNamespace(**locator) if isinstance(locator, dict) else locator

        if not locator:
            logger.error('Invalid locator provided.')
            return None

        web_elements = None
        try:
            if timeout == 0:
                web_elements = await asyncio.to_thread(driver.find_elements, locator.by, locator.selector)
            else:
                condition = (
                    EC.presence_of_all_elements_located
                    if timeout_for_event == 'presence_of_all_elements_located'
                    else EC.visibility_of_all_elements_located
                )
                web_elements = await asyncio.to_thread(
                    WebDriverWait(driver, timeout).until,
                    condition((locator.by, locator.selector)),
                )

            return await _parse_elements_list(web_elements, locator) if web_elements else None

        except TimeoutException as ex:
            logger.error(f'Timeout for locator: {print(locator.__dict__, text_color="yellow")}', ex, False)
            return None

        except Exception as ex:
            logger.error(f'Error locating element: {print(locator.__dict__, text_color="yellow")}', ex, False)
            return None

    async def get_webelement_as_screenshot(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        webelement: Optional[WebElement] = None,
    ) -> Optional[BinaryIO]:
        """
        Делает скриншот найденного веб-элемента.

        Args:
            locator (SimpleNamespace | dict): Данные локатора.
            timeout (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию 5.
            timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.
            message (Optional[str], optional): Не используется в этой функции. По умолчанию None.
            typing_speed (float, optional): Не используется в этой функции. По умолчанию 0.
            webelement (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию None.

        Returns:
            Optional[BinaryIO]: BinaryIO поток скриншота или None, если не удалось.
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(
                locator=locator, timeout=timeout, timeout_for_event=timeout_for_event
            )

        if not webelement:
            return None

        try:
            return webelement.screenshot_as_png
        except Exception as ex:
            logger.error('Failed to take screenshot', ex)
            return None

    async def execute_event(
        self,
        locator: SimpleNamespace | dict,
        timeout: float = 5,
        timeout_for_event: str = 'presence_of_element_located',
        message: str = None,
        typing_speed: float = 0,
    ) -> Optional[str | list[str] | bytes | list[bytes] | bool]:
        """
        Выполняет событие, связанное с локатором.

        Args:
            locator (SimpleNamespace | dict): Данные локатора.
            timeout (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию 5.
            timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.
            message (str, optional): Дополнительное сообщение для отправки с событием. По умолчанию None.
            typing_speed (float, optional): Скорость печати для событий send_keys (в секундах). По умолчанию 0.

        Returns:
            Optional[str | list[str] | bytes | list[bytes] | bool]: Результат выполнения события (str, список str, bytes, список bytes или bool).
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )
        events = str(locator.event).split(';')
        result: list = []

        web_element: WebElement | list[WebElement] | None = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            return False
        webelement = web_element[0] if isinstance(web_element, list) else web_element

        for event in events:
            if event == 'click()':
                try:
                    webelement.click()
                    continue
                except ElementClickInterceptedException as ex:
                    if locator.mandatory:
                        logger.error(f'Element click intercepted: {print(locator)}', ex, False)
                        return False
                except Exception as ex:
                    if locator.mandatory:
                        logger.error(f'Element click error:\\n {print(locator)} \\n', ex, False)
                        # try:
                        #     self.driver.execute_script("arguments[0].click();", webelement)
                        #     continue
                        # except Exception as ex:
                        #     logger.error(f"Element click error after javascript execution: {locator=}", ex)
                        #     return False
                        return False

            elif event.startswith('pause('):
                match = re.match(r'pause\\((\\d+)\\)', event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                if locator.mandatory:
                    logger.debug(f'Pause event parsing failed: {print(locator)}')
                    return False

            elif event == 'upload_media()':
                if not message and locator.mandatory:
                    logger.debug(f'Message is required for upload_media event. Message: {print(message)}')
                    return False
                try:
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    if locator.mandatory:
                        logger.debug(f'Error uploading media: {message=}', ex)
                        return False

            elif event == 'screenshot()':
                try:
                    result.append(await self.get_webelement_as_screenshot(locator, webelement=webelement))
                except Exception as ex:
                    logger.error(f'Error taking screenshot: {locator=}', ex, False)
                    return False

            elif event == 'clear()':
                try:
                    await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                    logger.error(f'Error clearing element: {locator=}', ex, False)
                    return False

            elif event.startswith('send_keys('):
                keys_to_send = event.replace('send_keys(', '').replace(')', '').split('+')
                try:
                    actions = ActionChains(self.driver)
                    for key in keys_to_send:
                        key = key.strip().strip('\'')
                        if hasattr(Keys, key):
                            key_to_send = getattr(Keys, key)
                            actions.send_keys(key_to_send)
                    await asyncio.to_thread(actions.perform)
                except Exception as ex:
                    logger.error(f'Error sending keys: {locator=}', ex, False)
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
    ) -> bool:
        """
        Отправляет сообщение веб-элементу.

        Args:
            locator (SimpleNamespace | dict): Данные локатора.
            timeout (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию 5.
            timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.
            message (str, optional): Сообщение для отправки веб-элементу. По умолчанию None.
            typing_speed (float, optional): Скорость печати для событий send_keys (в секундах). По умолчанию 0.

        Returns:
            bool: True, если сообщение отправлено успешно, False в противном случае.
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict) else None
        )

        def type_message(
            el: WebElement,
            message: str,
            replace_dict: dict = {';': 'SHIFT+ENTER'},
            typing_speed: float = typing_speed,
        ) -> bool:
            """Печатает сообщение в веб-элемент с указанной скоростью печати."""
            message = message.split(' ')
            for word in message:
                word += ' '
                try:
                    for letter in word:
                        if letter in replace_dict.keys():
                            self.actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
                        else:
                            self.actions.send_keys(letter)
                            self.actions.pause(typing_speed)
                            self.actions.perform()
                except Exception as ex:
                    logger.error(
                        f'Error typing message:/n message={print(message)},/n word={print(letter)},/n letter={print(letter)}/n',
                        ex,
                        False,
                    )
                    continue
            return True

        web_element: WebElement | list[WebElement] | None = await self.get_webelement_by_locator(
            locator=locator, timeout=timeout, timeout_for_event=timeout_for_event
        )
        if not web_element or (isinstance(web_element, list) and len(web_element) == 0):
            logger.debug('Web element was not found for sending message.')
            return False
        webelement = web_element[0] if isinstance(web_element, list) else web_element
        self.actions.move_to_element(webelement)
        type_message(
            el=webelement,
            message=message,
            replace_dict={';': 'SHIFT+ENTER'},
            typing_speed=typing_speed,
        )
        return True
```