# Модуль `driver.py` - Базовый класс для работы с веб-драйверами

## Обзор

Этот модуль предоставляет базовый класс `DriverBase` для работы с веб-драйверами.  Он инкапсулирует общие методы и атрибуты, используемые различными веб-драйверами (например, Chrome, Firefox, Edge). Класс `DriverBase` содержит методы для взаимодействия со страницей, выполнения JavaScript-кода и управления куками.  Для создания специализированных драйверов используется метакласс `DriverMeta`.

## Импорты и зависимости

### Модули Python

```python
import sys
import pickle
import time
import copy
from pathlib import Path
from typing import Type, Union
import urllib.parse
```

### Библиотека Selenium

```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException
)
```

### Собственные модули

```python
from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript.js import JavaScript
from src.utils.printer import pprint
from src.logger.logger import logger
from src.logger.exceptions import WebDriverException
```

Эти импорты обеспечивают необходимые функции для работы с веб-драйверами и интеграции с другими частями приложения.


## Классы

### `DriverBase`

**Описание**: Базовый класс для работы с веб-драйверами. Содержит общие методы и атрибуты для всех реализаций.

**Атрибуты**:

- `previous_url`: (str): URL предыдущей страницы.
- `referrer`: (str): URL реферера.
- `page_lang`: (str): Язык страницы.

**Методы**:

#### `driver_payload()`

**Описание**: Инициализирует методы JavaScript и `ExecuteLocator` для выполнения команд на странице.

**Возвращает**: `None`

#### `scroll()`

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:

- `scrolls` (int): Количество прокруток.
- `frame_size` (int): Размер рамки для прокрутки.
- `direction` (str): Направление прокрутки ('forward' или 'backward').
- `delay` (float): Задержка между прокрутками.

**Возвращает**: `None`

#### `locale()`

**Описание**: Определяет язык страницы.

**Возвращает**: `str`: Код языка страницы.

#### `get_url(url: str)`

**Описание**: Переходит по указанному URL и проверяет успешность перехода.

**Параметры**:

- `url` (str): URL для перехода.

**Возвращает**: `bool`: True, если переход успешен, иначе False.

#### `extract_domain(url: str)`

**Описание**: Извлекает доменное имя из URL.

**Параметры**:

- `url` (str): URL для извлечения домена.

**Возвращает**: `str`: Доменное имя.

#### `_save_cookies_localy(to_file: Union[str, Path])`

**Описание**: Сохраняет куки в файл.

**Параметры**:

- `to_file` (Union[str, Path]): Путь к файлу для сохранения куки.

**Возвращает**: `None`

#### `page_refresh()`

**Описание**: Обновляет текущую страницу.

**Возвращает**: `None`

#### `window_focus()`

**Описание**: Восстанавливает фокус на странице.

**Возвращает**: `None`

#### `wait(interval: float)`

**Описание**: Делает паузу на указанное время.

**Параметры**:

- `interval` (float): Время паузы в секундах.

**Возвращает**: `None`

#### `delete_driver_logs()`

**Описание**: Удаляет временные файлы и логи WebDriver.

**Возвращает**: `None`

### `DriverMeta`

**Описание**: Метакласс, который создает новый класс `Driver`, унаследованный от `DriverBase` и указанного класса веб-драйвера.

**Методы**:

#### `__call__(cls, webdriver_cls: Type, *args, **kwargs)`

**Описание**: Создает новый класс `Driver`.

**Параметры**:

- `webdriver_cls` (Type): Класс веб-драйвера.


**Возвращает**: `Driver`

### `Driver`

**Описание**: Динамически созданный класс веб-драйвера, унаследованный от `DriverBase` и конкретного класса веб-драйвера (например, Chrome, Firefox).

**Описание**: См. пример использования в разделе "Как использовать".


## Как использовать

Модуль предоставляет возможность создать веб-драйвер для различных браузеров, используя следующий синтаксис:

```python
from src.webdriver.driver import Driver, Chrome, Firefox, Edge

# Создаем объект для браузера Chrome
d = Driver(Chrome)

# Доступ к методам DriverBase через объект `d`
d.get_url("https://example.com")
d.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)
```

Подробный пример использования различных методов представлен в разделе "Пример использования методов".