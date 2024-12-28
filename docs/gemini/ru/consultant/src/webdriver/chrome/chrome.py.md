# Анализ кода модуля `chrome.py`

**Качество кода**
   - Соответствие требованиям по оформлению кода: 7/10
    - Плюсы
        -  Используется reStructuredText (RST) для docstring.
        -  Присутствует базовая обработка ошибок с использованием `try-except` и `logger.error`.
        -  Применяется `j_loads_ns` для загрузки JSON.
        -  Используется `fake-useragent` для генерации случайных user-agent.
        -  Реализован Singleton для управления экземпляром драйвера.
        -  Код хорошо структурирован с разделением ответственности.

    - Минусы
        -  Не везде используются docstring в формате reStructuredText (RST).
        -  Не все функции и методы имеют подробные RST-комментарии.
        -  В некоторых местах обработка исключений недостаточно детализирована.
        -  Избыточное использование блоков `try-except`, можно заменить на обработку с помощью `logger.error`.
        -  Некоторые комментарии после `#` недостаточно информативны.
        -  Импорт `header` без использования.
        -  Не соблюдается PEP8 в некоторых местах.
        -  Отсутствует проверка на существование директорий `profile_directory` и `binary_location`

**Рекомендации по улучшению**

1.  **Документация**:
    *   Добавить недостающие docstring в формате reStructuredText (RST) для всех функций, методов и класса, включая переменные.
    *   Переписать существующие комментарии в стиле RST.
    *   Соблюдать стандарты оформления docstring в Python (например, для Sphinx).
    *   Добавить более информативные комментарии после `#` для объяснения кода.
2.  **Импорты**:
    *   Удалить неиспользуемый импорт `header`.
3.  **Обработка ошибок**:
    *   Улучшить обработку ошибок с использованием `logger.error` и убрать избыточные блоки `try-except`.
4.  **Рефакторинг**:
    *   Соблюдать PEP8, улучшить читаемость кода (пробелы, длинна строк).
    *   Проверить на существование директорий `profile_directory` и `binary_location`.
    *   Улучшить именование переменных и методов.
    *   Добавить более подробные логи.
5.  **Безопасность**:
    *   Убедиться, что пути к файлам и каталогам безопасны и не допускают обхода каталогов.

**Оптимизированный код**

```python
"""
Модуль для управления Chrome WebDriver.
=========================================================================================

Этот модуль содержит класс :class:`Chrome`, который представляет собой
пользовательскую реализацию Chrome WebDriver, использующую Selenium.
Он интегрирует настройки конфигурации, определенные в файле `chrome.json`,
такие как user-agent и настройки профиля браузера, для обеспечения
гибкого и автоматизированного взаимодействия с браузером.

Основные характеристики:
    - Централизованная конфигурация через JSON-файлы.
    - Поддержка нескольких профилей браузера.
    - Улучшенное логирование и обработка ошибок.
    - Возможность передачи пользовательских параметров во время инициализации.

Пример использования
--------------------

Пример использования класса `Chrome`:

.. code-block:: python

    from src.webdriver.chrome import Chrome

    # Инициализация Chrome WebDriver с настройками user-agent и пользовательскими параметрами
    browser = Chrome(user_agent='Mozilla/5.0...', options=["--headless", "--disable-gpu"])
    browser.get("https://www.example.com")
    browser.quit()
"""

import os
import sys
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException

from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger




class Chrome(webdriver.Chrome):
    """
    Класс для управления Chrome WebDriver.

    Этот класс расширяет Selenium Chrome WebDriver и предоставляет шаблон singleton
    и пользовательские конфигурации.
    """

    _instance = None
    """
    _instance (Chrome): Единственный экземпляр Chrome WebDriver.
    """
    driver_name: str = 'chrome'
    """
    driver_name (str): Имя драйвера ('chrome').
    """
    config: SimpleNamespace
    """
    config (SimpleNamespace): Настройки конфигурации, загруженные из JSON-файла.
    """

    def __new__(cls, *args, **kwargs):
        """
        Гарантирует единственный экземпляр Chrome WebDriver.

        Если экземпляр уже существует, вызывается метод `window_open()`.

        :return: Единственный экземпляр Chrome WebDriver.
        :rtype: Chrome
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            # Открывает новое окно, если экземпляр уже существует.
            cls._instance.window_open()
        return cls._instance

    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs):
        """
        Инициализирует Chrome WebDriver с указанными параметрами и профилем.

        :param user_agent: Строка user-agent для использования.
                           По умолчанию используется случайный user agent.
        :type user_agent: Optional[str]
        :param options: Список параметров Chrome для передачи во время инициализации.
        :type options: Optional[List[str]]
        """
        try:
            # Устанавливает user_agent или генерирует случайный.
            user_agent = user_agent or UserAgent().random
            # Загружает конфигурацию из JSON-файла.
            self.config = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))

            # Проверяет, загружена ли конфигурация.
            if not self.config:
                logger.error('Ошибка в файле `chrome.json`.')
                return

            # Инициализирует объект параметров.
            options_obj = ChromeOptions()

            # Добавляет аргументы из конфигурации.
            if hasattr(self.config, 'options') and self.config.options:
                for option in self.config.options:
                    options_obj.add_argument(option)

            # Добавляет пользовательские параметры.
            if options:
                for option in options:
                    options_obj.add_argument(option)

            # Добавляет заголовки из конфигурации.
            if hasattr(self.config, 'headers') and self.config.headers:
                for key, value in vars(self.config.headers).items():
                    options_obj.add_argument(f'--{key}={value}')

            def normalize_path(path: str) -> str:
                """
                Заменяет плейсхолдеры фактическими путями среды.

                :param path: Путь со специальными плейсхолдерами,
                              например %APPDATA% или %LOCALAPPDATA%.
                :type path: str
                :return: Нормализованный путь с подставленными переменными среды.
                :rtype: str
                """
                if not path:
                    return ''
                return (
                    path.replace('%APPDATA%', os.environ.get('APPDATA', ''))
                    .replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA', ''))
                )

            # Нормализуем пути к профилю и бинарному файлу.
            profile_directory = Path(gs.path.root / normalize_path(self.config.profile_directory.testing))
            binary_location = Path(gs.path.root / normalize_path(self.config.binary_location.binary))


            # Проверяет существование директории профиля и добавляет аргумент.
            if profile_directory.exists():
                options_obj.add_argument(f'user-data-dir={profile_directory}')
            else:
                logger.error(f'Директория профиля не найдена: {profile_directory}')

             # Проверяет существование бинарного файла.
            if binary_location.exists():
                  # Устанавливает путь к исполняемому файлу.
                options_obj.binary_location = str(binary_location)
                # Инициализирует сервис Chrome Driver.
                service = ChromeService(executable_path=str(binary_location))
            else:
                logger.error(f'Бинарный файл не найден: {binary_location}')
                service = ChromeService()  # Используем сервис по умолчанию
        except Exception as ex:
             logger.error('Ошибка при настройке Chrome WebDriver:', ex)
             return

        try:
            # Инициализирует WebDriver.
            super().__init__(options=options_obj, service=service)
        except WebDriverException as ex:
            logger.critical('Ошибка при инициализации Chrome WebDriver:', ex)
            return
        except Exception as ex:
            logger.critical('Chrome WebDriver аварийно завершил работу. Общая ошибка:', ex)
            return

        self._payload()

    def _payload(self) -> None:
        """
        Загружает исполнитель для локаторов и JavaScript-сценариев.

        Этот метод инициализирует и присваивает необходимые исполнители для взаимодействия
        с веб-элементами и выполнения JavaScript в WebDriver.
        """
        js_executor = JavaScript(self)
        self.get_page_lang = js_executor.get_page_lang
        self.ready_state = js_executor.ready_state
        self.get_referrer = js_executor.get_referrer
        self.unhide_DOM_element = js_executor.unhide_DOM_element
        self.window_focus = js_executor.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message

if __name__ == "__main__":
    driver = Chrome(options=["--headless", "--disable-gpu"])
    driver.get(r"https://google.com")
```