# <input code>

```python
## \file hypotez/src/webdriver/chrome/chrome.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Module for Chrome WebDriver
=========================================================================================

This module contains a custom implementation of the Chrome WebDriver using Selenium. It integrates
configuration settings defined in the `chrome.json` file, such as user-agent and browser profile settings,
to enable flexible and automated browser interactions.

Key Features:
    - Centralized configuration via JSON files.
    - Support for multiple browser profiles.
    - Enhanced logging and error handling.

Example usage
--------------------

Example of using the `Chrome` class:

.. code-block:: python

    from src.webdriver.chrome import Chrome

    # Initialize Chrome WebDriver with user-agent settings
    browser = Chrome(user_agent='Mozilla/5.0...')
    browser.get("https://www.example.com")
    browser.quit()
"""

MODE = 'dev'

import os
import sys
from pathlib import Path
from typing import Optional
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException

import header
from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.utils.jjson import j_loads_ns
from src.logger import logger


class Chrome(webdriver.Chrome):
    """Class for Chrome WebDriver."""

    _instance = None
    driver_name: str = 'chrome'
    config: SimpleNamespace

    def __new__(cls, *args, **kwargs):
        """Ensure a single instance of Chrome WebDriver.

        If an instance already exists, it calls `window_open()`.

        Returns:
            Chrome: The singleton instance of the Chrome WebDriver.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._instance.window_open()  # Open a new window if instance already exists
        return cls._instance

    def __init__(self, user_agent: Optional[str] = None, *args, **kwargs):
        """Initializes the Chrome WebDriver with specified options and profile.

        Args:
            user_agent (Optional[str]): The user-agent string to be used. Defaults to a random user agent.
        """
        # ... (rest of the code)
```

# <algorithm>

**Шаг 1: Инициализация**

- Проверяет, существует ли уже экземпляр класса `Chrome`. Если нет, создаёт новый. В противном случае, вызывает метод `window_open()` для открытия нового окна.

**Пример:**

При первом запуске программы создается новый экземпляр `Chrome`. При повторном вызове - вызывается `window_open()`.

**Шаг 2: Загрузка настроек из конфигурационного файла `chrome.json`**

- Загружает настройки из файла `chrome.json` используя функцию `j_loads_ns`.
- Проверяет корректность загрузки и при ошибке возвращает, возможно, выводит сообщение об ошибке.


**Пример:**

Если в файле `chrome.json` не найдены важные параметры, то выполнение данной части прерывается.

**Шаг 3: Настройка параметров WebDriver**

- Создаёт экземпляр `ChromeOptions`.
- Добавляет аргументы (`--user-agent`, `--profile-directory` и др.) в `options` на основе данных из `chrome.json`.
- Настраивает путь к исполняемому файлу Chrome (`binary_location`).
- Настраивает путь к профилю Chrome (`profile_directory`).
- Создаёт экземпляр `ChromeService`.

**Пример:**

Если в `chrome.json` указано `--disable-gpu`, то он добавляется в `options`.

**Шаг 4: Инициализация WebDriver**

- Создает экземпляр `webdriver.Chrome` с настроенными `options` и `service`.
- Обрабатывает возможные исключения (`WebDriverException`).


**Пример:**

Если при запуске Chrome возникает ошибка, она обрабатывается и выводится сообщение об ошибке.

**Шаг 5: Загрузка дополнительных функций**

- Вызывает метод `_payload()` для инициализации вспомогательных функций (JavaScript).
- Загружает функции `ExecuteLocator` и `JavaScript` из других модулей.
- Присваивает `self` методы этих функций для использования в главном классе.

**Пример:**

Теперь можно получить `get_page_lang`, `execute_locator`, и т.д.


# <mermaid>

```mermaid
graph LR
    A[Chrome()] --> B{Проверка экземпляра};
    B -- Да --> C[window_open()];
    B -- Нет --> D[j_loads_ns("chrome.json")];
    D -- Успех --> E[Настройка options];
    E --> F[Создание ChromeService];
    F --> G[webdriver.Chrome(options, service)];
    G --> H{_payload()};
    H --> I[JavaScript(), ExecuteLocator()];
    I --> J[Инициализация методов];
    J --> K[get, quit];
    subgraph "Функции JavaScript и ExecuteLocator"
        I -- JavaScript --> L[get_page_lang, ...];
        I -- ExecuteLocator --> M[execute_locator, ...];
    end
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#ccf,stroke:#333,stroke-width:2px;
    style C fill:#ccf,stroke:#333,stroke-width:2px;
    style D fill:#ccf,stroke:#333,stroke-width:2px;
    style E fill:#ccf,stroke:#333,stroke-width:2px;
    style F fill:#ccf,stroke:#333,stroke-width:2px;
    style G fill:#ccf,stroke:#333,stroke-width:2px;
    style H fill:#ccf,stroke:#333,stroke-width:2px;
    style I fill:#ccf,stroke:#333,stroke-width:2px;
    style J fill:#ccf,stroke:#333,stroke-width:2px;
    style K fill:#ccf,stroke:#333,stroke-width:2px;
    style L fill:#ccf,stroke:#333,stroke-width:2px;
    style M fill:#ccf,stroke:#333,stroke-width:2px;

```

**Объяснение зависимостей:**

- `j_loads_ns` - из `src.utils.jjson` для парсинга JSON конфигурации.
- `JavaScript`, `ExecuteLocator` - из `src.webdriver.js` и `src.webdriver.executor` соответственно, для работы с JS-кодом и локаторами.
- `ChromeService` и `ChromeOptions` - из `selenium.webdriver.chrome`.
- `logger` - из `src.logger` для ведения журнала.
- `gs` - из `src` вероятно для доступа к системным переменным и путям.
- `header` - из `src` - неизвестное назначение без кода. Возможно, подключает дополнительные модули.


# <explanation>

**Импорты:**

- `os`, `sys`, `pathlib`, `typing`, `types`, `fake_useragent`, `selenium` и т.д. - стандартные и сторонние библиотеки Python, используемые для работы с файловой системой, обработкой данных, управлением браузером, обработкой ошибок и т.д.
- `header` - неизвестное назначение без кода. Полагаем, что это импорт дополнительных модулей, но точная роль неясна без полного кода.
- `gs` - из `src` вероятно для доступа к системным переменным и путям, для работы с конфигурацией.
- `j_loads_ns` из `src.utils.jjson` - функция для загрузки настроек из JSON.
- `logger` из `src.logger` - система логгирования.

**Классы:**

- `Chrome(webdriver.Chrome)` - класс для работы с Chrome WebDriver. Наследует `webdriver.Chrome` и реализует singleton-паттерн (только один экземпляр).
   - `_instance`: Статическая переменная для поддержания singleton-паттерна.
   - `driver_name`: имя драйвера
   - `config`: Объект `SimpleNamespace` для хранения загруженных настроек из `chrome.json`.
   - `__new__`: переопределенный метод для создания единственного экземпляра класса.
   - `__init__`: инициализирует WebDriver с опциями из конфигурационного файла.

**Функции:**

- `normalize_path`:  Принимает строку пути, заменяет плейсхолдеры (например, `%APPDATA%`) на соответствующие значения из окружения.
- `_payload`: Загружает вспомогательные функции для работы с JavaScript и локаторами.

**Переменные:**

- `user_agent`: строка, используемая в качестве User-Agent в запросах к веб-сайтам.

**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Класс `Chrome` содержит множество блоков `try...except`, но, например, в некоторых местах обработка ошибки `except Exception` кажется избыточной, так как может маскировать более специфичные ошибки.  Улучшение - более детальная и точная обработка исключений.
- **Конфигурация:** Настройки хранятся в `chrome.json`, но нет ясности о структуре этого файла.
- **Уровни логирования:** Использование `logger.debug`, `logger.error` и `logger.critical` - хороший подход, но следует использовать различные уровни логирования (`WARNING`, `INFO`) для более эффективной диагностики.
- **Singleton-паттерн:**  Возможно, использование Singleton-паттерна может ограничивать тесты. Обсуждение более подходящих решений, если singleton не нужен в данном случае.
- **Поведение при отсутствии файла `chrome.json` или ошибок в нем:** Программа  не обрабатывает ситуацию, когда файл `chrome.json` отсутствует или имеет неправильный формат. Необходимо добавить дополнительную проверку на наличие и корректность файла.
- **Документация:** Документация в коде довольно подробная, но может быть ещё улучшена (например,  описания типов аргументов и возвращаемых значений).

**Взаимосвязи с другими частями проекта:**

- Класс `Chrome` напрямую взаимодействует с `src.webdriver.executor`, `src.webdriver.js` и `src.utils.jjson`.
- Подключены зависимости для работы с Selenium, `fake_useragent`, обработкой ошибок и файловой системы.