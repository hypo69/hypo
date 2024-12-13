# Документация для `ksp_categories_monitors_lg.json`

## Обзор

Файл `ksp_categories_monitors_lg.json` содержит конфигурационные данные для сбора информации о мониторах LG с сайта KSP.  В файле представлены различные сценарии, каждый из которых описывает конкретную категорию мониторов по размеру. Для каждой категории определены URL-адрес, бренд, флаги активности и соответствие категориям PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [`LG monitors 21 - 22 inch`](#lg-monitors-21---22-inch)
    - [`LG monitors 22 -24 inch`](#lg-monitors-22--24-inch)
    - [`LG monitors 26 28 inch`](#lg-monitors-26-28-inch)
    - [`LG monitors about 29 inch`](#lg-monitors-about-29-inch)
    - [`LG monitors 31 32 inch`](#lg-monitors-31-32-inch)
    - [`LG monitors 34 inch`](#lg-monitors-34-inch)
    - [`LG monitors 48 inch`](#lg-monitors-48-inch)

## Структура файла

Файл представляет собой JSON-объект, содержащий единственный ключ `"scenarios"`, значением которого является объект, представляющий собой набор сценариев. Каждый сценарий имеет следующий формат:

- `"brand"` (str): Бренд монитора (в данном случае, всегда "LG").
- `"url"` (str): URL-адрес страницы с категорией мониторов на сайте KSP.
- `"checkbox"` (bool): Флаг, указывающий, нужно ли использовать чекбокс (в данном случае, всегда `false`).
- `"active"` (bool): Флаг, указывающий, активен ли сценарий (в данном случае, всегда `true`).
- `"condition"` (str): Состояние товара (в данном случае, всегда "new").
- `"presta_categories"` (dict): Объект, содержащий настройки соответствия категориям PrestaShop.
  - `"template"` (dict): Объект с ключом `"lg"` (бренд) и значением - названием категории в PrestaShop.

## Сценарии

### `LG monitors 21 - 22 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером 21-22 дюйма.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..134..31308..194..195"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 21 - 22" }`

### `LG monitors 22 -24 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером 22-24 дюйма.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..134..1649..198"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 22 - 24" }`

### `LG monitors 26 28 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером 26-28 дюймов.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..137..4831..199..4784..2037"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 26 - 28" }`

### `LG monitors about 29 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером около 29 дюймов.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..137..4831..199..4784..2037"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 26 - 28" }`

### `LG monitors 31 32 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером 31-32 дюйма.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..137..1948..200"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 31 - 33" }`

### `LG monitors 34 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером 34 дюйма.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..137..2129"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 34 - 38" }`

### `LG monitors 48 inch`

**Описание**:
Сценарий для сбора данных о мониторах LG размером 48 дюймов.

**Параметры**:
- `"brand"`: `"LG"`
- `"url"`: `"https://ksp.co.il/web/cat/230..137..4831..199..4784..2037"`
- `"checkbox"`: `false`
- `"active"`: `true`
- `"condition"`: `"new"`
- `"presta_categories"`:
    - `"template"`: `{ "lg": "PC MONITORS 50" }`