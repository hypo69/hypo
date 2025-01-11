# Документация для `product - for developer.json`

## Обзор

Данный файл содержит JSON-конфигурацию, описывающую локаторы и атрибуты для сбора данных о продуктах. Конфигурация предназначена для использования в автоматизированных процессах сбора данных с веб-страниц. Каждый элемент JSON представляет собой описание поля продукта, включая методы его определения (через селекторы, атрибуты), а также дополнительные параметры для обработки данных.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
    -   [id](#id)
    -   [id\_manufacturer](#id_manufacturer)
    -   [id\_supplier](#id_supplier)
    -   [id\_category\_default](#id_category_default)
    -   [new](#new)
    -   [cache\_default\_attribute](#cache_default_attribute)
    -   [id\_default\_image](#id_default_image)
    -   [id\_default\_combination](#id_default_combination)
    -   [id\_tax](#id_tax)
    -   [position\_in\_category](#position_in_category)
    -   [type](#type)
    -   [id\_shop\_default](#id_shop_default)
    -   [reference](#reference)
    -   [supplier\_reference](#supplier_reference)
    -   [location](#location)
    -   [width](#width)
    -   [height](#height)
    -   [depth](#depth)
    -   [weight](#weight)
    -   [quantity\_discount](#quantity_discount)
    -   [ean13](#ean13)
    -   [isbn](#isbn)
    -   [upc](#upc)
    -   [mpn](#mpn)
    -   [cache\_is\_pack](#cache_is_pack)
    -   [cache\_has\_attachments](#cache_has_attachments)
    -   [is\_virtual](#is_virtual)
    -   [state](#state)
    -   [additional\_delivery\_times](#additional_delivery_times)
    -   [delivery\_in\_stock](#delivery_in_stock)
    -   [delivery\_out\_stock](#delivery_out_stock)
    -   [product\_type](#product_type)
    -   [on\_sale](#on_sale)
    -   [online\_only](#online_only)
    -   [ecotax](#ecotax)
    -   [minimal\_quantity](#minimal_quantity)
    -   [low\_stock\_threshold](#low_stock_threshold)
    -   [low\_stock\_alert](#low_stock_alert)
    -   [price](#price)
    -   [wholesale\_price](#wholesale_price)
    -   [unity](#unity)
    -   [unit\_price\_ratio](#unit_price_ratio)
    -   [additional\_shipping\_cost](#additional_shipping_cost)
    -   [customizable](#customizable)
    -   [text\_fields](#text_fields)
    -   [uploadable\_files](#uploadable_files)
    -   [active](#active)
    -   [redirect\_type](#redirect_type)
    -   [id\_type\_redirected](#id_type_redirected)
    -   [available\_for\_order](#available_for_order)
    -   [available\_date](#available_date)
    -   [show\_condition](#show_condition)
    -   [condition](#condition)
    -   [show\_price](#show_price)
    -   [indexed](#indexed)
    -   [visibility](#visibility)
    -   [advanced\_stock\_management](#advanced_stock_management)
    -   [date\_add](#date_add)
    -   [date\_upd](#date_upd)
    -   [pack\_stock\_type](#pack_stock_type)
    -   [meta\_description](#meta_description)
    -   [meta\_keywords](#meta_keywords)
    -   [meta\_title](#meta_title)
    -   [link\_rewrite](#link_rewrite)
    -   [name](#name)
    -   [description](#description)
    -   [description\_short](#description_short)
    -   [affiliate\_short\_link](#affiliate_short_link)
    -   [affiliate\_text](#affiliate_text)
    -   [affiliate\_summary](#affiliate_summary)
    -   [affiliate\_summary\_2](#affiliate_summary_2)
    -   [available\_now](#available_now)
    -   [available\_later](#available_later)
    -   [associations](#associations)
    -   [ASIN](#asin)
    -   [Active (0/1)](#active-01)
    -   [Name*](#name)
    -   [Categories (x,y,z...)](#categories-xyz)
    -   [On sale (0/1)](#on-sale-01)
    -   [Discount amount](#discount-amount)
    -   [Discount percent](#discount-percent)
    -   [Discount from (yyyy-mm-dd)](#discount-from-yyyy-mm-dd)
    -   [Discount to (yyyy-mm-dd)](#discount-to-yyyy-mm-dd)
    -   [reference #](#reference-)
    -   [Supplier reference #](#supplier-reference-)
    -   [Supplier](#supplier)
    -   [UPC](#upc-1)
    -   [MPN](#mpn-1)
    -   [Ecotax](#ecotax-1)
    -   [Width](#width-1)
    -   [Height](#height-1)
    -   [Depth](#depth-1)
    -   [Weight](#weight-1)
    -   [Delivery time of in-stock products:](#delivery-time-of-in-stock-products)
    -   [Delivery time of out-of-stock products with allowed orders:](#delivery-time-of-out-of-stock-products-with-allowed-orders)
    -   [quantity](#quantity)
    -   [Minimal quantity](#minimal-quantity-1)
    -   [Low stock level](#low-stock-level)
    -   [Send me an email when the quantity is under this level](#send-me-an-email-when-the-quantity-is-under-this-level)
    -   [Visibility](#visibility-1)
    -   [Additional shipping cost](#additional-shipping-cost-1)
    -   [Unit for base price](#unit-for-base-price)
    -   [Base price](#base-price)
    -   [Summary](#summary)
    -   [Description](#description-1)
    -   [Tags (x,y,z...)](#tags-xyz)
    -   [Meta title](#meta-title-1)
    -   [Meta keywords](#meta-keywords-1)
    -   [Meta description](#meta-description-1)
    -   [Rewritten URL](#rewritten-url)
    -   [Label when in stock](#label-when-in-stock)
    -   [Label when backorder allowed](#label-when-backorder-allowed)
    -   [Available for order (0 = No, 1 = Yes)](#available-for-order-0--no-1--yes)
    -   [Product availability date](#product-availability-date)
    -   [Product creation date](#product-creation-date)
    -   [Show price (0 = No, 1 = Yes)](#show-price-0--no-1--yes)
    -   [Screenshot](#screenshot)
    -   [additional\_images\_urls](#additional_images_urls)
    -   [additional\_images\_alts](#additional_images_alts)
    -   [Delete existing images (0 = No, 1 = Yes)](#delete-existing-images-0--no-1--yes)
    -   [Feature (Name:Value:Position:Customized)](#feature-namevaluepositioncustomized)
    -   [Available online only (0 = No, 1 = Yes)](#available-online-only-0--no-1--yes)
    -   [Condition](#condition-1)
    -   [Customizable (0 = No, 1 = Yes)](#customizable-0--no-1--yes)
    -   [Uploadable files (0 = No, 1 = Yes)](#uploadable-files-0--no-1--yes)
    -   [Text fields (0 = No, 1 = Yes)](#text-fields-0--no-1--yes)
    -   [Action when out of stock](#action-when-out-of-stock)
    -   [Virtual product (0 = No, 1 = Yes)](#virtual-product-0--no-1--yes)
    -   [File URL](#file-url)
    -   [Number of allowed downloads](#number-of-allowed-downloads)
    -   [Expiration date (yyyy-mm-dd)](#expiration-date-yyyy-mm-dd)
    -   [Number of days](#number-of-days)
    -   [ID / Name of shop](#id--name-of-shop)
    -   [Advanced Stock Management](#advanced-stock-management-1)
    -   [Depends on stock](#depends-on-stock)
    -   [Warehouse](#warehouse)
    -   [Accessories (x,y,z...)](#accessories-xyz)
    -   [affiliate short link](#affiliate-short-link-1)
    -   [affiliate text](#affiliate-text-1)
    -   [affiliate summary](#affiliate-summary-1)
    -   [affiliate summary 2](#affiliate-summary-2-1)
    -   [Open AI Product Description](#open-ai-product-description)
    -   [Byer protection](#byer-protection)
    -   [Specification](#specification)
    -   [Refirbished product description](#refirbished-product-description)
    -   [Additional shipping details](#additional-shipping-details)
    -   [Product features](#product-features)
    -   [affiliate\_img\_HTML](#affiliate_img_html)
    -   [affiliate\_iframe](#affiliate_iframe)
     -   [Additional product info](#additional-product-info)
    -   [summary](#summary-1)

## Структура JSON

### `id`

**Описание**: Идентификатор продукта.

**Параметры**:

-   `attribute` (null): Атрибут для извлечения значения. В данном случае `null`, что может указывать на использование значения по умолчанию или отсутствие атрибута.
-   `by` (str): Метод определения элемента. В данном случае `"VALUE"`, что указывает на использование фиксированного значения.
-   `selector` (null): Селектор элемента. В данном случае `null`, так как значение фиксировано.
-   `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
-   `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
-   `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
-   `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
-   `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
-   `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_manufacturer`

**Описание**: Идентификатор производителя продукта.

**Параметры**:
- `attribute` (str): Атрибут для извлечения значения. В данном случае `"innerText"`.
- `by` (str): Метод определения элемента. В данном случае `"XPATH"`.
- `selector` (str): XPATH-селектор для поиска элемента.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_supplier`

**Описание**: Идентификатор поставщика продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (str): Метод определения элемента. В данном случае `"VALUE"`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_category_default`

**Описание**: Идентификатор категории продукта по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (str): Метод определения элемента. В данном случае `"VALUE"`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `new`

**Описание**: Флаг нового продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (str): Метод определения элемента. В данном случае `"VALUE"`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `cache_default_attribute`

**Описание**: Атрибут для кэширования по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_default_image`

**Описание**: Идентификатор изображения по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_default_combination`

**Описание**: Идентификатор комбинации по умолчанию.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_tax`

**Описание**: Идентификатор налога.

**Параметры**:
- `attribute` (str): Атрибут для извлечения значения. В данном случае `"$p.tax_rule"`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `position_in_category`

**Описание**: Позиция продукта в категории.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `type`

**Описание**: Тип продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `id_shop_default`

**Описание**: Идентификатор магазина по умолчанию.

**Параметры**:
- `attribute` (str): Атрибут для извлечения значения. В данном случае `"1"`.
- `by` (str): Метод определения элемента. В данном случае `"VALUE"`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `reference`

**Описание**: Артикул продукта.

**Параметры**:
- `attribute` (str): Атрибут для извлечения значения. В данном случае `"$d.current_url.split(f\'\'\'/\'\'\')[-2]"` - вычисляется из текущего URL.
- `by` (str): Метод определения элемента. В данном случае `"VALUE"`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `supplier_reference`

**Описание**: Артикул поставщика продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `location`

**Описание**: Местоположение продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `width`

**Описание**: Ширина продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `height`

**Описание**: Высота продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `depth`

**Описание**: Глубина продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `weight`

**Описание**: Вес продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `quantity_discount`

**Описание**: Флаг скидки на количество.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `ean13`

**Описание**: EAN13 код продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `isbn`

**Описание**: ISBN код продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `upc`

**Описание**: UPC код продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае `"first"`.
- `use_mouse` (bool): Флаг использования мыши. В данном случае `false`.
- `mandatory` (bool): Флаг обязательности наличия элемента. В данном случае `true`.
- `timeout` (int): Время ожидания (в секундах). В данном случае `0`.
- `timeout_for_event` (str): Событие для ожидания. В данном случае `"presence_of_element_located"`.
- `event` (null): Событие, которое нужно вызвать. В данном случае `null`.

### `mpn`

**Описание**: MPN (Manufacturer Part Number) продукта.

**Параметры**:
- `attribute` (null): Атрибут для извлечения значения. В данном случае `null`.
- `by` (null): Метод определения элемента. В данном случае `null`.
- `selector` (null): Селектор элемента. В данном случае `null`.
- `if_list` (str): Указывает, какое значение из списка использовать, если найдено несколько элементов. В данном случае