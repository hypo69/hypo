```MD
# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/utils/extract_product_id.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.aliexpress.utils 
	:platform: Windows, Unix
	:synopsis:

"""


import re
from src.logger import logger


def extract_prod_ids(urls: str | list[str]) -> str | list[str] | None:
    """ Extracts item IDs from a list of URLs or directly returns IDs if given.

    Args:
        urls (str | list[str]): A URL, a list of URLs, or product IDs.

    Returns:
        str | list[str] | None: A list of extracted item IDs, a single ID, or `None` if no valid ID is found.

    Examples:
        >>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
        '123456'

        >>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
        ['123456', '7891011']

        >>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
        ['123456']

        >>> extract_prod_ids("7891011")
        '7891011'

        >>> extract_prod_ids("https://www.example.com/item/abcdef.html")
        None
    """
    # Regular expression to find product identifiers
    pattern = re.compile(r"(?:item/|/)?(\\d+)\\.html")

    def extract_id(url: str) -> str | None:
        """ Extracts a product ID from a given URL or validates a product ID.

        Args:
            url (str): The URL or product ID.

        Returns:
            str | None: The extracted product ID or the input itself if it's a valid ID, or `None` if no valid ID is found.

        Examples:
            >>> extract_id("https://www.aliexpress.com/item/123456.html")
            '123456'

            >>> extract_id("7891011")
            '7891011'

            >>> extract_id("https://www.example.com/item/abcdef.html")
            None
        """
        # Check if the input is a valid product ID
        if url.isdigit():
            return url

        # Otherwise, try to extract the ID from the URL
        match = pattern.search(url)
        if match:
            return match.group(1)
        return

    if isinstance(urls, list):
        extracted_ids = [extract_id(url) for url in urls if extract_id(url) is not None]
        return extracted_ids if extracted_ids else None
    else:
        return extract_id(urls)
```

# <algorithm>

**Шаг 1:** Функция `extract_prod_ids` принимает на вход `urls` (строку или список строк).

**Шаг 1.1:** Если `urls` является списком, то функция `extract_id` вызывается для каждого элемента списка.  
* **Пример:** `urls = ["https://www.aliexpress.com/item/123456.html", "7891011.html"]`


**Шаг 2:** Функция `extract_id` проверяет, является ли входной параметр `url` строкой, содержащей только цифры. Если да, то это уже идентификатор продукта, и он возвращается.
* **Пример:** `url = "123456"` => возвращается "123456"

**Шаг 3:** Если `url` не является только цифрами, то функция ищет соответствие с регулярным выражением `pattern`.  
* **Пример:** `url = "https://www.aliexpress.com/item/123456.html"` => `match` содержит объект `match` с результатом поиска, и `match.group(1)` возвращает `123456`


**Шаг 4:** Если соответствие найдено, функция `extract_id` возвращает найденный идентификатор. В противном случае возвращается `None`.
* **Пример:** `url = "https://www.example.com/item/abcdef.html"` => возвращается `None`


**Шаг 5:** В функции `extract_prod_ids`, если `urls` – список, все идентификаторы собираются в `extracted_ids`.  
* **Пример:** `extracted_ids = ['123456', '7891011']`


**Шаг 6:** Если `extracted_ids` пуст, возвращается `None`, иначе – список `extracted_ids`.

**Шаг 7:** Если `urls` – строка, то вызывается `extract_id` для этой строки и возвращается результат.



# <mermaid>

```mermaid
graph TD
    A[extract_prod_ids(urls)] --> B{urls is list?};
    B -- Yes --> C[Loop through urls];
    B -- No --> D[extract_id(urls)];
    C --> E[extract_id(url)];
    E -- ID --> F[extracted_ids.append(ID)];
    E -- No ID --> G;
    F --> H{extracted_ids empty?};
    H -- Yes --> I[return None];
    H -- No --> J[return extracted_ids];
    D --> K[return extract_id(urls)];
    G --> H;
    
    subgraph extract_id(url)
        L[Is url digits?];
        L -- Yes --> M[return url];
        L -- No --> N[Search url with pattern];
        N -- Match --> O[return match.group(1)];
        N -- No Match --> P[return None];
    end
```

**Описание подключаемых зависимостей:**

* `re`: Модуль для работы с регулярными выражениями.  Необходим для поиска шаблона в URL.
* `src.logger`: Модуль для логирования. Используется для записи сообщений в лог.  Связь: Функция `extract_prod_ids` не использует `logger`, но импорт позволяет использовать логирование в других частях проекта, связанных с обработкой данных с AliExpress.

# <explanation>

* **Импорты:**
    * `re`: Модуль для работы с регулярными выражениями, необходим для извлечения числовой части идентификатора из URL.
    * `src.logger`: Логгер, позволяющий записывать информацию о выполнении, но в данном случае он не используется.

* **Классы:** Нет классов.

* **Функции:**
    * `extract_prod_ids(urls)`: Функция для извлечения идентификаторов продуктов из списка URL или одной URL-строки. Принимает на вход `urls` (строку или список строк) и возвращает идентификатор продукта (строку) или список идентификаторов, или `None`, если идентификатор не найден.
    * `extract_id(url)`: Вспомогательная функция для извлечения идентификатора продукта из одной URL-строки. Проверяет, является ли входящая строка `url` чистым числом. Если да, то это и есть ID. В противном случае использует регулярное выражение `pattern` для поиска идентификатора в URL. Возвращает идентификатор продукта или `None` при отсутствии.


* **Переменные:**
    * `MODE`: Переменная, хранящая режим работы (в данном случае 'dev').

* **Возможные ошибки или улучшения:**

    * Необходимо проверить корректность входных данных (например, `urls` не должен быть пустым списком).
    *  Можно добавить обработку исключений (например, `ValueError`, если в URL нет ожидаемого формата).
    * Вместо `if extract_id(url) is not None` можно использовать `if extract_id(url)` (проверка на не-None).
    * Добавьте документацию для `MODE` переменной.

**Цепочка взаимосвязей:**

Функция `extract_product_id` находится в слое обработки данных для AliExpress. Она используется в `src/suppliers/aliexpress/pipeline.py` (предполагается) для обработки данных из `aliexpress`, которые получаются из стороннего API.  Результат функции используется для дальнейшей обработки в обработке данных.