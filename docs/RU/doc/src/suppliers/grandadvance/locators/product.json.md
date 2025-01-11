# Описание локаторов продукта

## Обзор

Данный файл `product.json` содержит JSON-объект с описаниями локаторов для веб-элементов, связанных с информацией о продукте. Эти локаторы используются для автоматизации извлечения данных о продуктах с веб-страниц. Каждый локатор описывает, как найти определенный элемент на странице, используя XPath, CSS-селекторы или другие методы.

## Оглавление
- [close_pop_up](#close_pop_up)
- [id](#id)
- [id_manufacturer](#id_manufacturer)
- [id_supplier](#id_supplier)
- [id_product](#id_product)
- [id_category_default](#id_category_default)
- [new](#new)
- [cache_default_attribute](#cache_default_attribute)
- [id_default_image](#id_default_image)
- [default_image_url](#default_image_url)
- [id_default_combination](#id_default_combination)
- [id_tax](#id_tax)
- [position_in_category](#position_in_category)
- [type](#type)
- [id_shop_default](#id_shop_default)
- [reference](#reference)
- [supplier_reference](#supplier_reference)
- [location](#location)
- [width](#width)
- [height](#height)
- [depth](#depth)
- [weight](#weight)
- [quantity_discount](#quantity_discount)
- [ean13](#ean13)
- [isbn](#isbn)
- [upc](#upc)
- [mpn](#mpn)
- [cache_is_pack](#cache_is_pack)
- [cache_has_attachments](#cache_has_attachments)
- [is_virtual](#is_virtual)
- [state](#state)
- [additional_delivery_times](#additional_delivery_times)
- [delivery_in_stock](#delivery_in_stock)
- [delivery_out_stock](#delivery_out_stock)
- [product_type](#product_type)
- [on_sale](#on_sale)
- [online_only](#online_only)
- [ecotax](#ecotax)
- [minimal_quantity](#minimal_quantity)
- [low_stock_threshold](#low_stock_threshold)
- [low_stock_alert](#low_stock_alert)
- [price](#price)
- [wholesale_price](#wholesale_price)
- [unity](#unity)
- [unit_price_ratio](#unit_price_ratio)
- [additional_shipping_cost](#additional_shipping_cost)
- [customizable](#customizable)
- [text_fields](#text_fields)
- [uploadable_files](#uploadable_files)
- [active](#active)
- [redirect_type](#redirect_type)
- [id_type_redirected](#id_type_redirected)
- [available_for_order](#available_for_order)
- [available_date](#available_date)
- [show_condition](#show_condition)
- [condition](#condition)
- [show_price](#show_price)
- [indexed](#indexed)
- [visibility](#visibility)
- [advanced_stock_management](#advanced_stock_management)
- [date_add](#date_add)
- [date_upd](#date_upd)
- [pack_stock_type](#pack_stock_type)
- [meta_description](#meta_description)
- [meta_keywords](#meta_keywords)
- [meta_title](#meta_title)
- [link_rewrite](#link_rewrite)
- [name](#name)
- [description_short](#description_short)
- [description](#description)
- [specification](#specification)
- [affiliate_short_link](#affiliate_short_link)
- [affiliate_text](#affiliate_text)
- [affiliate_summary](#affiliate_summary)
- [affiliate_summary_2](#affiliate_summary_2)
- [available_now](#available_now)
- [available_later](#available_later)
- [associations](#associations)
- [ASIN](#ASIN)
- [Active (0/1)](#Active-(0/1))
- [Name*](#Name*)
- [Categories (x,y,z...)](#Categories-(x,y,z...))
- [Price tax excluded](#Price-tax-excluded)
- [Price tax included](#Price-tax-included)
- [Tax rule ID](#Tax-rule-ID)
- [Cost price](#Cost-price)
- [On sale (0/1)](#On-sale-(0/1))
- [Discount amount](#Discount-amount)
- [Discount percent](#Discount-percent)
- [Discount from (yyyy-mm-dd)](#Discount-from-(yyyy-mm-dd))
- [Discount to (yyyy-mm-dd)](#Discount-to-(yyyy-mm-dd))
- [reference #](#reference-#)
- [Supplier reference #](#Supplier-reference-#)
- [Supplier](#Supplier)
- [Brand](#Brand)
- [EAN13](#EAN13)
- [UPC](#UPC)
- [MPN](#MPN)
- [Ecotax](#Ecotax)
- [Width](#Width)
- [Height](#Height)
- [Depth](#Depth)
- [Weight](#Weight)
- [Delivery time of in-stock products:](#Delivery-time-of-in-stock-products:)
- [Delivery time of out-of-stock products with allowed orders:](#Delivery-time-of-out-of-stock-products-with-allowed-orders:)
- [Quantity](#Quantity)
- [Minimal quantity](#Minimal-quantity)
- [Low stock level](#Low-stock-level)
- [Send me an email when the quantity is under this level](#Send-me-an-email-when-the-quantity-is-under-this-level)
- [Visibility](#Visibility)
- [Additional shipping cost](#Additional-shipping-cost)
- [Unit for base price](#Unit-for-base-price)
- [Base price](#Base-price)
- [Summary](#Summary)
- [Description](#Description)
- [Tags (x,y,z...)](#Tags-(x,y,z...))
- [Meta title](#Meta-title)
- [Meta keywords](#Meta-keywords)
- [Meta description](#Meta-description)
- [Rewritten URL](#Rewritten-URL)
- [Label when in stock](#Label-when-in-stock)
- [Label when backorder allowed](#Label-when-backorder-allowed)
- [Available for order (0 = No, 1 = Yes)](#Available-for-order-(0-=-No,-1-=-Yes))
- [Product availability date](#Product-availability-date)
- [Product creation date](#Product-creation-date)
- [Show price (0 = No, 1 = Yes)](#Show-price-(0-=-No,-1-=-Yes))
- [Screenshot](#Screenshot)
- [images_urls](#images_urls)
- [additional_images_urls](#additional_images_urls)
- [additional_images_alts](#additional_images_alts)
- [Delete existing images (0 = No, 1 = Yes)](#Delete-existing-images-(0-=-No,-1-=-Yes))
- [Feature (Name:Value:Position:Customized)](#Feature-(Name:Value:Position:Customized))
- [Available online only (0 = No, 1 = Yes)](#Available-online-only-(0-=-No,-1-=-Yes))
- [Condition](#Condition)
- [Customizable (0 = No, 1 = Yes)](#Customizable-(0-=-No,-1-=-Yes))
- [Uploadable files (0 = No, 1 = Yes)](#Uploadable-files-(0-=-No,-1-=-Yes))
- [Text fields (0 = No, 1 = Yes)](#Text-fields-(0-=-No,-1-=-Yes))
- [Action when out of stock](#Action-when-out-of-stock)
- [Virtual product (0 = No, 1 = Yes)](#Virtual-product-(0-=-No,-1-=-Yes))
- [File URL](#File-URL)
- [Number of allowed downloads](#Number-of-allowed-downloads)
- [Expiration date (yyyy-mm-dd)](#Expiration-date-(yyyy-mm-dd))
- [Number of days](#Number-of-days)
- [ID / Name of shop](#ID-/-Name-of-shop)
- [Advanced Stock Management](#Advanced-Stock-Management)
- [Depends on stock](#Depends-on-stock)
- [Warehouse](#Warehouse)
- [Accessories (x,y,z...)](#Accessories-(x,y,z...))
- [affiliate short link](#affiliate-short-link)
- [affiliate text](#affiliate-text)
- [affiliate summary](#affiliate-summary)
- [affiliate summary 2](#affiliate-summary-2)
- [Open AI Product Description](#Open-AI-Product-Description)
- [Byer protection](#Byer-protection)
- [Specification](#Specification)
- [Refirbished product description](#Refirbished-product-description)
- [Additional shipping details](#Additional-shipping-details)

## Локаторы

### `close_pop_up`

**Описание**: Локатор для кнопки закрытия всплывающего окна.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (str): Метод поиска элемента, в данном случае "XPATH".
- `selector` (str): Xpath-селектор для кнопки закрытия: `//button[@class='close']`.
- `if_list` (str):  Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом. В данном случае `false`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (str): Событие, которое нужно выполнить на элементе, в данном случае `click()`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `locator_description` (str): Описание локатора: `"Закрыти попап окна"`.

### `id`

**Описание**: Локатор для идентификатора продукта.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом. В данном случае `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `id_manufacturer`

**Описание**: Локатор для идентификатора производителя.

**Параметры**:
- `attribute` (str): Атрибут элемента, который нужно получить: `"innerText"`.
- `by` (str): Метод поиска элемента: `"XPATH"`.
- `selector` (str): XPath-селектор для SKU: `//span[@class = 'ltr sku-copy']`.
- `if_list` (str):  Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.
- `locator_description` (str): Описание локатора: `"SKU morlevi"`.

### `id_supplier`

**Описание**: Локатор для идентификатора поставщика.

**Параметры**:
- `attribute` (int): Атрибут элемента, который нужно получить. В данном случае это значение  `2789`.
- `by` (str): Метод поиска элемента: `"VALUE"`.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.
- `locator_description` (str): Описание локатора: `"SKU morlevi"`.

### `id_product`

**Описание**: Локатор для идентификатора продукта.

**Параметры**:
- `attribute` (str): Атрибут элемента, который нужно получить: `"innerText"`.
- `by` (str): Метод поиска элемента: `"XPATH"`.
- `selector` (str): XPath-селектор для SKU: `//span[@class = 'part_number']`.
- `if_list` (str):  Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.
- `locator_description` (str): Описание локатора: `"SKU morlevi"`.

### `id_category_default`

**Описание**: Локатор для идентификатора категории по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `new`

**Описание**: Локатор для определения, является ли товар новым.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `cache_default_attribute`

**Описание**: Локатор для кэширования атрибута по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `id_default_image`

**Описание**: Локатор для идентификатора изображения по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `default_image_url`

**Описание**: Локатор для URL-адреса изображения по умолчанию.

**Параметры**:
- `attribute` (str): Атрибут элемента, который нужно получить: `"src"`.
- `by` (str): Метод поиска элемента: `"XPATH"`.
- `selector` (str): XPath-селектор для изображения: `//div[@class = 'big_image']//img`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (bool): Событие, которое нужно выполнить на элементе, в данном случае `false`.
- `locator_description` (str): Описание локатора: `""`.

### `id_default_combination`

**Описание**: Локатор для идентификатора комбинации по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `id_tax`

**Описание**: Локатор для идентификатора налога.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `position_in_category`

**Описание**: Локатор для позиции товара в категории.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `type`

**Описание**: Локатор для типа продукта.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `id_shop_default`

**Описание**: Локатор для идентификатора магазина по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `reference`

**Описание**: Локатор для артикула товара.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `supplier_reference`

**Описание**: Локатор для артикула поставщика.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `location`

**Описание**: Локатор для местоположения товара.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `width`

**Описание**: Локатор для ширины товара.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `height`

**Описание**: Локатор для высоты товара.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `depth`

**Описание**: Локатор для глубины товара.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `weight`

**Описание**: Локатор для веса товара.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `quantity_discount`

**Описание**: Локатор для скидки за количество.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `ean13`

**Описание**: Локатор для штрихкода EAN13.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null): Селектор не определен.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько: `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом: `false`.
- `mandatory` (bool): Указывает, является ли элемент обязательным для поиска: `true`.
- `timeout` (int): Время ожидания элемента в секундах: `0`.
- `timeout_for_event` (str): Указывает событие для таймаута, в данном случае `presence_of_element_located`.
- `event` (null): Событие, которое нужно выполнить на элементе, не определено.

### `isbn`

**Описание**: Локатор для штрихкода ISBN.

**Параметры**:
- `attribute` (null): Атрибут элемента, который нужно получить. В данном случае не используется.
- `by` (null): Метод поиска элемента не определен.
- `selector` (null