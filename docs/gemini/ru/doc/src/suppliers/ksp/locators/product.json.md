# Описание локаторов для страницы продукта KSP

## Обзор
Файл `product.json` содержит определения локаторов для элементов страницы продукта на сайте KSP. Эти локаторы используются для взаимодействия с веб-страницей, сбора данных и выполнения различных действий.

## Содержание

1.  [Локатор `close_pop_up`](#close_pop_up)
2.  [Локатор `id`](#id)
3.  [Локатор `id_manufacturer`](#id_manufacturer)
4.  [Локатор `id_supplier`](#id_supplier)
5.  [Локатор `id_product`](#id_product)
6.  [Локатор `id_category_default`](#id_category_default)
7.  [Локатор `new`](#new)
8.  [Локатор `cache_default_attribute`](#cache_default_attribute)
9.  [Локатор `id_default_image`](#id_default_image)
10. [Локатор `default_image_url`](#default_image_url)
11. [Локатор `id_default_combination`](#id_default_combination)
12. [Локатор `id_tax`](#id_tax)
13. [Локатор `position_in_category`](#position_in_category)
14. [Локатор `type`](#type)
15. [Локатор `id_shop_default`](#id_shop_default)
16. [Локатор `reference`](#reference)
17. [Локатор `supplier_reference`](#supplier_reference)
18. [Локатор `location`](#location)
19. [Локатор `width`](#width)
20. [Локатор `height`](#height)
21. [Локатор `depth`](#depth)
22. [Локатор `weight`](#weight)
23. [Локатор `quantity_discount`](#quantity_discount)
24. [Локатор `ean13`](#ean13)
25. [Локатор `isbn`](#isbn)
26. [Локатор `upc`](#upc)
27. [Локатор `mpn`](#mpn)
28. [Локатор `cache_is_pack`](#cache_is_pack)
29. [Локатор `cache_has_attachments`](#cache_has_attachments)
30. [Локатор `is_virtual`](#is_virtual)
31. [Локатор `state`](#state)
32. [Локатор `additional_delivery_times`](#additional_delivery_times)
33. [Локатор `delivery_in_stock`](#delivery_in_stock)
34. [Локатор `delivery_out_stock`](#delivery_out_stock)
35. [Локатор `product_type`](#product_type)
36. [Локатор `on_sale`](#on_sale)
37. [Локатор `online_only`](#online_only)
38. [Локатор `ecotax`](#ecotax)
39. [Локатор `minimal_quantity`](#minimal_quantity)
40. [Локатор `low_stock_threshold`](#low_stock_threshold)
41. [Локатор `low_stock_alert`](#low_stock_alert)
42. [Локатор `price`](#price)
43. [Локатор `wholesale_price`](#wholesale_price)
44. [Локатор `unity`](#unity)
45. [Локатор `unit_price_ratio`](#unit_price_ratio)
46. [Локатор `additional_shipping_cost`](#additional_shipping_cost)
47. [Локатор `customizable`](#customizable)
48. [Локатор `text_fields`](#text_fields)
49. [Локатор `uploadable_files`](#uploadable_files)
50. [Локатор `active`](#active)
51. [Локатор `redirect_type`](#redirect_type)
52. [Локатор `id_type_redirected`](#id_type_redirected)
53. [Локатор `available_for_order`](#available_for_order)
54. [Локатор `available_date`](#available_date)
55. [Локатор `show_condition`](#show_condition)
56. [Локатор `condition`](#condition)
57. [Локатор `show_price`](#show_price)
58. [Локатор `indexed`](#indexed)
59. [Локатор `visibility`](#visibility)
60. [Локатор `advanced_stock_management`](#advanced_stock_management)
61. [Локатор `date_add`](#date_add)
62. [Локатор `date_upd`](#date_upd)
63. [Локатор `pack_stock_type`](#pack_stock_type)
64. [Локатор `meta_description`](#meta_description)
65. [Локатор `meta_keywords`](#meta_keywords)
66. [Локатор `meta_title`](#meta_title)
67. [Локатор `link_rewrite`](#link_rewrite)
68. [Локатор `name`](#name)
69. [Локатор `description_short`](#description_short)
70. [Локатор `description`](#description)
71. [Локатор `specification`](#specification)
72. [Локатор `affiliate_short_link`](#affiliate_short_link)
73. [Локатор `affiliate_text`](#affiliate_text)
74. [Локатор `affiliate_summary`](#affiliate_summary)
75. [Локатор `affiliate_summary_2`](#affiliate_summary_2)
76. [Локатор `available_now`](#available_now)
77. [Локатор `available_later`](#available_later)
78. [Локатор `associations`](#associations)
79. [Локатор `ASIN`](#asin)
80. [Локатор `Active (0/1)`](#active-01)
81. [Локатор `Name*`](#name)
82. [Локатор `Categories (x,y,z...)`](#categories-xyz)
83. [Локатор `Price tax excluded`](#price-tax-excluded)
84. [Локатор `Price tax included`](#price-tax-included)
85. [Локатор `Tax rule ID`](#tax-rule-id)
86. [Локатор `Cost price`](#cost-price)
87. [Локатор `On sale (0/1)`](#on-sale-01)
88. [Локатор `Discount amount`](#discount-amount)
89. [Локатор `Discount percent`](#discount-percent)
90. [Локатор `Discount from (yyyy-mm-dd)`](#discount-from-yyyy-mm-dd)
91. [Локатор `Discount to (yyyy-mm-dd)`](#discount-to-yyyy-mm-dd)
92. [Локатор `reference #`](#reference-)
93. [Локатор `Supplier reference #`](#supplier-reference-)
94. [Локатор `Supplier`](#supplier)
95. [Локатор `Brand`](#brand)
96. [Локатор `EAN13`](#ean13-1)
97. [Локатор `UPC`](#upc-1)
98. [Локатор `MPN`](#mpn-1)
99. [Локатор `Ecotax`](#ecotax-1)
100. [Локатор `Width`](#width-1)
101. [Локатор `Height`](#height-1)
102. [Локатор `Depth`](#depth-1)
103. [Локатор `Weight`](#weight-1)
104. [Локатор `Delivery time of in-stock products:`](#delivery-time-of-in-stock-products)
105. [Локатор `Delivery time of out-of-stock products with allowed orders:`](#delivery-time-of-out-of-stock-products-with-allowed-orders)
106. [Локатор `Quantity`](#quantity)
107. [Локатор `Minimal quantity`](#minimal-quantity-1)
108. [Локатор `Low stock level`](#low-stock-level)
109. [Локатор `Send me an email when the quantity is under this level`](#send-me-an-email-when-the-quantity-is-under-this-level)
110. [Локатор `Visibility`](#visibility-1)
111. [Локатор `Additional shipping cost`](#additional-shipping-cost-1)
112. [Локатор `Unit for base price`](#unit-for-base-price)
113. [Локатор `Base price`](#base-price)
114. [Локатор `Summary`](#summary)
115. [Локатор `Description`](#description-1)
116. [Локатор `Tags (x,y,z...)`](#tags-xyz-1)
117. [Локатор `Meta title`](#meta-title-1)
118. [Локатор `Meta keywords`](#meta-keywords-1)
119. [Локатор `Meta description`](#meta-description-1)
120. [Локатор `Rewritten URL`](#rewritten-url)
121. [Локатор `Label when in stock`](#label-when-in-stock)
122. [Локатор `Label when backorder allowed`](#label-when-backorder-allowed)
123. [Локатор `Available for order (0 = No, 1 = Yes)`](#available-for-order-0-no-1-yes)
124. [Локатор `Product availability date`](#product-availability-date)
125. [Локатор `Product creation date`](#product-creation-date)
126. [Локатор `Show price (0 = No, 1 = Yes)`](#show-price-0-no-1-yes)
127. [Локатор `Screenshot`](#screenshot-1)
128. [Локатор `images_urls`](#images_urls)
129. [Локатор `additional_images_urls`](#additional_images_urls-1)
130. [Локатор `additional_images_alts`](#additional_images_alts-1)
131. [Локатор `Delete existing images (0 = No, 1 = Yes)`](#delete-existing-images-0-no-1-yes)
132. [Локатор `Feature (Name:Value:Position:Customized)`](#feature-namevaluepositioncustomized)
133. [Локатор `Available online only (0 = No, 1 = Yes)`](#available-online-only-0-no-1-yes)
134. [Локатор `Condition`](#condition-1)
135. [Локатор `Customizable (0 = No, 1 = Yes)`](#customizable-0-no-1-yes)
136. [Локатор `Uploadable files (0 = No, 1 = Yes)`](#uploadable-files-0-no-1-yes)
137. [Локатор `Text fields (0 = No, 1 = Yes)`](#text-fields-0-no-1-yes)
138. [Локатор `Action when out of stock`](#action-when-out-of-stock)
139. [Локатор `Virtual product (0 = No, 1 = Yes)`](#virtual-product-0-no-1-yes)
140. [Локатор `File URL`](#file-url)
141. [Локатор `Number of allowed downloads`](#number-of-allowed-downloads)
142. [Локатор `Expiration date (yyyy-mm-dd)`](#expiration-date-yyyy-mm-dd)
143. [Локатор `Number of days`](#number-of-days)
144. [Локатор `ID / Name of shop`](#id--name-of-shop)
145. [Локатор `Advanced Stock Management`](#advanced-stock-management-1)
146. [Локатор `Depends on stock`](#depends-on-stock)
147. [Локатор `Warehouse`](#warehouse)
148. [Локатор `Accessories (x,y,z...)`](#accessories-xyz)
149. [Локатор `affiliate short link`](#affiliate-short-link-1)
150. [Локатор `affiliate text`](#affiliate-text-1)
151. [Локатор `affiliate summary`](#affiliate-summary-1)
152. [Локатор `affiliate summary 2`](#affiliate-summary-2-1)
153. [Локатор `Open AI Product Description`](#open-ai-product-description)
154. [Локатор `Byer protection`](#byer-protection)
155. [Локатор `Specification`](#specification-1)
156. [Локатор `Refirbished product description`](#refirbished-product-description)
157. [Локатор `Additional shipping details`](#additional-shipping-details)

## Локаторы

### `close_pop_up`
**Описание**: Локатор для кнопки закрытия всплывающего окна.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (str): Метод поиска элемента - XPATH.
- `selector` (str): XPATH селектор `//button[@class='close']`.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (str): Событие для элемента - `click()`.
- `mandatory` (bool): Обязательный локатор - true.
- `locator_description` (str): Описание локатора - "Закрыти попап окна".

### `id`
**Описание**: Локатор для ID продукта.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `id_manufacturer`
**Описание**: Локатор для SKU производителя.
    
**Параметры**:
- `attribute` (str): Атрибут для извлечения - "innerText".
- `by` (str): Метод поиска элемента - XPATH.
- `selector` (str): XPATH селектор `//span[@class = 'ltr sku-copy']`.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.
- `locator_description` (str): Описание локатора - "SKU manufacturer".

### `id_supplier`
**Описание**: Локатор для SKU KSP.
    
**Параметры**:
- `attribute` (int): Атрибут для извлечения - 2787.
- `by` (str): Метод поиска элемента - VALUE.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 2 секунды.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.
- `locator_description` (str): Описание локатора - "SKU ksp".

### `id_product`
**Описание**: Локатор для ID продукта KSP.
    
**Параметры**:
- `attribute` (str): Атрибут для извлечения - "innerText".
- `by` (str): Метод поиска элемента - XPATH.
- `selector` (str): XPATH селектор `(//div[contains(@data-id, 'product-')])[1]//span`.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 2 секунды.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.
- `locator_description` (str): Описание локатора - "SKU ksp".

### `id_category_default`
**Описание**: Локатор для ID категории по умолчанию.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `new`
**Описание**: Локатор для нового товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `cache_default_attribute`
**Описание**: Локатор для кэшированного атрибута по умолчанию.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `id_default_image`
**Описание**: Локатор для ID изображения по умолчанию.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `default_image_url`
**Описание**: Локатор для URL изображения по умолчанию.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (str): Метод поиска элемента - XPATH.
- `selector` (str): XPATH селектор `(//li[@class = 'slide selected previous'])[1]//img`.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (str): Событие для элемента - `screenshot()`.
- `locator_description` (str): Описание локатора не указано.

### `id_default_combination`
**Описание**: Локатор для ID комбинации по умолчанию.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `id_tax`
**Описание**: Локатор для ID налога.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `position_in_category`
**Описание**: Локатор для позиции в категории.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `type`
**Описание**: Локатор для типа продукта.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `id_shop_default`
**Описание**: Локатор для ID магазина по умолчанию.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `reference`
**Описание**: Локатор для референса товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `supplier_reference`
**Описание**: Локатор для референса поставщика.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `location`
**Описание**: Локатор для местоположения товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `width`
**Описание**: Локатор для ширины товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `height`
**Описание**: Локатор для высоты товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `depth`
**Описание**: Локатор для глубины товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `weight`
**Описание**: Локатор для веса товара.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `quantity_discount`
**Описание**: Локатор для скидки по количеству.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор - true.
- `timeout` (int): Тайм-аут ожидания элемента - 0 секунд.
- `timeout_for_event` (str): Тайм-аут ожидания события - `presence_of_element_located`.
- `event` (null): Событие не указано.

### `ean13`
**Описание**: Локатор для EAN13.
    
**Параметры**:
- `attribute` (null): Атрибут для поиска не указан.
- `by` (null): Метод поиска не указан.
- `selector` (null): Селектор не указан.
- `if_list` (str): Если найдено несколько элементов, выбираем "first" (первый).
- `use_mouse` (bool): Не использовать мышь.
- `mandatory` (bool): Обязательный локатор -