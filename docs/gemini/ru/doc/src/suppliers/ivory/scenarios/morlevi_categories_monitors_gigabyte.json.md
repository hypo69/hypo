# Документация для `morlevi_categories_monitors_gigabyte.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев обработки категорий мониторов марки GIGABYTE на сайте morlevi.co.il. Каждый сценарий определяет параметры для конкретного размера монитора, включая URL для сбора данных, активность сценария и соответствие категориям PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Сценарии](#сценарии)
   - [GIGABYTE 22](#gigabyte-22)
   - [GIGABYTE 24-25](#gigabyte-24-25)
   - [GIGABYTE 27-29](#gigabyte-27-29)
   - [GIGABYTE 32](#gigabyte-32)
   - [GIGABYTE 34](#gigabyte-34)
    - [GIGABYTE 49](#gigabyte-49)

## Сценарии

### `GIGABYTE 22`

**Описание**: Сценарий для мониторов GIGABYTE с диагональю 22 дюйма.

**Параметры**:
- `brand` (str): "GIGABYTE".
- `url` (str): "----------------------------------GIGABYTE 22---------------------------------------" (URL не указан).
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "127,128,980".

### `GIGABYTE 24-25`

**Описание**: Сценарий для мониторов GIGABYTE с диагональю 24-25 дюймов.

**Параметры**:
- `brand` (str): "GIGABYTE".
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1807&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "127,129,980".

### `GIGABYTE 27-29`

**Описание**: Сценарий для мониторов GIGABYTE с диагональю 27-29 дюймов.

**Параметры**:
- `brand` (str): "GIGABYTE".
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1808&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "127,130,980".

### `GIGABYTE 32`

**Описание**: Сценарий для мониторов GIGABYTE с диагональю 32 дюйма.

**Параметры**:
- `brand` (str): "GIGABYTE".
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1809&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "127,131,980".

### `GIGABYTE 34`

**Описание**: Сценарий для мониторов GIGABYTE с диагональю 34 дюйма.

**Параметры**:
- `brand` (str): "GIGABYTE".
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1810&sort=datafloat2%2Cprice&keyword=".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "127,132,980".

### `GIGABYTE 49`
**Описание**: Сценарий для мониторов GIGABYTE с диагональю 49 дюймов.

**Параметры**:
- `brand` (str): "GIGABYTE".
- `url` (str): "-----------------------------  GIGABYTE 49 ---------------------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "127,133,980".