# Модуль ensure_https

## Обзор

Модуль `ensure_https` предназначен для обеспечения того, что предоставленная строка(и) URL содержит префикс `https://`. Если на вход поступает идентификатор продукта, то модуль строит полную URL-адрес с префиксом `https://`.

## Функции

### `ensure_https`

**Описание**: Функция `ensure_https` проверяет, содержит ли предоставленная строка (или список строк) URL префикс `https://`. Если нет, добавляет его.

**Параметры**:

- `prod_ids` (str | list[str]): Строка URL или список строк URL для проверки и изменения при необходимости.


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

**Описание**: Вспомогательная функция `ensure_https_single` обрабатывает одну строку URL или идентификатора продукта.

**Параметры**:

- `prod_id` (str): Строка URL или идентификатора продукта.


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


## Модульные переменные

### `MODE`

**Описание**: Переменная `MODE` содержит значение режима работы. В данном примере - 'dev'.
```