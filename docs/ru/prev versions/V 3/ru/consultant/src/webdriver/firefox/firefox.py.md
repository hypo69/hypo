### Анализ кода модуля `firefox.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Хорошая структура и организация кода.
  - Использование аннотаций типов.
  - Наличие документации к классам и методам.
  - Использование `logger` для логирования.
- **Минусы**:
  - Не все методы и функции имеют подробное описание в документации.
  - Не везде используются одинарные кавычки.
  - Есть устаревшие или неиспользуемые участки кода (например, закомментированная строка `profile = FirefoxProfile(profile_directory=profile_directory)`).
  - Не хватает обработки исключений в некоторых местах.

**Рекомендации по улучшению:**

1.  **Форматирование и стиль кода**:
    *   Привести весь код к единому стилю с использованием одинарных кавычек.
    *   Удалить или раскомментировать неиспользуемый код.
2.  **Документация**:
    *   Дополнить документацию для всех методов и функций, указав параметры, возвращаемые значения и возможные исключения.
    *   Пересмотреть и обновить комментарии, чтобы они были более точными и соответствовали текущему коду.
3.  **Обработка ошибок**:
    *   Добавить обработку исключений в те места, где это необходимо для повышения стабильности кода.
4.  **Использование `j_loads`**:
    *   Убедиться, что для загрузки JSON-конфигураций используется `j_loads_ns` из `src.utils.jjson`.
5.  **Логирование**:
    *   Проверить, что все важные моменты работы программы логируются с использованием `logger` из `src.logger.logger`.

**Оптимизированный код:**

```python
## \file /src/webdriver/firefox/firefox.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
rst
.. module:: src.webdriver.firefox
    :synopsys: Модуль для работы с WebDriver Firefox
"""

"""
WebDriver Firefox
=========================================================================================

Модуль содержит класс :class:`Firefox`, который расширяет функционал стандартного
`webdriver.Firefox`. Он предоставляет возможность настройки пользовательского профиля,
запуска в режиме киоска и установки пользовательских настроек, включая прокси.

Пример использования
--------------------

Пример использования класса `Firefox`:\

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

import os
import sys
import random
from pathlib import Path
from typing import Optional, List

from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException

from src import gs
#  добавление импорта
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

    Args:
        profile_name (Optional[str]): Имя пользовательского профиля Firefox.
        geckodriver_version (Optional[str]): Версия geckodriver.
        firefox_version (Optional[str]): Версия Firefox.
        user_agent (Optional[str]): Пользовательский агент в формате строки.
        proxy_file_path (Optional[str]): Путь к файлу с прокси.
        options (Optional[List[str]]): Список опций для Firefox.
        window_mode (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).
    """

    driver_name: str = 'firefox'
    service: 'Service'

    def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 options: Optional[List[str] = None],
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
        """
        Инициализация экземпляра класса Firefox.

        Args:
            profile_name (Optional[str]): Имя пользовательского профиля Firefox.
            geckodriver_version (Optional[str]): Версия geckodriver.
            firefox_version (Optional[str]): Версия Firefox.
            user_agent (Optional[str]): Пользовательский агент в формате строки.
            proxy_file_path (Optional[str]): Путь к файлу с прокси.
            options (Optional[List[str]]): Список опций для Firefox.
            window_mode (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.).

        """
        logger.info('Запуск Firefox WebDriver')
        #  объявление переменных
        profile = None
        options_obj = None
        #  Загрузка настроек Firefox
        config = j_loads_ns(Path(gs.path.src, 'webdriver', 'firefox', 'firefox.json'))
        #  Путь к geckodriver и бинарнику Firefox
        geckodriver_path: str = str(Path(gs.path.root, config.executable_path.geckodriver))
        firefox_binary_path: str = str(Path(gs.path.root, config.executable_path.firefox_binary))
        #  Инициализация сервиса
        service = Service(geckodriver_path)
        #  Настройка опций Firefox
        options_obj = Options()

        #  Добавление опций из файла настроек
        if hasattr(config, 'options') and config.options:
            for option in config.options:
                options_obj.add_argument(option)

        #  Установка режима окна из параметров
        if window_mode:
            options_obj.add_argument(f'--{window_mode}')

        #  Добавление опций, переданных при инициализации
        if options:
            for option in options:
                options_obj.add_argument(option)

        #  Добавление заголовков из настроек
        if hasattr(config, 'headers') and config.headers:
            for key, value in vars(config.headers).items():
                options_obj.add_argument(f'--{key}={value}')

        #  Установка пользовательского агента
        user_agent = user_agent or UserAgent().random
        options_obj.set_preference('general.useragent.override', user_agent)

        #  Установка прокси, если включены
        if hasattr(config, 'proxy_enabled') and config.proxy_enabled:
            self.set_proxy(options_obj)

        #  Настройка директории профиля
        profile_directory = config.profile_directory.os if config.profile_directory.default == 'os' else str(
            Path(gs.path.src, config.profile_directory.internal))

        if profile_name:
            profile_directory = str(Path(profile_directory).parent / profile_name)
        if '%LOCALAPPDATA%' in profile_directory:
            profile_directory = Path(profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA')))

        # profile = FirefoxProfile(profile_directory=profile_directory) <- @debug не грузится профиль

        try:

            super().__init__(service=service, options=options_obj)
            self._payload()
            logger.success(f'Браузер запустился {window_mode=}')
        except WebDriverException as ex:
            logger.critical("""
                ---------------------------------
                    Ошибка запуска WebDriver
                    Возможные причины:
                    - Обновление Firefox
                    - Отсутствие Firefox на ОС
                ----------------------------------""", ex)
            ...
            sys.exit(1)
        except Exception as ex:
            logger.critical('Ошибка Firefox WebDriver:', ex, exc_info=True)
            return

    def set_proxy(self, options: Options) -> None:
        """
        Настройка прокси из словаря, возвращаемого get_proxies_dict.

        Args:
            options (Options): Опции Firefox, в которые добавляются настройки прокси.
        """
        #  Получение словаря прокси
        proxies_dict = get_proxies_dict()
        #  Создание списка всех прокси
        all_proxies = proxies_dict.get('socks4', []) + proxies_dict.get('socks5', [])
        #  Перебор прокси для поиска рабочего
        working_proxy = None
        for proxy in random.sample(all_proxies, len(all_proxies)):
            if check_proxy(proxy):
                working_proxy = proxy
                break
        #  Настройка прокси, если он найден
        if working_proxy:
            proxy = working_proxy
            protocol = proxy.get('protocol')
            #  Настройка прокси в зависимости от протокола
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
        Загружает исполнителей для локаторов и JavaScript сценариев.
        """
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
```