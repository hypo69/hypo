# Локаторы для продукта

## Обзор

Данный JSON-файл содержит локаторы для элементов веб-страницы, связанные с информацией о продукте. Эти локаторы используются для извлечения или взаимодействия с данными продукта на веб-странице. Файл включает в себя настройки для каждого поля продукта, такие как атрибут, метод поиска (by), селектор, настройки списков, использование мыши, обязательность и таймауты.

## Содержание

- [Обзор](#обзор)
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
    - [`ASIN`](#ASIN)
    - [`Active (0/1)`](#Active-01)
    - [`Name*`](#Name*)
     - [`Categories (x,y,z...)`](#Categories-xyz)
    - [`Price tax excluded`](#Price-tax-excluded)
    - [`Price tax included`](#Price-tax-included)
    - [`Tax rule ID`](#Tax-rule-ID)
    - [`Cost price`](#Cost-price)
    - [`On sale (0/1)`](#On-sale-01)
    - [`Discount amount`](#Discount-amount)
    - [`Discount percent`](#Discount-percent)
    - [`Discount from (yyyy-mm-dd)`](#Discount-from-yyyy-mm-dd)
    - [`Discount to (yyyy-mm-dd)`](#Discount-to-yyyy-mm-dd)
    - [`reference #`](#reference-)
    - [`Supplier reference #`](#Supplier-reference-)
    - [`Supplier`](#Supplier)
    - [`Brand`](#Brand)
    - [`EAN13`](#EAN13-1)
    - [`UPC`](#UPC-1)
    - [`MPN`](#MPN-1)
    - [`Ecotax`](#Ecotax-1)
    - [`Width`](#Width-1)
    - [`Height`](#Height-1)
    - [`Depth`](#Depth-1)
    - [`Weight`](#Weight-1)
    - [`Delivery time of in-stock products:`](#Delivery-time-of-in-stock-products)
    - [`Delivery time of out-of-stock products with allowed orders:`](#Delivery-time-of-out-of-stock-products-with-allowed-orders)
    - [`Quantity`](#Quantity)
    - [`Minimal quantity`](#Minimal-quantity)
    - [`Low stock level`](#Low-stock-level)
    - [`Send me an email when the quantity is under this level`](#Send-me-an-email-when-the-quantity-is-under-this-level)
    - [`Visibility`](#Visibility-1)
    - [`Additional shipping cost`](#Additional-shipping-cost-1)
    - [`Unit for base price`](#Unit-for-base-price)
    - [`Base price`](#Base-price)
    - [`Summary`](#Summary)
    - [`Description`](#Description-1)
    - [`Tags (x,y,z...)`](#Tags-xyz-1)
    - [`Meta title`](#Meta-title-1)
    - [`Meta keywords`](#Meta-keywords-1)
    - [`Meta description`](#Meta-description-1)
    - [`Rewritten URL`](#Rewritten-URL)
    - [`Label when in stock`](#Label-when-in-stock)
    - [`Label when backorder allowed`](#Label-when-backorder-allowed)
    - [`Available for order (0 = No, 1 = Yes)`](#Available-for-order-0--No-1--Yes)
    - [`Product availability date`](#Product-availability-date)
    - [`Product creation date`](#Product-creation-date)
    - [`Show price (0 = No, 1 = Yes)`](#Show-price-0--No-1--Yes)
    - [`Screenshot`](#Screenshot)
    - [`additional_images_urls`](#additional_images_urls)
    - [`additional_images_alts`](#additional_images_alts)
    - [`Delete existing images (0 = No, 1 = Yes)`](#Delete-existing-images-0--No-1--Yes)
    - [`Feature (Name:Value:Position:Customized)`](#Feature-NameValuePositionCustomized)
    - [`Available online only (0 = No, 1 = Yes)`](#Available-online-only-0--No-1--Yes)
    - [`Condition`](#Condition-1)
    - [`Customizable (0 = No, 1 = Yes)`](#Customizable-0--No-1--Yes)
    - [`Uploadable files (0 = No, 1 = Yes)`](#Uploadable-files-0--No-1--Yes)
    - [`Text fields (0 = No, 1 = Yes)`](#Text-fields-0--No-1--Yes)
    - [`Action when out of stock`](#Action-when-out-of-stock)
    - [`Virtual product (0 = No, 1 = Yes)`](#Virtual-product-0--No-1--Yes)
    - [`File URL`](#File-URL)
    - [`Number of allowed downloads`](#Number-of-allowed-downloads)
    - [`Expiration date (yyyy-mm-dd)`](#Expiration-date-yyyy-mm-dd)
    - [`Number of days`](#Number-of-days)
    - [`ID / Name of shop`](#ID--Name-of-shop)
    - [`Advanced Stock Management`](#Advanced-Stock-Management)
    - [`Depends on stock`](#Depends-on-stock)
    - [`Warehouse`](#Warehouse)
    - [`Accessories (x,y,z...)`](#Accessories-xyz)
    - [`affiliate short link`](#affiliate-short-link)
    - [`affiliate text`](#affiliate-text-1)
    - [`affiliate summary`](#affiliate-summary-1)
    - [`affiliate summary 2`](#affiliate-summary-2-1)
    - [`Open AI Product Description`](#Open-AI-Product-Description)
    - [`Byer protection`](#Byer-protection)
    - [`Specification`](#Specification-1)
    - [`Refirbished product description`](#Refirbished-product-description)
    - [`Additional shipping details`](#Additional-shipping-details)

## Локаторы

### `id`

**Описание**: Локатор для поля `id` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_manufacturer`

**Описание**: Локатор для поля `id_manufacturer` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_supplier`

**Описание**: Локатор для поля `id_supplier` продукта.
**Параметры**:
-   `attribute` (int): Атрибут `2794`.
-   `by` (str): Метод поиска `VALUE`.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_category_default`

**Описание**: Локатор для поля `id_category_default` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `new`

**Описание**: Локатор для поля `new` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `cache_default_attribute`

**Описание**: Локатор для поля `cache_default_attribute` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_default_image`

**Описание**: Локатор для поля `id_default_image` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_default_combination`

**Описание**: Локатор для поля `id_default_combination` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_tax`

**Описание**: Локатор для поля `id_tax` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `position_in_category`

**Описание**: Локатор для поля `position_in_category` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `type`

**Описание**: Локатор для поля `type` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `id_shop_default`

**Описание**: Локатор для поля `id_shop_default` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `reference`

**Описание**: Локатор для поля `reference` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `supplier_reference`

**Описание**: Локатор для поля `supplier_reference` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `location`

**Описание**: Локатор для поля `location` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `width`

**Описание**: Локатор для поля `width` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `height`

**Описание**: Локатор для поля `height` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `depth`

**Описание**: Локатор для поля `depth` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `weight`

**Описание**: Локатор для поля `weight` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `quantity_discount`

**Описание**: Локатор для поля `quantity_discount` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `ean13`

**Описание**: Локатор для поля `ean13` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `isbn`

**Описание**: Локатор для поля `isbn` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `upc`

**Описание**: Локатор для поля `upc` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `mpn`

**Описание**: Локатор для поля `mpn` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `cache_is_pack`

**Описание**: Локатор для поля `cache_is_pack` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `cache_has_attachments`

**Описание**: Локатор для поля `cache_has_attachments` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `is_virtual`

**Описание**: Локатор для поля `is_virtual` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `state`

**Описание**: Локатор для поля `state` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `additional_delivery_times`

**Описание**: Локатор для поля `additional_delivery_times` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `delivery_in_stock`

**Описание**: Локатор для поля `delivery_in_stock` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `delivery_out_stock`

**Описание**: Локатор для поля `delivery_out_stock` продукта.
**Параметры**:
-   `attribute` (None): Атрибут не задан.
-   `by` (None): Метод поиска не задан.
-   `selector` (None): Селектор не задан.
-   `if_list` (str): Если это список, взять "first" элемент.
-   `use_mouse` (bool): Не использовать мышь.
-   `mandatory` (bool): Поле обязательное.
-    `timeout` (int): Тайм-аут 0 секунд.
-    `timeout_for_event` (str):  Ожидать присутствия элемента.
-    `event` (None): Событие не задано.

### `product_type`

**Описание**: Локатор для поля `product_type` продукта.
**Пара