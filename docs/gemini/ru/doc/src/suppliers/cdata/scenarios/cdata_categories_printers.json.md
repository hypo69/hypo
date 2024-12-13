# CData Categories Printers

## Обзор

Этот файл `cdata_categories_printers.json` содержит конфигурацию для сценариев принтеров CData, включая информацию о бренде, URL-адресах, параметрах фильтрации и соответствующих категориях PrestaShop.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
3.  [Сценарии](#сценарии)
    - [`HP DIO AIO A4`](#hp-dio-aio-a4)
    - [`HP DIO PRINTERONLY A4`](#hp-dio-printeronly-a4)
    - [`HP DIO AIO A3`](#hp-dio-aio-a3)
    - [`HP DIO PRINTERONLY A3`](#hp-dio-printeronly-a3)
    - [`HP LASER COLOR AIO A4`](#hp-laser-color-aio-a4)
    - [`HP LASER COLOR PRINTERONLY A4`](#hp-laser-color-printeronly-a4)
    - [`HP LASER BW AIO A4`](#hp-laser-bw-aio-a4)
    - [`HP LASER BW PRINTERONLY A4`](#hp-laser-bw-printeronly-a4)
    - [`HP LASER COLOR AIO A3`](#hp-laser-color-aio-a3)
    - [`HP LASER COLOR PRINTERONLY A3`](#hp-laser-color-printeronly-a3)
    - [`HP LASER BW AIO A3`](#hp-laser-bw-aio-a3)
    - [`HP LASER BW PRINTERONLY A3`](#hp-laser-bw-printeronly-a3)

## Структура JSON

Файл представляет собой JSON-объект со следующей структурой:

```json
{
  "scenarios": {
    "scenario_name": {
      "brand": "brand_name",
      "url": "url_to_filter_page",
      "checkbox": boolean,
      "active": boolean,
      "condition": "new"|"used"|"refurbished"
      "presta_categories": "comma_separated_category_ids"
    }
  }
}
```
   
* `scenarios`: Объект, содержащий различные сценарии для принтеров.
* `scenario_name`: Ключ, представляющий уникальное имя сценария.
* `brand`: Строка, обозначающая бренд принтера (например, `"HP"`).
* `url`: Строка, содержащая URL-адрес страницы с фильтрами на сайте поставщика.
* `checkbox`: Логическое значение, указывающее, используется ли чекбокс.
* `active`: Логическое значение, указывающее, активен ли сценарий.
* `condition`: Строка, указывающее на состояние товара (new, used, refurbished).
* `presta_categories`: Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

## Сценарии

### `HP DIO AIO A4`
**Описание**: Сценарий для многофункциональных принтеров HP DIO AIO формата A4.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219m!#-!4606!##!6354!##!4607!-#!214!#-!4585!-#!217!#-!4602&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,248,320"`

### `HP DIO PRINTERONLY A4`
**Описание**: Сценарий для принтеров HP DIO формата A4.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219m!#-!4605!-#!214!#-!4585!-#!217!#-!4602&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,248,320"`

### `HP DIO AIO A3`
**Описание**: Сценарий для многофункциональных принтеров HP DIO AIO формата A3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"---------------------------------------HP DIO AIO A3--------------------------------------------"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,248"`

### `HP DIO PRINTERONLY A3`
**Описание**: Сценарий для принтеров HP DIO формата A3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"---------------------------------------HP DIO PRINTERONLY A3--------------------------------------------"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,248"`

### `HP LASER COLOR AIO A4`
**Описание**: Сценарий для цветных лазерных многофункциональных принтеров HP A4.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219m!#-!4606!##!4607!-#!214!#-!4585!-#!217!#-!4601!-#!218!#-!4604&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,319,321,322"`

### `HP LASER COLOR PRINTERONLY A4`
**Описание**: Сценарий для цветных лазерных принтеров HP A4.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219!#-!4605!-#!214!#-!4585!-#!217!#-!4601!-#!218m!#-!4604&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,319,321,323"`

### `HP LASER BW AIO A4`
**Описание**: Сценарий для черно-белых лазерных многофункциональных принтеров HP A4.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219!#-!4606!##!4607!-#!214!#-!4585!-#!217!#-!4601!-#!218m!#-!4603&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,319,324,325"`

### `HP LASER BW PRINTERONLY A4`
**Описание**: Сценарий для черно-белых лазерных принтеров HP A4.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219!#-!4605!-#!214!#-!4585!-#!217!#-!4601!-#!218m!#-!4603&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,319,324,326"`

### `HP LASER COLOR AIO A3`
**Описание**: Сценарий для цветных лазерных многофункциональных принтеров HP A3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219!#-!4606!##!4607!-#!214!#-!4584!-#!217!#-!4601!-#!218m!#-!4604&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,327,328,329"`

### `HP LASER COLOR PRINTERONLY A3`
**Описание**: Сценарий для цветных лазерных принтеров HP A3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219!#-!4605!-#!214!#-!4584!-#!217!#-!4601!-#!218m!#-!4604&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,327,328,330"`

### `HP LASER BW AIO A3`
**Описание**: Сценарий для черно-белых лазерных многофункциональных принтеров HP A3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219m!#-!4606!##!4607!-#!214!#-!4584!-#!217!#-!4601!-#!218!#-!4603&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,327,331,332"`

### `HP LASER BW PRINTERONLY A3`
**Описание**: Сценарий для черно-белых лазерных принтеров HP A3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `"https://reseller.c-data.co.il/%D7%9E%D7%93%D7%A4%D7%A1%D7%95%D7%AA#/specFilters=219m!#-!4605!-#!214!#-!4584!-#!217!#-!4601!-#!218!#-!4603&manFilters=2"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"209,249,327,331,333"`