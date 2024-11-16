## \file hypotez/src/webdriver/_docs/driver_2.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver._docs """
MODE = 'debug'
Код в файле `driver.py` представляет собой базовый класс для работы с веб-драйверами, который инкапсулирует общие методы и атрибуты, применяемые к различным веб-драйверам (например, Chrome, Firefox, Edge). Вот подробное объяснение, что делает каждый компонент кода:

### Основные компоненты и их функции:

#### 1. **Импорты и зависимости**

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

from header import gs
from src.webdriver.executor import ExecuteLocator
from src.webdriver.javascript.js import JavaScript
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import WebDriverException
```

Импортирует необходимые библиотеки и модули, включая `selenium` для взаимодействия с браузером и собственные модули для управления настройками, логированием и исключениями.

#### 2. **Класс `DriverBase`**

```python
class DriverBase:
    """ Base class for a WebDriver with common attributes and methods.

    This class contains methods and attributes common to all WebDriver implementations, including functionalities for page interaction,
    JavaScript execution, and managing cookies.
    """
```

`DriverBase` — это базовый класс, который содержит общие методы и атрибуты для всех реализаций веб-драйверов. Он предоставляет функционал для взаимодействия с веб-страницей.

- **Атрибуты класса**:
  - `previous_url`, `referrer`, `page_lang` — хранят URL предыдущей страницы, реферера и язык страницы соответственно.
  - `ready_state`, `get_page_lang`, и т.д. — методы для выполнения JavaScript-кода на странице и взаимодействия с элементами.

- **Методы класса**:
  - `driver_payload()` — инициализирует методы JavaScript и `ExecuteLocator` для выполнения команд на странице.
  - `scroll()` — прокручивает страницу в указанном направлении.
  - `locale()` — определяет язык страницы.
  - `get_url(url: str)` — переходит по указанному URL и проверяет успешность перехода.
  - `extract_domain(url: str)` — извлекает доменное имя из URL.
  - `_save_cookies_localy(to_file: Union[str, Path])` — сохраняет куки в файл.
  - `page_refresh()` — обновляет текущую страницу.
  - `window_focus()` — восстанавливает фокус на странице.
  - `wait(interval: float)` — делает паузу на указанное время.
  - `delete_driver_logs()` — удаляет временные файлы и логи WebDriver.

#### 3. **Класс `DriverMeta`**

```python
class DriverMeta(type):
    def __call__(cls, webdriver_cls: Type, *args, **kwargs):
        """Creates a new Driver class that inherits from DriverBase and the specified WebDriver class.
        ...
        """
```

`DriverMeta` — это метакласс, который создает новый класс `Driver`, унаследованный от `DriverBase` и указанного класса веб-драйвера (например, `Chrome`, `Firefox`, `Edge`).

- **Метод `__call__`**:
  - Создает класс `Driver`, который наследует функциональность `DriverBase` и заданного веб-драйвера.
  - Инициализирует новый драйвер с помощью `driver_payload()`.

#### 4. **Класс `Driver`**

```python
class Driver(metaclass=DriverMeta):
    """
    A dynamically created WebDriver class that inherits from DriverBase and a specified WebDriver class.
    
    @code
    from src.webdriver import Driver, Chrome, Firefox, Edge
    d = Driver(Chrome)
    @endcode
    """
    ...
```

`Driver` — это класс, созданный с использованием метакласса `DriverMeta`. Он динамически наследует от `DriverBase` и указанного веб-драйвера.

### Как использовать этот код

Этот код позволяет создавать веб-драйверы для различных браузеров, используя следующий синтаксис:

```python
from src.webdriver import Driver, Chrome, Firefox, Edge

# Создаем объект для браузера Chrome
d = Driver(Chrome)

# Доступ к методам DriverBase через объект `d`
d.get_url("https://example.com")
d.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)
```

### Пример использования методов

1. **Открытие веб-страницы и проверка перехода**:

```python
d.get_url("https://example.com")
```

2. **Прокрутка страницы**:

```python
d.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)
```

3. **Определение языка страницы**:

```python
language = d.locale()
```

4. **Сохранение куки**:

```python
d._save_cookies_localy('cookies.pkl')
```

5. **Обновление страницы**:

```python
d.page_refresh()
```
