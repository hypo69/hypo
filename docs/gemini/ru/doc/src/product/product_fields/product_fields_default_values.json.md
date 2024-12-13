# Документация по файлу `product_fields_default_values.json`

## Обзор

Данный файл содержит JSON-структуру, представляющую собой набор полей и их значений по умолчанию для сущности "продукт". Он используется для определения структуры и начальных значений полей продукта в системе. Файл описывает структуру JSON объекта и не содержит исполняемого кода.

## Оглавление

1. [Структура JSON](#структура-json)
2. [Описание полей](#описание-полей)
    - [Основные атрибуты](#основные-атрибуты)
    - [Атрибуты ассоциаций](#атрибуты-ассоциаций)
    - [Атрибуты для наличия](#атрибуты-для-наличия)
    - [Настройки доставки и наличия](#настройки-доставки-и-наличия)
    - [Описание и характеристики](#описание-и-характеристики)
    - [Идентификаторы](#идентификаторы)
    - [Связанные настройки](#связанные-настройки)
    - [SEO и контент](#seo-и-контент)
    - [Настройки цен и количества](#настройки-цен-и-количества)
    - [Настройки отображения](#настройки-отображения)
    - [Размеры и вес](#размеры-и-вес)

## Структура JSON

Файл представляет собой JSON-объект, который содержит пары "ключ-значение", где ключи - это названия полей продукта, а значения - их значения по умолчанию.

```json
{
  "available_now": "",
  "available_later": "",
  "affiliate_short_link": "",
  "affiliate_text": "",
  "affiliate_summary": "",
  "affiliate_summary_2": "",
  "affiliate_image_large": "",
  "affiliate_image_medium": "",
  "affiliate_image_small": "",
  "active": 1,
  "additional_delivery_times": "",
  "additional_shipping_cost": "",
  "advanced_stock_management": "0",
  "associations": {
    "categories": {
      "category": [
        {
          "id": "2"
        }
      ]
    },
    "images": {
      "image": [
        {
          "id": ""
        }
      ]
    },
    "combinations": {
      "combination": {
        "id": ""
      }
    },
    "product_option_values": {
      "product_option_value": {
        "id": ""
      }
    },
    "product_features": {
      "product_feature": {
        "id": "",
        "id_feature_value": ""
      }
    },
    "tags": {
      "tag": {
        "id": ""
      }
    },
    "stock_availables": {
      "stock_available": [
        {
          "id": "",
          "id_product_attribute": ""
        }
      ]
    },
    "attachments": {
      "attachment": {
        "id": ""
      }
    },
    "accessories": {
      "product": {
        "id": ""
      }
    },
    "product_bundle": {
      "product": {
        "id": "",
        "id_product_attribute": "",
        "quantity": ""
      }
    }
  },
  "available_date": "",
  "available_for_order": 1,
  "cache_default_attribute": "",
  "cache_has_attachments": "",
  "cache_is_pack": "",
  "condition": "new",
  "customizable": "",
  "date_add": "",
  "date_upd": "",
  "default_image_url": "",
  "images_urls": "",
  "delivery_additional_message": "",
  "delivery_in_stock": "",
  "delivery_out_stock": "",
  "depth": "",
  "description": "",
  "description_short": "",
  "ean13": "",
  "ecotax": "",
  "height": "",
  "id_category_default": 2,
  "id_default_combination": "",
  "id_default_image": "",
  "id_lang": 1,
  "id_manufacturer": "",
  "id_product": "",
  "id_shop": 1,
  "id_shop_default": 1,
  "id_supplier": "",
  "id_tax": 13,
  "id_type_redirected": "",
  "indexed": "",
  "is_virtual": 0,
  "isbn": "",
  "locale": "",
  "location": "",
  "low_stock_alert": "",
  "low_stock_threshold": "",
  "meta_description": "",
  "meta_keywords": "",
  "meta_title": "",
  "link_rewrite": "",
  "name": "",
  "ingredients": "",
  "how_to_use": "",
  "specification": "",
  "minimal_quantity": 1,
  "mpn": "",
  "on_sale": 1,
  "online_only": 0,
  "out_of_stock": "",
  "pack_stock_type": "",
  "position_in_category": "",
  "price": "",
  "product_type": "standard",
  "quantity_discount": "",
  "redirect_type": "",
  "reference": "",
  "show_condition": 1,
  "show_price": 1,
  "state": 1,
  "supplier_reference": "",
  "text_fields": "",
  "unit_price_ratio": "",
  "unity": "",
  "upc": "",
  "uploadable_files": "",
  "visibility": 1,
  "volume": "",
  "weight": "",
  "wholesale_price": "",
  "width": ""
}
```
## Описание полей

### Основные атрибуты

*   `available_now` (string): Текст, отображаемый, когда товар в наличии.
*   `available_later` (string): Текст, отображаемый, когда товара нет в наличии, но он будет доступен.
*   `affiliate_short_link` (string): Короткая партнерская ссылка.
*   `affiliate_text` (string): Партнерский текст.
*   `affiliate_summary` (string): Партнерское описание.
*   `affiliate_summary_2` (string): Второе партнерское описание.
*   `affiliate_image_large` (string): URL большого партнерского изображения.
*   `affiliate_image_medium` (string): URL среднего партнерского изображения.
*   `affiliate_image_small` (string): URL маленького партнерского изображения.
*    `active` (integer): Флаг активности продукта (1 - активен, 0 - неактивен).
*    `additional_delivery_times` (string): Дополнительное время доставки.
*    `additional_shipping_cost` (string): Дополнительная стоимость доставки.
*    `advanced_stock_management` (string): Флаг использования расширенного управления запасами.

### Атрибуты ассоциаций
*  `associations` (object): Объект, содержащий ассоциации продукта с другими сущностями.
    * `categories` (object): Ассоциации с категориями.
        * `category` (array): Массив категорий, к которым привязан продукт.
            * `id` (string): ID категории.
    *   `images` (object): Ассоциации с изображениями.
        *   `image` (array): Массив изображений, связанных с продуктом.
            *   `id` (string): ID изображения.
    *   `combinations` (object): Ассоциации с комбинациями продукта.
        *   `combination` (object): Объект комбинации продукта.
            *    `id` (string): ID комбинации.
    *   `product_option_values` (object): Ассоциации со значениями опций продукта.
        *  `product_option_value` (object): Объект значения опции продукта.
            *   `id` (string): ID значения опции.
    *   `product_features` (object): Ассоциации со свойствами продукта.
        *    `product_feature` (object): Объект свойства продукта.
            *   `id` (string): ID свойства продукта.
            *    `id_feature_value` (string): ID значения свойства продукта.
    *   `tags` (object): Ассоциации с тегами.
        *   `tag` (object): Объект тега.
            *   `id` (string): ID тега.
    *  `stock_availables` (object): Ассоциации с доступностью запасов.
        *   `stock_available` (array): Массив доступности запасов.
             *   `id` (string): ID доступности запасов.
             *    `id_product_attribute` (string): ID атрибута продукта.
     *   `attachments` (object): Ассоциации с прикрепленными файлами.
        *   `attachment` (object): Объект прикрепленного файла.
            *  `id` (string): ID прикрепленного файла.
    *  `accessories` (object): Ассоциации с аксессуарами.
        *   `product` (object): Объект аксессуара.
            * `id` (string): ID аксессуара.
    *  `product_bundle` (object): Ассоциации с комплектами продуктов.
        *  `product` (object): Объект продукта в комплекте.
            *  `id` (string): ID продукта в комплекте.
            *  `id_product_attribute` (string): ID атрибута продукта в комплекте.
            *  `quantity` (string): Количество продукта в комплекте.

### Атрибуты для наличия
*   `available_date` (string): Дата доступности продукта.
*    `available_for_order` (integer): Флаг доступности для заказа (1 - доступен, 0 - нет).
*    `cache_default_attribute` (string): Кэш атрибута по умолчанию.
*    `cache_has_attachments` (string): Кэш наличия прикрепленных файлов.
*   `cache_is_pack` (string): Кэш, является ли продукт набором.
### Настройки доставки и наличия
*   `condition` (string): Состояние продукта ("new", "used", "refurbished").
*    `customizable` (string): Флаг возможности кастомизации продукта.
*   `date_add` (string): Дата добавления продукта.
*    `date_upd` (string): Дата обновления продукта.
*    `default_image_url` (string): URL изображения по умолчанию.
*    `images_urls` (string): URL изображений продукта.
*   `delivery_additional_message` (string): Дополнительное сообщение о доставке.
*   `delivery_in_stock` (string): Сообщение о доставке при наличии на складе.
*   `delivery_out_stock` (string): Сообщение о доставке при отсутствии на складе.
### Описание и характеристики
*    `depth` (string): Глубина продукта.
*   `description` (string): Полное описание продукта.
*    `description_short` (string): Краткое описание продукта.
*   `ean13` (string): EAN13 штрихкод.
*    `ecotax` (string): Эко налог.
*    `height` (string): Высота продукта.
### Идентификаторы
*   `id_category_default` (integer): ID категории по умолчанию.
*   `id_default_combination` (string): ID комбинации по умолчанию.
*    `id_default_image` (string): ID изображения по умолчанию.
*    `id_lang` (integer): ID языка.
*    `id_manufacturer` (string): ID производителя.
*    `id_product` (string): ID продукта.
*   `id_shop` (integer): ID магазина.
*   `id_shop_default` (integer): ID магазина по умолчанию.
*    `id_supplier` (string): ID поставщика.
*   `id_tax` (integer): ID налога.
*   `id_type_redirected` (string): ID типа перенаправления.
### Связанные настройки
*   `indexed` (string): Флаг индексации.
*    `is_virtual` (integer): Флаг, является ли продукт виртуальным (1 - да, 0 - нет).
*   `isbn` (string): ISBN код.
*   `locale` (string): Локаль продукта.
*    `location` (string): Местоположение продукта на складе.
*   `low_stock_alert` (string): Флаг предупреждения о низком запасе.
*   `low_stock_threshold` (string): Порог низкого запаса.
### SEO и контент
*    `meta_description` (string): Мета-описание продукта.
*    `meta_keywords` (string): Мета-ключевые слова продукта.
*   `meta_title` (string): Мета-заголовок продукта.
*   `link_rewrite` (string): ЧПУ для URL.
*    `name` (string): Название продукта.
*    `ingredients` (string): Состав продукта.
*    `how_to_use` (string): Инструкция по применению.
*    `specification` (string): Спецификация продукта.
### Настройки цен и количества
*    `minimal_quantity` (integer): Минимальное количество для заказа.
*    `mpn` (string): MPN код.
*   `on_sale` (integer): Флаг, находится ли товар на распродаже (1 - да, 0 - нет).
*    `online_only` (integer): Флаг, продается ли товар только онлайн (1 - да, 0 - нет).
*   `out_of_stock` (string): Обработка товара, которого нет в наличии.
*    `pack_stock_type` (string): Тип управления запасами для набора товаров.
*    `position_in_category` (string): Позиция товара в категории.
*   `price` (string): Цена продукта.
### Настройки отображения
*    `product_type` (string): Тип продукта ("standard", "pack", "virtual").
*    `quantity_discount` (string): Информация о скидках за количество.
*    `redirect_type` (string): Тип перенаправления.
*    `reference` (string): Артикул продукта.
*   `show_condition` (integer): Флаг, показывать ли состояние продукта (1 - да, 0 - нет).
*    `show_price` (integer): Флаг, показывать ли цену продукта (1 - да, 0 - нет).
*   `state` (integer): Состояние продукта (1 - включен, 0 - выключен).
*    `supplier_reference` (string): Артикул поставщика.
### Размеры и вес
*   `text_fields` (string): Текстовые поля.
*    `unit_price_ratio` (string): Коэффициент цены за единицу.
*    `unity` (string): Единица измерения.
*   `upc` (string): UPC код.
*   `uploadable_files` (string): Флаг загружаемых файлов.
*    `visibility` (integer): Видимость продукта (1 - виден, 0 - скрыт).
*   `volume` (string): Объем продукта.
*    `weight` (string): Вес продукта.
*    `wholesale_price` (string): Оптовая цена продукта.
*    `width` (string): Ширина продукта.