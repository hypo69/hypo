# Документация для `11248 body and spa.json`

## Обзор

Файл `11248 body and spa.json` содержит JSON-конфигурацию для сценариев обработки категорий товаров. В частности, он определяет URL, условия и категории PrestaShop для сценария `feet-hand-treatment`.

## Оглавление

1. [Обзор](#Обзор)
2. [Структура JSON](#Структура-JSON)
    - [Сценарии](#Сценарии)
        - [feet-hand-treatment](#feet-hand-treatment)
            - [url](#url)
            - [condition](#condition)
            - [presta_categories](#presta_categories)
                - [default_category](#default_category)
                - [additional_categories](#additional_categories)
            - [price_rule](#price_rule)


## Структура JSON

### Сценарии

Корневой элемент JSON, содержащий в себе объекты сценариев.

#### `feet-hand-treatment`

Сценарий обработки товаров для категории "feet-hand-treatment".

##### `url`

**Описание**: URL, связанный со сценарием обработки.

**Тип**: `string`

**Пример**: `"https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/"`

##### `condition`

**Описание**: Условие для сценария обработки.

**Тип**: `string`

**Возможные значения**: `"new"`

**Пример**: `"new"`

##### `presta_categories`

**Описание**: Объект, содержащий информацию о категориях PrestaShop.

###### `default_category`

**Описание**: Идентификатор основной категории PrestaShop.

**Тип**: `integer`

**Пример**: `11259`

###### `additional_categories`

**Описание**: Список дополнительных категорий PrestaShop (может быть пустым).

**Тип**: `array`

**Пример**: `[ "" ]`

##### `price_rule`

**Описание**: Правило ценообразования, применимое к сценарию.

**Тип**: `integer`

**Пример**: `1`