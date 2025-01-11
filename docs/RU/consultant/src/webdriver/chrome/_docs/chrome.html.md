# Анализ кода модуля `chrome`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код структурирован и разбит на логические блоки.
    *   Используется класс для инкапсуляции логики управления драйвером Chrome.
    *   Присутствует обработка исключений, хотя и не везде оптимально.
    *   Используется `logger` для логирования.
    *   Наличие документации в виде HTML файла.
*   **Минусы:**
    *   Не используется `j_loads` для загрузки `json` файлов.
    *   Смешение кода с HTML-документацией в одном файле.
    *   Не все методы документированы в формате RST.
    *   Обработка ошибок местами избыточна и не всегда информативна.
    *   Некоторые переменные не имеют аннотации типов.
    *   Использование `return` без значения в некоторых местах, где это может быть не очевидно.
    *   Использование не стандартного способа обработки `settings` из `json`.
    *   Не все комментарии достаточно подробны.
    *   Не везде используются одинарные кавычки для строк в коде.

**Рекомендации по улучшению:**

1.  **Использование `j_loads_ns`:** Заменить `j_loads` на `j_loads_ns` при загрузке `chrome.json`.
2.  **Разделение кода и документации:** Отделить код Python от HTML документации.
3.  **Документирование методов в RST:** Добавить docstring в формате RST для всех методов, включая `__init__`, `find_free_port` и `set_options`.
4.  **Оптимизация обработки ошибок:** Использовать `logger.error` вместо `try-except` в тех случаях, где это возможно.
5.  **Аннотации типов:** Добавить аннотации типов для переменных, где это необходимо.
6.  **Уточнение возвращаемых значений:** Явно указывать, что возвращает `None` в случаях, когда не найдено свободных портов или при ошибках.
7.  **Улучшение обработки настроек:** Использовать более явные проверки ключей в словаре `settings` вместо `if not settings or`.
8.  **Детализация комментариев:** Уточнить комментарии, чтобы было понятно, что именно делает каждый блок кода.
9.  **Унификация кавычек:** Использовать только одинарные кавычки для строк в Python-коде, двойные только в операциях вывода или логах.
10. **Улучшить метод `set_options`:** Преобразование `settings` к словарю и добавление параметров в ChromeOptions должно быть более понятным и эффективным.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
"""
Модуль для управления веб-драйвером Chrome.
=========================================================================================

Этот модуль содержит класс :class:`Chrome`, который является подклассом `selenium.webdriver.Chrome`
и предоставляет дополнительные функции для настройки и управления Chrome WebDriver.
"""

import os
import socket
from pathlib import Path
from typing import List, Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent

from selenium.common.exceptions import WebDriverException
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Chrome(webdriver.Chrome):
    """
    Подкласс `selenium.webdriver.Chrome`, предоставляющий дополнительные функции.

    Этот класс расширяет функциональность `selenium.webdriver.Chrome`, добавляя возможности
    для настройки и инициализации Chrome WebDriver с учетом специфических требований проекта.
    """

    driver_name: str = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
        """Инициализирует Chrome WebDriver с заданными опциями и профилем.

        Args:
            user_agent (dict, optional): Настройки user-agent для Chrome WebDriver.
                По умолчанию используется случайный user-agent.
                Подробности: https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066

        """
        # Инициализация user_agent
        self.user_agent = user_agent if user_agent else UserAgent().random

        try:
            # Загрузка настроек Chrome из JSON файла
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))
            if not settings:
                logger.critical('Ошибка в файле конфигурации \'chrome.json\'')
                return

            # Определение каталога профиля Chrome
            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data')

            # Настройка пути к ChromeDriver
            chromedriver_path_parts: list = settings.get('driver', {}).get('chromedriver', [])
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))

            # Настройка пути к бинарному файлу Chrome
            binary_location_parts: list = settings.get('driver', {}).get('chrome_binary', [])
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts))

            # Настройка опций Chrome
            self.options: ChromeOptions = self.set_options(settings)
            self.options.add_argument(f'user-data-dir={profile_directory}')

            # Определение сервиса Chrome с указанным путем к бинарному файлу
            self.service = ChromeService(executable_path=binary_location)

             # Поиск свободного порта
            free_port: int = gs.webdriver_current_port
            gs.webdriver_current_port += 1
            
            if free_port:
                # Установка порта для WebDriver
                self.options.add_argument(f'--port={free_port}')
                logger.info(f'Установлен порт WebDriver: {free_port}')
            else:
                 logger.critical('Нет свободных портов в диапазоне (9500, 9599)')
                 return

        except Exception as e:
            logger.critical('Ошибка при настройке Chrome WebDriver', exc_info=True)
            return

        try:
            # Инициализация WebDriver
            logger.info('Запуск Chrome WebDriver')
            super().__init__(options=self.options, service=self.service)
        except WebDriverException as ex:
            logger.critical('Ошибка инициализации Chrome WebDriver', exc_info=True)
            """@todo Implement driver restart"""
            return
        except Exception as ex:
             # Логирование общей ошибки при запуске WebDriver
            logger.critical('Chrome WebDriver завершил работу с ошибкой', exc_info=True)
            """@todo Implement program restart"""
            return


    def find_free_port(self, start_port: int, end_port: int) -> int | None:
        """Ищет свободный порт в заданном диапазоне.

        Args:
            start_port (int): Начальный порт диапазона.
            end_port (int): Конечный порт диапазона.

        Returns:
            int | None: Свободный порт или None, если свободный порт не найден.
        """
        for port in range(start_port, end_port + 1):
            try:
                # Проверка доступности порта
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port))
                    return port
            except OSError as ex:
                logger.debug(f'Порт {port} занят', exc_info=True)
        return None


    def set_options(self, settings: dict | None = None) -> ChromeOptions:
        """Устанавливает параметры запуска для Chrome WebDriver.

        Args:
            settings (dict | None, optional): Конфигурационные настройки для Chrome.

        Returns:
            ChromeOptions: Объект `ChromeOptions` с указанными параметрами запуска.
        """
        options: ChromeOptions = ChromeOptions()

        if not settings:
            return options

        # Обработка опций, если они есть
        if 'options' in settings and isinstance(settings['options'], list):
            options_dict = {}
            for item in settings['options']:
                if isinstance(item, str) and '=' in item:
                   key, value = item.split('=')
                   options_dict[key.strip()] = value.strip()
            for key, value in options_dict.items():
                options.add_argument(f'--{key}={value}')


        # Обработка заголовков, если они есть
        if 'headers' in settings and isinstance(settings['headers'], dict):
            for key, value in settings['headers'].items():
                options.add_argument(f'--{key}={value}')

        return options
```