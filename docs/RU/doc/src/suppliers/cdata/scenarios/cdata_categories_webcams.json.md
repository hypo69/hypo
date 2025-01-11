# Документация для `cdata_categories_webcams.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сбора данных о веб-камерах с сайта C-Data. Конфигурация включает сценарии для различных брендов (например, MICROSOFT, HP), определяя параметры для сбора данных, такие как URL, активность, условия и категории PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Сценарии](#сценарии)
        - [Cams MICROSOFT](#cams-microsoft)
        - [Cams HP](#cams-hp)
- [Пример использования](#пример-использования)

## Структура JSON

### Сценарии

Раздел "scenarios" содержит определения для каждого бренда.

#### `Cams MICROSOFT`

**Описание**:
Сценарий для сбора данных о веб-камерах бренда MICROSOFT.

**Параметры**:
- `brand` (str): Название бренда ("MICROSOFT").
- `url` (str): URL-адрес для сбора данных.
- `checkbox` (bool): Флаг для чекбокса (всегда `false`).
- `active` (bool): Флаг активности сценария (всегда `true`).
- `condition` (str): Условие товара ("new").
- `presta_categories` (str): ID категорий PrestaShop ("520,523,984").

**Пример**:
```json
    "Cams MICROSOFT": {
      "brand": "MICROSOFT",
      "url": "https://reseller.c-data.co.il/camwebs-and-controllers#/manFilters=1&pageSize=33&viewMode=grid&orderBy=0&pageNumber=1",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "520,523,984"
    }
```

#### `Cams HP`

**Описание**:
Сценарий для сбора данных о веб-камерах бренда HP.

**Параметры**:
- `brand` (str): Название бренда ("HP").
- `url` (str): URL-адрес для сбора данных.
- `checkbox` (bool): Флаг для чекбокса (всегда `false`).
- `active` (bool): Флаг активности сценария (всегда `true`).
- `condition` (str): Условие товара ("new").
- `presta_categories` (str): ID категорий PrestaShop ("520,523,985").

**Пример**:
```json
    "Cams HP": {
      "brand": "HP",
      "url": "https://reseller.c-data.co.il/camwebs-and-controllers#/manFilters=2&pageSize=33&viewMode=grid&orderBy=0&pageNumber=1",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "520,523,985"
    }
```

## Пример использования

```json
{
  "scenarios": {
    "Cams MICROSOFT": {
      "brand": "MICROSOFT",
      "url": "https://reseller.c-data.co.il/camwebs-and-controllers#/manFilters=1&pageSize=33&viewMode=grid&orderBy=0&pageNumber=1",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "520,523,984"
    },
    "Cams HP": {
      "brand": "HP",
      "url": "https://reseller.c-data.co.il/camwebs-and-controllers#/manFilters=2&pageSize=33&viewMode=grid&orderBy=0&pageNumber=1",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "520,523,985"
    }
  }
}
```

Данная конфигурация может использоваться в скриптах для автоматизированного сбора данных о веб-камерах, указанных брендов, с веб-сайта C-Data.