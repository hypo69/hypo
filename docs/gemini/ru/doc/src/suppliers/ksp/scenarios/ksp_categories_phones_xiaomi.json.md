# Документация для `ksp_categories_phones_xiaomi.json`

## Обзор

Данный файл содержит JSON-конфигурацию для категорий наушников Xiaomi, используемых в сценариях KSP. Он определяет соответствие между названиями категорий и их идентификаторами, а также содержит информацию о бренде, URL-адресе и другие параметры.

## Оглавление

1. [Общая структура](#общая-структура)
2. [Раздел `scenarios`](#раздел-scenarios)
    - [In-ear Bud](#in-ear-bud)
    - [Xiaomi Mi In-ear Bud cable 3.5mm connection](#xiaomi-mi-in-ear-bud-cable-35mm-connection)

## Общая структура

Файл представляет собой JSON-объект, который содержит единственный ключ `scenarios`. Значение ключа `scenarios` является словарем, где каждый ключ представляет собой название сценария, а значение – это словарь с информацией о сценарии.

## Раздел `scenarios`

Раздел `scenarios` содержит список сценариев для парсинга категорий наушников Xiaomi. Каждый сценарий представляет собой словарь со следующими ключами:

- `brand` (str): Название бренда продукта.
- `url` (str): URL-адрес страницы категории.
- `checkbox` (bool): Флаг, указывающий, является ли сценарий активным (в данном контексте всегда `false`).
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние продукта (в данном случае всегда `new`).
- `presta_categories` (dict): Словарь соответствий между ID категорий и их названиями.

### `In-ear Bud`

**Описание**: Сценарий для парсинга категории "In-ear Bud" наушников Xiaomi.

**Параметры**:
- `brand` (str): "XIAOMI"
- `url` (str): "https://ksp.co.il/web/cat/242..2202..1250"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict): Словарь категорий:
    - `"3459"`: `"In-ear Bud"`
    - `"3198"`: `"CONSUMER ELECTRONICS"`
    - `"3433"`: `"Smartphones smart devices"`
    - `"3436"`: `"Speakers & Audio"`
    - `"3454"`: `"Headphones in Speakers & Audio"`
    - `"4206"`: `"BT Connection"`
    - `"3460"`: `"In-ear Buds"`
    - `"3437"`: `"TV & Audio"`
    - `"3997"`: `"Headphones in TV & Audio"`
    - `"4218"`: `"BT in TV & Audio"`
    - `"4018"`: `"BT In-ear Bud in TV & Audio"`
    - `"2250"`: `"brand:  XIAOMI"`
    - `"4245"`: `"Xiaoimi BT Headphones"`
     

### `Xiaomi Mi In-ear Bud cable 3.5mm connection`

**Описание**: Сценарий для парсинга категории "Xiaomi Mi In-ear Bud cable 3.5mm connection" наушников Xiaomi.

**Параметры**:
- `brand` (str): "XIAOMI"
- `url` (str): "https://ksp.co.il/web/cat/242..2202..1250..5162"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict): Словарь категорий:
    - `"3459"`: `"Xiaomi Mi In-ear Bud cable 3.5mm connection"`
    - `"3198"`: `"CONSUMER ELECTRONICS"`
    - `"3433"`: `"Smartphones smart devices"`
    - `"3436"`: `"Speakers & Audio"`
    - `"3454"`: `"Headphones in Speakers & Audio"`
    - `"4206"`: `"BT Connection"`
    - `"3460"`: `"In-ear Buds"`
    - `"3437"`: `"TV & Audio"`
    - `"3997"`: `"Headphones in TV & Audio"`
    - `"4218"`: `"BT in TV & Audio"`
    - `"4018"`: `"BT In-ear Bud in TV & Audio"`
    - `"2250"`: `"brand:  XIAOMI"`
    - `"2479"`: `"BT Earbuds"`
    - `"3494"`: `"Redmi Buds 3"`