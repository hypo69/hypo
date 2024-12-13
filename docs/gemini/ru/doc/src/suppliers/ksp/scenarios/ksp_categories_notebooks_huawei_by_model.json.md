# Документация для `ksp_categories_notebooks_huawei_by_model.json`

## Обзор

Данный файл содержит JSON-структуру, описывающую сценарии для сбора данных о ноутбуках Huawei по моделям с сайта KSP. Каждый сценарий определяет конкретную модель ноутбука, её бренд, URL для сбора данных, и связанные категории PrestaShop.

## Оглавление
- [Структура файла](#структура-файла)
- [Раздел `scenarios`](#раздел-scenarios)
    - [Сценарий `Huawei MateBook 14`](#сценарий-huawei-matebook-14)
    - [Сценарий `Huawei Matebook D14`](#сценарий-huawei-matebook-d14)

## Структура файла

Файл представляет собой JSON-объект со следующим форматом:

```json
{
  "scenarios": {
    "Модель ноутбука 1": {
        "brand": "Бренд",
        "url": "URL для сбора данных",
        "checkbox": false,
        "active": true,
         "condition":"new",
        "presta_categories": {
            "id категории 1": "Название категории 1",
            "id категории 2": "Название категории 2",
             "id категории 3": "Название категории 3",
            "id категории 4": "Название категории 4"

        }
    },
    "Модель ноутбука 2": {
        "brand": "Бренд",
        "url": "URL для сбора данных",
        "checkbox": false,
        "active": true,
         "condition":"new",
         "presta_categories": {
            "id категории 1": "Название категории 1",
            "id категории 2": "Название категории 2",
             "id категории 3": "Название категории 3",
            "id категории 4": "Название категории 4"

        }
    },
    ...
  }
}
```

## Раздел `scenarios`

Данный раздел содержит список сценариев, каждый из которых описывает определённую модель ноутбука Huawei. Каждый сценарий представляет собой объект со следующими полями:

- `brand` (str): Бренд ноутбука (например, "HUAWEI").
- `url` (str): URL-адрес для сбора данных о товаре с сайта KSP.
- `checkbox` (bool): Логическое значение, указывающее, используется ли чекбокс для этого сценария. Всегда `false`.
- `active` (bool): Логическое значение, указывающее, активен ли сценарий. Всегда `true`.
- `condition` (str): Условие товара, всегда `"new"`.
- `presta_categories` (dict): Словарь, связывающий идентификаторы категорий PrestaShop с их названиями.

### Сценарий `Huawei MateBook 14`

#### Описание

Сценарий для сбора данных о ноутбуке Huawei MateBook 14.

#### Поля

-   `brand`: `"HUAWEI"`
-   `url`: `"https://ksp.co.il/web/cat/268..271..583..31024"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    ```json
     {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"

      }
    ```

### Сценарий `Huawei Matebook D14`

#### Описание

Сценарий для сбора данных о ноутбуке Huawei Matebook D14.

#### Поля

-   `brand`: `"HUAWEI"`
-   `url`: `"https://ksp.co.il/web/cat/268..271..583..23286"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    ```json
    {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"

      }
    ```