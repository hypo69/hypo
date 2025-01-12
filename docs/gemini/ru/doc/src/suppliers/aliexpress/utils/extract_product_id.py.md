# Модуль `extract_product_id`

## Обзор

Модуль `extract_product_id` предоставляет функции для извлечения идентификаторов товаров из URL-адресов AliExpress. Он также обрабатывает случаи, когда входные данные уже являются идентификаторами товаров.

## Содержание

1. [Функции](#Функции)
    - [`extract_prod_ids`](#extract_prod_ids)
    - [`extract_id`](#extract_id)

## Функции

### `extract_prod_ids`

**Описание**: Извлекает идентификаторы товаров из списка URL-адресов или возвращает идентификаторы, если они переданы напрямую.

**Параметры**:
- `urls` (str | list[str]): URL-адрес, список URL-адресов или идентификаторы товаров.

**Возвращает**:
- `str | list[str] | None`: Список извлеченных идентификаторов товаров, единичный идентификатор или `None`, если не найдено ни одного допустимого идентификатора.

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

**Описание**: Извлекает идентификатор товара из заданного URL-адреса или проверяет его, если это идентификатор товара.

**Параметры**:
- `url` (str): URL-адрес или идентификатор товара.

**Возвращает**:
- `str | None`: Извлеченный идентификатор товара или сам ввод, если он является допустимым идентификатором, или `None`, если допустимый идентификатор не найден.

**Примеры**:
```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
```