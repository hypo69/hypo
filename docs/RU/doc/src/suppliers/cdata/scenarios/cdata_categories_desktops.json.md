# Документация для `cdata_categories_desktops.json`

## Обзор

Файл `cdata_categories_desktops.json` содержит JSON-объект со сценариями для десктопов разных брендов (HP, ASUS, DELL) и с разными типами процессоров (I3, I5, I7, I9, AMD, Pentium). Каждый сценарий содержит информацию о бренде, URL-адресе для поиска, статусе чекбокса, активности, состоянии товара и связанных категориях PrestaShop.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
3.  [Описание полей](#описание-полей)
    *   [scenarios](#scenarios)
    *   [scenario_name](#scenario_name)
        *   [brand](#brand)
        *   [url](#url)
        *   [checkbox](#checkbox)
        *   [active](#active)
        *   [condition](#condition)
        *   [presta_categories](#presta_categories)

## Структура файла

Файл представляет собой JSON-объект со структурой:

```json
{
  "scenarios": {
    "SCENARIO_NAME_1": {
      "brand": "BRAND_NAME",
      "url": "URL_ADDRESS",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "CONDITION_TYPE",
      "presta_categories": "CATEGORIES_STRING"
    },
        "SCENARIO_NAME_2": {
      "brand": "BRAND_NAME",
      "url": "URL_ADDRESS",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "CONDITION_TYPE",
      "presta_categories": "CATEGORIES_STRING"
    },
        "SCENARIO_NAME_N": {
      "brand": "BRAND_NAME",
      "url": "URL_ADDRESS",
      "checkbox": BOOLEAN,
      "active": BOOLEAN,
      "condition": "CONDITION_TYPE",
      "presta_categories": "CATEGORIES_STRING"
    }
  }
}
```

## Описание полей

### `scenarios`
- **Описание**:  Объект, содержащий набор сценариев для десктопов. Каждый ключ - это название сценария, а значение - объект с деталями сценария.

### `scenario_name`

Каждый сценарий имеет следующие поля:

#### `brand`
- **Описание**: Название бренда десктопа (например, HP, ASUS, DELL).
- **Тип**: `строка`

#### `url`
- **Описание**: URL-адрес для поиска десктопов на сайте поставщика.
- **Тип**: `строка`

#### `checkbox`
- **Описание**: Статус чекбокса (используется или нет).
- **Тип**: `boolean`

#### `active`
- **Описание**: Статус активности сценария.
- **Тип**: `boolean`

#### `condition`
- **Описание**: Состояние товара (например, "new").
- **Тип**: `строка`

#### `presta_categories`
- **Описание**: Список ID категорий PrestaShop, к которым относится товар.
- **Тип**: `строка`, разделенные запятыми.