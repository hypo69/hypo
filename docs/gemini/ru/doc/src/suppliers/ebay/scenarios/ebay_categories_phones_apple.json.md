# Документация для `ebay_categories_phones_apple.json`

## Обзор

Файл `ebay_categories_phones_apple.json` содержит JSON-конфигурацию для сценариев сбора данных о телефонах Apple с eBay. Он определяет параметры для различных моделей iPhone, включая URL-адреса для поиска, условия, категории PrestaShop и комбинации продуктов.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [scenarios](#scenarios)
3. [Описание сценариев](#описание-сценариев)
    - [iPhone XS MAX](#iphone-xs-max)
    - [iPhone XS](#iphone-xs)
    - [iPhone XR](#iphone-xr)
    - [iPhone X](#iphone-x)
    - [iPhone SE 2022](#iphone-se-2022)
    - [iPhone SE 2020](#iphone-se-2020)
    - [iPhone SE](#iphone-se)
    - [iPhone 1ST GENERATION](#iphone-1st-generation)
    - [iPhone 11](#iphone-11)
    - [iPhone 11 PRO](#iphone-11-pro)
    - [iPhone 11 PRO MAX](#iphone-11-pro-max)
    - [iPhone 12](#iphone-12)
    - [iPhone 12 MINI](#iphone-12-mini)
    - [iPhone 12 PRO](#iphone-12-pro)
    - [iPhone 12 PRO MAX](#iphone-12-pro-max)
    - [iPhone 13](#iphone-13)
    - [iPhone 13 MINI](#iphone-13-mini)
    - [iPhone 13 PRO](#iphone-13-pro)
    - [iPhone 13 PRO MAX](#iphone-13-pro-max)
    - [iPhone 14](#iphone-14)
    - [iPhone 14 PLUS](#iphone-14-plus)
    - [iPhone 14 PRO](#iphone-14-pro)
    - [iPhone 14 PRO MAX](#iphone-14-pro-max)
    - [iPhone 3G](#iphone-3g)
    - [iPhone 3GS](#iphone-3gs)
    - [iPhone 4](#iphone-4)
    - [iPhone 4S](#iphone-4s)
    - [iPhone 5](#iphone-5)
    - [iPhone 5C](#iphone-5c)
    - [iPhone 5S](#iphone-5s)
    - [iPhone 6](#iphone-6)
    - [iPhone 6 PLUS](#iphone-6-plus)
    - [iPhone 6S](#iphone-6s)
    - [iPhone 6S PLUS](#iphone-6s-plus)
    - [iPhone 7](#iphone-7)
    - [iPhone 7 PLUS](#iphone-7-plus)
    - [iPhone 8](#iphone-8)
    - [iPhone 8 PLUS](#iphone-8-plus)

## Структура JSON

### `scenarios`
Корневой раздел JSON, содержащий в себе все сценарии для сбора данных. Каждый ключ в этом разделе представляет собой конкретную модель iPhone, а значение – это объект с настройками для этой модели.

## Описание сценариев

Каждый сценарий представляет собой объект JSON со следующими ключами:

-   `brand` (str): Бренд продукта, всегда `"APPLE"` для данного файла.
-   `url` (str): URL-адрес для поиска товаров на eBay.
-   `active` (bool): Указывает, активен ли данный сценарий.
-   `condition` (str): Условие товара, в данном случае всегда `"new"`.
-   `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары. Содержит ключ `template`, значение которого – словарь, связывающий "apple" с конкретной моделью iPhone.
-  `product combinations` (list, optional): Список, который определяет комбинации продуктов. Может содержать `"bundle"` и/или `"color"`. Присутствует только у некоторых моделей.
- `checkbox` (bool, optional): Поле, обозначающее, показывать ли чекбокс для данного сценария. Присутствует только у некоторых моделей.

### `iPhone XS MAX`
**Описание**: Сценарий для сбора данных о iPhone XS MAX.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520XS%2520Max`
-   **active**: `true`
-   **condition**: `new`
-   **presta_categories**: `{"template": {"apple": "iPhone XS MAX"}}`
-   **product combinations**: `["bundle", "color"]`

### `iPhone XS`
**Описание**: Сценарий для сбора данных о iPhone XS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520XS`
-   **active**: `true`
-   **condition**: `new`
-   **presta_categories**: `{"template": {"apple": "iPhone XS"}}`
-   **product combinations**: `["bundle", "color"]`

### `iPhone XR`
**Описание**: Сценарий для сбора данных о iPhone XR.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520XR`
-   **active**: `true`
-   **condition**: `new`
-   **presta_categories**: `{"template": {"apple": "iPhone XR"}}`
-   **product combinations**: `["bundle", "color"]`

### `iPhone X`
**Описание**: Сценарий для сбора данных о iPhone X.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520X`
-   **active**: `true`
-   **condition**: `new`
-   **presta_categories**: `{"template": {"apple": "iPhone X"}}`
-   **product combinations**: `["bundle", "color"]`

### `iPhone SE 2022`
**Описание**: Сценарий для сбора данных о iPhone SE 2022.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520SE%2520%25283rd%2520Generation%2529`
-   **active**: `true`
-   **condition**: `new`
-    **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone SE 2022"}}`

### `iPhone SE 2020`
**Описание**: Сценарий для сбора данных о iPhone SE 2020.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520SE%2520%25282nd%2520Generation%2529`
-   **active**: `true`
-   **condition**: `new`
-    **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone SE 2020"}}`

### `iPhone SE`
**Описание**: Сценарий для сбора данных о iPhone SE.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520SE`
-   **active**: `true`
-   **condition**: `new`
-    **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone SE 2022"}}`

### `iPhone 1ST GENERATION`
**Описание**: Сценарий для сбора данных о iPhone 1ST GENERATION.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 1ST GENERATION"}}`

### `iPhone 11`
**Описание**: Сценарий для сбора данных о iPhone 11.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 11"}}`

### `iPhone 11 PRO`
**Описание**: Сценарий для сбора данных о iPhone 11 PRO.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011%2520Pro`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 11 PRO"}}`

### `iPhone 11 PRO MAX`
**Описание**: Сценарий для сбора данных о iPhone 11 PRO MAX.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011%2520Pro%2520Max`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 11 PRO MAX"}}`

### `iPhone 12`
**Описание**: Сценарий для сбора данных о iPhone 12.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 12"}}`

### `iPhone 12 MINI`
**Описание**: Сценарий для сбора данных о iPhone 12 MINI.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012%2520mini`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 12 MINI"}}`

### `iPhone 12 PRO`
**Описание**: Сценарий для сбора данных о iPhone 12 PRO.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012%2520Pro`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 12 PRO"}}`

### `iPhone 12 PRO MAX`
**Описание**: Сценарий для сбора данных о iPhone 12 PRO MAX.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012%2520Pro`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 12 PRO MAX"}}`

### `iPhone 13`
**Описание**: Сценарий для сбора данных о iPhone 13.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 13"}}`

### `iPhone 13 MINI`
**Описание**: Сценарий для сбора данных о iPhone 13 MINI.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013%2520mini`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 13 MINI"}}`

### `iPhone 13 PRO`
**Описание**: Сценарий для сбора данных о iPhone 13 PRO.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013%2520Pro`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 13 PRO"}}`

### `iPhone 13 PRO MAX`
**Описание**: Сценарий для сбора данных о iPhone 13 PRO MAX.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013%2520Pro%2520Max`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 13 PRO MAX"}}`

### `iPhone 14`
**Описание**: Сценарий для сбора данных о iPhone 14.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 14"}}`

### `iPhone 14 PLUS`
**Описание**: Сценарий для сбора данных о iPhone 14 PLUS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014%2520Plus`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 14 PLUS"}}`

### `iPhone 14 PRO`
**Описание**: Сценарий для сбора данных о iPhone 14 PRO.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014%2520Pro`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 14 PRO"}}`

### `iPhone 14 PRO MAX`
**Описание**: Сценарий для сбора данных о iPhone 14 PRO MAX.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014%2520Pro%2520Max`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 14 PRO MAX"}}`

### `iPhone 3G`
**Описание**: Сценарий для сбора данных о iPhone 3G.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25203G`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 3G"}}`

### `iPhone 3GS`
**Описание**: Сценарий для сбора данных о iPhone 3GS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25203GS`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 3GS"}}`

### `iPhone 4`
**Описание**: Сценарий для сбора данных о iPhone 4.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25204`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 4"}}`

### `iPhone 4S`
**Описание**: Сценарий для сбора данных о iPhone 4S.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25204s`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 4S"}}`

### `iPhone 5`
**Описание**: Сценарий для сбора данных о iPhone 5.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25205`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 5"}}`

### `iPhone 5C`
**Описание**: Сценарий для сбора данных о iPhone 5C.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25205c`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 5C"}}`

### `iPhone 5S`
**Описание**: Сценарий для сбора данных о iPhone 5S.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25205s`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 5S"}}`

### `iPhone 6`
**Описание**: Сценарий для сбора данных о iPhone 6.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_fsrp=1&LH_FS=1&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&rt=nc&Model=Apple%2520iPhone%25206&_oaa=1&_dcat=9355`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 6"}}`

### `iPhone 6 PLUS`
**Описание**: Сценарий для сбора данных о iPhone 6 PLUS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25206%2520Plus`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 6 PLUS"}}`

### `iPhone 6S`
**Описание**: Сценарий для сбора данных о iPhone 6S.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_fsrp=1&LH_FS=1&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&rt=nc&Model=Apple%2520iPhone%25206s&_oaa=1&_dcat=9355`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 6S"}}`

### `iPhone 6S PLUS`
**Описание**: Сценарий для сбора данных о iPhone 6S PLUS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_fsrp=1&LH_FS=1&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&rt=nc&Model=Apple%2520iPhone%25206s%2520Plus&_oaa=1&_dcat=9355`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 6S PLUS"}}`

### `iPhone 7`
**Описание**: Сценарий для сбора данных о iPhone 7.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25207`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 7"}}`

### `iPhone 7 PLUS`
**Описание**: Сценарий для сбора данных о iPhone 7 PLUS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25207%2520Plus`
-   **active**: `true`
-   **condition**: `new`
-   **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 7 PLUS"}}`

### `iPhone 8`
**Описание**: Сценарий для сбора данных о iPhone 8.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25208`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 8"}}`

### `iPhone 8 PLUS`
**Описание**: Сценарий для сбора данных о iPhone 8 PLUS.
-   **brand**: `APPLE`
-   **url**: `https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25208%2520Plus`
-   **active**: `true`
-   **condition**: `new`
-  **checkbox**: `false`
-   **presta_categories**: `{"template": {"apple": "iPhone 8 PLUS"}}`