### Анализ кода модуля `chrome`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Использование `j_loads_ns` для загрузки JSON.
    - Наличие комментариев, хоть и не в формате RST.
    - Использование `logger` для логирования.
    - Разделение настроек драйвера и бинарного пути в `chrome.json`.
    - Обработка `WebDriverException`.
- **Минусы**:
    - Отсутствие RST-документации для функций и класса.
    - Использование `try-except` без конкретики.
    - Смешивание настроек в `settings`.
    - Использование множественных `return` в `__init__`.
    - Непоследовательное использование кавычек в коде.
    - Код не соответствует PEP8.
    - Избыточное использование `if ... in ...`
    - Не используется `self.d`

**Рекомендации по улучшению**:
- Добавить RST-документацию для всех функций и класса.
- Конкретизировать исключения в `try-except` блоках.
- Упростить логику получения пути к драйверу и бинарнику.
- Использовать `j_loads_ns`  вместо  `j_loads`.
- Переработать инициализацию для исключения множественных `return`.
- Привести код в соответствие со стандартами PEP8.
- Избегать ненужных проверок `if not settings or ...`
- Использовать `self.d` для хранения экземпляра драйвера.
- Использовать f-строки для форматирования.
- Использовать более конкретные типы для аннотаций.
- Улучшить форматирование настроек в `set_options`, разделив логику.
- Обрабатывать ошибки при создании сокета более явно.
- Использовать `Path` для создания путей, избегая конкатенации.

**Оптимизированный код**:
```python
"""
Модуль для работы с Chrome WebDriver.
=====================================

Модуль содержит класс :class:`Chrome`, который является подклассом `selenium.webdriver.Chrome`
и предоставляет дополнительную функциональность для настройки и управления экземпляром Chrome WebDriver.

:var driver_name: Имя драйвера.
:vartype driver_name: str
:var d: Экземпляр WebDriver.
:vartype d: selenium.webdriver.Chrome
:var options: Опции Chrome.
:vartype options: selenium.webdriver.chrome.options.Options
:var user_agent: Настройки User-Agent.
:vartype user_agent: dict

Пример использования
---------------------
.. code-block:: python

    from src.webdriver.chrome import Chrome

    driver = Chrome()
    driver.get("https://www.example.com")
    driver.quit()
"""
import os
import socket
from pathlib import Path
from typing import List, Dict, Optional
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

    :ivar driver_name: Имя драйвера.
    :vartype driver_name: str
    :ivar d: Экземпляр WebDriver.
    :vartype d: webdriver.Chrome
    :ivar options: Опции Chrome.
    :vartype options: ChromeOptions
    :ivar user_agent: Настройки User-Agent.
    :vartype user_agent: dict
    """

    driver_name = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """
        Инициализирует Chrome WebDriver с заданными параметрами и профилем.

        :param user_agent: Настройки User-Agent для Chrome WebDriver.
        :type user_agent: dict, optional
        :raises Exception: Если возникают ошибки при настройке или инициализации WebDriver.

        :Example:
        >>> driver = Chrome()
        >>> driver.get('https://example.com')
        """
        self.user_agent = user_agent if user_agent else UserAgent().random

        try:
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json')) # Загрузка настроек из JSON
            if not settings:
                logger.critical("Ошибка в файле конфигурации 'chrome.json'.") # Логирование критической ошибки
                return

            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data') # Определение пути к профилю
            
            # Получение пути к драйверу
            chromedriver_path_parts: list = settings.get('driver', {}).get('chromedriver', []) # Получение частей пути к драйверу
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver # Замена 'chrome' на путь по умолчанию
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))#  Формирование полного пути к драйверу

            # Получение пути к бинарнику
            binary_location_parts: list = settings.get('driver', {}).get('chrome_binary', []) # Получение частей пути к бинарнику
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver# Замена 'chrome' на путь по умолчанию
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts)) #  Формирование полного пути к бинарнику
            
            self.options: ChromeOptions = self._set_options(settings.get('options'), settings.get('headers')) # Настройка опций Chrome
            self.options.add_argument(f'user-data-dir={profile_directory}') #  Добавление аргумента о пути к профилю

            self.service = ChromeService(executable_path=binary_location) #  Создание сервиса Chrome
            
            free_port: Optional[int] = gs.webdriver_current_port # Получение свободного порта
            gs.webdriver_current_port += 1 #  Инкремент текущего порта
            if free_port:
                self.options.add_argument(f'--port={free_port}') # Добавление порта к опциям
                logger.info(f'Установлен порт WebDriver: {free_port}') #  Логирование установки порта
            else:
                logger.critical("Нет свободных портов в диапазоне (9500, 9599).") # Логирование критической ошибки
                return

        except Exception as e:
            logger.critical(f'Ошибка при настройке Chrome WebDriver: {e}') # Логирование ошибки настройки
            return
        
        try:
            logger.info("Запуск Chrome WebDriver") # Логирование начала запуска
            self.d = super().__init__(options=self.options, service=self.service)  # Инициализация WebDriver
        except WebDriverException as ex:
            logger.critical(f"Ошибка инициализации Chrome WebDriver: {ex}") # Логирование ошибки инициализации
            return
        except Exception as ex:
            logger.critical(f"Chrome WebDriver аварийно завершил работу. Общая ошибка: {ex}")  # Логирование общей ошибки
            return

    def find_free_port(self, start_port: int, end_port: int) -> Optional[int]:
        """
        Находит свободный порт в заданном диапазоне.

        :param start_port: Начальный порт диапазона.
        :type start_port: int
        :param end_port: Конечный порт диапазона.
        :type end_port: int
        :return: Свободный порт, если есть, иначе None.
        :rtype: int | None
        
        :Example:
            >>> chrome = Chrome()
            >>> port = chrome.find_free_port(9000, 9010)
            >>> if port:
            >>>     print(f"Свободный порт: {port}")
        """
        for port in range(start_port, end_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port)) # Попытка привязать сокет к порту
                    return port # Возврат свободного порта
            except OSError as ex:
                 logger.debug(f"Порт {port} занят: {ex}") # Логирование занятости порта
        return None
    
    def _set_options(self, options_settings: Optional[list] = None, headers_settings: Optional[dict] = None) -> ChromeOptions:
        """
        Устанавливает опции запуска для Chrome WebDriver.

        :param options_settings: Настройки опций Chrome.
        :type options_settings: list, optional
        :param headers_settings: Настройки заголовков Chrome.
        :type headers_settings: dict, optional
        :return: Объект `ChromeOptions` с заданными опциями.
        :rtype: ChromeOptions

        :Example:
            >>> chrome = Chrome()
            >>> options = chrome._set_options(options_settings=['--headless', '--disable-gpu'], headers_settings={'User-Agent': 'custom'})
            >>> print(options)
        """
        options = ChromeOptions()
        
        if options_settings:
            options_dict = {}
            for item in options_settings:
                if '=' in item:
                    key, value = item.split('=')
                    options_dict[key.strip()] = value.strip()
            for key, value in options_dict.items():
                options.add_argument(f"--{key}={value}") # Добавление опций из словаря
        
        if headers_settings:
            for key, value in headers_settings.items():
                options.add_argument(f"--{key}={value}") # Добавление заголовков
        
        return options