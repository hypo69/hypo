# Документация для `morlevi_categories_headsets.json`

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
3.  [Сценарии](#сценарии)
    - [HEADSET_LOGITECH](#headset_logitech)
    - [HEADSET_MICROSOFT](#headset_microsoft)
    - [HEADSET_ZALMAN](#headset_zalman)
    - [HEADSET_CORSAIR](#headset_corsair)
    - [HEADSET_COOLER MASTER](#headset_cooler-master)

## Обзор

Файл `morlevi_categories_headsets.json` содержит JSON-структуру, определяющую сценарии для парсинга категорий наушников от поставщика Morlevi. Каждый сценарий включает информацию о бренде, шаблоне, URL, настройках активности, состояния товара и соответствиях с категориями PrestaShop.

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "template": "TEMPLATE_NAME",
      "url": "URL_TO_PARSE",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "template_key": "PRESTA_CATEGORY"
        }
      }
    }
  }
}
```

## Сценарии

### `HEADSET_LOGITECH`

**Описание**:
Сценарий для парсинга наушников бренда LOGITECH.

**Параметры**:
- `brand` (str): "LOGITECH".
- `template` (str): "HEADSET_LOGITECH".
- `url` (str): "https://www.morlevi.co.il/Cat/162?p_315=29&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (dict): Словарь с соответствиями категорий PrestaShop, где "logitech" соответствует "HEADPHONES".

**Пример**:
```json
    "HEADSET_LOGITECH": {
      "brand": "LOGITECH",
      "template": "HEADSET_LOGITECH",
      "url": "https://www.morlevi.co.il/Cat/162?p_315=29&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": {
          "logitech": "HEADPHONES"
        }
      }
    },
```

### `HEADSET_MICROSOFT`

**Описание**:
Сценарий для парсинга наушников бренда MICROSOFT.

**Параметры**:
- `brand` (str): "MICROSOFT".
- `template` (str): "HEADSET_MICROSOFT".
- `url` (str): "https://www.morlevi.co.il/Cat/162?p_315=42&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (dict): Словарь с соответствиями категорий PrestaShop, где "microsoft" соответствует "HEADPHONES".

**Пример**:
```json
    "HEADSET_MICROSOFT": {
      "brand": "MICROSOFT",
      "template": "HEADSET_MICROSOFT",
      "url": "https://www.morlevi.co.il/Cat/162?p_315=42&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": {
          "microsoft": "HEADPHONES"
        }
      }
    },
```

### `HEADSET_ZALMAN`

**Описание**:
Сценарий для парсинга наушников бренда ZALMAN.

**Параметры**:
- `brand` (str): "ZALMAN".
- `template` (str): "HEADSET_ZALMAN".
- `url` (str): "https://www.morlevi.co.il/Cat/162?p_315=34&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (dict): Словарь с соответствиями категорий PrestaShop, где "zalman" соответствует "HEADPHONES".

**Пример**:
```json
    "HEADSET_ZALMAN": {
        "brand": "ZALMAN",
        "template": "HEADSET_ZALMAN",
        "url": "https://www.morlevi.co.il/Cat/162?p_315=34&sort=datafloat2%2Cprice&keyword=",
        "checkbox": false,
        "active": true,
        "condition":"new",
        "presta_categories": {
          "template": {
            "zalman": "HEADPHONES"
           }
        }
      },
```

### `HEADSET_CORSAIR`

**Описание**:
Сценарий для парсинга наушников бренда CORSAIR.

**Параметры**:
- `brand` (str): "CORSAIR".
- `template` (str): "HEADSET_CORSAIR".
- `url` (str): "https://www.morlevi.co.il/Cat/162?p_315=20&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (dict): Словарь с соответствиями категорий PrestaShop, где "corsair" соответствует "HEADPHONES".

**Пример**:
```json
    "HEADSET_CORSAIR": {
      "brand": "CORSAIR",
      "template": "HEADSET_CORSAIR",
      "url": "https://www.morlevi.co.il/Cat/162?p_315=20&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": {
          "corsair": "HEADPHONES"
          }
        }
      },
```

### `HEADSET_COOLER MASTER`

**Описание**:
Сценарий для парсинга наушников бренда COOLER MASTER.

**Параметры**:
- `brand` (str): "COOLER MASTER".
- `template` (str): "HEADSET_COOLER MASTER".
- `url` (str): "https://www.morlevi.co.il/Cat/162?p_315=74&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (dict): Словарь с соответствиями категорий PrestaShop, где "cooler master" соответствует "HEADPHONES".

**Пример**:
```json
    "HEADSET_COOLER MASTER": {
      "brand": "COOLER MASTER",
      "template": "HEADSET_COOLER MASTER",
      "url": "https://www.morlevi.co.il/Cat/162?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": {
          "cooler master": "HEADPHONES"
        }
      }
    }
```