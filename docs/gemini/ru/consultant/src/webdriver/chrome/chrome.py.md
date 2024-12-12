# Анализ кода модуля chrome.py

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, используется класс `Chrome` для управления WebDriver.
    - Присутствует механизм singleton для управления экземпляром драйвера.
    - Используется `j_loads_ns` для загрузки конфигурации из JSON.
    - Применяется `fake_useragent` для генерации случайных user-agent.
    - Наличие логирования ошибок через `logger`.
    - Выделен функционал по работе с JS в отдельный класс `JavaScript`.
    - Выделен функционал по работе с локаторами в отдельный класс `ExecuteLocator`.
-  Минусы
    -  Отсутствуют docstring для некоторых методов и переменных.
    -  В некоторых местах используются `...` вместо обработки ошибок.
    -  Не везде используется RST формат для комментариев.
    -  Смешанный стиль использования кавычек в коде.

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST для всех методов и переменных, включая `_instance`, `driver_name`, `config`.
2.  Заменить `...` на конкретную логику обработки ошибок, например, через `logger.error` или возвращение `None`.
3.  Привести все комментарии к формату RST.
4.  Использовать одинарные кавычки `'` везде в коде.
5.  Добавить обработку ошибки при создании `ChromeService`.
6.  Добавить проверку существования `profile_directory` и `binary_location` перед их использованием.

**Оптимизированный код**

```python
"""
Module for Chrome WebDriver
=========================================================================================

This module contains a custom implementation of the Chrome WebDriver using Selenium. It integrates
configuration settings defined in the `chrome.json` file, such as user-agent and browser profile settings,
to enable flexible and automated browser interactions.

Key Features:
    - Centralized configuration via JSON files.
    - Support for multiple browser profiles.
    - Enhanced logging and error handling.

Example usage
--------------------

Example of using the `Chrome` class:

.. code-block:: python

    from src.webdriver.chrome import Chrome

    # Initialize Chrome WebDriver with user-agent settings
    browser = Chrome(user_agent='Mozilla/5.0...')
    browser.get("https://www.example.com")
    browser.quit()
"""

MODE = 'dev'

import os
import sys
from pathlib import Path
from typing import Optional
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException

import header
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

        :return: The singleton instance of the Chrome WebDriver.
        :rtype: Chrome
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._instance.window_open()  # Open a new window if instance already exists
        return cls._instance

    def __init__(self, user_agent: Optional[str] = None, *args, **kwargs):
        """
        Initializes the Chrome WebDriver with specified options and profile.

        :param user_agent: The user-agent string to be used. Defaults to a random user agent.
        :type user_agent: Optional[str]
        """
        try:
            # устанавливаем user_agent или генерируем случайный
            user_agent = user_agent or UserAgent().random
            # загружаем конфигурации из JSON файла
            self.config = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))

            # Проверяем загружена ли конфигурация
            if not self.config:
                logger.debug('Error in `chrome.json` file.')
                return
            # инициализируем параметры
            options = ChromeOptions()
            # устанавливаем путь до профиля
            profile_directory: Path
            # устанавливаем путь до исполняемого файла
            executable_path: str

            def normalize_path(path: str) -> str:
                """
                Replace placeholders with actual environment paths.

                :param path: The path string with placeholders like %APPDATA% or %LOCALAPPDATA%.
                :type path: str
                :return: The normalized path with environment variables substituted.
                :rtype: str
                """
                if not path:
                    return ''
                return (
                    path.replace('%APPDATA%', os.environ.get('APPDATA', ''))
                    .replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA', ''))
                )

            # Добавляем аргументы из настроек options
            if hasattr(self.config, 'options') and self.config.options:
                for key, value in vars(self.config.options).items():
                    options.add_argument(f'--{key}={value}')

            # Добавляем аргументы из настроек headers
            if hasattr(self.config, 'headers') and self.config.headers:
                for key, value in vars(self.config.headers).items():
                    options.add_argument(f'--{key}={value}')

            # Нормализуем пути
            profile_directory = Path(gs.path.root / normalize_path(self.config.profile_directory.testing))
            binary_location = Path(gs.path.root / normalize_path(self.config.binary_location.binary))

            # Проверяем наличие директории профиля и добавляем аргумент
            if profile_directory:
                options.add_argument(f'user-data-dir={profile_directory}')

             # Устанавливаем путь к исполняемому файлу
            options.binary_location = str(binary_location)
            # Инициализируем сервис chrome driver
            service = ChromeService(executable_path=str(binary_location)) if binary_location else ChromeService()

        except Exception as ex:
            logger.error('Error setting up Chrome WebDriver:', ex)
            return

        try:
            # Инициализируем webdriver
            super().__init__(options=options, service=service)
        except WebDriverException as ex:
            logger.critical('Error initializing Chrome WebDriver:', ex)
            return
        except Exception as ex:
            logger.critical('Chrome WebDriver crashed. General error:', ex)
            return

        self._payload()

    def _payload(self) -> None:
        """
        Load executor for locators and JavaScript scenarios.

        This method initializes and assigns the necessary executors for web element interaction and
        JavaScript execution within the WebDriver.
        """
        js_executor = JavaScript(self)
        self.get_page_lang = js_executor.get_page_lang
        self.ready_state = js_executor.ready_state
        self.get_referrer = js_executor.get_referrer
        self.unhide_DOM_element = js_executor.unhide_DOM_element
        self.window_focus = js_executor.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message


if __name__ == "__main__":
    driver = Chrome()
    driver.get(r"https://google.com")