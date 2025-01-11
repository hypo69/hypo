# Модуль `extract_product_id`

## Обзор

Модуль `extract_product_id` предназначен для извлечения идентификаторов продуктов (item IDs) из URL-адресов AliExpress или их проверки, если предоставлен непосредственно ID. Он поддерживает как единичные URL, так и списки URL, а также проверку предоставленных ID.

## Содержание

1.  [Функции](#Функции)
    -   [`extract_prod_ids`](#extract_prod_ids)

## Функции

### `extract_prod_ids`

**Описание**: Извлекает идентификаторы продуктов из списка URL-адресов или возвращает их, если даны непосредственно ID.

**Параметры**:

-   `urls` (str | list[str]): URL-адрес, список URL-адресов или идентификаторы продуктов.

**Возвращает**:

-   `str | list[str] | None`: Список извлеченных идентификаторов продуктов, отдельный ID или `None`, если не найдено ни одного допустимого ID.

**Примеры использования:**

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
   
#### `extract_id`

**Описание**: Извлекает идентификатор продукта из заданного URL-адреса или проверяет ID продукта.

**Параметры**:

-   `url` (str): URL-адрес или идентификатор продукта.

**Возвращает**:

-   `str | None`: Извлеченный идентификатор продукта, входные данные, если они являются допустимым ID, или `None`, если не найден допустимый ID.

**Примеры использования:**

```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
```