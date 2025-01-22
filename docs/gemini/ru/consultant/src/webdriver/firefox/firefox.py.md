### Анализ кода модуля `firefox`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, разделен на функции и классы.
    - Используется логирование для отслеживания ошибок и событий.
    - Применяются асинхронные операции.
    - Имеется базовая документация.
- **Минусы**:
    - Не все функции имеют подробное RST-описание.
    - Используются двойные кавычки для строк, что противоречит заданному стандарту.
    - Смешаны настройки из файла и параметры, переданные при инициализации.
    - Отсутствует проверка версий geckodriver и Firefox.
    -  Дублирование кода `return` в блоках `except`.

**Рекомендации по улучшению**:

1.  **Унификация кавычек**:
    - Заменить все двойные кавычки на одинарные в коде, кроме `print`, `input` и логгера.
2.  **Документирование**:
    -   Добавить RST-документацию для всех функций и методов.
3.  **Импорты**:
    -  Импортировать `logger` через `from src.logger.logger import logger`.
4.  **Обработка ошибок**:
    -   Убрать дублирование `return` в блоках `except`, использовать обработку ошибок через `logger.error`
5.  **Параметры**:
    - Убрать дублирование параметров, передаваемых при инициализации, использовать только конфиг.
6.  **Версии**:
    - Добавить проверку версий geckodriver и Firefox при инициализации.
7. **Логика**:
    - Добавить в метод `_payload` проверку на существование вызываемых функций.
8.  **Улучшение кода**:
    - Заменить `vars(settings.headers).items()` на `settings.headers.__dict__.items()`, поскольку первый вариант может включать методы и нежелательные атрибуты.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с WebDriver Firefox
=================================================

Модуль содержит класс :class:`Firefox`, который расширяет функционал стандартного
`webdriver.Firefox`. Он предоставляет возможность настройки пользовательского профиля,
запуска в режиме киоска и установки пользовательских настроек, включая прокси.

Пример использования
--------------------

Пример использования класса `Firefox`:

.. code-block:: python

    if __name__ == "__main__":
        profile_name = 'custom_profile'
        geckodriver_version = 'v0.29.0'
        firefox_version = '78.0'
        proxy_file_path = 'path/to/proxies.txt'

        browser = Firefox(
            profile_name=profile_name,
            geckodriver_version=geckodriver_version,
            firefox_version=firefox_version,
            proxy_file_path=proxy_file_path
        )
        browser.get('https://www.example.com')
        browser.quit()
"""

import os
import random
from pathlib import Path
from typing import Optional, List

from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException

from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.webdriver.proxy import download_proxies_list, get_proxies_dict, check_proxy
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from fake_useragent import UserAgent
import header


class Firefox(WebDriver):
    """
    Расширение для `webdriver.Firefox` с дополнительной функциональностью.

    :param profile_name: Имя пользовательского профиля Firefox.
    :type profile_name: Optional[str]
    :param geckodriver_version: Версия geckodriver.
    :type geckodriver_version: Optional[str]
    :param firefox_version: Версия Firefox.
    :type firefox_version: Optional[str]
    :param user_agent: Пользовательский агент в формате строки.
    :type user_agent: Optional[str]
    :param proxy_file_path: Путь к файлу с прокси.
    :type proxy_file_path: Optional[str]
    :param options: Список опций для Firefox.
    :type options: Optional[List[str]]
    :param window_mode: Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)
    :type window_mode: Optional[str]
    """
    driver_name: str = 'firefox'

    def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 options: Optional[List[str]] = None,
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
        """
        Инициализирует WebDriver Firefox с заданными параметрами.

        :param profile_name: Имя пользовательского профиля Firefox.
        :type profile_name: Optional[str]
        :param geckodriver_version: Версия geckodriver.
        :type geckodriver_version: Optional[str]
        :param firefox_version: Версия Firefox.
        :type firefox_version: Optional[str]
        :param user_agent: Пользовательский агент в формате строки.
        :type user_agent: Optional[str]
        :param proxy_file_path: Путь к файлу с прокси.
        :type proxy_file_path: Optional[str]
        :param options: Список опций для Firefox.
        :type options: Optional[List[str]]
        :param window_mode: Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)
        :type window_mode: Optional[str]
        """
        service = None
        profile = None
        options_obj = None

        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'firefox' / 'firefox.json')) # Загрузка настроек Firefox
        geckodriver_path: str = str(Path(gs.path.root, settings.executable_path.geckodriver)) # Путь к geckodriver
        firefox_binary_path: str = str(Path(gs.path.root, settings.executable_path.firefox_binary)) # Путь к бинарнику Firefox

        service = Service(geckodriver_path) # Инициализация сервиса
        options_obj = Options() # Настройка опций Firefox

        if hasattr(settings, 'options') and settings.options:  # Добавление опций из файла настроек
            for option in settings.options:
                options_obj.add_argument(option)

        if hasattr(settings, 'window_mode') and settings.window_mode: # Установка режима окна из конфига
            window_mode = window_mode or settings.window_mode
        
        if window_mode: # Установка режима окна из параметров
            if window_mode == 'kiosk':
                options_obj.add_argument('--kiosk')
            elif window_mode == 'windowless':
               options_obj.add_argument('--headless')

        if options:  # Добавление опций, переданных при инициализации
            for option in options:
                options_obj.add_argument(option)

        if hasattr(settings, 'headers') and settings.headers: # Добавление заголовков из настроек
            for key, value in settings.headers.__dict__.items():
                 options_obj.add_argument(f'--{key}={value}')

        user_agent = user_agent or UserAgent().random  # Установка пользовательского агента
        options_obj.set_preference('general.useragent.override', user_agent)

        if hasattr(settings, 'proxy_enabled') and settings.proxy_enabled:  # Установка прокси, если включены
            self.set_proxy(options_obj)

        profile_directory = settings.profile_directory.os if settings.profile_directory.default == 'os' else str(Path(gs.path.src, settings.profile_directory.internal)) # Настройка директории профиля

        if profile_name:
            profile_directory = str(Path(profile_directory).parent / profile_name)
        if '%LOCALAPPDATA%' in profile_directory:
             profile_directory = Path(profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA')))

        profile = FirefoxProfile(profile_directory=profile_directory)

        try:
            logger.info('Запуск Firefox WebDriver')
            super().__init__(service=service, options=options_obj)
            self._payload() # Выполнение пользовательских действий после инициализации драйвера
        except WebDriverException as ex:
             logger.critical("""
                ---------------------------------
                    Ошибка запуска WebDriver
                    Возможные причины:
                    - Обновление Firefox
                    - Отсутствие Firefox на ОС
                ----------------------------------""", ex)
        except Exception as ex:
            logger.critical('Ошибка работы Firefox WebDriver:', ex)


    def set_proxy(self, options: Options) -> None:
        """
        Настраивает прокси из словаря, возвращаемого `get_proxies_dict`.

        :param options: Опции Firefox, в которые добавляются настройки прокси.
        :type options: Options
        """
        proxies_dict = get_proxies_dict() # Получение словаря прокси
        all_proxies = proxies_dict.get('socks4', []) + proxies_dict.get('socks5', []) # Создание списка всех прокси
        working_proxy = None
        for proxy in random.sample(all_proxies, len(all_proxies)): # Перебор прокси для поиска рабочего
            if check_proxy(proxy):
                working_proxy = proxy
                break

        if working_proxy: # Настройка прокси, если он найден
            proxy = working_proxy
            protocol = proxy.get('protocol')
            if protocol == 'http':  # Настройка прокси в зависимости от протокола
                options.set_preference('network.proxy.type', 1)
                options.set_preference('network.proxy.http', proxy['host'])
                options.set_preference('network.proxy.http_port', int(proxy['port']))
                options.set_preference('network.proxy.ssl', proxy['host'])
                options.set_preference('network.proxy.ssl_port', int(proxy['port']))
                logger.info(f"Настройка HTTP Proxy: http://{proxy['host']}:{proxy['port']}")

            elif protocol == 'socks4':
                options.set_preference('network.proxy.type', 1)
                options.set_preference('network.proxy.socks', proxy['host'])
                options.set_preference('network.proxy.socks_port', int(proxy['port']))
                logger.info(f"Настройка SOCKS4 Proxy: {proxy['host']}:{proxy['port']}")

            elif protocol == 'socks5':
                options.set_preference('network.proxy.type', 1)
                options.set_preference('network.proxy.socks', proxy['host'])
                options.set_preference('network.proxy.socks_port', int(proxy['port']))
                logger.info(f"Настройка SOCKS5 Proxy: {proxy['host']}:{proxy['port']}")

            else:
                logger.warning(f"Неизвестный тип прокси: {protocol}")
        else:
            logger.warning('Нет доступных прокси в предоставленном файле.')


    def _payload(self) -> None:
        """
        Загружает исполнителей для локаторов и JavaScript сценариев.
        """
        j = JavaScript(self)
        if hasattr(j, 'get_page_lang'):
           self.get_page_lang = j.get_page_lang
        if hasattr(j, 'ready_state'):
            self.ready_state = j.ready_state
        if hasattr(j, 'get_referrer'):
            self.get_referrer = j.ready_state
        if hasattr(j, 'unhide_DOM_element'):
           self.unhide_DOM_element = j.unhide_DOM_element
        if hasattr(j, 'window_focus'):
           self.window_focus = j.window_focus
        

        execute_locator = ExecuteLocator(self)
        if hasattr(execute_locator, 'execute_locator'):
           self.execute_locator = execute_locator.execute_locator
        if hasattr(execute_locator, 'get_webelement_as_screenshot'):
            self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        if hasattr(execute_locator, 'get_webelement_by_locator'):
            self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        if hasattr(execute_locator, 'get_attribute_by_locator'):
            self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        if hasattr(execute_locator, 'send_message'):
            self.send_message = self.send_key_to_webelement = execute_locator.send_message

if __name__ == "__main__":
    driver = Firefox()
    driver.get(r"https://google.com")