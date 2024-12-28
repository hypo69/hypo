# Анализ кода модуля `chrome.html`

**Качество кода**
8
-  Плюсы
    -   Код хорошо структурирован и понятен, включая docstring, комментарии, использование HTML для документации.
    -   Присутствует разделение на секции с описанием ключевых компонентов.
    -   Используется `fake_useragent` для генерации случайных user-agent.
    -   Код обработки JSON файла вынесен в отдельную функцию.
    -   Используется `logger` для логирования ошибок и важной информации.
    -   Есть обработка `WebDriverException` и общих исключений.
-  Минусы
    -  Документация в формате HTML не соответствует требованиям по reStructuredText (RST) для docstrings.
    -  В коде встречаются `return` без возвращаемого значения, которые лучше заменить на `return None`.
    -  Некоторые комментарии содержат слова "получаем", "делаем", что противоречит инструкциям.
    -  Не все функции имеют docstring.
    -   В HTML-документации не используется нумерация списков.
    -    Используется `j_loads`  а не `j_loads_ns`
    -    Не используется импорт os.path и sys.
    -    Встречаются `...` в блоке `except`

**Рекомендации по улучшению**

1.  **Переписать docstring**: Переписать все docstring в формате reStructuredText (RST).
2.  **Использовать `j_loads_ns`**: Заменить `j_loads` на `j_loads_ns`.
3.  **Обработка ошибок**:
    -   Заменить `return` в блоках `except` на `return None`
    -   Удалить `...` в блоке `except`
4. **Улучшить комментарии**: Переписать комментарии, избегая слов "получаем", "делаем" и т.п.
5. **Добавить недостающие импорты**: Добавить `import os.path`, `import sys`.
6. **Улучшить HTML**: Переписать HTML, используя нумерованные списки в разделах с компонентами.

**Оптимизированный код**

```html
# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>chrome.py Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }

        h1, h2, h3 {
            color: #2c3e50;
        }

        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
            font-size: 0.9em;
        }

        .code-block {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>chrome.py Documentation</h1>
    <p>Here’s the <code>chrome.py</code> file with Doxygen comments translated to English and formatted as requested, including a summary of the <code>chrome.json</code> file:</p>

    <div class="code-block">
        <pre><code># -*- coding: utf-8 -*-
#  module: src.webdriver.chrome._docs
#   """
#   Модуль для работы с веб-драйвером Chrome.
#   =========================================================================================
#
#   Этот модуль содержит класс :class:`Chrome`, который используется для управления экземпляром веб-драйвера Chrome.
#   Он загружает настройки из файла `chrome.json`, устанавливает различные опции и предоставляет удобный интерфейс для
#   взаимодействия с браузером.
#   """
import os
import socket
from pathlib import Path
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent

from selenium.common.exceptions import WebDriverException
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
import os.path
import sys


class Chrome(webdriver.Chrome):
    """
    Подкласс `selenium.webdriver.Chrome`, предоставляющий дополнительную функциональность.
    =========================================================================================
    
    Этот класс расширяет базовый класс `selenium.webdriver.Chrome` и включает методы для настройки
    опций Chrome, управления портами и инициализации WebDriver. Он также обеспечивает логирование
    ошибок и управление user-agent.
    """
    driver_name = 'chrome'
    d: webdriver.Chrome = None
    options: ChromeOptions = ChromeOptions()
    user_agent: dict = None

    def __init__(self, user_agent: dict = None, *args, **kwargs) -> None:
        """
        Инициализирует веб-драйвер Chrome с заданными опциями и профилем.
    
        :param user_agent:  Словарь настроек user-agent для веб-драйвера Chrome.
        :type user_agent: dict, optional
        :raises Exception: Если возникает ошибка при настройке веб-драйвера.
    
        .. note::
            Подробности о настройках user-agent можно найти по ссылке:
             https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066
        """
        self.user_agent = user_agent if user_agent else UserAgent().random
        # код загружает настройки Chrome из JSON файла
        try:
            settings: dict = j_loads_ns(Path(gs.path.src, 'webdriver', 'chrome', 'chrome.json'))
            if not settings:
                logger.critical("Ошибка в файле конфигурации 'chrome.json'.")
                return None
    
            # определяет путь к профилю пользователя Chrome
            profile_directory: str = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome for Testing', 'User Data')
            
            # устанавливает путь к ChromeDriver
            chromedriver_path_parts: list = settings['driver']['chromedriver']
            if 'chrome' in chromedriver_path_parts:
                index = chromedriver_path_parts.index('chrome')
                chromedriver_path_parts[index] = gs.default_webdriver
            chromedriver_path: str = str(Path(gs.path.bin, *chromedriver_path_parts))
            
            # устанавливает путь к бинарному файлу Chrome
            binary_location_parts: list = settings['driver']['chrome_binary']
            if 'chrome' in binary_location_parts:
                index = binary_location_parts.index('chrome')
                binary_location_parts[index] = gs.default_webdriver
            binary_location: str = str(Path(gs.path.bin, *binary_location_parts))
            
            # устанавливает опции Chrome
            self.options: ChromeOptions = self.set_options(settings)
            self.options.add_argument(f'user-data-dir={profile_directory}')
            
            # создает сервис Chrome с указанием бинарного файла
            self.service = ChromeService(executable_path=binary_location)
            
            # находит свободный порт
            free_port = gs.webdriver_current_port
            gs.webdriver_current_port += 1
            
            if free_port:
                self.options.add_argument(f'--port={free_port}')
                logger.info(f'Установлен порт веб-драйвера на {free_port}')
                
            else:
                logger.critical("Нет свободных портов в диапазоне (9500, 9599).")
                return None
    
        except Exception as e:
            logger.critical('Ошибка при настройке веб-драйвера Chrome.', exc_info=True)
            return None
        
        try:
            logger.info("Запуск веб-драйвера Chrome.")
            service = None
            super().__init__(options=self.options, service=self.service)
    
        except WebDriverException as ex:
            logger.critical("Ошибка при инициализации веб-драйвера Chrome:", ex, exc_info=True)
             # @todo Implement driver restart
            return None
        except Exception as ex:
            logger.critical("Веб-драйвер Chrome аварийно завершил работу. Общая ошибка:", ex, exc_info=True)
            # @todo Implement program restart
            return None
    
    def find_free_port(self, start_port: int, end_port: int) -> int |  None:
        """
        Ищет свободный порт в заданном диапазоне.
    
        :param start_port: Начальный порт диапазона.
        :type start_port: int
        :param end_port: Конечный порт диапазона.
        :type end_port: int
        :return: Свободный порт, если он доступен, иначе None.
        :rtype: int | None
    
        :raises Exception: Если возникает ошибка при проверке порта.
        """
        for port in range(start_port, end_port + 1):
            try:
                # проверяет доступность порта
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port))
                    return port
            except OSError as ex:
                logger.debug(f"Порт {port} занят.", exc_info=True)
        return None
    
    def set_options(self, settings: list | dict | None = None) -> ChromeOptions:
        """
        Устанавливает параметры запуска для веб-драйвера Chrome.
    
        :param settings: Настройки конфигурации для опций Chrome.
        :type settings: list | dict | None, optional
        :return: Объект `ChromeOptions` с указанными параметрами запуска.
        :rtype: ChromeOptions
    
        """
        if not settings or ('options' not in settings and 'headers' not in settings):
            return None
    
        options = ChromeOptions()
    
        if 'options' in settings:
            # преобразует список в формат [key=value, key2=value2, ...] в словарь
            options_dict = {}
            for item in settings['options']:
                key, value = item.split('=')
                options_dict[key.strip()] = value.strip()
        
            # добавляет настройки из словаря в объект ChromeOptions
            [options.add_argument(f"--{key}={value}") for key, value in options_dict.items()]
    
        if 'headers' in settings and settings['headers']:
            [options.add_argument(f"--{key}={value}") for key, value in settings['headers'].items()]
    
        return options
</code></pre>
    </div>

    <h2>Summary of <code>chrome.py</code> File</h2>
    <p>The <code>chrome.py</code> file defines a <code>Chrome</code> class that extends the <code>selenium.webdriver.Chrome</code> class to provide additional functionality for setting up and configuring a Chrome WebDriver instance. This class is designed for advanced use cases and includes methods for finding free ports, setting options, and initializing the WebDriver.</p>

    <h3>Key Components</h3>
    <ol>
        <li><strong>Imports</strong>: Standard and third-party libraries for WebDriver configuration and utilities.</li>
        <li>
            <strong><code>Chrome</code> Class</strong>:
            <ul>
                <li><strong>Purpose</strong>: Customizes and initializes a Chrome WebDriver instance with additional configuration options.</li>
                <li>
                    <strong>Attributes</strong>:
                    <ul>
                        <li><code>driver_name</code>: The name of the WebDriver being used.</li>
                        <li><code>d</code>: WebDriver instance.</li>
                        <li><code>options</code>: Chrome options for configuration.</li>
                        <li><code>user_agent</code>: User-agent settings for the WebDriver.</li>
                    </ul>
                </li>
                <li>
                    <strong>Methods</strong>:
                    <ul>
                        <li><code>__init__</code>: Initializes the Chrome WebDriver with the specified options and profile.</li>
                        <li><code>find_free_port</code>: Finds an available port in a specified range.</li>
                        <li><code>set_options</code>: Sets up Chrome options based on provided settings.</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ol>

    <h2><code>chrome.json</code> File</h2>
    <p>Here’s a brief overview of the <code>chrome.json</code> file used for configuration:</p>

    <div class="code-block">
        <pre><code>{
  "profiles": {
      "one.last.bit": {
        "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data\\\\Default",
        "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
        "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data\\\\Default"
      },
      "@todo": "Organize management from a shared storage system `Keepass`"
    },
    "locator_description": "You can use profiles from different directories. Multiple profiles can be available on the system.",

  "driver": {
    "chromedriver": [ "webdrivers", "chrome", "125.0.6422.14", "chromedriver.exe" ],
    "chrome_binary": [ "webdrivers", "chrome", "125.0.6422.14", "win64-125.0.6422.14", "chrome-win64", "chrome.exe" ],
    "locator_description": "Different driver versions are in different folders. I work with a tested version of the browser. The system updates to the latest version in the background."
  },

  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "locator_description headers": "Adjustable for any agent. Details in `fake-useragent`."
}
</code></pre>
    </div>

    <h3><code>chrome.json</code> File Components</h3>
    <ol>
        <li><strong>profiles</strong>: Defines the directories for different Chrome profiles.</li>
        <li>
            <strong>driver</strong>:
            <ul>
                <li><code>chromedriver</code>: Path configuration for ChromeDriver.</li>
                <li><code>chrome_binary</code>: Path configuration for the Chrome binary.</li>
            </ul>
        </li>
        <li><strong>headers</strong>: Default headers for the WebDriver, including user-agent and other HTTP headers.</li>
    </ol>

    <p>Feel free to ask if you need more details or further adjustments!</p>
</body>
</html>
```