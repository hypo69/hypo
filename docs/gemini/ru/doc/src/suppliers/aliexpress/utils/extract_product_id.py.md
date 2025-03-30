# Модуль `extract_product_id`

## Обзор

Модуль `extract_product_id` предназначен для извлечения идентификаторов товаров (product IDs) из URL-адресов, связанных с платформой AliExpress. Он предоставляет функциональность для работы как с единичными URL, так и со списками URL, и возвращает извлеченные идентификаторы. Если в предоставленных URL не удается найти допустимые идентификаторы, модуль возвращает `None`.

## Подробней

Этот модуль играет важную роль в процессах, где необходимо автоматизированно извлекать и обрабатывать идентификаторы товаров с AliExpress. Например, это может быть полезно для мониторинга цен, сбора данных о товарах или интеграции с другими системами. Модуль использует регулярные выражения для поиска и извлечения идентификаторов из URL.
Расположение файла: `hypotez/src/suppliers/aliexpress/utils/extract_product_id.py` указывает на его принадлежность к подсистеме работы с поставщиком AliExpress и утилитам.

## Функции

### `extract_prod_ids`

```python
def extract_prod_ids(urls: str | list[str]) -> str | list[str] | None:
    """
    Args:
        urls (str | list[str]): URL-адрес или список URL-адресов, или идентификаторы продуктов.

    Returns:
        str | list[str] | None: Список извлеченных идентификаторов товаров, одиночный ID или `None`, если не найдено допустимого ID.

    Example:
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

**Описание**: Извлекает идентификаторы товаров из списка URL-адресов или возвращает идентификаторы, если они были переданы напрямую.

**Параметры**:

-   `urls` (str | list[str]): URL-адрес, список URL-адресов или идентификаторы товаров.

**Возвращает**:

-   `str | list[str] | None`: Список извлеченных идентификаторов товаров, одиночный ID или `None`, если не найдено допустимого ID.

**Примеры**:

Примеры использования функции с различными параметрами:

-   Извлечение ID из одного URL:

    ```python
    >>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
    '123456'
    ```

-   Извлечение ID из списка URL:

    ```python
    >>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
    ['123456', '7891011']
    ```

-   Извлечение ID из списка, содержащего невалидный URL:

    ```python
    >>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
    ['123456']
    ```

-   Передача ID напрямую:

    ```python
    >>> extract_prod_ids("7891011")
    '7891011'
    ```

-   Невалидный URL:

    ```python
    >>> extract_prod_ids("https://www.example.com/item/abcdef.html")
    None
    ```

### `extract_id`

```python
def extract_id(url: str) -> str | None:
    """
    Args:
        url (str): URL-адрес или идентификатор продукта.

    Returns:
        str | None: Извлеченный идентификатор продукта или сам ввод, если это допустимый ID, или `None`, если не найдено допустимого ID.

    Example:
        >>> extract_id("https://www.aliexpress.com/item/123456.html")
        '123456'

        >>> extract_id("7891011")
        '7891011'

        >>> extract_id("https://www.example.com/item/abcdef.html")
        None
    """
```

**Описание**: Извлекает идентификатор продукта из заданного URL-адреса или проверяет, является ли вход допустимым идентификатором продукта.

**Параметры**:

-   `url` (str): URL-адрес или идентификатор продукта.

**Возвращает**:

-   `str | None`: Извлеченный идентификатор продукта, сам ввод, если это допустимый ID, или `None`, если не найдено допустимого ID.

**Примеры**:

Примеры использования функции с различными параметрами:

-   Извлечение ID из URL:

    ```python
    >>> extract_id("https://www.aliexpress.com/item/123456.html")
    '123456'
    ```

-   Передача ID напрямую:

    ```python
    >>> extract_id("7891011")
    '7891011'
    ```

-   Невалидный URL:

    ```python
    >>> extract_id("https://www.example.com/item/abcdef.html")
    None
    ```