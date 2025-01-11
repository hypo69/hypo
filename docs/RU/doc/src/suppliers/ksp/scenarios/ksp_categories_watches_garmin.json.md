# Документация для `ksp_categories_watches_garmin.json`

## Обзор

Файл `ksp_categories_watches_garmin.json` содержит JSON-структуру, описывающую сценарии для парсинга категорий часов бренда GARMIN на сайте KSP. Каждый сценарий включает в себя информацию о конкретной модели часов, URL для парсинга, флаги активности и условия, а также соответствующие категории PrestaShop.

## Содержание

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
3.  [Описание сценариев](#описание-сценариев)
    -   [EPIX](#epix)
    -   [Fenix 6](#fenix-6)
    -   [Fenix 7](#fenix-7)
    -   [HRM](#hrm)
    -   [Vivo](#vivo)
    -   [Venu](#venu)
    -   [Lily](#lily)
    -   [Instinct](#instinct)
    -   [Swim](#swim)
    -   [Enduro](#enduro)
    -   [Forerunner](#forerunner)

## Структура файла

Файл имеет корневой объект с ключом `"scenarios"`, значением которого является объект, содержащий ключи, представляющие названия моделей часов (например, "EPIX", "Fenix 6"). Каждый ключ-модель имеет объект со следующими атрибутами:
- `"brand"`: Бренд часов (всегда "GARMIN" в данном файле).
- `"url"`: URL страницы категории на сайте KSP для парсинга.
- `"checkbox"`: Флаг, определяющий, использовать ли чекбокс (всегда `false` в данном файле).
- `"active"`: Флаг, определяющий, активен ли сценарий (всегда `true` в данном файле).
- `"condition"`: Условие товара (всегда "new" в данном файле).
- `"presta_categories"`: Объект, содержащий соответствия идентификаторов категорий PrestaShop к их названиям.

## Описание сценариев

### EPIX
**Описание**: Сценарий для парсинга категории часов GARMIN EPIX.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..33807`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Fenix 6
**Описание**: Сценарий для парсинга категории часов GARMIN Fenix 6.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..9393..13927..9392..13929..13930..9391`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Fenix 7
**Описание**: Сценарий для парсинга категории часов GARMIN Fenix 7.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..32654..32651..32657`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-   **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### HRM
**Описание**: Сценарий для парсинга категории датчиков сердечного ритма GARMIN HRM.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..33807`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Vivo
**Описание**: Сценарий для парсинга категории часов GARMIN Vivo.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..31651..33932..13858..13860..10115..10116`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Venu
**Описание**: Сценарий для парсинга категории часов GARMIN Venu.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..10117..15956..15955..25643..24313..31738`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Lily
**Описание**: Сценарий для парсинга категории часов GARMIN Lily.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..25048`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-   **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Instinct
**Описание**: Сценарий для парсинга категории часов GARMIN Instinct.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..6109..33962`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-   **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Swim
**Описание**: Сценарий для парсинга категории часов GARMIN Swim.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..10118`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-   **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Enduro
**Описание**: Сценарий для парсинга категории часов GARMIN Enduro.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..21932`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`

### Forerunner
**Описание**: Сценарий для парсинга категории часов GARMIN Forerunner.
-   **`brand`**: `GARMIN`
-   **`url`**: `https://ksp.co.il/web/cat/2085..2160..8336..17956..27545..7820..7821..15741..4104..7822`
-   **`checkbox`**: `false`
-   **`active`**: `true`
-  **`condition`**: `new`
-   **`presta_categories`**:
    -   `"3405"`: `"GOOGLE PIXEL PRO"`
    -   `"3198"`: `"CONSUMER ELECTRONICS"`
    -   `"3202"`: `"computer,smartphone,gaming console,smart device"`
    -   `"6471"`: `"Smartphones"`
    -   `"3403"`: `"GOOGLE"`