# Документация для `ksp_categories_tablets_lenovo.json`

## Обзор

Данный файл `ksp_categories_tablets_lenovo.json` содержит сценарии для категорий планшетов Lenovo, используемые для настройки процесса сбора данных с сайта KSP. Каждый сценарий определяет бренд, URL-адрес страницы категории на сайте, флаг активности, состояние товара и соответствие с категориями PrestaShop.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
3.  [Описание сценариев](#описание-сценариев)
    *   [TAB M7 TB-7305](#tab-m7-tb-7305)
    *   [TAB M8](#tab-m8)
    *   [TAB M10](#tab-m10)
    *   [TAB P11](#tab-p11)
    *   [TAB P12](#tab-p12)
    *   [Yoga Smart Tab](#yoga-smart-tab)
    *   [Yoga TAB 11](#yoga-tab-11)
    *   [Yoga TAB 13](#yoga-tab-13)
    
## Структура файла

Файл представляет собой JSON-объект со следующей структурой:

-   `scenarios`: Объект, содержащий сценарии для каждой модели планшета. Ключи объекта - это названия моделей планшетов.
-   Каждый сценарий представлен объектом со следующими полями:
    -   `brand` (str): Бренд планшета, в данном случае всегда "LENOVO".
    -   `url` (str): URL-адрес страницы категории планшета на сайте KSP.
    -   `checkbox` (bool): Флаг, указывающий на использование чекбокса (в данном файле всегда `false`).
    -   `active` (bool): Флаг, определяющий, активен ли сценарий.
    -   `condition` (str): Состояние товара, в данном случае всегда `new`.
    -  `presta_categories` (dict | str): Сопоставление категорий PrestaShop, либо словарь, либо строка.

## Описание сценариев

### `TAB M7 TB-7305`

**Описание**: Сценарий для планшета Lenovo TAB M7 TB-7305.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..133790..11613"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-    `presta_categories` (dict):
        - `"3508"`: `"7-8 inch"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"3227"`: `"Tablets"`
        - `"2572"`: `"LENOVO TAB"`

### `TAB M8`

**Описание**: Сценарий для планшета Lenovo TAB M8.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..13379"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-    `presta_categories` (dict):
         - `"3405"`: `"GOOGLE PIXEL PRO"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"6471"`: `"Smartphones"`
        - `"3403"`: `"GOOGLE"`

### `TAB M10`

**Описание**: Сценарий для планшета Lenovo TAB M10.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..9721..19433..13544"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-  `presta_categories` (dict):
         - `"3405"`: `"GOOGLE PIXEL PRO"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"6471"`: `"Smartphones"`
        - `"3403"`: `"GOOGLE"`

### `TAB P11`

**Описание**: Сценарий для планшета Lenovo TAB P11.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..22065..30559..21476"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-   `presta_categories` (dict):
         - `"3405"`: `"GOOGLE PIXEL PRO"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"6471"`: `"Smartphones"`
        - `"3403"`: `"GOOGLE"`

### `TAB P12`

**Описание**: Сценарий для планшета Lenovo TAB P12.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..32548"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
- `presta_categories` (str): `"697,700,682,260,1,2,429,826,999,1004"`

### `Yoga Smart Tab`

**Описание**: Сценарий для планшета Lenovo Yoga Smart Tab.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..9734"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-    `presta_categories` (dict):
         - `"3405"`: `"GOOGLE PIXEL PRO"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"6471"`: `"Smartphones"`
        - `"3403"`: `"GOOGLE"`

### `Yoga TAB 11`

**Описание**: Сценарий для планшета Lenovo Yoga TAB 11.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..26718"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-    `presta_categories` (dict):
         - `"3405"`: `"GOOGLE PIXEL PRO"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"6471"`: `"Smartphones"`
        - `"3403"`: `"GOOGLE"`

### `Yoga TAB 13`

**Описание**: Сценарий для планшета Lenovo Yoga TAB 13.

**Параметры**:

-   `brand` (str): `"LENOVO"`.
-   `url` (str): `"https://ksp.co.il/web/cat/1045..270..159..26718"`.
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): `"new"`.
-    `presta_categories` (dict):
         - `"3405"`: `"GOOGLE PIXEL PRO"`
        - `"3198"`: `"CONSUMER ELECTRONICS"`
        - `"3202"`: `"computer,smartphone,gaming console,smart device"`
        - `"6471"`: `"Smartphones"`
        - `"3403"`: `"GOOGLE"`