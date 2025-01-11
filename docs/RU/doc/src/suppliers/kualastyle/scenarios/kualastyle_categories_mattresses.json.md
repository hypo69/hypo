# Документация для `kualastyle_categories_mattresses.json`

## Обзор

Файл `kualastyle_categories_mattresses.json` содержит JSON-конфигурацию для категории "Матрасы" в рамках поставщика Kualastyle. Он определяет имя категории на сайте, наличие подкатегорий и набор сценариев.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Ключи верхнего уровня](#ключи-верхнего-уровня)
    - [`category name on site`](#category-name-on-site)
    - [`have subcategories`](#have-subcategories)
    - [`scenarios`](#scenarios)

## Структура JSON

### Ключи верхнего уровня

JSON-файл содержит следующие ключи верхнего уровня:

-   `category name on site`
-   `have subcategories`
-   `scenarios`

### `category name on site`

**Описание**:
Указывает название категории на сайте поставщика Kualastyle.

**Тип данных**: `str`

**Пример**:
```json
"category name on site": "מזרנים"
```

### `have subcategories`

**Описание**:
Логическое значение, определяющее, есть ли у текущей категории подкатегории.

**Тип данных**: `bool`

**Пример**:
```json
"have subcategories": false
```

### `scenarios`

**Описание**:
Словарь, содержащий сценарии для текущей категории. В данном случае пустой, так как подкатегории отсутствуют.

**Тип данных**: `dict`

**Пример**:
```json
"scenarios": {}
```