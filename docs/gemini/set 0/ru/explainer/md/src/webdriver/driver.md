# <input code>

```python
## \file hypotez/src/webdriver/driver.py
# -*- coding: utf-8 -*-\
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

MODE = 'dev'

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


class Driver:
    """
    .. class:: Driver
       :platform: Windows, Unix
       :synopsis: Унифицированный класс для взаимодействия с Selenium WebDriver.

    Класс обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

    Атрибуты:
        driver (selenium.webdriver): Экземпляр Selenium WebDriver.
    """

    def __init__(self, webdriver_cls, *args, **kwargs):
        """
        .. method:: __init__(self, webdriver_cls, *args, **kwargs)
        
        Инициализирует экземпляр класса Driver.

        :param webdriver_cls: Класс WebDriver, например Chrome или Firefox.
        :type webdriver_cls: type
        :param args: Позиционные аргументы для драйвера.
        :param kwargs: Ключевые аргументы для драйвера.

        Пример:
            >>> from selenium.webdriver import Chrome
            >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)

    # ... (остальной код)
```

```mermaid
graph LR
    A[Driver] --> B{__init__(webdriver_cls, *args, **kwargs)};
    B --> C[self.driver = webdriver_cls(*args, **kwargs)];
    A --> D[get_url(url)];
    D --> E[self.driver.get(url)];
    D --> F{ready_state != 'complete'};
    F -- True --> G[self.previous_url = _previous_url];
    F -- False --> H[_save_cookies_localy()];
    G --> I[return True];
    H --> J[return True];
    E --> K[Exception];
    K --> L[logger.error(...)] --> I;
    D --> M{url != _previous_url};
    M -- True --> G;
    M -- False --> I;

    subgraph "Selenium WebDriver"
        C --> N[get()];
    end
    
    subgraph "src.logger"
        K --> O[logger.error(...)]
    end


    subgraph "gs"
        H --> P[open(gs.cookies_filepath, 'wb')];
    end
    
    subgraph "pickle"
        P --> Q[pickle.dump(self.driver.get_cookies(), cookiesfile)]
    end

```

```markdown
# <algorithm>

1. **Инициализация (`__init__`):**
   - Принимает класс WebDriver (`webdriver_cls`) и аргументы для его инициализации.
   - Проверяет, что `webdriver_cls` является допустимым классом WebDriver.
   - Создает экземпляр WebDriver (`self.driver`).
   - **Пример:** `driver = Driver(Chrome, executable_path='/path/to/chromedriver')` создаст экземпляр Chrome WebDriver с указанным путём к драйверу.

2. **Переход по URL (`get_url`):**
   - Сохраняет предыдущий URL.
   - Переходит по URL (`self.driver.get(url)`).
   - Ожидает завершения загрузки страницы (`self.ready_state != 'complete'`).
   - Если текущий URL отличается от ожидаемого, обновляет `self.previous_url`.
   - Сохраняет куки (`_save_cookies_localy()`).
   - Возвращает `True` при успешном переходе и `False` при ошибке.
   - **Пример:** `driver.get_url('https://example.com')` переходит на страницу example.com и сохраняет куки.

3. **Прокрутка страницы (`scroll`):**
   - Использует вспомогательную функцию `carousel` для прокрутки в заданном направлении.
   - `carousel` выполняет цикл прокруток с заданной задержкой.
   - Обрабатывает исключения во время прокрутки.
   - **Пример:** `driver.scroll(scrolls=3, direction='down')` прокрутит страницу вниз 3 раза.

4. **Получение языка страницы (`locale`):**
   - Ищет мета-тег `Content-Language` для определения языка.
   - Если не находит, пытается определить язык с помощью JavaScript.
   - Возвращает код языка или `None`.
   - **Пример:** `driver.locale` вернёт код языка (например, 'en') или `None`, если язык не найден.

5. **Сохранение куки (`_save_cookies_localy`):**
   - Сохраняет куки в локальный файл (`gs.cookies_filepath`) с помощью `pickle`.
   - Обрабатывает исключения при сохранении.
   - **Пример:** Сохраняет куки в файл 'cookies.pkl'.

6. **Извлечение HTML-контента (`fetch_html`):**
   - Обрабатывает запросы к файлам (`url.startswith('file://')`) и веб-страницам (`url.startswith('http://')` или `url.startswith('https://')`).
   - Если URL соответствует файлу, читает его и возвращает `True`.
   - Если URL соответствует URL страницы, выполняет `get_url(url)` и получает `page_source` , сохраняя его в `self.html_content`.
   - **Пример:** `driver.fetch_html('file:///path/to/file.html')` считывает содержимое файла `file.html`.


**Взаимодействие:**

- Класс `Driver` использует `selenium.webdriver` для работы с браузером.
- `Driver` взаимодействует с модулем `gs` для получения пути к файлу куки.
- `Driver` использует `logger` для вывода сообщений об ошибках и отладки.


```

```markdown
# <explanation>

**Импорты:**

- `copy`, `pickle`, `time`, `re`, `Path`, `Optional`, `typing`: Стандартные библиотеки Python для работы с копированием, сериализацией, временем, регулярными выражениями, путями к файлам и типизацией.
- `By`, `InvalidArgumentException`, `ElementClickInterceptedException`, `ElementNotInteractableException`, `ElementNotVisibleException`: Модули `selenium.webdriver.common.by` и `selenium.common.exceptions` для работы с селекторами элементов и обработки исключений Selenium.
- `header`: Вероятно, содержит собственные определения или импорты, связанные с заголовками запросов, но подробности не указаны.
- `gs`: Модуль, вероятно, содержит константы или функции для работы с глобальными настройками, такими как пути к файлам с куки (`gs.cookies_filepath`).
- `logger`, `ExecuteLocatorException`, `WebDriverException`: Из модулей `src.logger` и `src.logger.exceptions` для ведения журналов и обработки специфических исключений при работе с драйвером.

**Классы:**

- `Driver`:  Основной класс для работы с веб-драйверами Selenium. Он предоставляет унифицированный интерфейс для различных браузеров, таких как Chrome, Firefox, и Edge. Атрибут `driver` хранит экземпляр `WebDriver`.

**Функции:**

- `__init__`: Инициализирует экземпляр класса `Driver`, принимая класс WebDriver (`webdriver_cls`) и аргументы для его создания.
- `get_url`: Переходит по URL. Обрабатывает исключения при переходе.
- `scroll`: Прокручивает страницу в указанном направлении.
- `locale`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `_save_cookies_localy`: Сохраняет куки в локальный файл.
- `fetch_html`: Извлекает HTML-контент из файла или веб-страницы.

**Переменные:**

- `MODE`: Переменная, скорее всего, для определения режима работы (например, 'dev', 'prod').

**Возможные ошибки и улучшения:**

- Отсутствие проверки на валидность аргументов `webdriver_cls`. Может быть полезно проверять, что `webdriver_cls` - это действительно класс из библиотеки Selenium.
- Более подробная обработка ошибок. В некоторых местах, например, в `fetch_html`, возможны дополнительные проверки на корректность URL-адреса.
- Добавьте проверку на корректность `gs.cookies_filepath`, чтобы предотвратить ошибки при работе с файлами.
- Использование `try...except` блоков в `__init_subclass__` для обработки возможных ошибок.
- Вместо `self.wait(delay)` рассмотреть использование `WebDriverWait` для более гибкого ожидания определенных условий.
- Дополнительные методы проверки состояния драйвера (например, `is_alive()`).


**Взаимосвязи с другими частями проекта:**

Модуль `driver.py` сильно зависит от модулей `src.logger`, `gs`.  Эти модули отвечают за логирование и доступ к глобальным настройкам проекта соответственно.  `selenium` используется для работы с веб-драйверами.  Цепочка взаимосвязей предполагает наличие других модулей (`src`), использующих `driver` для взаимодействия с веб-страницами.