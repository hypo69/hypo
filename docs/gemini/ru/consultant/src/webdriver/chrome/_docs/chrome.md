# Анализ кода модуля `chrome`

## Качество кода
7
-  Плюсы
    - Код структурирован и разбит на классы и функции.
    - Используются стандартные библиотеки и `selenium`.
    - Наличие комментариев.
    - Использование `logger` для логирования.
    - Управление портами.
    - Использование `j_loads_ns` для загрузки json.
    - Управление заголовками.
-  Минусы
    -  Не все функции и методы имеют docstring.
    -  Использование `try-except` без явного логирования.
    -  Смешивание комментариев в стиле Doxygen и Python docstring.
    -  Не везде используется форматирование кода.

## Рекомендации по улучшению
1. Добавить docstring к методам и классам.
2. Использовать `logger.error` вместо общих `except Exception`.
3.  Удалить Doxygen комментарии и использовать только docstring.
4.  Использовать одинарные кавычки в Python коде.
5.  Унифицировать использование `list` и `dict`.
6.  Добавить обработку ошибок при загрузке настроек.
7.  Обеспечить более надежный поиск свободного порта, возможно с проверкой на занятость через `lsof` в Linux.
8.  Реализовать перехват `WebDriverException` и перезапуск драйвера.
9.  Улучшить обработку случаев отсутствия настроек.
10. Добавить валидацию данных из json файла `chrome.json`.
11. Добавить примеры использования класса в docstring.
12. Улучшить читаемость кода, например разбить длинные строки.
13. Проверку на `None` в `set_options`.
14. Заменить `return` на `return None` если возвращается `None`.
15. Использование f-string форматирования.
16. Добавить комментарии для сложных моментов кода.

## Оптимизированный код

```python
"""
Модуль для управления WebDriver Chrome.
=========================================================================================

Этот модуль содержит класс :class:`Chrome`, который наследуется от `selenium.webdriver.Chrome`
и предоставляет дополнительные возможности для настройки и управления экземпляром Chrome WebDriver.

Пример использования
--------------------

Пример создания экземпляра `Chrome`:

.. code-block:: python

    from src.webdriver.chrome.chrome import Chrome
    from src.logger.logger import logger

    try:
        driver = Chrome()
        driver.get('https://www.example.com')
        logger.info('Successfully opened page.')
    except Exception as e:
        logger.error(f'Failed to initialize Chrome webdriver: {e}')
    finally:
        if driver:
            driver.quit()
            logger.info('Driver quited.')
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
    Расширение класса `selenium.webdriver.Chrome` для добавления дополнительной функциональности.

    Предоставляет методы для настройки и управления экземпляром Chrome WebDriver,
    включая управление профилями, портами и заголовками.
    """
    driver_name = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
        """
        Инициализирует экземпляр Chrome WebDriver с заданными параметрами.

        Args:
            user_agent (dict, optional): Настройки user-agent.
                Defaults to a random user-agent.
            *args: Дополнительные аргументы для родительского класса.
            **kwargs: Дополнительные именованные аргументы для родительского класса.
        """
        self.user_agent = user_agent if user_agent else UserAgent().random
        try:
            # Загрузка настроек из файла chrome.json
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))
            if not settings:
                logger.critical('Ошибка в файле конфигурации \'chrome.json\'.')
                return

            #  Определение пути к каталогу профиля
            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data')
            
            # Настройка пути к ChromeDriver
            chromedriver_path_parts: list = settings.get('driver', {}).get('chromedriver', [])
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))
            
            # Настройка пути к исполняемому файлу Chrome
            binary_location_parts: list = settings.get('driver', {}).get('chrome_binary', [])
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts))
            
            # Установка опций Chrome
            self.options: ChromeOptions = self.set_options(settings)
            self.options.add_argument(f'user-data-dir={profile_directory}')
            
            # Определение сервиса Chrome
            self.service = ChromeService(executable_path=binary_location)
            
            # Поиск свободного порта
            free_port = gs.webdriver_current_port
            gs.webdriver_current_port += 1
            
            if free_port:
                self.options.add_argument(f'--port={free_port}')
                logger.info(f'Установлен порт WebDriver: {free_port}')
            else:
                logger.critical('Нет свободных портов в диапазоне (9500, 9599)')
                return

        except Exception as e:
            logger.error('Ошибка при настройке Chrome WebDriver.', exc_info=True)
            return

        try:
            logger.info('Запуск Chrome WebDriver')
            super().__init__(options=self.options, service=self.service)

        except WebDriverException as ex:
            logger.error(f'Ошибка инициализации Chrome WebDriver: {ex}', exc_info=True)
            # TODO: Implement driver restart
            return
        except Exception as ex:
            logger.error(f'Chrome WebDriver аварийно завершил работу. Общая ошибка: {ex}', exc_info=True)
            # TODO: Implement program restart
            return

    def find_free_port(self, start_port: int, end_port: int) -> int | None:
        """
        Находит свободный порт в заданном диапазоне.

        Args:
            start_port (int): Начальный порт диапазона.
            end_port (int): Конечный порт диапазона.

        Returns:
            int | None: Свободный порт, если найден, иначе None.
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
        """
        Устанавливает параметры запуска для Chrome WebDriver.

        Args:
             settings (dict, optional): Настройки для Chrome. Defaults to None.

        Returns:
             ChromeOptions: Объект `ChromeOptions` с заданными параметрами.
        """
        if not settings or ('options' not in settings and 'headers' not in settings):
            return ChromeOptions()

        options = ChromeOptions()

        if 'options' in settings:
            # Преобразование списка параметров в словарь
            options_dict = {}
            for item in settings['options']:
                if '=' in item:
                    key, value = item.split('=', 1)
                    options_dict[key.strip()] = value.strip()
                else:
                  logger.warning(f'Неправильный формат параметра {item} в `options`')
                  continue


            # Добавление параметров в объект ChromeOptions
            for key, value in options_dict.items():
                options.add_argument(f'--{key}={value}')

        if 'headers' in settings and isinstance(settings['headers'], dict):
            for key, value in settings['headers'].items():
                 options.add_argument(f'--{key}={value}')

        return options
```