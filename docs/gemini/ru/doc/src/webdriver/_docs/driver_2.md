# Модуль `driver_2.py`

## Обзор

Данный модуль предоставляет базовый класс `DriverBase` для работы с веб-драйверами, обеспечивая общие атрибуты и методы, используемые различными типами драйверов (Chrome, Firefox, Edge). Класс `Driver` создается динамически с использованием метакласса `DriverMeta` и наследует функциональность `DriverBase` и конкретного типа драйвера.

## Импорты

```python
import sys
import pickle
import time
import copy
from pathlib import Path
from typing import Type, Union
import urllib.parse
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

from src import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript.js import JavaScript
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import WebDriverException
```

Импортирует необходимые библиотеки, включая `selenium`, для взаимодействия с браузером, а также собственные модули для работы с настройками, логированием и исключениями.

## Классы

### `DriverBase`

**Описание**: Базовый класс для веб-драйвера, содержащий общие атрибуты и методы. Обеспечивает функциональность взаимодействия со страницей, выполнения JavaScript-кода и управления куками.

**Атрибуты**:

- `previous_url` (str): URL предыдущей страницы.
- `referrer` (str): Ссылка реферера.
- `page_lang` (str): Язык страницы.
- `ready_state` (bool): Признак готовности страницы.
- ... (и другие атрибуты, если они присутствуют)


**Методы**:

- `driver_payload()`: Инициализирует методы JavaScript и `ExecuteLocator` для выполнения команд на странице.

- `scroll(scrolls: int = 3, frame_size: int = 500, direction: str = 'forward', delay: float = 0.5)`: Прокручивает страницу в указанном направлении.
  - `scrolls` (int): Количество прокруток.
  - `frame_size` (int): Размер фрейма для прокрутки.
  - `direction` (str): Направление прокрутки ('forward' или 'backward').
  - `delay` (float): Задержка между прокрутками.

- `locale()`: Определяет язык страницы.
  - Возвращает: str | None

- `get_url(url: str)`: Переходит по указанному URL и проверяет успешность перехода.
  - `url` (str): Адрес URL.
  - Возвращает: bool

- `extract_domain(url: str)`: Извлекает доменное имя из URL.
  - `url` (str): URL-адрес.
  - Возвращает: str

- `_save_cookies_localy(to_file: Union[str, Path])`: Сохраняет куки в файл.
  - `to_file` (Union[str, Path]): Путь к файлу для сохранения.

- `page_refresh()`: Обновляет текущую страницу.

- `window_focus()`: Восстанавливает фокус на странице.

- `wait(interval: float)`: Делает паузу на указанное время.
  - `interval` (float): Время паузы в секундах.

- `delete_driver_logs()`: Удаляет временные файлы и логи WebDriver.


### `DriverMeta`

**Описание**: Метакласс для создания нового класса `Driver`, унаследованного от `DriverBase` и заданного класса веб-драйвера.

**Методы**:

- `__call__(cls, webdriver_cls: Type, *args, **kwargs)`: Создаёт новый класс `Driver`.
  - `webdriver_cls` (Type): Класс веб-драйвера (например, `Chrome`, `Firefox`).
  - `*args`: Дополнительные аргументы.
  - `**kwargs`: Дополнительные ключевые аргументы.


### `Driver`

**Описание**: Динамически созданный класс веб-драйвера, наследующий `DriverBase` и указанный тип веб-драйвера.

**Описание**: Пример использования:

```python
from src.webdriver import Driver, Chrome, Firefox, Edge

# Создаем объект для браузера Chrome
d = Driver(Chrome)

# Доступ к методам DriverBase через объект `d`
d.get_url("https://example.com")
```

##  Как использовать

Для использования необходимо импортировать нужный тип драйвера и создать объект `Driver`, передавая тип драйвера в качестве аргумента.  Затем можно использовать методы базового класса для взаимодействия со страницей.


## Примеры использования методов

Примеры использования методов `DriverBase` приведены в разделе "Как использовать этот код".