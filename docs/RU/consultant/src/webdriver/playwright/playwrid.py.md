# Анализ кода модуля `playwrid.py`

**Качество кода: 8**
-  Плюсы
    - Код хорошо структурирован, с использованием классов и методов.
    - Присутствует документация в формате docstring для классов и методов.
    - Используется `j_loads_ns` для загрузки JSON-файлов.
    - Применено логирование с использованием `logger`.
    - Есть обработка ошибок с помощью `try-except` и `logger.error`.
    - Наличие примера использования в `if __name__ == "__main__":`
-  Минусы
    - Некоторые docstring не соответствуют стандарту rst и не включают примеры использования.
    - Используется `if hasattr(settings, 'headless')` вместо более явной проверки.
    - Обработка ошибок в методе `start` не позволяет продолжить работу программы после ошибки.
    -  Не все docstring содержат описание типов параметров и возвращаемого значения.

**Рекомендации по улучшению**

1.  **Улучшение документации**:
    - Добавить примеры использования в docstring.
    - Уточнить типы параметров и возвращаемых значений в docstring.
    - Добавить описание исключений, которые могут быть вызваны функциями.
    - Использовать rst-формат для docstring.
2.  **Улучшение обработки параметров**:
    - Заменить `if hasattr(settings, 'headless')` на более явную проверку, например, `settings.get('headless', True)`.
3.  **Обработка ошибок**:
    - Изменить обработку ошибок в методе `start` для более гибкой работы (например, возможность перезапустить браузер).
4.  **Использование `logger`**:
    -   Использовать `logger.error` вместо `logger.critical` для обработки ошибок, которые не являются критическими.
5.  **Улучшение читаемости кода**:
    - Добавить type hint для `settings` в методе `_set_launch_options`.
6.  **Соответствие стандартам кода**:
    - Использовать одинарные кавычки для строк в коде, двойные - только в операциях вывода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.playwright
    :platform: Windows, Unix
    :synopsis: Playwright Crawler

This module defines a subclass of `PlaywrightCrawler` called `Playwrid`.
It provides additional functionality such as the ability to set custom browser settings, profiles,
and launch options using Playwright.

Example usage:

.. code-block:: python

    if __name__ == "__main__":
        browser = Playwrid(options=['--headless'])
        browser.start('https://www.example.com')
"""

from pathlib import Path
from typing import Optional, Dict, Any, List
from types import SimpleNamespace
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger # import logger


class Playwrid(PlaywrightCrawler):
    """
    Subclass of `PlaywrightCrawler` that provides additional functionality.

    :ivar driver_name: Name of the driver, defaults to 'playwrid'.
    :vartype driver_name: str
    """
    driver_name = 'playwrid'
    context = None

    def __init__(self, settings_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Initializes the Playwright Crawler with the specified launch options, settings, and user agent.

        :param settings_name: Name of the settings file to use.
        :type settings_name: Optional[str]
        :param user_agent: The user-agent string to be used. Defaults to a random user agent.
        :type user_agent: Optional[str]
        :param options: A list of Playwright options to be passed during initialization.
        :type options: Optional[List[str]]

        Example:
            >>> browser = Playwrid(options=['--headless'])
            >>> browser.start('https://www.example.com')
        """
        # код исполняет загрузку настроек
        settings = self._load_settings(settings_name)
        # код исполняет настройку параметров запуска
        launch_options = self._set_launch_options(settings, user_agent, options)

        super().__init__(
            playwright_launch_options=launch_options,
            browser_type=settings.browser_type,
            **kwargs
        )

    def _load_settings(self, settings_name: Optional[str] = None) -> SimpleNamespace:
        """
        Loads the settings for the Playwrid Crawler.

        :param settings_name: Name of the settings file to use.
        :type settings_name: Optional[str]
        :returns: A SimpleNamespace object containing the settings.
        :rtype: SimpleNamespace

        Example:
            >>> settings = _load_settings('custom_settings')
        """
        # код исполняет получение пути к файлу настроек
        settings_path = Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        # код исполняет загрузку настроек
        settings = j_loads_ns(settings_path)

        # код исполняет проверку наличия дополнительных настроек
        if settings_name:
            custom_settings_path = settings_path.parent / f'{settings_name}.json'
            # код исполняет загрузку дополнительных настроек
            if custom_settings_path.exists():
                settings = j_loads_ns(custom_settings_path)

        return settings

    def _set_launch_options(self, settings: SimpleNamespace, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Configures the launch options for the Playwright Crawler.

        :param settings: A SimpleNamespace object containing launch settings.
        :type settings: SimpleNamespace
        :param user_agent: The user-agent string to be used.
        :type user_agent: Optional[str]
        :param options: A list of Playwright options to be passed during initialization.
        :type options: Optional[List[str]]
        :returns: A dictionary with launch options for Playwright.
        :rtype: Dict[str, Any]

        Example:
            >>> settings = SimpleNamespace(headless=False, options=['--disable-gpu'])
            >>> launch_options = _set_launch_options(settings, user_agent='custom_user_agent', options=['--proxy-server=127.0.0.1:8888'])
        """
        # код инициализирует параметры запуска
        launch_options = {
            'headless': settings.headless if hasattr(settings, 'headless') else True,
            'args': settings.options if hasattr(settings, 'options') else []
        }

        # код добавляет пользовательский user-agent, если он предоставлен
        if user_agent:
            launch_options['user_agent'] = user_agent

        # код объединяет пользовательские параметры с параметрами по умолчанию
        if options:
            launch_options['args'].extend(options)

        return launch_options

    def start(self, url: str) -> None:
        """
        Starts the Playwrid Crawler and navigates to the specified URL.

        :param url: The URL to navigate to.
        :type url: str

        Example:
            >>> browser = Playwrid(options=['--headless'])
            >>> browser.start('https://www.example.com')
        """
        try:
            # код исполняет запуск Playwright Crawler
            logger.info(f'Starting Playwright Crawler for {url}')
            super().run()
        except Exception as ex:
            # код исполняет логирование ошибки
            logger.error('Playwrid Crawler failed with an error:', ex)
            ... # TODO: Добавить возможность перезапуска браузера

    @property
    def current_url(self) -> Optional[str]:
        """
        Returns the current URL of the browser.

        :returns: The current URL.
        :rtype: Optional[str]

        Example:
            >>> browser = Playwrid(options=['--headless'])
            >>> browser.start('https://www.example.com')
            >>> current_url = browser.current_url
        """
        # код проверяет наличие контекста
        if self.context:
            return self.context.page.url
        return None


if __name__ == '__main__':
    browser = Playwrid(options=['--headless'])
    browser.start('https://www.example.com')
```