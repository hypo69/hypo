# Категории телефонов Nokia для KSP

## Обзор

Этот файл содержит JSON-конфигурацию сценариев для определения категорий телефонов Nokia на сайте KSP. Он включает в себя информацию о различных моделях телефонов Nokia, их URL-адресах на сайте KSP, а также информацию о связанных категориях PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Сценарии](#сценарии)
    - [`Nokia 110 4G`](#nokia-110-4g)
    - [`Nokia 105 4G`](#nokia-105-4g)
    - [`Nokia XR20 TA-1362`](#nokia-xr20-ta-1362)
    - [`NOKIA G10`](#nokia-g10)
    - [`Nokia 800 Tough`](#nokia-800-tough)
    - [`NOKIA 215 4G`](#nokia-215-4g)
    - [`NOKIA 5310`](#nokia-5310)
    - [`NOKIA 225 4G`](#nokia-225-4g)
    - [`NOKIA 110`](#nokia-110)
    - [`NOKIA 220 4G`](#nokia-220-4g)
    - [`Nokia 230`](#nokia-230)
    - [`Nokia 105`](#nokia-105)
    - [`NOKIA G11`](#nokia-g11)
    - [`NOKIA G21`](#nokia-g21)

## Структура JSON

JSON состоит из одного объекта с ключом `scenarios`, значением которого является объект, содержащий описания сценариев для различных моделей телефонов Nokia.

## Сценарии

Каждый сценарий представляет собой запись с ключом, соответствующим названию модели телефона. Он содержит следующие поля:

-   `brand` (str): Бренд телефона ("NOKIA").
-   `url` (str): URL-адрес страницы товара на сайте KSP.
-   `checkbox` (bool): Флаг, определяющий, выбран ли данный сценарий.
-   `active` (bool): Флаг, указывающий, активен ли данный сценарий.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Объект с категориями PrestaShop.
    -   `template` (dict): Объект с ключом `nokia`, значением которого является название модели телефона.

### `Nokia 110 4G`

**Описание**: Конфигурация для модели Nokia 110 4G.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..36478"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 110 4G"

### `Nokia 105 4G`

**Описание**: Конфигурация для модели Nokia 105 4G.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..36285"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 105 4G"

### `Nokia XR20 TA-1362`

**Описание**: Конфигурация для модели Nokia XR20 TA-1362.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..33389"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA XR20"

### `NOKIA G10`

**Описание**: Конфигурация для модели NOKIA G10.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..26225"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA G10"

### `Nokia 800 Tough`

**Описание**: Конфигурация для модели Nokia 800 Tough.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..24205"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 800 TOUGH"

### `NOKIA 215 4G`

**Описание**: Конфигурация для модели NOKIA 215 4G.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..22710"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 215 4G"

### `NOKIA 5310`

**Описание**: Конфигурация для модели NOKIA 5310.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..20947"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 5310"

### `NOKIA 225 4G`

**Описание**: Конфигурация для модели NOKIA 225 4G.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..18063"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 225 4G"

### `NOKIA 110`

**Описание**: Конфигурация для модели NOKIA 110.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..10307"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 110"

### `NOKIA 220 4G`

**Описание**: Конфигурация для модели NOKIA 220 4G.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..10050"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 220 4G"

### `Nokia 230`

**Описание**: Конфигурация для модели Nokia 230.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..7423"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 230"

### `Nokia 105`

**Описание**: Конфигурация для модели Nokia 105.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..573..325..2348"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA 105"

### `NOKIA G11`

**Описание**: Конфигурация для модели NOKIA G11.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..325..573..37077"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA G11"

### `NOKIA G21`

**Описание**: Конфигурация для модели NOKIA G21.

**Параметры**:
- `brand` (str): "NOKIA"
- `url` (str): "https://ksp.co.il/web/cat/272..325..573..37077"
- `checkbox` (bool): false
- `active` (bool): true
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict):
        - `nokia` (str): "NOKIA G21"