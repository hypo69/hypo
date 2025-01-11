# morlevi_categories_psu_gigabyte.json

## Обзор

Данный JSON-файл содержит конфигурации сценариев для парсинга блоков питания (PSU) бренда AOURUS BY GIGABYTE с сайта morlevi.co.il. Каждый сценарий включает информацию о модели, URL для парсинга, статусе активности, а также связанных категориях PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [AOURUS BY GIGABYTE 450W](#aourus-by-gigabyte-450w)
    - [AOURUS BY GIGABYTE 500W](#aourus-by-gigabyte-500w)
    - [AOURUS BY GIGABYTE 550W](#aourus-by-gigabyte-550w)
    - [AOURUS BY GIGABYTE 600W](#aourus-by-gigabyte-600w)
    - [AOURUS BY GIGABYTE 650W](#aourus-by-gigabyte-650w)
    - [AOURUS BY GIGABYTE 700W](#aourus-by-gigabyte-700w)
    - [AOURUS BY GIGABYTE 750W](#aourus-by-gigabyte-750w)
    - [AOURUS BY GIGABYTE 850W](#aourus-by-gigabyte-850w)

## Структура JSON

Файл представляет собой JSON-объект с ключом `scenarios`, который содержит объект с ключами, представляющими названия моделей блоков питания. Каждая модель имеет набор атрибутов:

- `brand` (str): Бренд блока питания.
- `name` (str): Мощность блока питания.
- `url` (str): URL-адрес для парсинга (может быть placeholder).
- `checkbox` (bool): Флаг для использования (не используется).
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Условие товара, всегда "new".
- `presta_categories` (str): Строка с идентификаторами категорий PrestaShop, разделенными запятыми.

## Сценарии

### AOURUS BY GIGABYTE 450W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 450W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"450W"`
- `url` (str): `"--------------------------------------AOURUS BY GIGABYTE 450W-------------------------------------------"`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"158,511,188"`

### AOURUS BY GIGABYTE 500W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 500W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"500W"`
- `url` (str): `"--------------------------------------AOURUS BY GIGABYTE 500W-------------------------------------------"`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"158,511,189"`

### AOURUS BY GIGABYTE 550W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 550W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"550W"`
- `url` (str): `"---------------------------------AOURUS BY GIGABYTE 550W--------------------------------------"`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"151,158,511,190"`

### AOURUS BY GIGABYTE 600W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 600W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"600W"`
- `url` (str): `"--------------------------------------AOURUS BY GIGABYTE 600W-------------------------------------------"`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"151,158,511,191"`

### AOURUS BY GIGABYTE 650W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 650W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"650W"`
- `url` (str): `"--------------------------------------AOURUS BY GIGABYTE 650W-------------------------------------------"`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"151,158,511,192"`

### AOURUS BY GIGABYTE 700W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 700W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"700W"`
- `url` (str): `"--------------------------------------AOURUS BY GIGABYTE 700W-------------------------------------------"`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"151,158,511,193"`

### AOURUS BY GIGABYTE 750W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 750W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"750W"`
- `url` (str): `"https://www.morlevi.co.il/Cat/339?p_145=670&sort=datafloat2%2Cprice&keyword="`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"151,158,511,194"`

### AOURUS BY GIGABYTE 850W

**Описание**: Конфигурация сценария для блока питания AOURUS BY GIGABYTE мощностью 850W.

**Параметры**:
- `brand` (str): `"AOURUS BY GIGABYTE"`
- `name` (str): `"850W"`
- `url` (str): `"https://www.morlevi.co.il/Cat/339?p_145=672&sort=datafloat2%2Cprice&keyword="`
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): `"new"`
- `presta_categories` (str): `"151,158,511,571"`