# morlevi_categories_cases_corsair.json

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для парсинга категорий корпусов бренда CORSAIR с сайта morlevi.co.il. Каждый сценарий определяет условия фильтрации и сопоставления с категориями PrestaShop.

## Оглавление

- [Сценарии](#Сценарии)
  - [CORSAIR MID TOWER](#CORSAIR-MID-TOWER)
  - [CORSAIR full tower](#CORSAIR-full-tower)
  - [CORSAIR mini tower](#CORSAIR-mini-tower)
  - [CORSAIR gaming MID TOWER](#CORSAIR-gaming-MID-TOWER)
  - [CORSAIR gaming full tower](#CORSAIR-gaming-full-tower)
  - [CORSAIR mini itx](#CORSAIR-mini-itx)

## Сценарии

### `CORSAIR MID TOWER`

**Описание**: Сценарий для парсинга корпусов CORSAIR форм-фактора MID TOWER.

**Параметры**:
- `brand` (str): "CORSAIR" - бренд товара.
- `template` (str):  "" - шаблон для дальнейшего использования (пустой).
- `url` (str): "https://www.morlevi.co.il/Cat/99?p_315=20&p_124=540&sort=datafloat2%2Cprice&keyword=" - URL-адрес для парсинга.
- `checkbox` (bool): `false` -  отметка для использования чекбокса (не используется).
- `active` (bool): `true` - определяет, активен ли данный сценарий.
-  `condition` (str): "new" - условие для товара.
- `presta_categories` (dict): Словарь, содержащий сопоставления категорий PrestaShop.
  - `template` (dict): Словарь для сопоставления `corsair` с "MINI ITX"

### `CORSAIR full tower`

**Описание**: Сценарий для парсинга корпусов CORSAIR форм-фактора FULL TOWER.

**Параметры**:
- `brand` (str): "CORSAIR" - бренд товара.
- `template` (str):  "" - шаблон для дальнейшего использования (пустой).
- `url` (str): `null` - URL-адрес для парсинга.
- `checkbox` (bool): `false` -  отметка для использования чекбокса (не используется).
- `active` (bool): `true` - определяет, активен ли данный сценарий.
-  `condition` (str): "new" - условие для товара.
- `presta_categories` (dict): Словарь, содержащий сопоставления категорий PrestaShop.
  - `template` (dict): Словарь для сопоставления `corsair` с "FULL TOWER"

### `CORSAIR mini tower`

**Описание**: Сценарий для парсинга корпусов CORSAIR форм-фактора MINI TOWER.

**Параметры**:
- `brand` (str): "CORSAIR" - бренд товара.
- `template` (str):  "" - шаблон для дальнейшего использования (пустой).
- `url` (str): `null` - URL-адрес для парсинга.
- `checkbox` (bool): `false` -  отметка для использования чекбокса (не используется).
- `active` (bool): `true` - определяет, активен ли данный сценарий.
- `condition` (str): "new" - условие для товара.
- `presta_categories` (dict): Словарь, содержащий сопоставления категорий PrestaShop.
  - `template` (dict): Словарь для сопоставления `corsair` с "MINI TOWER"

### `CORSAIR gaming MID TOWER`

**Описание**: Сценарий для парсинга игровых корпусов CORSAIR форм-фактора MID TOWER.

**Параметры**:
- `brand` (str): "CORSAIR" - бренд товара.
- `template` (str):  "" - шаблон для дальнейшего использования (пустой).
- `url` (str): `null` - URL-адрес для парсинга.
- `checkbox` (bool): `false` -  отметка для использования чекбокса (не используется).
- `active` (bool): `true` - определяет, активен ли данный сценарий.
- `condition` (str): "new" - условие для товара.
- `presta_categories` (dict): Словарь, содержащий сопоставления категорий PrestaShop.
  - `template` (dict): Словарь для сопоставления `corsair` с "MID TOWER"

### `CORSAIR gaming full tower`

**Описание**: Сценарий для парсинга игровых корпусов CORSAIR форм-фактора FULL TOWER.

**Параметры**:
- `brand` (str): "CORSAIR" - бренд товара.
- `template` (str):  "" - шаблон для дальнейшего использования (пустой).
- `url` (str): "https://www.morlevi.co.il/Cat/99?p_315=20&p_124=546&sort=datafloat2%2Cprice&keyword=" - URL-адрес для парсинга.
- `checkbox` (bool): `false` -  отметка для использования чекбокса (не используется).
- `active` (bool): `true` - определяет, активен ли данный сценарий.
-  `condition` (str): "new" - условие для товара.
- `presta_categories` (dict): Словарь, содержащий сопоставления категорий PrestaShop.
  - `template` (dict): Словарь для сопоставления `corsair` с "GAMING FULL TOWER"

### `CORSAIR mini itx`

**Описание**: Сценарий для парсинга корпусов CORSAIR форм-фактора MINI ITX.

**Параметры**:
- `brand` (str): "CORSAIR" - бренд товара.
- `template` (str):  "" - шаблон для дальнейшего использования (пустой).
- `url` (str): `null` - URL-адрес для парсинга.
- `checkbox` (bool): `false` -  отметка для использования чекбокса (не используется).
- `active` (bool): `true` - определяет, активен ли данный сценарий.
- `condition` (str): "new" - условие для товара.
- `presta_categories` (dict): Словарь, содержащий сопоставления категорий PrestaShop.
  - `template` (dict): Словарь для сопоставления `corsair` с "MINI ITX"