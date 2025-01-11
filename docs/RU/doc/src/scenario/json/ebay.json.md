# Документация для `ebay.json`

## Обзор

Файл `ebay.json` содержит конфигурационные параметры для сбора данных с сайта eBay. Он определяет поставщика, правила ценообразования, методы сбора данных и другие настройки, необходимые для работы парсера.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [supplier](#supplier)
    - [supplier_prefix](#supplier_prefix)
    - [start_url](#start_url)
    - [price_rule](#price_rule)
    - [supplier_id](#supplier_id)
    - [num_items_4_flush](#num_items_4_flush)
    - [if_login](#if_login)
    - [parcing method [webdriver|api]](#parcing-method-webdriverapi)
    - [about method web scrapping [webdriver|api]](#about-method-web-scrapping-webdriverapi)
    - [collect_products_from_categorypage](#collect_products_from_categorypage)
    - [scenario_files](#scenario_files)
    - [excluded](#excluded)
    - [last_runned_scenario](#last_runned_scenario)

## Структура JSON

### `supplier`

**Описание**: Имя поставщика, в данном случае `ebay`.

**Тип**: `string`

**Значение**: `"ebay"`

### `supplier_prefix`

**Описание**: Префикс поставщика, используемый для идентификации.

**Тип**: `string`

**Значение**: `"ebay"`

### `start_url`

**Описание**: Начальный URL для парсинга сайта eBay.

**Тип**: `string`

**Значение**: `"https://www.ebay.com/"`

### `price_rule`

**Описание**: Правило ценообразования.

**Тип**: `string`

**Значение**: `"1"`

### `supplier_id`

**Описание**: Идентификатор поставщика.

**Тип**: `string`

**Значение**: `"2792"`

### `num_items_4_flush`

**Описание**: Количество элементов, после сбора которых необходимо выполнить сброс (flush).

**Тип**: `number`

**Значение**: `300`

### `if_login`

**Описание**: Флаг, указывающий, нужно ли выполнять вход на сайт.

**Тип**: `boolean`

**Значение**: `false`

### `parcing method [webdriver|api]`

**Описание**: Метод парсинга: `web` (webdriver) или `api`.

**Тип**: `string`

**Значение**: `"web"`

### `about method web scrapping [webdriver|api]`

**Описание**: Пояснение к выбранному методу парсинга.

**Тип**: `string`

**Значение**: `"Если я работаю через API мне не нужен webdriver"`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, нужно ли собирать товары со страницы категории.

**Тип**: `boolean`

**Значение**: `false`

### `scenario_files`

**Описание**: Список файлов сценариев для парсинга.

**Тип**: `array`

**Значение**:
```json
[
    "ebay_categories_phones_apple.json",
    "ebay_stores_mmhfcom.json",
    "ebay_stores_pacificindustriesltd.json",
    "ebay_stores_thegasketsman75.json",
    "ebay_stores_himaio12.json"
]
```

### `excluded`

**Описание**: Список исключенных товаров. На данный момент пуст.

**Тип**: `array`

**Значение**:
```json
[]
```

### `last_runned_scenario`

**Описание**: Имя последнего запущенного сценария. На данный момент пусто.

**Тип**: `string`

**Значение**: `""`