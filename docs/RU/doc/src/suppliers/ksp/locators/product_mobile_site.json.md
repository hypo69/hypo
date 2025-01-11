# Описание локаторов для мобильной версии сайта KSP

## Обзор
Этот файл содержит JSON-объект с локаторами для элементов на мобильной версии сайта KSP. Локаторы используются для автоматизации взаимодействия с веб-элементами при тестировании или сборе данных.

## Содержание
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
- [Active (0/1)](#active-01)
- [Name*](#name-1)
- [Categories (x,y,z...)](#categories-xyz)
- [Price tax excluded](#price-tax-excluded)
- [Price tax included](#price-tax-included)
- [Tax rule ID](#tax-rule-id)
- [Cost price](#cost-price)
- [On sale (0/1)](#on-sale-01)
- [Discount amount](#discount-amount)
- [Discount percent](#discount-percent)
- [Discount from (yyyy-mm-dd)](#discount-from-yyyy-mm-dd)
- [Discount to (yyyy-mm-dd)](#discount-to-yyyy-mm-dd)
- [reference #](#reference-2)
- [Supplier reference #](#supplier-reference-1)
- [Supplier](#supplier)
- [Brand](#brand)
- [EAN13](#ean13-1)
- [UPC](#upc-1)
- [MPN](#mpn-1)
- [Ecotax](#ecotax-1)
- [Width](#width-1)
- [Height](#height-1)
- [Depth](#depth-1)
- [Weight](#weight-1)
- [Delivery time of in-stock products:](#delivery-time-of-in-stock-products)
- [Delivery time of out-of-stock products with allowed orders:](#delivery-time-of-out-of-stock-products-with-allowed-orders)
- [Quantity](#quantity)
- [Minimal quantity](#minimal-quantity-1)
- [Low stock level](#low-stock-level)
- [Send me an email when the quantity is under this level](#send-me-an-email-when-the-quantity-is-under-this-level)
- [Visibility](#visibility-1)
- [Additional shipping cost](#additional-shipping-cost-1)
- [Unit for base price](#unit-for-base-price)
- [Base price](#base-price)
- [Summary](#summary)
- [Tags (x,y,z...)](#tags-xyz)
- [Meta title](#meta-title-1)
- [Meta keywords](#meta-keywords-1)
- [Meta description](#meta-description-1)
- [Rewritten URL](#rewritten-url)
- [Label when in stock](#label-when-in-stock)
- [Label when backorder allowed](#label-when-backorder-allowed)
- [Available for order (0 = No, 1 = Yes)](#available-for-order-0--no-1--yes)
- [Product availability date](#product-availability-date)
- [Product creation date](#product-creation-date)
- [Show price (0 = No, 1 = Yes)](#show-price-0--no-1--yes)
- [images_urls](#images_urls)
- [additional_images_urls](#additional_images_urls)
- [additional_images_alts](#additional_images_alts)
- [Delete existing images (0 = No, 1 = Yes)](#delete-existing-images-0--no-1--yes)
- [Feature (Name:Value:Position:Customized)](#feature-namevaluepositioncustomized)
- [Available online only (0 = No, 1 = Yes)](#available-online-only-0--no-1--yes)
- [Condition](#condition-1)
- [Customizable (0 = No, 1 = Yes)](#customizable-0--no-1--yes)
- [Uploadable files (0 = No, 1 = Yes)](#uploadable-files-0--no-1--yes)
- [Text fields (0 = No, 1 = Yes)](#text-fields-0--no-1--yes)
- [Action when out of stock](#action-when-out-of-stock)
- [Virtual product (0 = No, 1 = Yes)](#virtual-product-0--no-1--yes)
- [File URL](#file-url)
- [Number of allowed downloads](#number-of-allowed-downloads)
- [Expiration date (yyyy-mm-dd)](#expiration-date-yyyy-mm-dd)
- [Number of days](#number-of-days)
- [ID / Name of shop](#id--name-of-shop)
- [Advanced Stock Management](#advanced-stock-management-1)
- [Depends on stock](#depends-on-stock)
- [Warehouse](#warehouse)
- [Accessories (x,y,z...)](#accessories-xyz)
- [affiliate short link](#affiliate-short-link-1)
- [affiliate text](#affiliate-text-1)
- [affiliate summary](#affiliate-summary-1)
- [affiliate summary 2](#affiliate-summary-2-1)
- [Open AI Product Description](#open-ai-product-description)
- [Byer protection](#byer-protection)
- [Specification](#specification-1)
- [Refirbished product description](#refirbished-product-description)
- [Additional shipping details](#additional-shipping-details)


## Локаторы

### `close_pop_up`
**Описание**: Локатор для кнопки закрытия всплывающего окна.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-селектор для кнопки закрытия - `//button[@class='close']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (str): Событие, которое необходимо выполнить - `click()`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `locator_description` (str): Описание локатора - `Закрыти попап окна`.

### `id`
**Описание**: Локатор для идентификатора элемента.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `id_manufacturer`
**Описание**: Локатор для идентификатора производителя товара (SKU manufacturer).

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.
- `locator_description` (str): Описание локатора - `SKU manufacturer`.

### `id_supplier`
**Описание**: Локатор для идентификатора поставщика товара (SKU ksp).

**Параметры**:
- `attribute` (str): Значение атрибута - `2787`.
- `by` (str): Тип локатора - `VALUE`.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `2`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.
- `locator_description` (str): Описание локатора - `SKU ksp`.

### `id_product`
**Описание**: Локатор для идентификатора товара (mobile version SKU ksp).

**Параметры**:
- `attribute` (str): Атрибут, значение которого нужно извлечь - `innerText`.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-селектор для поиска элемента - `//span[contains(text(),'מקט')]`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `2`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.
- `locator_description` (str): Описание локатора - `mobile version SKU ksp`.

### `id_category_default`
**Описание**: Локатор для идентификатора категории товара по умолчанию.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `new`
**Описание**: Локатор для определения, является ли товар новым.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `cache_default_attribute`
**Описание**: Локатор для атрибута кэширования по умолчанию.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `id_default_image`
**Описание**: Локатор для идентификатора изображения по умолчанию.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `default_image_url`
**Описание**: Локатор для URL изображения по умолчанию.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-селектор для поиска элемента - `//div[contains(@class, 'swiper-slide')]//img`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `screenshot()`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `locator_description` (str): Описание локатора не указано.

### `id_default_combination`
**Описание**: Локатор для идентификатора комбинации товара по умолчанию.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `id_tax`
**Описание**: Локатор для идентификатора налога товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `position_in_category`
**Описание**: Локатор для позиции товара в категории.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `type`
**Описание**: Локатор для типа товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `id_shop_default`
**Описание**: Локатор для идентификатора магазина по умолчанию.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `reference`
**Описание**: Локатор для артикула товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `supplier_reference`
**Описание**: Локатор для артикула товара у поставщика.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `location`
**Описание**: Локатор для местоположения товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `width`
**Описание**: Локатор для ширины товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `height`
**Описание**: Локатор для высоты товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `depth`
**Описание**: Локатор для глубины товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `weight`
**Описание**: Локатор для веса товара.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `quantity_discount`
**Описание**: Локатор для информации о скидке за количество.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `ean13`
**Описание**: Локатор для кода EAN13.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `isbn`
**Описание**: Локатор для кода ISBN.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `upc`
**Описание**: Локатор для кода UPC.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `mpn`
**Описание**: Локатор для кода MPN.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `cache_is_pack`
**Описание**: Локатор для определения, является ли товар набором.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `cache_has_attachments`
**Описание**: Локатор для определения, имеет ли товар вложения.

**Параметры**:
- `attribute` (None): Атрибут не используется.
- `by` (None): Тип локатора не используется.
- `selector` (None): Селектор не используется.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка, если их несколько - `first`.
- `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия - `False`.
- `mandatory` (bool): Является ли локатор обязательным - `True`.
- `timeout` (int): Таймаут ожидания - `0`.
- `timeout_for_event` (str): Тип ожидания - `presence_of_element_located`.
- `event` (None): Событие не используется.

### `is_virtual`
**Описание**: Локатор для определения, является ли товар виртуальным.

**Пара