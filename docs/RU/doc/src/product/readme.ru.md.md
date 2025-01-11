# Модуль `src.product.product.py`

## Обзор

Модуль `src.product.product` определяет поведение продукта в проекте, обеспечивая взаимодействие между веб-сайтом, продуктом и API PrestaShop. Он использует классы из модулей `src.endpoints.prestashop`, `src.category`, и `src.product.product_fields`.

## Оглавление

1.  [Классы](#классы)
    -   [`Product`](#product)
    -   [`ProductFields`](#productfields)
    -   [`PrestaShop`](#prestashop)
2.  [Статические методы](#статические-методы)
    -   [`get_parent_categories`](#get_parent_categories)

## Классы

### `Product`

**Описание**: Класс `Product` наследуется от `ProductFields` и `PrestaShop`, предоставляя методы для работы с продуктами. Изначально собирает данные со страницы продукта и затем работает с API PrestaShop.

**Методы**:

-   `__init__`

    **Описание**: Инициализирует объект `Product`.

    **Параметры**:
    -   `*args`: Переменная длина аргументов.
    -   `**kwargs`: Произвольные именованные аргументы.

-   `get_parent_categories`

    **Описание**: Возвращает список родительских категорий для указанной категории.

    **Параметры**:
    -   `id_category` (int): ID категории.
    -   `dept` (int, optional): Глубина категории. По умолчанию 0.

    **Возвращает**:
        -   list: Список родительских категорий.

    **Возможные исключения**:
    -   `TypeError`: Если `id_category` не является целым числом.

### `ProductFields`

**Описание**: Базовый класс для работы с полями продукта. (Описание класса `ProductFields` отсутствует в предоставленном коде, но будет нужно для полной документации)

### `PrestaShop`

**Описание**: Класс для работы с API PrestaShop. (Описание класса `PrestaShop` отсутствует в предоставленном коде, но будет нужно для полной документации)

## Статические методы

### `get_parent_categories`

**Описание**: Получает список родительских категорий для заданной категории по её ID. Дублирует функцию `get_parents` из класса `Category`.

**Параметры**:
-   `id_category` (int): ID категории.
-   `dept` (int, optional): Глубина категории. По умолчанию 0.

**Возвращает**:
-   `list`: Список родительских категорий.

**Возможные исключения**:
 - `TypeError`: Если `id_category` не является целым числом.

# Модуль `src.product.product_fields.product_fields.py`

## Обзор

Модуль `hypotez/src/product/product_fields/product_fields.py` содержит класс `ProductFields`, предназначенный для работы с полями товаров в системе управления контентом PrestaShop. Класс предоставляет свойства и методы для доступа и изменения различных полей товара, а также для загрузки данных из файлов. Документация описывает структуру таблиц PrestaShop, содержащих информацию о товарах, и методы работы с полями этих таблиц.

## Оглавление

1.  [Классы](#классы)
    -   [`ProductFields`](#productfields)
2.  [Свойства](#свойства)
    -   [`id_product`](#id_product)
    -   [`id_supplier`](#id_supplier)
    -   [`id_manufacturer`](#id_manufacturer)
    -   [`id_category_default`](#id_category_default)
    -   [`id_shop_default`](#id_shop_default)
    -   [`id_tax`](#id_tax)
    -   [`on_sale`](#on_sale)
    -   [`online_only`](#online_only)
    -   [`ean13`](#ean13)
    -   [`isbn`](#isbn)
    -   [`upc`](#upc)
    -   [`mpn`](#mpn)
    -   [`ecotax`](#ecotax)
    -   [`quantity`](#quantity)
    -   [`minimal_quantity`](#minimal_quantity)
    -   [`low_stock_threshold`](#low_stock_threshold)
    -   [`low_stock_alert`](#low_stock_alert)
    -   [`price`](#price)
    -   [`wholesale_price`](#wholesale_price)
    -   [`unity`](#unity)
    -   [`unit_price_ratio`](#unit_price_ratio)
    -   [`additional_shipping_cost`](#additional_shipping_cost)
    -   [`reference`](#reference)
    -   [`supplier_reference`](#supplier_reference)
    -   [`location`](#location)
    -   [`width`](#width)
    -   [`height`](#height)
    -   [`depth`](#depth)
    -   [`weight`](#weight)
    -   [`volume`](#volume)
    -   [`out_of_stock`](#out_of_stock)
    -   [`additional_delivery_times`](#additional_delivery_times)
    -   [`quantity_discount`](#quantity_discount)
    -   [`customizable`](#customizable)
    -   [`uploadable_files`](#uploadable_files)
    -   [`text_fields`](#text_fields)
    -   [`active`](#active)
    -   [`redirect_type`](#redirect_type)
    -   [`id_type_redirected`](#id_type_redirected)
    -   [`available_for_order`](#available_for_order)
    -   [`available_date`](#available_date)
    -   [`show_condition`](#show_condition)
    -   [`condition`](#condition)
    -   [`show_price`](#show_price)
    -   [`indexed`](#indexed)
    -   [`visibility`](#visibility)
    -   [`cache_is_pack`](#cache_is_pack)
    -   [`cache_has_attachments`](#cache_has_attachments)
    -   [`is_virtual`](#is_virtual)
    -   [`cache_default_attribute`](#cache_default_attribute)
    -   [`date_add`](#date_add)
    -   [`date_upd`](#date_upd)
    -   [`advanced_stock_management`](#advanced_stock_management)
    -   [`pack_stock_type`](#pack_stock_type)
    -   [`state`](#state)
    -   [`product_type`](#product_type)
    -  [`link_to_video`](#link_to_video)
    -   [`images_urls`](#images_urls)

## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` предоставляет методы и свойства для работы с полями товаров в базе данных PrestaShop. Он загружает данные полей из файлов и предоставляет методы доступа и изменения этих полей.

**Атрибуты**:
-   `product_fields_list`: Список названий полей товара, загруженный из файла `fields_list.txt`.
-   `language`: Словарь, содержащий соответствие между кодами языков и их идентификаторами в PrestaShop.
-   `presta_fields`: Объект `SimpleNamespace`, содержащий поля товара.
-   `assist_fields_dict`: Словарь дополнительных служебных полей (например, URL изображений).

**Методы**:

-   `__init__(self)`

    **Описание**: Инициализирует объект `ProductFields`. Загружает список полей, языки и дефолтные значения.

-   `_load_product_fields_list(self) -> List[str]`

    **Описание**: Загружает список полей из файла `fields_list.txt`.

    **Возвращает**:
        - `List[str]`: Список полей товара.

-   `_payload(self) -> bool`

    **Описание**: Загружает дефолтные значения полей из файла `product_fields_default_values.json`. Возвращает `True`, если загрузка успешна, иначе `False`.

     **Возвращает**:
        - `bool`: `True` если загрузка прошла успешно, иначе `False`.

## Свойства

### `id_product`

**Описание**: `ID` товара. Для нового товара ID назначается из PrestaShop.

**Доступ**: `product_fields.id_product`

**Установление**: `product_fields.id_product = value`

**Параметры**:
- `value` (int, optional): Требуется при операциях над существующим товаром. `ps_product.id`. Для нового товара ID вернется из системы при занесении товара в базу данных.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `id_supplier`

**Описание**: `ID` поставщика.

**Доступ**: `product_fields.id_supplier`

**Установление**: `product_fields.id_supplier = value`

**Параметры**:
- `value` (int, optional): ID поставщика.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `id_manufacturer`

**Описание**: `ID` производителя.

**Доступ**: `product_fields.id_manufacturer`

**Установление**: `product_fields.id_manufacturer = value`

**Параметры**:
- `value` (int, optional): ID производителя.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `id_category_default`

**Описание**: `ID` категории по умолчанию.

**Доступ**: `product_fields.id_category_default`

**Установление**: `product_fields.id_category_default = value`

**Параметры**:
- `value` (int, optional): ID категории по умолчанию.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `id_shop_default`

**Описание**: `ID` магазина по умолчанию.

**Доступ**: `product_fields.id_shop_default`

**Установление**: `product_fields.id_shop_default = value`

**Параметры**:
- `value` (int, optional): ID магазина по умолчанию.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `id_tax`

**Описание**: `ID` налога.

**Доступ**: `product_fields.id_tax`

**Установление**: `product_fields.id_tax = value`

**Параметры**:
- `value` (int, optional): ID налога.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `on_sale`

**Описание**:  Флаг "в продаже".

**Доступ**: `product_fields.on_sale`

**Установление**: `product_fields.on_sale = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - в продаже, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `online_only`

**Описание**:  Флаг "продавать только онлайн".

**Доступ**: `product_fields.online_only`

**Установление**: `product_fields.online_only = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - продавать только онлайн, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `ean13`

**Описание**: EAN-13 код.

**Доступ**: `product_fields.ean13`

**Установление**: `product_fields.ean13 = value`

**Параметры**:
- `value` (str, optional): EAN-13 код.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `isbn`

**Описание**: ISBN код.

**Доступ**: `product_fields.isbn`

**Установление**: `product_fields.isbn = value`

**Параметры**:
- `value` (str, optional): ISBN код.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `upc`

**Описание**: UPC код.

**Доступ**: `product_fields.upc`

**Установление**: `product_fields.upc = value`

**Параметры**:
- `value` (str, optional): UPC код.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `mpn`

**Описание**: MPN код.

**Доступ**: `product_fields.mpn`

**Установление**: `product_fields.mpn = value`

**Параметры**:
- `value` (str, optional): MPN код.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `ecotax`

**Описание**: Экологический налог.

**Доступ**: `product_fields.ecotax`

**Установление**: `product_fields.ecotax = value`

**Параметры**:
- `value` (float, optional): Размер экологического налога.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `quantity`

**Описание**: Количество товара в наличии.

**Доступ**: `product_fields.quantity`

**Установление**: `product_fields.quantity = value`

**Параметры**:
- `value` (int, optional): Количество товара в наличии.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `minimal_quantity`

**Описание**: Минимальное количество для заказа.

**Доступ**: `product_fields.minimal_quantity`

**Установление**: `product_fields.minimal_quantity = value`

**Параметры**:
- `value` (int, optional): Минимальное количество для заказа.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `low_stock_threshold`

**Описание**: Порог низкого запаса.

**Доступ**: `product_fields.low_stock_threshold`

**Установление**: `product_fields.low_stock_threshold = value`

**Параметры**:
- `value` (int, optional): Порог низкого запаса.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `low_stock_alert`

**Описание**:  Флаг оповещения о низком запасе.

**Доступ**: `product_fields.low_stock_alert`

**Установление**: `product_fields.low_stock_alert = value`

**Параметры**:
- `value` (int, optional):  Флаг. `1` - оповещать, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `price`

**Описание**:  Цена товара.

**Доступ**: `product_fields.price`

**Установление**: `product_fields.price = value`

**Параметры**:
- `value` (float, optional): Цена товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `wholesale_price`

**Описание**: Оптовая цена товара.

**Доступ**: `product_fields.wholesale_price`

**Установление**: `product_fields.wholesale_price = value`

**Параметры**:
- `value` (float, optional): Оптовая цена товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `unity`

**Описание**: Единица измерения.

**Доступ**: `product_fields.unity`

**Установление**: `product_fields.unity = value`

**Параметры**:
- `value` (str, optional): Единица измерения.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `unit_price_ratio`

**Описание**: Коэффициент цены за единицу.

**Доступ**: `product_fields.unit_price_ratio`

**Установление**: `product_fields.unit_price_ratio = value`

**Параметры**:
- `value` (float, optional): Коэффициент цены за единицу.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `additional_shipping_cost`

**Описание**: Дополнительные расходы на доставку.

**Доступ**: `product_fields.additional_shipping_cost`

**Установление**: `product_fields.additional_shipping_cost = value`

**Параметры**:
- `value` (float, optional): Дополнительные расходы на доставку.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `reference`

**Описание**: Артикул товара.

**Доступ**: `product_fields.reference`

**Установление**: `product_fields.reference = value`

**Параметры**:
- `value` (str, optional): Артикул товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `supplier_reference`

**Описание**: Артикул поставщика.

**Доступ**: `product_fields.supplier_reference`

**Установление**: `product_fields.supplier_reference = value`

**Параметры**:
- `value` (str, optional): Артикул поставщика.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `location`

**Описание**: Местоположение товара на складе.

**Доступ**: `product_fields.location`

**Установление**: `product_fields.location = value`

**Параметры**:
- `value` (str, optional): Местоположение товара на складе.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `width`

**Описание**: Ширина товара.

**Доступ**: `product_fields.width`

**Установление**: `product_fields.width = value`

**Параметры**:
- `value` (float, optional): Ширина товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `height`

**Описание**: Высота товара.

**Доступ**: `product_fields.height`

**Установление**: `product_fields.height = value`

**Параметры**:
- `value` (float, optional): Высота товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `depth`

**Описание**: Глубина товара.

**Доступ**: `product_fields.depth`

**Установление**: `product_fields.depth = value`

**Параметры**:
- `value` (float, optional): Глубина товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `weight`

**Описание**: Вес товара.

**Доступ**: `product_fields.weight`

**Установление**: `product_fields.weight = value`

**Параметры**:
- `value` (float, optional): Вес товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `volume`

**Описание**: Объем товара.

**Доступ**: `product_fields.volume`

**Установление**: `product_fields.volume = value`

**Параметры**:
- `value` (float, optional): Объем товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `out_of_stock`

**Описание**: Статус отсутствия на складе.

**Доступ**: `product_fields.out_of_stock`

**Установление**: `product_fields.out_of_stock = value`

**Параметры**:
- `value` (int, optional): Статус отсутствия на складе.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `additional_delivery_times`

**Описание**:  Дополнительное время доставки.

**Доступ**: `product_fields.additional_delivery_times`

**Установление**: `product_fields.additional_delivery_times = value`

**Параметры**:
- `value` (int, optional): Дополнительное время доставки.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `quantity_discount`

**Описание**:  Флаг "скидки по количеству".

**Доступ**: `product_fields.quantity_discount`

**Установление**: `product_fields.quantity_discount = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - скидка по количеству, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `customizable`

**Описание**:  Флаг "настраиваемый".

**Доступ**: `product_fields.customizable`

**Установление**: `product_fields.customizable = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - настраиваемый, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `uploadable_files`

**Описание**:  Количество загружаемых файлов.

**Доступ**: `product_fields.uploadable_files`

**Установление**: `product_fields.uploadable_files = value`

**Параметры**:
- `value` (int, optional): Количество загружаемых файлов.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `text_fields`

**Описание**:  Количество текстовых полей.

**Доступ**: `product_fields.text_fields`

**Установление**: `product_fields.text_fields = value`

**Параметры**:
- `value` (int, optional): Количество текстовых полей.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `active`

**Описание**: Флаг активности товара.

**Доступ**: `product_fields.active`

**Установление**: `product_fields.active = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - активен, `0` - не активен.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `redirect_type`

**Описание**: Тип редиректа.

**Доступ**: `product_fields.redirect_type`

**Установление**: `product_fields.redirect_type = value`

**Параметры**:
- `value` (str, optional): Тип редиректа.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `id_type_redirected`

**Описание**: `ID` редиректа.

**Доступ**: `product_fields.id_type_redirected`

**Установление**: `product_fields.id_type_redirected = value`

**Параметры**:
- `value` (int, optional): `ID` редиректа.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `available_for_order`

**Описание**:  Флаг "доступен для заказа".

**Доступ**: `product_fields.available_for_order`

**Установление**: `product_fields.available_for_order = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - доступен, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `available_date`

**Описание**: Дата доступности.

**Доступ**: `product_fields.available_date`

**Установление**: `product_fields.available_date = value`

**Параметры**:
- `value` (str, optional): Дата доступности.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `show_condition`

**Описание**:  Флаг "показывать условие".

**Доступ**: `product_fields.show_condition`

**Установление**: `product_fields.show_condition = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - показывать, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `condition`

**Описание**:  Условие товара.

**Доступ**: `product_fields.condition`

**Установление**: `product_fields.condition = value`

**Параметры**:
- `value` (str, optional): Условие товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `show_price`

**Описание**:  Флаг "показывать цену".

**Доступ**: `product_fields.show_price`

**Установление**: `product_fields.show_price = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - показывать, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `indexed`

**Описание**: Флаг индексирования.

**Доступ**: `product_fields.indexed`

**Установление**: `product_fields.indexed = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - индексировать, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `visibility`

**Описание**: Видимость товара.

**Доступ**: `product_fields.visibility`

**Установление**: `product_fields.visibility = value`

**Параметры**:
- `value` (str, optional): Видимость товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `cache_is_pack`

**Описание**:  Флаг "кешировать как набор".

**Доступ**: `product_fields.cache_is_pack`

**Установление**: `product_fields.cache_is_pack = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - кешировать, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `cache_has_attachments`

**Описание**:  Флаг "кешировать вложения".

**Доступ**: `product_fields.cache_has_attachments`

**Установление**: `product_fields.cache_has_attachments = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - кешировать, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `is_virtual`

**Описание**:  Флаг "виртуальный товар".

**Доступ**: `product_fields.is_virtual`

**Установление**: `product_fields.is_virtual = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - виртуальный, `0` - нет.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `cache_default_attribute`

**Описание**: Кеш атрибута по умолчанию.

**Доступ**: `product_fields.cache_default_attribute`

**Установление**: `product_fields.cache_default_attribute = value`

**Параметры**:
- `value` (int, optional): Кеш атрибута по умолчанию.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `date_add`

**Описание**: Дата добавления.

**Доступ**: `product_fields.date_add`

**Установление**: `product_fields.date_add = value`

**Параметры**:
- `value` (str, optional): Дата добавления.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `date_upd`

**Описание**: Дата обновления.

**Доступ**: `product_fields.date_upd`

**Установление**: `product_fields.date_upd = value`

**Параметры**:
- `value` (str, optional): Дата обновления.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `advanced_stock_management`

**Описание**:  Флаг "расширенное управление запасами".

**Доступ**: `product_fields.advanced_stock_management`

**Установление**: `product_fields.advanced_stock_management = value`

**Параметры**:
- `value` (int, optional): Флаг. `1` - включено, `0` - выключено.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `pack_stock_type`

**Описание**:  Тип управления запасами в наборе.

**Доступ**: `product_fields.pack_stock_type`

**Установление**: `product_fields.pack_stock_type = value`

**Параметры**:
- `value` (int, optional): Тип управления запасами в наборе.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `state`

**Описание**:  Состояние товара.

**Доступ**: `product_fields.state`

**Установление**: `product_fields.state = value`

**Параметры**:
- `value` (int, optional): Состояние товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `product_type`

**Описание**:  Тип товара.

**Доступ**: `product_fields.product_type`

**Установление**: `product_fields.product_type = value`

**Параметры**:
- `value` (str, optional): Тип товара.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `link_to_video`

**Описание**:  Ссылка на видео.

**Доступ**: `product_fields.link_to_video`

**Установление**: `product_fields.link_to_video = value`

**Параметры**:
- `value` (str, optional): Ссылка на видео.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.

### `images_urls`

**Описание**:  Список URL изображений.

**Доступ**: `product_fields.images_urls`

**Установление**: `product_fields.images_urls = value`

**Параметры**:
- `value` (list, optional): Список URL изображений.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.