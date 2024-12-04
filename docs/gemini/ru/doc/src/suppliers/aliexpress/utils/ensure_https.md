# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для обеспечения того, что предоставленная строка(и) URL содержат префикс `https://`. Если входные данные представляют собой идентификатор продукта, он строит полный URL с префиксом `https://`.

## Функции

### `ensure_https`

**Описание**: Функция проверяет, содержит ли входной URL-адрес или список URL-адресов префикс `https://`. Если нет, добавляет его. Если входной параметр является идентификатором продукта, функция строит полный URL-адрес с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): Строка URL-адреса или список строк URL-адресов, которые необходимо проверить и изменить при необходимости.

**Возвращает**:
- str | list[str]: Строка URL-адреса или список строк URL-адресов с префиксом `https://`.

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

**Описание**: Функция обрабатывает одну строку URL или идентификатор продукта, добавляя префикс `https://`, если он отсутствует.

**Параметры**:
- `prod_id` (str): Строка URL-адреса или идентификатора продукта.

**Возвращает**:
- str: Строка URL-адреса с префиксом `https://`.

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

**Описание**: Переменная `MODE` хранит значение конфигурации (например, "dev", "prod").

```
MODE = 'dev'
```


## Использование

Функция `ensure_https` принимает на вход строку или список строк, представляющих URL-адреса или идентификаторы продуктов. Она возвращает изменённый список URL-адресов или строку. Внутренняя функция `ensure_https_single` обрабатывает одну строку, определяя, является ли она идентификатором продукта и добавляя префикс `https://` при необходимости.  Обратите внимание на логику обработки ошибок и использование логгера.
```
```