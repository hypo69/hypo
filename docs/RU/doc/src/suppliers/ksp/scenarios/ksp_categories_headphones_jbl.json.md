# Документация для `ksp_categories_headphones_jbl.json`

## Обзор

Этот файл содержит JSON-структуру, определяющую сценарии для наушников JBL, которые будут использоваться для категоризации товаров в PrestaShop. Каждый сценарий включает информацию о бренде, URL-адресе категории на сайте KSP, состоянии товара (новый), и соответствии шаблону категории в PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [JBL Tune 225TWS True Wireless Earbuds](#jbl-tune-225tws-true-wireless-earbuds)
    - [JBL 200BT In-ear Bud Headphones](#jbl-200bt-in-ear-bud-headphones)
    - [In-ear Bud, JBL 125BT Neckband Headphones](#in-ear-bud-jbl-125bt-neckband-headphones)
    - [JBL 650BTNC Over-ear Headphones](#jbl-650btnc-over-ear-headphones)
    - [In-ear Bud, JBL C100SI Headphones](#in-ear-bud-jbl-c100si-headphones)
    - [In-ear Bud, JBL 115BT Neckband Headphones](#in-ear-bud-jbl-115bt-neckband-headphones)

## Структура файла

Файл имеет корневой ключ `scenarios`, который содержит объект. Внутри этого объекта каждый ключ представляет собой название сценария для определенной модели наушников JBL.  Каждый сценарий является объектом со следующими ключами:

- `brand` (str): Бренд продукта, всегда "JBL".
- `url` (str): URL-адрес страницы категории на сайте KSP.
- `checkbox` (bool): Флаг, который в данный момент всегда `false`.
- `active` (bool): Флаг, указывающий, активен ли сценарий, всегда `true`.
- `condition` (str): Состояние товара, всегда "new".
- `presta_categories` (dict): Объект, содержащий шаблоны категорий PrestaShop.
  - `template` (dict): Объект, где ключ `"jbl"` соответствует названию товара в PrestaShop.

## Сценарии

### `JBL Tune 225TWS True Wireless Earbuds`

**Описание**: Сценарий для беспроводных наушников JBL Tune 225TWS.

**Параметры**:
- `brand` (str):  "JBL"
- `url` (str):  "https://ksp.co.il/web/cat/242..1250..3127..36135"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict): `{"jbl": "JBL Tune 225TWS True Wireless Earbuds"}`

### `JBL 200BT In-ear Bud Headphones`

**Описание**: Сценарий для беспроводных наушников-вкладышей JBL 200BT.

**Параметры**:
- `brand` (str):  "JBL"
- `url` (str): "https://ksp.co.il/web/cat/242..1250..3127..36130"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict): `{"jbl": "JBL 200BT True Wireless In-ear Bud Headphones"}`

### `In-ear Bud, JBL 125BT Neckband Headphones`

**Описание**: Сценарий для наушников с шейным ободом JBL 125BT.

**Параметры**:
- `brand` (str): "JBL"
- `url` (str): "https://ksp.co.il/web/cat/242..1250..3127..36125"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict): `{"jbl": "In-ear Bud, JBL 125BT Neckband Headphones"}`

### `JBL 650BTNC Over-ear Headphones`

**Описание**: Сценарий для накладных наушников JBL 650BTNC.

**Параметры**:
- `brand` (str): "JBL"
- `url` (str): "https://ksp.co.il/web/cat/242..3127..1252..36119"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict): `{"jbl": "JBL 650BTNC Over-ear Headphones"}`

### `In-ear Bud, JBL C100SI Headphones`

**Описание**: Сценарий для вкладышей JBL C100SI.

**Параметры**:
- `brand` (str): "JBL"
- `url` (str): "https://ksp.co.il/web/cat/242..1250..3127..36117"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict): `{"jbl": "In-ear Bud, JBL C100SI Headphones"}`

### `In-ear Bud, JBL 115BT Neckband Headphones`

**Описание**: Сценарий для наушников с шейным ободом JBL 115BT.

**Параметры**:
- `brand` (str): "JBL"
- `url` (str): "https://ksp.co.il/web/cat/242..1250..3127..36118"
- `checkbox` (bool): `false`
- `active` (bool): `true`
- `condition` (str): "new"
- `presta_categories` (dict):
    - `template` (dict): `{"jbl": "In-ear Bud, JBL 125BT Neckband Headphones"}`