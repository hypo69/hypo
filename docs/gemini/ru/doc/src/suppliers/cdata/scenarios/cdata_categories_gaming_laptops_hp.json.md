# Документация для `cdata_categories_gaming_laptops_hp.json`

## Обзор

Файл `cdata_categories_gaming_laptops_hp.json` содержит JSON-структуру, описывающую сценарии для категорий игровых ноутбуков HP. Каждый сценарий определяет характеристики конкретной модели, такие как бренд, URL, состояние чекбокса, статус активности, состояние и категории PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание сценариев](#описание-сценариев)
    - [`HP GAMING 14 I5`](#hp-gaming-14-i5)
    - [`HP GAMING 14 I7`](#hp-gaming-14-i7)
    - [`HP GAMING 14 I9`](#hp-gaming-14-i9)
    - [`HP GAMING 14 AMD`](#hp-gaming-14-amd)
    - [`HP GAMING 15 I5`](#hp-gaming-15-i5)
    - [`HP GAMING 15 I7`](#hp-gaming-15-i7)
    - [`HP GAMING 15 I9`](#hp-gaming-15-i9)
    - [`HP GAMING 15 AMD`](#hp-gaming-15-amd)
    - [`HP GAMING 17 I5`](#hp-gaming-17-i5)
    - [`HP GAMING 17 I7`](#hp-gaming-17-i7)
    - [`HP GAMING 17 I9`](#hp-gaming-17-i9)
    - [`HP GAMING 17 AMD`](#hp-gaming-17-amd)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "scenario_name": {
      "brand": "string",
      "url": "string",
      "checkbox": boolean,
      "active": boolean,
      "condition": "string",
      "presta_categories": "string"
    }
  }
}
```

Где:

- `"scenarios"`: Объект, содержащий все сценарии.
- `"scenario_name"`: Ключ, представляющий имя сценария (например, `"HP GAMING 14 I5"`).
- `"brand"`: (string) Бренд ноутбука (в данном случае `"HP"`).
- `"url"`: (string) URL, связанный со сценарием (может быть строкой-заполнителем или реальным URL).
- `"checkbox"`: (boolean) Состояние чекбокса (всегда `false`).
- `"active"`: (boolean) Статус активности сценария (всегда `true`).
- `"condition"`: (string) Состояние продукта (всегда `"new"`).
- `"presta_categories"`: (string) Строка, представляющая категории PrestaShop, разделенные запятыми.

## Описание сценариев

### `HP GAMING 14 I5`

**Описание**: Сценарий для игрового ноутбука HP 14 дюймов с процессором Intel Core i5.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"---------------------------HP GAMING 14 I5-----------------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,101,10,5,462"`.

### `HP GAMING 14 I7`

**Описание**: Сценарий для игрового ноутбука HP 14 дюймов с процессором Intel Core i7.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"------------------------------HP GAMING 14 I7---------------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,101,10,6,463"`.

### `HP GAMING 14 I9`

**Описание**: Сценарий для игрового ноутбука HP 14 дюймов с процессором Intel Core i9.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"--------------------------------HP GAMING 14 I9------------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,101,10,7,464"`.

### `HP GAMING 14 AMD`

**Описание**: Сценарий для игрового ноутбука HP 14 дюймов с процессором AMD.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"---------------------------------HP GAMING 14 AMD-----------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,101,10,234,465"`.

### `HP GAMING 15 I5`

**Описание**: Сценарий для игрового ноутбука HP 15 дюймов с процессором Intel Core i5.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4634!-#!225!#-!4663!##!6406&manFilters=2"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,102,11,5,469"`.

### `HP GAMING 15 I7`

**Описание**: Сценарий для игрового ноутбука HP 15 дюймов с процессором Intel Core i7.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4635!-#!225!#-!4663!##!6406&manFilters=2"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,102,11,6,470"`.

### `HP GAMING 15 I9`

**Описание**: Сценарий для игрового ноутбука HP 15 дюймов с процессором Intel Core i9.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"--------------------------------HP GAMING 15 I9------------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,102,11,7,471"`.

### `HP GAMING 15 AMD`

**Описание**: Сценарий для игрового ноутбука HP 15 дюймов с процессором AMD.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"-------------------------HP GAMING 15 AMD-------------------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,102,,11,234,472"`.

### `HP GAMING 17 I5`

**Описание**: Сценарий для игрового ноутбука HP 17 дюймов с процессором Intel Core i5.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"---------------------------------HP GAMING 17 I5-----------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,103,12,5,476"`.

### `HP GAMING 17 I7`

**Описание**: Сценарий для игрового ноутбука HP 17 дюймов с процессором Intel Core i7.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"------------------------------------HP GAMING 17 I7---------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,103,12,6,477"`.

### `HP GAMING 17 I9`

**Описание**: Сценарий для игрового ноутбука HP 17 дюймов с процессором Intel Core i9.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"-------------------------------------HP GAMING 17 I9-------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,103,12,7,478"`.

### `HP GAMING 17 AMD`

**Описание**: Сценарий для игрового ноутбука HP 17 дюймов с процессором AMD.

**Параметры**:

- `"brand"`: `"HP"`.
- `"url"`: `"------------------------------------HP GAMING 17 AMD--------------------------"`.
- `"checkbox"`: `false`.
- `"active"`: `true`.
- `"condition"`: `"new"`.
- `"presta_categories"`: `"3,49,50,52,103,12,234,479"`.