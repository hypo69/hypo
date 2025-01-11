# Документация для `hypotez/src/suppliers/amazon/scenarios/amazon_categories_ottomans.json`

## Обзор

Файл `amazon_categories_ottomans.json` содержит JSON-конфигурацию для сценария обработки категории "OTOMANS" (пуфики) на Amazon. Включает в себя URL, условия, настройки категорий PrestaShop и правило ценообразования.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
    - [OTOMANS](#ottomans)
      - [url](#url)
      - [condition](#condition)
      - [presta_categories](#presta_categories)
        - [default_category](#default_category)
        - [additional_categories](#additional_categories)
      - [price_rule](#price_rule)

## Структура JSON

### `scenarios`

Корневой объект, содержащий сценарии для обработки категорий.

### `OTOMANS`

Объект, описывающий сценарий обработки категории "OTOMANS" (пуфики).

#### `url`

**Описание**: URL-адрес для поиска товаров категории "OTOMANS" на Amazon.

**Значение**:
```
"https://amzn.to/44Mknp7"
```

#### `condition`

**Описание**: Условие для отбора товаров.

**Значение**:
```
"new"
```

#### `presta_categories`

Объект, описывающий настройки категорий PrestaShop для данной категории Amazon.

##### `default_category`

**Описание**: Объект, определяющий соответствие между ID категории PrestaShop и названием категории.

**Значение**:
```
{ "11057": "OTOMANS" }
```

##### `additional_categories`

**Описание**: Массив дополнительных категорий PrestaShop. В данном случае массив пуст.

**Значение**:
```
[ "" ]
```
#### `price_rule`

**Описание**: Правило ценообразования, применяемое к товарам.

**Значение**:
```
1
```