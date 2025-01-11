# Документация для `morlevi_categories_ups.json`

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [Сценарии](#сценарии)
    - [ups APC](#ups-apc)
    - [ups EATON](#ups-eaton)

## Обзор

Файл `morlevi_categories_ups.json` содержит JSON-структуру, описывающую сценарии для парсинга категорий товаров ИБП (UPS) от поставщика Morlevi. Каждый сценарий определяет бренд, URL для парсинга, параметры фильтрации и категории PrestaShop.

## Структура JSON

### Сценарии

Раздел "scenarios" содержит объекты, представляющие конкретные сценарии парсинга. Каждый объект имеет ключи:

- `brand`: Бренд ИБП.
- `url`: URL-адрес страницы категории на сайте Morlevi.
- `checkbox`: Логическое значение, указывающее, нужно ли использовать чекбокс.
- `active`: Логическое значение, указывающее, активен ли сценарий.
- `condition`: Состояние товара
- `presta_categories`:  Список ID категорий PrestaShop, к которым относятся товары.

#### `ups APC`

**Описание**: Сценарий для парсинга ИБП бренда APC.

**Параметры**:
-   `brand` (str):  "APC".
-   `url` (str): "https://www.morlevi.co.il/Cat/332?p_315=86&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): "new".
-   `presta_categories` (str): "158,247".

#### `ups EATON`

**Описание**: Сценарий для парсинга ИБП бренда EATON.

**Параметры**:
-   `brand` (str):  "EATON".
-   `url` (str): "https://www.morlevi.co.il/Cat/332?p_315=59&sort=datafloat2%2Cprice&keyword=".
-   `checkbox` (bool): `false`.
-   `active` (bool): `true`.
-   `condition` (str): "new".
-   `presta_categories` (str): "158,247".