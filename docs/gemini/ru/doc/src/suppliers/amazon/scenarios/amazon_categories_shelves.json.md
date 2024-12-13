# Документация для файла `amazon_categories_shelves.json`

## Обзор

Файл `amazon_categories_shelves.json` содержит JSON-конфигурацию для сценария импорта данных о полках с Amazon. Конфигурация включает URL товара, условие, сопоставления категорий PrestaShop, и правило ценообразования.

## Содержание

1.  [Обзор](#Обзор)
2.  [Структура JSON](#Структура-JSON)
    - [Сценарии](#Сценарии)
        - [SHELVES](#SHELVES)
            - [url](#url)
            - [condition](#condition)
            - [presta_categories](#presta_categories)
                - [default_category](#default_category)
                - [additional_categories](#additional_categories)
            - [price_rule](#price_rule)
    
## Структура JSON

### Сценарии

Раздел `scenarios` содержит различные сценарии. В данном файле присутствует только один сценарий.

#### SHELVES

Сценарий `SHELVES` описывает правила и параметры для импорта данных о полках.

##### `url`

**Описание**: URL товара на Amazon.

**Тип**: `string`

**Пример**: `"https://amzn.to/3pObxZa"`

##### `condition`

**Описание**: Состояние товара (например, `"new"`).

**Тип**: `string`

**Пример**: `"new"`

##### `presta_categories`

**Описание**:  Сопоставления категорий PrestaShop.

**Тип**: `object`

###### `default_category`

**Описание**:  Сопоставление идентификатора категории PrestaShop с категорией Amazon.

**Тип**: `object`

**Пример**: `{ "11060": "SHELVES" }`

###### `additional_categories`

**Описание**:  Список дополнительных категорий PrestaShop.

**Тип**: `array`

**Пример**: `[ "" ]`

##### `price_rule`

**Описание**: Идентификатор правила ценообразования.

**Тип**: `number`

**Пример**: `1`