# Документация для `livingroom.json`

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
    - [Tables](#tables)
  - [excluded](#excluded)
    - [Designed armchairs](#designed-armchairs)
    - [Dressers for the living room](#dressers-for-the-living-room)
    - [Sofas and Sectionals](#sofas-and-sectionals)
    - [Bookcases and Display Cabinets](#bookcases-and-display-cabinets)
    - [Tables cofee](#tables-cofee)
   

## Обзор

Файл `livingroom.json` содержит конфигурацию для сбора данных о товарах для гостиной с сайта Kualastyle. Он определяет сценарии для сбора данных, а также исключения, которые не нужно обрабатывать.

## Структура JSON

### `scenarios`

Содержит сценарии сбора данных.

#### `Tables`
- **Описание**: Настройки для сбора данных о столах.
    - **`url`** (str): URL-адрес для сбора данных.
    - **`condition`** (str): Условие сбора данных ("new").
    - **`presta_categories`** (dict): Соответствие категорий PrestaShop.
        - **`default_category`** (dict): Словарь с соответствиями категорий.
           - `"10997"` (str): Идентификатор категории PrestaShop и его имя.
    - **`price_rule`** (int): Правило цены.

### `excluded`

Содержит исключенные из обработки категории товаров.

#### `Designed armchairs`

- **Описание**: Настройки исключения для дизайнерских кресел.
    - **`url`** (str): URL-адрес исключенной категории.
    - **`condition`** (str): Условие для исключения ("new").
    - **`presta_categories`** (dict): Категории PrestaShop.
         - **`default_category`** (dict): Соответствие категорий.
            - `"11057"` (str): Идентификатор категории и его имя.
    - **`price_rule`** (int): Правило цены.

#### `Dressers for the living room`

- **Описание**: Настройки исключения для комодов для гостиной.
    - **`url`** (str): URL-адрес исключенной категории.
    - **`condition`** (str): Условие для исключения ("new").
    - **`presta_categories`** (dict): Категории PrestaShop.
        - **`default_category`** (dict): Соответствие категорий.
           -  `"11059"` (str): Идентификатор категории и его имя.
    - **`price_rule`** (int): Правило цены.
    
#### `Sofas and Sectionals`

- **Описание**: Настройки исключения для диванов и секций.
    - **`url`** (str): URL-адрес исключенной категории.
    -  **`active`** (str): Активность исключения.
    - **`condition`** (str): Условие для исключения ("new").
    - **`presta_categories`** (dict): Категории PrestaShop.
        - **`default_category`** (dict): Соответствие категорий.
           -  `"11055"` (str): Идентификатор категории и его имя.
    - **`checkbox`** (str): Флаг для чекбокса.
    - **`price_rule`** (int): Правило цены.

#### `Bookcases and Display Cabinets`

- **Описание**: Настройки исключения для книжных шкафов и витрин.
    - **`url`** (str): URL-адрес исключенной категории.
    - **`condition`** (str): Условие для исключения ("new").
    - **`presta_categories`** (dict): Категории PrestaShop.
        - **`default_category`** (dict): Соответствие категорий.
           - `"11059"` (str): Идентификатор категории и его имя.
    - **`price_rule`** (int): Правило цены.

#### `Tables cofee`

- **Описание**: Настройки исключения для кофейных столиков.
    - **`url`** (str): URL-адрес исключенной категории.
    - **`condition`** (str): Условие для исключения ("new").
    - **`presta_categories`** (dict): Категории PrestaShop.
        - **`default_category`** (dict): Соответствие категорий.
           - `"11058"` (str): Идентификатор категории и его имя.
    - **`price_rule`** (int): Правило цены.