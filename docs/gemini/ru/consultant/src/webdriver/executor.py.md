# Анализ кода модуля `executor.py`

**Качество кода**
7
-  Плюсы
    - Код разбит на логические блоки с использованием классов и методов.
    - Используется асинхронное программирование для неблокирующих операций.
    - Присутствует обработка исключений для более стабильной работы.
    - Используются `dataclass` для представления данных.
    - Наличие mermaid диаграмм в docstring
-  Минусы
    -   Смешанный стиль комментариев (не везде RST).
    -   Не полное использование логгера.
    -   Избыточное использование `try-except` блоков.
    -   Не всегда понятные и полные docstring.
    -   Использование `...` для заглушек.
    -   Смешанное использование `logger.debug` и `logger.error`
    -   Отсутствует единый стиль обработки исключений.
    -   Множественные вложенные условия, делающие код сложным для понимания.
    -   Не везде используется `j_loads` или `j_loads_ns`.
    -   Много неиспользуемого или закомментированного кода
    -   Плохая читаемость кода в блоке `send_message`
    -   Не полное соответствие с PEP8

**Рекомендации по улучшению**

1.  **Документация**:
    -   Полностью переписать комментарии в формате RST.
    -   Добавить подробные docstring к каждой функции, методу и классу.
    -   Использовать rst-блоки для mermaid
    -   Указать типы данных для параметров функций и возвращаемых значений.

2.  **Логирование**:
    -   Использовать `logger.error` для записи ошибок, а `logger.debug` для отладочной информации.
    -   Использовать форматирование строк f-string.
    -   Добавить контекст в сообщения логгера, чтобы облегчить отладку.
    -   Использовать один стиль логгирования

3.  **Обработка ошибок**:
    -   Убрать лишние блоки `try-except` и использовать `logger.error` для записи исключений.
    -   Удалить или заменить `...` на конкретные действия.
    -   Обработка ошибок должна быть единообразной

4.  **Код**:
    -   Удалить неиспользуемый код и закомментированный код.
    -   Упростить логику в функциях, разбив их на более мелкие и понятные.
    -   Пересмотреть условные конструкции, избегать излишней вложенности
    -   Привести код в соответствие с PEP8
    -   Перенести импорты в начало файла и сгруппировать их по категориям.
    -   Избегать повторений в коде, вынося общие части в отдельные функции.
    -   Улучшить читаемость `send_message`

5.  **Использование `j_loads`**:
    -   Использовать `j_loads` или `j_loads_ns` для чтения файлов конфигурации или других JSON-подобных данных.
    -   Убедиться, что все данные, которые должны быть прочитаны, обрабатываются с использованием `j_loads`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль `executor` предназначен для выполнения действий с веб-элементами на основе предоставленных конфигураций,
известных как "локаторы". Эти конфигурации представляют собой словари, содержащие информацию о том,
как находить и взаимодействовать с элементами на веб-странице.

Модуль предоставляет следующие функциональные возможности:

1. **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`,
   что обеспечивает гибкую работу с данными локатора.

2. **Взаимодействие с веб-элементами**: В зависимости от предоставленных данных, модуль выполняет различные действия,
   такие как клики, отправка сообщений, выполнение событий и получение атрибутов веб-элементов.

3. **Обработка ошибок**: Модуль поддерживает продолжение выполнения в случае ошибки, позволяя обрабатывать веб-страницы,
   которые могут содержать нестабильные элементы.

4. **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы,
   обеспечивая идентификацию и взаимодействие с одним или несколькими веб-элементами одновременно.

Этот модуль обеспечивает гибкость и универсальность при работе с веб-элементами,
позволяя автоматизировать сложные сценарии веб-взаимодействия.

"""

import asyncio
import re
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

from src import gs
from src.logger.exceptions import (
    DefaultSettingsException,
    ExecuteLocatorException,
    WebDriverException,
)
from src.logger.logger import logger
from src.utils.image import save_png
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint




@dataclass
class ExecuteLocator:
    """
    Класс-обработчик локаторов веб-элементов с использованием Selenium.

    :param driver: Экземпляр веб-драйвера Selenium.
    :type driver: Optional[object]
    :param actions: Объект для выполнения цепочки действий.
    :type actions: ActionChains
    :param by_mapping: Словарь соответствия строк методам поиска элементов.
    :type by_mapping: dict
    :param mode: Режим работы ('debug', 'dev' и т.д.).
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
        :param message: Сообщение для отправки (опционально).
        :type message: Optional[str]
        :param typing_speed: Скорость печати для событий send_keys (опционально).
        :type typing_speed: Optional[float]
        :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение при ошибке.
        :type continue_on_error: Optional[bool]
        :raises ExecuteLocatorException: Если возникает ошибка при выполнении локатора.
        :return: Результат выполнения действий с локатором.
        :rtype: str | list | dict | WebElement | bool

        ```mermaid
                graph TD
            A[Начало] --> B[Проверка типа локатора]
            B --> C{Локатор SimpleNamespace?}
            C -->|Да| D[Использовать локатор]
            C -->|Нет| E[Преобразовать в SimpleNamespace]
            E --> D
            D --> F[Определение async _parse_locator]
            F --> G[Проверка наличия event, attribute, mandatory]
            G -->|Нет| H[Вернуть None]
            G -->|Да| I[Попытка сопоставить by и вычислить attribute]
            I --> J[Перехват ошибок и запись в лог]
            J --> K{Есть event?}
            K -->|Да| L[Выполнить event]
            K -->|Нет| M{Есть attribute?}
            M -->|Да| N[Получить attribute по локатору]
            M -->|Нет| O[Получить веб-элемент по локатору]
            L --> P[Вернуть результат event]
            N --> P[Вернуть результат attribute]
            O --> P[Вернуть веб-элемент]
            P --> Q[Вернуть результат _parse_locator]
            Q --> R[Вернуть результат execute_locator]
            R --> S[Конец]
        ```
        """
        # Преобразование локатора в SimpleNamespace, если это словарь
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        if not locator or (not locator.attribute and not locator.selector):
            return None  # Локатор-заглушка

        async def _parse_locator(
                locator: Union[dict, SimpleNamespace], message: Optional[str]
        ) -> str | list | dict | WebElement | bool:
            """
            Разбирает и выполняет инструкции локатора.

            :param locator: Данные локатора.
            :type locator: Union[dict, SimpleNamespace]
            :param message: Сообщение для отправки (если применимо).
            :type message: Optional[str]
            :raises ExecuteLocatorException: В случае ошибки при выполнении локатора
            :return: Результат выполнения инструкций локатора.
            :rtype: str | list | dict | WebElement | bool
            """
            locator = (
                locator if isinstance(locator, SimpleNamespace)
                else SimpleNamespace(**locator)
            )
            if all([locator.event, locator.attribute, locator.mandatory]) is None:
                return

            try:
                locator.by = self.by_mapping.get(locator.by.upper(), locator.by)
                if locator.attribute:
                    locator.attribute = await self.evaluate_locator(locator.attribute)
                    #  Установка константного или формульного значения в аттрибут локатора
                    if locator.by == 'VALUE':
                        return locator.attribute

            except Exception as ex:
                if MODE in ('dev', 'debug'):
                    logger.debug(f"Ошибка при обработке локатора: {locator=}, {ex}", )
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
            A[Начало] --> B[Проверка типа атрибута]
            B -->|Список| C[Итерация по каждому атрибуту в списке]
            C --> D[Вызов _evaluate для каждого атрибута]
            D --> E[Возврат результатов asyncio.gather]
            B -->|Нет| F[Вызов _evaluate для одного атрибута]
            F --> G[Возврат результата _evaluate]
            G --> H[Конец]
            E --> H
        ```
        """

        async def _evaluate(attr: str) -> Optional[str]:
            """
            Вычисляет значение атрибута.

            :param attr: Строка атрибута.
            :type attr: str
            :return: Вычисленное значение атрибута.
            :rtype: Optional[str]
            """
            if re.match(r"^%\w+%", attr):
                key = re.findall(r"%(\w+)%", attr)[0]
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
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: dict | SimpleNamespace
        :param timeout: Максимальное время ожидания появления элемента (по умолчанию 5 секунд).
        :type timeout: Optional[float]
        :param timeout_for_event: Тип условия ожидания (по умолчанию 'presence_of_element_located').
        :type timeout_for_event: str
        :raises ExecuteLocatorException: Если возникает ошибка при извлечении атрибутов.
        :return: Значение атрибута(ов) или словарь с атрибутами.
        :rtype: Union[str, list, dict, WebElement | list[WebElement] | None]

        ```mermaid
                graph TD
            A[Начало] --> B[Проверка типа локатора]
            B -->|Да| C[Преобразовать в SimpleNamespace если нужно]
            C --> D[Вызвать get_webelement_by_locator]
            D --> E[Проверка наличия web_element]
            E -->|Нет| F[Записать debug-сообщение и вернуть None]
            E -->|Да| G[Проверка является ли locator.attribute строкой-словарем]
            G -->|Да| H[Разобрать строку locator.attribute в словарь]
            H --> I[Проверка является ли web_element списком]
            I -->|Да| J[Получить атрибуты для каждого элемента]
            J --> K[Вернуть список атрибутов]
            I -->|Нет| L[Получить атрибуты для одного web_element]
            L --> K
            G -->|Нет| M[Проверка является ли web_element списком]
            M -->|Да| N[Получить атрибуты для каждого элемента в списке]
            N --> O[Вернуть список атрибутов или один атрибут]
            M -->|Нет| P[Получить атрибут для одного web_element]
            P --> O
            O --> Q[Конец]
            F --> Q
        ```
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        web_element: WebElement = await self.get_webelement_by_locator(locator, timeout, timeout_for_event)
        if not web_element:
            if MODE in ('dev', 'debug'):
                logger.debug(f"Элемент не найден: {locator=}", )
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
                    logger.debug(f"Неверный формат строки атрибутов: {pprint(attr_string, text_color='WHITE', bg_color='RED')}, {ex}")
                return
            except Exception as ex:
                if MODE in ('dev', 'debug'):
                   logger.debug(f"Неверный формат строки атрибутов: {pprint(attr_string, text_color='WHITE', bg_color='RED')}, {ex}")
                return

        def _get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict:
            """
            Извлекает значения атрибутов для каждого ключа в заданном словаре.

            :param element: Веб-элемент, из которого нужно извлечь атрибуты.
            :type element: WebElement
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
                        logger.debug(f"Ошибка при получении атрибутов '{key}' или '{value}' из элемента, {ex}")
                    return
            return result

        if web_element:
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
                        logger.debug(f"Ошибка в get_attribute(): {pprint(locator, text_color='YELLOW', bg_color='BLACK')}, {ex}")
                    return
            return web_element.get_attribute(locator.attribute)
        return None

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
        :param timeout_for_event: Условие ожидания ('presence_of_element_located', 'element_to_be_clickable').
        :type timeout_for_event: Optional[str]
        :raises ValueError: Если передан некорректный локатор.
        :return: Найденный веб-элемент или список элементов.
        :rtype: WebElement | List[WebElement] | None
        """
        timeout = timeout if timeout > 0 else locator.timeout

        async def _parse_elements_list(
                web_elements: WebElement | List[WebElement],
                locator: SimpleNamespace
        ) -> WebElement | List[WebElement]:
            """
            Фильтрует веб-элементы по правилу, указанному в `locator.if_list`.

            :param web_elements: Список веб-элементов.
            :type web_elements: WebElement | List[WebElement]
            :param locator: Локатор с правилами фильтрации.
            :type locator: SimpleNamespace
            :return: Отфильтрованный веб-элемент или список элементов.
            :rtype: WebElement | List[WebElement]
            """
            if not isinstance(web_elements, list):
                return web_elements

            if_list = locator.if_list

            if if_list == 'all':
                return web_elements
            if if_list == 'first':
                return web_elements[0]
            if if_list == 'last':
                return web_elements[-1]
            if if_list == 'even':
                return [web_elements[i] for i in range(0, len(web_elements), 2)]
            if if_list == 'odd':
                return [web_elements[i] for i in range(1, len(web_elements), 2)]
            if isinstance(if_list, list):
                return [web_elements[i] for i in if_list]
            if isinstance(if_list, int):
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
            raise ValueError('Некорректный локатор.')

        web_elements = None
        try:
            if timeout == 0:
                web_elements = driver.find_elements(locator.by, locator.selector)
            else:
                condition = (
                    EC.presence_of_all_elements_located
                    if timeout_for_event == 'presence_of_all_elements_located'
                    else EC.visibility_of_all_elements_located
                )

                web_elements = await asyncio.to_thread(
                    WebDriverWait(driver, timeout).until,
                    condition((locator.by, locator.selector))
                )
            return await _parse_elements_list(web_elements, locator)
        except TimeoutException as ex:
            if MODE in ('dev', 'debug'):
                logger.error(f'Таймаут при поиске локатора: {locator}, {ex}')
            return None
        except Exception as ex:
            if MODE in ('dev', 'debug'):
                logger.error(f'Ошибка при поиске локатора: {locator}, {ex}')
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
        Делает снимок экрана найденного веб-элемента.

        :param locator: Локатор элемента.
        :type locator: dict | SimpleNamespace
        :param timeout: Время ожидания.
        :type timeout: float
        :param timeout_for_event: Тип события для ожидания.
        :type timeout_for_event: str
        :param message: Сообщение для отправки.
        :type message: Optional[str]
        :param typing_speed: Скорость печати.
        :type typing_speed: float
        :param continue_on_error: Флаг для продолжения при ошибке.
        :type continue_on_error: bool
        :param webelement: Готовый веб-элемент (опционально).
        :type webelement: Optional[WebElement]
        :return: Снимок экрана в виде байтового потока или None.
        :rtype: BinaryIO | None
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator=locator, timeout=timeout,
                                                             timeout_for_event=timeout_for_event)

        if not webelement:
            return

        try:
            screenshot_stream = webelement.screenshot_as_png
            return screenshot_stream
        except Exception as ex:
            logger.error(f"Не удалось сделать скриншот, {ex}")
            return None

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

        :param locator: Локатор, указывающий элемент и событие для выполнения.
        :type locator: SimpleNamespace | dict
        :param timeout: Время ожидания для поиска элемента.
        :type timeout: float
        :param timeout_for_event: Время ожидания для события.
        :type timeout_for_event: str
        :param message: Сообщение для отправки с событием (если применимо).
        :type message: Optional[str]
        :param typing_speed: Скорость печати для событий send_keys.
        :type typing_speed: float
         :return: True в случае успешного выполнения, False в противном случае.
        :rtype: str | list[str] | bytes | list[bytes] | bool
        """
        locator = (
            locator if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator) if isinstance(locator, dict)
            else None
        )
        events = str(locator.event).split(";")
        result: list = []

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
                        logger.error(f"Клик перехвачен: {locator=}, {ex}")
                    return False
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка при клике: {locator=}, {ex}")
                    return False

            elif event.startswith("pause("):
                match = re.match(r"pause\((\d+)\)", event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    result.append(True)
                    continue
                if MODE in ('dev', 'debug'):
                    logger.debug(f"Некорректная пауза: {locator=}")
                return False

            elif event == "upload_media()":
                if not message:
                    if MODE in ('dev', 'debug'):
                        logger.debug(
                            f"Необходимо сообщение для upload_media: {pprint(message, text_color='WHITE',bg_color='RED')}")
                    return False
                try:
                    await asyncio.to_thread(webelement.send_keys, message)
                    result.append(True)
                    continue
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.debug(f"Ошибка при загрузке медиа: {message=}, {ex}")
                    return False

            elif event == "screenshot()":
                try:
                    result.append(await self.get_webelement_as_screenshot(locator, webelement=webelement))
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка при снятии скриншота: {locator=}, {ex}")
                    return False

            elif event == "clear()":
                try:
                   await asyncio.to_thread(webelement.clear)
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка при очистке элемента: {locator=}, {ex}")
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
                        logger.error(f"Ошибка при отправке клавиш: {locator=}, {ex}")
                    return False

            elif event.startswith("type("):
                message = event.replace("type(", "").replace(")", "")
                try:
                    if typing_speed:
                        for character in message:
                            await asyncio.to_thread(webelement.send_keys, character)
                            await asyncio.sleep(typing_speed)
                    else:
                        await asyncio.to_thread(webelement.send_keys, message)
                except Exception as ex:
                     if MODE in ('dev', 'debug'):
                         logger.error(f"Ошибка при вводе текста: {locator=}, {ex}")
                     return False

        return result if result else True

    async def send_message(self,
                        locator: SimpleNamespace | dict,
                        timeout: float = 5,
                        timeout_for_event: str = 'presence_of_element_located',
                        message: str = None,
                        typing_speed: float = 0,
                        continue_on_error: bool = True,

    ) -> bool:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Информация о расположении элемента на странице.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки.
        :type message: Optional[str]
        :param typing_speed: Скорость печати в секундах.
        :type typing_speed: float
        :return: True в случае успешной отправки, False в противном случае.
        :rtype: bool

        :Example:
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
            Печатает сообщение в веб-элемент с заданной скоростью.

            :param el: Веб-элемент для печати сообщения.
            :type el: WebElement
            :param message: Сообщение для печати.
            :type message: str
            :param replace_dict: Словарь замен символов.
            :type replace_dict: dict
            :param typing_speed: Скорость печати в секундах.
            :type typing_speed: float
            :return: True в случае успешной печати, False в противном случае.
            :rtype: bool
            :Example:
                >>> element = driver.get_element_by_id("messageBox")
                >>> driver.type_message(el=element, message="Hello World", typing_speed=0.1)
                True
            """

            message = message.split(" ")

            for word in message:
                word += " "
                try:
                    for letter in word:
                        if letter in replace_dict:
                            self.actions.key_down(Keys.SHIFT).send_keys(
                                Keys.ENTER
                            ).key_up(Keys.SHIFT)
                            self.actions.perform()

                        else:
                            self.actions.send_keys(letter)
                            self.actions.pause(typing_speed)
                            self.actions.perform()
                except Exception as ex:
                    if MODE in ('dev', 'debug'):
                        logger.error(f"Ошибка при вводе сообщения: {message=}, {word=}, {letter=}, {ex}")
                    continue
            return True

        webelement = await self.get_webelement_by_locator(locator = locator, timeout =  timeout, timeout_for_event = timeout_for_event)
        if not webelement or (isinstance(webelement, list) and not webelement):
            return False
        webelement = webelement[0] if isinstance(webelement, list) else webelement
        self.actions.move_to_element(webelement)
        type_message(
            el=we