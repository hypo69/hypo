# Документация для `ksp_categories_monitors_lenovo.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)
4. [Примеры сценариев](#примеры-сценариев)

## Обзор

Этот JSON-файл содержит конфигурационные данные для мониторинга категорий товаров Lenovo на сайте KSP. Каждый сценарий представляет собой набор параметров для определения категории товара, включая URL страницы, бренд и соответствие категориям PrestaShop.

## Структура JSON

Файл содержит корневой объект с ключом `"scenarios"`, значением которого является объект, где каждый ключ представляет собой название сценария, а значение - объект с настройками для этого сценария.

```json
{
  "scenarios": {
    "Название сценария 1": {
      "brand": "Бренд",
      "url": "URL страницы категории",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": {
        "template": { "lenovo": "Категория PrestaShop" }
      }
    },
     "Название сценария 2": {
      "brand": "Бренд",
      "url": "URL страницы категории",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": {
        "template": { "lenovo": "Категория PrestaShop" }
      }
    }
    // ... другие сценарии ...
  }
}
```

## Описание полей

### `scenarios`

-   **Описание**: Объект, содержащий все сценарии мониторинга.
-   **Тип**: `Object`
-   **Ключ**: `string` (название сценария)
-   **Значение**: `Object` (параметры сценария)

### Параметры сценария

Каждый сценарий (объект внутри `scenarios`) содержит следующие поля:

-   `brand`
    -   **Описание**: Бренд товара, в данном случае - "Lenovo".
    -   **Тип**: `string`
-   `url`
    -   **Описание**: URL страницы категории товара на сайте KSP.
    -   **Тип**: `string`
-   `checkbox`
    -   **Описание**: Флаг, указывающий, используется ли чекбокс (не используется, всегда `false`).
    -   **Тип**: `boolean`
-   `active`
    -   **Описание**: Флаг, указывающий, активен ли сценарий (`true` - активен, `false` - не активен).
    -   **Тип**: `boolean`
-    `condition`
    -   **Описание**: Состояние товара, в данном случае "new".
    -   **Тип**: `string`
-   `presta_categories`
    -   **Описание**: Объект, содержащий соответствие категорий для PrestaShop.
    -   **Тип**: `Object`
    -   `template`
        -   **Описание**: Объект, содержащий шаблон соответствия категорий.
        -   **Тип**: `Object`
        -    **Ключ**: `"lenovo"`
             -    **Описание**: Ключ для поиска в шаблоне категорий.
             -    **Тип**: `string`
        -   **Значение**: Категория PrestaShop для данного сценария.
            -   **Тип**: `string`

## Примеры сценариев

### "Lenovo Monitor L Series 23,8"

```json
"Lenovo Monitor L Series 23,8": {
    "brand": "Lenovo",
    "url": "https://ksp.co.il/web/cat/159..230..38350..1649",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": {
        "template": { "lenovo": "PC MONITORS 22 - 24" }
    }
}
```

Этот сценарий предназначен для мониторинга мониторов Lenovo L Series с диагональю 23.8 дюйма. Он указывает на URL категории, бренд "Lenovo" и соответствует категории "PC MONITORS 22 - 24" в PrestaShop.

### "Lenovo Monitor G Series 34"

```json
"Lenovo Monitor G Series 34": {
    "brand": "Lenovo",
    "url": "https://ksp.co.il/web/cat/230..159..38352..2129",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": {
        "template": { "lenovo": "PC MONITORS 34 - 38" }
    }
}
```

Этот сценарий отслеживает мониторы Lenovo G Series с диагональю 34 дюйма.  Он соответствует категории "PC MONITORS 34 - 38" в PrestaShop.

### Другие сценарии

Аналогично, файл содержит сценарии для различных серий и размеров мониторов Lenovo, каждый из которых имеет свой URL и соответствие категориям PrestaShop.