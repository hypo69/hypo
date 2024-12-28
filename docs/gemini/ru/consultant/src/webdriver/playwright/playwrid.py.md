# Анализ кода модуля `playwrid`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и следует объектно-ориентированному подходу.
    - Используются docstring для описания классов, методов и функций в формате reStructuredText (RST), что соответствует требованиям.
    - Присутствует обработка ошибок с использованием `logger.error`.
    - Используются `j_loads_ns` для загрузки JSON файлов.
- Минусы
    - Не все блоки `try-except` логируют ошибки.
    - Могут быть добавлены дополнительные проверки на типы переменных для повышения надежности кода.
    - Некоторые комментарии могут быть более конкретными.

**Рекомендации по улучшению**

1.  **Логирование ошибок:**
    -  Добавить `logger.error` в `try-except` блоки, чтобы логировать возникающие ошибки.
2.  **Проверка типов:**
    -  Усилить проверки типов переменных для предотвращения неожиданных ошибок.
3. **Комментарии**:
    -  Уточнить комментарии для более ясного понимания кода.
4.  **Улучшить читаемость кода:**
    -  Использовать более информативные имена переменных.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с Playwright Crawler
=========================================================================================

Этот модуль определяет подкласс `PlaywrightCrawler` под названием `Playwrid`.
Он предоставляет дополнительные возможности, такие как установка пользовательских настроек браузера,
профилей и параметров запуска с использованием Playwright.

Пример использования
--------------------

Пример использования класса `Playwrid`:

.. code-block:: python

    if __name__ == "__main__":
        browser = Playwrid(options=["--headless"])
        browser.start("https://www.example.com")
"""

MODE = 'dev'

from pathlib import Path
from typing import Optional, Dict, Any, List
from types import SimpleNamespace

from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
#  импортируем gs
from src import gs
#  импортируем j_loads_ns из  src.utils.jjson
from src.utils.jjson import j_loads_ns
#  импортируем logger для логирования
from src.logger.logger import logger


class Playwrid(PlaywrightCrawler):
    """
    Подкласс `PlaywrightCrawler`, предоставляющий дополнительные функции.

    :ivar driver_name: Имя драйвера, по умолчанию `playwrid`.
    :vartype driver_name: str
    :ivar context: Контекст страницы, по умолчанию `None`.
    :vartype context: Optional[Any]
    """
    driver_name = 'playwrid'
    context = None

    def __init__(self, settings_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Инициализирует Playwright Crawler с заданными параметрами запуска, настройками и User-Agent.

        :param settings_name: Имя файла настроек.
        :type settings_name: Optional[str]
        :param user_agent: Строка User-Agent. По умолчанию используется случайный User-Agent.
        :type user_agent: Optional[str]
        :param options: Список опций Playwright для передачи во время инициализации.
        :type options: Optional[List[str]]
        """
        # загружаем настройки
        settings = self._load_settings(settings_name)
        # устанавливаем параметры запуска браузера
        launch_options = self._set_launch_options(settings, user_agent, options)

        super().__init__(
            playwright_launch_options=launch_options,
            browser_type=settings.browser_type,
            **kwargs
        )

    def _load_settings(self, settings_name: Optional[str] = None) -> SimpleNamespace:
        """
        Загружает настройки для Playwrid Crawler.

        :param settings_name: Имя файла настроек для загрузки.
        :type settings_name: Optional[str]
        :returns: Объект SimpleNamespace, содержащий загруженные настройки.
        :rtype: SimpleNamespace
        """
        #  определяем путь к файлу с настройками по умолчанию
        settings_path = Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        #  загружаем настройки из файла по умолчанию
        settings = j_loads_ns(settings_path)

        #  проверяем, задано ли имя файла с пользовательскими настройками
        if settings_name:
            #  определяем путь к файлу с пользовательскими настройками
            custom_settings_path = settings_path.parent / f'{settings_name}.json'
            #  проверяем, существует ли файл с пользовательскими настройками
            if custom_settings_path.exists():
                # загружаем пользовательские настройки
                settings = j_loads_ns(custom_settings_path)

        return settings

    def _set_launch_options(self, settings: SimpleNamespace, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Настраивает параметры запуска для Playwright Crawler.

        :param settings: Объект SimpleNamespace, содержащий настройки запуска.
        :type settings: SimpleNamespace
        :param user_agent: Строка User-Agent для использования.
        :type user_agent: Optional[str]
        :param options: Список дополнительных опций Playwright.
        :type options: Optional[List[str]]
        :returns: Словарь с опциями запуска для Playwright.
        :rtype: Dict[str, Any]
        """
        #  инициализируем словарь с основными опциями запуска
        launch_options = {
            "headless": settings.headless if hasattr(settings, 'headless') else True,
            "args": settings.options if hasattr(settings, 'options') else []
        }

        #  добавляем пользовательский User-Agent, если он предоставлен
        if user_agent:
            launch_options['user_agent'] = user_agent

        #  расширяем список аргументов дополнительными опциями, если они предоставлены
        if options:
            launch_options['args'].extend(options)

        return launch_options

    def start(self, url: str) -> None:
        """
        Запускает Playwrid Crawler и переходит по указанному URL.

        :param url: URL для перехода.
        :type url: str
        """
        try:
            # логируем запуск краулера
            logger.info(f"Starting Playwright Crawler for {url}")
            super().run()
        except Exception as ex:
            # логируем ошибку запуска краулера
            logger.critical('Playwrid Crawler failed with an error:', ex)

    @property
    def current_url(self) -> Optional[str]:
        """
        Возвращает текущий URL браузера.

        :returns: Текущий URL.
        :rtype: Optional[str]
        """
        # проверяем, существует ли контекст страницы
        if self.context:
            return self.context.page.url
        return None


if __name__ == "__main__":
    browser = Playwrid(options=["--headless"])
    browser.start("https://www.example.com")