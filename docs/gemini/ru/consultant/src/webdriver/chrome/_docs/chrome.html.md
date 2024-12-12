# Анализ кода модуля `chrome.html`

**Качество кода**
**7/10**
 -  Плюсы
    - Код хорошо структурирован и понятен.
    - Использование `logger` для логирования ошибок и отладки.
    - Применение `j_loads_ns` для загрузки JSON конфигурации.
    - Реализация поиска свободного порта.
    - Наличие документации в виде HTML.
 -  Минусы
    - Отсутствие reStructuredText (RST) документации в коде Python.
    - Не везде используется `logger.error` для обработки исключений.
    - Избыточное использование блоков `try-except`.
    - Присутствие TODO комментариев, указывающих на нереализованные функции.
    - Не полное соответствие с ранее обработанными файлами.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить docstring в формате RST для всех классов, функций и методов.
    -  Переписать комментарии после `#` в формате RST.

2.  **Обработка ошибок**:
    - Использовать `logger.error` вместо стандартных `try-except` там где это уместно.
    - Убрать избыточные блоки `try-except`, перенести обработку ошибок на уровень выше.

3.  **Импорты**:
    -  Убедиться в наличии всех необходимых импортов, сравнить с ранее обработанными файлами.

4.  **Структура кода**:
     -  Убедиться в соответствии имен переменных, функций и импортов с ранее обработанными файлами.

5.  **Улучшения кода**:
    -  Реализовать функционал `driver restart` и `program restart`.
    - Убрать лишние комментарии которые не несут информации.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

"""
Модуль для настройки и запуска Chrome WebDriver.
=========================================================================================

Этот модуль содержит класс :class:`Chrome`, который расширяет
функциональность `selenium.webdriver.Chrome`.
Он предоставляет дополнительные возможности для настройки и запуска Chrome WebDriver,
включая установку параметров запуска, выбор свободного порта и управление профилями.

Пример использования
--------------------

Пример использования класса `Chrome`:

.. code-block:: python

    from src.webdriver.chrome.chrome import Chrome

    driver = Chrome()
    driver.get("https://www.example.com")
    driver.quit()
"""
import os
import socket
from pathlib import Path
from typing import List, Dict, Optional, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent

from selenium.common.exceptions import WebDriverException
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

MODE = 'debug'

class Chrome(webdriver.Chrome):
    """
    Расширение класса `selenium.webdriver.Chrome` для дополнительной настройки.

    Предоставляет дополнительные методы для настройки и запуска Chrome WebDriver.
    Включает функциональность установки параметров запуска, выбора свободного порта и управления профилями.
    """
    driver_name = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """
        Инициализирует Chrome WebDriver с заданными опциями и профилем.

        :param user_agent: (dict, optional) Настройки User-Agent для Chrome WebDriver.
          По умолчанию использует случайный User-Agent.
        :raises Exception: Если возникает ошибка при настройке или запуске драйвера.
        """
        self.user_agent = user_agent if user_agent else UserAgent().random

        try:
            # Загрузка настроек Chrome из JSON-файла.
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))
            if not settings:
                logger.critical("Ошибка в файле конфигурации 'chrome.json'.")
                return

            # Определение директории профиля Chrome.
            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data')

            # Настройка пути к ChromeDriver.
            chromedriver_path_parts: list = settings['driver']['chromedriver']
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))

            # Настройка пути к бинарному файлу Chrome.
            binary_location_parts: list = settings['driver']['chrome_binary']
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts))

            # Установка опций Chrome.
            self.options: ChromeOptions = self.set_options(settings)
            self.options.add_argument(f'user-data-dir={profile_directory}')

            # Определение сервиса Chrome с указанным путем к бинарному файлу.
            self.service = ChromeService(executable_path=binary_location)

            # Поиск свободного порта.
            free_port = gs.webdriver_current_port
            gs.webdriver_current_port += 1

            if free_port:
                self.options.add_argument(f'--port={free_port}')
                logger.info(f'Установлен порт WebDriver: {free_port}')
            else:
                logger.critical("Нет доступных свободных портов в диапазоне (9500, 9599).")
                return

        except Exception as e:
            logger.error(f'Ошибка при настройке Chrome WebDriver: {e}')
            return

        try:
            logger.info("Запуск Chrome WebDriver")
            # Инициализация родительского класса с заданными опциями и сервисом.
            super().__init__(options=self.options, service=self.service)
        except WebDriverException as ex:
             # Логирование и обработка ошибки инициализации WebDriver
            logger.error(f"Ошибка инициализации Chrome WebDriver: {ex}")
            # @todo Implement driver restart
            return
        except Exception as ex:
            # Логирование и обработка общей ошибки запуска WebDriver
            logger.error(f"Chrome WebDriver завершился с ошибкой: {ex}")
            # @todo Implement program restart
            return


    def find_free_port(self, start_port: int, end_port: int) -> Optional[int]:
        """
        Находит свободный порт в заданном диапазоне.

        :param start_port: Начальный порт диапазона.
        :param end_port: Конечный порт диапазона.
        :return: Свободный порт или None, если свободный порт не найден.
        """
        for port in range(start_port, end_port + 1):
            try:
                # Проверка доступности порта, попытка привязать к нему сокет.
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port))
                    return port
            except OSError as ex:
                # Логирование занятого порта.
                logger.debug(f"Порт {port} занят: {ex}")
        return None

    def set_options(self, settings: Optional[dict] = None) -> ChromeOptions:
        """
        Устанавливает параметры запуска для Chrome WebDriver.

        :param settings: (dict, optional) Настройки конфигурации для опций Chrome.
        :return: Объект `ChromeOptions` с заданными параметрами запуска.
        """
        if not settings or ('options' not in settings and 'headers' not in settings):
            return ChromeOptions()

        options = ChromeOptions()

        if 'options' in settings:
            # Преобразование списка параметров в словарь.
            options_dict = {}
            for item in settings['options']:
                key, value = item.split('=')
                options_dict[key.strip()] = value.strip()
            # Добавление параметров из словаря в объект ChromeOptions.
            [options.add_argument(f"--{key}={value}") for key, value in options_dict.items()]

        if 'headers' in settings and settings['headers']:
            # Добавление заголовков из словаря в объект ChromeOptions.
            [options.add_argument(f"--{key}={value}") for key, value in settings['headers'].items()]

        return options
```