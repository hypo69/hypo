# Модуль `hypotez/src/suppliers/aliexpress/utils/ensure_https.py`

## Обзор

Модуль `ensure_https.py` отвечает за обеспечение того, что предоставленные URL-строки содержат префикс `https://`. Если входные данные представляют собой идентификатор продукта, модуль строит полный URL-адрес с префиксом `https://`.

## Функции

### `ensure_https`

**Описание**: Функция проверяет, что входные данные (строка или список строк) содержат префикс `https://`. Если нет, добавляет его.

**Параметры**:
- `prod_ids` (str | list[str]): URL-строка или список URL-строк для проверки и изменения, если необходимо.

**Возвращает**:
- str | list[str]: URL-строка или список URL-строк с префиксом `https://`.

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

**Описание**: Функция проверяет, что одна URL-строка или идентификатор продукта содержит префикс `https://`. Если нет, добавляет его.

**Параметры**:
- `prod_id` (str): URL-строка или идентификатор продукта.

**Возвращает**:
- str: URL-строка с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:
```python
>>> ensure_https_single("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https_single("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
```

## Модульные переменные

### `MODE`

**Описание**: Переменная, содержащая режим работы модуля.


```
```