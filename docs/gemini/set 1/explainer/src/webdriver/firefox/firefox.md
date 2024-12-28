# <input code>

```python
## \file hypotez/src/webdriver/firefox/firefox.py
# -*- coding: utf-8 -*-\
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
        # ... (остальной код)
```

# <algorithm>

**Шаг 1:** Инициализация переменных: `service`, `profile`, `options`.


**Шаг 2:** Загрузка настроек из файла `firefox.json` в переменную `settings`.


**Шаг 3:** Получение путей к `geckodriver` и `Firefox` бинарнику из `settings`.


**Шаг 4:** Инициализация сервиса `Service` с путем к `geckodriver`.


**Шаг 5:** Настройка опций `Options`:
    * Добавление аргументов, настроенных в `settings.options`.
    * Добавление заголовков, настроенных в `settings.headers`.


**Шаг 6:** Установка пользовательского агента (`user_agent`) или случайного с помощью `UserAgent`.


**Шаг 7:** Если `proxy_enabled` в `settings` - настройка прокси (метод `set_proxy`).


**Шаг 8:** Настройка профиля Firefox.
    * Использует `profile_directory` из `settings`, а если `profile_name` задан, то используется путь к профилю внутри.
    * Обработка специального символа `%LOCALAPPDATA%`, чтобы работать с переменной окружения.
    * Создание объекта `FirefoxProfile`.


**Шаг 9:** Инициализация WebDriver:
    * Запуск WebDriver с настройками.
    * Вызов `_payload()` после инициализации драйвера для выполнения пользовательских действий.


**Шаг 10:** Обработка исключений `WebDriverException` и других исключений.


**Шаг 11:** В методе `set_proxy`:
   * Получение прокси из `get_proxies_dict`.
   * Выбор случайного рабочего прокси (с помощью `check_proxy`) из списка доступных прокси.
   * Настройка прокси в `options` в зависимости от типа протокола.


**Шаг 12:** В методе `_payload`:
   * Инициализация объектов `JavaScript` и `ExecuteLocator`.
   * Назначение обработчиков для различных задач (например, `get_page_lang`, `execute_locator`).


**Пример данных:**

* `settings`: `{ "executable_path": { "geckodriver": "/path/to/geckodriver", "firefox_binary": "/path/to/firefox" }, ...}`
* `profile_name`: "custom_profile"
* `user_agent`: "Mozilla/5.0 ..."
* `proxies_dict`: `{"socks4": [{"host": "127.0.0.1", "port": "9050", "protocol": "socks4"}], "socks5": [...]}
* `working_proxy`: `{"host": "127.0.0.1", "port": "9050", "protocol": "socks4"}`

Данные передаются между функциями и классами через аргументы, атрибуты и возвращаемые значения. Например, `get_proxies_dict` возвращает `proxies_dict`, который используется в `set_proxy`. `settings` передаются из `gs` и `firefox.json`.


# <mermaid>

```mermaid
graph LR
    A[main] --> B(Firefox);
    B --> C{Настройки из firefox.json};
    C --> D[Загрузка geckodriver и Firefox];
    D --> E[Инициализация FirefoxProfile];
    E --> F[Настройка прокси (set_proxy)];
    F --> G[Инициализация WebDriver];
    G --> H[Вызов _payload()];
    H --> I[Настройка исполнителей (ExecuteLocator, JavaScript)];
    I --> J[Получение страницы];
    J --> K[Выполнение действий на странице];
    subgraph "Подключаемые зависимости"
        C --> L[gs];
        L --> M[src.webdriver.executor];
        L --> N[src.webdriver.js];
        L --> O[src.webdriver.proxy];
        L --> P[src.utils.jjson];
        L --> Q[src.logger.logger];
        L --> R[fake_useragent];
    end
```

**Объяснение зависимостей в диаграмме:**

* `gs`: предоставляет глобальные настройки, пути к файлам и ресурсам.
* `src.webdriver.executor`: содержит логику для работы с локаторами элементов на странице.
* `src.webdriver.js`: содержит логику для работы с JavaScript на странице.
* `src.webdriver.proxy`: содержит функции для работы с прокси-серверами (скачивание, проверка).
* `src.utils.jjson`: содержит функции для работы с JSON-данными.
* `src.logger.logger`: содержит функции для логирования.
* `fake_useragent`: предоставляет функциональность для генерации случайных пользовательских агентов.


# <explanation>

**Импорты:**

- `os`, `random`, `pathlib`, `typing`, `selenium.webdriver.*`: Стандартные библиотеки Python и Selenium для работы с файлами, случайными числами, типизацией и веб-драйвером.
- `gs`:  Этот импорт (`from src import gs`) указывает на то, что `gs` содержит глобальные настройки и конфигурацию проекта.  `gs` вероятно определяет переменные, такие как пути к файлам, директориям и т.д.
- `src.webdriver.executor`, `src.webdriver.js`, `src.webdriver.proxy`, `src.utils.jjson`, `src.logger.logger`: Импортируются из папки `src` модули, отвечающие за разные функции, связанные с работой с веб-драйвером.  Локализация в `src` говорит о внутренней структуре проекта.

**Классы:**

- `Firefox`: Наследует от `selenium.webdriver.Firefox` и расширяет его функциональность.  Он предоставляет дополнительные возможности, такие как настройка профиля, прокси и пользовательского агента.  Атрибут `driver_name` указывает на тип драйвера.  `__init__` инициализирует все необходимое для работы драйвера, включая настройки, загрузку профиля и запуск.
- `ExecuteLocator`, `JavaScript`: Эти классы, находящиеся в подпапках `src/webdriver`, отвечают за функциональность, связанную с локаторами и JavaScript.  В `Firefox` создаются их экземпляры для использования их методов.

**Функции:**

- `__init__`: Конструктор класса `Firefox`, принимает параметры для настройки драйвера.
- `set_proxy`: Настраивает прокси-сервер для драйвера.
- `_payload`: Выполняет дополнительные действия после инициализации драйвера.


**Переменные:**

- `MODE`: Переменная, вероятно, определяющая режим работы (например, 'dev', 'prod').
- `settings`:  Объект, содержащий настройки, загруженные из файла `firefox.json`.

**Возможные ошибки и улучшения:**

- **Проверка корректности настроек:** Необходимо добавить проверку корректности пути к geckodriver, файлу с прокси, профилем, чтобы избежать ошибок при запуске.
- **Обработка пустого списка прокси:**  В коде не предусмотрена обработка случая, когда список прокси пуст.
- **Логирование ошибок:**  Добавить более подробное логирование ошибок, особенно в `set_proxy` (например, если `get_proxies_dict` вернул пустой список).
- **Улучшение выбора прокси:**  Более оптимальный алгоритм выбора прокси, например, учитывающий скорость ответа.  Использование функции рандомизации не оптимально для поиска рабочего прокси.


**Взаимосвязь с другими частями проекта:**

- `gs` содержит пути к файлам, что указывает на наличие инфраструктуры для управления конфигурацией.
-  Модули в `src.webdriver` взаимосвязаны для обеспечения комплексной работы с веб-драйвером.
- Взаимодействие с другими частями проекта осуществляется через импорты и вызовы функций.


Этот код предоставляет гибкую настройку Firefox WebDriver и имеет хорошее структурирование.  Доработка по ошибкам позволит сделать его еще более надежным и стабильным.