# Документация для `morlevi_categories_monitors_dell.json`

## Обзор

Данный файл содержит JSON-структуру с описанием сценариев для парсинга категорий мониторов бренда DELL с сайта morlevi.co.il. Каждый сценарий включает информацию о размере монитора, URL для парсинга, флаги активности и соответствия, а также категории PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
  - [Сценарий](#сценарий)
    - [brand](#brand)
    - [url](#url)
    - [checkbox](#checkbox)
    - [active](#active)
    - [condition](#condition)
    - [presta_categories](#presta_categories)

## Структура JSON

### `scenarios`

Объект, содержащий сценарии для парсинга. Ключи - это названия сценариев (например, "DELL 22").

```json
{
  "scenarios": {
    "DELL 22": {
      "brand": "DELL",
      "url": "--------------------------------- DELL 22 -----------------------------------------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,128,528"
    },
    "DELL 24-25": {
      "brand": "DELL",
      "url": "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1807&p_75=483&p_75=292&p_75=293&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "127,129,528"
    },
    "DELL 27-29": {
      "brand": "DELL",
      "url": "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1808&p_75=297&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "127,130,528"
    },
    "DELL 32": {
      "brand": "DELL",
      "url": "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1809&p_75=298&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,131,528"
    },
    "DELL 34": {
      "brand": "DELL",
      "url": " --------------------------  DELL 34 -----------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,132,528"
    },
    "DELL 49": {
      "brand": "DELL",
      "url": "-----------------------------  DELL 49 ---------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,133,528"
    }
  }
}
```

### Сценарий

Каждый сценарий представлен объектом со следующими полями:

#### `brand`

**Описание**: Строка, представляющая бренд товара.

**Тип**: `string`

**Пример**: `"DELL"`

#### `url`

**Описание**: Строка, представляющая URL для парсинга.

**Тип**: `string`

**Пример**: `"https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1807&p_75=483&p_75=292&p_75=293&sort=datafloat2%2Cprice&keyword="`

#### `checkbox`

**Описание**: Логическое значение, указывающее, включен ли сценарий.

**Тип**: `boolean`

**Пример**: `false`

#### `active`

**Описание**: Логическое значение, указывающее, активен ли сценарий.

**Тип**: `boolean`

**Пример**: `true`

#### `condition`

**Описание**: Строка, представляющая состояние товара.

**Тип**: `string`

**Пример**: `"new"`

#### `presta_categories`

**Описание**: Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

**Тип**: `string`

**Пример**: `"127,129,528"`