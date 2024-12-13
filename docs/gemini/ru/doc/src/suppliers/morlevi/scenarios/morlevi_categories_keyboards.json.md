# Документация `morlevi_categories_keyboards.json`

## Обзор

Файл `morlevi_categories_keyboards.json` содержит конфигурацию сценариев для категорий клавиатур и мышей, используемых поставщиком Morlevi. Каждый сценарий определяет бренд, шаблон, URL, флаг активации, состояние продукта и соответствующие категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
  - [Сценарии](#сценарии)
  - [Пример сценария](#пример-сценария)

## Структура файла

### Сценарии

Файл представляет собой JSON-объект с ключом `"scenarios"`, значением которого является объект, содержащий сценарии для различных категорий клавиатур и мышей. Каждый ключ в объекте `"scenarios"` представляет собой уникальный сценарий (например, `"COOLER MASTER USB KEYBOARD"`).

### Пример сценария

Каждый сценарий имеет следующие атрибуты:

-   `brand` (str): Бренд продукта (например, `"COOLER MASTER"`).
-   `template` (str): Шаблон продукта (например, `"COOLER MASTER KEYBOARD"`).
-   `url` (str): URL-адрес, связанный с продуктом (например, `"https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword="`).
-   `checkbox` (bool): Флаг, указывающий, что некий флажок для сценария имеет состояние `false`.
-   `active` (bool): Флаг, указывающий, активен ли сценарий (например, `true`).
-   `condition` (str): Состояние продукта (например, `"new"`).
-   `presta_categories` (str | dict): Категории PrestaShop, связанные со сценарием. Может быть строкой с ID категорий, разделенных запятыми (например, `"203,204,315"`) или объектом, где ключ template, значение категории PrestaShop.

#### Пример объекта в `scenarios`:

```json
    "COOLER MASTER USB KEYBOARD": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER KEYBOARD",
      "url": "https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": { "template": { "computer accessories": "WIRED KB" } }
    }
```

#### Пример объекта в `scenarios`:

```json
   "GENIUS USB KEYBOARD": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER USB KEYBOARD",
      "url": "https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,204,315"
    }
```

Данный файл предназначен для конфигурации и управления различными сценариями импорта данных для поставщика Morlevi.