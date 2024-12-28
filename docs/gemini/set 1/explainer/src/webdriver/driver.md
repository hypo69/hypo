# <input code>

```python
## \file hypotez/src/webdriver/driver.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.driver
   :platform: Windows, Unix
   :synopsis: Модуль для работы с веб-драйверами Selenium.

   Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для работы с веб-драйверами Selenium.

   Основные функции:
   
   1. **Инициализация драйвера**: создание экземпляра Selenium WebDriver.
   2. **Навигация**: переход по URL, прокрутка и извлечение контента.
   3. **Работа с куки**: сохранение и управление куки.
   4. **Обработка исключений**: логирование ошибок.

Пример использования:
    >>> from selenium.webdriver import Chrome
    >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    >>> driver.get_url('https://example.com')
"""



import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException
)
import header
from src import gs
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException
```

# <algorithm>

**Шаг 1: Инициализация драйвера**

- Принимает класс WebDriver (например, `Chrome`, `Firefox`) и параметры для его создания (`executable_path`, и т.д.)
- Создаёт экземпляр WebDriver.

**Шаг 2: Проверка типа webdriver_cls**

- Проверяет, что переданный `webdriver_cls` является допустимым классом WebDriver, иначе выбрасывает `TypeError`.


**Шаг 3: Метод `scroll`**

- Вызывает внутреннюю функцию `carousel` для прокрутки в заданном направлении.
- Если направление 'both', то вызывает `carousel` дважды для прокрутки вверх и вниз.
- Логирует ошибки, которые могут возникнуть во время прокрутки.

**Шаг 4: Метод `get_url`**

- Сохраняет текущий URL.
- Переходит по URL используя `self.driver.get(url)`.
- Ожидает завершения загрузки страницы (цикл `while`).
- Сравнивает текущий URL с ожидаемым.
- Сохраняет куки в файл `gs.cookies_filepath`.
- Возвращает `True` при успехе, `False` в противном случае, обрабатывая различные исключения (WebDriverException, InvalidArgumentException и др.).


**Шаг 5: Метод `fetch_html`**

- Проверяет тип URL (локальный файл или веб-страница).
- Если локальный файл, то пытается прочитать его содержимое.
- Если веб-страница, то вызывает `get_url` и извлекает `page_source`.
- Логирует ошибки при чтении файла или получении контента.


# <mermaid>

```mermaid
graph TD
    A[Driver Class] --> B{__init__(webdriver_cls, *args, **kwargs)};
    B --> C[driver = webdriver_cls(*args, **kwargs)];
    C --> D{hasattr(webdriver_cls, 'get')};
    D -- True --> E[Driver initialized];
    D -- False --> F[TypeError];
    E --> G[get_url(url)];
    G --> H[self.driver.get(url)];
    H --> I[while self.ready_state != 'complete'];
    I --> J[if url != _previous_url];
    J --> K[self.previous_url = _previous_url];
    K --> L[self._save_cookies_localy()];
    L --> M[return True];
    G --> N[Exception];
    N --> O[logger.error];
    O --> M;
    G --> P[WebDriverException];
    P --> O;
    G --> Q[InvalidArgumentException];
    Q --> O;
    G --> R[Exception];
    R --> O;
    E --> S[scroll(scrolls, frame_size, direction, delay)];
    S --> T[carousel(direction, scrolls, frame_size, delay)];
    T -- Success --> U[return True];
    T -- Error --> O;
    E --> V[fetch_html(url)];
    V --> W[if url.startswith('file://')];
    W --> X[try to read file];
    X -- Success --> Y[return True];
    X -- Error --> O;
    W --> Z[return False];
    V --> AA[if url.startswith('http')];
    AA --> AB[self.get_url(url)];
    AB -- Success --> AC[self.html_content = self.page_source];
    AC --> Y;
    AB -- Error --> O;
    AA --> AD[return False];
    subgraph init_subclass
        E --> AA[__init_subclass__(browser_name=None, **kwargs)];
        AA --> AE[if browser_name is None];
        AE -- True --> AF[ValueError];
        AE -- False --> AG[cls.browser_name = browser_name];
        AG --> E;
    end
```

# <explanation>

**Импорты:**

- `copy`, `pickle`, `time`, `re`, `pathlib`, `typing`, `selenium.webdriver`, `selenium.common.exceptions` — стандартные библиотеки Python и Selenium, используемые для копирования, сериализации данных, управления временем, регулярных выражений, работы с файлами, типов данных и обработки исключений.
- `header` — вероятно, собственный модуль, предоставляющий дополнительные функции.
- `src.gs` —  модуль из проекта, вероятно, содержащий глобальные константы или настройки.
- `src.logger` и `src.logger.exceptions` —  модуль и подмодуль для логирования и обработки специфических исключений, используемых для вывода сообщений об ошибках и отслеживания проблем.


**Классы:**

- **`Driver`:**  Основной класс для взаимодействия с веб-драйверами.  Используется для инициализации драйвера, навигации по сайту, управления куки, прокрутки и извлечения контента.
   - `driver (selenium.webdriver)`: экземпляр веб-драйвера, предоставляемого Selenium.
   - `__init__(self, webdriver_cls, *args, **kwargs)`:  Инициализирует экземпляр класса, принимая класс веб-драйвера и аргументы для его инициализации. Важно: проверка корректности типа драйвера.
   - `__init_subclass__(cls, *, browser_name=None, **kwargs)`: Автоматически вызывается при создании подкласса `Driver`, проверяет наличие `browser_name` и инициализирует его.  Это полезно для работы с разными типами браузеров, например, Chrome, Firefox, Edge.  Однако, данная функция требует дополнительного понимания работы `__init_subclass__`.
   - `__getattr__(self, item)`:  Прокси-метод для доступа к атрибутам драйвера (например, `driver.current_url`).
   - `scroll(self, scrolls, frame_size, direction, delay)`: Прокручивает страницу в заданном направлении.
   - `get_url(self, url)`: Переходит по URL, ожидает полной загрузки и сохраняет куки. Обрабатывает ошибки при переходе (например, неверный URL, ошибка драйвера).
   - `locale(self)`:  Определяет язык страницы.
   - `wait(self, delay)`:  Ожидает указанное количество времени.
   - `_save_cookies_localy(self)`:  Сохраняет куки в файл.
   - `fetch_html(self, url)`: Извлекает HTML-контент из файла или URL.


**Функции:**

- `carousel(direction, scrolls, frame_size, delay)`: Вложенная функция для прокрутки.  Предназначена для повторного вызова для прокрутки вверх/вниз.

**Переменные:**

- `MODE`: Строковая переменная, хранит режим работы ('dev').
- `gs.cookies_filepath`:  Путь к файлу, в котором сохраняются куки.

**Возможные ошибки и улучшения:**

- **Недостаточная обработка ошибок:** Хотя код содержит `try...except` блоки, некоторые исключения могут не быть отловлены или обработаны адекватно. Нужно добавить более подробное описание исключений и их решений.
- **Упрощение кода `fetch_html`**: Логика для обработки локальных файлов и веб-страниц выглядит несколько громоздко.  Можно выделить отдельные функции для каждого типа.
- **Документация**: Документация к классам и методам могла бы быть более подробной, особенно по параметрам и возвращаемым значениям.
- **Комментарии**: Больше комментариев внутри кода, особенно в сложных местах, могут улучшить читаемость и понимание.
- **Переменные с фиксированными значениями**:  Значения по умолчанию в методах `scroll` и `carousel` (`scrolls = 1`, `frame_size = 600`, `delay = 0.3`) — могут быть не самыми лучшими для всех случаев, нужно рассмотреть возможность их адаптации.
- **`return True` в `_save_cookies_localy`**: Возвращение `True` в `_save_cookies_localy` бессмысленно, если метод ничего не возвращает.  Удалите этот `return`.


**Взаимосвязь с другими частями проекта:**

- `src.gs`:  Поле `gs.cookies_filepath` указывает на необходимость существования внешней переменной, задающей путь к файлу куки.
- `src.logger`: Для логирования ошибок, сообщений и отладки.


**Общее замечание:**

Код структурирован и хорошо документирован, но требует дополнительных улучшений для повышения его надежности и читаемости.  Обработка различных типов исключений и более подробная документация улучшат код.