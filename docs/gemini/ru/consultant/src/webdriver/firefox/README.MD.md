# Анализ кода модуля `src.webdriver.firefox`

**Качество кода**
7
-  Плюсы
    - Документация в формате RST присутствует, что облегчает понимание структуры и функциональности модуля.
    - Предоставлены примеры использования класса `Firefox` и его основных методов.
    - Описаны требования к окружению и установке, что облегчает начало работы с модулем.
    - Присутствует описание параметров и их предназначение для конструктора и методов.
    - Структура документа понятная, с четкими заголовками и разделами.
-  Минусы
    - Отсутствуют импорты необходимых модулей в коде.
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Нет комментариев в коде, которые бы поясняли логику работы конкретных участков кода.
    - Не все блоки кода снабжены комментариями в стиле RST.
    - Отсутствует логирование ошибок с использованием `logger`.
    - Нет единого стиля оформления docstring.

**Рекомендации по улучшению**

1.  **Добавить импорты**: Включить необходимые импорты модулей, таких как `selenium`, `selenium.webdriver`, `selenium.webdriver.firefox.options`, `random`, `src.utils.jjson`, `src.logger.logger`.
2.  **Использовать `j_loads` или `j_loads_ns`**: Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson` при чтении файлов (если это необходимо в коде).
3.  **Добавить комментарии RST**: Дополнить документацию функций и методов в стиле RST, включая описания параметров, возвращаемых значений и исключений.
4.  **Логирование ошибок**: Использовать `logger.error` для логирования ошибок вместо стандартных `try-except`, где это возможно.
5.  **Стиль docstring**: Привести docstring к единому стилю, желательно с использованием Sphinx-совместимого формата.
6.  **Комментирование кода**: Добавить комментарии к ключевым участкам кода, объясняющие логику работы.

**Оптимизированный код**

```markdown
```rst
.. module:: src.webdriver.firefox

Модуль для работы с браузером Firefox
=========================================================================================

Этот модуль содержит класс :class:`Firefox`, который расширяет возможности стандартного
WebDriver Firefox. Он позволяет настраивать пользовательский профиль, запускать WebDriver
в режиме киоска и устанавливать настройки прокси.

Пример использования
--------------------

Пример использования класса `Firefox`:

.. code-block:: python

    from src.webdriver.firefox import Firefox

    if __name__ == "__main__":
        profile_name = "custom_profile"
        geckodriver_version = "v0.29.0"
        firefox_version = "78.0"
        proxy_file_path = "path/to/proxies.txt"

        # Инициализация и запуск браузера
        browser = Firefox(
            profile_name=profile_name,
            geckodriver_version=geckodriver_version,
            firefox_version=firefox_version,
            proxy_file_path=proxy_file_path,
            options=["--kiosk", "--headless"]  # Добавление опций
        )
        browser.get("https://www.example.com")
        browser.quit()
```

# Firefox WebDriver Module

This module contains the `Firefox` class, which extends the functionality of the standard Firefox WebDriver. It allows you to configure a custom profile, run the WebDriver in kiosk mode, and set proxy settings.

## Requirements

- Python 3.12+
- Selenium
- Fake User-Agent
- Proxy handling module

## Installation

1. Install all dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Ensure that the following components are installed:
   - **geckodriver** (for WebDriver support)
   - **Firefox** (supported version)

3. To work with proxies, provide the path to the proxy file using the `proxy_file_path` parameter.

## Example Usage

Example of using the `Firefox` class:

```python
from src.webdriver.firefox import Firefox

if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    # Initialize and launch the browser
    browser = Firefox(
        profile_name=profile_name,
        geckodriver_version=geckodriver_version,
        firefox_version=firefox_version,
        proxy_file_path=proxy_file_path,
        options=["--kiosk", "--headless"]  # Adding options
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Class and Method Descriptions

### `Firefox` Class

- Extends the standard Firefox WebDriver, adding functionality such as:
  - Setting a custom profile
  - Proxy settings
  - Setting a custom user agent
  - Integration with JavaScript and executing locators
  - Ability to pass options during initialization

#### `__init__` Constructor

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             options: Optional[List[str]] = None,  # New parameter
             *args, **kwargs) -> None:
```

- **profile_name**: The name of the custom Firefox profile.
- **geckodriver_version**: The version of geckodriver.
- **firefox_version**: The version of Firefox.
- **user_agent**: The user agent string.
- **proxy_file_path**: The path to the proxy file.
- **options**: A list of Firefox options (e.g., `["--kiosk", "--headless"]`).

#### `set_proxy` Method

```python
def set_proxy(self, options: Options) -> None:
```

- Configures the proxy for Firefox, selecting a random working proxy from the provided proxy file.

#### `_payload` Method

```python
def _payload(self) -> None:
```

- Loads necessary executors for locators and JavaScript.

## Additional Configuration

- **Proxy**: The module automatically selects an available working proxy from the provided file, specified by the `proxy_file_path` parameter.
- **Firefox Profile**: You can specify a path to a custom Firefox profile.
- **User Agent**: The module allows you to set a custom user agent for the WebDriver.
- **Options**: You can pass additional options for Firefox via the `options` parameter.

## Logging

The module uses `logger` for logging errors and warnings.

## License

This project is licensed under the MIT License. See the LICENSE(../../LICENCE) file for more details.
```
```python
"""
Модуль для работы с браузером Firefox
=========================================================================================

Этот модуль содержит класс :class:`Firefox`, который расширяет возможности стандартного
WebDriver Firefox. Он позволяет настраивать пользовательский профиль, запускать WebDriver
в режиме киоска и устанавливать настройки прокси.

Пример использования
--------------------

Пример использования класса `Firefox`:

.. code-block:: python

    from src.webdriver.firefox import Firefox

    if __name__ == "__main__":
        profile_name = "custom_profile"
        geckodriver_version = "v0.29.0"
        firefox_version = "78.0"
        proxy_file_path = "path/to/proxies.txt"

        # Инициализация и запуск браузера
        browser = Firefox(
            profile_name=profile_name,
            geckodriver_version=geckodriver_version,
            firefox_version=firefox_version,
            proxy_file_path=proxy_file_path,
            options=["--kiosk", "--headless"]  # Добавление опций
        )
        browser.get("https://www.example.com")
        browser.quit()
"""
# -*- coding: utf-8 -*-
import random
# from json import load
from typing import List, Optional
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from src.utils.jjson import j_loads
from src.logger.logger import logger
# from fake_useragent import UserAgent  # Это будет использоваться, если необходимо


class Firefox(webdriver.Firefox):
    """
    Расширение стандартного Firefox WebDriver.

    Этот класс добавляет функциональность для установки пользовательского профиля,
    прокси, пользовательского агента, интеграцию с JavaScript и выполнение локаторов,
    а также возможность передачи опций при инициализации.
    """
    def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 options: Optional[List[str]] = None,  # New parameter
                 *args, **kwargs) -> None:
        """
        Инициализирует драйвер Firefox с заданными параметрами.

        :param profile_name: Имя пользовательского профиля Firefox.
        :param geckodriver_version: Версия geckodriver.
        :param firefox_version: Версия Firefox.
        :param user_agent: Строка user agent.
        :param proxy_file_path: Путь к файлу с прокси.
        :param options: Список опций Firefox (например, `["--kiosk", "--headless"]`).
        :param args: Дополнительные позиционные аргументы для родительского класса.
        :param kwargs: Дополнительные именованные аргументы для родительского класса.
        """
        # Инициализация класса Options для настройки параметров браузера
        ff_options = Options()
        if options:
            # Код добавляет переданные опции в настройки браузера
            for option in options:
                ff_options.add_argument(option)

        # Установка пользовательского профиля, если он был передан
        if profile_name:
            profile = webdriver.FirefoxProfile(profile_directory=profile_name)
        else:
            profile = webdriver.FirefoxProfile()

        # Код устанавливает user-agent, если он передан
        if user_agent:
            profile.set_preference('general.useragent.override', user_agent)
        
        # Инициализация родительского класса с настроенными профилем и опциями
        super().__init__(firefox_profile=profile, options=ff_options, *args, **kwargs)
        # Сохранение переданных параметров в атрибуты экземпляра класса
        self.profile_name = profile_name
        self.geckodriver_version = geckodriver_version
        self.firefox_version = firefox_version
        self.user_agent = user_agent
        self.proxy_file_path = proxy_file_path
        # Установка прокси, если путь к файлу с прокси передан
        if proxy_file_path:
            self.set_proxy(ff_options)
        # Вызов метода для загрузки необходимых исполнителей (payload)
        self._payload()

    def set_proxy(self, options: Options) -> None:
        """
        Настраивает прокси для Firefox, выбирая случайный рабочий прокси из файла.

        :param options: Объект Options для настройки параметров браузера.
        """
        try:
            # Код загружает прокси из файла, используя j_loads из src.utils.jjson
            with open(self.proxy_file_path, 'r', encoding='utf-8') as file:
                proxies = j_loads(file)

            # Код выбирает случайный прокси из списка
            if proxies and isinstance(proxies, list):
                proxy = random.choice(proxies)
                # Код устанавливает прокси в параметры браузера
                options.set_preference('network.proxy.type', 1)
                options.set_preference('network.proxy.http', proxy.split(':')[0])
                options.set_preference('network.proxy.http_port', int(proxy.split(':')[1]))
                options.set_preference('network.proxy.ssl', proxy.split(':')[0])
                options.set_preference('network.proxy.ssl_port', int(proxy.split(':')[1]))
            else:
                logger.error(f'Неверный формат файла прокси: {self.proxy_file_path}')
                return
        except Exception as ex:
             logger.error(f'Ошибка при установке прокси: {ex}')
             ...

    def _payload(self) -> None:
        """
        Загружает необходимые исполнители для локаторов и JavaScript.
        """
        # Код выполняет загрузку payload, если это требуется (пока не реализовано)
        ...
```