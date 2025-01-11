# Документация для `ksp_categories_tablets_AMAZON.json`

## Оглавление
1. [Обзор](#обзор)
2. [Описание структуры JSON](#описание-структуры-json)
3. [Раздел `scenarios`](#раздел-scenarios)
    - [Общая структура сценария](#общая-структура-сценария)
    - [Сценарий `Amazon Fire 7`](#сценарий-amazon-fire-7)
    - [Сценарий `TAB M8`](#сценарий-tab-m8)

## Обзор

Файл `ksp_categories_tablets_AMAZON.json` содержит JSON-конфигурацию для сценариев парсинга категорий планшетов от поставщика KSP, ориентированных на бренды AMAZON и LENOVO. Каждый сценарий описывает параметры для конкретной модели, включая URL для парсинга и категории PrestaShop.

## Описание структуры JSON

JSON-файл представляет собой словарь с одним ключом `scenarios`, значением которого является другой словарь. Этот вложенный словарь содержит именованные сценарии, где каждый ключ - это название модели (например, `"Amazon Fire 7"`), а значение - словарь с параметрами этого сценария.

## Раздел `scenarios`

Этот раздел содержит все доступные сценарии для парсинга категорий планшетов.

### Общая структура сценария

Каждый сценарий имеет следующую структуру:

- `brand` (str): Бренд планшета.
- `url` (str): URL-адрес страницы каталога KSP для конкретного планшета.
- `checkbox` (bool): Флаг для отметки, используется или нет. В данном случае всегда `false`.
- `active` (bool): Флаг активности сценария, `true` если сценарий используется.
- `condition` (str): Состояние товара.
- `presta_categories` (dict): Словарь соответствий между идентификаторами категорий PrestaShop и их названиями.

### Сценарий `Amazon Fire 7`

#### **Описание**:
Сценарий для парсинга категорий планшета Amazon Fire 7.

#### **Параметры**:

- `brand` (str): "AMAZON"
- `url` (str): "https://ksp.co.il/web/cat/1045..270..159..31989..26718..133790"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict): Словарь категорий PrestaShop.

  - `"3405"`: "GOOGLE PIXEL PRO"
  - `"3198"`: "CONSUMER ELECTRONICS"
  - `"3202"`: "computer,smartphone,gaming console,smart device"
  - `"6471"`: "Smartphones"
  - `"3403"`: "GOOGLE"


### Сценарий `TAB M8`

#### **Описание**:
Сценарий для парсинга категорий планшета Lenovo TAB M8.

#### **Параметры**:

- `brand` (str): "LENOVO"
- `url` (str): "https://ksp.co.il/web/cat/1045..270..159..13379"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict): Словарь категорий PrestaShop.

    - `"3405"`: "GOOGLE PIXEL PRO"
    - `"3198"`: "CONSUMER ELECTRONICS"
    - `"3202"`: "computer,smartphone,gaming console,smart device"
    - `"6471"`: "Smartphones"
    - `"3403"`: "GOOGLE"