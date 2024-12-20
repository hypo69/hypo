# Схема API для продукта PrestaShop

## Обзор

Данный документ описывает структуру JSON-схемы для продукта в PrestaShop API. Эта схема определяет поля и структуру данных, используемых для представления информации о продукте.

## Содержание

- [Обзор](#обзор)
- [Описание полей](#описание-полей)
  - [product](#product)
    - [Основные параметры](#основные-параметры)
    - [Языковые параметры](#языковые-параметры)
      - [delivery_in_stock](#delivery_in_stock)
      - [delivery_out_stock](#delivery_out_stock)
      - [meta_description](#meta_description)
      - [meta_keywords](#meta_keywords)
      - [meta_title](#meta_title)
      - [link_rewrite](#link_rewrite)
      - [name](#name)
      - [description](#description)
      - [description_short](#description_short)
      - [available_now](#available_now)
      - [available_later](#available_later)
      - [affiliate_short_link](#affiliate_short_link)
      - [affiliate_text](#affiliate_text)
      - [affiliate_summary](#affiliate_summary)
      - [affiliate_summary_2](#affiliate_summary_2)
    - [Ассоциации](#ассоциации)
      - [categories](#categories)
      - [images](#images)
      - [combinations](#combinations)
      - [product_option_values](#product_option_values)
      - [product_features](#product_features)
      - [tags](#tags)
      - [stock_availables](#stock_availables)
      - [attachments](#attachments)
      - [accessories](#accessories)
      - [product_bundle](#product_bundle)

## Описание полей

### `product`

Корневой элемент, содержащий всю информацию о продукте.

#### Основные параметры

- `id` (str): Идентификатор продукта.
- `id_manufacturer` (str): Идентификатор производителя.
- `id_supplier` (str): Идентификатор поставщика.
- `id_category_default` (str): Идентификатор категории по умолчанию.
- `new` (str): Является ли продукт новым.
- `cache_default_attribute` (str): Кешированный идентификатор атрибута по умолчанию.
- `id_default_image` (str): Идентификатор изображения по умолчанию.
- `id_default_combination` (str): Идентификатор комбинации по умолчанию.
- `id_tax` (str): Идентификатор налога.
- `position_in_category` (str): Позиция продукта в категории.
- `type` (str): Тип продукта.
- `id_shop_default` (str): Идентификатор магазина по умолчанию.
- `reference` (str): Артикул.
- `supplier_reference` (str): Артикул поставщика.
- `location` (str): Местоположение.
- `width` (str): Ширина.
- `height` (str): Высота.
- `depth` (str): Глубина.
- `weight` (str): Вес.
- `quantity_discount` (str): Наличие скидки по количеству.
- `ean13` (str): EAN13 код.
- `isbn` (str): ISBN код.
- `upc` (str): UPC код.
- `mpn` (str): MPN код.
- `cache_is_pack` (str): Является ли продукт набором.
- `cache_has_attachments` (str): Имеет ли продукт вложения.
- `is_virtual` (str): Является ли продукт виртуальным.
- `state` (str): Состояние продукта.
- `additional_delivery_times` (str): Дополнительное время доставки.
- `product_type` (str): Тип продукта.
- `on_sale` (str): Находится ли продукт в продаже.
- `online_only` (str): Продается ли продукт только онлайн.
- `ecotax` (str): Эко налог.
- `minimal_quantity` (str): Минимальное количество для заказа.
- `low_stock_threshold` (str): Порог низкого запаса.
- `low_stock_alert` (str): Оповещение о низком запасе.
- `price` (str): Цена.
- `wholesale_price` (str): Оптовая цена.
- `unity` (str): Единица измерения.
- `unit_price_ratio` (str): Коэффициент цены за единицу.
- `additional_shipping_cost` (str): Дополнительная стоимость доставки.
- `customizable` (str): Возможность настройки.
- `text_fields` (str): Количество текстовых полей.
- `uploadable_files` (str): Количество загружаемых файлов.
- `active` (str): Активность продукта.
- `redirect_type` (str): Тип перенаправления.
- `id_type_redirected` (str): Идентификатор перенаправленного типа.
- `available_for_order` (str): Доступен ли продукт для заказа.
- `available_date` (str): Дата доступности.
- `show_condition` (str): Отображать ли состояние.
- `condition` (str): Состояние.
- `show_price` (str): Отображать ли цену.
- `indexed` (str): Индексирован ли продукт.
- `visibility` (str): Видимость продукта.
- `advanced_stock_management` (str): Расширенное управление запасами.
- `date_add` (str): Дата добавления.
- `date_upd` (str): Дата обновления.
- `pack_stock_type` (str): Тип управления запасами для набора.

#### Языковые параметры

##### `delivery_in_stock`

Текст доставки при наличии на складе.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `delivery_out_stock`

Текст доставки при отсутствии на складе.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `meta_description`

Мета-описание продукта.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `meta_keywords`

Мета-ключевые слова продукта.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `meta_title`

Мета-заголовок продукта.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `link_rewrite`

Ссылка на продукт.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `name`

Название продукта.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `description`

Полное описание продукта.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `description_short`

Краткое описание продукта.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `available_now`

Текст доступности в данный момент.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `available_later`

Текст доступности позже.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `affiliate_short_link`

Короткая партнерская ссылка.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `affiliate_text`

Партнерский текст.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `affiliate_summary`

Партнерский краткий обзор.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

##### `affiliate_summary_2`

Второй партнерский краткий обзор.

- `language` (list): Список объектов, каждый из которых содержит текст для конкретного языка.
    - `attrs` (dict): Атрибуты объекта.
        - `id` (str): Идентификатор языка.
    - `value` (str): Текстовое значение для данного языка.

#### Ассоциации

##### `categories`

Категории, к которым принадлежит продукт.

- `category` (list): Список объектов, каждый из которых содержит идентификатор категории.
    - `id` (str): Идентификатор категории.

##### `images`

Изображения продукта.

- `image` (dict): Объект, содержащий идентификатор изображения.
    - `id` (str): Идентификатор изображения.

##### `combinations`

Комбинации продукта.

- `combination` (dict): Объект, содержащий идентификатор комбинации.
    - `id` (str): Идентификатор комбинации.

##### `product_option_values`

Значения опций продукта.

- `product_option_value` (dict): Объект, содержащий идентификатор значения опции продукта.
  - `id` (str): Идентификатор значения опции продукта.

##### `product_features`

Характеристики продукта.

- `product_feature` (dict): Объект, содержащий идентификатор характеристики продукта и значение характеристики.
    - `id` (str): Идентификатор характеристики продукта.
    - `id_feature_value` (str): Идентификатор значения характеристики.

##### `tags`

Теги продукта.

- `tag` (dict): Объект, содержащий идентификатор тега.
    - `id` (str): Идентификатор тега.

##### `stock_availables`

Доступность на складе.

- `stock_available` (dict): Объект, содержащий идентификатор доступности на складе и идентификатор атрибута продукта.
  - `id` (str): Идентификатор доступности на складе.
  - `id_product_attribute` (str): Идентификатор атрибута продукта.

##### `attachments`

Вложения продукта.

- `attachment` (dict): Объект, содержащий идентификатор вложения.
    - `id` (str): Идентификатор вложения.

##### `accessories`

Аксессуары продукта.

- `product` (dict): Объект, содержащий идентификатор аксессуара продукта.
    - `id` (str): Идентификатор аксессуара продукта.

##### `product_bundle`

Наборы продуктов.

- `product` (dict): Объект, содержащий идентификатор продукта в наборе, идентификатор атрибута продукта и количество.
  - `id` (str): Идентификатор продукта в наборе.
  - `id_product_attribute` (str): Идентификатор атрибута продукта.
  - `quantity` (str): Количество продукта в наборе.