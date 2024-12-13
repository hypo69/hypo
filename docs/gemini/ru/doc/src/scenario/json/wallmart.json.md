# Документация для `hypotez/src/scenario/json/wallmart.json`

## Обзор

Данный JSON-файл содержит конфигурацию для парсинга веб-сайта поставщика `ksp`. Он определяет основные настройки для процесса сбора данных о продуктах, включая URL-адрес начала работы, правила ценообразования и другие параметры.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [supplier](#supplier)
    - [supplier_prefix](#supplier_prefix)
    - [start_url](#start_url)
    - [price_rule](#price_rule)
    - [num_items_4_flush](#num_items_4_flush)
    - [if_login](#if_login)
    - [collect_products_from_categorypage](#collect_products_from_categorypage)
    - [parcing method [webdriver|api]](#parcing-method-webdriverapi)
    - [about method web scrapping [webdriver|api]](#about-method-web-scrapping-webdriverapi)
    - [scenarios](#scenarios)

## Структура JSON

### `supplier`

**Описание**: Название поставщика.

**Тип**: `string`

**Значение**: `ksp`

### `supplier_prefix`

**Описание**: Префикс для идентификации поставщика.

**Тип**: `string`

**Значение**: `ksp`

### `start_url`

**Описание**: URL-адрес начальной страницы сайта для парсинга.

**Тип**: `string`

**Значение**: `https://www.ksp.co.il/`

### `price_rule`

**Описание**: Правило для расчета цены. В данном случае, к исходной цене добавляется 100.

**Тип**: `string`

**Значение**: `+100`

### `num_items_4_flush`

**Описание**: Количество элементов, после обработки которых нужно сбросить данные.

**Тип**: `number`

**Значение**: `300`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход в систему.

**Тип**: `boolean`

**Значение**: `false`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать продукты со страниц категорий.

**Тип**: `boolean`

**Значение**: `false`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга данных. Может быть `web` или `api`.

**Тип**: `string`

**Значение**: `web`

### `about method web scrapping [webdriver|api]`

**Описание**: Описание метода парсинга веб-страницы.

**Тип**: `string`

**Значение**: `Если я работаю через API мне не нужен webdriver`

### `scenarios`

**Описание**: Словарь, содержащий сценарии парсинга. В данном файле пуст.

**Тип**: `dict`

**Значение**: `{}`