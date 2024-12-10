## \file hypotez/src/webdriver/firefox/firefox.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с WebDriver Firefox
=========================================================================================

Этот модуль содержит класс :class:`Firefox`, который расширяет функционал стандартного 
`webdriver.Firefox`. Он предоставляет возможность настройки пользовательского профиля, 
запуска в режиме киоска и установки пользовательских настроек, включая прокси.

Пример использования
--------------------

Пример использования класса `Firefox`:

.. code-block:: python

    if __name__ == "__main__":
        profile_name = "custom_profile"
        geckodriver_version = "v0.29.0"
        firefox_version = "78.0"
        proxy_file_path = "path/to/proxies.txt"

        browser = Firefox(
            profile_name=profile_name, 
            geckodriver_version=geckodriver_version, 
            firefox_version=firefox_version,
            proxy_file_path=proxy_file_path
        )
        browser.get("https://www.example.com")
        browser.quit()
"""

MODE = 'dev'

import os
import random
from pathlib import Path
from typing import Optional
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
    :param geckodriver_version: Версия geckodriver.
    :param firefox_version: Версия Firefox.
    :param user_agent: Пользовательский агент в формате строки.
    :param proxy_file_path: Путь к файлу с прокси.
    """
    driver_name: str = 'firefox'

    def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 *args, **kwargs) -> None:
        service = None
        profile = None
        options = None

        # Загрузка настроек Firefox
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'firefox' / 'firefox.json'))

        # Путь к geckodriver и бинарнику Firefox
        geckodriver_path: str = str(Path(gs.path.root, settings.executable_path.geckodriver))
        firefox_binary_path: str = str(Path(gs.path.root, settings.executable_path.firefox_binary))

        # Инициализация сервиса
        service = Service(geckodriver_path)

        # Настройка опций Firefox
        options = Options()
        if hasattr(settings, 'options') and settings.options:
            for key, value in vars(settings.options).items():
                options.add_argument(f'--{key}={value}')

        if hasattr(settings, 'headers') and settings.headers:
            for key, value in vars(settings.headers).items():
                options.add_argument(f'--{key}={value}')

        # Установка пользовательского агента
        user_agent = user_agent or UserAgent().random
        options.set_preference('general.useragent.override', user_agent)

        if hasattr(settings, 'proxy_enabled') and settings.proxy_enabled:
            self.set_proxy(options)

        # Настройка профиля
        profile_directory = settings.profile_directory.os if settings.profile_directory.default == 'os' else str(Path(gs.path.src, settings.profile_directory.internal))

        if profile_name:
            profile_directory = str(Path(profile_directory).parent / profile_name)

        if '%LOCALAPPDATA%' in profile_directory:
            profile_directory = Path(profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA')))

        profile = FirefoxProfile(profile_directory=profile_directory)

        try:
            logger.info('Запуск Firefox WebDriver')
            super().__init__(service=service, options=options)

            # Выполнение пользовательских действий после инициализации драйвера
            self._payload()

        except WebDriverException as ex:
            logger.critical("""
                ---------------------------------
                    Ошибка запуска WebDriver
                    Возможные причины:
                    - Обновление Firefox
                    - Отсутствие Firefox на ОС
                ----------------------------------""", ex)
            ...
            return
        except Exception as ex:
            logger.critical('Ошибка работы Firefox WebDriver:', ex)
            ...
            return

    def set_proxy(self,options:Options) -> None:
        """
        Настройка прокси из словаря, возвращаемого get_proxies_dict
        """
        # Настройка прокси из словаря, возвращаемого get_proxies_dict
        proxies_dict = get_proxies_dict()

        all_proxies = proxies_dict.get('socks4') + proxies_dict.get('socks5')

        # Попытка найти рабочий прокси
        working_proxy = None
        for proxy in random.sample(all_proxies, len(all_proxies)):  # перемешиваем прокси, чтобы случайно выбирать
            if check_proxy(proxy):
                working_proxy = proxy
                break

        # Код выбирает случайный прокси из всех доступных типов
        if working_proxy:
            proxy = working_proxy
            protocol = proxy.get('protocol')  # Получение типа протокола (http, socks4, socks5)

            # Настройка прокси в зависимости от протокола
            if protocol == 'http':
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
        Load executors for locators and JavaScript scenarios.
        """
        ...
        j = JavaScript(self)
        self.get_page_lang = j.get_page_lang
        self.ready_state = j.ready_state
        self.get_referrer = j.ready_state
        self.unhide_DOM_element = j.unhide_DOM_element
        self.window_focus = j.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message

if __name__ == "__main__":
    driver = Firefox()
    driver.get(r"https://google.com")
