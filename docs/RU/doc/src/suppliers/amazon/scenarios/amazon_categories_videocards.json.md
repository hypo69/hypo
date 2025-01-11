# Документация для `hypotez/src/suppliers/amazon/scenarios/amazon_categories_videocards.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [VIDEOCARDS GIGABYTE NEW](#videocards-gigabyte-new)
    - [VIDEOCARDS GIGABYTE USED](#videocards-gigabyte-used)

## Обзор

Данный файл `amazon_categories_videocards.json` содержит конфигурацию сценариев для парсинга видеокарт бренда GIGABYTE с сайта Amazon. Каждый сценарий определяет параметры для поиска и фильтрации товаров, включая условие (`new`, `used`), URL для поиска, категорию, а также правило ценообразования.

## Структура JSON
Файл имеет корневой объект с ключом `"scenarios"`, который содержит объект, ключи которого являются названиями сценариев. Каждый сценарий представлен объектом со следующими ключами:
- `"brand"`: Название бренда видеокарт (например, `"GIGABYTE"`).
- `"url"`: URL-адрес для поиска товаров на Amazon.
- `"active"`: Булево значение, указывающее, активен ли сценарий (например, `true`).
- `"condition"`: Состояние товара (`"new"` или `"used"`).
- `"presta_categories"`: Объект, определяющий соответствие между названием бренда и категорией PrestaShop.
- `"checkbox"`: Булево значение, указывающее, используется ли чекбокс (например, `false`).
- `"price_rule"`: Правило ценообразования (например, `1`).

## Сценарии

### `VIDEOCARDS GIGABYTE NEW`
**Описание**:
Сценарий для поиска новых видеокарт GIGABYTE.

**Параметры**:
- `brand` (str): `GIGABYTE`.
- `url` (str): `https://www.amazon.com/s?k=video+cards+gigabyte&i=electronics&bbn=172282&rh=n%3A172282%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AGIGABYTE%7CGigabyte%2Cp_n_condition-type%3A2224371011&dc&qid=1676213463&rnid=2224369011&ref=sr_nr_p_n_condition-type_1&ds=v1%3AVCRt9bSSpHdfd3sCc77vMRorubXPCRtN7SM2vVBM8fA`.
- `active` (bool): `true`.
- `condition` (str): `new`.
- `presta_categories` (dict):
    - `template` (dict):
        - `gigabyte` (str): `VIDEOCARDS`.
- `checkbox` (bool): `false`.
- `price_rule` (int): `1`.

### `VIDEOCARDS GIGABYTE USED`
**Описание**:
Сценарий для поиска б/у видеокарт GIGABYTE.

**Параметры**:
- `brand` (str): `GIGABYTE`.
- `url` (str): `https://www.amazon.com/s?k=video+cards+gigabyte&i=electronics&bbn=172282&rh=n%3A172282%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AGIGABYTE%7CGigabyte%2Cp_n_condition-type%3A2224373011&dc&qid=1676213812&rnid=2224369011&ref=sr_nr_p_n_condition-type_2&ds=v1%3AoSZQwtl9Ns40qx0BtCgu5jLXQ0hbQt7d6%2F9wM5zFM%2BQ`.
- `active` (bool): `true`.
- `condition` (str): `used`.
- `presta_categories` (dict):
    - `template` (dict):
        - `gigabyte` (str): `VIDEOCARDS`.
- `checkbox` (bool): `false`.
- `price_rule` (int): `1`.