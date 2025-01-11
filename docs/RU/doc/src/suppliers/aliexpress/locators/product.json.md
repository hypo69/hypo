# Документация для `hypotez/src/suppliers/aliexpress/locators/product.json`

## Обзор

Данный файл `product.json` содержит JSON-объект, описывающий локаторы для элементов веб-страницы, используемые для сбора данных о продуктах с AliExpress. Каждый локатор определяет, как найти конкретный элемент на странице, какие данные из него извлечь, и какие действия с ним необходимо выполнить.

## Оглавление

1.  [Обзор](#обзор)
2.  [Описание структуры локаторов](#описание-структуры-локаторов)
3.  [Детальное описание локаторов](#детальное-описание-локаторов)

## Описание структуры локаторов

Каждый локатор в файле представлен в виде JSON-объекта со следующими ключами:

-   `attribute` (str | int | list | null): Атрибут элемента, который необходимо извлечь. Если `null`, извлекается текст или HTML.
-   `by` (str | null): Метод поиска элемента, например, `XPATH`, `VALUE`. Если `null`, используется внутренний поиск по названию поля.
-   `selector` (str | null): Строка для поиска элемента, например, XPATH-выражение.
-   `if_list` (str): Указывает, что делать, если найдено несколько элементов: `'first'` - выбрать первый, `'all'` - выбрать все.
-   `use_mouse` (bool): Если `true`, для взаимодействия с элементом используется мышь.
-   `mandatory` (bool): Если `true`, отсутствие элемента приведет к ошибке.
-   `timeout` (int): Максимальное время ожидания элемента в секундах.
-   `timeout_for_event` (str): Событие для ожидания, например, `presence_of_element_located`.
-   `event` (str | list | null): Событие для взаимодействия с элементом, например, `'click()'` или `null`.
-  `logic for action[AND|OR|XOR|VALUE|null]` (str | null): Логика для составного селектора
-   `locator_description` (str): Описание назначения локатора.

## Детальное описание локаторов

### `close_banner`

**Описание**: Локатор для кнопки закрытия всплывающего окна.

**Параметры**:
-   `attribute`: `null`
-   `by`: `XPATH`
-   `selector`: `//button[@id = 'closeXButton']`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `click()`
-   `locator_description`: "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"

### `id`

**Описание**: Локатор для идентификатора продукта.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id"

### `id_manufacturer`

**Описание**: Локатор для идентификатора производителя.

**Параметры**:
-   `attribute`: `11290`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_manufacturer"

### `id_supplier`

**Описание**: Локатор для идентификатора поставщика.

**Параметры**:
-   `attribute`: `11267`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_supplier"

### `id_category_default`

**Описание**: Локатор для идентификатора категории по умолчанию.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_category_default"

### `condition`

**Описание**: Локатор для условия товара (новый, б/у и т.д.).

**Параметры**:
-   `attribute`: `"new"`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "condition"

### `cache_default_attribute`

**Описание**: Локатор для кэширования атрибута по умолчанию.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "cache_default_attribute"

### `default_image_url`

**Описание**: Локатор для URL изображения по умолчанию.

**Параметры**:
-   `attribute`: `src`
-   `by`: `XPATH`
-   `selector`: `//img[contains(@class, 'zoomImg')]`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "default_image_url"

### `id_default_combination`

**Описание**: Локатор для идентификатора комбинации по умолчанию.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_default_combination"

### `id_tax`

**Описание**: Локатор для идентификатора налога.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_tax"

### `position_in_category`

**Описание**: Локатор для позиции товара в категории.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "position_in_category"

### `type`

**Описание**: Локатор для типа товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "type"

### `id_shop_default`

**Описание**: Локатор для идентификатора магазина по умолчанию.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_shop_default"

### `product_reference_and_volume_and_price_for_100`

**Описание**: Локатор для получения данных о референсе, объеме и цене за 100 грамм.

**Параметры**:
-   `attribute`: `null`
-   `by`: `XPATH`
-   `selector`: `//div[@data-widget_type='shortcode.default']`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "На сайте кривой HTML, поэтому одним локатором вытескиваю 3 значения, а потом делаю парсинг. Приходит список из четырех объектов: объем, цена за 100 гр, артикул, пустой div"

### `reference`

**Описание**: Локатор для получения референса товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "reference Собирается в коде из supplier.supplier_id + f.supplier_reference"

### `supplier_reference`

**Описание**: Локатор для референса поставщика.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-  `selector`: `null`
-  `logic for action[AND|OR|XOR|VALUE|null]`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "supplier_reference Получаю через локатор product_reference_and_volume_and_price_for_100"

### `additional_images_urls`

**Описание**: Локатор для получения URL дополнительных изображений.

**Параметры**:
-   `attribute`: `src`
-   `by`: `XPATH`
-   `selector`: `//ol[contains(@class, 'flex-control-thumbs')]//img`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`

### `additional_images_alts`

**Описание**: Локатор для получения атрибутов alt дополнительных изображений.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`

### `location`

**Описание**: Локатор для местоположения товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "location"

### `width`

**Описание**: Локатор для ширины товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "width"

### `height`

**Описание**: Локатор для высоты товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "height"

### `depth`

**Описание**: Локатор для глубины товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "depth"

### `weight`

**Описание**: Локатор для веса товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `logic for action[AND|OR|XOR|VALUE|null]`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "weight"

### `quantity_discount`

**Описание**: Локатор для скидок при покупке определенного количества товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "quantity_discount"

### `ean13`

**Описание**: Локатор для EAN13 кода товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "ean13"

### `isbn`

**Описание**: Локатор для ISBN кода товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "isbn"

### `upc`

**Описание**: Локатор для UPC кода товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "upc"

### `mpn`

**Описание**: Локатор для MPN кода товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "mpn"

### `cache_is_pack`

**Описание**: Локатор для проверки, является ли товар набором.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "cache_is_pack"

### `cache_has_attachments`

**Описание**: Локатор для проверки, есть ли у товара вложения.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "cache_has_attachments"

### `is_virtual`

**Описание**: Локатор для определения, является ли товар виртуальным.

**Параметры**:
-   `attribute`: `"0"`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "is_virtual"

### `out_of_stock`

**Описание**: Локатор для проверки, есть ли товар в наличии.

**Параметры**:
-   `attribute`: `null`
-   `by`: `XPATH`
-   `selector`: `//p[contains(@class, 'out-of-stock')]`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-    `event`: `null`
-   `locator_description`: "out_of_stock"

### `state`

**Описание**: Локатор для состояния товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "state"

### `additional_delivery_times`

**Описание**: Локатор для получения дополнительного времени доставки.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "additional_delivery_times"

### `delivery_in_stock`

**Описание**: Локатор для определения способа доставки товара в наличии.

**Параметры**:
-   `attribute`: `"Israel Post"`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "delivery_in_stock (Israel Post)"

### `delivery_out_stock`

**Описание**: Локатор для определения способа доставки товара, которого нет в наличии.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "delivery_out_stock"

### `product_type`

**Описание**: Локатор для типа продукта.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "product_type"

### `on_sale`

**Описание**: Локатор для определения, является ли товар акционным.

**Параметры**:
-   `attribute`: `0`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "on_sale"

### `online_only`

**Описание**: Локатор для определения, является ли товар доступным только онлайн.

**Параметры**:
-   `attribute`: `1`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "online_only"

### `ecotax`

**Описание**: Локатор для определения экологического налога.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "ecotax"

### `minimal_quantity`

**Описание**: Локатор для минимального количества товара для заказа.

**Параметры**:
-   `attribute`: `1`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "minimal_quantity"

### `low_stock_threshold`

**Описание**: Локатор для порога низкого уровня запасов.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "low_stock_threshold"

### `low_stock_alert`

**Описание**: Локатор для оповещения о низком уровне запасов.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "low_stock_alert"

### `price`

**Описание**: Локатор для цены товара.

**Параметры**:
-   `attribute`: `"innerText"`
-   `by`: `XPATH`
-   `selector`: `//p[@class='price']`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "price"

### `wholesale_price`

**Описание**: Локатор для оптовой цены товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "wholesale_price"

### `unity`

**Описание**: Локатор для единицы измерения.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "unity"

### `unit_price_ratio`

**Описание**: Локатор для коэффициента цены за единицу.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "unit_price_ratio"

### `additional_shipping_cost`

**Описание**: Локатор для дополнительной стоимости доставки.

**Параметры**:
-   `attribute`: `30`
-   `by`: `VALUE`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `true`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "Стоимость отправки. 30 шек. by: VALUE означает, что я беру значение из attribute"

### `customizable`

**Описание**: Локатор для определения, можно ли кастомизировать товар.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "customizable"

### `text_fields`

**Описание**: Локатор для текстовых полей кастомизации товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "text_fields"

### `uploadable_files`

**Описание**: Локатор для загружаемых файлов кастомизации товара.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "uploadable_files"

### `active`

**Описание**: Локатор для определения, является ли товар активным.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "active"

### `redirect_type`

**Описание**: Локатор для типа редиректа.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "redirect_type"

### `id_type_redirected`

**Описание**: Локатор для идентификатора перенаправленного типа.

**Параметры**:
-   `attribute`: `null`
-   `by`: `null`
-   `selector`: `null`
-   `if_list`: `first`
-   `use_mouse`: `false`
-   `mandatory`: `false`
-   `timeout`: `0`
-   `timeout_for_event`: `presence_of_element_located`
-   `event`: `null`
-   `locator_description`: "id_type_redirected"

### `available_for_order`

**Описание**: Локатор для определения, доступен ли товар для заказа.

**Параметры**:
-   `attribute`: `null