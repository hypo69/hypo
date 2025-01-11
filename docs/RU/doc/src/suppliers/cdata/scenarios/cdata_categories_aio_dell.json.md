# Документация для `cdata_categories_aio_dell.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для категорий товаров AIO (All-In-One) бренда DELL, полученных от поставщика CData. Каждый сценарий определяет параметры для конкретной модели AIO, включая бренд, URL, статус активности, условие (состояние) и соответствие категориям PrestaShop.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [DELL 21.5 - I3](#dell-215---i3)
    - [DELL 21.5 - I5](#dell-215---i5)
    - [DELL 21.5 - I7](#dell-215---i7)
    - [DELL 21.5 - I9](#dell-215---i9)
    - [DELL 21.5 amd](#dell-215-amd)
    - [DELL 23.5 I3](#dell-235-i3)
    - [DELL 23.8 I5](#dell-238-i5)
    - [DELL 23.8 I7](#dell-238-i7)
    - [DELL 23.5 I9](#dell-235-i9)
    - [DELL 23.5 amd](#dell-235-amd)
    - [DELL 27 I3](#dell-27-i3)
    - [DELL 27 I5](#dell-27-i5)
    - [DELL 27 I7](#dell-27-i7)
    - [DELL 27 ATOM](#dell-27-atom)
    - [DELL 27 I9](#dell-27-i9)
    - [DELL 27 amd](#dell-27-amd)
    - [DELL 34 I3](#dell-34-i3)
    - [DELL 34 I5](#dell-34-i5)
    - [DELL 34 I7](#dell-34-i7)
    - [DELL 34 I9](#dell-34-i9)
    - [DELL 34 amd](#dell-34-amd)

## Структура JSON

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "Название сценария": {
      "brand": "Бренд товара",
      "url": "URL товара",
      "checkbox": "Статус чекбокса (true/false)",
      "active": "Статус активности (true/false)",
       "condition":"Состояние товара",
      "presta_categories": "Список ID категорий PrestaShop (разделенные запятой)"
    },
      ...
  }
}
```
## Сценарии

### `DELL 21.5 - I3`

**Описание**: Настройки для модели AIO DELL 21.5 дюймов с процессором Intel Core i3.

**Параметры**:
- `brand`: "DELL"
- `url`: "--------------AIO DELL 21.5 - I3---------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,37,303,41,37"

### `DELL 21.5 - I5`

**Описание**: Настройки для модели AIO DELL 21.5 дюймов с процессором Intel Core i5.

**Параметры**:
- `brand`: "DELL"
- `url`: "--------------AIO DELL 21.5 - I5---------------2"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,38,303,41,38"

### `DELL 21.5 - I7`

**Описание**: Настройки для модели AIO DELL 21.5 дюймов с процессором Intel Core i7.

**Параметры**:
- `brand`: "DELL"
- `url`: "---------------AIO DELL 21.5 - I7---------------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,39,41,39"

### `DELL 21.5 - I9`

**Описание**: Настройки для модели AIO DELL 21.5 дюймов с процессором Intel Core i9.

**Параметры**:
- `brand`: "DELL"
- `url`: "----------------AIO DELL 21.5 - I9------------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,41,301"

### `DELL 21.5 amd`

**Описание**: Настройки для модели AIO DELL 21.5 дюймов с процессором AMD.

**Параметры**:
- `brand`: "DELL"
- `url`: "----------------AIO DELL 21.5 amd----------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,41,302"

### `DELL 23.5 I3`

**Описание**: Настройки для модели AIO DELL 23.5 дюймов с процессором Intel Core i3.

**Параметры**:
- `brand`: "DELL"
- `url`: "----------------AIO DELL 23.5 I3---------------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,37,303,42,37"

### `DELL 23.8 I5`

**Описание**: Настройки для модели AIO DELL 23.8 дюймов с процессором Intel Core i5.

**Параметры**:
- `brand`: "DELL"
- `url`: "https://reseller.c-data.co.il/All-In-One#/specFilters=227m!#-!4634!-#!225!#-!5510&manFilters=4"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,38,303,42"

### `DELL 23.8 I7`

**Описание**: Настройки для модели AIO DELL 23.8 дюймов с процессором Intel Core i7.

**Параметры**:
- `brand`: "DELL"
- `url`: "https://reseller.c-data.co.il/All-In-One#/specFilters=225!#-!5510!-#!227m!#-!4635&manFilters=4"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,42,39"

### `DELL 23.5 I9`

**Описание**: Настройки для модели AIO DELL 23.5 дюймов с процессором Intel Core i9.

**Параметры**:
- `brand`: "DELL"
- `url`: "----------------AIO DELL 23.5 I9-------------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,42,301"

### `DELL 23.5 amd`

**Описание**: Настройки для модели AIO DELL 23.5 дюймов с процессором AMD.

**Параметры**:
- `brand`: "DELL"
- `url`: "---------------AIO DELL 23.5 amd---------------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,42,302"

### `DELL 27 I3`

**Описание**: Настройки для модели AIO DELL 27 дюймов с процессором Intel Core i3.

**Параметры**:
- `brand`: "DELL"
- `url`: "---------------AIO DELL 27 I3-----------0"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,37,303,43,37"

### `DELL 27 I5`

**Описание**: Настройки для модели AIO DELL 27 дюймов с процессором Intel Core i5.

**Параметры**:
- `brand`: "DELL"
- `url`: "-----------------AIO DELL 27 I5-------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,38,303,43"

### `DELL 27 I7`

**Описание**: Настройки для модели AIO DELL 27 дюймов с процессором Intel Core i7.

**Параметры**:
- `brand`: "DELL"
- `url`: "https://reseller.c-data.co.il/All-In-One#/specFilters=227m!#-!30335!-#!225!#-!5512&manFilters=4"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,43,39"

### `DELL 27 ATOM`

**Описание**: Настройки для модели AIO DELL 27 дюймов с процессором Intel ATOM.

**Параметры**:
- `brand`: "DELL"
- `url`: "https://reseller.c-data.co.il/All-In-One#/specFilters=227!#-!4652!-#!225m!#-!5512&manFilters=4"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,43,519"

### `DELL 27 I9`

**Описание**: Настройки для модели AIO DELL 27 дюймов с процессором Intel Core i9.

**Параметры**:
- `brand`: "DELL"
- `url`: "-------------AIO DELL 27 I9-------------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,43,301"

### `DELL 27 amd`

**Описание**: Настройки для модели AIO DELL 27 дюймов с процессором AMD.

**Параметры**:
- `brand`: "DELL"
- `url`: "-------------AIO DELL 27 amd-----------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,43,302"

### `DELL 34 I3`

**Описание**: Настройки для модели AIO DELL 34 дюймов с процессором Intel Core i3.

**Параметры**:
- `brand`: "DELL"
- `url`: "-------------AIO DELL 34 I3------------------0"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,37,303,227,37"

### `DELL 34 I5`

**Описание**: Настройки для модели AIO DELL 34 дюймов с процессором Intel Core i5.

**Параметры**:
- `brand`: "DELL"
- `url`: "--------------AIO DELL 34 I5------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,38,303,227,38"

### `DELL 34 I7`

**Описание**: Настройки для модели AIO DELL 34 дюймов с процессором Intel Core i7.

**Параметры**:
- `brand`: "DELL"
- `url`: "--------------AIO DELL 34 I7------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,227,39"

### `DELL 34 I9`

**Описание**: Настройки для модели AIO DELL 34 дюймов с процессором Intel Core i9.

**Параметры**:
- `brand`: "DELL"
- `url`: "-------------AIO DELL 34 I9-------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,227,301"

### `DELL 34 amd`

**Описание**: Настройки для модели AIO DELL 34 дюймов с процессором AMD.

**Параметры**:
- `brand`: "DELL"
- `url`: "------------AIO DELL 34 amd-------------"
- `checkbox`: `false`
- `active`: `true`
-  `condition`: "new"
- `presta_categories`: "35,303,227,302"