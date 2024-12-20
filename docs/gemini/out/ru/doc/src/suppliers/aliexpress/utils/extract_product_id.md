# Модуль extract_product_id

## Обзор

Модуль `extract_product_id` предназначен для извлечения идентификаторов продуктов из списков URL-адресов или из единичного URL-адреса. Он может также принимать непосредственно идентификатор продукта. Модуль использует регулярные выражения для извлечения идентификатора из URL-адреса и возвращает список или строку извлеченных идентификаторов.

## Функции

### `extract_prod_ids`

**Описание**: Функция извлекает идентификаторы продуктов из списка URL-адресов или единичного URL-адреса, либо возвращает ID, если входные данные - это ID.

**Параметры**:
- `urls` (str | list[str]): URL-адрес или список URL-адресов, содержащих идентификаторы продуктов, или сам идентификатор продукта.

**Возвращает**:
- str | list[str] | None: Список извлеченных идентификаторов, единичный идентификатор или `None`, если не удалось найти действительный идентификатор.

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

**Вызывает исключения**:
- Нет.


### `extract_id`

**Описание**: Функция извлекает идентификатор продукта из URL-адреса или проверяет, является ли входной строка идентификатором продукта.

**Параметры**:
- `url` (str): URL-адрес или идентификатор продукта.

**Возвращает**:
- str | None: Извлеченный идентификатор продукта, или входное значение, если это действительный идентификатор, или `None`, если действительный идентификатор не найден.

**Примеры**:
```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
```

**Вызывает исключения**:
- Нет.

## Модульные переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы модуля.

**Значение**: `'dev'`


```