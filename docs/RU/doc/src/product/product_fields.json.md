# `product_fields.json`

## Обзор

Этот файл содержит JSON-структуру, представляющую поля продукта.
Файл содержит различные атрибуты продукта, такие как цены, описание, названия, наличие на складе, изображения, и другие параметры.

## Содержание

- [Обзор](#обзор)
- [Описание полей](#описание-полей)
   - [`associations`](#associations)
   - [`active`](#active)
   - [`additional_delivery_times`](#additional_delivery_times)
   - [`additional_shipping_cost`](#additional_shipping_cost)
   - [`advanced_stock_management`](#advanced_stock_management)
   - [`affiliate_short_link`](#affiliate_short_link)
   - [`affiliate_summary`](#affiliate_summary)
   - [`affiliate_summary_2`](#affiliate_summary_2)
   - [`affiliate_text`](#affiliate_text)
   - [`available_date`](#available_date)
   - [`available_for_order`](#available_for_order)
   - [`available_later`](#available_later)
   - [`available_now`](#available_now)
   - [`cache_default_attribute`](#cache_default_attribute)
   - [`cache_has_attachments`](#cache_has_attachments)
   - [`cache_is_pack`](#cache_is_pack)
   - [`additional_categories_append`](#additional_categories_append)
   - [`additional_categories`](#additional_categories)
   - [`condition`](#condition)
   - [`customizable`](#customizable)
   - [`date_add`](#date_add)
   - [`date_upd`](#date_upd)
   - [`delivery_in_stock`](#delivery_in_stock)
   - [`delivery_out_stock`](#delivery_out_stock)
   - [`depth`](#depth)
   - [`description`](#description)
   - [`description_short`](#description_short)
   - [`ean13`](#ean13)
   - [`ecotax`](#ecotax)
   - [`height`](#height)
   - [`how_to_use`](#how_to_use)
   - [`id_category_default`](#id_category_default)
   - [`id_default_combination`](#id_default_combination)
   - [`id_default_image`](#id_default_image)
   - [`id_lang`](#id_lang)
   - [`id_manufacturer`](#id_manufacturer)
   - [`id_product`](#id_product)
   - [`id_shop_default`](#id_shop_default)
   - [`id_shop`](#id_shop)
   - [`id_supplier`](#id_supplier)
   - [`id_tax`](#id_tax)
   - [`id_type_redirected`](#id_type_redirected)
    - [`images_urls`](#images_urls)
   - [`indexed`](#indexed)
   - [`ingridients`](#ingridients)
   - [`is_virtual`](#is_virtual)
   - [`isbn`](#isbn)
   - [`link_rewrite`](#link_rewrite)
   - [`location`](#location)
   - [`low_stock_alert`](#low_stock_alert)
   - [`low_stock_threshold`](#low_stock_threshold)
    - [`meta_description`](#meta_description)
   - [`meta_keywords`](#meta_keywords)
   - [`meta_title`](#meta_title)
    - [`minimal_quantity`](#minimal_quantity)
   - [`mpn`](#mpn)
    - [`name`](#name)
   - [`online_only`](#online_only)
   - [`on_sale`](#on_sale)
   - [`out_of_stock`](#out_of_stock)
   - [`pack_stock_type`](#pack_stock_type)
   - [`position_in_category`](#position_in_category)
   - [`price`](#price)
   - [`product_type`](#product_type)
   - [`quantity`](#quantity)
    - [`quantity_discount`](#quantity_discount)
   - [`redirect_type`](#redirect_type)
   - [`reference`](#reference)
   - [`show_condition`](#show_condition)
   - [`show_price`](#show_price)
    - [`state`](#state)
   - [`supplier_reference`](#supplier_reference)
    - [`text_fields`](#text_fields)
   - [`unit_price_ratio`](#unit_price_ratio)
    - [`unity`](#unity)
   - [`upc`](#upc)
   - [`uploadable_files`](#uploadable_files)
    - [`default_image_url`](#default_image_url)
   - [`visibility`](#visibility)
   - [`volume`](#volume)
    - [`weight`](#weight)
   - [`wholesale_price`](#wholesale_price)
   - [`width`](#width)
    - [`affiliate_image_medium`](#affiliate_image_medium)
    - [`affiliate_image_small`](#affiliate_image_small)
    - [`delivery_additional_message`](#delivery_additional_message)

## Описание полей

### `associations`
**Описание**: null.
Указывает на связанные продукты.

### `active`
**Описание**: Числовое значение 1 или 0.
Указывает, активен ли продукт (1 - да, 0 - нет).

### `additional_delivery_times`
**Описание**: Целое число.
Дополнительное время доставки в днях.

### `additional_shipping_cost`
**Описание**: Строка, представляющая стоимость дополнительной доставки.
Дополнительная стоимость доставки.

### `advanced_stock_management`
**Описание**: Целое число 1 или 0.
Указывает, используется ли продвинутое управление запасами (1 - да, 0 - нет).

### `affiliate_short_link`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Содержит короткие ссылки для аффилиатов в разных языках.

### `affiliate_summary`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Содержит краткое описание для аффилиатов в разных языках.

### `affiliate_summary_2`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Содержит второе краткое описание для аффилиатов в разных языках.

### `affiliate_text`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Содержит текст для аффилиатов в разных языках.

### `available_date`
**Описание**: Строка, представляющая дату доступности товара.
Дата, когда товар будет доступен.

### `available_for_order`
**Описание**: Числовое значение 1 или 0.
Указывает, доступен ли продукт для заказа (1 - да, 0 - нет).

### `available_later`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Сообщение, когда товар будет доступен для заказа позже, на разных языках.

### `available_now`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Сообщение, когда товар доступен для заказа, на разных языках.

### `cache_default_attribute`
**Описание**: Строка
Идентификатор атрибута по умолчанию.

### `cache_has_attachments`
**Описание**: Строка
Указывает, есть ли вложения.

### `cache_is_pack`
**Описание**: Строка
Указывает, является ли товар набором.

### `additional_categories_append`
**Описание**: `null`.
Указывает на дополнительные категории.

### `additional_categories`
**Описание**: `null`.
Указывает на дополнительные категории.

### `condition`
**Описание**: Строка.
Состояние продукта ("new", "used", и т. д.).

### `customizable`
**Описание**: Строка.
Указывает, можно ли настроить продукт.

### `date_add`
**Описание**: Строка.
Дата добавления продукта.

### `date_upd`
**Описание**: Строка.
Дата последнего обновления продукта.

### `delivery_in_stock`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Сообщение о доставке, когда товар в наличии, на разных языках.

### `delivery_out_stock`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Сообщение о доставке, когда товара нет в наличии, на разных языках.

### `depth`
**Описание**: Строка.
Глубина продукта.

### `description`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Полное описание продукта на разных языках.

### `description_short`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Краткое описание продукта на разных языках.

### `ean13`
**Описание**: Строка.
Штрихкод EAN13.

### `ecotax`
**Описание**: Строка.
Размер эко-налога.

### `height`
**Описание**: Строка.
Высота продукта.

### `how_to_use`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Инструкции по использованию продукта на разных языках.

### `id_category_default`
**Описание**: Целое число.
Идентификатор категории по умолчанию.

### `id_default_combination`
**Описание**: Строка.
Идентификатор комбинации по умолчанию.

### `id_default_image`
**Описание**: Строка.
Идентификатор изображения по умолчанию.

### `id_lang`
**Описание**: Целое число.
Идентификатор языка.

### `id_manufacturer`
**Описание**: Строка.
Идентификатор производителя.

### `id_product`
**Описание**: Строка.
Идентификатор продукта.

### `id_shop_default`
**Описание**: Целое число.
Идентификатор магазина по умолчанию.

### `id_shop`
**Описание**: null.
Идентификатор магазина.

### `id_supplier`
**Описание**: Строка.
Идентификатор поставщика.

### `id_tax`
**Описание**: Целое число.
Идентификатор налога.

### `id_type_redirected`
**Описание**: Строка.
Идентификатор перенаправленного типа.

### `images_urls`
**Описание**: `null`.
URL-адреса изображений.

### `indexed`
**Описание**: Строка.
Указывает, проиндексирован ли продукт.

### `ingridients`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Список ингредиентов на разных языках.

### `is_virtual`
**Описание**: Числовое значение 1 или 0.
Указывает, является ли продукт виртуальным (1 - да, 0 - нет).

### `isbn`
**Описание**: Строка.
ISBN продукта.

### `link_rewrite`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Ссылка для переписывания на разных языках.

### `location`
**Описание**: Строка.
Расположение продукта.

### `low_stock_alert`
**Описание**: Строка.
Уведомление о низком уровне запасов.

### `low_stock_threshold`
**Описание**: Строка.
Порог низкого уровня запасов.

### `meta_description`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Мета-описание продукта на разных языках.

### `meta_keywords`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Мета-ключевые слова продукта на разных языках.

### `meta_title`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Мета-заголовок продукта на разных языках.

### `minimal_quantity`
**Описание**: Строка.
Минимальное количество для заказа.

### `mpn`
**Описание**: Строка.
Номер производителя.

### `name`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Название продукта на разных языках.

### `online_only`
**Описание**: Числовое значение 1 или 0.
Указывает, продается ли продукт только онлайн (1 - да, 0 - нет).

### `on_sale`
**Описание**: Строка.
Указывает, продается ли продукт со скидкой.

### `out_of_stock`
**Описание**: Целое число.
Указывает, как обрабатывать товары, которых нет в наличии.

### `pack_stock_type`
**Описание**: Строка.
Тип запаса для набора.

### `position_in_category`
**Описание**: Строка.
Позиция продукта в категории.

### `price`
**Описание**: `null`.
Цена продукта.

### `product_type`
**Описание**: Строка.
Тип продукта.

### `quantity`
**Описание**: Строка.
Количество продукта.

### `quantity_discount`
**Описание**: Строка.
Информация о скидках за количество.

### `redirect_type`
**Описание**: Строка.
Тип перенаправления.

### `reference`
**Описание**: Строка.
Артикул продукта.

### `show_condition`
**Описание**: Числовое значение 1 или 0.
Указывает, показывать ли состояние продукта (1 - да, 0 - нет).

### `show_price`
**Описание**: Числовое значение 1 или 0.
Указывает, показывать ли цену продукта (1 - да, 0 - нет).

### `state`
**Описание**: Строка.
Состояние продукта.

### `supplier_reference`
**Описание**: Строка.
Артикул поставщика.

### `text_fields`
**Описание**: Строка.
Текстовые поля.

### `unit_price_ratio`
**Описание**: Строка.
Отношение цены за единицу.

### `unity`
**Описание**: Строка.
Единица измерения.

### `upc`
**Описание**: Строка.
UPC продукта.

### `uploadable_files`
**Описание**: Строка.
Указывает, можно ли загружать файлы для продукта.

### `default_image_url`
**Описание**: `null`.
URL-адрес изображения по умолчанию.

### `visibility`
**Описание**: Целое число.
Видимость продукта.

### `volume`
**Описание**: `null`.
Объем продукта.

### `weight`
**Описание**: Строка.
Вес продукта.

### `wholesale_price`
**Описание**: Строка.
Оптовая цена продукта.

### `width`
**Описание**: Строка.
Ширина продукта.

### `affiliate_image_medium`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Медиум изображения для аффилиатов.

### `affiliate_image_small`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Маленькое изображение для аффилиатов.

### `delivery_additional_message`
**Описание**: Объект с `language`, содержащий массив объектов с атрибутами `id` и `value`.
Дополнительное сообщение о доставке на разных языках.