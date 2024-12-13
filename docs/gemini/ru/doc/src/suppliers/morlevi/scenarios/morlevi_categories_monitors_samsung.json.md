# Документация для `morlevi_categories_monitors_samsung.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев парсинга категорий мониторов Samsung с сайта morlevi.co.il.
Каждый сценарий определяет URL, бренд, условия и соответствующие категории PrestaShop для мониторов Samsung разных размеров.

## Оглавление

- [Сценарии](#сценарии)
  - [`SAMSUNG 21 - 22`](#samsung-21---22)
  - [`SAMSUNG 23 - 24`](#samsung-23---24)
  - [`SAMSUNG 26 - 28`](#samsung-26---28)
  - [`SAMSUNG 29 - 31`](#samsung-29---31)
  - [`SAMSUNG 32 - 34`](#samsung-32---34)

## Сценарии

### `SAMSUNG 21 - 22`

**Описание**: Сценарий для парсинга мониторов Samsung размером 21-22 дюйма.

**Параметры**:
- `brand` (str): "SAMSUNG" - бренд мониторов.
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_350=1805&p_315=28&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
- `checkbox` (bool): `false` - флаг для использования чекбокса.
- `active` (bool): `true` - флаг активности сценария.
- `condition` (str): "new" - условие товара.
- `presta_categories` (dict):
    - `template` (dict):
        - `samsung` (str): "PC MONITORS 21 - 22" - категория PrestaShop.

### `SAMSUNG 23 - 24`

**Описание**: Сценарий для парсинга мониторов Samsung размером 23-24 дюйма.

**Параметры**:
- `brand` (str): "SAMSUNG" - бренд мониторов.
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_350=1806&p_315=28&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
- `checkbox` (bool): `false` - флаг для использования чекбокса.
- `active` (bool): `true` - флаг активности сценария.
- `condition` (str): "new" - условие товара.
- `presta_categories` (dict):
    - `template` (dict):
        - `samsung` (str): "PC MONITORS 23 - 24" - категория PrestaShop.

### `SAMSUNG 26 - 28`

**Описание**: Сценарий для парсинга мониторов Samsung размером 26-28 дюймов.

**Параметры**:
- `brand` (str): "SAMSUNG" - бренд мониторов.
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_350=1807&p_315=28&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
- `checkbox` (bool): `false` - флаг для использования чекбокса.
- `active` (bool): `true` - флаг активности сценария.
- `condition` (str): "new" - условие товара.
- `presta_categories` (dict):
    - `template` (dict):
        - `samsung` (str): "PC MONITORS 26 - 28" - категория PrestaShop.

### `SAMSUNG 29 - 31`

**Описание**: Сценарий для парсинга мониторов Samsung размером 29-31 дюйм.

**Параметры**:
- `brand` (str): "SAMSUNG" - бренд мониторов.
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_350=1808&p_315=28&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
- `checkbox` (bool): `false` - флаг для использования чекбокса.
- `active` (bool): `true` - флаг активности сценария.
- `condition` (str): "new" - условие товара.
- `presta_categories` (dict):
    - `template` (dict):
        - `samsung` (str): "PC MONITORS 29 - 31" - категория PrestaShop.

### `SAMSUNG 32 - 34`

**Описание**: Сценарий для парсинга мониторов Samsung размером 32-34 дюйма.

**Параметры**:
- `brand` (str): "SAMSUNG" - бренд мониторов.
- `url` (str): "https://www.morlevi.co.il/Cat/8?p_350=1809&p_350=1810&p_315=28&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
- `checkbox` (bool): `false` - флаг для использования чекбокса.
- `active` (bool): `true` - флаг активности сценария.
- `condition` (str): "new" - условие товара.
- `presta_categories` (dict):
    - `template` (dict):
        - `samsung` (str): "PC MONITORS 32 - 34" - категория PrestaShop.