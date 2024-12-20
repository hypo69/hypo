# Документация для `men-treatment.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [scenarios](#scenarios)
    - [url](#url)
    - [name](#name)
    - [condition](#condition)
    - [presta_categories](#presta_categories)
    - [default_category](#default_category)
    - [additional_categories](#additional_categories)

## Обзор

Данный файл `men-treatment.json` содержит конфигурацию для сценария обработки товаров из категории "טיפוח לגבר" (уход для мужчин) с сайта hbdeadsea.co.il. Он определяет URL, имя, условие новизны товаров и категории PrestaShop, к которым относятся эти товары.

## Структура JSON

### `scenarios`

**Описание**: Корневой объект, содержащий настройки для сценария обработки.

### `url`

**Описание**: URL страницы с товарами.

**Тип**: `строка`

**Значение**: `https://hbdeadsea.co.il/product-category/men-treatment/`

### `name`

**Описание**: Название категории товаров.

**Тип**: `строка`

**Значение**: `טיפוח לגבר`

### `condition`

**Описание**: Условие для товаров (в данном случае - "new").

**Тип**: `строка`

**Значение**: `new`

### `presta_categories`

**Описание**: Объект, содержащий настройки категорий PrestaShop.

### `default_category`

**Описание**: ID категории PrestaShop по умолчанию.

**Тип**: `число`

**Значение**: `11111`

### `additional_categories`

**Описание**: Массив дополнительных категорий PrestaShop.

**Тип**: `массив`

**Значение**: `[""]`

**Примечание**: В данном случае массив содержит пустую строку, что означает отсутствие дополнительных категорий.