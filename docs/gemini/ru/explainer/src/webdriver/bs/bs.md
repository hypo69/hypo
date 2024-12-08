# <input code>

```python
## \file hypotez/src/webdriver/bs/bs.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.webdriver.bs 
	:platform: Windows, Unix
	:synopsis: parse pages with `BeautifulSoup` and XPath 
```python
if __name__ == "__main__":
    driver = Driver()
    # For file
    driver.get_url('path/to/your/file.html')
    # For URL
    driver.get_url('https://example.com')
    driver.execute_locator(locator)
```

"""
MODE = 'dev'


import re
from math import log
from bs4 import BeautifulSoup
from types import SimpleNamespace
from lxml import etree
import requests
from pathlib import Path
from src import gs
from src.webdriver.driver import Driver
from src.logger import logger

class BS:
    
    html_content:str
    def __init__(self, url:str|None=None):
        """"""
        self.html_content = url


    def get_url(self, url: str):
        """ Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath

        @param url: The file path or URL to fetch HTML content from
        """

        if url.startswith('file://'):
            # Remove 'file://' prefix and clean up the path
            cleaned_url = url.replace(r'file:///', '')
            
            # Extract the Windows path if it's in the form of 'c:/... ' or 'C:/...'
            match = re.search(r'[a-zA-Z]:[\\\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Exception while reading the file:', ex)
                        ...
                else:
                    logger.error('Local file not found:', file_path)
                    ...
            else:
                logger.error('Invalid file path:', cleaned_url)
                ...
        elif url.startswith('https://'):
            # Handle web URLs
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check for HTTP request errors
                self.html_content = response.text
                return True
            except requests.RequestException as ex:
                logger.error(f"Error fetching {url}:", ex)
                ...
        else:
            logger.error('Invalid URL or file path:', url)
            ...
        


    def execute_locator(self,locator:SimpleNamespace|dict, url: str = None):
        """ мини версия экзкьютора вебдрайвера `Driver` (`src.webdriver.executor`)"""
        ...
        if url:
            self.get_url(url)
            
        soup = BeautifulSoup(self.html_content, 'lxml')
        tree = etree.HTML(str(soup))  # Convert BeautifulSoup object to lxml tree
        attribute = locator.attribute
        by = locator.by
        selector = locator.selector
        elements = None
        
        if by.upper() == 'ID':
            elements = tree.xpath(f'//*[@id="{attribute}"]')
        elif by.upper() == 'CSS':
            elements = tree.xpath(f'//*[contains(@class, "{attribute}")]')
        elif by.upper() == 'TEXT':
            elements = tree.xpath(f'//input[@type="{attribute}"]')
         ## @todo: - это костыль, а не логика"""
        else:
            ...
            elements = tree.xpath(selector)
            
        return elements
    
if __name__ == "__main__":
    driver = Driver()
    # For file
    driver.get_url('path/to/your/file.html')
    # For URL
    driver.get_url('https://example.com')
    locator:SimpleNamespace
    driver.execute_locator(locator)
```

# <algorithm>

**Шаг 1**: Инициализация `BS` объекта.
    * Вход: URL (опционально)
    * Выход: Объект `BS` с `html_content` (изначально `None`, если URL не передан)


**Шаг 2**: Вызов `get_url(url)`
    * Вход: `url` (путь к файлу или URL)
    * Выход: `True` при успешном получении контента, `False` при ошибке.
    * Алгоритм:
        * Проверка типа URL:
            * `file://`: Обработка файлов.
                * Извлечение пути файла.
                * Проверка существования файла.
                * Чтение файла в `self.html_content`.
                * Возврат `True`.
            * `https://`: Обработка веб-страниц.
                * Отправка запроса `requests.get()`.
                * Проверка статуса ответа (`response.raise_for_status()`).
                * Чтение ответа в `self.html_content`.
                * Возврат `True`.
            * В противном случае: Возврат `False` и логирование ошибки.


**Шаг 3**: Вызов `execute_locator(locator, url)`
    * Вход: `locator` (объект `SimpleNamespace` или словарь с локейтером) и `url` (опционально).
    * Выход: Список найденных элементов (`elements`), или `None` при ошибке.
    * Алгоритм:
        * Если `url` передан, то вызов `get_url()`.
        * Парсинг `html_content` с помощью `BeautifulSoup` в `soup`.
        * Преобразование `soup` в `lxml` дерево (`tree`).
        * Извлечение атрибутов из `locator`.
        * Выполнение XPath запроса в зависимости от типа локейтера (`by`).
        * Возврат найденных элементов.


**Пример**:


1. Пользователь предоставляет URL 'https://example.com'.
2. `get_url('https://example.com')` загружает HTML-контент страницы.
3. `execute_locator(locator)` парсит загруженный контент, используя XPath, и возвращает список элементов, соответствующих локейтеру.

# <mermaid>

```mermaid
graph LR
    A[BS Object] --> B{get_url(url)};
    B -- file:// --> C[Read from File];
    B -- https:// --> D[Fetch from URL];
    C --> E[html_content = content];
    D --> E;
    E --> F[execute_locator(locator, url)];
    F --> G{Parse with BeautifulSoup};
    G --> H[Convert to lxml tree];
    H --> I[XPath Query];
    I -- ID --> J[Elements with ID];
    I -- CSS --> K[Elements with class];
    I -- TEXT --> L[Elements with type];
    I -- Other --> M[Elements with selector];
    J --> N[Return Elements];
    K --> N;
    L --> N;
    M --> N;
    subgraph Dependencies
        E --> O[logger];
        E --> P[requests];
        E --> Q[Path];
        E --> R[bs4];
        E --> S[lxml];
    end
```

**Объяснение зависимостей**:
* `logger`: Для логирования ошибок и информации.
* `requests`: Для получения данных с веб-страниц.
* `Path`: Для работы с файловыми путями.
* `bs4`: Библиотека для парсинга HTML.
* `lxml`: Библиотека для работы с XML и HTML.


# <explanation>

**Импорты**:

* `re`: Для работы с регулярными выражениями, в основном для обработки путей файлов.
* `math`: В данном случае не используется (необходим для потенциального использования в другом контексте).
* `bs4`: Для работы с HTML-контентом, создание `BeautifulSoup` объектов.
* `types`: Для использования `SimpleNamespace`.
* `lxml.etree`: Для работы с XML-данными, конвертация  `BeautifulSoup` объектов в `lxml` деревья.
* `requests`: Для получения HTML контента из URL.
* `pathlib`: Для работы с путями к файлам, создание `Path` объектов.
* `src.gs`: Возможно, вспомогательный модуль проекта.
* `src.webdriver.driver`: Модуль, содержащий класс `Driver`.
* `src.logger`: Модуль для логирования.

**Классы**:

* `BS`: Класс для парсинга HTML контента с использованием `BeautifulSoup` и XPath.
    * `html_content`: Хранит полученный HTML контент.
    * `__init__`: Инициализирует объект, принимая URL.
    * `get_url`: Загружает HTML контент из файла или URL, используя `requests` для веб-страниц и чтение из файла для локальных файлов.
    * `execute_locator`: Выполняет поиск элементов по заданному локейтеру с помощью XPath.


**Функции**:

* `get_url`:  Получение HTML контента из файла или URL.
* `execute_locator`: Выполнение локейтора.
* `__init__`: Инициализация `BS` объекта.

**Переменные**:

* `MODE`: Строковая константа.
* `locator`: Объект `SimpleNamespace` или словарь с локейтером.
* `url`: Строка, представляющая URL или путь к файлу.

**Возможные ошибки и улучшения**:

* **Обработка ошибок**: Класс `BS` содержит обработку ошибок, например, при чтении файла, и логирование ошибок. В `get_url` необходимо добавить обработку случаев, когда `response.raise_for_status()` возвращает ошибку, а в `execute_locator` обработку случая, когда locator не содержит необходимых атрибутов.

* **Модульная структура**: Улучшение: Использование аргументов `url` и `locator` в `execute_locator` для более гибкого и модульного дизайна.

* **Типизация**: Используются аннотации типов (`url: str`), что положительно сказывается на читаемости и поддержке кода.

* **Непонятные возвращаемые значения**: Непонятно, почему `get_url` возвращает `bool`, а не `requests.Response` или `bytes`.

* **Запись логов**: `logger.error(...)` должен принимать более подробную информацию (например, текущий контекст).

* **Неполная реализация**: Не реализовано `elif by.upper() == 'NAME'`, `elif by.upper() == 'TAG'` и т.д.

* **Управляющие структуры**: В `execute_locator` логика поиска для каждого типа локейтера могла бы быть более централизованной, например, в отдельном словаре или функции.


**Взаимосвязи с другими частями проекта**:

* `src.webdriver.driver`: Класс `BS` взаимодействует с классом `Driver` для получения и обработки данных.
* `src.logger`: Используется для логирования ошибок, связанных с получением и обработкой данных.
* `src.gs`: Вероятно, это вспомогательный модуль, предоставляющий дополнительные функции.