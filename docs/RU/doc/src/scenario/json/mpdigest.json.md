# Документация для `mpdigest.json`

## Обзор

Файл `mpdigest.json` содержит конфигурационные данные для поставщика `mpdigest`. Он определяет основные URL, правила ценообразования, условия входа в систему, категории товаров, а также ссылки на другие сценарии и исключения. Этот файл используется для сбора и обработки данных о продуктах с сайта поставщика `mpdigest` и других связанных с ним ресурсов.

## Оглавление
1.  [Основные параметры](#основные-параметры)
2.  [Ссылки на AliExpress](#ссылки-на-aliexpress)
3.  [Сценарии](#сценарии)
4.  [Исключения](#исключения)

## Основные параметры
### `supplier`
**Описание**: Название поставщика.
- **Значение**: `"mpdigest"`
### `supplier_prefix`
**Описание**: Префикс поставщика.
- **Значение**: `"mpdigest"`
### `start_url`
**Описание**: Начальный URL для сбора данных.
- **Значение**: `"https://www.mpdigest.com/category/on-the-market/"`
### `price_rule`
**Описание**: Правило ценообразования.
- **Значение**: `"+0"`
### `if_login`
**Описание**: Указывает, требуется ли вход в систему.
- **Значение**: `false`
### `login_url`
**Описание**: URL для входа в систему (если требуется).
- **Значение**: `""` (пустая строка, так как `if_login` равен `false`)
### `root_category`
**Описание**: Корневая категория.
- **Значение**: `3`
### `collect_products_from_categorypage`
**Описание**: Указывает, нужно ли собирать продукты со страницы категории.
- **Значение**: `false`

## Ссылки на AliExpress

### `aliexpres_ajax_store`
**Описание**: URL для AJAX-запросов к магазинам AliExpress.
- **Значение**: `"https://he.aliexpress.com/store/productGroupsAjax.htm?storeId="`
### `catalog_wholesale-products`
**Описание**: Каталог оптовых продуктов на AliExpress для разных языковых версий.
- **Значение**: 
    - `"ALL NOT SORTED"`: `"https://www.aliexpress.com/wholesale.html?spm=a2g0o.11810135.0.0.61b4IPjRIPjR75"`
    - `"HE"`: `"https://www.he.aliexpress.com/shop categories page.html"`
    - `"RU"`: `"https://www.aliexpress.com/shop categories page.html"`
    - `"EN"`: `"https://www.aliexpress.com/shop categories page.html"`
    - `"FR"`: `"https://fr.aliexpress.com/shop categories page.html"`

## Сценарии

### `scenario_files`
**Описание**: Список файлов сценариев для обработки.
- **Значение**:
    - `"aliexpress_stores_elctronic_toys.json"`
    - `"aliexpress_stores_baby_clothing.json"`

## Исключения

### `excluded`
**Описание**: Список исключенных файлов сценариев.
- **Значение**:
    - `"aliexpress_stores_battery.json"`
    - `"aliexpress_stores_brands.json"`
    - `"aliexpress_stores_computer_components.json"`
    - `"aliexpress_stores_computer_components_fans.json"`
    - `"aliexpress_stores_computers.json"`
    - `"aliexpress_stores_electronics.json"`
    - `"aliexpress_stores_elctronic_components_audio.json"`
    - `"aliexpress_stores_elctronic_components_leds.json"`
    - `"aliexpress_stores_elctronic_toys.json"`
    - `"aliexpress_stores_lighting.json"`
    - `"aliexpress_stores_leds.json"`
    - `"aliexpress_stores_malls.json"`
    - `"aliexpress_stores_memory.json"`
    - `"aliexpress_stores_phones_repair_computers.json"`