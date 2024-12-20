# Документация для файла `amazon_stores_lenovo.json`

## Обзор

Файл `amazon_stores_lenovo.json` содержит конфигурацию для сбора данных о товарах из магазина Lenovo на Amazon. Он определяет структуру магазина, его идентификаторы, URL, а также сценарии для различных категорий товаров, таких как ZenBook, ROG Gaming, TUF Gaming и другие. Каждый сценарий содержит URL, флаг активности, условие (например, "new"), соответствующие категории PrestaShop и правило ценообразования.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [store](#store)
    - [scenarios](#scenarios)
        - [ZenBook](#zenbook)
        - [ROG Gaming](#rog-gaming)
        - [TUF Gaming](#tuf-gaming)
        - [VIVOBook](#vivobook)
        - [ChromeBook](#chromebook)
        - [Asus ProArt Studiobook](#asus-proart-studiobook)
        - [Asus ProArt Desktops](#asus-proart-desktops)

## Структура JSON

### `store`

Объект `store` содержит основную информацию о магазине Lenovo на Amazon.

**Описание**:

Основные сведения о магазине, включая идентификаторы, URL, и настройки для сбора данных.

**Поля**:

- `store_id` (str): Уникальный идентификатор магазина.
- `supplier_id` (int): Идентификатор поставщика.
- `get store banners` (bool): Флаг для получения баннеров магазина.
- `description` (str): Описание магазина.
- `about` (str): Информация о магазине.
- `url` (str): URL магазина на Amazon.
- `shop categories page` (str): URL страницы категорий магазина (в данном случае пустая строка).
- `shop categories json file` (str): Путь к JSON-файлу категорий магазина (в данном случае пустая строка).
-   `scenarios` (dict): Словарь, содержащий сценарии для сбора данных о различных продуктах.

### `scenarios`

Объект `scenarios` содержит сценарии для сбора данных о конкретных категориях товаров.

**Описание**:

Набор сценариев, каждый из которых описывает условия для парсинга товаров определенной категории.

Каждый сценарий имеет следующие поля:
- `url` (str): URL страницы категории товаров.
- `active` (bool): Флаг активности сценария (активен или нет).
-   `condition` (str): Условие товара.
- `presta_categories` (dict): Соответствие категорий Amazon категориям PrestaShop.
- `checkbox` (bool): Флаг для использования чекбокса при выборе товаров.
- `price_rule` (int): Правило ценообразования.

#### `ZenBook`

**Описание**:
Сценарий для сбора данных о ноутбуках ZenBook.
#### `ROG Gaming`

**Описание**:
Сценарий для сбора данных о товарах ROG Gaming.
#### `TUF Gaming`

**Описание**:
Сценарий для сбора данных о товарах TUF Gaming.
#### `VIVOBook`

**Описание**:
Сценарий для сбора данных о ноутбуках VIVOBook.
#### `ChromeBook`

**Описание**:
Сценарий для сбора данных о ноутбуках ChromeBook.
#### `Asus ProArt Studiobook`

**Описание**:
Сценарий для сбора данных о ноутбуках Asus ProArt Studiobook.
#### `Asus ProArt Desktops`

**Описание**:
Сценарий для сбора данных о десктопах Asus ProArt.

## Заключение

Этот документ описывает структуру и содержание файла `amazon_stores_lenovo.json`, используемого для конфигурации сбора данных о товарах из магазина Lenovo на Amazon. Разработчики могут использовать эту информацию для понимания и модификации конфигурации магазина.