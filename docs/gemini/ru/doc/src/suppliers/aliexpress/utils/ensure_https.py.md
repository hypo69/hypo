# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для проверки и обеспечения того, чтобы предоставленные URL-адреса или идентификаторы продуктов содержали префикс `https://`. Если входные данные являются идентификатором продукта, модуль преобразует их в полный URL-адрес с префиксом `https://`.

## Содержание

- [Функции](#Функции)
    - [`ensure_https`](#ensure_https)
    - [`ensure_https_single`](#ensure_https_single)

## Функции

### `ensure_https`

**Описание**: Обеспечивает, чтобы предоставленные URL-адреса или идентификаторы продуктов содержали префикс `https://`. Если входные данные являются идентификатором продукта, он конструирует полный URL-адрес с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): URL-адрес или список URL-адресов для проверки и изменения, если необходимо.

**Возвращает**:
- `str | list[str]`: URL-адрес или список URL-адресов с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

**Примеры**:
```python
>>> ensure_https("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

>>> ensure_https("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
```

### `ensure_https_single`

**Описание**: Обеспечивает, чтобы одиночный URL-адрес или идентификатор продукта имел префикс `https://`.

**Параметры**:
- `prod_id` (str): URL-адрес или идентификатор продукта.

**Возвращает**:
- `str`: URL-адрес с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:
```python
>>> ensure_https_single("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https_single("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
```