# <input code>

```python
## \file hypotez/src/webdriver/bs/bs.py
# -*- coding: utf-8 -*-\
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
from src.webdriver import Driver
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
            
            # Extract the Windows path if it's in the form of 'c:/... or 'C:/...'
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
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

**Шаг 1:**  Инициализация `BS` объекта.
* Пример: `bs_object = BS("https://example.com")`  
* Результат: Создание объекта `BS` с `html_content` установленным в значение `None`.

**Шаг 2:** Вызов `get_url`.
* Пример: `bs_object.get_url("https://example.com")`
* Алгоритм:
    * Проверка начала `url` (проверяет на "file://" и "https://").
    * **Если `file://`**:
        * Читает файл по указанному пути.
        * Возвращает `True` при успехе, `False` при ошибке.
    * **Если `https://`**:
        * Использует `requests` для получения HTML страницы.
        * Возвращает `True` при успехе, `False` при ошибке.
    * **В остальных случаях:**
        * Выводит ошибку и возвращает `False`.

**Шаг 3:** Вызов `execute_locator`.
* Пример: `bs_object.execute_locator(locator)`.
* Алгоритм:
    * Проверка наличия `url` и вызов `get_url` если она существует.
    * Использует `BeautifulSoup` для парсинга `html_content`.
    * Использует `lxml.etree` для получения XPath элементов.
    * Возвращает найденные элементы, используя XPath в зависимости от `locator.by` ("ID", "CSS", "TEXT").
    * Обрабатывает разные типы локейторов.

**Шаг 4:** Вызов метода `execute_locator` из класса `Driver`. 
* Пример: `driver = Driver(); driver.execute_locator(locator)`.


# <mermaid>

```mermaid
graph TD
    A[BS Object] --> B{get_url(url)};
    B -- file:// --> C[Read File];
    B -- https:// --> D[Fetch URL];
    B -- other --> E[Error];
    C --> F[html_content = file_content];
    D --> G[html_content = response_text];
    E --> H[log Error];
    F --> I[Execute locator];
    G --> I;
    I --> J[BeautifulSoup];
    J --> K[lxml.etree];
    K --> L[XPath Query];
    L --> M[Return elements];
    
```

# <explanation>

**Импорты:**

* `re`: Для работы с регулярными выражениями (например, для обработки путей к файлам).
* `math`: Для математических функций (в данном коде не используется).
* `bs4`: Библиотека `BeautifulSoup` для парсинга HTML.
* `types`: Модуль `SimpleNamespace` для создания именных пространств.
* `lxml`: Библиотека `lxml` для работы с XML и HTML, обеспечивающая более эффективное парсинг, чем `BeautifulSoup` для XPath запросов.
* `requests`: Для запроса HTML с удаленных ресурсов.
* `pathlib`: Для работы с путями к файлам.
* `src.gs`: Вероятно, модуль, связанный с Google Sheets.
* `src.webdriver`: Модуль, содержащий класс `Driver` и связанный с управлением веб-драйвером.
* `src.logger`: Модуль для логирования.


**Классы:**

* `BS`: Класс для работы с HTML страницами с помощью `BeautifulSoup` и XPath.
    * `html_content`: Хранит содержимое HTML страницы (строка).
    * `__init__`: Инициализирует `html_content`.
    * `get_url`: Загружает содержимое HTML из файла или URL.
    * `execute_locator`: Ищет элементы на странице по заданному локейтору.


**Функции:**

* `get_url`:
    * Аргументы: `url` (путь к файлу или URL).
    * Возвращаемое значение: `True` при успехе, `False` при ошибке.
    * Функция `get_url` загружает содержимое HTML из файла или URL и сохраняет его в атрибуте `html_content` класса `BS`.

* `execute_locator`:
    * Аргументы: `locator` (объект SimpleNamespace или словарь с информацией о локейторе), `url` (опциональный параметр для перегрузки `url`).
    * Возвращаемое значение: список найденных элементов (или None).
    * Функция выполняет поиск элементов на странице с помощью XPath на основе данных из `locator` и возвращает список найденных элементов.

**Переменные:**

* `MODE`: Переменная, хранит режим работы.
* `locator`: Объект `SimpleNamespace`, передается в функцию `execute_locator` для указания локейтора.
* `url`: Строка, представляющая собой URL.


**Возможные ошибки и улучшения:**

* Недостаточно обработан случай, когда в `locator.selector` есть ошибки (например, неверный XPath).
* Отсутствует обработка различных типов локейторов (например, "LINK TEXT", "PARTIAL LINK TEXT").
* Функция `execute_locator` слишком специфична и жестко связана с классами `Driver` и `SimpleNamespace`. Нужно добавить обработку разных типов локейторов.
* Нет явного логирования в методе `execute_locator` при неудачном поиске элементов, добавление логирования в случае, если функция не смогла найти ничего по заданному XPath-выражению.

**Взаимосвязь с другими частями проекта:**

Код активно использует классы и методы из `src.webdriver` и `src.logger`, что указывает на использование фреймворка для работы с веб-драйвером и логированием. Класс `Driver` скорее всего, отвечает за инициализацию и взаимодействие с веб-драйвером.  Взаимодействия с `gs` пока не очевидно, но предполагается, что этот модуль может быть вовлечен в последующие этапы обработки данных.