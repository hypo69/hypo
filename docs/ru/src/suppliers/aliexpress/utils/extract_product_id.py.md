# Модуль для извлечения ID продуктов из URL-адресов AliExpress

## Обзор

Модуль `extract_product_id` предназначен для извлечения идентификаторов (ID) товаров из URL-адресов, связанных с AliExpress. Он предоставляет функциональность для обработки как одиночных URL-адресов, так и списков URL-адресов, возвращая соответствующие ID товаров.

## Подробней

Этот модуль важен для автоматизации процессов, связанных с парсингом данных с AliExpress, позволяя извлекать уникальные идентификаторы товаров для дальнейшего использования, например, для мониторинга цен, анализа ассортимента или интеграции с другими системами. Он использует регулярные выражения для поиска и извлечения ID из URL.

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
```

**Описание**: Извлекает ID товаров из списка URL-адресов или возвращает ID, если он был предоставлен напрямую.

**Как работает функция**:

1.  Определяет, является ли входной параметр (`urls`) списком или строкой.
2.  Если это список, применяет функцию `extract_id` к каждому элементу списка, чтобы извлечь ID товара.
3.  Если это строка, пытается извлечь ID непосредственно из этой строки с помощью функции `extract_id`.
4.  Возвращает список извлеченных ID, одиночный ID или `None`, если ID не найден.

**Параметры**:

*   `urls` (str | list[str]): URL-адрес, список URL-адресов или ID товаров.

**Возвращает**:

*   `str | list[str] | None`: Список извлеченных ID товаров, одиночный ID или `None`, если не найден допустимый ID.

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
```

**Описание**: Извлекает ID товара из заданного URL-адреса или проверяет ID товара.

**Как работает функция**:

1.  Проверяет, является ли входная строка (`url`) числом. Если да, то возвращает её как ID товара.
2.  Если строка не является числом, пытается извлечь ID из URL-адреса с использованием регулярного выражения.
3.  Если ID успешно извлечен, возвращает его. В противном случае возвращает `None`.

**Параметры**:

*   `url` (str): URL-адрес или ID товара.

**Возвращает**:

*   `str | None`: Извлеченный ID товара или входные данные, если они являются допустимым ID, или `None`, если не найден допустимый ID.

**Примеры**:

```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
```