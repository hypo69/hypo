# Документация для `morlevi_categories_mb_gigabyte.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев обработки материнских плат Gigabyte, получаемых с сайта Morlevi. Он определяет категории товаров, URL-адреса, условия и настройки для интеграции с PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [GIGABYTE INTEL LGA1700 12 Gen Z690](#gigabyte-intel-lga1700-12-gen-z690)
    - [GIGABYTE INTEL LGA1700 12 Gen B660](#gigabyte-intel-lga1700-12-gen-b660)
    - [GIGABYTE INTEL LGA1700 12 H610](#gigabyte-intel-lga1700-12-h610)
    - [GIGABYTE INTEL LGA1200 H510](#gigabyte-intel-lga1200-h510)
    - [GIGABYTE INTEL LGA1200 B560](#gigabyte-intel-lga1200-b560)
    - [GIGABYTE INTEL LGA1200 Z590](#gigabyte-intel-lga1200-z590)
    - [GIGABYTE INTEL LGA1200 H410 GEN10](#gigabyte-intel-lga1200-h410-gen10)
    - [GIGABYTE INTEL LGA1200 H470 GEN10](#gigabyte-intel-lga1200-h470-gen10)
    - [GIGABYTE INTEL LGA2066 X299](#gigabyte-intel-lga2066-x299)
    - [GIGABYTE AMD AM4+  A520](#gigabyte-amd-am4-a520)
    - [GIGABYTE AMD AM4+  B450](#gigabyte-amd-am4-b450)
    - [GIGABYTE AMD AM4+  B550](#gigabyte-amd-am4-b550)
    - [GIGABYTE AMD AM4+  X570/X570S](#gigabyte-amd-am4-x570x570s)
    - [GIGABYTE AMD Threadripper   TRX40](#gigabyte-amd-threadripper-trx40)
    - [GIGABYTE AMD Threadripper   X399](#gigabyte-amd-threadripper-x399)
    - [GIGABYTE AMD Threadripper   WRX80](#gigabyte-amd-threadripper-wrx80)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "scenario_name_1": {
      "brand": "string",
      "url": "string",
      "checkbox": boolean,
      "active": boolean,
      "condition":"string",
       "presta_categories": {
        "template": { "gigabyte": "string" }
      },
      "price_rule": number
    },
    "scenario_name_2": {
        ...
    },
       ...
  }
}
```

Где:

- `"scenarios"`:  Объект, содержащий все сценарии.
- `"scenario_name_1"`: Название конкретного сценария (ключ объекта).
  - `"brand"`: Бренд товара.
  - `"url"`: URL-адрес категории товаров на сайте Morlevi.
  - `"checkbox"`:  Логический флаг, связанный с пользовательским интерфейсом (не влияет на логику обработки).
  - `"active"`:  Логический флаг, указывающий, активен ли данный сценарий.
  - `"condition"`: Условие товара (в данном случае "new").
  - `"presta_categories"`: Объект, содержащий данные для сопоставления с категориями PrestaShop.
  - `"template"`: Объект, содержащий соответствия для шаблонов категорий.
      - `"gigabyte"`: Значение для соответствия категории Gigabyte.
  - `"price_rule"`: Правило ценообразования.

## Сценарии

### `GIGABYTE INTEL LGA1700 12 Gen Z690`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel Z690 для процессоров LGA1700 12-го поколения.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/378"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel Z690"}`
- **`price_rule`**: `1`

### `GIGABYTE INTEL LGA1700 12 Gen B660`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel B660 для процессоров LGA1700 12-го поколения.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/388"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel B660"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA1700 12 H610`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel H610 для процессоров LGA1700 12-го поколения.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/389"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel H610"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA1200 H510`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel H510 для процессоров LGA1200.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/364"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel H610"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA1200 B560`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel B560 для процессоров LGA1200.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/365"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel B560"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA1200 Z590`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel Z590 для процессоров LGA1200.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/360"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel B560"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA1200 H410 GEN10`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel H410 для процессоров LGA1200 10-го поколения.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/343"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel H410"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA1200 H470 GEN10`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel H470 для процессоров LGA1200 10-го поколения.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/343"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel H470"}`
- **`price_rule`**: не указан

### `GIGABYTE INTEL LGA2066 X299`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете Intel X299 для процессоров LGA2066.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/28?p_95=411"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "Intel X299"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD AM4+  A520`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD A520 для процессоров AM4+.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/350"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD A520"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD AM4+  B450`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD B450 для процессоров AM4+.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/311"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD B450"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD AM4+  B550`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD B550 для процессоров AM4+.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/340"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD B550"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD AM4+  X570/X570S`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD X570/X570S для процессоров AM4+.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/22?p_95=4022&p_95=3225"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD X570"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD Threadripper   TRX40`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD TRX40 для процессоров Threadripper.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/349"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD TRX40"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD Threadripper   X399`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD X399 для процессоров Threadripper.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/353"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD X399"}`
- **`price_rule`**: не указан

### `GIGABYTE AMD Threadripper   WRX80`

**Описание**: Сценарий для материнских плат GIGABYTE на чипсете AMD WRX80 для процессоров Threadripper.
- **`brand`**: "GIGABYTE"
- **`url`**: "https://www.morlevi.co.il/Cat/366"
- **`checkbox`**: `false`
- **`active`**: `true`
- **`condition`**: `"new"`
- **`presta_categories`**:
    - **`template`**: `{"gigabyte": "AMD WRX80"}`
- **`price_rule`**: не указан