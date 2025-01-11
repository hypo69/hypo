# Документация для `soap-bar.json`

## Обзор

Файл `soap-bar.json` содержит конфигурацию для обработки данных о мыле в виде брусков с веб-сайта `hbdeadsea.co.il`. Он включает URL-адрес категории, название категории, состояние товаров и соответствие категориям PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [`url`](#url)
    - [`name`](#name)
    - [`condition`](#condition)
    - [`presta_categories`](#presta_categories)
        - [`default_category`](#default_category)
        - [`additional_categories`](#additional_categories)

## Структура JSON

### `url`

**Описание**: URL-адрес категории мыла в виде брусков на веб-сайте `hbdeadsea.co.il`.

**Тип**: `str`

**Пример**: `"https://hbdeadsea.co.il/product-category/soap-bar/"`

### `name`

**Описание**: Название категории на иврите.

**Тип**: `str`

**Пример**: `"סבונים מוצקים"`

### `condition`

**Описание**: Массив, содержащий условия для товаров в этой категории.

**Тип**: `list[str]`

**Пример**: `["new"]`

### `presta_categories`

**Описание**: Объект, содержащий соответствия категориям PrestaShop.

**Тип**: `dict`

#### `default_category`

**Описание**: ID категории по умолчанию в PrestaShop.

**Тип**: `int`

**Пример**: `11111`

#### `additional_categories`

**Описание**: Массив с ID дополнительных категорий в PrestaShop.

**Тип**: `list[str]`

**Пример**: `[""]`