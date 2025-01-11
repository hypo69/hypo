# Документация для `morlevi_categories_monitors_aoc.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев парсинга категорий мониторов бренда AOC с сайта Morlevi. Каждый сценарий определяет параметры для конкретного размера монитора, включая URL, бренд, статус активности, условие (новое) и соответствующие категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Сценарии](#сценарии)
    - [`AOC 22`](#aoc-22)
    - [`AOC 23`](#aoc-23)
    - [`AOC 24-25`](#aoc-24-25)
    - [`AOC 27-29`](#aoc-27-29)
    - [`AOC 32`](#aoc-32)
    - [`AOC 34`](#aoc-34)
    - [`AOC 49`](#aoc-49)

## Структура JSON

JSON-файл содержит один корневой объект с ключом `"scenarios"`, значением которого является объект, содержащий наборы сценариев. Каждый сценарий представлен объектом с ключом, являющимся названием сценария (например, `"AOC 22"`) и со следующими атрибутами:
 - `brand` (str): Название бренда.
 - `url` (str): URL-адрес для парсинга.
 - `checkbox` (bool): Флаг для выбора чекбокса.
 - `active` (bool): Флаг, указывающий, активен ли сценарий.
 - `condition` (str): Условие товара, например "new".
 - `presta_categories` (str): Строка, содержащая ID категорий PrestaShop, разделенные запятыми.

## Сценарии

### `AOC 22`

**Описание**: Сценарий для парсинга мониторов AOC 22 дюйма.

**Параметры**:
- `brand` (str): "AOC".
- `url` (str): "---------------------------------------AOC 22-------------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,128,529"`.

### `AOC 23`

**Описание**: Сценарий для парсинга мониторов AOC 23 дюйма.

**Параметры**:
- `brand` (str): `"AOC"`.
- `url` (str): `"https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1806&sort=datafloat2%2Cprice&keyword="`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,128,529"`.

### `AOC 24-25`

**Описание**: Сценарий для парсинга мониторов AOC размером 24-25 дюймов.

**Параметры**:
- `brand` (str): `"AOC"`.
- `url` (str): `"https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1807&sort=datafloat2%2Cprice&keyword="`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,129,529"`.

### `AOC 27-29`

**Описание**: Сценарий для парсинга мониторов AOC размером 27-29 дюймов.

**Параметры**:
- `brand` (str): `"AOC"`.
- `url` (str): `"https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1808&sort=datafloat2%2Cprice&keyword="`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,130,529"`.

### `AOC 32`

**Описание**: Сценарий для парсинга мониторов AOC 32 дюйма.

**Параметры**:
- `brand` (str): `"AOC"`.
- `url` (str): `"https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1809&sort=datafloat2%2Cprice&keyword="`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,131,529"`.

### `AOC 34`

**Описание**: Сценарий для парсинга мониторов AOC 34 дюйма.

**Параметры**:
- `brand` (str): `"AOC"`.
- `url` (str): `" --------------------------  AOC 34 -----------------------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,132,529"`.

### `AOC 49`

**Описание**: Сценарий для парсинга мониторов AOC 49 дюймов.

**Параметры**:
- `brand` (str): `"AOC"`.
- `url` (str): `"-----------------------------  AOC 49 ---------------------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"127,133,529"`.