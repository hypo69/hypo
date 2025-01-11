# Анализ кода модуля `firefox`

**Качество кода: 8/10**

- **Плюсы:**
    - Код хорошо структурирован и использует классы для инкапсуляции логики.
    - Имеется обработка исключений при инициализации драйвера.
    - Используется `j_loads_ns` для загрузки настроек из JSON.
    - Применяется `fake_useragent` для генерации случайных user-agent.
    - Документация в `markdown` формате для `firefox.md` представлена корректно.
    - Добавлены docstring к классам и методам.
    - Логирование ошибок происходит с помощью `logger.error`.
- **Минусы:**
    - Отсутствуют проверки на корректность путей при загрузке настроек.
    - Не используются аннотации типов для всех переменных.
    - `try-except` блоки используют `...` вместо обработки конкретных ошибок.
    - Некоторые строки кода могут быть более читаемыми при использовании форматирования строк f-string.
    - Не все импорты расположены в алфавитном порядке.
    - В `firefox.md` не указан пример инициализации `Firefox` класса.

**Рекомендации по улучшению:**

1.  **Импорты**: Отсортировать импорты по алфавиту и проверить на наличие лишних.
2.  **Пути**: Добавить проверку на корректность путей при загрузке настроек.
3.  **Обработка исключений**: Заменить `...` на конкретную обработку исключений и логирование.
4.  **Аннотации типов**: Добавить аннотации типов для всех переменных.
5.  **Форматирование строк**: Использовать f-строки для форматирования строк.
6.  **Документация**:
    -   Добавить пример инициализации класса `Firefox` в файл `firefox.md`.
    -   Пересмотреть документацию методов, сделать ее более подробной.
7.  **Логирование**: Использовать `logger.error` для всех ошибок.

**Оптимизированный код:**

```python
"""
Модуль для управления веб-драйвером Firefox.
=========================================================================================

Этот модуль определяет подкласс `Firefox` класса `webdriver.Firefox`,
предоставляющий дополнительные возможности, такие как запуск Firefox в режиме киоска
и настройка профиля Firefox для веб-драйвера.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.firefox.firefox import Firefox

    driver = Firefox()
    driver.get("https://www.example.com")
    driver.quit()
"""

import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, Any, List
from fake_useragent import UserAgent

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Firefox(WebDriver):
    """
    Подкласс `webdriver.Firefox`, предоставляющий дополнительные возможности.

    :param user_agent: (Optional[dict]) Словарь настроек user-agent.
    :param args: (tuple) Дополнительные позиционные аргументы.
    :param kwargs: (dict) Дополнительные именованные аргументы.

    :ivar driver_name: (str) Имя драйвера.
    """
    driver_name: str = 'firefox'

    def __init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """
        Инициализирует веб-драйвер Firefox с заданными параметрами запуска и профилем.

        Args:
            user_agent (Optional[dict], optional): Словарь, содержащий настройки user-agent.
                Если не указан, генерируется случайный user-agent. Defaults to None.
            *args: Произвольные позиционные аргументы.
            **kwargs: Произвольные именованные аргументы.
        """
        self.user_agent: str = user_agent if user_agent else UserAgent().random

        try:
            settings: SimpleNamespace = j_loads_ns(Path(gs.path.src, 'webdriver', 'firefox', 'firefox.json'))
        except Exception as ex:
            logger.error(f'Ошибка при загрузке настроек из файла firefox.json: {ex}')
            return

        geckodriver_path_parts: List[str] = settings.geckodriver
        geckodriver_path: str = str(Path(gs.path.bin, *geckodriver_path_parts))

        profile: FirefoxProfile = self._set_profile(settings.profile)
        options: Options = self._set_options(settings)

        service: Service = Service(geckodriver_path)

        if profile:
            options.profile = profile

        try:
            logger.info("Запуск Firefox")
            super().__init__(options=options, service=service)
        except WebDriverException as ex:
            logger.critical(f"""
                ---------------------------------
                    Не удалось запустить драйвер Firefox.
                    Возможно, требуется обновление самого Firefox,
                    или драйвер не установлен в системе.
                ----------------------------------
                {ex}
                """)
            return
        except Exception as ex:
            logger.critical(f'Ошибка при запуске веб-драйвера Firefox: {ex}')
            return

    def _set_options(self, settings: SimpleNamespace) -> Options:
        """
        Устанавливает параметры запуска для веб-драйвера Firefox.

        Args:
            settings (SimpleNamespace): Настройки для параметров Firefox.

        Returns:
            Options: Объект Options с заданными параметрами запуска.
        """
        options: Options = Options()

        if settings.options:
            for opt in settings.options:
                if 'headless' in opt:
                    options.headless = True
                else:
                    options.add_argument(opt)

        if settings.headers:
             [options.add_argument(f"--{key}={value}") for key, value in settings.headers.items()]

        return options

    def _set_profile(self, profile: SimpleNamespace) -> FirefoxProfile:
        """
        Настраивает профиль Firefox для веб-драйвера.

        Args:
            profile (SimpleNamespace): Объект SimpleNamespace, содержащий настройки профиля.

        Returns:
             FirefoxProfile: Объект FirefoxProfile, представляющий профиль.
        """
        profile_directory: str = profile.profile_path[profile.default_profile_from]

        if '%APPDATA%' in profile_directory:
             profile_directory = Path(profile_directory.replace('%APPDATA%', os.environ.get('APPDATA', '')))
             profile_directory = Path(profile_directory / profile.default_profile_directory[0])
        else:
             profile_directory = Path(gs.path.src / 'webdriver' / 'firefox' / 'profiles' / profile.default_profile_directory[0])

        firefox_profile: FirefoxProfile = FirefoxProfile(profile_directory=str(profile_directory))
        return firefox_profile
```

### Обновленный файл `firefox.md`

```markdown
# Firefox WebDriver

## Overview

This code defines a subclass of `webdriver.Firefox` called `Firefox`. It provides additional functionality such as the ability to launch Firefox in kiosk mode and the ability to set up a Firefox profile for the webdriver.

## Class: Firefox

### Attributes

- `driver_name`: A class attribute set to `'firefox'`.

### Methods

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

Initializes the Firefox webdriver with the specified launch options and profile.

- **Parameters:**
  - `user_agent` (`dict`, optional): A dictionary containing user agent settings. If not provided, a random user agent is generated.
  - `*args`: Additional positional arguments.
  - `**kwargs`: Additional keyword arguments.

#### `_set_options(self, settings: SimpleNamespace) -> Options`

Sets the launch options for the Firefox webdriver.

- **Parameters:**
  - `settings` (`SimpleNamespace`): Settings for the Firefox options.

- **Returns:**
  - `Options`: An Options object with the specified launch options.

#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

Sets up a Firefox profile for the webdriver.

- **Parameters:**
  - `profile` (`SimpleNamespace`): A SimpleNamespace object containing profile settings.

- **Returns:**
  - `FirefoxProfile`: A FirefoxProfile object representing the profile.

## Usage

### Creating a Firefox instance with default settings

```python
from src.webdriver.firefox.firefox import Firefox

driver = Firefox()
driver.get("https://www.example.com")
driver.quit()
```

### Creating a Profile with User Agent

```python
profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "user-agent-string")
```

### Disabling Images

```python
profile = FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
```

### Blocking Pop-up Windows

```python
profile = FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
```

### Setting File Download Path

```python
profile = FirefoxProfile()
profile.set_preference("browser.download.dir", "/path/to/download/folder")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
```

### Disabling Browser Notifications

```python
profile = FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
```

## Options Examples

### Launching in Headless Mode

```python
options = Options()
options.headless = True
```

### Setting Browser Language

```python
options = Options()
options.add_argument('-lang=es')
```

### Custom Command Line Parameters

```python
options = Options()
options.add_argument('--some-option=value')
```

### Managing Debug Messages

```python
options = Options()
options.add_argument('-vv')
```

### Launching in Fullscreen Mode

```python
options = Options()
options.add_argument('--kiosk')
```

## Links

- [Documentation on Firefox Profile Settings](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Documentation on Firefox Options](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)
```