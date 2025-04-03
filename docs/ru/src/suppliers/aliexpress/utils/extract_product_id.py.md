# Модуль для извлечения идентификаторов продуктов из URL-адресов AliExpress

## Обзор

Модуль предназначен для извлечения идентификаторов товаров из URL-адресов AliExpress. Он предоставляет функцию `extract_prod_ids`, которая принимает URL-адрес или список URL-адресов и возвращает соответствующий идентификатор товара или список идентификаторов.

## Подробней

Этот модуль полезен для автоматического извлечения идентификаторов продуктов из URL-адресов AliExpress, что может быть полезно для различных целей, таких как мониторинг цен, сбор данных о продуктах и т.д.

## Функции

### `extract_prod_ids`

```python
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

**Назначение**: Извлекает идентификаторы товаров из списка URL-адресов или возвращает идентификаторы, если они уже предоставлены.

**Параметры**:

-   `urls` (str | list[str]): URL-адрес, список URL-адресов или идентификаторы товаров.

**Возвращает**:

-   `str | list[str] | None`: Список извлеченных идентификаторов товаров, один идентификатор или `None`, если не найдено ни одного допустимого идентификатора.

**Как работает функция**:

1.  Функция `extract_prod_ids` принимает на вход строку или список строк, представляющих собой URL-адреса или идентификаторы товаров.
2.  Определяется регулярное выражение `pattern` для поиска идентификаторов товаров в URL-адресах.
3.  Определяется внутренняя функция `extract_id`, которая извлекает идентификатор товара из заданного URL-адреса или проверяет, является ли входная строка допустимым идентификатором товара.
4.  Если входные данные являются списком, функция применяет функцию `extract_id` к каждому URL-адресу в списке и возвращает список извлеченных идентификаторов.
5.  Если входные данные являются строкой, функция вызывает `extract_id` для этой строки и возвращает результат.

```
    Начало
    │
    ├───Является ли urls списком?
    │   ├───Да
    │   │   ├───Применяем extract_id к каждому URL в списке
    │   │   ├───Возвращаем список извлеченных ID
    │   │   │   └───Список пуст? -> Возвращаем None
    │   │   └───Конец
    │   └───Нет
    │       ├───Вызываем extract_id для urls
    │       └───Конец
    └───Конец
```

**Примеры**:

```python
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
```

### `extract_id`

```python
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
```

**Назначение**: Извлекает идентификатор товара из заданного URL-адреса или проверяет, является ли входная строка допустимым идентификатором товара.

**Параметры**:

-   `url` (str): URL-адрес или идентификатор товара.

**Возвращает**:

-   `str | None`: Извлеченный идентификатор товара или сам ввод, если это допустимый идентификатор, или `None`, если не найдено ни одного допустимого идентификатора.

**Как работает функция**:

1.  Функция `extract_id` принимает на вход строку, представляющую собой URL-адрес или идентификатор товара.
2.  Функция проверяет, состоит ли входная строка только из цифр. Если это так, функция предполагает, что это допустимый идентификатор товара, и возвращает его.
3.  В противном случае функция пытается извлечь идентификатор товара из URL-адреса, используя регулярное выражение `pattern`.
4.  Если регулярное выражение находит соответствие, функция возвращает извлеченный идентификатор товара.
5.  Если регулярное выражение не находит соответствия, функция возвращает `None`.

```
    Начало
    │
    ├───Является ли URL числом?
    │   ├───Да
    │   │   ├───Возвращаем URL
    │   │   └───Конец
    │   └───Нет
    │       ├───Пытаемся извлечь ID из URL с помощью регулярного выражения
    │       │   ├───Найдено соответствие?
    │       │   │   ├───Возвращаем извлеченный ID
    │       │   │   └───Конец
    │       │   └───Нет соответствия
    │       │       ├───Возвращаем None
    │       │       └───Конец
    │       └───Конец
    └───Конец
```

**Примеры**:

```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None