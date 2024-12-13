# Конфигурация поставщика controldcs

## Обзор

Этот файл содержит конфигурацию для поставщика `controldcs`. Он определяет основные параметры для сбора данных о товарах, включая URL-адреса, правила ценообразования, настройки входа в систему и список файлов сценариев для обработки.

## Оглавление

1.  [Основные параметры](#основные-параметры)
2.  [URL-адреса](#url-адреса)
3.  [Настройки каталога товаров](#настройки-каталога-товаров)
4.  [Файлы сценариев](#файлы-сценариев)
5.  [Исключенные файлы](#исключенные-файлы)

## Основные параметры

### `supplier`
**Описание**: Название поставщика.

**Значение**: `controldcs`

### `supplier_prefix`
**Описание**: Префикс поставщика.

**Значение**: `controldcs`

### `start_url`
**Описание**: Стартовый URL поставщика.

**Значение**: `https://www.controldcs.com/`

### `wholesale_products_url`
**Описание**: URL для оптовых товаров.

**Значение**:  `` (пусто)

### `price_rule`
**Описание**: Правило ценообразования.

**Значение**: `+0`

### `num_items_4_flush`
**Описание**: Количество товаров для сброса.

**Значение**: `300`

### `if_login`
**Описание**: Флаг, указывающий, требуется ли вход в систему.

**Значение**: `true`

### `login_url`
**Описание**: URL для входа в систему.

**Значение**:  `` (пусто)

### `root_category`
**Описание**: Корневая категория.

**Значение**: `3`

### `collect_products_from_categorypage`
**Описание**: Флаг, указывающий, нужно ли собирать товары со страницы категории.

**Значение**: `false`

### `aliexpres_ajax_store`
**Описание**: URL для AJAX-запросов на странице магазина AliExpress.

**Значение**: `https://he.aliexpress.com/store/productGroupsAjax.htm?storeId=`

## URL-адреса

### `catalog_wholesale-products`
**Описание**: URL-адреса для каталога оптовых товаров на разных языках.

**Значение**:
   -  `ALL NOT SORTED`: `https://www.aliexpress.com/wholesale.html?spm=a2g0o.11810135.0.0.61b4IPjRIPjR75`
   -  `HE`: `https://www.he.aliexpress.com/shop categories page.html`
   -  `RU`: `https://www.aliexpress.com/shop categories page.html`
   -  `EN`: `https://www.aliexpress.com/shop categories page.html`
   -  `FR`: `https://fr.aliexpress.com/shop categories page.html`

## Файлы сценариев

### `scenario_files`
**Описание**: Список файлов сценариев для обработки.

**Значение**:
   -  `aliexpress_stores_elctronic_toys.json`
   -  `aliexpress_stores_baby_clothing.json`

## Исключенные файлы

### `excluded`
**Описание**: Список исключенных файлов сценариев.

**Значение**:
   - `aliexpress_stores_battery.json`
   - `aliexpress_stores_brands.json`
   - `aliexpress_stores_computer_components.json`
   - `aliexpress_stores_computer_components_fans.json`
   - `aliexpress_stores_computers.json`
   - `aliexpress_stores_electronics.json`
   - `aliexpress_stores_elctronic_components_audio.json`
   - `aliexpress_stores_elctronic_components_leds.json`
   - `aliexpress_stores_elctronic_toys.json`
   - `aliexpress_stores_lighting.json`
   - `aliexpress_stores_leds.json`
   - `aliexpress_stores_malls.json`
   - `aliexpress_stores_memory.json`
   - `aliexpress_stores_phones_repair_computers.json`