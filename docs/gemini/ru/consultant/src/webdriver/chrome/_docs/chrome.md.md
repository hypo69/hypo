# Анализ кода модуля `chrome`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, с использованием классов и методов для организации логики.
    - Присутствует обработка ошибок и логирование.
    - Используется `fake-useragent` для генерации случайных `user-agent`.
    -  Конфигурация webdriver вынесена в отдельный файл `chrome.json`.
 -  Минусы
    -  Не все функции и методы имеют подробное описание в формате reStructuredText (RST).
    -   В коде используются `try-except` блоки без конкретизации исключений, что может затруднить отладку.
    - Некоторые комментарии после `#` могут быть более подробными.
    - Не используется `j_loads_ns` для чтения `json` файла.

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST ко всем функциям, методам и классам, чтобы документация была более понятной и соответствовала стандартам.
2.  Использовать `j_loads_ns` для загрузки `json` файлов.
3.  Улучшить обработку ошибок, добавляя конкретные типы исключений в `try-except` блоки и использовать `logger.error` для вывода ошибок.
4.  Переписать комментарии после `#` на более подробные, описывающие назначение кода.
5.  Удалить лишние импорты, которые не используются в коде.

**Оптимизированный код**

```python
"""
Модуль для работы с Chrome WebDriver.
=========================================================================================

Этот модуль предоставляет класс :class:`Chrome`, который является подклассом `selenium.webdriver.Chrome`
и обеспечивает дополнительную функциональность для настройки и запуска Chrome WebDriver.

Используется Chrome для разработчиков. Версия определяется в файле `chrome.json`.

Пример использования
--------------------

Пример использования класса `Chrome`:

.. code-block:: python

    chrome_driver = Chrome()
    chrome_driver.get('https://example.com')
    ...
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
    Подкласс `selenium.webdriver.Chrome`, предоставляющий дополнительную функциональность.

    :ivar driver_name: Имя используемого веб-драйвера.
    :vartype driver_name: str
    :ivar d: Экземпляр веб-драйвера Chrome.
    :vartype d: webdriver.Chrome
    :ivar options: Опции для настройки Chrome.
    :vartype options: ChromeOptions
    :ivar user_agent: Настройки User-Agent.
    :vartype user_agent: dict
    """

    driver_name = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
        """
        Инициализирует Chrome WebDriver с заданными опциями и профилем.

        :param user_agent: Настройки User-Agent для Chrome WebDriver.
        :type user_agent: dict, optional
        :raises FileNotFoundError: Если файл конфигурации `chrome.json` не найден.
        :raises KeyError: Если в файле конфигурации отсутствуют необходимые ключи.
        :raises Exception: При возникновении других ошибок во время настройки WebDriver.
        :return: None
        
        .. note::
           Подробнее про User-Agent можно посмотреть тут: https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066
        """
        self.user_agent = user_agent if user_agent else UserAgent().random

        try:
            # Загрузка настроек Chrome из JSON-файла
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))
            if not settings:
                logger.critical('Файл конфигурации \'chrome.json\' не найден или пуст.')
                return

            # Определение каталога профиля Chrome
            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data')

            # Настройка пути к ChromeDriver
            chromedriver_path_parts: list = settings['driver']['chromedriver']
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))

            # Настройка пути к исполняемому файлу Chrome
            binary_location_parts: list = settings['driver']['chrome_binary']
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts))

            # Настройка опций Chrome
            self.options: ChromeOptions = self.set_options(settings)
            self.options.add_argument(f'user-data-dir={profile_directory}')

            # Определение сервиса Chrome с указанным расположением бинарного файла
            self.service = ChromeService(executable_path=binary_location)

            # Поиск свободного порта
            free_port = gs.webdriver_current_port
            gs.webdriver_current_port += 1

            if free_port:
                self.options.add_argument(f'--port={free_port}')
                logger.info(f'Установлен порт WebDriver: {free_port}')
            else:
                logger.critical('Нет свободных портов в диапазоне (9500, 9599).')
                return

        except FileNotFoundError as e:
            logger.error(f'Файл конфигурации не найден: {e}', exc_info=True)
            return
        except KeyError as e:
            logger.error(f'Отсутствует необходимый ключ в конфигурации: {e}', exc_info=True)
            return
        except Exception as e:
            logger.critical('Ошибка при настройке Chrome WebDriver.', exc_info=True)
            return

        try:
            logger.info('Запуск Chrome WebDriver.')
            service = None
            # Инициализация веб-драйвера с заданными опциями и сервисом
            super().__init__(options=self.options, service=self.service)

        except WebDriverException as ex:
            logger.critical(f'Ошибка инициализации Chrome WebDriver: {ex}', exc_info=True)
            """ @todo Implement driver restart """
            return
        except Exception as ex:
            logger.critical(f'Chrome WebDriver завершился с ошибкой: {ex}', exc_info=True)
            """ @todo Implement program restart """
            return

    def find_free_port(self, start_port: int, end_port: int) -> int | None:
        """
        Находит свободный порт в заданном диапазоне.

        :param start_port: Начальный порт диапазона.
        :type start_port: int
        :param end_port: Конечный порт диапазона.
        :type end_port: int
        :return: Свободный порт или None, если нет доступных портов.
        :rtype: int | None
        """
        for port in range(start_port, end_port + 1):
            try:
                # Проверка доступности порта
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port))
                    return port
            except OSError as ex:
                logger.debug(f'Порт {port} занят: {ex}', exc_info=True)
        return None

    def set_options(self, settings: list | dict | None = None) -> ChromeOptions:
        """
        Устанавливает опции запуска для Chrome WebDriver.

        :param settings: Настройки конфигурации для опций Chrome.
        :type settings: list | dict | None
        :return: Объект `ChromeOptions` с заданными опциями запуска.
        :rtype: ChromeOptions
        """
        if not settings or ('options' not in settings and 'headers' not in settings):
            return ChromeOptions()

        options = ChromeOptions()

        if 'options' in settings:
            # Преобразование списка параметров в словарь
            options_dict = {}
            for item in settings['options']:
                try:
                    key, value = item.split('=')
                    options_dict[key.strip()] = value.strip()
                except ValueError as e:
                    logger.error(f'Неверный формат опции: {item} - {e}', exc_info=True)
                    continue

            # Добавление настроек из словаря в объект ChromeOptions
            [options.add_argument(f'--{key}={value}') for key, value in options_dict.items()]

        if 'headers' in settings and settings['headers']:
            [options.add_argument(f'--{key}={value}') for key, value in settings['headers'].items()]

        return options
```