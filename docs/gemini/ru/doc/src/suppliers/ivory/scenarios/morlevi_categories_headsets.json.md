# Документация для `morlevi_categories_headsets.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [HEADSET_LOGITECH](#headset_logitech)
    - [HEADSET_MICROSOFT](#headset_microsoft)
    - [HEADSET_ZALMAN](#headset_zalman)
    - [HEADSET_CORSAIR](#headset_corsair)
    - [HEADSET_COOLER MASTER](#headset_cooler-master)

## Обзор

Файл `morlevi_categories_headsets.json` содержит конфигурацию для различных сценариев, связанных с гарнитурами (headsets) от разных производителей на сайте morlevi.co.il. Каждый сценарий определяет параметры для сбора данных о гарнитурах конкретного бренда.

## Структура JSON

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "template": "TEMPLATE_NAME",
      "url": "URL_FOR_CATEGORY",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
           "BRAND_NAME_LOWERCASE": "PRESTA_CATEGORY_NAME"
         }
      }
    }
  }
}
```

где:
- `"scenarios"`: Объект, содержащий все сценарии.
- `SCENARIO_NAME`: Название сценария (например, "HEADSET_LOGITECH").
- `"brand"`: Название бренда гарнитуры.
- `"template"`: Шаблон для использования.
- `"url"`: URL страницы с товарами на сайте morlevi.co.il.
- `"checkbox"`: Логический флаг для чекбокса, всегда `false`.
- `"active"`: Логический флаг, указывающий, активен ли сценарий, всегда `true`.
- `"condition"`: Состояние товара, всегда `"new"`.
- `"presta_categories"`: Объект, содержащий соответствие шаблона и категории PrestaShop.
    - `"template"`: Объект, содержащий соответствие бренда в нижнем регистре и категории PrestaShop.
      - `BRAND_NAME_LOWERCASE`: Название бренда в нижнем регистре.
      - `PRESTA_CATEGORY_NAME`: Название категории PrestaShop.

## Сценарии

### `HEADSET_LOGITECH`

**Описание**: Сценарий для гарнитур бренда Logitech.

**Параметры**:
- `"brand"`: `"LOGITECH"`.
- `"template"`: `"HEADSET_LOGITECH"`.
- `"url"`: `"https://www.morlevi.co.il/Cat/162?p_315=29&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`:
  ```json
  {
    "template": {
      "logitech": "HEADPHONES"
    }
  }
  ```

### `HEADSET_MICROSOFT`

**Описание**: Сценарий для гарнитур бренда Microsoft.

**Параметры**:
- `"brand"`: `"MICROSOFT"`.
- `"template"`: `"HEADSET_MICROSOFT"`.
- `"url"`: `"https://www.morlevi.co.il/Cat/162?p_315=42&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`:
  ```json
  {
    "template": {
      "microsoft": "HEADPHONES"
    }
  }
  ```

### `HEADSET_ZALMAN`

**Описание**: Сценарий для гарнитур бренда Zalman.

**Параметры**:
- `"brand"`: `"ZALMAN"`.
- `"template"`: `"HEADSET_ZALMAN"`.
- `"url"`: `"https://www.morlevi.co.il/Cat/162?p_315=34&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`:
  ```json
  {
    "template": {
      "zalman": "HEADPHONES"
    }
  }
  ```

### `HEADSET_CORSAIR`

**Описание**: Сценарий для гарнитур бренда Corsair.

**Параметры**:
- `"brand"`: `"CORSAIR"`.
- `"template"`: `"HEADSET_CORSAIR"`.
- `"url"`: `"https://www.morlevi.co.il/Cat/162?p_315=20&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`:
  ```json
  {
    "template": {
      "corsair": "HEADPHONES"
    }
  }
  ```

### `HEADSET_COOLER MASTER`

**Описание**: Сценарий для гарнитур бренда Cooler Master.

**Параметры**:
- `"brand"`: `"COOLER MASTER"`.
- `"template"`: `"HEADSET_COOLER MASTER"`.
- `"url"`: `"https://www.morlevi.co.il/Cat/162?p_315=74&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`:
  ```json
  {
    "template": {
      "cooler master": "HEADPHONES"
    }
  }
  ```