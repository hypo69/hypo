# Модуль `product_fields`

## Обзор

Модуль `product_fields` предназначен для описания полей товара в формате API PrestaShop. Он включает класс `ProductFields`, который содержит информацию о каждом поле товара, используемом в таблицах PrestaShop. Этот модуль также обеспечивает функциональность для определения языка текста с использованием библиотеки `langdetect`.

## Содержание

- [Классы](#классы)
    - [`ProductFields`](#productfields)
- [Функции](#функции)
    - [`_load_product_fields_list`](#_load_product_fields_list)
    - [`_payload`](#_payload)
- [Свойства](#свойства)
    - [`associations`](#associations)
    - [`id_product`](#id_product)
    - [`id_supplier`](#id_supplier)
    - [`id_manufacturer`](#id_manufacturer)
    - [`id_category_default`](#id_category_default)
    - [`additional_categories`](#additional_categories)
    - [`id_shop_default`](#id_shop_default)
    - [`id_shop`](#id_shop)
    - [`id_tax`](#id_tax)
    - [`on_sale`](#on_sale)
    - [`online_only`](#online_only)
    - [`ean13`](#ean13)
    - [`isbn`](#isbn)
    - [`upc`](#upc)
    - [`mpn`](#mpn)
    - [`ecotax`](#ecotax)
    - [`minimal_quantity`](#minimal_quantity)
    - [`low_stock_threshold`](#low_stock_threshold)
    - [`low_stock_alert`](#low_stock_alert)
    - [`price`](#price)
    - [`wholesale_price`](#wholesale_price)
    - [`unity`](#unity)
    - [`unit_price_ratio`](#unit_price_ratio)
    - [`additional_shipping_cost`](#additional_shipping_cost)
    - [`reference`](#reference)
    - [`supplier_reference`](#supplier_reference)
    - [`location`](#location)
    - [`width`](#width)
    - [`height`](#height)
    - [`depth`](#depth)
    - [`weight`](#weight)
    - [`volume`](#volume)
    - [`out_of_stock`](#out_of_stock)
    - [`additional_delivery_times`](#additional_delivery_times)
    - [`quantity_discount`](#quantity_discount)
    - [`customizable`](#customizable)
    - [`uploadable_files`](#uploadable_files)
    - [`text_fields`](#text_fields)
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
    - [`cache_is_pack`](#cache_is_pack)
    - [`cache_has_attachments`](#cache_has_attachments)
    - [`is_virtual`](#is_virtual)
    - [`cache_default_attribute`](#cache_default_attribute)
    - [`date_add`](#date_add)
    - [`date_upd`](#date_upd)
    - [`advanced_stock_management`](#advanced_stock_management)
    - [`pack_stock_type`](#pack_stock_type)
    - [`state`](#state)
    - [`product_type`](#product_type)
    - [`description`](#description)
    - [`description_short`](#description_short)
    - [`link_rewrite`](#link_rewrite)
    - [`meta_description`](#meta_description)
    - [`meta_keywords`](#meta_keywords)
    - [`meta_title`](#meta_title)
    - [`name`](#name)
    - [`available_now`](#available_now)
    - [`available_later`](#available_later)
    - [`delivery_in_stock`](#delivery_in_stock)
    - [`delivery_out_stock`](#delivery_out_stock)
    - [`delivery_additional_message`](#delivery_additional_message)
    - [`affiliate_short_link`](#affiliate_short_link)
    - [`affiliate_text`](#affiliate_text)
    - [`affiliate_summary`](#affiliate_summary)
    - [`affiliate_summary_2`](#affiliate_summary_2)
    - [`affiliate_image_small`](#affiliate_image_small)
    - [`affiliate_image_medium`](#affiliate_image_medium)
    - [`affiliate_image_large`](#affiliate_image_large)
    - [`ingredients`](#ingredients)
    - [`specification`](#specification)
    - [`how_to_use`](#how_to_use)
    - [`id_default_image`](#id_default_image)
    - [`link_to_video`](#link_to_video)
    - [`images_urls`](#images_urls)
    - [`local_image_path`](#local_image_path)
    - [`local_video_path`](#local_video_path)
    - [`position_in_category`](#position_in_category)
    - [`page_lang`](#page_lang)
  

## Классы

### `ProductFields`

**Описание**: Класс, описывающий поля товара в формате API PrestaShop.

**Методы**:

- `__init__`:
    - **Описание**: Инициализация класса. Загружаются данные полей, языков и их идентификаторов.
- `_load_product_fields_list`:
    - **Описание**: Загрузка списка полей из файла.
    - **Возвращает**:
        - `List[str]`: Список полей, загруженных из текстового файла.
- `_payload`:
    - **Описание**: Загрузка дефолтных значений полей.
    - **Возвращает**:
        - `bool`: `True`, если загрузка прошла успешно, иначе `False`.

## Функции

### `_load_product_fields_list`

**Описание**: Загрузка списка полей из файла.

**Возвращает**:
   - `List[str]`: Список полей, загруженных из текстового файла.

### `_payload`

**Описание**: Загрузка дефолтных значений полей.

**Возвращает**:
   - `bool`: True, если загрузка прошла успешно, иначе False.

## Свойства

### `associations`

- **Описание**: Возвращает или устанавливает словарь ключей ассоциаций.
- **Тип**: `Optional[Dict]`
- **Setter**: `associations(self, value: Dict[str, Optional[str]])`
    - **Описание**: Устанавливает словарь ассоциаций.

### `id_product`

- **Описание**: `ps_product.id: int(10) unsigned`
- **Тип**: `Optional[int]`
- **Setter**: `id_product(self, value: int = None)`
    - **Описание**: ID товара. Для нового тoвара id назначется из `PrestaShop`.
    - **Параметры**:
        - `value` (`int`, optional): ID товара. Требуется при операциях над существующим товаром. По умолчанию `None`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`
### `id_supplier`

- **Описание**: `ps_product.id_supplier: int(10) unsigned`
- **Тип**: `Optional[int]`
- **Setter**: `id_supplier(self, value: int = None)`
    - **Описание**: Привязываю товар к id поставщика
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `id_manufacturer`

- **Описание**: `ps_product.id_manufacturer: int(10) unsigned`
- **Тип**: `int`
- **Setter**: `id_manufacturer(self, value: int = None)`
     - **Описание**:  Бренд может быть передан как по имени так и по ID.
     - **Параметры**:
        - `value` (`int`, optional): ID бренда. По умолчанию `None`.

###  `id_category_default`

- **Описание**: `ps_product.id_category_default: int(10) unsigned`
- **Тип**: `int`
- **Setter**: `id_category_default(self, value: int)`
   -  **Описание**:  Сюда передается та категория, которая будет однозначно - родительская `ps_product.id_category_default: int(10) unsigned`

### `additional_categories`

- **Описание**: Возвращает словарь категорий товара из файла сценария, таблица `ps_category_product`.
- **Тип**: `dict | None`
- **Setter**: `additional_categories(self, value: int | list[int])`
    - **Описание**: Дополнительные к основной категории. При задании доп ключей предыдущие значения заменяются новыми.

### `id_shop_default`

- **Описание**: `ps_product.id_shop_default: int(10) unsigned`
- **Тип**: `int`
- **Setter**: `id_shop_default(self, value: int = None)`
     - **Описание**: `ID` магазина заказчика

### `id_shop`

- **Описание**: `ps_product.id_shop_default: int(10) unsigned`
- **Тип**: `int`
- **Setter**: `id_shop(self, value: int = None)`
     - **Описание**: `ID` магазина заказчика

### `id_tax`

- **Описание**: `ps_product.id_tax: int(10) unsigned`
- **Тип**: `int`
- **Setter**: `id_tax(self, value: int)`
    - **Описание**: `ID` ндс. מע''מ = 13

### `on_sale`

- **Описание**: `ps_product.on_sale: tinyint(1)  unsigned`
- **Тип**: `int`
- **Setter**: `on_sale(self, value = 0 )`
    - **Описание**: `1` - распродажа. По умолчанию 0.
    - **Возвращает**:
        - `bool`:

### `online_only`

- **Описание**: `ps_product.online_only: tinyint(1) unsigned`
- **Тип**: `int`
- **Setter**: `online_only(self, value = 0) -> bool`
    - **Описание**: Товар только онлайн.
    - **Возвращает**:
       - `bool` : `True` если успешно, иначе `False`

### `ean13`

- **Описание**: `ps_product.ean13 varchar(13)`
- **Тип**: `str | None`
- **Setter**: `ean13(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `ean13`.
    - **Возвращает**:
       - `bool` : `True` если успешно, иначе `False`

### `isbn`

- **Описание**: `isbn` varchar(32)
- **Тип**: `str | None`
- **Setter**: `isbn(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `isbn`.
    - **Возвращает**:
       - `bool` : `True` если успешно, иначе `False`

### `upc`

- **Описание**: `upc` varchar(12)
- **Тип**: `str | None`
- **Setter**: `upc(self, value:str = None, lang:str = 'en') -> str | None`
    - **Описание**: `ps_product.upc`.
    - **Возвращает**:
       - `bool` : `True` если успешно, иначе `False`

### `mpn`

- **Описание**: `ps_product.mpn` varchar(40)
- **Тип**: `str`
- **Setter**: `mpn(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `mpn`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `ecotax`

- **Описание**: `ps_product.ecotax` decimal(17,6)
- **Тип**: `str`
- **Setter**: `ecotax(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `ecotax`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `minimal_quantity`

- **Описание**: `ps_product.minimal_quantity` int(10)
- **Тип**: `int`
- **Setter**: `minimal_quantity(self, value: int = 0) -> bool`
    - **Описание**: `minimal_quantity`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `low_stock_threshold`

- **Описание**: `ps_product.low_stock_threshold` int(10)
- **Тип**: `int`
- **Setter**: `low_stock_threshold(self, value: str = '') -> bool`
    - **Описание**: `low_stock_threshold`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `low_stock_alert`

- **Описание**: `ps_product.low_stock_alert` tinyint(1)
- **Тип**: `int`
- **Setter**: `low_stock_alert(self, value: int = 0) -> bool`
    - **Описание**: `low_stock_alert`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `price`

- **Описание**: `ps_product.price` decimal(20,6)
- **Тип**: `float`
- **Setter**: `price(self, value: str | int | float) -> bool`
    - **Описание**: `price`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `wholesale_price`

- **Описание**: `ps_product.wholesale_price` decimal(20,6)
- **Тип**: `float`
- **Setter**: `wholesale_price(self, value:str = None, lang:str = 'en') -> float`
     - **Описание**: `wholesale_price`.
      - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `unity`

- **Описание**: `ps_product.unity` varchar(255)
- **Тип**: `str`
- **Setter**: `unity(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `unity`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `unit_price_ratio`

- **Описание**: `ps_product.unit_price_ratio` decimal(20,6)
- **Тип**: `float`
- **Setter**: `unit_price_ratio(self, value: float = 0) -> bool`
    - **Описание**: `unit_price_ratio`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `additional_shipping_cost`

- **Описание**: `ps_product.additional_shipping_cost` decimal(20,6)
- **Тип**: `float`
- **Setter**: `additional_shipping_cost(self, value: int = 1) -> bool`
    - **Описание**: `additional_shipping_cost`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `reference`

- **Описание**: `ps_product.reference` varchar(64)
- **Тип**: `str`
- **Setter**: `reference(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `reference`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `supplier_reference`

- **Описание**: `ps_product.supplier_reference` varchar(64)
- **Тип**: `str`
- **Setter**: `supplier_reference(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `supplier_reference`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `location`

- **Описание**: `ps_product.location` varchar(255)
- **Тип**: `str`
- **Setter**: `location(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `location`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `width`

- **Описание**: `ps_product.width` decimal(20,6)
- **Тип**: `float`
- **Setter**: `width(self, value: float = None) -> bool`
    - **Описание**: `width`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `height`

- **Описание**: `ps_product.height` decimal(20,6)
- **Тип**: `float`
- **Setter**: `height(self, value: float = None) -> bool`
    - **Описание**: `height`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `depth`

- **Описание**: `ps_product.depth` decimal(20,6)
- **Тип**: `float`
- **Setter**: `depth(self, value: float = None) -> bool`
    - **Описание**: `depth`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `weight`

- **Описание**: `ps_product.weight` decimal(20,6)
- **Тип**: `float`
- **Setter**: `weight(self, value: float = None) -> bool`
    - **Описание**: `weight`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `volume`

- **Описание**: `ps_product.state` int(11)
- **Тип**: `int`
- **Setter**: `volume(self, value: int = 0) -> bool`
    - **Описание**: `volume`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `out_of_stock`

- **Описание**: `ps_product.out_of_stock` int(10)
- **Тип**: `int`
- **Setter**: `out_of_stock(self, value: int = None) -> bool`
    - **Описание**: `out_of_stock`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `additional_delivery_times`

- **Описание**: `ps_product.additional_delivery_times tinyint(1)`
- **Тип**: `int`
- **Setter**: `additional_delivery_times(self, value: int = 0) -> bool`
    - **Описание**: `additional_delivery_times`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `quantity_discount`

- **Описание**: `ps_product.quantity_discount` tinyint(1)
- **Тип**: `int`
- **Setter**: `quantity_discount(self, value: int = 0) -> bool`
    - **Описание**: `quantity_discount`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `customizable`

- **Описание**: `ps_product.customizable` tinyint(2)
- **Тип**: `int`
- **Setter**: `customizable(self, value: int = 0) -> bool`
    - **Описание**: `customizable`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `uploadable_files`

- **Описание**: `ps_product.uploadable_files` tinyint(4)
- **Тип**: `int`
- **Setter**: `uploadable_files(self, value: int = 0) -> bool`
    - **Описание**: `uploadable_files`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `text_fields`

- **Описание**: `ps_product.text_fields` tinyint(4)
- **Тип**: `int`
- **Setter**: `text_fields(self, value: int = 0) -> bool`
    - **Описание**: `text_fields`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `active`

- **Описание**: `ps_product.active` tinyint(1)
- **Тип**: `int`
- **Setter**: `active(self, value: int = 1) -> bool`
    - **Описание**: `active`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `redirect_type`

- **Описание**: `ps_product.redirect_type enum('404','301-product','302-product','301-category','302-category')`
- **Тип**: `str`
- **Setter**: `redirect_type(self, value: EnumRedirect | str) -> bool`
    - **Описание**: Редирект.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `id_type_redirected`

- **Описание**: `ps_product.id_type_redirected tinyint(10)`
- **Тип**: `int`
- **Setter**: `id_type_redirected(self, value: int = 0) -> bool`
    - **Описание**: `id_type_redirected`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `available_for_order`

- **Описание**: `ps_product.available_for_order` tinyint(10)
- **Тип**: `int`
- **Setter**: `available_for_order(self, value: int = 0) -> bool`
    - **Описание**: `available_for_order`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `available_date`

- **Описание**: `ps_product.available_date` date
- **Тип**: `Date`
- **Setter**: `available_date(self, value: Date = Date.today) -> bool`
    - **Описание**: `available_date`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `show_condition`

- **Описание**: `ps_product.show_condition` tinyint(1)
- **Тип**: `int`
- **Setter**: `show_condition(self, value: int = 1) -> bool`
    - **Описание**: `show_condition`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `condition`

- **Описание**: `ps_product.condition enum('new','used','refurbished')`
- **Тип**: `str`
- **Setter**: `condition(self, value: EnumCondition | str = EnumCondition.NEW) -> bool`
    - **Описание**: `condition`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `show_price`

- **Описание**: `ps_product.show_price tinyint(1)`
- **Тип**: `int`
- **Setter**: `show_price(self, value: int = 1) -> bool`
    - **Описание**: `show_price`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `indexed`

- **Описание**: `ps_product.indexed tinyint(1)`
- **Тип**: `int`
- **Setter**: `indexed(self, value: int = 1) -> bool`
    - **Описание**: `indexed`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `visibility`

- **Описание**: `ps_product.visibility` enum('both','catalog','search','none')
- **Тип**: `str`
- **Setter**: `visibility(self, value: EnumVisibity = EnumVisibity.BOTH) -> bool`
    - **Описание**: `visibility`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `cache_is_pack`

- **Описание**: `ps_product.cache_is_pack` tinyint(1)
- **Тип**: `int`
- **Setter**: `cache_is_pack(self, value: int = 1) -> bool`
    - **Описание**: `cache_is_pack`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `cache_has_attachments`

- **Описание**: `ps_product.cache_has_attachments` tinyint(1)
- **Тип**: `int`
- **Setter**: `cache_has_attachments(self, value: int = 1) -> bool`
    - **Описание**: `cache_has_attachments`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `is_virtual`

- **Описание**: `ps_product.is_virtual` tinyint(1)
- **Тип**: `int`
- **Setter**: `is_virtual(self, value: int = 1) -> bool`
    - **Описание**: `is_virtual`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `cache_default_attribute`

- **Описание**: `ps_product.cache_default_attribute` int(10)
- **Тип**: `int`
- **Setter**: `cache_default_attribute(self, value: int = 1) -> bool`
    - **Описание**: `cache_default_attribute`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `date_add`

- **Описание**: `ps_product.date_add` datetime
- **Тип**: `Date`
- **Setter**: `date_add(self, value: Date = Date.today()) -> bool`
    - **Описание**: `date_add`.
    - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `date_upd`

- **Описание**: `ps_product.date_upd` datetime
- **Тип**: `Date`
- **Setter**: `date_upd(self, value: Date = Date.today()) -> bool`
    - **Описание**: `date_upd`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `advanced_stock_management`

- **Описание**: `ps_product.advanced_stock_management` tinyint(1)
- **Тип**: `int`
- **Setter**: `advanced_stock_management(self, value: int = 0) -> bool`
    - **Описание**: `advanced_stock_management`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `pack_stock_type`

- **Описание**: `ps_product.pack_stock_type` int(11)
- **Тип**: `int`
- **Setter**: `pack_stock_type(self, value: int = 0) -> bool`
    - **Описание**: `pack_stock_type`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `state`

- **Описание**: `ps_product.state` int(11)
- **Тип**: `int`
- **Setter**: `state(self, value: int = 0) -> bool`
    - **Описание**: `state`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `product_type`

- **Описание**: `ps_product.product_type` enum('standard', 'pack', 'virtual', 'combinations', '')
- **Тип**: `str`
- **Setter**: `product_type(self, product_type: EnumProductType = EnumProductType.STANDARD) -> bool`
    - **Описание**: `product_type`.
     - **Возвращает**:
        - `bool`: `True` если успешно, иначе `False`

### `description`

- **Описание**: `ps_product_lang.description text`
- **Тип**: `str`
- **Setter**: `description(self, value: str | list = '', lang:str = 'en') -> bool`
    - **Описание**: Описание.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `description_short`

- **Описание**: `ps_product_lang.description_short text`
- **Тип**: `str`
- **Setter**: `description_short(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `description_short`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `link_rewrite`

- **Описание**: `ps_product_lang.link_rewrite` varchar(128)
- **Тип**: `str`
- **Setter**: `link_rewrite(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `link_rewrite`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `meta_description`

- **Описание**: `ps_product_lang.meta_description varchar(512)`
- **Тип**: `str`
- **Setter**: `meta_description(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `meta_description`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `meta_keywords`

- **Описание**: `ps_product_lang.meta_keywords varchar(255)`
- **Тип**: `str`
- **Setter**: `meta_keywords(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `meta_keywords`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `meta_title`

- **Описание**: `s_product_lang.meta_title varchar(128)`
- **Тип**: `str`
- **Setter**: `meta_title(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `meta_title`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `name`

- **Описание**: `ps_product_lang.name varchar(128)`
- **Тип**: `str`
- **Setter**: `name(self, value: str, lang:str = 'en') -> bool`
    - **Описание**: `name`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `available_now`

- **Описание**: `ps_product_lang.available_now varchar(255)`
- **Тип**: `str`
- **Setter**: `available_now(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `available_now`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `available_later`

- **Описание**: `ps_product_lang.available_later varchar(255)`
- **Тип**: `str`
- **Setter**: `available_later(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `available_later`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `delivery_in_stock`

- **Описание**: `ps_product_lang.delivery_in_stock varchar(255)`
- **Тип**: `str`
- **Setter**: `delivery_in_stock(self, value:str = None, lang:str = 'en') -> bool`
    - **Описание**: `delivery_in_stock`.
    - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `delivery_out_stock`

- **Описание**: `ps_product_lang.delivery_out_stock varchar(256)`
- **Тип**: `str`
- **Setter**: `delivery_out_stock(self, value:str = None, lang:str = 'en') -> bool`
     - **Описание**: `delivery_out_stock`.
     - **Возвращает**:
         - `bool`: `True` если успешно, иначе `False`

### `delivery_additional_message`

- **Описание**: `ps_product_lang.delivery_out_stock`
- **Тип**: `str`
- **Setter**: `delivery_additional