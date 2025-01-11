# Документация для `morlevi_categories_monitors_philips-----.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для парсинга мониторов бренда PHILIPS с сайта morlevi.co.il. Каждый сценарий определяет URL для парсинга, бренд, активность, тип товара и категории PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [`PHILIPS 22`](#philips-22)
    - [`PHILIPS 24-25`](#philips-24-25)
    - [`PHILIPS 27-29`](#philips-27-29)
    - [`PHILIPS 32`](#philips-32)
    - [`PHILIPS 34`](#philips-34)
    - [`PHILIPS 49`](#philips-49)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "url": "URL_FOR_PARSING",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": "PRESTA_CATEGORIES_IDS"
    }
  }
}
```

- `"scenarios"`: Объект, содержащий все сценарии парсинга.
    - `"SCENARIO_NAME"`: Ключ, представляющий название сценария.
        - `"brand"`: Строка, содержащая название бренда.
        - `"url"`: Строка, представляющая URL для парсинга.
        - `"checkbox"`: Логическое значение, указывающее, активен ли чекбокс (всегда `false`).
        - `"active"`: Логическое значение, указывающее, активен ли сценарий (всегда `true`).
        - `"condition"`: Строка, указывающая состояние товара (всегда `"new"`).
        - `"presta_categories"`: Строка, содержащая идентификаторы категорий PrestaShop через запятую.

## Сценарии

### `PHILIPS 22`

**Описание**: Сценарий для парсинга мониторов PHILIPS с диагональю 22 дюйма.

**Параметры**:
- `"brand"`: `"PHILIPS"`
- `"url"`: `"https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1805&p_75=289&sort=datafloat2%2Cprice&keyword="`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`: `"127,128,526"`

### `PHILIPS 24-25`

**Описание**: Сценарий для парсинга мониторов PHILIPS с диагональю 24-25 дюймов.

**Параметры**:
- `"brand"`: `"PHILIPS"`
- `"url"`: `"https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1807&p_75=483&sort=datafloat2%2Cprice&keyword="`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`: `"127,129,526"`

### `PHILIPS 27-29`

**Описание**: Сценарий для парсинга мониторов PHILIPS с диагональю 27-29 дюймов.

**Параметры**:
- `"brand"`: `"PHILIPS"`
- `"url"`: `"https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1808&p_75=297&sort=datafloat2%2Cprice&keyword="`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`: `"127,130,526"`

### `PHILIPS 32`

**Описание**: Сценарий для парсинга мониторов PHILIPS с диагональю 32 дюйма.

**Параметры**:
- `"brand"`: `"PHILIPS"`
- `"url"`: `"https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1809&p_75=298&sort=datafloat2%2Cprice&keyword="`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`: `"127,131,526"`

### `PHILIPS 34`

**Описание**: Сценарий для парсинга мониторов PHILIPS с диагональю 34 дюйма.

**Параметры**:
- `"brand"`: `"PHILIPS"`
- `"url"`: `" --------------------------  PHILIPS 34 -----------------------------------"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`: `"127,132,526"`

### `PHILIPS 49`

**Описание**: Сценарий для парсинга мониторов PHILIPS с диагональю 49 дюймов.

**Параметры**:
- `"brand"`: `"PHILIPS"`
- `"url"`: `"-----------------------------  PHILIPS 49 ---------------------------------"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`: `"127,133,526"`