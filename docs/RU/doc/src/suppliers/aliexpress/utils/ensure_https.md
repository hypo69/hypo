# Модуль `hypotez/src/suppliers/aliexpress/utils/ensure_https.py`

## Обзор

Модуль `ensure_https` предназначен для обеспечения того, что предоставленная строка(и) URL содержит префикс `https://`. Если входные данные представляют собой идентификатор продукта, модуль строит полный URL с префиксом `https://`.

## Функции

### `ensure_https`

**Описание**: Функция проверяет, что входные данные (строка или список строк) содержат префикс `https://`. Если нет, добавляет его. Если вход – это идентификатор продукта, функция создает полный URL с `https://` и базовым адресом `aliexpress.com`.

**Параметры**:

- `prod_ids` (str | list[str]): Строка URL или список строк URL, которые необходимо проверить и изменить при необходимости.

**Возвращает**:

- str | list[str]: Строка URL или список строк URL с префиксом `https://`.

**Возможные исключения**:

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

**Описание**: Функция проверяет, что входная строка (URL или идентификатор продукта) содержит префикс `https://`. Если нет, добавляет его. Если вход – это идентификатор продукта, функция создает полный URL с `https://` и базовым адресом `aliexpress.com`.

**Параметры**:

- `prod_id` (str): Строка URL или идентификатор продукта.

**Возвращает**:

- str: Строка URL с префиксом `https://`.

**Возможные исключения**:

- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:

```python
>>> ensure_https_single("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https_single("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
```

## Использование

Функция `ensure_https` используется для обработки как одиночных URL, так и списков URL, добавляя префикс `https://` к адресам или строкам, представляющим идентификаторы товаров. Обратите внимание на обработку ошибок в случае невалидных входных данных и логгирования ошибок.
```
```