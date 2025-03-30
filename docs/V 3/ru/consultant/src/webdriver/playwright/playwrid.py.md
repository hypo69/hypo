## Анализ кода модуля `playwrid.py`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование `PlaywrightCrawler` из библиотеки `crawlee`.
    - Класс хорошо структурирован и предоставляет удобные методы для взаимодействия с веб-страницами.
    - Использование `logger` для логирования.
    - Наличие примеров использования в блоке `if __name__ == "__main__":`.
    - Использование `SimpleNamespace` для конфигурирования.
- **Минусы**:
    - Не везде используется аннотация типов.
    - Не все методы и классы имеют подробные docstring.
    - Есть устаревшие комментарии.
    - Не используется `j_loads` или `j_loads_ns` для загрузки конфигурации.

**Рекомендации по улучшению:**

1.  **Документация**:
    - Добавить docstring для класса `Playwrid`, описывающий его основное назначение и функциональность.
    - Добавить аннотации типов для всех аргументов и возвращаемых значений функций.
    - Описать все атрибуты класса `Playwrid` в docstring класса.
2.  **Конфигурация**:
    - Использовать `j_loads_ns` для загрузки конфигурации из файла `playwrid.json`.
3.  **Логирование**:
    - Улучшить логирование ошибок, добавив `exc_info=True` для отображения трассировки стека.
4.  **Обработка исключений**:
    - Рассмотреть возможность добавления более специфичных блоков `except` для обработки различных типов исключений.
5.  **Удаление неиспользуемого кода**:
    - Удалить закомментированные строки кода, если они не несут полезной информации.
6. **Использовать одинарные кавычки**:
   - Заменить двойные кавычки на одинарные, где это необходимо.

**Оптимизированный код:**

```python
## \file /src/webdriver/playwright/playwrid.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для Playwright Crawler
==============================

Этот модуль определяет подкласс `PlaywrightCrawler` под названием `Playwrid`.
Он предоставляет дополнительные функции, такие как возможность установки пользовательских настроек браузера, профилей и параметров запуска с использованием Playwright.

Пример использования:

>>> if __name__ == '__main__':
...     browser = Playwrid(options=['--headless'])
...     browser.start('https://www.example.com')
"""
import asyncio
from pathlib import Path
from typing import Optional, Dict, Any, List
from types import SimpleNamespace

# from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext

import header
from header import __root__
from src import gs
from src.webdriver.playwright.executor import PlaywrightExecutor
from src.webdriver.js import JavaScript
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Playwrid(PlaywrightCrawler):
    """
    Подкласс `PlaywrightCrawler`, который предоставляет дополнительные функции.
    """

    driver_name: str = 'playwrid'
    base_path: Path = __root__ / 'src' / 'webdriver' / 'playwright'
    config: SimpleNamespace = j_loads_ns(base_path / 'playwrid.json')
    context = None

    def __init__(
        self,
        user_agent: Optional[str] = None,
        options: Optional[List[str]] = None,
        *args,
        **kwargs,
    ) -> None:
        """
        Инициализирует Playwright Crawler с указанными параметрами запуска, настройками и user agent.

        Args:
            user_agent (Optional[str]): User-agent для использования.
            options (Optional[List[str]]): Список опций Playwright для передачи во время инициализации.
        """
        launch_options = self._set_launch_options(user_agent, options)
        self.executor = PlaywrightExecutor()
        # Pass launch_options to PlaywrightCrawler if it accepts them
        # Otherwise, remove launch_options from the parameters
        super().__init__(
            browser_type=self.config.browser_type,
            # launch_options=launch_options,  # Remove or adjust if not accepted
            **kwargs,
        )
        # If PlaywrightCrawler does not accept launch_options, set them separately
        if hasattr(self, 'set_launch_options'):
            self.set_launch_options(launch_options)
        else:
            # Handle launch options differently if needed
            pass

    def _set_launch_options(
        self, user_agent: Optional[str] = None, options: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Конфигурирует параметры запуска для Playwright Crawler.

        Args:
            user_agent (Optional[str]): User-agent для использования.
            options (Optional[List[str]]): Список опций Playwright для передачи во время инициализации.

        Returns:
            Dict[str, Any]: Словарь с параметрами запуска для Playwright.
        """
        launch_options = {
            'headless': self.config.headless
            if hasattr(self.config, 'headless')
            else True,
            'args': self.config.options if hasattr(self.config, 'options') else [],
        }

        # Add custom user-agent if provided
        if user_agent:
            launch_options['user_agent'] = user_agent

        # Merge custom options with default options
        if options:
            launch_options['args'].extend(options)

        return launch_options

    async def start(self, url: str) -> None:
        """
        Запускает Playwrid Crawler и переходит по указанному URL.

        Args:
            url (str): URL для перехода.
        """
        try:
            logger.info(f'Starting Playwright Crawler for {url}')
            await self.executor.start()  # Start the executor
            await self.executor.goto(url)  # Goto url
            super().run(url)  # run crawler
            # получаем контекст
            self.context = self.crawling_context
        except Exception as ex:
            logger.critical('Playwrid Crawler failed with an error:', ex, exc_info=True)

    @property
    def current_url(self) -> Optional[str]:
        """
        Возвращает текущий URL браузера.

        Returns:
            Optional[str]: Текущий URL.
        """
        if self.context and self.context.page:
            return self.context.page.url
        return None

    def get_page_content(self) -> Optional[str]:
        """
        Возвращает HTML-содержимое текущей страницы.

        Returns:
            Optional[str]: HTML-содержимое страницы.
        """
        if self.context and self.context.page:
            return self.context.page.content()
        return None

    async def get_element_content(self, selector: str) -> Optional[str]:
        """
        Возвращает inner HTML-содержимое одного элемента на странице по CSS-селектору.

        Args:
            selector (str): CSS-селектор для элемента.

        Returns:
            Optional[str]: Inner HTML-содержимое элемента или None, если не найден.
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(selector)
                return await element.inner_html()
            except Exception as ex:
                logger.warning(
                    f'Element with selector \'{selector}\' not found or error during extraction: {ex}'
                )
                return None
        return None

    async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
        """
        Возвращает текстовое значение одного элемента на странице по XPath.

        Args:
            xpath (str): XPath элемента.

        Returns:
            Optional[str]: Текстовое значение элемента или None, если не найден.
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(f'xpath={xpath}')
                return await element.text_content()
            except Exception as ex:
                logger.warning(
                    f'Element with XPath \'{xpath}\' not found or error during extraction: {ex}'
                )
                return None
        return None

    async def click_element(self, selector: str) -> None:
        """
        Кликает на один элемент на странице по CSS-селектору.

        Args:
            selector (str): CSS-селектор элемента для клика.
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(selector)
                await element.click()
            except Exception as ex:
                logger.warning(
                    f'Element with selector \'{selector}\' not found or error during click: {ex}'
                )

    async def execute_locator(
        self,
        locator: dict | SimpleNamespace,
        message: Optional[str] = None,
        typing_speed: float = 0,
    ) -> str | List[str] | bytes | List[bytes] | bool:
        """
        Выполняет локатор через executor.

        Args:
            locator (dict | SimpleNamespace): Данные локатора.
            message (Optional[str]): Опциональное сообщение для событий.
            typing_speed (float): Опциональная скорость печати для событий.

        Returns:
            str | List[str] | bytes | List[bytes] | bool: Статус выполнения.
        """
        return await self.executor.execute_locator(locator, message, typing_speed)


if __name__ == '__main__':

    async def main():
        browser = Playwrid(options=['--headless'])
        await browser.start('https://www.example.com')

        # Получение HTML всего документа
        html_content = browser.get_page_content()
        if html_content:
            print(html_content[:200])  # Выведем первые 200 символов для примера
        else:
            print('Не удалось получить HTML-контент.')

        # Получение HTML элемента по селектору
        element_content = await browser.get_element_content('h1')
        if element_content:
            print('\nСодержимое элемента h1:')
            print(element_content)
        else:
            print('\nЭлемент h1 не найден.')

        # Получение значения элемента по xpath
        xpath_value = await browser.get_element_value_by_xpath('//head/title')
        if xpath_value:
            print(f'\nЗначение элемента по XPATH //head/title: {xpath_value}')
        else:
            print('\nЭлемент по XPATH //head/title не найден')

        # Нажатие на кнопку (при наличии)
        await browser.click_element('button')

        locator_name = {
            'attribute': 'innerText',
            'by': 'XPATH',
            'selector': '//h1',
            'if_list': 'first',
            'use_mouse': False,
            'timeout': 0,
            'timeout_for_event': 'presence_of_element_located',
            'event': None,
            'mandatory': True,
            'locator_description': 'Название товара',
        }

        name = await browser.execute_locator(locator_name)
        print('Name:', name)

        locator_click = {
            'attribute': None,
            'by': 'CSS',
            'selector': 'button',
            'if_list': 'first',
            'use_mouse': False,
            'timeout': 0,
            'timeout_for_event': 'presence_of_element_located',
            'event': 'click()',
            'mandatory': True,
            'locator_description': 'название товара',
        }
        await browser.execute_locator(locator_click)
        await asyncio.sleep(3)

    asyncio.run(main())