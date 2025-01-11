# Документация для `morlevi_categories_monitors_lenovo.json`

## Обзор

Файл `morlevi_categories_monitors_lenovo.json` содержит JSON-структуру, определяющую сценарии для сбора данных о мониторах Lenovo с веб-сайта Morlevi. Каждый сценарий соответствует определенному размеру мониторов и включает URL-адрес для сбора данных, настройки фильтрации и сопоставление с категориями PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [`LENOVO 21 - 22`](#lenovo-21---22)
    - [`LENOVO 23 - 24`](#lenovo-23---24)
    - [`LENOVO 26 - 28`](#lenovo-26---28)
    - [`LENOVO 27 - 29`](#lenovo-27---29)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "url": "URL_TO_SCRAPE",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "CONDITION_TYPE",
      "presta_categories": {
        "template": {
          "TEMPLATE_NAME": "PRESTA_CATEGORY_NAME"
        }
      }
    }
  }
}
```

Где:

- `scenarios`:  Объект, содержащий сценарии сбора данных.
- `SCENARIO_NAME`: Ключ, определяющий название сценария.
- `brand`: Строка, определяющая бренд продукта (в данном случае `LENOVO`).
- `url`: Строка, содержащая URL-адрес, с которого необходимо собирать данные.
- `checkbox`: Булево значение, указывающее, нужно ли использовать чекбокс (в данном случае всегда `false`).
- `active`: Булево значение, указывающее, активен ли сценарий (в данном случае всегда `true`).
- `condition`: Строка, указывающая состояние товара (в данном случае всегда `new`).
- `presta_categories`: Объект, содержащий информацию о категориях PrestaShop.
  - `template`: Объект, содержащий шаблон категорий.
    - `TEMPLATE_NAME`: Ключ, определяющий имя шаблона (в данном случае `lenovo`).
    - `PRESTA_CATEGORY_NAME`: Строка, содержащая имя категории PrestaShop.

## Сценарии

### `LENOVO 21 - 22`

**Описание**:
Сценарий для сбора данных о мониторах Lenovo размером 21-22 дюйма.

**Параметры**:
- `brand` (str): `LENOVO`
- `url` (str): `https://www.morlevi.co.il/Cat/8?p_350=1805&p_315=6&sort=datafloat2%2Cprice&keyword=`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `new`
- `presta_categories` (dict):
  - `template` (dict):
    - `lenovo` (str): `PC MONITORS 21 - 22`

### `LENOVO 23 - 24`

**Описание**:
Сценарий для сбора данных о мониторах Lenovo размером 23-24 дюйма.

**Параметры**:
- `brand` (str): `LENOVO`
- `url` (str): `https://www.morlevi.co.il/Cat/8?p_350=1806&p_350=1807&p_315=6&sort=datafloat2%2Cprice&keyword=`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `new`
- `presta_categories` (dict):
  - `template` (dict):
    - `lenovo` (str): `PC MONITORS 23 - 24`

### `LENOVO 26 - 28`

**Описание**:
Сценарий для сбора данных о мониторах Lenovo размером 26-28 дюймов.

**Параметры**:
- `brand` (str): `LENOVO`
- `url` (str): `https://www.morlevi.co.il/Cat/8?p_350=1808&p_315=6&sort=datafloat2%2Cprice&keyword=`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `new`
- `presta_categories` (dict):
  - `template` (dict):
    - `lenovo` (str): `PC MONITORS 26 - 28`

### `LENOVO 27 - 29`

**Описание**:
Сценарий для сбора данных о мониторах Lenovo размером 27-29 дюймов.

**Параметры**:
- `brand` (str): `LENOVO`
- `url` (str): `https://www.morlevi.co.il/Cat/8?p_350=1808&p_315=6&sort=datafloat2%2Cprice&keyword=`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `new`
- `presta_categories` (dict):
  - `template` (dict):
    - `lenovo` (str): `PC MONITORS 27 - 29`