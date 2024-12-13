# Документация для `ksp_categories_phones_asus.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Раздел "scenarios"](#раздел-scenarios)
    - [Описание](#описание-1)
    - [Структура сценария](#структура-сценария)
      - [brand](#brand)
      - [url](#url)
      - [checkbox](#checkbox)
      - [active](#active)
      - [condition](#condition)
      - [presta_categories](#presta_categories)
        - [template](#template)
4. [Примеры](#примеры)

## Обзор

Файл `ksp_categories_phones_asus.json` содержит JSON-структуру с данными о сценариях для парсинга категорий телефонов Asus с сайта ksp.co.il. Каждый сценарий определяет настройки для конкретной модели телефона, включая URL страницы, состояние чекбокса, активность и соответствие категориям PrestaShop.

## Структура JSON

Файл представляет собой JSON-объект с одним ключом "scenarios", значением которого является объект, содержащий сценарии для различных моделей телефонов.

## Раздел "scenarios"

### Описание
Объект `scenarios` содержит набор сценариев для парсинга. Каждый ключ в этом объекте является названием конкретного сценария (модели телефона), а значение – объект с настройками для этого сценария.

### Структура сценария
Каждый сценарий включает следующие поля:

  - **brand**: (string) Производитель телефона. Всегда "ASUS" для этого файла.
  - **url**: (string) URL страницы с категорией товара на сайте ksp.co.il.
  - **checkbox**: (boolean) Состояние чекбокса (всегда false в данном файле).
  - **active**: (boolean) Флаг, указывающий, активен ли сценарий (всегда true в данном файле).
  - **condition**: (string) Условие товара, например, "new".
  - **presta_categories**: (object) Объект, содержащий информацию о категориях PrestaShop.
    - **template**: (object) Объект, содержащий соответствие для PrestaShop.
        - **asus**: (string) Название модели телефона для PrestaShop.

#### brand

**Описание**:
Название бренда производителя телефона.
**Тип**:
`string`
**Пример**:
`"ASUS"`

#### url

**Описание**:
URL-адрес страницы категории товара на сайте ksp.co.il.
**Тип**:
`string`
**Пример**:
`"https://ksp.co.il/web/cat/573..1358..24585"`

#### checkbox
**Описание**:
Состояние чекбокса.
**Тип**:
`boolean`
**Возможные значения**:
`true` или `false` (в данном случае всегда `false`).

#### active

**Описание**:
Флаг, указывающий, активен ли данный сценарий.
**Тип**:
`boolean`
**Возможные значения**:
`true` или `false` (в данном случае всегда `true`).

#### condition
**Описание**:
Состояние товара.
**Тип**:
`string`
**Пример**:
`"new"`

#### presta_categories
**Описание**:
Объект, содержащий информацию о категориях PrestaShop.
**Тип**:
`object`
**Содержимое**:
Объект с ключом `template`.

##### template

**Описание**:
Объект, содержащий соответствие для PrestaShop.
**Тип**:
`object`
**Содержимое**:
Объект с ключом `asus`, значением которого является название модели телефона для PrestaShop.

## Примеры

```json
{
  "scenarios": {
    "Asus Zenfone 8": {
      "brand": "ASUS",
      "url": "https://ksp.co.il/web/cat/573..1358..24585",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": { "asus": "ZENFONE 8" }
      }
    },
    "Asus Zenfone 9": {
      "brand": "ASUS",
      "url": "https://ksp.co.il/web/cat/573..1358..40840",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": { "asus": "ZENFONE 9" }
      }
    },
    "Asus ROG Phone 6": {
      "brand": "ASUS",
      "url": "https://ksp.co.il/web/cat/573..1358..40085",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": { "asus": "ROGFONE 6" }
      }
    },
    "ROGFONE 6 PRO": {
      "brand": "ASUS",
      "url": "https://ksp.co.il/web/cat/573..1358..43737",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": { "asus": "ROGFONE 6 PRO" }
      }
    },
    "ROGFONE 6 PRO BATMAN EDITION": {
      "brand": "ASUS",
      "url": "https://ksp.co.il/web/cat/573..1358..43370",
       "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": {
        "template": { "asus": "ROGFONE 6 PRO BATMAN EDITION" }
      }
    }
  }
}
```