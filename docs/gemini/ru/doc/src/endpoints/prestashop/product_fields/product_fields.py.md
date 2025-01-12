# Модуль `product_fields`

## Обзор

Модуль `product_fields.py` содержит класс `ProductFields`, предназначенный для представления и управления полями товаров в PrestaShop API. Он включает в себя методы для установки и получения значений полей, соответствующих структуре таблиц PrestaShop, а также обеспечивает базовую поддержку мультиязычных полей.

## Содержание

1. [Классы](#Классы)
   - [`ProductFields`](#ProductFields)
2. [Функции](#Функции)
    - [`_payload`](#_payload)

## Классы

### `ProductFields`

**Описание**:
Класс, описывающий поля товара в формате API PrestaShop.

**Параметры**:
- `lang_index` (int): Индекс языка.
- `product_fields_list` (List[str], optional): Список полей продукта. По умолчанию не инициализируется.
- `presta_fields` (SimpleNamespace, optional): Пространство имен для хранения полей PrestaShop. По умолчанию не инициализируется.
- `assist_fields_dict` (Dict[str, any], optional): Словарь вспомогательных полей. По умолчанию пустой словарь.
- `base_path` (Path): базовый путь к файлу. По умолчанию `gs.path.endpoints / 'prestashop'`.

**Методы**:
- `__post_init__`: Инициализация класса после создания экземпляра. Загружаются данные полей, языков и их идентификаторов.
- `_payload`: Загружает дефолтные значения полей из файлов.
- `associations` (property, setter): Возвращает/устанавливает словарь ключей ассоциаций.
- `id_product` (property, setter): Возвращает/устанавливает `ID` товара.
- `id_supplier` (property, setter): Возвращает/устанавливает `ID` поставщика.
- `id_manufacturer` (property, setter): Возвращает/устанавливает `ID` бренда.
- `id_category_default` (property, setter): Возвращает/устанавливает главную категорию товара.
- `additional_categories` (property, setter): Возвращает/устанавливает дополнительные категории товара.
- `id_shop_default` (property, setter): Возвращает/устанавливает ID магазина по умолчанию.
- `id_shop` (property, setter): Возвращает/устанавливает ID магазина.
- `id_tax` (property, setter): Возвращает/устанавливает `ID` НДС.
- `on_sale` (property, setter): Возвращает/устанавливает флаг "распродажа".
- `online_only` (property, setter): Возвращает/устанавливает флаг "только онлайн".
- `ean13` (property, setter): Возвращает/устанавливает EAN13.
- `isbn` (property, setter): Возвращает/устанавливает ISBN.
- `upc` (property, setter): Возвращает/устанавливает UPC.
- `mpn` (property, setter): Возвращает/устанавливает MPN.
- `ecotax` (property, setter): Возвращает/устанавливает эконалог.
- `minimal_quantity` (property, setter): Возвращает/устанавливает минимальное количество.
- `low_stock_threshold` (property, setter): Возвращает/устанавливает порог низкого запаса.
- `low_stock_alert` (property, setter): Возвращает/устанавливает оповещение о низком запасе.
- `price` (property, setter): Возвращает/устанавливает цену товара.
- `wholesale_price` (property, setter): Возвращает/устанавливает оптовую цену.
- `unity` (property, setter): Возвращает/устанавливает единицу измерения.
- `unit_price_ratio` (property, setter): Возвращает/устанавливает отношение цены за единицу.
- `additional_shipping_cost` (property, setter): Возвращает/устанавливает дополнительную стоимость доставки.
- `reference` (property, setter): Возвращает/устанавливает артикул.
- `supplier_reference` (property, setter): Возвращает/устанавливает артикул поставщика.
- `location` (property, setter): Возвращает/устанавливает местоположение.
- `width` (property, setter): Возвращает/устанавливает ширину.
- `height` (property, setter): Возвращает/устанавливает высоту.
- `depth` (property, setter): Возвращает/устанавливает глубину.
- `weight` (property, setter): Возвращает/устанавливает вес.
- `volume` (property, setter): Возвращает/устанавливает объем.
- `out_of_stock` (property, setter): Возвращает/устанавливает флаг "нет в наличии".
- `additional_delivery_times` (property, setter): Возвращает/устанавливает дополнительное время доставки.
- `quantity_discount` (property, setter): Возвращает/устанавливает флаг "скидка за количество".
- `customizable` (property, setter): Возвращает/устанавливает флаг "настраиваемый".
- `uploadable_files` (property, setter): Возвращает/устанавливает количество загружаемых файлов.
- `text_fields` (property, setter): Возвращает/устанавливает количество текстовых полей.
- `active` (property, setter): Возвращает/устанавливает флаг "активный".
- `redirect_type` (property, setter): Возвращает/устанавливает тип перенаправления.
- `id_type_redirected` (property, setter): Возвращает/устанавливает `ID` перенаправления.
- `available_for_order` (property, setter): Возвращает/устанавливает флаг "доступен для заказа".
- `available_date` (property, setter): Возвращает/устанавливает дату доступности.
- `show_condition` (property, setter): Возвращает/устанавливает флаг "показать состояние".
- `condition` (property, setter): Возвращает/устанавливает состояние товара.
- `show_price` (property, setter): Возвращает/устанавливает флаг "показать цену".
- `indexed` (property, setter): Возвращает/устанавливает флаг "проиндексирован".
- `visibility` (property, setter): Возвращает/устанавливает видимость товара.
- `cache_is_pack` (property, setter): Возвращает/устанавливает флаг "является набором".
- `cache_has_attachments` (property, setter): Возвращает/устанавливает флаг "есть вложения".
- `is_virtual` (property, setter): Возвращает/устанавливает флаг "виртуальный".
- `cache_default_attribute` (property, setter): Возвращает/устанавливает `ID` атрибута по умолчанию.
- `date_add` (property, setter): Возвращает/устанавливает дату добавления.
- `date_upd` (property, setter): Возвращает/устанавливает дату обновления.
- `advanced_stock_management` (property, setter): Возвращает/устанавливает флаг "управление запасами".
- `pack_stock_type` (property, setter): Возвращает/устанавливает тип управления запасами для набора.
- `state` (property, setter): Возвращает/устанавливает состояние товара.
- `product_type` (property, setter): Возвращает/устанавливает тип товара.
- `description` (property, setter): Возвращает/устанавливает описание товара.
- `description_short` (property, setter): Возвращает/устанавливает краткое описание товара.
- `link_rewrite` (property, setter): Возвращает/устанавливает ссылку для переписывания.
- `meta_description` (property, setter): Возвращает/устанавливает мета-описание товара.
- `meta_keywords` (property, setter): Возвращает/устанавливает мета-ключевые слова товара.
- `meta_title` (property, setter): Возвращает/устанавливает мета-заголовок товара.
- `name` (property, setter): Возвращает/устанавливает название товара.
- `available_now` (property, setter): Возвращает/устанавливает текст о наличии товара.
- `available_later` (property, setter): Возвращает/устанавливает текст о будущей доступности.
- `delivery_in_stock` (property, setter): Возвращает/устанавливает текст о доставке при наличии.
- `delivery_out_stock` (property, setter): Возвращает/устанавливает текст о доставке при отсутствии.
- `delivery_additional_message` (property, setter): Возвращает/устанавливает дополнительное сообщение о доставке.
- `affiliate_short_link` (property, setter): Возвращает/устанавливает короткую ссылку на партнера.
- `affiliate_text` (property, setter): Возвращает/устанавливает партнерский текст.
- `affiliate_summary` (property, setter): Возвращает/устанавливает краткое описание для партнера.
- `affiliate_summary_2` (property, setter): Возвращает/устанавливает второе краткое описание для партнера.
- `affiliate_image_small` (property, setter): Возвращает/устанавливает маленькое изображение партнера.
- `affiliate_image_medium` (property, setter): Возвращает/устанавливает среднее изображение партнера.
- `affiliate_image_large` (property, setter): Возвращает/устанавливает большое изображение партнера.
- `ingredients` (property, setter): Возвращает/устанавливает ингридиенты.
- `specification` (property, setter): Возвращает/устанавливает спецификацию.
- `how_to_use` (property, setter): Возвращает/устанавливает инструкцию по применению.
- `id_default_image` (property, setter): Возвращает/устанавливает `ID` изображения по умолчанию.
-  `link_to_video` (property, setter): Возвращает/устанавливает ссылку на видео.
- `images_urls` (property, setter): Возвращает/устанавливает список URL изображений.
- `local_image_path` (property, setter): Возвращает/устанавливает путь к локальному изображению.
- `local_video_path` (property, setter): Возвращает/устанавливает путь к локальному видео.
- `position_in_category` (property, setter): Возвращает/устанавливает позицию в категории.
- `page_lang` (property, setter): Возвращает/устанавливает код языка страницы.

## Функции

### `_payload`

**Описание**:
Загрузка дефолтных значений полей.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.