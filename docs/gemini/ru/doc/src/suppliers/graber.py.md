# Модуль `graber.py`

## Обзор

Модуль `graber.py` представляет собой базовый класс `Graber` для сбора данных о товарах со страниц HTML поставщиков. Этот класс использует веб-драйвер для извлечения целевых полей, таких как название, описание, спецификация, артикул, цена и т.д. Местоположение каждого поля определяется с помощью локаторов, которые хранятся в JSON-файлах в директории `locators` каждого поставщика.

## Оглавление

- [Классы](#классы)
    - [`Context`](#context)
    - [`Graber`](#graber)
- [Декораторы](#декораторы)
    - [`close_pop_up`](#close_pop_up)
- [Функции](#функции)
    - [`set_field_value`](#set_field_value)
    - [`grab_page`](#grab_page)
    - [`error`](#error)
- [Методы Graber](#методы-graber)
    - [`additional_shipping_cost`](#additional_shipping_cost)
    - [`delivery_in_stock`](#delivery_in_stock)
    - [`active`](#active)
    - [`additional_delivery_times`](#additional_delivery_times)
    - [`advanced_stock_management`](#advanced_stock_management)
    - [`affiliate_short_link`](#affiliate_short_link)
    - [`affiliate_summary`](#affiliate_summary)
    - [`affiliate_summary_2`](#affiliate_summary_2)
    - [`affiliate_text`](#affiliate_text)
    - [`affiliate_image_large`](#affiliate_image_large)
    - [`affiliate_image_medium`](#affiliate_image_medium)
    - [`affiliate_image_small`](#affiliate_image_small)
    - [`available_date`](#available_date)
    - [`available_for_order`](#available_for_order)
    - [`available_later`](#available_later)
    - [`available_now`](#available_now)
    - [`additional_categories`](#additional_categories)
    - [`cache_default_attribute`](#cache_default_attribute)
    - [`cache_has_attachments`](#cache_has_attachments)
    - [`cache_is_pack`](#cache_is_pack)
    - [`condition`](#condition)
    - [`customizable`](#customizable)
    - [`date_add`](#date_add)
    - [`date_upd`](#date_upd)
    - [`delivery_out_stock`](#delivery_out_stock)
    - [`depth`](#depth)
    - [`description`](#description)
    - [`description_short`](#description_short)
    - [`id_category_default`](#id_category_default)
    - [`id_default_combination`](#id_default_combination)
    - [`id_product`](#id_product)
    - [`locale`](#locale)
    - [`id_default_image`](#id_default_image)
    - [`ean13`](#ean13)
    - [`ecotax`](#ecotax)
    - [`height`](#height)
    - [`how_to_use`](#how_to_use)
    - [`id_manufacturer`](#id_manufacturer)
    - [`id_supplier`](#id_supplier)
    - [`id_tax`](#id_tax)
    - [`id_type_redirected`](#id_type_redirected)
    - [`images_urls`](#images_urls)
    - [`indexed`](#indexed)
    - [`ingredients`](#ingredients)
    - [`meta_description`](#meta_description)
    - [`meta_keywords`](#meta_keywords)
    - [`meta_title`](#meta_title)
    - [`is_virtual`](#is_virtual)
    - [`isbn`](#isbn)
    - [`link_rewrite`](#link_rewrite)
    - [`location`](#location)
    - [`low_stock_alert`](#low_stock_alert)
    - [`low_stock_threshold`](#low_stock_threshold)
    - [`minimal_quantity`](#minimal_quantity)
    - [`mpn`](#mpn)
    - [`name`](#name)
    - [`online_only`](#online_only)
    - [`on_sale`](#on_sale)
    - [`out_of_stock`](#out_of_stock)
    - [`pack_stock_type`](#pack_stock_type)
    - [`price`](#price)
    - [`product_type`](#product_type)
    - [`quantity`](#quantity)
    - [`quantity_discount`](#quantity_discount)
    - [`redirect_type`](#redirect_type)
    - [`reference`](#reference)
    - [`show_condition`](#show_condition)
    - [`show_price`](#show_price)
    - [`state`](#state)
    - [`text_fields`](#text_fields)
    - [`unit_price_ratio`](#unit_price_ratio)
    - [`unity`](#unity)
    - [`upc`](#upc)
    - [`uploadable_files`](#uploadable_files)
    - [`default_image_url`](#default_image_url)
    - [`visibility`](#visibility)
    - [`weight`](#weight)
    - [`wholesale_price`](#wholesale_price)
    - [`width`](#width)
    - [`specification`](#specification)
     - [`link`](#link)
    -   [`byer_protection`](#byer_protection)
    -   [`customer_reviews`](#customer_reviews)
     - [`link_to_video`](#link_to_video)
    - [`local_image_path`](#local_image_path)
    - [`local_video_path`](#local_video_path)
    
## Классы

### `Context`

**Описание**: Класс для хранения глобальных настроек.

**Атрибуты**:
- `driver` (`'Driver'`): Объект драйвера, используется для управления браузером или другим интерфейсом.
- `locator` (`SimpleNamespace`): Пространство имен для хранения локаторов.
- `supplier_prefix` (`str`): Префикс поставщика.
- `locator_for_decorator` (`SimpleNamespace`): Локатор для использования в декораторе `@close_pop_up`.

### `Graber`

**Описание**: Базовый класс сбора данных со страницы для всех поставщиков.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.
- `set_field_value`: Универсальная функция для установки значений полей с обработкой ошибок.
- `grab_page`: Асинхронная функция для сбора полей продукта.
- `error`: Обработчик ошибок для полей.

## Декораторы

### `close_pop_up`

**Описание**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
- `value` (`'Driver'`, optional): Дополнительное значение для декоратора.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

## Функции

### `set_field_value`
**Описание**: Универсальная функция для установки значений полей с обработкой ошибок.
    
**Параметры**:
- `value` (`Any`): Значение для установки.
- `locator_func` (`Callable[[], Any]`): Функция для получения значения из локатора.
- `field_name` (`str`): Название поля.
- `default` (`Any`, optional): Значение по умолчанию. По умолчанию пустая строка.
    
**Возвращает**:
- `Any`: Установленное значение.

### `grab_page`
**Описание**: Асинхронная функция для сбора полей продукта.
    
**Параметры**:
- `args` (`tuple`): Кортеж с названиями полей для сбора.
- `kwards` (`dict`): Словарь с ключами и значениями для каждого поля.
    
**Возвращает**:
- `ProductFields`: Собранные поля продукта.

### `error`
**Описание**: Обработчик ошибок для полей.
    
**Параметры**:
- `field` (`str`): Название поля.

## Методы Graber

### `additional_shipping_cost`
**Описание**: Извлекает и устанавливает дополнительную стоимость доставки.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `delivery_in_stock`
**Описание**: Извлекает и устанавливает статус наличия на складе.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `active`
**Описание**: Извлекает и устанавливает статус активности.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs. Принимаемое значение: 1/0

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `additional_delivery_times`
**Описание**: Извлекает и устанавливает дополнительное время доставки.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `advanced_stock_management`
**Описание**: Извлекает и устанавливает статус расширенного управления запасами.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_short_link`
**Описание**: Извлекает и устанавливает короткую партнерскую ссылку.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_summary`
**Описание**: Извлекает и устанавливает партнерскую сводку.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_summary_2`
**Описание**: Извлекает и устанавливает партнерскую сводку 2.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_text`
**Описание**: Извлекает и устанавливает партнерский текст.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_image_large`
**Описание**: Извлекает и устанавливает большое партнерское изображение.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_image_medium`
**Описание**: Извлекает и устанавливает среднее партнерское изображение.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `affiliate_image_small`
**Описание**: Извлекает и устанавливает маленькое партнерское изображение.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `available_date`
**Описание**: Извлекает и устанавливает дату доступности.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `available_for_order`
**Описание**: Извлекает и устанавливает статус доступности для заказа.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `available_later`
**Описание**: Извлекает и устанавливает статус доступности позже.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `available_now`
**Описание**: Извлекает и устанавливает статус доступности сейчас.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `additional_categories`
**Описание**: Устанавливает дополнительные категории.
    
**Параметры**:
- `value` (`Optional[str | list]`, optional): Строка или список категорий.

**Возвращает**:
- `dict`: Словарь с ID категорий.

### `cache_default_attribute`
**Описание**: Извлекает и устанавливает кэшированный атрибут по умолчанию.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `cache_has_attachments`
**Описание**: Извлекает и устанавливает статус кэширования наличия вложений.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `cache_is_pack`
**Описание**: Извлекает и устанавливает статус кэширования, является ли товар упаковкой.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `condition`
**Описание**: Извлекает и устанавливает состояние товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `customizable`
**Описание**: Извлекает и устанавливает статус настраиваемости.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `date_add`
**Описание**: Извлекает и устанавливает дату добавления.
    
**Параметры**:
- `value` (`Optional[str | datetime.date]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `date_upd`
**Описание**: Извлекает и устанавливает дату обновления.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `delivery_out_stock`
**Описание**: Извлекает и устанавливает статус доставки при отсутствии на складе.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `depth`
**Описание**: Извлекает и устанавливает глубину товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `description`
**Описание**: Извлекает и устанавливает описание товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `description_short`
**Описание**: Извлекает и устанавливает краткое описание товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `id_category_default`
**Описание**: Устанавливает ID категории по умолчанию.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха.

### `id_default_combination`
**Описание**: Извлекает и устанавливает ID комбинации по умолчанию.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `id_product`
**Описание**: Извлекает и устанавливает ID товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `locale`
**Описание**: Извлекает и устанавливает локаль.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.locale`.

### `id_default_image`
**Описание**: Извлекает и устанавливает ID изображения по умолчанию.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `ean13`
**Описание**: Извлекает и устанавливает код EAN13.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `ecotax`
**Описание**: Извлекает и устанавливает эконалог.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `height`
**Описание**: Извлекает и устанавливает высоту товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `how_to_use`
**Описание**: Извлекает и устанавливает информацию о том, как использовать товар.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.how_to_use`.

### `id_manufacturer`
**Описание**: Извлекает и устанавливает ID производителя.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.id_manufacturer`.

### `id_supplier`
**Описание**: Извлекает и устанавливает ID поставщика.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `id_tax`
**Описание**: Извлекает и устанавливает ID налога.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.id_tax`.

### `id_type_redirected`
**Описание**: Извлекает и устанавливает ID типа перенаправления.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.id_type_redirected`.

### `images_urls`
**Описание**: Извлекает и устанавливает URL изображений.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.images_urls`.

### `indexed`
**Описание**: Извлекает и устанавливает статус индексации.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `ingredients`
**Описание**: Извлекает и устанавливает ингредиенты товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `meta_description`
**Описание**: Извлекает и устанавливает мета-описание товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `meta_keywords`
**Описание**: Извлекает и устанавливает мета-ключевые слова товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `meta_title`
**Описание**: Извлекает и устанавливает мета-заголовок товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `is_virtual`
**Описание**: Извлекает и устанавливает статус виртуального товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `isbn`
**Описание**: Извлекает и устанавливает ISBN товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `link_rewrite`
**Описание**: Извлекает и устанавливает переписанную ссылку товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `location`
**Описание**: Извлекает и устанавливает местоположение товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `low_stock_alert`
**Описание**: Извлекает и устанавливает статус оповещения о низком запасе.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `low_stock_threshold`
**Описание**: Извлекает и устанавливает порог низкого запаса.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `minimal_quantity`
**Описание**: Извлекает и устанавливает минимальное количество товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `mpn`
**Описание**: Извлекает и устанавливает MPN (номер детали производителя).
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `name`
**Описание**: Извлекает и устанавливает название товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `online_only`
**Описание**: Извлекает и устанавливает статус "только онлайн".
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `on_sale`
**Описание**: Извлекает и устанавливает статус "в продаже".
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `out_of_stock`
**Описание**: Извлекает и устанавливает статус "нет в наличии".
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `pack_stock_type`
**Описание**: Извлекает и устанавливает тип запаса упаковки.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `price`
**Описание**: Извлекает и устанавливает цену товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `product_type`
**Описание**: Извлекает и устанавливает тип товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `quantity`
**Описание**: Извлекает и устанавливает количество товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `quantity_discount`
**Описание**: Извлекает и устанавливает скидку по количеству товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `redirect_type`
**Описание**: Извлекает и устанавливает тип перенаправления.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `reference`
**Описание**: Извлекает и устанавливает артикул товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `show_condition`
**Описание**: Извлекает и устанавливает статус отображения состояния товара.
    
**Параметры**:
- `value` (`Optional[int]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `show_price`
**Описание**: Извлекает и устанавливает статус отображения цены товара.
    
**Параметры**:
- `value` (`Optional[int]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `state`
**Описание**: Извлекает и устанавливает состояние товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `text_fields`
**Описание**: Извлекает и устанавливает текстовые поля товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `unit_price_ratio`
**Описание**: Извлекает и устанавливает отношение цены за единицу товара.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `unity`
**Описание**: Извлекает и устанавливает единицу измерения товара.
    
**Параметры**:
- `value` (`Optional[str]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `upc`
**Описание**: Извлекает и устанавливает код UPC товара.
    
**Параметры**:
- `value` (`Optional[str]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `uploadable_files`
**Описание**: Извлекает и устанавливает информацию о загружаемых файлах.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `default_image_url`
**Описание**: Извлекает и устанавливает URL изображения по умолчанию.
    
**Параметры**:
- `value` (`Optional[Any]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `visibility`
**Описание**: Извлекает и устанавливает видимость товара.
   
**Параметры**:
- `value` (`Optional[str]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `None`: устанавливает значение в `ProductFields.visibility`.

### `weight`
**Описание**: Извлекает и устанавливает вес товара.
    
**Параметры**:
- `value` (`Optional[float]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `wholesale_price`
**Описание**: Извлекает и устанавливает оптовую цену товара.
    
**Параметры**:
- `value` (`Optional[float]`, optional): Значение, которое можно передать в kwargs.

**Возвращает**:
- `bool`: `True` в случае успеха, `None` в случае ошибки.

### `width`
**Описание**: Извлекает и устанавли