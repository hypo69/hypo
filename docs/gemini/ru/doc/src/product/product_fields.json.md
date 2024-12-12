# product_fields.json

## Обзор

Этот файл содержит JSON-представление структуры данных, описывающей поля продукта. Эти поля используются для хранения информации о продуктах в системе, включая их характеристики, наличие на складе, цены, описания и другие важные атрибуты.

## Оглавление

1. [Обзор](#обзор)
2. [Описание полей](#описание-полей)
    - [associations](#associations)
    - [active](#active)
    - [additional_delivery_times](#additional_delivery_times)
    - [additional_shipping_cost](#additional_shipping_cost)
    - [advanced_stock_management](#advanced_stock_management)
    - [affiliate_short_link](#affiliate_short_link)
    - [affiliate_summary](#affiliate_summary)
    - [affiliate_summary_2](#affiliate_summary_2)
    - [affiliate_text](#affiliate_text)
    - [available_date](#available_date)
    - [available_for_order](#available_for_order)
    - [available_later](#available_later)
    - [available_now](#available_now)
    - [cache_default_attribute](#cache_default_attribute)
    - [cache_has_attachments](#cache_has_attachments)
    - [cache_is_pack](#cache_is_pack)
    - [additional_categories_append](#additional_categories_append)
    - [additional_categories](#additional_categories)
    - [condition](#condition)
    - [customizable](#customizable)
    - [date_add](#date_add)
    - [date_upd](#date_upd)
    - [delivery_in_stock](#delivery_in_stock)
    - [delivery_out_stock](#delivery_out_stock)
    - [depth](#depth)
    - [description](#description)
    - [description_short](#description_short)
    - [ean13](#ean13)
    - [ecotax](#ecotax)
    - [height](#height)
    - [how_to_use](#how_to_use)
    - [id_category_default](#id_category_default)
    - [id_default_combination](#id_default_combination)
    - [id_default_image](#id_default_image)
    - [id_lang](#id_lang)
    - [id_manufacturer](#id_manufacturer)
    - [id_product](#id_product)
    - [id_shop_default](#id_shop_default)
    - [id_shop](#id_shop)
    - [id_supplier](#id_supplier)
    - [id_tax](#id_tax)
    - [id_type_redirected](#id_type_redirected)
    - [images_urls](#images_urls)
    - [indexed](#indexed)
    - [ingridients](#ingridients)
    - [is_virtual](#is_virtual)
    - [isbn](#isbn)
    - [link_rewrite](#link_rewrite)
    - [location](#location)
    - [low_stock_alert](#low_stock_alert)
    - [low_stock_threshold](#low_stock_threshold)
    - [meta_description](#meta_description)
    - [meta_keywords](#meta_keywords)
    - [meta_title](#meta_title)
    - [minimal_quantity](#minimal_quantity)
    - [mpn](#mpn)
    - [name](#name)
    - [online_only](#online_only)
    - [on_sale](#on_sale)
    - [out_of_stock](#out_of_stock)
    - [pack_stock_type](#pack_stock_type)
    - [position_in_category](#position_in_category)
    - [price](#price)
    - [product_type](#product_type)
    - [quantity](#quantity)
    - [quantity_discount](#quantity_discount)
    - [redirect_type](#redirect_type)
    - [reference](#reference)
    - [show_condition](#show_condition)
    - [show_price](#show_price)
    - [state](#state)
    - [supplier_reference](#supplier_reference)
    - [text_fields](#text_fields)
    - [unit_price_ratio](#unit_price_ratio)
    - [unity](#unity)
    - [upc](#upc)
    - [uploadable_files](#uploadable_files)
    - [default_image_url](#default_image_url)
    - [visibility](#visibility)
    - [volume](#volume)
    - [weight](#weight)
    - [wholesale_price](#wholesale_price)
    - [width](#width)
    - [affiliate_image_medium](#affiliate_image_medium)
    - [affiliate_image_small](#affiliate_image_small)
    - [delivery_additional_message](#delivery_additional_message)

## Описание полей

### `associations`
**Описание**:  Связи продукта с другими сущностями (например, категории).  В данном файле указано как `null`.

### `active`
**Описание**:  Статус активности продукта.
**Тип**:  `int` (0 или 1).
**Значение по умолчанию**: `1`.
`1` - продукт активен, `0` - продукт не активен.

### `additional_delivery_times`
**Описание**:  Дополнительное время доставки.
**Тип**:  `int`
**Значение по умолчанию**: `0`.

### `additional_shipping_cost`
**Описание**:  Дополнительная стоимость доставки.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `advanced_stock_management`
**Описание**:  Включено ли расширенное управление складом.
**Тип**:  `int` (0 или 1).
**Значение по умолчанию**: `0`.
`1` - включено, `0` - выключено.

### `affiliate_short_link`
**Описание**:  Короткая ссылка для партнерской программы.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `affiliate_summary`
**Описание**:  Краткое описание для партнерской программы.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `affiliate_summary_2`
**Описание**:  Краткое описание 2 для партнерской программы.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `affiliate_text`
**Описание**:  Текст для партнерской программы.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `available_date`
**Описание**:  Дата доступности продукта.
**Тип**:  `str`
**Формат**: `YYYY-MM-DD` или пустая строка.
**Значение по умолчанию**: `""`.

### `available_for_order`
**Описание**:  Доступен ли продукт для заказа.
**Тип**:  `int` (0 или 1).
**Значение по умолчанию**: `1`.
`1` - доступен, `0` - не доступен.

### `available_later`
**Описание**:  Сообщение о доступности продукта позже.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `available_now`
**Описание**:  Сообщение о доступности продукта сейчас.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": 1
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": 1
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": 1
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `cache_default_attribute`
**Описание**: Кеш для атрибута по умолчанию.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `cache_has_attachments`
**Описание**: Кеш для наличия вложений.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `cache_is_pack`
**Описание**: Кеш для обозначения, является ли продукт упаковкой.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `additional_categories_append`
**Описание**: Дополнительные категории, к которым добавляется продукт.
**Тип**: `null`
**Значение по умолчанию**: `null`.

### `additional_categories`
**Описание**:  Дополнительные категории продукта.
**Тип**: `null`
**Значение по умолчанию**: `null`.

### `condition`
**Описание**: Состояние продукта (например, новый, б/у).
**Тип**:  `str`
**Значение по умолчанию**: `"new"`.

### `customizable`
**Описание**: Указывает, настраиваемый ли продукт.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `date_add`
**Описание**: Дата добавления продукта.
**Тип**:  `str`
**Формат**: `YYYY-MM-DD HH:MM:SS` или пустая строка.
**Значение по умолчанию**: `""`.

### `date_upd`
**Описание**:  Дата обновления продукта.
**Тип**:  `str`
**Формат**: `YYYY-MM-DD HH:MM:SS` или пустая строка.
**Значение по умолчанию**: `""`.

### `delivery_in_stock`
**Описание**:  Сообщение о доставке продукта в наличии.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": false
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": false
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": false
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `delivery_out_stock`
**Описание**: Сообщение о доставке продукта не в наличии.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": "\\u05d4\\u05de\\u05dc\\u05d0\\u05d9 \\u05d0\\u05d6\\u05dc"
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": "\\u05d4\\u05de\\u05dc\\u05d0\\u05d9 \\u05d0\\u05d6\\u05dc"
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": "\\u05d4\\u05de\\u05dc\\u05d0\\u05d9 \\u05d0\\u05d6\\u05dc"
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `depth`
**Описание**: Глубина продукта.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `description`
**Описание**:  Полное описание продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `description_short`
**Описание**:  Краткое описание продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `ean13`
**Описание**:  Штрих-код EAN13.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `ecotax`
**Описание**:  Экологический налог.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `height`
**Описание**:  Высота продукта.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `how_to_use`
**Описание**:  Инструкция по применению продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `id_category_default`
**Описание**:  ID категории по умолчанию.
**Тип**:  `int`
**Значение по умолчанию**: `2`.

### `id_default_combination`
**Описание**:  ID комбинации по умолчанию.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `id_default_image`
**Описание**:  ID изображения по умолчанию.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `id_lang`
**Описание**:  ID языка.
**Тип**: `int`
**Значение по умолчанию**: `1`.

### `id_manufacturer`
**Описание**: ID производителя.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `id_product`
**Описание**: ID продукта.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `id_shop_default`
**Описание**: ID магазина по умолчанию.
**Тип**: `int`
**Значение по умолчанию**: `1`.

### `id_shop`
**Описание**:  ID магазина.
**Тип**: `null`
**Значение по умолчанию**: `null`.

### `id_supplier`
**Описание**: ID поставщика.
**Тип**:  `str`
**Значение по умолчанию**: `"11267"`.

### `id_tax`
**Описание**: ID налога.
**Тип**: `int`
**Значение по умолчанию**: `13`.

### `id_type_redirected`
**Описание**: ID типа редиректа.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `images_urls`
**Описание**:  URL-адреса изображений продукта.
**Тип**: `null`
**Значение по умолчанию**: `null`.

### `indexed`
**Описание**:  Указывает, индексирован ли продукт для поиска.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `ingridients`
**Описание**:  Ингредиенты продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `is_virtual`
**Описание**:  Указывает, является ли продукт виртуальным.
**Тип**: `int`
**Значение по умолчанию**: `0`.
`1` - виртуальный, `0` - физический.

### `isbn`
**Описание**: ISBN код продукта.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `link_rewrite`
**Описание**:  URL-имя продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `location`
**Описание**:  Местоположение продукта.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `low_stock_alert`
**Описание**:  Уведомление о низком остатке на складе.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `low_stock_threshold`
**Описание**:  Порог низкого остатка на складе.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `meta_description`
**Описание**:  Meta-описание продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `meta_keywords`
**Описание**:  Meta-ключевые слова продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `meta_title`
**Описание**:  Meta-заголовок продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `minimal_quantity`
**Описание**:  Минимальное количество для заказа.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `mpn`
**Описание**:  Номер производителя.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `name`
**Описание**:  Название продукта.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `online_only`
**Описание**:  Доступен ли продукт только онлайн.
**Тип**: `int`
**Значение по умолчанию**: `1`.
`1` - только онлайн, `0` - также в обычных магазинах.

### `on_sale`
**Описание**:  Указывает, является ли продукт акционным.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `out_of_stock`
**Описание**:  Статус наличия на складе.
**Тип**: `int`
**Значение по умолчанию**: `0`.

### `pack_stock_type`
**Описание**:  Тип управления запасами для упаковки.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `position_in_category`
**Описание**:  Позиция продукта в категории.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `price`
**Описание**:  Цена продукта.
**Тип**: `null`
**Значение по умолчанию**: `null`.

### `product_type`
**Описание**:  Тип продукта.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `quantity`
**Описание**:  Количество продукта в наличии.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `quantity_discount`
**Описание**:  Скидки в зависимости от количества.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `redirect_type`
**Описание**:  Тип переадресации.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `reference`
**Описание**:  Уникальный артикул продукта.
**Тип**:  `str`
**Значение по умолчанию**: `"11267-389"`.

### `show_condition`
**Описание**:  Показывать ли условие продукта.
**Тип**:  `int`
**Значение по умолчанию**: `1`.
`1` - показывать, `0` - не показывать.

### `show_price`
**Описание**:  Показывать ли цену продукта.
**Тип**: `int`
**Значение по умолчанию**: `1`.
`1` - показывать, `0` - не показывать.

### `state`
**Описание**:  Состояние продукта.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `supplier_reference`
**Описание**: Артикул поставщика.
**Тип**:  `str`
**Значение по умолчанию**: `"389"`.

### `text_fields`
**Описание**: Текстовые поля.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `unit_price_ratio`
**Описание**:  Соотношение цены за единицу.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `unity`
**Описание**: Единица измерения.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `upc`
**Описание**: Штрих-код UPC.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `uploadable_files`
**Описание**:  Возможность загрузки файлов для продукта.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `default_image_url`
**Описание**:  URL изображения по умолчанию.
**Тип**: `null`
**Значение по умолчанию**: `null`.

### `visibility`
**Описание**:  Видимость продукта.
**Тип**:  `int`
**Значение по умолчанию**: `1`.

### `volume`
**Описание**: Объем продукта.
**Тип**:  `null`
**Значение по умолчанию**: `null`.

### `weight`
**Описание**: Вес продукта.
**Тип**: `str`
**Значение по умолчанию**: `""`.

### `wholesale_price`
**Описание**: Оптовая цена.
**Тип**:  `str`
**Значение по умолчанию**: `"False"`.

### `width`
**Описание**: Ширина продукта.
**Тип**:  `str`
**Значение по умолчанию**: `""`.

### `affiliate_image_medium`
**Описание**: Среднее изображение для партнерской программы.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `affiliate_image_small`
**Описание**:  Маленькое изображение для партнерской программы.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.

### `delivery_additional_message`
**Описание**: Дополнительное сообщение о доставке.
**Тип**: `object`
**Структура**:
```json
{
    "language": [
        {
            "attrs": {
                "id": "1"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "2"
            },
            "value": ""
        },
        {
            "attrs": {
                "id": "3"
            },
            "value": ""
        }
    ]
}
```
**Описание**:  Содержит значения для разных языков.