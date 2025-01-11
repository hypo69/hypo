# Документация для `morlevi_categories_psu_antec.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [ANTEC 450W](#antec-450w)
    - [ANTEC 500W](#antec-500w)
    - [ANTEC 550W](#antec-550w)
    - [ANTEC 600W](#antec-600w)
    - [ANTEC 650W](#antec-650w)
    - [ANTEC 700W](#antec-700w)
    - [ANTEC 750W](#antec-750w)

## Обзор

Файл `morlevi_categories_psu_antec.json` содержит конфигурационные данные для сценариев парсинга блоков питания (PSU) бренда ANTEC с сайта morlevi.co.il. Каждый сценарий определяет параметры для конкретной модели PSU, включая URL, состояние, и связанные категории PrestaShop.

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "SCENARIO_NAME": {
      "brand": "BRAND_NAME",
      "name": "MODEL_NAME",
      "url": "URL",
      "checkbox": false,
      "active": true,
      "condition":"CONDITION",
      "presta_categories": "CATEGORIES"
    },
    ...
  }
}
```

Где:

-   `scenarios`: Объект, содержащий сценарии парсинга.
-   `SCENARIO_NAME`: Название сценария (например, "ANTEC 450W").
-   `brand`: Бренд блока питания (например, "ANTEC").
-   `name`: Модель блока питания (например, "450W").
-   `url`: URL страницы продукта на сайте morlevi.co.il.
-   `checkbox`: Логический флаг, определяющий состояние чекбокса (всегда `false`).
-   `active`: Логический флаг, указывающий, активен ли сценарий (всегда `true`).
-   `condition`: Состояние продукта (всегда `new`).
-   `presta_categories`: Строка, содержащая ID категорий PrestaShop, связанных с продуктом.

## Сценарии

### ANTEC 450W

**Описание**: Конфигурация для парсинга блока питания ANTEC 450W.

-   **Бренд**: `ANTEC`
-   **Модель**: `450W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=634&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-    **Состояние**: `new`
-   **Категории PrestaShop**: `158,511,188,577`

### ANTEC 500W

**Описание**: Конфигурация для парсинга блока питания ANTEC 500W.

-   **Бренд**: `ANTEC`
-   **Модель**: `500W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=635&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-    **Состояние**: `new`
-   **Категории PrestaShop**: `158,511,189,577`

### ANTEC 550W

**Описание**: Конфигурация для парсинга блока питания ANTEC 550W.

-   **Бренд**: `ANTEC`
-   **Модель**: `550W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=678&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-    **Состояние**: `new`
-   **Категории PrestaShop**: `151,158,511,190,577`

### ANTEC 600W

**Описание**: Конфигурация для парсинга блока питания ANTEC 600W.

-   **Бренд**: `ANTEC`
-   **Модель**: `600W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=636&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-    **Состояние**: `new`
-   **Категории PrestaShop**: `151,158,511,191,577`

### ANTEC 650W

**Описание**: Конфигурация для парсинга блока питания ANTEC 650W.

-   **Бренд**: `ANTEC`
-   **Модель**: `650W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=637&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-    **Состояние**: `new`
-   **Категории PrestaShop**: `151,158,511,192,577`

### ANTEC 700W

**Описание**: Конфигурация для парсинга блока питания ANTEC 700W.

-   **Бренд**: `ANTEC`
-   **Модель**: `700W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=669&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-   **Состояние**: `new`
-   **Категории PrestaShop**: `151,158,511,193,577`

### ANTEC 750W

**Описание**: Конфигурация для парсинга блока питания ANTEC 750W.

-   **Бренд**: `ANTEC`
-   **Модель**: `750W`
-   **URL**: `https://www.morlevi.co.il/Cat/66?p_145=670&sort=datafloat2%2Cprice&keyword=`
-   **Чекбокс**: `false`
-   **Активен**: `true`
-   **Состояние**: `new`
-   **Категории PrestaShop**: `151,158,511,194,577`