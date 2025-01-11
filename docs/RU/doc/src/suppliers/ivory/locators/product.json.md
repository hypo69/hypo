# `product.json`

## Обзор

Файл `product.json` содержит JSON-объект, представляющий собой набор локаторов для различных элементов веб-страницы, связанных с информацией о продукте. Каждый элемент имеет свой уникальный ключ и набор параметров, определяющих способ его поиска и взаимодействия с ним на странице. Эти локаторы используются для автоматизации тестирования и сбора данных о продуктах.

## Содержание

- [Обзор](#обзор)
- [Локаторы](#локаторы)
    - [`close_pop_up`](#close_pop_up)
    - [`id`](#id)
    - [`id_manufacturer`](#id_manufacturer)
    - [`id_supplier`](#id_supplier)
    - [`id_product`](#id_product)
    - [`id_category_default`](#id_category_default)
    - [`new`](#new)
    - [`cache_default_attribute`](#cache_default_attribute)
    - [`id_default_image`](#id_default_image)
    - [`default_image_url`](#default_image_url)
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
    - [`description_short`](#description_short)
    - [`description`](#description)
    - [`specification`](#specification)
    - [`affiliate_short_link`](#affiliate_short_link)
    - [`affiliate_text`](#affiliate_text)
    - [`affiliate_summary`](#affiliate_summary)
    - [`affiliate_summary_2`](#affiliate_summary_2)
    - [`available_now`](#available_now)
    - [`available_later`](#available_later)
    - [`associations`](#associations)
    - [`ASIN`](#asin)
    - [`Active (0/1)`](#active-01)
    - [`Name*`](#name-1)
    - [`Categories (x,y,z...)`](#categories-xyz)
    - [`Price tax excluded`](#price-tax-excluded)
    - [`Price tax included`](#price-tax-included)
    - [`Tax rule ID`](#tax-rule-id)
    - [`Cost price`](#cost-price)
    - [`On sale (0/1)`](#on-sale-01)
    - [`Discount amount`](#discount-amount)
    - [`Discount percent`](#discount-percent)
    - [`Discount from (yyyy-mm-dd)`](#discount-from-yyyy-mm-dd)
    - [`Discount to (yyyy-mm-dd)`](#discount-to-yyyy-mm-dd)
    - [`reference #`](#reference-1)
    - [`Supplier reference #`](#supplier-reference-1)
    - [`Supplier`](#supplier)
    - [`Brand`](#brand)
    - [`EAN13`](#ean13-1)
    - [`UPC`](#upc-1)
    - [`MPN`](#mpn-1)
    - [`Ecotax`](#ecotax-1)
    - [`Width`](#width-1)
    - [`Height`](#height-1)
    - [`Depth`](#depth-1)
    - [`Weight`](#weight-1)
    - [`Delivery time of in-stock products:`](#delivery-time-of-in-stock-products)
    - [`Delivery time of out-of-stock products with allowed orders:`](#delivery-time-of-out-of-stock-products-with-allowed-orders)
    - [`Quantity`](#quantity)
    - [`Minimal quantity`](#minimal-quantity-1)
    - [`Low stock level`](#low-stock-level)
    - [`Send me an email when the quantity is under this level`](#send-me-an-email-when-the-quantity-is-under-this-level)
    - [`Visibility`](#visibility-1)
    - [`Additional shipping cost`](#additional-shipping-cost-1)
    - [`Unit for base price`](#unit-for-base-price)
    - [`Base price`](#base-price)
    - [`Summary`](#summary)
    - [`Description`](#description-1)
    - [`Tags (x,y,z...)`](#tags-xyz)
    - [`Meta title`](#meta-title-1)
    - [`Meta keywords`](#meta-keywords-1)
    - [`Meta description`](#meta-description-1)
    - [`Rewritten URL`](#rewritten-url)
    - [`Label when in stock`](#label-when-in-stock)
    - [`Label when backorder allowed`](#label-when-backorder-allowed)
    - [`Available for order (0 = No, 1 = Yes)`](#available-for-order-0--no-1--yes)
    - [`Product availability date`](#product-availability-date)
    - [`Product creation date`](#product-creation-date)
    - [`Show price (0 = No, 1 = Yes)`](#show-price-0--no-1--yes)
    - [`Screenshot`](#screenshot)
    - [`images_urls`](#images_urls)
    - [`additional_images_urls`](#additional_images_urls)
    - [`additional_images_alts`](#additional_images_alts)
    - [`Delete existing images (0 = No, 1 = Yes)`](#delete-existing-images-0--no-1--yes)
    - [`Feature (Name:Value:Position:Customized)`](#feature-namevaluepositioncustomized)
    - [`Available online only (0 = No, 1 = Yes)`](#available-online-only-0--no-1--yes)
    - [`Condition`](#condition-1)
    - [`Customizable (0 = No, 1 = Yes)`](#customizable-0--no-1--yes)
    - [`Uploadable files (0 = No, 1 = Yes)`](#uploadable-files-0--no-1--yes)
    - [`Text fields (0 = No, 1 = Yes)`](#text-fields-0--no-1--yes)
    - [`Action when out of stock`](#action-when-out-of-stock)
    - [`Virtual product (0 = No, 1 = Yes)`](#virtual-product-0--no-1--yes)
    - [`File URL`](#file-url)
    - [`Number of allowed downloads`](#number-of-allowed-downloads)
    - [`Expiration date (yyyy-mm-dd)`](#expiration-date-yyyy-mm-dd)
    - [`Number of days`](#number-of-days)
    - [`ID / Name of shop`](#id--name-of-shop)
    - [`Advanced Stock Management`](#advanced-stock-management-1)
    - [`Depends on stock`](#depends-on-stock)
    - [`Warehouse`](#warehouse)
    - [`Accessories (x,y,z...)`](#accessories-xyz)
    - [`affiliate short link`](#affiliate-short-link-1)
     - [`affiliate text`](#affiliate-text-1)
     - [`affiliate summary`](#affiliate-summary-1)
      - [`affiliate summary 2`](#affiliate-summary-2-1)
    - [`Open AI Product Description`](#open-ai-product-description)
    - [`Byer protection`](#byer-protection)
    - [`Specification`](#specification-1)
    - [`Refirbished product description`](#refirbished-product-description)
     - [`Additional shipping details`](#additional-shipping-details)

## Локаторы

### `close_pop_up`

**Описание**: Локатор для кнопки закрытия всплывающего окна.

**Параметры**:
- `attribute`: `null`.
- `by`: `"XPATH"`.
- `selector`: `"//button[@class='close']"`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"click()"`
- `mandatory`: `true`.
- `locator_description`: `"Закрыти попап окна"`.

### `id`

**Описание**: Локатор для идентификатора продукта.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `id_manufacturer`

**Описание**: Локатор для извлечения SKU производителя.

**Параметры**:
- `attribute`: `"innerText"`.
- `by`: `"XPATH"`.
- `selector`: `""`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.
- `locator_description`: `"SKU morlevi"`.

### `id_supplier`

**Описание**: Локатор для идентификатора поставщика.

**Параметры**:
- `attribute`: `11343`.
- `by`: `"VALUE"`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.
- `locator_description`: `"11343 ivory"`.

### `id_product`

**Описание**: Локатор для извлечения SKU товара.

**Параметры**:
- `attribute`: `"innerText"`.
- `by`: `"XPATH"`.
- `selector`: `"//span[@class = 'barcode-specific-area']"`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.
- `locator_description`: `"SKU ivory"`.

### `id_category_default`

**Описание**: Локатор для идентификатора категории товара по умолчанию.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `new`

**Описание**: Локатор для определения нового статуса товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `cache_default_attribute`

**Описание**: Локатор для кэширования атрибутов товара по умолчанию.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `id_default_image`

**Описание**: Локатор для идентификатора изображения товара по умолчанию.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `default_image_url`

**Описание**: Локатор для извлечения URL изображения товара по умолчанию.

**Параметры**:
- `attribute`: `"src"`.
- `by`: `"XPATH"`.
- `selector`: `"//img[@id = 'img_zoom_inout']"`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.
- `mandatory`: `true`.
- `locator_description`: `"URL картинки"`.

### `id_default_combination`

**Описание**: Локатор для идентификатора комбинации товара по умолчанию.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `id_tax`

**Описание**: Локатор для идентификатора налога товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `position_in_category`

**Описание**: Локатор для позиции товара в категории.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `default_image_url`: `null`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `type`

**Описание**: Локатор для типа товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `id_shop_default`

**Описание**: Локатор для идентификатора магазина по умолчанию.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `reference`

**Описание**: Локатор для артикула товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `supplier_reference`

**Описание**: Локатор для артикула поставщика.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `location`

**Описание**: Локатор для местоположения товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `width`

**Описание**: Локатор для ширины товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `height`

**Описание**: Локатор для высоты товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `depth`

**Описание**: Локатор для глубины товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `weight`

**Описание**: Локатор для веса товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `quantity_discount`

**Описание**: Локатор для скидки на количество товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `ean13`

**Описание**: Локатор для штрихкода EAN13 товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `isbn`

**Описание**: Локатор для ISBN товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `upc`

**Описание**: Локатор для штрихкода UPC товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `mpn`

**Описание**: Локатор для MPN товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `cache_is_pack`

**Описание**: Локатор для определения, является ли товар комплектом.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `cache_has_attachments`

**Описание**: Локатор для определения, есть ли у товара вложения.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `is_virtual`

**Описание**: Локатор для определения, является ли товар виртуальным.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `state`

**Описание**: Локатор для состояния товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `additional_delivery_times`

**Описание**: Локатор для дополнительного времени доставки.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `delivery_in_stock`

**Описание**: Локатор для времени доставки товара в наличии.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `delivery_out_stock`

**Описание**: Локатор для времени доставки товара, отсутствующего в наличии.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `product_type`

**Описание**: Локатор для типа продукта.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `on_sale`

**Описание**: Локатор для определения, находится ли товар в продаже.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `online_only`

**Описание**: Локатор для определения, доступен ли товар только онлайн.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `ecotax`

**Описание**: Локатор для экологического налога товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `minimal_quantity`

**Описание**: Локатор для минимального количества товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `low_stock_threshold`

**Описание**: Локатор для порога низкого запаса товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `low_stock_alert`

**Описание**: Локатор для оповещения о низком запасе товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `price`

**Описание**: Локатор для цены товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `wholesale_price`

**Описание**: Локатор для оптовой цены товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `unity`

**Описание**: Локатор для единицы измерения товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `unit_price_ratio`

**Описание**: Локатор для коэффициента цены за единицу товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `additional_shipping_cost`

**Описание**: Локатор для дополнительной стоимости доставки.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `customizable`

**Описание**: Локатор для определения, является ли товар настраиваемым.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse`: `false`.
- `mandatory`: `true`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `text_fields`

**Описание**: Локатор для текстовых полей товара.

**Параметры**:
- `attribute`: `null`.
- `by`: `null`.
- `selector`: `null`.
- `if_list`: `"first"`.
- `use_mouse