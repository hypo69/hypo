# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для обеспечения наличия префикса `https://` в предоставленных URL-строках. Если входные данные представляют собой идентификатор продукта, модуль конструирует полный URL с префиксом `https://`.

## Содержание

1. [Функции](#Функции)
    - [`ensure_https`](#ensure_https)
    - [`ensure_https_single`](#ensure_https_single)

## Функции

### `ensure_https`

**Описание**:
    Гарантирует, что предоставленная URL-строка или список URL-строк содержит префикс `https://`. Если входные данные являются идентификатором продукта, функция строит полный URL с префиксом `https://`.

**Параметры**:
    - `prod_ids` (str | list[str]): URL-строка или список URL-строк для проверки и изменения, если это необходимо.

**Возвращает**:
    - `str | list[str]`: URL-строка или список URL-строк с префиксом `https://`.

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

**Описание**:
    Гарантирует, что отдельная URL-строка или идентификатор продукта имеет префикс `https://`.

**Параметры**:
    - `prod_id` (str): URL-строка или идентификатор продукта.

**Возвращает**:
    - `str`: URL-строка с префиксом `https://`.

**Вызывает исключения**:
    - `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:
```python
>>> ensure_https_single("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https_single("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
```