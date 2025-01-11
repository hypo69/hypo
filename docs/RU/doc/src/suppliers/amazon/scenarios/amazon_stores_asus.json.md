# Документация для `amazon_stores_asus.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
   - [Раздел "store"](#раздел-store)
   - [Раздел "scenarios"](#раздел-scenarios)
     - [Сценарий "ZenBook"](#сценарий-zenbook)
     - [Сценарий "ROG Gaming"](#сценарий-rog-gaming)
     - [Сценарий "TUF Gaming"](#сценарий-tuf-gaming)
     - [Сценарий "VIVOBook"](#сценарий-vivobook)
     - [Сценарий "ChromeBook"](#сценарий-chromebook)
     - [Сценарий "Asus ProArt Studiobook"](#сценарий-asus-proart-studiobook)
     - [Сценарий "Asus ProArt Desktops"](#сценарий-asus-proart-desktops)

## Обзор

Файл `amazon_stores_asus.json` содержит конфигурацию для парсинга товаров с магазина ASUS на Amazon. Включает в себя общую информацию о магазине и настройки для различных сценариев парсинга, соответствующих разным линейкам продуктов ASUS.

## Структура файла

Файл имеет следующую структуру:

```json
{
  "store": {
      // Информация о магазине
    },
  "scenarios": {
      // Настройки для различных сценариев парсинга
    }
}
```

### Раздел "store"

Содержит общую информацию о магазине ASUS на Amazon.

*   `store_id` (str): Уникальный идентификатор магазина.
*   `supplier_id` (int): Идентификатор поставщика.
*   `get store banners` (bool): Флаг, указывающий, нужно ли получать баннеры магазина.
*   `description` (str): Описание магазина.
*    `about` (str): Дополнительная информация о магазине.
*   `brand` (str): Бренд магазина.
*   `url` (str): URL-адрес магазина на Amazon.
*   `shop categories page` (str): URL-адрес страницы категорий магазина (если есть, пустая строка в данном случае).
*   `shop categories json file` (str): Путь к файлу JSON со списком категорий магазина (если есть, пустая строка в данном случае).

### Раздел "scenarios"

Содержит настройки для различных сценариев парсинга, соответствующих различным линейкам продуктов ASUS.

#### Сценарий "ZenBook"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*   `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).

#### Сценарий "ROG Gaming"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*    `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).

#### Сценарий "TUF Gaming"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*  `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).

#### Сценарий "VIVOBook"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*    `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).

#### Сценарий "ChromeBook"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*   `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).

#### Сценарий "Asus ProArt Studiobook"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*   `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).

#### Сценарий "Asus ProArt Desktops"

*   `brand` (str): Бренд продукта.
*   `url` (str): URL-адрес страницы продукта на Amazon.
*   `active` (bool): Флаг, указывающий, активен ли сценарий.
*   `condition` (str): Состояние товара ("new").
*   `presta_categories` (dict): Соответствие категорий PrestaShop.
    *   `template` (dict): Шаблон категорий.
        * `asus` (str): категория продукта.
*   `checkbox` (bool): Флаг, указывающий, является ли чекбокс (в данном случае `false`).
*   `price_rule` (int): Правило цены (идентификатор).