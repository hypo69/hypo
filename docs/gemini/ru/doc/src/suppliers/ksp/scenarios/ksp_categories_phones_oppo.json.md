# Категории телефонов OPPO для KSP

## Обзор

Этот файл содержит JSON-конфигурацию для сценариев парсинга категорий телефонов бренда OPPO с сайта KSP. Каждая запись в разделе `scenarios` определяет параметры для конкретной модели телефона, включая URL, статус активности, состояние товара и соответствующие категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Сценарии](#сценарии)
    - [`Oppo A74`](#oppo-a74)
    - [`Oppo A93`](#oppo-a93)
    - [`Oppo A94`](#oppo-a94)
    - [`Oppo Reno 5`](#oppo-reno-5)
    - [`Oppo Reno 5 PRO`](#oppo-reno-5-pro)
    - [`Oppo Reno 6`](#oppo-reno-6)
    - [`Oppo Reno7 Z`](#oppo-reno7-z)
    - [`Oppo Reno7`](#oppo-reno7)
    - [`Oppo A96`](#oppo-a96)
    - [`Oppo Find X5`](#oppo-find-x5)
    - [`Oppo Find X5 PRO`](#oppo-find-x5-pro)

## Структура файла

Файл представляет собой JSON-объект с единственным ключом `scenarios`, значением которого является словарь. Каждый ключ этого словаря представляет собой название модели телефона и содержит в себе данные для парсинга.

```json
{
  "scenarios": {
    "Model Name": {
      "brand": "Brand Name",
      "url": "URL",
      "checkbox": boolean,
      "active": boolean,
      "condition": "new" | "used",
       "presta_categories": {
        "template": {
           "category_name": "Presta Category Name"
          }
       }
    }
  }
}
```
- `brand`: Бренд телефона (всегда "OPPO" в этом файле).
- `url`: URL страницы товара на сайте KSP.
- `checkbox`: Логическое значение, определяющее состояние чекбокса (не используется).
- `active`: Логическое значение, определяющее активность сценария.
- `condition`: Состояние товара ("new" или "used").
- `presta_categories`: Словарь, описывающий категории PrestaShop.
- `template`: Словарь с ключом "oppo" и названием категории PrestaShop.

## Сценарии

### `Oppo A74`

**Описание**: Сценарий для парсинга товаров модели Oppo A74.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..28472`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO A74`

### `Oppo A93`

**Описание**: Сценарий для парсинга товаров модели Oppo A93.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..21447`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO A93`

### `Oppo A94`

**Описание**: Сценарий для парсинга товаров модели Oppo A94.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..25412`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO A94`

### `Oppo Reno 5`

**Описание**: Сценарий для парсинга товаров модели Oppo Reno 5.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..25491`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO RENO 5`

### `Oppo Reno 5 PRO`

**Описание**: Сценарий для парсинга товаров модели Oppo Reno 5 PRO.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..25800`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO RENO 5 PRO`

### `Oppo Reno 6`

**Описание**: Сценарий для парсинга товаров модели Oppo Reno 6.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..28099`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO RENO 6`

### `Oppo Reno7 Z`

**Описание**: Сценарий для парсинга товаров модели Oppo Reno7 Z.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..36732`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO RENO 7Z`

### `Oppo Reno7`

**Описание**: Сценарий для парсинга товаров модели Oppo Reno7.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..36731`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO RENO 7`

### `Oppo A96`

**Описание**: Сценарий для парсинга товаров модели Oppo A96.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..37544`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO A96`

### `Oppo Find X5`

**Описание**: Сценарий для парсинга товаров модели Oppo Find X5.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..42014`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO FIND X5`

### `Oppo Find X5 PRO`

**Описание**: Сценарий для парсинга товаров модели Oppo Find X5 PRO.

- **brand**: `OPPO`
- **url**: `https://ksp.co.il/web/cat/573..21448..42025`
- **checkbox**: `false`
- **active**: `true`
- **condition**: `new`
- **presta_categories**:
  - **template**: 
    - **oppo**: `OPPO FIND X5 PRO`