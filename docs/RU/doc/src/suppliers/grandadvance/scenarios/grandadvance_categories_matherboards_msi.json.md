# grandadvance_categories_matherboards_msi.json

## Обзор

Данный файл представляет собой JSON-конфигурацию, содержащую информацию о категориях материнских плат производства MSI для сайта Grand Advance. Каждая запись в JSON описывает категорию материнских плат по сокету, включая URL для получения списка товаров, флаг активности и соответствующие категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [MOTHERBOARD socket 1200](#motherboard-socket-1200)
  - [MOTHERBOARD socket 1151](#motherboard-socket-1151)
  - [MOTHERBOARD socket 2066](#motherboard-socket-2066)
  - [MOTHERBOARD socket AM4](#motherboard-socket-am4)
  - [MOTHERBOARD socket TR4](#motherboard-socket-tr4)

## Структура JSON

### `MOTHERBOARD socket 1200`

**Описание**: Информация о категории материнских плат с сокетом 1200.

**Параметры**:

-   `brand` (str): Производитель материнской платы (`MSI`).
-   `url` (str): URL для получения списка товаров данной категории на сайте Grand Advance.
-   `checkbox` (bool): Флаг для отметки чекбокса. Всегда `false`.
-   `active` (bool): Флаг активности категории (`true`).
-    `condition` (str): Состояние товара (`new`).
-   `presta_categories` (str): Категории PrestaShop, к которым относится данная категория материнских плат.
   
**Пример**:
```json
{
    "brand": "MSI",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=785&manId=69",
    "checkbox": false,
    "active": true, "condition":"new","presta_categories": "56,57,59"
}
```
### `MOTHERBOARD socket 1151`

**Описание**: Информация о категории материнских плат с сокетом 1151.

**Параметры**:

-   `brand` (str): Производитель материнской платы (`MSI`).
-   `url` (str): URL для получения списка товаров данной категории на сайте Grand Advance.
-   `checkbox` (bool): Флаг для отметки чекбокса. Всегда `false`.
-   `active` (bool): Флаг активности категории (`true`).
-    `condition` (str): Состояние товара (`new`).
-   `presta_categories` (str): Категории PrestaShop, к которым относится данная категория материнских плат.
   
**Пример**:
```json
{
    "brand": "MSI",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=733&manId=69",
    "checkbox": false,
    "active": true, "condition":"new","presta_categories": "56,57,60"
}
```
### `MOTHERBOARD socket 2066`

**Описание**: Информация о категории материнских плат с сокетом 2066.

**Параметры**:

-   `brand` (str): Производитель материнской платы (`MSI`).
-   `url` (str): URL для получения списка товаров данной категории на сайте Grand Advance.
-   `checkbox` (bool): Флаг для отметки чекбокса. Всегда `false`.
-   `active` (bool): Флаг активности категории (`true`).
-    `condition` (str): Состояние товара (`new`).
-   `presta_categories` (str): Категории PrestaShop, к которым относится данная категория материнских плат.
   
**Пример**:
```json
{
    "brand": "MSI",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=766&manId=69",
    "checkbox": false,
    "active": true, "condition":"new","presta_categories": "56,57,62"
}
```

### `MOTHERBOARD socket AM4`

**Описание**: Информация о категории материнских плат с сокетом AM4.

**Параметры**:

-   `brand` (str): Производитель материнской платы (`MSI`).
-   `url` (str): URL для получения списка товаров данной категории на сайте Grand Advance.
-   `checkbox` (bool): Флаг для отметки чекбокса. Всегда `false`.
-   `active` (bool): Флаг активности категории (`true`).
-    `condition` (str): Состояние товара (`new`).
-   `presta_categories` (str): Категории PrestaShop, к которым относится данная категория материнских плат.
   
**Пример**:
```json
{
    "brand": "MSI",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=758&manId=69",
    "checkbox": false,
    "active": true, "condition":"new","presta_categories": "56,57,58"
}
```

### `MOTHERBOARD socket TR4`

**Описание**: Информация о категории материнских плат с сокетом TR4.

**Параметры**:

-   `brand` (str): Производитель материнской платы (`MSI`).
-   `url` (str): URL для получения списка товаров данной категории на сайте Grand Advance.
-   `checkbox` (bool): Флаг для отметки чекбокса. Всегда `false`.
-   `active` (bool): Флаг активности категории (`true`).
-    `condition` (str): Состояние товара (`new`).
-   `presta_categories` (str): Категории PrestaShop, к которым относится данная категория материнских плат.

**Пример**:
```json
{
    "brand": "MSI",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=758&manId=69",
    "checkbox": false,
    "active": true, "condition":"new","presta_categories": "56,57,58"
}
```