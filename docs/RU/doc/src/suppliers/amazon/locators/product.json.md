# Модуль `product.json`

## Обзор

Этот файл содержит JSON-структуру, описывающую локаторы и параметры для извлечения данных о продуктах с сайта Amazon. Каждый ключ верхнего уровня представляет собой поле продукта, а его значение - это объект, содержащий инструкции по извлечению данных.

## Содержание

- [Обзор](#обзор)
- [Локаторы](#локаторы)
    - [id](#id)
    - [id\_manufacturer](#id_manufacturer)
    - [id\_supplier](#id_supplier)
    - [id\_category\_default](#id_category_default)
    - [new](#new)
    - [cache\_default\_attribute](#cache_default_attribute)
    - [id\_default\_image](#id_default_image)
    - [id\_default\_combination](#id_default_combination)
    - [id\_tax](#id_tax)
    - [position\_in\_category](#position_in_category)
    - [type](#type)
    - [id\_shop\_default](#id_shop_default)
    - [reference](#reference)
    - [supplier\_reference](#supplier_reference)
    - [location](#location)
    - [width](#width)
    - [height](#height)
    - [depth](#depth)
    - [weight](#weight)
    - [quantity\_discount](#quantity_discount)
    - [ean13](#ean13)
    - [isbn](#isbn)
    - [upc](#upc)
    - [mpn](#mpn)
    - [cache\_is\_pack](#cache_is_pack)
    - [cache\_has\_attachments](#cache_has_attachments)
    - [is\_virtual](#is_virtual)
    - [state](#state)
    - [additional\_delivery\_times](#additional_delivery_times)
    - [delivery\_in\_stock](#delivery_in_stock)
    - [delivery\_out\_stock](#delivery_out_stock)
    - [product\_type](#product_type)
    - [on\_sale](#on_sale)
    - [online\_only](#online_only)
    - [ecotax](#ecotax)
    - [minimal\_quantity](#minimal_quantity)
    - [low\_stock\_threshold](#low_stock_threshold)
    - [low\_stock\_alert](#low_stock_alert)
    - [price](#price)
        - [price.new](#price-new)
        - [price.ref](#price-ref)
    - [wholesale\_price](#wholesale_price)
    - [unity](#unity)
    - [unit\_price\_ratio](#unit_price_ratio)
    - [additional\_shipping\_cost](#additional_shipping_cost)
    - [customizable](#customizable)
    - [text\_fields](#text_fields)
    - [uploadable\_files](#uploadable_files)
    - [active](#active)
    - [redirect\_type](#redirect_type)
    - [id\_type\_redirected](#id_type_redirected)
    - [available\_for\_order](#available_for_order)
    - [available\_date](#available_date)
    - [show\_condition](#show_condition)
    - [condition](#condition)
    - [show\_price](#show_price)
    - [indexed](#indexed)
    - [visibility](#visibility)
    - [advanced\_stock\_management](#advanced_stock_management)
    - [date\_add](#date_add)
    - [date\_upd](#date_upd)
    - [pack\_stock\_type](#pack_stock_type)
    - [meta\_description](#meta_description)
    - [meta\_keywords](#meta_keywords)
    - [meta\_title](#meta_title)
    - [link\_rewrite](#link_rewrite)
    - [name](#name)
    - [description](#description)
    - [specification](#specification)
    - [available\_now](#available_now)
    - [available\_later](#available_later)
    - [associations](#associations)
    - [ASIN](#asin)
    - [Active (0/1)](#active-01)
     - [Categories (x,y,z...)](#categories-xyz)
    - [On sale (0/1)](#on-sale-01)
    - [Discount amount](#discount-amount)
    - [Discount percent](#discount-percent)
    - [Discount from (yyyy-mm-dd)](#discount-from-yyyy-mm-dd)
    - [Discount to (yyyy-mm-dd)](#discount-to-yyyy-mm-dd)
    - [reference #](#reference-)
    - [Supplier reference #](#supplier-reference-)
    - [Supplier](#supplier)
    - [UPC](#upc-1)
    - [MPN](#mpn-1)
    - [Ecotax](#ecotax-1)
    - [Width](#width-1)
    - [Height](#height-1)
    - [Depth](#depth-1)
    - [Weight](#weight-1)
    - [Delivery time of in-stock products:](#delivery-time-of-in-stock-products)
    - [Delivery time of out-of-stock products with allowed orders:](#delivery-time-of-out-of-stock-products-with-allowed-orders)
    - [quantity](#quantity)
    - [Minimal quantity](#minimal-quantity-1)
    - [Low stock level](#low-stock-level)
    - [Send me an email when the quantity is under this level](#send-me-an-email-when-the-quantity-is-under-this-level)
    - [Visibility](#visibility-1)
    - [Additional shipping cost](#additional-shipping-cost-1)
    - [Unit for base price](#unit-for-base-price)
    - [Base price](#base-price)
    - [Description](#description-1)
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
    - [Screenshot](#screenshot)
    - [additional\_images\_urls](#additional_images_urls)
    - [additional\_images\_alts](#additional_images_alts)
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
    - [affiliate\_short\_link](#affiliate_short_link)
    - [affiliate\_text](#affiliate_text)
    - [affiliate\_summary](#affiliate_summary)
    - [affiliate\_summary\_2](#affiliate_summary_2)
    - [Open AI Product Description](#open-ai-product-description)
    - [Byer protection](#byer-protection)
    - [Specification](#specification-1)
    - [Refirbished product description](#refirbished-product-description)
    - [Additional shipping details](#additional-shipping-details)
    - [Product features](#product-features)
    - [affiliate\_img\_HTML](#affiliate_img_html)
    - [affiliate\_iframe](#affiliate_iframe)
    - [Additional product info](#additional-product-info)
    - [description\_short](#description_short)


## Локаторы

### `id`

**Описание**: Локатор для идентификатора продукта.

**Параметры**:
- `attribute`:  `null`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_manufacturer`

**Описание**: Локатор для идентификатора производителя продукта.

**Параметры**:
- `attribute`: `innerText`
- `by`: `XPATH`
- `selector`: `//span[contains(text(), 'Brand')]/parent::td/following-sibling::td/span[contains(@class, 'po-break-word')]`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_supplier`

**Описание**: Локатор для идентификатора поставщика продукта.

**Параметры**:
- `attribute`: `2800`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_category_default`

**Описание**: Локатор для идентификатора категории продукта по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `new`

**Описание**: Локатор для отметки нового продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `cache_default_attribute`

**Описание**: Локатор для кэширования атрибута по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_default_image`

**Описание**: Локатор для идентификатора изображения продукта по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_default_combination`

**Описание**: Локатор для идентификатора комбинации продукта по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_tax`

**Описание**: Локатор для идентификатора налога продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `position_in_category`

**Описание**: Локатор для позиции продукта в категории.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `type`

**Описание**: Локатор для типа продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_shop_default`

**Описание**: Локатор для идентификатора магазина по умолчанию.

**Параметры**:
- `attribute`: `"1"`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `reference`

**Описание**: Локатор для ссылки на продукт.

**Параметры**:
- `attribute`: `$d.current_url.split(f\'\'\'/\'\'\')[-2]`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `supplier_reference`

**Описание**: Локатор для ссылки на поставщика продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `location`

**Описание**: Локатор для местоположения продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `width`

**Описание**: Локатор для ширины продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `height`

**Описание**: Локатор для высоты продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `depth`

**Описание**: Локатор для глубины продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `weight`

**Описание**: Локатор для веса продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `quantity_discount`

**Описание**: Локатор для скидки на количество продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `ean13`

**Описание**: Локатор для штрих-кода EAN13 продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `isbn`

**Описание**: Локатор для ISBN продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `upc`

**Описание**: Локатор для UPC продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `mpn`

**Описание**: Локатор для MPN продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `cache_is_pack`

**Описание**: Локатор для кэширования отметки, является ли продукт набором.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `cache_has_attachments`

**Описание**: Локатор для кэширования отметки, есть ли у продукта вложения.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `is_virtual`

**Описание**: Локатор для отметки, является ли продукт виртуальным.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `state`

**Описание**: Локатор для состояния продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `additional_delivery_times`

**Описание**: Локатор для дополнительного времени доставки продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `delivery_in_stock`

**Описание**: Локатор для времени доставки товара в наличии.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `delivery_out_stock`

**Описание**: Локатор для времени доставки товара при отсутствии на складе.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `product_type`

**Описание**: Локатор для типа продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `on_sale`

**Описание**: Локатор для отметки, находится ли продукт в распродаже.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `online_only`

**Описание**: Локатор для отметки, доступен ли продукт только онлайн.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `ecotax`

**Описание**: Локатор для экологического налога продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `minimal_quantity`

**Описание**: Локатор для минимального количества продукта для заказа.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `low_stock_threshold`

**Описание**: Локатор для порога низкого уровня запасов продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `low_stock_alert`

**Описание**: Локатор для оповещения о низком уровне запасов продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `price`

**Описание**: Локатор для цены продукта.

#### `price.new`

**Описание**: Локатор для новой цены продукта.

**Параметры**:
- `attribute`: `innerText`
- `by`: `XPATH`
- `selector`: `//div[contains(@data-csa-c-asin, '$_(driver.current_url.split(f\'\'\'/\'\'\')[-2])_$') and contains(@id, 'corePriceDisplay')]//span[1]`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

#### `price.ref`

**Описание**: Локатор для референсной цены продукта.

**Параметры**:
- `attribute`: `innerText`
- `by`: `XPATH`
- `selector`: `//div[contains(@data-csa-c-asin, '$_(driver.current_url.split(f\'\'\'/\'\'\')[-2])_$') and contains(@id, 'corePrice_desktop')]//span[contains(@class, 'apexPriceToPay')]//span`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `wholesale_price`

**Описание**: Локатор для оптовой цены продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `unity`

**Описание**: Локатор для единицы измерения продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `unit_price_ratio`

**Описание**: Локатор для соотношения цены за единицу продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `additional_shipping_cost`

**Описание**: Локатор для дополнительных расходов на доставку продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `customizable`

**Описание**: Локатор для отметки, является ли продукт настраиваемым.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `text_fields`

**Описание**: Локатор для текстовых полей продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `uploadable_files`

**Описание**: Локатор для отметки, имеет ли продукт загружаемые файлы.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `active`

**Описание**: Локатор для отметки, активен ли продукт.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `redirect_type`

**Описание**: Локатор для типа редиректа продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `id_type_redirected`

**Описание**: Локатор для идентификатора типа редиректа продукта.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `available_for_order`

**Описание**: Локатор для отметки, доступен ли продукт для заказа.

**Параметры**:
- `attribute`: `null`
- `by`: `null`