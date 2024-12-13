# `product.json`

## Обзор

Файл `product.json` содержит конфигурацию локаторов для извлечения данных о продуктах с веб-страниц. Этот файл определяет, какие атрибуты продукта нужно извлечь, как их найти на странице (с помощью CSS-селекторов или XPath), и другие параметры, такие как обязательность, тайм-аут и т.д.

## Оглавление

- [Обзор](#обзор)
- [Локаторы](#локаторы)

## Локаторы

### `id`
**Описание**: Локатор для идентификатора продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `VALUE`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `id_manufacturer`
**Описание**: Локатор для идентификатора производителя.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `id_supplier`
**Описание**: Локатор для идентификатора поставщика.
**Атрибуты**:
  - `attribute`: `11234`
  - `by`: `VALUE`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `id_category_default`
**Описание**: Локатор для идентификатора категории по умолчанию.
**Атрибуты**:
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
**Описание**: Локатор для определения, является ли продукт новым.
**Атрибуты**:
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
**Описание**: Локатор для кэшированного атрибута по умолчанию.
**Атрибуты**:
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
**Описание**: Локатор для идентификатора изображения по умолчанию.
**Атрибуты**:
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
**Описание**: Локатор для идентификатора комбинации по умолчанию.
**Атрибуты**:
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
**Описание**: Локатор для идентификатора налога.
**Атрибуты**:
  - `attribute`: `$p.tax_rule`
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
**Атрибуты**:
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
**Атрибуты**:
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
**Атрибуты**:
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
**Описание**: Локатор для референса продукта.
**Атрибуты**:
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
**Описание**: Локатор для референса поставщика.
**Атрибуты**:
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
**Описание**: Локатор для местоположения.
**Атрибуты**:
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
**Атрибуты**:
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
**Атрибуты**:
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
**Атрибуты**:
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
**Атрибуты**:
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
**Описание**: Локатор для скидки на количество.
**Атрибуты**:
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
**Описание**: Локатор для EAN13.
**Атрибуты**:
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
**Описание**: Локатор для ISBN.
**Атрибуты**:
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
**Описание**: Локатор для UPC.
**Атрибуты**:
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
**Описание**: Локатор для MPN.
**Атрибуты**:
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
**Описание**: Локатор для кэшированной информации о том, является ли продукт набором.
**Атрибуты**:
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
**Описание**: Локатор для кэшированной информации о наличии вложений.
**Атрибуты**:
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
**Описание**: Локатор для определения, является ли продукт виртуальным.
**Атрибуты**:
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
**Атрибуты**:
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
**Описание**: Локатор для дополнительного времени доставки.
**Атрибуты**:
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
**Описание**: Локатор для времени доставки товаров в наличии.
**Атрибуты**:
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
**Описание**: Локатор для времени доставки товаров, которых нет в наличии.
**Атрибуты**:
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
**Атрибуты**:
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
**Описание**: Локатор для определения, находится ли продукт на распродаже.
**Атрибуты**:
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
**Описание**: Локатор для определения, продается ли продукт только онлайн.
**Атрибуты**:
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
**Описание**: Локатор для эко-налога.
**Атрибуты**:
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
**Описание**: Локатор для минимального количества для заказа.
**Атрибуты**:
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
**Описание**: Локатор для порога низкого запаса.
**Атрибуты**:
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
**Описание**: Локатор для оповещения о низком запасе.
**Атрибуты**:
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
**Атрибуты**:
  - `attribute`: `innerText`
  - `by`: `XPATH`
  - `selector`: `//div[contains(@data-csa-c-asin, '$_(driver.current_url.split(f\'\'\'/\'\'\')[-2])_$') and contains(@id, 'corePrice_desktop')]// span[contains(@class, 'apexPriceToPay')]//span`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `wholesale_price`
**Описание**: Локатор для оптовой цены.
**Атрибуты**:
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
**Описание**: Локатор для единицы измерения.
**Атрибуты**:
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
**Описание**: Локатор для отношения цены за единицу.
**Атрибуты**:
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
**Описание**: Локатор для дополнительной стоимости доставки.
**Атрибуты**:
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
**Описание**: Локатор для определения, является ли продукт настраиваемым.
**Атрибуты**:
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
**Описание**: Локатор для текстовых полей.
**Атрибуты**:
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
**Описание**: Локатор для загружаемых файлов.
**Атрибуты**:
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
**Описание**: Локатор для определения активности продукта.
**Атрибуты**:
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
**Описание**: Локатор для типа редиректа.
**Атрибуты**:
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
**Описание**: Локатор для идентификатора перенаправленного типа.
**Атрибуты**:
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
**Описание**: Локатор для определения, доступен ли продукт для заказа.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `available_date`
**Описание**: Локатор для даты доступности продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `show_condition`
**Описание**: Локатор для определения, отображать ли состояние продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `condition`
**Описание**: Локатор для состояния продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `show_price`
**Описание**: Локатор для определения, отображать ли цену продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `indexed`
**Описание**: Локатор для определения, проиндексирован ли продукт.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `visibility`
**Описание**: Локатор для видимости продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `advanced_stock_management`
**Описание**: Локатор для определения, используется ли расширенное управление запасами.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `date_add`
**Описание**: Локатор для даты добавления продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `date_upd`
**Описание**: Локатор для даты обновления продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `pack_stock_type`
**Описание**: Локатор для типа запаса набора.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `meta_description`
**Описание**: Локатор для мета-описания продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `meta_keywords`
**Описание**: Локатор для мета-ключевых слов продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `meta_title`
**Описание**: Локатор для мета-заголовка продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `link_rewrite`
**Описание**: Локатор для перезаписи ссылки.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `name`
**Описание**: Локатор для имени продукта.
**Атрибуты**:
  - `attribute`: `innerText`
  - `by`: `XPATH`
  - `selector`: `//span[@id='productTitle']`
  - `if_list`: `first`
  - `use_mouse`: `false`
  - `mandatory`: `true`
  - `timeout`: `0`
  - `timeout_for_event`: `presence_of_element_located`
  - `event`: `null`

### `description`
**Описание**: Локатор для описания продукта.
**Атрибуты**:
  - `attribute`: `null`
  - `by`: `null`
  - `selector`: `null`
  - `if