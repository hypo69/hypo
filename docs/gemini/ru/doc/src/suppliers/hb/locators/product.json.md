# Локаторы для страницы продукта HB

## Обзор

Этот файл содержит JSON-структуру, определяющую локаторы для различных элементов на странице продукта HB. Локаторы используются для автоматизированного взаимодействия с элементами веб-страницы при парсинге данных.

## Содержание

- [close_banner](#close_banner)
- [id](#id)
- [id_manufacturer](#id_manufacturer)
- [id_supplier](#id_supplier)
- [id_product](#id_product)
- [id_category_default](#id_category_default)
- [condition](#condition)
- [cache_default_attribute](#cache_default_attribute)
- [default_image_url](#default_image_url)
- [id_default_combination](#id_default_combination)
- [id_tax](#id_tax)
- [position_in_category](#position_in_category)
- [type](#type)
- [id_shop_default](#id_shop_default)
- [product_reference_and_volume_and_price_for_100](#product_reference_and_volume_and_price_for_100)
- [reference](#reference)
- [supplier_reference](#supplier_reference)
- [additional_images_urls](#additional_images_urls)
- [additional_images_alts](#additional_images_alts)
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
- [out_of_stock](#out_of_stock)
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
- [description](#description)
- [specification](#specification)
- [description_short](#description_short)
- [affiliate_short_link](#affiliate_short_link)
- [affiliate_text](#affiliate_text)
- [affiliate_summary](#affiliate_summary)
- [affiliate_summary_2](#affiliate_summary_2)
- [affiliate_image_small](#affiliate_image_small)
- [affiliate_image_medium](#affiliate_image_medium)
- [affiliate_image_large](#affiliate_image_large)
- [ingredients](#ingredients)
- [how_to_use](#how_to_use)
- [specification](#specification-1)
- [available_now](#available_now)
- [available_later](#available_later)
- [quantity](#quantity)
- [link_to_video](#link_to_video)
- [associations](#associations)
- [Active (0/1)](#active-01)
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
- [Brand](#brand)
- [Low stock level](#low-stock-level)
- [Send me an email when the quantity is under this level](#send-me-an-email-when-the-quantity-is-under-this-level)
- [Tags (x,y,z...)](#tags-xyz)
- [Label when in stock](#label-when-in-stock)
- [Label when backorder allowed](#label-when-backorder-allowed)
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
- [Advanced Stock Management](#advanced-stock-management-1)
- [Depends on stock](#depends-on-stock)
- [Warehouse](#warehouse)
- [Accessories (x,y,z...)](#accessories-xyz)
- [Open AI Product Description](#open-ai-product-description)
- [Byer protection](#byer-protection)
- [Specification](#specification-2)
- [Refirbished product description](#refirbished-product-description)
- [Additional shipping details](#additional-shipping-details)

## Локаторы

### `close_banner`

**Описание**: Локатор для кнопки закрытия всплывающего окна. Используется XPATH. Закрывает pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`).

**Параметры**:
- `attribute`: `null`
- `by`: `XPATH`
- `selector`: `//button[@id = 'closeXButton']`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `click()`
- `locator_description`: `Закрываю pop-up окно, если оно не появилось - не страшно (\`mandatory\`:\`false\`)`

### `id`

**Описание**: Локатор для `id` товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `id`

### `id_manufacturer`

**Описание**: Локатор для `id` производителя товара.

**Параметры**:
- `attribute`: `11290`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `id_manufacturer`

### `id_supplier`

**Описание**: Локатор для `id` поставщика товара.

**Параметры**:
- `attribute`: `11267`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `HB id_supplier`

### `id_product`

**Описание**: Локатор для `id` товара.

**Параметры**:
- `attribute`: `""`
- `by`: `XPATH`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `HB id_product`

### `id_category_default`

**Описание**: Локатор для `id` категории товара по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `id_category_default`

### `condition`

**Описание**: Локатор для условия товара (новый/б.у.).

**Параметры**:
- `attribute`: `"new"`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `condition`

### `cache_default_attribute`

**Описание**: Локатор для кэшированного атрибута по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `cache_default_attribute`

### `default_image_url`

**Описание**: Локатор для URL-адреса изображения товара по умолчанию.

**Параметры**:
- `attribute`: `src`
- `by`: `XPATH`
- `selector`: `//img[contains(@class, 'zoomImg')]`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `default_image_url`

### `id_default_combination`

**Описание**: Локатор для `id` комбинации товара по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `id_default_combination`

### `id_tax`

**Описание**: Локатор для `id` налога на товар.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `id_tax`

### `position_in_category`

**Описание**: Локатор для позиции товара в категории.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `position_in_category`

### `type`

**Описание**: Локатор для типа товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `type`

### `id_shop_default`

**Описание**: Локатор для `id` магазина по умолчанию.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `id_shop_default`

### `product_reference_and_volume_and_price_for_100`

**Описание**: Локатор для получения данных об артикуле, объеме и цене за 100 гр. На сайте кривой HTML, поэтому одним локатором вытескиваю 3 значения, а потом делаю парсинг. Приходит список из четырех объектов: объем, цена за 100 гр, артикул, пустой div.

**Параметры**:
- `attribute`: `null`
- `by`: `XPATH`
- `selector`: `//div[@data-widget_type='shortcode.default']`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `На сайте кривой HTML, поэтому одним локатором вытескиваю 3 значения, а потом делаю парсинг. Приходит список из четырех объектов: объем, цена за 100 гр, артикул, пустой div`

### `reference`

**Описание**: Локатор для артикула товара. Собирается в коде из `supplier.supplier_id` + `f.supplier_reference`.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `reference Собирается в коде из supplier.supplier_id + f.supplier_reference`

### `supplier_reference`

**Описание**: Локатор для артикула поставщика. Получаю через локатор `product_reference_and_volume_and_price_for_100`.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `supplier_reference Получаю через локатор product_reference_and_volume_and_price_for_100`

### `additional_images_urls`

**Описание**: Локатор для получения URL-адресов дополнительных изображений товара.

**Параметры**:
- `attribute`: `src`
- `by`: `XPATH`
- `selector`: `//ol[contains(@class, 'flex-control-thumbs')]//img`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `additional_images_alts`

**Описание**: Локатор для получения атрибутов `alt` дополнительных изображений товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`

### `location`

**Описание**: Локатор для местоположения товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `location`

### `width`

**Описание**: Локатор для ширины товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `width`

### `height`

**Описание**: Локатор для высоты товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `height`

### `depth`

**Описание**: Локатор для глубины товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `depth`

### `weight`

**Описание**: Локатор для веса товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `weight`

### `quantity_discount`

**Описание**: Локатор для скидки по количеству.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `quantity_discount`

### `ean13`

**Описание**: Локатор для EAN13 кода.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `ean13`

### `isbn`

**Описание**: Локатор для ISBN кода.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `isbn`

### `upc`

**Описание**: Локатор для UPC кода.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `upc`

### `mpn`

**Описание**: Локатор для MPN кода.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `mpn`

### `cache_is_pack`

**Описание**: Локатор для кэшированного значения, является ли товар набором.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `cache_is_pack`

### `cache_has_attachments`

**Описание**: Локатор для кэшированного значения, имеет ли товар вложения.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `cache_has_attachments`

### `is_virtual`

**Описание**: Локатор для флага, является ли товар виртуальным.

**Параметры**:
- `attribute`: `"0"`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `is_virtual`

### `out_of_stock`

**Описание**: Локатор для определения, есть ли товар в наличии.

**Параметры**:
- `attribute`: `null`
- `by`: `XPATH`
- `selector`: `//p[contains(@class, 'out-of-stock')]`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `out_of_stock`

### `state`

**Описание**: Локатор для состояния товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `state`

### `additional_delivery_times`

**Описание**: Локатор для дополнительного времени доставки.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `additional_delivery_times`

### `delivery_in_stock`

**Описание**: Локатор для способа доставки товара в наличии.

**Параметры**:
- `attribute`: `"Israel Post"`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `delivery_in_stock (Israel Post)`

### `delivery_out_stock`

**Описание**: Локатор для способа доставки товара, которого нет в наличии.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `delivery_out_stock`

### `product_type`

**Описание**: Локатор для типа товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `product_type`

### `on_sale`

**Описание**: Локатор для флага, находится ли товар в распродаже.

**Параметры**:
- `attribute`: `0`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `on_sale`

### `online_only`

**Описание**: Локатор для флага, продается ли товар только онлайн.

**Параметры**:
- `attribute`: `1`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `online_only`

### `ecotax`

**Описание**: Локатор для эко-налога.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `ecotax`

### `minimal_quantity`

**Описание**: Локатор для минимального количества товара для заказа.

**Параметры**:
- `attribute`: `1`
- `by`: `VALUE`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `minimal_quantity`

### `low_stock_threshold`

**Описание**: Локатор для порога низкого запаса.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `low_stock_threshold`

### `low_stock_alert`

**Описание**: Локатор для оповещения о низком запасе.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `low_stock_alert`

### `price`

**Описание**: Локатор для цены товара.

**Параметры**:
- `attribute`: `"innerText"`
- `by`: `XPATH`
- `selector`: `//p[@class='price']`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `true`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `price`

### `wholesale_price`

**Описание**: Локатор для оптовой цены товара.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `wholesale_price`

### `unity`

**Описание**: Локатор для единицы измерения.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_of_element_located`
- `event`: `null`
- `locator_description`: `unity`

### `unit_price_ratio`

**Описание**: Локатор для коэффициента цены за единицу.

**Параметры**:
- `attribute`: `null`
- `by`: `null`
- `selector`: `null`
- `if_list`: `first`
- `use_mouse`: `false`
- `mandatory`: `false`
- `timeout`: `0`
- `timeout_for_event`: `presence_