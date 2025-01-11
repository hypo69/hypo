# Анализ кода модуля `chrome`

## Качество кода
**Соответствие требованиям по оформлению кода: 8/10**
-   **Плюсы**
    -   Код хорошо структурирован и разбит на логические блоки.
    -   Используется `j_loads_ns` для загрузки JSON-конфигурации.
    -   Присутствует обработка исключений.
    -   Используется `logger` для логирования ошибок.
    -   Реализован паттерн Singleton для управления экземпляром WebDriver.
    -   Добавлены RST-комментарии для модуля и класса.
-   **Минусы**
    -   Не все функции и методы имеют docstring в формате RST.
    -   В некоторых местах отсутствует подробное описание функциональности.
    -   В `__init__` много логики, что снижает читаемость.
    -   Не все комментарии начинаются с заглавной буквы.
    -   Импорт `header` не используется.
    -   Использовано `vars()` для `self.config.headers`, что может быть менее явным.
    -   Потенциально избыточный блок `try-except` в `__init__`, можно заменить на обработку ошибок с помощью `logger.error`.

## Рекомендации по улучшению

1.  **Документация:**
    -   Добавить подробные RST-комментарии к методам `__new__`, `_payload`, `normalize_path`.
    -   Уточнить документацию по параметрам функций.
2.  **Улучшения:**
    -   Удалить неиспользуемый импорт `header`.
    -   В `__init__` вынести логику добавления аргументов и путей в отдельные методы, для улучшения читаемости.
    -   Использовать более явный доступ к атрибутам вместо `vars(self.config.headers).items()`.
    -   Избавиться от избыточных `try-except` в `__init__`, используя `logger.error` для обработки исключений.
    -   Добавить проверку на наличие `profile_directory` и `binary_location`, чтобы избежать ошибок.
    -   Упростить и сделать более явным код `if hasattr(self.config, 'options') and self.config.options` и `if hasattr(self.config, 'headers') and self.config.headers`.
3. **Форматирование:**
    -   Всегда использовать одинарные кавычки (`'`) для строк в коде, кроме строк для вывода в лог.
    -   Все комментарии после `#` должны начинаться с заглавной буквы и быть более подробными.

## Оптимизированный код

```python
# -*- coding: utf-8 -*-
# file: src/webdriver/chrome/chrome.py
#! venv/bin/python/python3.12
"""
```rst
.. module:: src.webdriver.chrome
    .. synonpsys: Module for Chrome WebDriver
```
Chrome WebDriver
=========================================================================================

This module contains a custom implementation of the Chrome WebDriver using Selenium. It integrates
configuration settings defined in the `chrome.json` file, such as user-agent and browser profile settings,
to enable flexible and automated browser interactions.

Key Features:
    - Centralized configuration via JSON files.
    - Support for multiple browser profiles.
    - Enhanced logging and error handling.
    - Ability to pass custom options during initialization.

Example usage
--------------------

Example of using the `Chrome` class:

.. code-block:: python

    from src.webdriver.chrome import Chrome

    # Initialize Chrome WebDriver with user-agent settings and custom options
    browser = Chrome(user_agent='Mozilla/5.0...', options=["--headless", "--disable-gpu"])
    browser.get("https://www.example.com")
    browser.quit()
"""

import os
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException

from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

class Chrome(webdriver.Chrome):
    """
    Class for Chrome WebDriver.

    This class extends the Selenium Chrome WebDriver and provides a singleton pattern and custom configurations.
    """
    _instance = None
    """
    _instance (Chrome): The single instance of the Chrome WebDriver.
    """
    driver_name: str = 'chrome'
    """
    driver_name (str): The name of the driver ('chrome').
    """
    config: SimpleNamespace
    """
    config (SimpleNamespace): Configuration settings loaded from a JSON file.
    """

    def __new__(cls, *args, **kwargs):
        """
        Ensure a single instance of Chrome WebDriver.

        If an instance already exists, it calls `window_open()`.

        Returns:
            Chrome: The singleton instance of the Chrome WebDriver.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            # Открывает новое окно, если экземпляр уже существует.
            cls._instance.window_open()
        return cls._instance

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs):
        """
        Initializes the Chrome WebDriver with specified options and profile.

        Args:
            user_agent (Optional[str]): The user-agent string to be used. Defaults to a random user agent.
            options (Optional[List[str]]): A list of Chrome options to be passed during initialization.
        """
        try:
            # Устанавливает user_agent или генерирует случайный
            user_agent = user_agent or UserAgent().random
            # Загружает конфигурации из JSON файла
            self.config = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))

            # Проверяет загрузку конфигурации
            if not self.config:
                logger.debug('Error in `chrome.json` file.')
                return

            # Инициализирует объект опций
            options_obj = ChromeOptions()

            # Добавляет аргументы из конфигурации
            self._add_config_options(options_obj)
            # Добавляет пользовательские опции
            self._add_custom_options(options_obj, options)
            # Добавляет заголовки из конфигурации
            self._add_config_headers(options_obj)

            # Нормализует пути
            profile_directory = Path(gs.path.root / self._normalize_path(self.config.profile_directory.testing))
            binary_location = Path(gs.path.root / self._normalize_path(self.config.binary_location.binary))

            # Проверяет наличие директории профиля и добавляет аргумент
            if profile_directory:
                 options_obj.add_argument(f'user-data-dir={profile_directory}')

            # Устанавливает путь к исполняемому файлу
            options_obj.binary_location = str(binary_location)
            # Инициализирует сервис Chrome driver
            service = ChromeService(executable_path=str(binary_location)) if binary_location else ChromeService()
        except Exception as ex:
            logger.error('Error setting up Chrome WebDriver:', ex)
            return

        try:
            # Инициализирует WebDriver
            super().__init__(options=options_obj, service=service)
        except WebDriverException as ex:
            logger.critical('Error initializing Chrome WebDriver:', ex)
            return
        except Exception as ex:
            logger.critical('Chrome WebDriver crashed. General error:', ex)
            return

        # Загружает дополнительные функции
        self._payload()

    def _add_config_options(self, options_obj: ChromeOptions) -> None:
        """
        Adds options from the configuration to ChromeOptions.

        Args:
            options_obj (ChromeOptions): Chrome options object.
        """
        # Проверяет наличие итерируемых параметров в конфигурации
        if hasattr(self.config, 'options') and isinstance(self.config.options, list):
            for option in self.config.options:
                options_obj.add_argument(option)

    def _add_custom_options(self, options_obj: ChromeOptions, options: Optional[List[str]]) -> None:
        """
        Adds custom options to ChromeOptions.

        Args:
            options_obj (ChromeOptions): Chrome options object.
            options (Optional[List[str]]): List of custom options.
        """
        # Проверяет наличие кастомных опций и добавляет их
        if options:
            for option in options:
                options_obj.add_argument(option)

    def _add_config_headers(self, options_obj: ChromeOptions) -> None:
        """
        Adds headers from the configuration to ChromeOptions.

        Args:
             options_obj (ChromeOptions): Chrome options object.
        """
        # Проверяет наличие заголовков в конфигурации и добавляет их
        if hasattr(self.config, 'headers') and self.config.headers:
            for key, value in self.config.headers.__dict__.items():
                options_obj.add_argument(f'--{key}={value}')

    def _normalize_path(self, path: str) -> str:
        """
        Replaces placeholders with actual environment paths.

        Args:
            path (str): The path string with placeholders like %APPDATA% or %LOCALAPPDATA%.
        Returns:
            str: The normalized path with environment variables substituted.
        """
        if not path:
            return ''
        # Заменяет переменные окружения в пути
        return (
            path.replace('%APPDATA%', os.environ.get('APPDATA', ''))
            .replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA', ''))
        )

    def _payload(self) -> None:
        """
        Loads executor for locators and JavaScript scenarios.

        This method initializes and assigns the necessary executors for web element interaction and
        JavaScript execution within the WebDriver.
        """
        # Инициализирует JavaScript executor
        js_executor = JavaScript(self)
        self.get_page_lang = js_executor.get_page_lang
        self.ready_state = js_executor.ready_state
        self.get_referrer = js_executor.get_referrer
        self.unhide_DOM_element = js_executor.unhide_DOM_element
        self.window_focus = js_executor.window_focus

        # Инициализирует executor для локаторов
        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message

if __name__ == "__main__":
    driver = Chrome(options=["--headless", "--disable-gpu"])
    driver.get(r"https://google.com")
```