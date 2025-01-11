# Документация для `aliexpress.json`

## Обзор

Файл `aliexpress.json` содержит конфигурацию для парсера AliExpress. Он определяет основные параметры, такие как URL, правила ценообразования, список сценариев, а также параметры для сбора данных о продуктах. Файл также содержит информацию о последнем запущенном сценарии и прерванном товаре.

## Содержание

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
    -   [supplier](#supplier)
    -   [supplier_id](#supplier_id)
    -   [supplier_prefix](#supplier_prefix)
    -   [start_url](#start_url)
    -   [price_rule](#price_rule)
    -   [if_login](#if_login)
    -   [login_url](#login_url)
    -   [collect_products_from_categorypage](#collect_products_from_categorypage)
    -   [aliexpres_ajax_store](#aliexpres_ajax_store)
    -   [scenario_files](#scenario_files)
    -   [out](#out)
    -   [last_runned_scenario](#last_runned_scenario)
    -   [locator_description](#locator_description)
    -   [scenario_interrupted](#scenario_interrupted)

## Структура файла

### `supplier`

**Описание**: Имя поставщика.

**Тип**: `str`

**Значение**: `"aliexpress"`

### `supplier_id`

**Описание**: Уникальный идентификатор поставщика.

**Тип**: `str`

**Значение**: `"2801"`

### `supplier_prefix`

**Описание**: Префикс для идентификации поставщика.

**Тип**: `str`

**Значение**: `"aliexpress"`

### `start_url`

**Описание**: Начальный URL для парсинга.

**Тип**: `str`

**Значение**: `"https://www.aliexpress.com/"`

### `price_rule`

**Описание**: Правило для расчета цены.

**Тип**: `str`

**Значение**: `"+0"`

### `if_login`

**Описание**: Флаг, указывающий, требуется ли вход в систему.

**Тип**: `bool`

**Значение**: `false`

### `login_url`

**Описание**: URL для входа в систему.

**Тип**: `str`

**Значение**: `"https://www.login.aliexpress.com"`

### `collect_products_from_categorypage`

**Описание**: Флаг, указывающий, следует ли собирать товары со страницы категории.

**Тип**: `bool`

**Значение**: `true`

### `aliexpres_ajax_store`

**Описание**: URL для AJAX запросов для получения данных магазина.

**Тип**: `str`

**Значение**: `"https://he.aliexpress.com/store/productGroupsAjax.htm?storeId="`

### `scenario_files`

**Описание**: Список файлов сценариев для парсинга.

**Тип**: `list[str]`

**Пример**:
```json
[
    "aliexpress_stores_6388_1053035_hi5group.json",
    "aliexpress_stores_baby_clothing.json",
    "towels.json"
]
```

### `out`

**Описание**: Список файлов с результатами парсинга.

**Тип**: `list[str]`

**Пример**:
```json
[
    "aliexpress_stores_6058_911603061_ASUS_ROG.json",
    "aliexpress_stores_6600_911935962_Cellphone_discount_Store.json",
    "aliexpress_stores_2857_4247007_keyestudio_STEM.json",
     ...
]
```

### `last_runned_scenario`

**Описание**: Имя последнего запущенного сценария.

**Тип**: `str`

**Значение**: `"aliexpress_stores_6600_911935962_Cellphone_discount_Store.json"`

### `locator_description`

**Описание**: Описание локатора. (В данном случае пустая строка)

**Тип**: `str`

**Значение**: `""`

### `scenario_interrupted`

**Описание**: Товар, на котором прервался последний сценарий.

**Тип**: `str`

**Значение**: `"iPhone 13 & 13 MINI"`