# Документация для `morlevi_categories_monitors_dell.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев парсинга категорий мониторов бренда DELL с сайта morlevi.co.il. Каждый сценарий определяет параметры для определенной группы размеров мониторов, включая URL-адрес, бренд, состояние и связанные категории PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
   - [DELL 22](#dell-22)
   - [DELL 24-25](#dell-24-25)
   - [DELL 27-29](#dell-27-29)
   - [DELL 32](#dell-32)
   - [DELL 34](#dell-34)
   - [DELL 49](#dell-49)

## Структура JSON

JSON файл имеет следующую структуру:

```json
{
  "scenarios": {
    "scenario_name": {
      "brand": "brand_name",
      "url": "url_string",
      "checkbox": boolean,
      "active": boolean,
      "condition": "condition_string",
      "presta_categories": "comma_separated_categories"
    }
  }
}
```

Где:

- `"scenarios"`: Объект, содержащий сценарии.
- `"scenario_name"`: Уникальный идентификатор сценария (например, "DELL 22").
- `"brand"`: Название бренда (например, "DELL").
- `"url"`: URL-адрес для парсинга.
- `"checkbox"`: Логическое значение, указывающее состояние чекбокса (используется для UI).
- `"active"`: Логическое значение, указывающее, активен ли сценарий.
- `"condition"`: Состояние товара (например, "new").
- `"presta_categories"`: Строка с категориями PrestaShop, разделёнными запятыми.

## Сценарии

### DELL 22

**Описание**: Сценарий для мониторов DELL размером 22 дюйма.

**Параметры**:

-   `brand` (str): "DELL".
-   `url` (str): "--------------------------------- DELL 22 -----------------------------------------------------------------".
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): "new".
-  `presta_categories` (str): "127,128,528".

### DELL 24-25

**Описание**: Сценарий для мониторов DELL размером 24-25 дюймов.

**Параметры**:

-   `brand` (str): "DELL".
-   `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1807&p_75=483&p_75=292&p_75=293&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): "new".
- `presta_categories` (str): "127,129,528".

### DELL 27-29

**Описание**: Сценарий для мониторов DELL размером 27-29 дюймов.

**Параметры**:

-   `brand` (str): "DELL".
-   `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1808&p_75=297&sort=datafloat2%2Cprice&keyword=".
-  `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): "new".
-   `presta_categories` (str): "127,130,528".

### DELL 32

**Описание**: Сценарий для мониторов DELL размером 32 дюйма.

**Параметры**:

-   `brand` (str): "DELL".
-   `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1809&p_75=298&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): "new".
-   `presta_categories` (str): "127,131,528".

### DELL 34

**Описание**: Сценарий для мониторов DELL размером 34 дюйма.

**Параметры**:

-   `brand` (str): "DELL".
-   `url` (str): " --------------------------  DELL 34 -----------------------------------".
-   `checkbox` (bool): `false`.
-  `active` (bool): `true`.
-   `condition` (str): "new".
-   `presta_categories` (str): "127,132,528".

### DELL 49

**Описание**: Сценарий для мониторов DELL размером 49 дюймов.

**Параметры**:

-  `brand` (str): "DELL".
-   `url` (str): "-----------------------------  DELL 49 ---------------------------------".
-   `checkbox` (bool): `false`.
-  `active` (bool): `true`.
-   `condition` (str): "new".
-  `presta_categories` (str): "127,133,528".