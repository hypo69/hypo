# Анализ кода модуля `playwrid.py`

**Качество кода**
8
- Плюсы
    - Код структурирован и разбит на логические блоки.
    - Используются классы и наследование для расширения функциональности.
    - Присутствует базовая обработка ошибок с использованием `try-except` и `logger`.
    - Используется `j_loads_ns` для загрузки настроек из JSON.
    - Добавлено логгирование запуска и ошибок.
 - Минусы
    - Отсутствуют docstring для функций `current_url`.
    - Не все функции имеют docstring в формате reStructuredText (RST).
    - Использованы общие блоки `try-except` вместо более точного логирования.
    - Необходимо добавить более подробные комментарии и docstring в RST формате.
    - Не хватает проверки на существование `user_agent` и других ключей, чтобы избежать ошибок доступа к атрибутам.
    - Присутствует использование `...` в `current_url`, что не является хорошей практикой.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате RST для всех функций и классов.
    -   Переписать docstring для `__init__` и других методов в соответствии с RST стандартами.
2.  **Обработка ошибок**:
    -   Улучшить обработку ошибок, используя `logger.error` вместо общих `try-except`.
    -   Логировать конкретные ошибки при доступе к атрибутам `settings`.
3.  **Импорты**:
    -   Проверить и добавить отсутствующие импорты.
4.  **Рефакторинг**:
    -   Изменить `current_url` на метод, а не свойство.
    -   Убрать `...` в `current_url` и добавить логику получения текущего URL.
    -   Добавить проверку на наличие ключей в словаре `settings` перед их использованием.
5.  **Комментарии**:
    -   Добавить комментарии к коду с использованием `#` для пояснения действий.
6.  **Соответствие стилю**:
    -   Использовать одинарные кавычки `'` во всем коде.
    -   Привести имена переменных и функций к единому стилю.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Playwright Crawler.
=========================================================================================

Этот модуль определяет подкласс `PlaywrightCrawler` под названием `Playwrid`.
Он предоставляет дополнительные функции, такие как возможность устанавливать пользовательские настройки браузера, профили и параметры запуска с помощью Playwright.

Пример использования
--------------------

Пример использования класса `Playwrid`:

.. code-block:: python

    if __name__ == "__main__":
        browser = Playwrid()
        browser.start("https://www.example.com")
"""

from pathlib import Path
from typing import Optional, Dict, Any
from types import SimpleNamespace
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


MODE = 'dev'


class Playwrid(PlaywrightCrawler):
    """
    Подкласс `PlaywrightCrawler`, предоставляющий дополнительные функциональные возможности.

    :ivar driver_name: Имя драйвера.
    :vartype driver_name: str
    :ivar context: Контекст браузера.
    :vartype context: Any
    """

    driver_name = 'playwrid'
    context = None

    def __init__(self, settings_name: Optional[str] = None, user_agent: Optional[Dict[str, Any]] = None, *args, **kwargs) -> None:
        """
        Инициализирует Playwright Crawler с заданными параметрами запуска, настройками и пользовательским агентом.

        :param settings_name: Имя файла настроек для использования.
        :type settings_name: str, optional
        :param user_agent: Словарь, содержащий настройки пользовательского агента.
        :type user_agent: dict, optional
        :raises FileNotFoundError: If the settings file does not exist.
        """
        # код загружает настройки из JSON файла
        try:
            settings = self._load_settings(settings_name)
        except FileNotFoundError as ex:
             logger.error(f'Ошибка загрузки файла настроек {settings_name}: {ex}')
             raise

        # код устанавливает параметры запуска браузера
        launch_options = self._set_launch_options(settings)

        # код инициализирует родительский класс PlaywrightCrawler
        super().__init__(
            playwright_launch_options=launch_options,
            browser_type=settings.browser_type,
            **kwargs
        )

    def _load_settings(self, settings_name: Optional[str] = None) -> SimpleNamespace:
        """
        Загружает настройки для Playwrid Crawler.

        :param settings_name: Имя файла настроек для использования.
        :type settings_name: str, optional
        :return: Объект SimpleNamespace, содержащий настройки.
        :rtype: SimpleNamespace
        :raises FileNotFoundError: If the settings file does not exist.
        """
        # код формирует путь к файлу настроек по умолчанию
        settings_path = Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')
        # код загружает настройки из файла
        settings = j_loads_ns(settings_path)

        # код проверяет, передано ли имя пользовательского файла настроек
        if settings_name:
            # код формирует путь к пользовательскому файлу настроек
            custom_settings_path = settings_path.parent / f'{settings_name}.json'
            # код проверяет наличие файла пользовательских настроек
            if custom_settings_path.exists():
                # код загружает пользовательские настройки
                settings = j_loads_ns(custom_settings_path)
            else:
                logger.error(f'Файл настроек {custom_settings_path} не найден')
                raise FileNotFoundError(f'Файл настроек {custom_settings_path} не найден')

        return settings

    def _set_launch_options(self, settings: SimpleNamespace) -> Dict[str, Any]:
        """
        Настраивает параметры запуска для Playwright Crawler.

        :param settings: Объект SimpleNamespace, содержащий параметры запуска.
        :type settings: SimpleNamespace
        :return: Словарь с параметрами запуска для Playwright.
        :rtype: dict
        """
        # код устанавливает базовые параметры запуска
        options = {
            'headless': getattr(settings, 'headless', True),
            'args': getattr(settings, 'options', [])
        }

        # код проверяет наличие пользовательского агента в настройках
        if hasattr(settings, 'user_agent'):
            options['user_agent'] = settings.user_agent
        return options

    def start(self, url: str) -> None:
        """
        Запускает Playwrid Crawler и переходит по указанному URL.

        :param url: URL для перехода.
        :type url: str
        """
        try:
            # код логирует начало работы краулера
            logger.info(f'Запуск Playwright Crawler для {url}')
            # код запускает краулер
            super().run()
        except Exception as ex:
            # код логирует ошибку запуска краулера
            logger.critical(f'Playwrid Crawler не запустился с ошибкой: {ex}')
            ...

    def current_url(self) -> Optional[str]:
        """
        Возвращает текущий URL открытой страницы.

        :return: Текущий URL страницы или None, если URL не удалось получить.
        :rtype: str, optional
        """
        try:
            # код пытается получить текущий URL из контекста браузера
            if self.context and self.context.page:
                return self.context.page.url
            else:
                logger.error('Не удалось получить текущий URL: Контекст или страница браузера не инициализированы.')
                return None
        except Exception as ex:
            # код логирует ошибку при получении URL
            logger.error(f'Ошибка при получении текущего URL: {ex}')
            return None

```