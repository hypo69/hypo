# Документация для `ksp_categories_headphones_xiaomi.json`

## Обзор

Данный файл содержит JSON-структуру, описывающую сценарии для наушников Xiaomi, включая их URL-адреса на сайте KSP, условия, категории PrestaShop и другие параметры.

## Оглавление

1. [Раздел "scenarios"](#раздел-scenarios)
    - [In-ear Bud](#in-ear-bud)
    - [Xiaomi Mi In-ear Bud cable 3.5mm connection](#xiaomi-mi-in-ear-bud-cable-35mm-connection)
 

## Раздел "scenarios"

Данный раздел содержит сценарии для различных моделей наушников Xiaomi.

### In-ear Bud

**Описание**: Сценарий для наушников In-ear Bud от Xiaomi.

**Параметры**:

- `brand` (str): Бренд наушников, "XIAOMI".
- `url` (str): URL-адрес категории на сайте KSP, "https://ksp.co.il/web/cat/242..2202..1250".
- `checkbox` (bool): Флаг, указывающий, выбран ли чекбокс (в данном случае `false`).
- `active` (bool): Флаг, указывающий, активен ли сценарий (в данном случае `true`).
- `condition` (str): Состояние товара, "new".
- `presta_categories` (dict): Категории PrestaShop.
  - `template` (dict): Шаблон для категорий.
        -  `xiaomi` (str): Категория "HEADPHONES".

### Xiaomi Mi In-ear Bud cable 3.5mm connection

**Описание**: Сценарий для наушников Xiaomi Mi In-ear Bud с кабельным подключением 3.5 мм.

**Параметры**:

- `brand` (str): Бренд наушников, "XIAOMI".
- `url` (str): URL-адрес категории на сайте KSP, "https://ksp.co.il/web/cat/242..2202..1250..5162".
- `checkbox` (bool): Флаг, указывающий, выбран ли чекбокс (в данном случае `false`).
- `active` (bool): Флаг, указывающий, активен ли сценарий (в данном случае `true`).
- `condition` (str): Состояние товара, "new".
- `presta_categories` (dict): Категории PrestaShop.
    - `3459` (str): Категория "Xiaomi Mi In-ear Bud cable 3.5mm connection".
    - `template` (dict): Шаблон для категорий.
        - `xiaomi` (str): Категория "HEADPHONES".
    - `2250` (str): Категория "brand:  XIAOMI".
    - `2479` (str): Категория "BT Earbuds".
    - `3494` (str): Категория "Redmi Buds 3".