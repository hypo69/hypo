## Улучшенный код

```python
"""
.. module:: src.webdriver
   :platform: Windows, Unix
   :synopsis: Модуль `executor` выполняет действия с веб-элементами на основе предоставленных конфигураций,
       известных как "локаторы". Эти конфигурации (или "локаторы") представляют собой словари, содержащие информацию о том,
       как найти и взаимодействовать с элементами на веб-странице. Модуль предоставляет следующие функциональные возможности:

   1. **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`,
      что обеспечивает гибкую работу с данными локатора.

   2. **Взаимодействие с веб-элементами**: В зависимости от предоставленных данных модуль может выполнять различные действия,
      такие как клики, отправка сообщений, выполнение событий и извлечение атрибутов веб-элементов.

   3. **Обработка ошибок**: Модуль поддерживает продолжение выполнения в случае возникновения ошибки, позволяя обрабатывать веб-страницы,
      которые могут иметь нестабильные элементы или требовать особого подхода.

   4. **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, позволяя идентифицировать и взаимодействовать
      с одним или несколькими веб-элементами одновременно.

   Этот модуль обеспечивает гибкость и универсальность при работе с веб-элементами, позволяя автоматизировать сложные сценарии веб-взаимодействия.
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
    StaleElementReferenceException,  # Этот импорт был добавлен
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

    :param driver: Экземпляр веб-драйвера Selenium.
    :type driver: Optional[object]
    :param actions: Экземпляр ActionChains для выполнения цепочек действий.
    :type actions: ActionChains
    :param by_mapping: Словарь для сопоставления строк с константами By.
    :type by_mapping: dict
    :param mode: Режим работы (например, 'debug').
    :type mode: str
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
        Инициализирует ActionChains при наличии драйвера.
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

        :param locator: Данные локатора (dict, SimpleNamespace или Locator).
        :type locator: dict | SimpleNamespace
        :param timeout: Время ожидания для поиска элемента.
        :type timeout: Optional[float]
        :param timeout_for_event: Условие ожидания ('presence_of_element_located', 'element_to_be_clickable').
        :type timeout_for_event: Optional[str]
        :param message: Сообщение для отправки (если применимо).
        :type message: Optional[str]
        :param typing_speed: Скорость печати для событий send_keys.
        :type typing_speed: Optional[float]
        :param continue_on_error: Продолжать ли выполнение при ошибке.
        :type continue_on_error: Optional[bool]
        :return: Результат выполнения в зависимости от инструкций локатора.
        :rtype: str | list | dict | WebElement | bool

        ```mermaid
                graph TD
            A[Начало] --> B[Проверка, является ли локатор SimpleNamespace или dict]
            B --> C{Локатор SimpleNamespace?}
            C -->|Да| D[Использовать локатор как есть]
            C -->|Нет| E[Преобразовать dict в SimpleNamespace]
            E --> D
            D --> F[Определение асинхронной функции _parse_locator]
            F --> G[Проверка, есть ли у локатора событие, атрибут или обязательность]
            G -->|Нет| H[Возврат None]
            G -->|Да| I[Попытка сопоставления by и вычисления атрибута]
            I --> J[Перехват исключений и логирование (если нужно)]
            J --> K{У локатора есть событие?}
            K -->|Да| L[Выполнение события]
            K -->|Нет| M{У локатора есть атрибут?}
            M -->|Да| N[Получение атрибута по локатору]
            M -->|Нет| O[Получение веб-элемента по локатору]
            L --> P[Возврат результата события]
            N --> P[Возврат результата атрибута]
            O --> P[Возврат результата веб-элемента]
            P --> Q[Возврат окончательного результата _parse_locator]
            Q --> R[Возврат результата execute_locator]
            R --> S[Конец]

        ```
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not locator.attribute and not locator.selector:
            return None  # <- локатор - заглушка

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
            :rtype: Union[str, list, dict, WebElement, bool]
            """
            locator = (
                locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator)
            )
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return

            try:
                # Код пытается получить значение `locator.by` из словаря `self.by_mapping`, иначе оставляет как есть
                locator.by = self.by_mapping.get(locator.by.upper(), locator.by)
                if locator.attribute:
                    # Код вызывает метод `evaluate_locator` для обработки атрибута
                    locator.attribute = await self.evaluate_locator(locator.attribute)
            except Exception as ex:
                if MODE in ('dev','debug'):
                    logger.debug(f"Locator Error: {locator=}")
                    ...
                return

            if locator.event:
                # Код вызывает метод `execute_event` для выполнения события
                return await self.execute_event(locator, timeout, timeout_for_event, message, typing_speed)
            if locator.attribute:
                # Код вызывает метод `get_attribute_by_locator` для получения атрибута
                return await self.get_attribute_by_locator(locator)
            # Код вызывает метод `get_webelement_by_locator` для получения веб-элемента
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
            A[Начало] --> B[Проверка, является ли атрибут списком]
            B -->|Да| C[Итерация по каждому атрибуту в списке]
            C --> D[Вызов _evaluate для каждого атрибута]
            D --> E[Возврат собранных результатов из asyncio.gather]
            B -->|Нет| F[Вызов _evaluate для единичного атрибута]
            F --> G[Возврат результата _evaluate]
            G --> H[Конец]
            E --> H
        ```
        """
        async def _evaluate(attr: str) -> Optional[str]:
            """
            Внутренняя функция для вычисления атрибута.

            :param attr: Атрибут для вычисления.
            :type attr: str
            :return: Вычисленный атрибут.
            :rtype: Optional[str]
            """
            return getattr(Keys, re.findall(r"%(\\w+)%", attr)[0], None) if re.match(r"^%\\w+%", attr) else attr

        if isinstance(attribute, list):
            # Код собирает результаты вычисления каждого атрибута из списка
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        # Код возвращает результат вычисления атрибута
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
            A[Начало] --> B[Проверка, является ли локатор SimpleNamespace или dict]
            B -->|Да| C[Преобразовать локатор в SimpleNamespace (если нужно)]
            C --> D[Вызов get_webelement_by_locator]
            D --> E[Проверка, найден ли web_element]
            E -->|Нет| F[Логирование отладочного сообщения и возврат]
            E -->|Да| G[Проверка, является ли locator.attribute строкой, похожей на словарь]
            G -->|Да| H[Разбор строки locator.attribute в словарь]
            H --> I[Проверка, является ли web_element списком]
            I -->|Да| J[Получение атрибутов для каждого элемента в списке]
            J --> K[Возврат списка атрибутов]
            I -->|Нет| L[Получение атрибутов для одиночного web_element]
            L --> K
            G -->|Нет| M[Проверка, является ли web_element списком]
            M -->|Да| N[Получение атрибутов для каждого элемента в списке]
            N --> O[Возврат списка атрибутов или одного атрибута]
            M -->|Нет| P[Получение атрибута для одиночного web_element]
            P --> O
            O --> Q[Конец]
            F --> Q
        ```
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        # Код получает веб-элемент по локатору
        web_element: WebElement = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            if MODE in ('dev','debug'):
                logger.debug(f"Не нашелся : {locator=}\\n", None, False)
            ...
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
                if MODE in ('dev','debug'):
                    logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}\\n", ex, False)
                return
            except Exception as ex:
                if MODE in ('dev','debug'):
                    logger.debug(f"Invalid attribute string format: {pprint(attr_string, text_color='WHITE', bg_color='RED')}\\n", ex, False)
                return

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """
            Получает значения атрибутов для каждого ключа в заданном словаре.

            :param web_element: Веб-элемент, из которого извлекаются атрибуты.
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
                    if MODE in ('dev','debug'):
                        logger.debug(
                            f"Error retrieving attributes '{key}' or '{value}' from element.", ex, False)
                    ...
                    return
            return result

        if web_element:
            # Проверка, является ли атрибут строкой, похожей на словарь
            if isinstance(locator.attribute, str) and locator.attribute.startswith("{"):
                attr_dict = _parse_dict_string(locator.attribute)

                if isinstance(web_element, list):
                    # Код получает атрибуты из списка веб-элементов
                    return [_get_attributes_from_dict(el, attr_dict) for el in web_element]
                # Код получает атрибуты из веб-элемента
                return _get_attributes_from_dict(web_element, attr_dict)

            if isinstance(web_element, list):
                ret: list = []
                try:
                    for e in web_element:
                        ret.append(f'{e.get_attribute(locator.attribute)}')
                    return ret if len(ret) > 1 else ret[0]
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.debug(f"Error in get_attribute(): {pprint(locator, text_color='YELLOW', bg_color='BLACK')}\\n", ex, False)
                    return
            # Код получает атрибут из веб-элемента
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
        :param locator: Локатор для поиска веб-элемента.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания.
        :type timeout: Optional[float]
        :param timeout_for_event: Условие ожидания.
        :type timeout_for_event: Optional[str]
        :return: Найденный веб-элемент или список элементов, или None, если ничего не найдено.
        :rtype: WebElement | List[WebElement] | None
        .. :todo:
            Продумать как передать `timeout_for_event`
        """
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
            web_elements: WebElement | List[WebElement],
            locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрует список веб-элементов в соответствии с правилом, указанным в `locator.if_list`.

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
            raise ValueError('Некорректный локатор.')
            ...

        web_elements = None
        try:
            # Если timeout = 0, то сразу выполняется поиск элемента без ожидания
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

            # Код возвращает результат работы функции `_parse_elements_list`
            return await _parse_elements_list(web_elements, locator)
        except TimeoutException as ex:
            if MODE in ('dev', 'debug'):
                logger.error(f'Таймаут для локатора: {locator}', ex, False)
                ...
            return None
        except Exception as ex:
            if MODE in ('dev', 'debug'):
                logger.error(f'Ошибка локатора: {locator}', ex, False)
                ...
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
        Делает скриншот найденного веб-элемента.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания появления элемента.
        :type timeout: float
        :param timeout_for_event: Тип условия ожидания.
        :type timeout_for_event: str
        :param message: Сообщение для отправки элементу.
        :type message: Optional[str]
        :param typing_speed: Скорость печати для событий отправки сообщения.
        :type typing_speed: float
        :param continue_on_error: Продолжать ли выполнение при ошибке.
        :type continue_on_error: bool
        :param webelement: Предварительно полученный веб-элемент.
        :type webelement: Optional[WebElement]
        :return: Бинарный поток скриншота или None в случае ошибки.
        :rtype: BinaryIO | None
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        # Код получает веб-элемент, если он не передан
        if not webelement:
            webelement = await self.get_webelement_by_locator(locator = locator, timeout = timeout, timeout_for_event = timeout_for_event)

        if not webelement:
            return

        try:
            # Код получает скриншот веб-элемента в виде бинарного потока
            screenshot_stream = webelement.screenshot_as_png
            return screenshot_stream
        except Exception as ex:
            logger.error(f"Не удалось захватить скриншот\\n", ex)
            ...
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

        :param locator: Локатор, определяющий элемент и событие для выполнения.
        :type locator: SimpleNamespace | dict
        :param timeout: Время ожидания для поиска элемента.
        :type timeout: float
        :param timeout_for_event: Условие ожидания для события.
        :type timeout_for_event: str
        :param message: Сообщение для отправки с событием.
        :type message: Optional[str]
        :param typing_speed: Скорость печати для событий send_keys.
        :type typing_speed: float
        :return: True, если выполнение события прошло успешно, False в противном случае.
        :rtype: str | list[str] | bytes | list[bytes] | bool
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )
        events = str(locator.event).split(";")
        result: list = []
        # Код получает веб-элемент по локатору
        webelement = await self.get_webelement_by_locator(
            locator,
            timeout,
            timeout_for_event
        )

        if not webelement:
            return False
        # Код выбирает первый элемент из списка, если получен список веб-элементов
        webelement = webelement[0] if isinstance(webelement, list) else webelement

        for event in events:
            if event == "click()":
                try:
                    # Код выполняет клик по веб-элементу
                    webelement.click()
                    # await asyncio.to_thread(webelement.click)
                    # result.append(True)
                    continue
                except ElementClickInterceptedException as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Element click intercepted:  {locator=}\\n", ex, False)
                        ...
                    return
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Element click intercepted: {locator=}\\n", ex, False)
                        ...
                    return

            elif event.startswith("pause("):
                # Код извлекает длительность паузы из строки события
                match = re.match(r"pause\\((\\d+)\\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                if MODE in ('dev','debug'):
                    logger.debug(f"Должна быть пауза, но что-то не срослось: {locator=}\\n")
                    ...
                return False

            elif event == "upload_media()":
                if not message:
                    if MODE in ('dev','debug'):
                        logger.debug(f"Message is required for upload_media event. Message: {pprint(message, text_color='WHITE',bg_color='RED')}", None, False)
                    return False
                try:
                    # Код отправляет сообщение в веб-элемент (используется для загрузки файлов)
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.debug(f"Error uploading media: {message=}", ex, False)
                        ...
                    return False

            elif event == "screenshot()":
                try:
                    # Код делает скриншот веб-элемента
                    result.append(await self.get_webelement_as_screenshot(locator, webelement=webelement))
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Error taking screenshot: {locator=}", ex, False)
                        ...
                    return False

            elif event == "clear()":
                try:
                    # Код очищает веб-элемент
                    await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Error clearing element: {locator=}", ex, False)
                    return False

            elif event.startswith("send_keys("):
                # Код извлекает клавиши для отправки из строки события
                keys_to_send = event.replace("send_keys(", "").replace(")", "").split("+")
                try:
                    actions = ActionChains(self.driver)
                    for key in keys_to_send:
                        key = key.strip().strip("\'")
                        if hasattr(Keys, key):
                            key_to_send = getattr(Keys, key)
                            actions.send_keys(key_to_send)
                    # Код выполняет отправку клавиш
                    await asyncio.to_thread(actions.perform)
                except Exception as ex:
                    if MODE in ('dev','debug'):
                        logger.error(f"Error sending keys: {locator=}", ex, False)
                    return False

            elif event.startswith("type("):
                # Код извлекает сообщение для ввода из строки события
                message = event.replace("type(", "").replace(")", "")
                if typing_speed:
                    for character in message:
                        # Код вводит сообщение посимвольно с заданной скоростью
                        await asyncio.to_thread(webelement.send_keys, character)
                        await asyncio.sleep(typing_speed)
                else:
                    # Код вводит сообщение целиком
                    await asyncio.to_thread(webelement.send_keys, message)
        # Код возвращает результат выполнения событий
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
        Отправляет сообщение в веб-элемент.

        :param locator: Информация о местоположении элемента на странице.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки в веб-элемент.
        :type message: Optional[str]
        :param typing_speed: Скорость печати сообщения в секундах.
        :type typing_speed: float
        :return: True, если сообщение было успешно отправлено, False в противном случае.
        :rtype: bool

        Пример:
            >>> driver = Driver()
            >>> driver.send_message(locator={"id": "messageBox"}, message="Hello World", typing_speed=0.1)
            True
        """
        ...

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
            Печатает сообщение в веб-элемент с заданной скоростью печати.

            :param el: Веб-элемент, в который нужно ввести сообщение.
            :type el: WebElement
            :param message: Сообщение для ввода.
            :type message: str
            :param replace_dict: Словарь для замены символов в сообщении.
            :type replace_dict: dict
            :param typing_speed: Скорость печати сообщения в секундах.
            :type typing_speed: float
            :return: True, если сообщение было успешно введено, False в противном случае.
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
                            """ TODO:
                                делать проверку в словаре подмен """
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
                    if MODE in ('dev','debug'):
                        logger.error(f"Error typing message\\n{message=}\\n{word=}\\n{letter=}\\n", ex)
                    ...
                    continue  # <- если была ошибка в передаче буквы - пока игнорую ёё
                    """ TODO:
                        Установить обработчик ошибок """
            return True

        ...
        # Код получает веб-элемент по локатору
        webelement = await self.get_webelement_by_locator(locator = locator, timeout =  timeout, timeout_for_event = timeout_for_event)
        if not webelement or (isinstance(webelement, list) and len(webelement) == 0):
            return
        # Код выбирает первый элемент из списка, если получен список веб-элементов
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

## Внесённые изменения

1.  **Документация модуля**:
    *   Добавлено подробное описание модуля в формате reStructuredText (RST), включая цели модуля, основные функции и принципы работы.

2.  **Документация класса `ExecuteLocator`**:
    *   Добавлены docstring для класса `ExecuteLocator` с описанием параметров.
    *   Добавлены docstring для методов `__post_init__`, `