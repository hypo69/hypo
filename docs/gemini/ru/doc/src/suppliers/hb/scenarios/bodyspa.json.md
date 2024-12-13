# Документация для `bodyspa.json`

## Обзор

Файл `bodyspa.json` содержит JSON-структуру, описывающую сценарии для категорий товаров "Body Spa" на сайте hbdeadsea.co.il. Каждый сценарий включает URL, имя категории на иврите, условие (в данном случае всегда "new") и информацию о категориях PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Сценарии](#сценарии)
        - [feet-hand-treatment](#feet-hand-treatment)
        - [creams-butters-serums-for-body](#creams-butters-serums-for-body)
        - [bath-products](#bath-products)
        - [soaps-bar](#soaps-bar)
        - [Body and Spa Products](#body-and-spa-products)
        - [desodorants](#desodorants)

## Структура JSON

### Сценарии

Словарь `scenarios` содержит ключи, представляющие собой идентификаторы сценариев, и значения, являющиеся объектами, описывающими каждый сценарий.

#### `feet-hand-treatment`

**Описание**:
Сценарий для категории "טיפוח כפות ידיים ורגליים" (уход за руками и ногами).

**Поля**:
- `url` (str): URL страницы категории на сайте: `https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/`
- `name` (str): Название категории на иврите: `טיפוח כפות ידיים ורגליים`
- `condition` (str): Условие, всегда `new`.
- `presta_categories` (dict):
    - `default_category` (int): ID категории PrestaShop по умолчанию: `11259`.
    - `additional_categories` (list): Список дополнительных ID категорий PrestaShop, пустой список: `[]`.

#### `creams-butters-serums-for-body`

**Описание**:
Сценарий для категории "קרמים, חמאות וסרומים לגוף" (крема, масла и сыворотки для тела).

**Поля**:
- `url` (str): URL страницы категории на сайте: `https://hbdeadsea.co.il/product-category/bodyspa/creams-butters-serums-for-body/`
- `name` (str): Название категории на иврите: `קרמים, חמאות וסרומים לגוף`
- `condition` (str): Условие, всегда `new`.
- `presta_categories` (dict):
    - `default_category` (int): ID категории PrestaShop по умолчанию: `11260`.
    - `additional_categories` (list): Список дополнительных ID категорий PrestaShop, пустой список: `[]`.

#### `bath-products`

**Описание**:
Сценарий для категории "מוצרי רחצה" (продукты для ванны).

**Поля**:
- `url` (str): URL страницы категории на сайте: `https://hbdeadsea.co.il/product-category/bodyspa/bath-products/`
- `name` (str): Название категории на иврите: `מוצרי רחצה`
- `condition` (str): Условие, всегда `new`.
- `presta_categories` (dict):
    - `default_category` (int): ID категории PrestaShop по умолчанию: `11261`.
    - `additional_categories` (list): Список дополнительных ID категорий PrestaShop, пустой список: `[]`.

#### `soaps-bar`

**Описание**:
Сценарий для категории "סבונים מוצקים" (твердое мыло).

**Поля**:
- `url` (str): URL страницы категории на сайте: `https://hbdeadsea.co.il/product-category/soap-bar/https://hbdeadsea.co.il/product-category/soap-bar`
- `name` (str): Название категории на иврите: `סבונים מוצקים`
- `condition` (str): Условие, всегда `new`.
- `presta_categories` (dict):
    - `default_category` (int): ID категории PrestaShop по умолчанию: `11262`.
    - `additional_categories` (list): Список дополнительных ID категорий PrestaShop, пустой список: `[]`.

#### `Body and Spa Products`

**Описание**:
Сценарий для категории "גוף וספא" (тело и спа).

**Поля**:
- `url` (str): URL страницы категории на сайте: `https://hbdeadsea.co.il/product-category/bodyspa/body-spa-products/`
- `name` (str): Название категории на иврите: `גוף וספא`
- `condition` (str): Условие, всегда `new`.
- `presta_categories` (dict):
    - `default_category` (int): ID категории PrestaShop по умолчанию: `11263`.
    - `additional_categories` (list): Список дополнительных ID категорий PrestaShop, пустой список: `[]`.

#### `desodorants`

**Описание**:
Сценарий для категории "דאודוראנטים" (дезодоранты).

**Поля**:
- `url` (str): URL страницы категории на сайте: `https://hbdeadsea.co.il/product-category/bodyspa/%d7%93%d7%90%d7%95%d7%93%d7%95%d7%a8%d7%a0%d7%98/`
- `name` (str): Название категории на иврите: `דאודוראנטים`
- `condition` (str): Условие, всегда `new`.
- `presta_categories` (dict):
    - `default_category` (int): ID категории PrestaShop по умолчанию: `11264`.
    - `additional_categories` (list): Список дополнительных ID категорий PrestaShop, пустой список: `[]`.