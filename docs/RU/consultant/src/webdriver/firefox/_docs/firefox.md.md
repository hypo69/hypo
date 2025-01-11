# Анализ кода модуля `firefox`

**Качество кода**
**7/10**
- Плюсы
    - Код структурирован и разбит на методы, что улучшает читаемость.
    - Используются аннотации типов для улучшения понимания кода.
    - Присутствует обработка исключений при инициализации драйвера.
    - Используется `j_loads_ns` для загрузки настроек из json.
- Минусы
    - Отсутствуют docstring для класса и методов в формате reStructuredText (RST).
    - Комментарии `#` не объясняют подробно каждую строку кода.
    - В блоке `try-except` используется `return` без возвращаемого значения, что может привести к ошибкам.
    - Используется `logger.critical` для обработки ошибок, когда возможно использование `logger.error`.

**Рекомендации по улучшению**
1.  Добавить docstring в формате reStructuredText (RST) для класса `Firefox` и его методов `__init__`, `_set_options`, `_set_profile`.
2.  Заменить комментарии `#` на более подробные объяснения в формате RST.
3.  Удалить `return` без возвращаемого значения в блоках `try-except`.
4.  Использовать `logger.error` вместо `logger.critical` в блоке `except Exception as ex`.
5.  Добавить проверку на наличие ключей в `settings.options` и `settings.headers`.
6.  Использовать `Path` для конструирования путей и `os.environ.get` для получения переменных среды.

**Оптимизированный код**

```python
"""
Модуль для управления веб-драйвером Firefox.
=========================================================================================

Этот модуль предоставляет класс :class:`Firefox`, который является подклассом
:class:`selenium.webdriver.Firefox` и предоставляет дополнительные возможности, такие
как запуск Firefox в режиме киоска и настройку профиля Firefox для веб-драйвера.

Пример использования
--------------------

Пример создания экземпляра класса `Firefox`:

.. code-block:: python

    from src.webdriver.firefox.firefox import Firefox

    driver = Firefox()
    driver.get("https://www.example.com")
    driver.quit()

"""

import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, Any
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException
from fake_useragent import UserAgent

from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

class Firefox(WebDriver):
    """
    Расширение класса `webdriver.Firefox` с дополнительными функциями.

    :ivar driver_name: Имя драйвера ('firefox').
    """
    driver_name = 'firefox'
    
    def __init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """
        Инициализирует веб-драйвер Firefox с заданными параметрами запуска и профилем.

        :param user_agent: Словарь с настройками user agent. Если не задан, используется случайный user agent.
        :type user_agent: Optional[dict]
        """
        # если user_agent не передан, то генерируется случайный.
        self.user_agent = user_agent if user_agent else UserAgent().random

        # Загрузка настроек из файла `firefox.json`.
        settings: SimpleNamespace = j_loads_ns(Path(gs.path.src, 'webdriver', 'firefox', 'firefox.json'))

        # Формирование пути к geckodriver.
        geckodriver_path_parts: list[str] = settings.geckodriver
        geckodriver_path: str = str(Path(gs.path.bin, *geckodriver_path_parts))

        # Установка профиля и параметров запуска.
        profile: FirefoxProfile = self._set_profile(settings.profile)
        options: Options = self._set_options(settings)

        # Инициализация сервиса драйвера.
        service = Service(geckodriver_path)

        # Если профиль установлен, добавляем его в параметры.
        if profile:
            options.profile = profile
        
        try:
            # Запуск Firefox.
            logger.info("Start Firefox")
            super().__init__(options=options, service=service)
        except WebDriverException as ex:
            # Обработка исключения при запуске драйвера.
            logger.error("""
                ---------------------------------
                    Не поднялся драйвер
                    так бывает при обновлениях самого Firefox
                    ну, или он не установлен в ос.
            ----------------------------------""", ex)
            
        except Exception as ex:
            # Обработка общей ошибки.
            logger.error(f' Упал webdriver Firefox. Общая ошибка:  {ex}')

    def _set_options(self, settings: SimpleNamespace) -> Options:
        """
        Устанавливает параметры запуска для веб-драйвера Firefox.

        :param settings: Настройки для параметров Firefox.
        :type settings: SimpleNamespace
        :return: Объект Options с установленными параметрами запуска.
        :rtype: selenium.webdriver.firefox.options.Options
        """
        # Создание объекта Options.
        options = Options()

        # Проверка и добавление параметров запуска.
        if hasattr(settings, 'options') and settings.options:
            for opt in settings.options:
                if 'headless' in opt:
                    options.headless = True
                else:
                    options.add_argument(opt)

        # Проверка и добавление заголовков.
        if hasattr(settings, 'headers') and settings.headers:
           [options.add_argument(f"--{key}={value}") for key, value in settings.headers.items()]

        return options

    def _set_profile(self, profile: SimpleNamespace) -> FirefoxProfile:
        """
        Настраивает профиль Firefox для веб-драйвера.

        :param profile: Объект SimpleNamespace с настройками профиля.
        :type profile: SimpleNamespace
        :return: Объект FirefoxProfile, представляющий профиль.
        :rtype: FirefoxProfile
        """
        # Получение пути к каталогу профиля.
        profile_directory = profile.profile_path[profile.default_profile_from]
        
        # Обработка переменной окружения APPDATA.
        if '%APPDATA%' in profile_directory:
            profile_directory = Path(profile_directory.replace('%APPDATA%', os.environ.get('APPDATA', '')))
            profile_directory = Path(profile_directory / profile.default_profile_directory[0])
        else:
            profile_directory = Path(gs.path.src / 'webdriver' / 'firefox' / 'profiles' / profile.default_profile_directory[0])

        # Создание объекта FirefoxProfile.
        profile = FirefoxProfile(profile_directory=str(profile_directory))
        return profile
```
### Обновленный файл `firefox.md`

```markdown
# Firefox WebDriver

## Обзор

Этот код определяет подкласс `webdriver.Firefox` с именем `Firefox`. Он предоставляет дополнительные функции, такие как возможность запуска Firefox в режиме киоска и возможность настройки профиля Firefox для веб-драйвера.

## Класс: Firefox

### Атрибуты

- `driver_name`: Атрибут класса, установленный в `\'firefox\'`.

### Методы

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

Инициализирует веб-драйвер Firefox с указанными параметрами запуска и профилем.

- **Параметры:**
  - `user_agent` (`dict`, optional): Словарь, содержащий настройки user agent. Если не предоставлен, генерируется случайный user agent.

#### `_set_options(self, settings: SimpleNamespace) -> Options`

Устанавливает параметры запуска для веб-драйвера Firefox.

- **Параметры:**
  - `settings` (`SimpleNamespace`): Настройки для параметров Firefox.

- **Возвращает:**
  - `Options`: Объект Options с указанными параметрами запуска.

#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

Настраивает профиль Firefox для веб-драйвера.

- **Параметры:**
  - `profile` (`SimpleNamespace`): Объект SimpleNamespace, содержащий настройки профиля.

- **Возвращает:**
  - `FirefoxProfile`: Объект FirefoxProfile, представляющий профиль.

## Использование

### Создание профиля с User Agent

```python
profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "user-agent-string")
```

### Отключение изображений

```python
profile = FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
```

### Блокировка всплывающих окон

```python
profile = FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
```

### Настройка пути для скачивания файлов

```python
profile = FirefoxProfile()
profile.set_preference("browser.download.dir", "/path/to/download/folder")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
```

### Отключение уведомлений браузера

```python
profile = FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
```

## Примеры параметров

### Запуск в режиме без графического интерфейса

```python
options = Options()
options.headless = True
```

### Установка языка браузера

```python
options = Options()
options.add_argument(\'-lang=es\')
```

### Пользовательские параметры командной строки

```python
options = Options()
options.add_argument(\'--some-option=value\')
```

### Управление сообщениями отладки

```python
options = Options()
options.add_argument(\'-vv\')
```

### Запуск в полноэкранном режиме

```python
options = Options()
options.add_argument(\'--kiosk\')
```

## Ссылки

- [Документация по настройкам профиля Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Документация по параметрам Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)
```