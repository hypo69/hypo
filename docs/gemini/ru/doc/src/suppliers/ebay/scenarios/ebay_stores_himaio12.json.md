# Документация для `ebay_stores_himaio12.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [Секция `store`](#секция-store)
    - [Секция `scenarios`](#секция-scenarios)
        - [Сценарий `Gaming Concoles`](#сценарий-gaming-concoles)
            - [`presta_categories`](#presta_categories)
 
## Обзор

Данный файл в формате JSON содержит конфигурацию магазина eBay с идентификатором `thegasketsman75`, предназначенную для интеграции с другими системами. Он описывает основные параметры магазина и сценарии для загрузки товаров с определёнными условиями.

## Структура JSON

Файл состоит из двух основных секций: `store` и `scenarios`.

### Секция `store`

Секция `store` содержит общую информацию о магазине eBay.

**Описание полей**:

- `store_id` (str): Идентификатор магазина на eBay (`thegasketsman75`).
- `supplier_id` (int): Идентификатор поставщика (4534).
- `get store banners` (bool): Флаг, указывающий на необходимость получения баннеров магазина (`true`).
- `description` (str): Описание магазина (`thegasketsman75 Gasket KIT`).
- `about` (str): Дополнительная информация о магазине (пустая строка).
- `url` (str): URL магазина на eBay (`https://www.ebay.com/str/himaio12`).
- `shop categories page` (str): URL страницы категорий магазина (пустая строка).
- `shop categories json file` (str): Путь к файлу JSON с категориями магазина (пустая строка).

### Секция `scenarios`

Секция `scenarios` содержит набор сценариев для загрузки товаров, сгруппированных по категориям.

#### Сценарий `Gaming Concoles`

Этот сценарий описывает загрузку товаров из категории "Gaming Concoles".

**Описание полей**:

- `url` (str): URL страницы магазина, откуда будет выполняться загрузка (`https://www.ebay.com/str/himaio12`).
- `active` (bool): Флаг, указывающий на активность сценария (`true`).
- `condition` (str): Условие товара (`new`).
- `presta_categories` (dict): Словарь с категориями PrestaShop, к которым будут привязаны товары.
- `checkbox` (bool): Флаг для использования чекбокса ( `false` ).
- `price_rule` (int): Правило ценообразования (1).

##### `presta_categories`

Содержит соответствие категорий eBay и PrestaShop.

**Описание полей**:

- `template` (dict): Категории в формате `{"ebay_category": "presta_category"}`.
    - `gaming` (str): Категория `CONSOLES`  в PrestaShop.