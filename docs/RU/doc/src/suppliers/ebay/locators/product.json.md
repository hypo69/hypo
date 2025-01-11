# Описание локаторов для продукта eBay

## Обзор

Этот файл `product.json` содержит определения локаторов для извлечения данных о продуктах с веб-сайта eBay. Локаторы определены в формате JSON и используются для автоматизации процесса сбора данных о продуктах, таких как их характеристики, цены, описания и т.д.

## Содержание

- [Локаторы](#локаторы)
    - [`id`](#id)
    - [`id_manufacturer`](#id_manufacturer)
    - [`id_supplier`](#id_supplier)
    - [`id_category_default`](#id_category_default)
    - [`new`](#new)
    - [`cache_default_attribute`](#cache_default_attribute)
    - [`id_default_image`](#id_default_image)
    - [`id_default_combination`](#id_default_combination)
    - [`id_tax`](#id_tax)
    - [`position_in_category`](#position_in_category)
    - [`type`](#type)
    - [`id_shop_default`](#id_shop_default)
    - [`reference`](#reference)
    - [`supplier_reference`](#supplier_reference)
    - [`location`](#location)
    - [`width`](#width)
    - [`height`](#height)
    - [`depth`](#depth)
    - [`weight`](#weight)
    - [`quantity_discount`](#quantity_discount)
    - [`ean13`](#ean13)
    - [`isbn`](#isbn)
    - [`upc`](#upc)
    - [`mpn`](#mpn)
    - [`cache_is_pack`](#cache_is_pack)
    - [`cache_has_attachments`](#cache_has_attachments)
    - [`is_virtual`](#is_virtual)
    - [`state`](#state)
    - [`additional_delivery_times`](#additional_delivery_times)
    - [`delivery_in_stock`](#delivery_in_stock)
    - [`delivery_out_stock`](#delivery_out_stock)
    - [`product_type`](#product_type)
    - [`on_sale`](#on_sale)
    - [`online_only`](#online_only)
    - [`ecotax`](#ecotax)
    - [`minimal_quantity`](#minimal_quantity)
    - [`low_stock_threshold`](#low_stock_threshold)
    - [`low_stock_alert`](#low_stock_alert)
    - [`price`](#price)
    - [`wholesale_price`](#wholesale_price)
    - [`unity`](#unity)
    - [`unit_price_ratio`](#unit_price_ratio)
    - [`additional_shipping_cost`](#additional_shipping_cost)
    - [`customizable`](#customizable)
    - [`text_fields`](#text_fields)
    - [`uploadable_files`](#uploadable_files)
    - [`active`](#active)
    - [`redirect_type`](#redirect_type)
    - [`id_type_redirected`](#id_type_redirected)
    - [`available_for_order`](#available_for_order)
    - [`available_date`](#available_date)
    - [`show_condition`](#show_condition)
    - [`condition`](#condition)
    - [`show_price`](#show_price)
    - [`indexed`](#indexed)
    - [`visibility`](#visibility)
    - [`advanced_stock_management`](#advanced_stock_management)
    - [`date_add`](#date_add)
    - [`date_upd`](#date_upd)
    - [`pack_stock_type`](#pack_stock_type)
    - [`meta_description`](#meta_description)
    - [`meta_keywords`](#meta_keywords)
    - [`meta_title`](#meta_title)
    - [`link_rewrite`](#link_rewrite)
    - [`name`](#name)
    - [`description`](#description)
    - [`description_short`](#description_short)
    - [`specification`](#specification)
    - [`affiliate_short_link`](#affiliate_short_link)
    - [`affiliate_text`](#affiliate_text)
    - [`affiliate_summary`](#affiliate_summary)
    - [`affiliate_summary_2`](#affiliate_summary_2)
    - [`available_now`](#available_now)
    - [`available_later`](#available_later)
     - [`associations`](#associations)
    - [`ASIN`](#asin)
    - [`Active (0/1)`](#active_0_1)
    - [`Name*`](#name)
    - [`Categories (x,y,z...)`](#categories_x_y_z)
    - [`Price tax excluded`](#price_tax_excluded)
    - [`Price tax included`](#price_tax_included)
    - [`Tax rule ID`](#tax_rule_id)
    - [`Cost price`](#cost_price)
    - [`On sale (0/1)`](#on_sale_0_1)
    - [`Discount amount`](#discount_amount)
    - [`Discount percent`](#discount_percent)
    - [`Discount from (yyyy-mm-dd)`](#discount_from_yyyy_mm_dd)
    - [`Discount to (yyyy-mm-dd)`](#discount_to_yyyy_mm_dd)
    - [`reference #`](#reference_number)
    - [`Supplier reference #`](#supplier_reference_number)
    - [`Supplier`](#supplier)
    - [`Brand`](#brand)
    - [`EAN13`](#ean13_1)
    - [`UPC`](#upc_1)
    - [`MPN`](#mpn_1)
    - [`Ecotax`](#ecotax_1)
    - [`Width`](#width_1)
    - [`Height`](#height_1)
    - [`Depth`](#depth_1)
    - [`Weight`](#weight_1)
    - [`Delivery time of in-stock products:`](#delivery_time_of_in_stock_products)
    - [`Delivery time of out-of-stock products with allowed orders:`](#delivery_time_of_out_of_stock_products_with_allowed_orders)
    - [`Quantity`](#quantity)
    - [`Minimal quantity`](#minimal_quantity_1)
    - [`Low stock level`](#low_stock_level)
    - [`Send me an email when the quantity is under this level`](#send_me_an_email_when_the_quantity_is_under_this_level)
    - [`Visibility`](#visibility_1)
    - [`Additional shipping cost`](#additional_shipping_cost_1)
    - [`Unit for base price`](#unit_for_base_price)
    - [`Base price`](#base_price)
    - [`Summary`](#summary)
    - [`Description`](#description_1)
    - [`Tags (x,y,z...)`](#tags_x_y_z)
    - [`Meta title`](#meta_title_1)
    - [`Meta keywords`](#meta_keywords_1)
    - [`Meta description`](#meta_description_1)
    - [`Rewritten URL`](#rewritten_url)
    - [`Label when in stock`](#label_when_in_stock)
    - [`Label when backorder allowed`](#label_when_backorder_allowed)
    - [`Available for order (0 = No, 1 = Yes)`](#available_for_order_0_no_1_yes)
    - [`Product availability date`](#product_availability_date)
    - [`Product creation date`](#product_creation_date)
    - [`Show price (0 = No, 1 = Yes)`](#show_price_0_no_1_yes)
    - [`Screenshot`](#screenshot)
    - [`additional_images_urls`](#additional_images_urls)
    - [`additional_images_alts`](#additional_images_alts)
    - [`Delete existing images (0 = No, 1 = Yes)`](#delete_existing_images_0_no_1_yes)
    - [`Feature (Name:Value:Position:Customized)`](#feature_name_value_position_customized)
     - [`Available online only (0 = No, 1 = Yes)`](#available_online_only_0_no_1_yes)
    - [`Condition`](#condition_1)
    - [`Customizable (0 = No, 1 = Yes)`](#customizable_0_no_1_yes)
    - [`Uploadable files (0 = No, 1 = Yes)`](#uploadable_files_0_no_1_yes)
    - [`Text fields (0 = No, 1 = Yes)`](#text_fields_0_no_1_yes)
    - [`Action when out of stock`](#action_when_out_of_stock)
    - [`Virtual product (0 = No, 1 = Yes)`](#virtual_product_0_no_1_yes)
    - [`File URL`](#file_url)
    - [`Number of allowed downloads`](#number_of_allowed_downloads)
    - [`Expiration date (yyyy-mm-dd)`](#expiration_date_yyyy_mm_dd)
    - [`Number of days`](#number_of_days)
     - [`ID / Name of shop`](#id_name_of_shop)
    - [`Advanced Stock Management`](#advanced_stock_management_1)
    - [`Depends on stock`](#depends_on_stock)
    - [`Warehouse`](#warehouse)
    - [`Accessories (x,y,z...)`](#accessories_x_y_z)
     - [`affiliate short link`](#affiliate_short_link_1)
    - [`affiliate text`](#affiliate_text_1)
    - [`affiliate summary`](#affiliate_summary_1)
    - [`affiliate summary 2`](#affiliate_summary_2_1)
    - [`Open AI Product Description`](#open_ai_product_description)
    - [`Byer protection`](#byer_protection)
    - [`Specification`](#specification_1)
    - [`Refirbished product description`](#refirbished_product_description)
    - [`Additional shipping details`](#additional_shipping_details)

## Локаторы

### `id`

**Описание**: Локатор для идентификатора продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_manufacturer`

**Описание**: Локатор для идентификатора производителя продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_supplier`

**Описание**: Локатор для идентификатора поставщика.

**Параметры**:

- `attribute` (int): Атрибут `2792`.
- `by` (str): Метод поиска `VALUE`.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_category_default`

**Описание**: Локатор для идентификатора категории по умолчанию.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `new`

**Описание**: Локатор для определения, является ли продукт новым.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `cache_default_attribute`

**Описание**: Локатор для кешированного атрибута по умолчанию.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_default_image`

**Описание**: Локатор для идентификатора изображения по умолчанию.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_default_combination`

**Описание**: Локатор для идентификатора комбинации по умолчанию.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_tax`

**Описание**: Локатор для идентификатора налога.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `position_in_category`

**Описание**: Локатор для позиции продукта в категории.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `type`

**Описание**: Локатор для типа продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `id_shop_default`

**Описание**: Локатор для идентификатора магазина по умолчанию.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `reference`

**Описание**: Локатор для артикула продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `supplier_reference`

**Описание**: Локатор для артикула поставщика.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `location`

**Описание**: Локатор для местоположения продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `width`

**Описание**: Локатор для ширины продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `height`

**Описание**: Локатор для высоты продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `depth`

**Описание**: Локатор для глубины продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `weight`

**Описание**: Локатор для веса продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `quantity_discount`

**Описание**: Локатор для определения наличия скидок по количеству.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `ean13`

**Описание**: Локатор для штрихкода EAN13 продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `isbn`

**Описание**: Локатор для ISBN продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `upc`

**Описание**: Локатор для штрихкода UPC продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `mpn`

**Описание**: Локатор для MPN продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `cache_is_pack`

**Описание**: Локатор для определения, является ли продукт комплектом.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `cache_has_attachments`

**Описание**: Локатор для определения, есть ли у продукта вложения.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `is_virtual`

**Описание**: Локатор для определения, является ли продукт виртуальным.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `state`

**Описание**: Локатор для состояния продукта.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `additional_delivery_times`

**Описание**: Локатор для дополнительных сроков доставки.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для ожидания элемента.
- `timeout_for_event` (str): Событие для ожидания перед применением таймаута.
-  `event` (null): Событие не задано.

### `delivery_in_stock`

**Описание**: Локатор для времени доставки товара в наличии.

**Параметры**:

- `attribute` (null): Атрибут не задан.
- `by` (null): Метод поиска не задан.
- `selector` (null): Селектор не задан.
- `if_list` (str): Возвращает первый элемент из списка, если применимо.
- `use_mouse` (bool): Использование мыши не требуется.
- `mandatory` (bool): Обязательный локатор.
-  `timeout` (int):  Таймаут в секундах для