# Документация для `ksp_categories_wathces_apple.json`

## Обзор

Этот файл содержит JSON-конфигурацию сценариев для парсинга данных по Apple Watch с сайта KSP. Он включает в себя настройки для разных моделей Apple Watch, таких как Apple Watch SE, Series 7 и Series 6, а также определяет их характеристики, категории и комбинации параметров.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Сценарии (scenarios)](#сценарии-scenarios)
        - [Apple Watch SE](#apple-watch-se)
        - [Apple Watch Series 7](#apple-watch-series-7)
        - [Apple Watch Series 6](#apple-watch-series-6)
- [Описание полей](#описание-полей)
    - [Общие поля](#общие-поля)
    - [Поля `presta_categories`](#поля-presta_categories)
    - [Поля `combinations`](#поля-combinations)

## Структура JSON

### Сценарии (scenarios)

Объект `scenarios` содержит в себе определения для различных моделей Apple Watch. Каждый ключ в `scenarios` представляет собой название конкретной модели, а значение - объект с детальными настройками для этой модели.

#### Apple Watch SE

```json
"Apple Watch SE": {
  "brand": "APPLE",
  "url": "https://ksp.co.il/web/cat/2085..245..29185..28724",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": {
    "3405": "GOOGLE PIXEL PRO",
    "3198": "CONSUMER ELECTRONICS",
    "3202": "computer,smartphone,gaming console,smart device",
    "6471": "Smartphones",
    "3403": "GOOGLE"
  },
  "price_rule": 1,
  "combinations": {
    "size:select": "40 mm",
    "color:color": "black",
    "reseller:select": "Autorized Reseller",
    "importer:select": "Official Importer",
    "warranty:select": "1 year"
  }
}
```
#### Apple Watch Series 7

```json
"Apple Watch Series 7": {
  "brand": "APPLE",
  "url": "https://ksp.co.il/web/cat/245..2085..29150..29229",
  "checkbox": false,
  "active": true,
  "condition":"new",
  "presta_categories": {
    "3405": "GOOGLE PIXEL PRO",
    "3198": "CONSUMER ELECTRONICS",
    "3202": "computer,smartphone,gaming console,smart device",
    "6471": "Smartphones",
    "3403": "GOOGLE"
  },
  "price_rule": 1,
  "combinations": {
    "size:select": "40 mm",
    "color:color": "black",
    "reseller:select": "Autorized Reseller",
    "importer:select": "Official Importer",
    "warranty:select": "1 year"
  }
}
```

#### Apple Watch Series 6

```json
"Apple Watch Series 6": {
  "brand": "APPLE",
  "url": "https://ksp.co.il/web/cat/2085..245..16121",
  "checkbox": false,
  "active": true,
  "condition":"new",
   "presta_categories": {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"

      },
  "price_rule": 1,
  "combinations": {
    "size:select": "40 mm",
    "color:color:": "black",
    "reseller:select": "Autorized Reseller",
    "importer:select": "Official Importer",
    "warranty:select": "1 year"
  }
}
```

## Описание полей

### Общие поля

-   `brand` (str): Бренд товара, в данном случае "APPLE".
-   `url` (str): URL-адрес страницы товара на сайте KSP.
-   `checkbox` (bool):  Флаг для чека, не используется.
-   `active` (bool): Флаг, указывающий, активен ли данный сценарий.
-  `condition` (str): Состояние товара.
-  `price_rule` (int):  Правило цены.

### Поля `presta_categories`

-   `presta_categories` (dict): Словарь, связывающий идентификаторы категорий PrestaShop с названиями категорий.
    -   Ключи словаря (str): Идентификатор категории PrestaShop.
    -   Значения словаря (str): Название категории или описание, к которой относится товар.

### Поля `combinations`

-   `combinations` (dict): Словарь, определяющий комбинации характеристик товара.
    -   Ключи словаря (str): Составные ключи в формате "параметр:тип". Например, "size:select", "color:color", и т.д.
    -   Значения словаря (str): Значение параметра. Например, "40 mm" для размера, "black" для цвета.