### Анализ кода модуля `executor`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код структурирован, используются асинхронные операции для эффективного взаимодействия с Playwright.
    - Присутствует базовая документация в виде docstring, описывающая назначение классов и методов.
    - Используется `SimpleNamespace` для более удобного доступа к атрибутам.
    - Логирование ошибок реализовано через `logger.error` и `logger.debug`, что помогает при отладке.
- **Минусы**:
    - Не везде используется `j_loads_ns` для загрузки конфигураций.
    - Некоторые docstring требуют доработки в соответствии с RST.
    - Излишнее использование `try-except` блоков, что может затруднить чтение кода.
    - Код нуждается в рефакторинге для большей читаемости и соответствия PEP8.
    - Отсутствует обработка ошибок в методе `send_message`.

**Рекомендации по улучшению**:

1.  **Документация**:
    - Привести docstring к стандарту RST, добавив описания параметров, типов возвращаемых значений, примеры использования и исключений.
    - Добавить описание модуля.

2.  **Импорты**:
    - Все импорты должны быть выровнены по алфавиту.
    - Импорт `logger` должен быть из `src.logger.logger import logger`.

3.  **Конфигурация**:
    - Использовать `j_loads_ns` для загрузки конфигурации из JSON файлов.

4.  **Обработка ошибок**:
    - Уменьшить использование try-except, заменяя на `logger.error` для логирования ошибок без перехвата.
    - Добавить обработку ошибок в `send_message` и других методах.

5.  **Форматирование**:
    - Привести код в соответствие со стандартами PEP8, уделив внимание выравниванию и пробелам.
    - Использовать одинарные кавычки `'` для строк, двойные `"` только в `print, input, logger`.

6.  **Рефакторинг**:
    - Улучшить читаемость, разбив сложные функции на более мелкие и понятные.

7. **`execute_locator`**:
    - Использовать `all([locator.event, locator.attribute, locator.mandatory]) is None` -> `not any([locator.event, locator.attribute, locator.mandatory])`.
    - Убрать лишний `return` в `try`

8.  **Комментарии**:
    - Использовать более описательные комментарии в коде.

**Оптимизированный код**:

```python
# /src/webdriver/playwright/executor.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Модуль для управления браузером с использованием Playwright.
============================================================

Модуль предоставляет класс :class:`PlaywrightExecutor`, который
используется для управления браузером через Playwright. Он поддерживает
различные типы браузеров и выполняет действия, такие как навигация, ввод
текста, клики и получение атрибутов элементов.

Пример использования:
---------------------
.. code-block:: python

    executor = PlaywrightExecutor(browser_type='chromium')
    await executor.start()
    await executor.goto('https://example.com')
    element = await executor.execute_locator({'by': 'css', 'selector': 'h1'})
    print(element)
    await executor.stop()
"""
import asyncio
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from playwright.async_api import Locator, Page, async_playwright
from types import SimpleNamespace

from src import gs
from src.logger.logger import logger  # Исправлен импорт logger
from src.utils.jjson import j_loads_ns
from src.logger.exceptions import WebDriverException


class PlaywrightExecutor:
    """
    Выполняет команды на основе локаторов в стиле executor, используя Playwright.
    """

    def __init__(self, browser_type: str = 'chromium', **kwargs) -> None:
        """
        Инициализирует экземпляр PlaywrightExecutor.

        :param browser_type: Тип запускаемого браузера (например, 'chromium', 'firefox', 'webkit').
        :type browser_type: str
        :param kwargs: Дополнительные параметры конфигурации.
        :type kwargs: dict
        """
        self.driver = None
        self.browser_type = browser_type
        self.page: Optional[Page] = None
        self.config: SimpleNamespace = j_loads_ns(
            Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        )  # Используем j_loads_ns

    async def start(self) -> None:
        """
        Запускает Playwright и открывает браузер.
        """
        try:
            self.driver = await async_playwright().start()
            browser = await getattr(self.driver, self.browser_type).launch(
                headless=True, args=self.config.options
            )
            self.page = await browser.new_page()
        except Exception as ex:
            logger.critical('Playwright failed to start browser', ex)  # Используем logger.critical

    async def stop(self) -> None:
        """
        Закрывает браузер и останавливает Playwright.
        """
        try:
            if self.page:
                await self.page.close()
            if self.driver:
                await self.driver.stop()
                self.driver = None
            logger.info('Playwright stopped')  # Используем logger.info
        except Exception as ex:
            logger.error(f'Playwright failed to close browser: {ex}')  # Используем logger.error

    async def execute_locator(
        self,
        locator: dict | SimpleNamespace,
        message: Optional[str] = None,
        typing_speed: float = 0,
    ) -> str | List[str] | dict | bytes | bool | None:
        """
        Выполняет действия, указанные в локаторе.

        :param locator: Локатор элемента (словарь или SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки (если применимо).
        :type message: Optional[str]
        :param typing_speed: Скорость печати (если применимо).
        :type typing_speed: float
        :returns: Результат выполнения действия.
        :rtype: str | List[str] | dict | bytes | bool | None
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
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )

        if not locator or (not locator.attribute and not locator.selector):  # Проверка на None и обязательные поля
            return None  # <- локатор - заглушка

        async def _parse_locator(
            locator: SimpleNamespace, message: Optional[str]
        ) -> str | List[str] | dict | bytes | bool | None:
            """
            Внутренняя функция для обработки локатора.

            :param locator: Локатор элемента (SimpleNamespace).
            :type locator: SimpleNamespace
            :param message: Сообщение для отправки (если применимо).
            :type message: Optional[str]
            :returns: Результат выполнения действия.
            :rtype: str | List[str] | dict | bytes | bool | None
            """
            if not any([locator.event, locator.attribute, locator.mandatory]): # Проверка наличия event, attribute или mandatory
                return

            try:
                if locator.attribute:
                    locator.attribute = await self.evaluate_locator(locator.attribute)
                    """Я могу установить константное или формульное значение в аттрибут локатора и забирать его при условии {'by':'VALUE'}"""
                    if locator.by == 'VALUE':
                        return locator.attribute
            except Exception as ex:
                logger.debug(f'Locator Error: {locator=}')
                return

            if locator.event:
                return await self.execute_event(locator, message, typing_speed)
            if locator.attribute:
                return await self.get_attribute_by_locator(locator)
            return await self.get_webelement_by_locator(locator)

        return await _parse_locator(locator, message)

    async def evaluate_locator(
        self, attribute: str | List[str] | dict
    ) -> Optional[str | List[str] | dict]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param attribute: Атрибуты для оценки.
        :type attribute: str | List[str] | dict
        :returns: Оцененные атрибуты.
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
            Внутренняя функция для оценки одного атрибута.
            
            :param attr: Атрибут для оценки.
            :type attr: str
            :returns: Оцененный атрибут.
            :rtype: Optional[str]
            """
            return attr  # Playwright не использует Key
            # return getattr(Keys, re.findall(r"%(\\w+)%", attr)[0], None) if re.match(r"^%\\w+%", attr) else attr

        if isinstance(attribute, list):
            return await asyncio.gather(*[_evaluate(attr) for attr in attribute])
        return await _evaluate(str(attribute))

    async def get_attribute_by_locator(
        self, locator: dict | SimpleNamespace
    ) -> Optional[str | List[str] | dict]:
        """
        Получает атрибут элемента по локатору.

        :param locator: Локатор элемента.
        :type locator: dict | SimpleNamespace
        :returns: Значение атрибута или None.
        :rtype: Optional[str | List[str] | dict]
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )
        element = await self.get_webelement_by_locator(locator)

        if not element:
            logger.debug(f'Element not found: {locator=}')  # Используем logger.debug
            return None

        def _parse_dict_string(attr_string: str) -> dict | None:
            """
            Разбирает строку типа '{attr1:attr2}' в словарь.

            :param attr_string: Строка, представляющая структуру словаря.
            :type attr_string: str
            :returns: Словарь или None в случае ошибки.
            :rtype: dict | None
            """
            try:
                return {
                    k.strip(): v.strip()
                    for k, v in (pair.split(':') for pair in attr_string.strip('{}').split(','))
                }
            except ValueError as ex:
                logger.debug(f'Invalid attribute string format: {attr_string}\\n{ex}')  # Используем logger.debug
                return None

        async def _get_attribute(el: Locator, attr: str) -> Optional[str]:
            """
            Получает значение атрибута элемента.

            :param el: Элемент для получения атрибута.
            :type el: Locator
            :param attr: Имя атрибута.
            :type attr: str
            :returns: Значение атрибута или None в случае ошибки.
            :rtype: Optional[str]
            """
            try:
                return await el.get_attribute(attr)
            except Exception as ex:
                logger.debug(f'Error getting attribute \'{attr}\' from element: {ex}')  # Используем logger.debug
                return None

        async def _get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict:
            """
            Получает несколько атрибутов из элемента на основе словаря.

            :param element: Элемент для получения атрибутов.
            :type element: Locator
            :param attr_dict: Словарь с ключами и значениями, представляющими имена атрибутов.
            :type attr_dict: dict
            :returns: Словарь с полученными атрибутами.
            :rtype: dict
            """
            result = {}
            for key, value in attr_dict.items():
                result[key] = await _get_attribute(element, key)
                result[value] = await _get_attribute(element, value)

            return result

        if isinstance(locator.attribute, str) and locator.attribute.startswith('{'):
            attr_dict = _parse_dict_string(locator.attribute)
            if attr_dict:
                if isinstance(element, list):
                    return await asyncio.gather(
                        *[_get_attributes_from_dict(el, attr_dict) for el in element]
                    )
                return await _get_attributes_from_dict(element, attr_dict)

        if isinstance(element, list):
            return await asyncio.gather(*[_get_attribute(el, locator.attribute) for el in element])

        return await _get_attribute(element, locator.attribute)

    async def get_webelement_by_locator(
        self, locator: dict | SimpleNamespace
    ) -> Optional[Locator | List[Locator]]:
        """
        Получает веб-элемент по локатору.

        :param locator: Локатор элемента (словарь или SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :returns: Элемент Playwright Locator.
        :rtype: Optional[Locator | List[Locator]]
        """
        locator = (
            SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else locator
        )
        if not locator:
           raise ValueError('Некорректный локатор.')

        try:
            if locator.by.upper() == 'XPATH':
                elements = self.page.locator(f'xpath={locator.selector}')
            else:
                elements = self.page.locator(locator.selector)
            if locator.if_list == 'all':
                return await elements.all()
            elif locator.if_list == 'first':
                return elements.first
            elif locator.if_list == 'last':
                return elements.last
            elif locator.if_list == 'even':
                list_elements = await elements.all()
                return [list_elements[i] for i in range(0, len(list_elements), 2)]
            elif locator.if_list == 'odd':
                list_elements = await elements.all()
                return [list_elements[i] for i in range(1, len(list_elements), 2)]
            elif isinstance(locator.if_list, list):
                list_elements = await elements.all()
                return [list_elements[i] for i in locator.if_list]
            elif isinstance(locator.if_list, int):
                list_elements = await elements.all()
                return list_elements[locator.if_list - 1]
            else:
                return elements
        except Exception as ex:
            logger.error(f'Ошибка поиска элемента: {locator=} \\n {ex}', ex, False)
            return None

    async def get_webelement_as_screenshot(
        self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None
    ) -> Optional[bytes]:
        """
        Делает скриншот веб-элемента.

        :param locator: Локатор элемента (словарь или SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param webelement: Локатор веб-элемента.
        :type webelement: Optional[Locator]
        :returns: Скриншот в виде байтов или None.
        :rtype: Optional[bytes]
        """
        locator = (
           locator if isinstance(locator, SimpleNamespace) else SimpleNamespace(**locator) if isinstance(locator,dict) else None
        )

        if not webelement:
            webelement = await self.get_webelement_by_locator(locator)

        if not webelement:
            logger.debug(f'Не найден элемент для screenshot: {locator=}')  # Используем logger.debug
            return

        try:
            screenshot_bytes = await webelement.screenshot()
            return screenshot_bytes
        except Exception as ex:
            logger.error('Не удалось захватить скриншот', ex)  # Используем logger.error
            return

    async def execute_event(
        self,
        locator: dict | SimpleNamespace,
        message: Optional[str] = None,
        typing_speed: float = 0,
    ) -> str | List[str] | bytes | List[bytes] | bool:
        """
        Выполняет событие, связанное с локатором.

        :param locator: Локатор элемента (словарь или SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для события (если применимо).
        :type message: Optional[str]
        :param typing_speed: Скорость печати (если применимо).
        :type typing_speed: float
        :returns: Результат выполнения события.
        :rtype: str | List[str] | bytes | List[bytes] | bool
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(**locator)
            if isinstance(locator, dict)
            else None
        )
        events = str(locator.event).split(';')
        result: list = []
        element = await self.get_webelement_by_locator(locator)
        if not element:
            logger.debug(f'Element for event not found: {locator=}')  # Используем logger.debug
            return False

        element = element[0] if isinstance(element, list) else element

        for event in events:
            if event == 'click()':
                try:
                    await element.click()
                    continue
                except Exception as ex:
                    logger.error(f'Ошибка при клике: {ex}\\n {locator=}')  # Используем logger.error
                    return False

            elif event.startswith('pause('):
                match = re.match(r'pause\\((\\d+)\\)', event)
                if match:
                    pause_duration = int(match.group(1))
                    await asyncio.sleep(pause_duration)
                    continue
                logger.debug(f'Должна быть пауза, но что-то не срослось: {locator=}')  # Используем logger.debug
                return False

            elif event == 'upload_media()':
                if not message:
                    logger.debug(f'Message is required for upload_media event. {message=}')  # Используем logger.debug
                    return False
                try:
                    await element.set_input_files(message)  # работает в input type file
                    continue
                except Exception as ex:
                    logger.error(f'Ошибка загрузки файла: {ex}\\n {locator=}')  # Используем logger.error
                    return False

            elif event == 'screenshot()':
                try:
                    result.append(
                        await self.get_webelement_as_screenshot(locator, webelement=element)
                    )
                except Exception as ex:
                    logger.error(f'Ошибка при захвате скриншота: {ex}\\n {locator=}')  # Используем logger.error
                    return False

            elif event == 'clear()':
                try:
                    await element.clear()
                    continue
                except Exception as ex:
                    logger.error(f'Ошибка при очистке поля: {ex}\\n {locator=}')  # Используем logger.error
                    return False

            elif event.startswith('send_keys('):
                keys_to_send = event.replace('send_keys(', '').replace(')', '').split('+')
                try:
                    for key in keys_to_send:
                        key = key.strip().strip("'")
                        if key:
                            await element.type(key)
                except Exception as ex:
                    logger.error(f'Ошибка при отправке клавиш: {ex}\\n {locator=}')  # Используем logger.error
                    return False

            elif event.startswith('type('):
                message = event.replace('type(', '').replace(')', '')
                if typing_speed:
                    for character in message:
                        await element.type(character)
                        await asyncio.sleep(typing_speed)
                else:
                    await element.type(message)
        return result if result else True

    async def send_message(
        self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0
    ) -> bool:
        """
        Отправляет сообщение в веб-элемент.

        :param locator: Локатор элемента (словарь или SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки.
        :type message: str
        :param typing_speed: Скорость печати.
        :type typing_speed: float
        :returns: `True`, если сообщение отправлено успешно, `False` иначе.
        :rtype: bool
        """
        locator = (
            locator
            if isinstance(locator, SimpleNamespace)
            else SimpleNamespace(locator)
        )
        element = await self.get_webelement_by_locator(locator)
        if not element or (isinstance(element, list) and len(element) == 0):
            logger.debug(f"Элемент не найден: {locator=}") # Используем logger.debug
            return False
        element = element[0] if isinstance(element, list) else element

        try:
            if typing_speed:
                for character in message:
                    await element.type(character)
                    await asyncio.sleep(typing_speed)
            else:
                await element.type(message)
            return True
        except Exception as ex:
            logger.error(f"Ошибка при отправке сообщения: {ex}\\n{locator=}")
            return False

    async def goto(self, url: str) -> None:
        """
        Переходит по указанному URL.

        :param url: URL для перехода.
        :type url: str
        """
        if self.page:
            try:
                await self.page.goto(url)
            except Exception as ex:
                logger.error(f'Error navigation {url=}\\n {ex}')  # Используем logger.error