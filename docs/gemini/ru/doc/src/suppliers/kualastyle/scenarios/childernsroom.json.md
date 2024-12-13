# Документация для `childernsroom.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сбора данных о товарах из раздела детской комнаты на сайте Kualastyle. Конфигурация разделена на сценарии для разных типов товаров, включая кровати Noar и шкафы.

## Оглавление

- [Сценарии](#Сценарии)
    - [Noar Beds](#Noar-Beds)
    - [Aronot](#Aronot)
        - [Noar Beds](#Noar-Beds-1)

## Сценарии

### `Noar Beds`

**Описание**:
Конфигурация для сбора данных о кроватях Noar.

**Поля**:
- `url` (str): URL-адрес страницы с кроватями Noar.
- `condition` (str): Условие товара (например, "new").
- `presta_categories` (dict): Категории PrestaShop, в которые должны быть отнесены товары.
    - `default_category` (dict): Словарь, сопоставляющий ID категории PrestaShop с путем к категории.
- `price_rule` (int): Правило ценообразования.

**Пример**:
```json
{
    "url": "https://kualastyle.com/collections/%D7%9E%D7%99%D7%98%D7%95%D7%AA-%D7%A0%D7%95%D7%A2%D7%A8",
    "condition": "new",
    "presta_categories": {
      "default_category": { "11025": "home->furniture->childernroom->noarberd" }
    },
    "price_rule": 1
}
```

### `Aronot`

**Описание**:
Раздел с конфигурацией для сбора данных о шкафах.

#### `Noar Beds`
**Описание**:
Конфигурация для сбора данных о шкафах из раздела Noar Beds.

**Поля**:
- `url` (str): URL-адрес страницы со шкафами Noar.
- `condition` (str): Условие товара (например, "new").
- `presta_categories` (dict): Категории PrestaShop, в которые должны быть отнесены товары.
    - `default_category` (dict): Словарь, сопоставляющий ID категории PrestaShop с путем к категории.
- `price_rule` (int): Правило ценообразования.

**Пример**:
```json
{
    "url": "https://kualastyle.com/collections/%D7%90%D7%A8%D7%95%D7%A0%D7%95%D7%AA-%D7%97%D7%93%D7%A8%D7%99-%D7%99%D7%9C%D7%93%D7%99%D7%9D",
    "condition": "new",
    "presta_categories": {
        "default_category": { "11071": "home->furniture->childernroom->noarberd" }
    },
    "price_rule": 1
}
```