# Модуль product_fields

## Обзор

Модуль `product_fields.py` предназначен для описания полей товара в формате API PrestaShop. Он содержит класс `ProductFields`, который определяет структуру и методы для работы с полями товара, включая мультиязычные значения и связи с другими сущностями PrestaShop, такими как категории, изображения и характеристики.

## Подробней

Модуль предоставляет класс `ProductFields`, который упрощает взаимодействие с API PrestaShop при создании и обновлении информации о товарах. Он включает механизмы для загрузки дефолтных значений полей, установки мультиязычных значений, а также для управления связями с другими объектами, такими как категории, изображения и комбинации товаров.

## Классы

### `ProductFields`

**Описание**: Класс, описывающий поля товара в формате API PrestaShop. Предоставляет методы для установки и получения значений полей товара, а также для управления связями с другими сущностями PrestaShop.

**Методы**:
- `__post_init__`: Инициализирует объект класса после создания экземпляра.
- `_payload`: Загружает дефолтные значения полей.
- `_set_multilang_value`: Устанавливает мультиязычное значение для заданного поля.
- `id_product`: property `ps_product.id_product: int(10) unsigned`
- `id_product`: setter `ID` товара. Для нового товара id назначается из `PrestaShop`.
- `id_supplier`: property `ps_product.id_supplier: int(10) unsigned`
- `id_supplier`: setter `ID` поставщика.
- `id_manufacturer`: property `ps_product.id_manufacturer: int(10) unsigned`
- `id_manufacturer`: setter `ID` бренда.
- `id_category_default`: property `ps_product.id_category_default: int(10) unsigned`
- `id_category_default`: setter `ID` главной категории товара.
- `id_shop_default`: property `ps_product.id_shop_default: int(10) unsigned`
- `id_shop_default`: setter `ID` магазина по умолчанию.
- `id_shop`: property `ps_product.id_shop: int(10) unsigned`
- `id_shop`: setter `ID` магазина (для multishop).
- `id_tax`: property `ps_product.id_tax: int(11) unsigned`
- `id_tax`: setter `ID` налога.
- `position_in_category`: property `ps_category_product.position: int(10) unsigned`
- `position_in_category`: setter Позиция товара в категории.
- `on_sale`: property `ps_product.on_sale: tinyint(1) unsigned`
- `on_sale`: setter Флаг распродажи.
- `online_only`: property `ps_product.online_only: tinyint(1) unsigned`
- `online_only`: setter Флаг "только онлайн".
- `ean13`: property `ps_product.ean13: varchar(13)`
- `ean13`: setter EAN13 код товара.
- `isbn`: property `ps_product.isbn: varchar(32)`
- `isbn`: setter ISBN код товара.
- `upc`: property `ps_product.upc: varchar(12)`
- `upc`: setter UPC код товара.
- `mpn`: property `ps_product.mpn: varchar(40)`
- `mpn`: setter MPN код товара.
- `ecotax`: property `ps_product.ecotax: decimal(17,6)`
- `ecotax`: setter Эко налог.
- `minimal_quantity`: property `ps_product.minimal_quantity: int(10) unsigned`
- `minimal_quantity`: setter Минимальное количество товара для заказа.
- `low_stock_threshold`: property `ps_product.low_stock_threshold: int(10)`
- `low_stock_threshold`: setter Пороговое значение для уведомления о низком запасе.
- `low_stock_alert`: property `ps_product.low_stock_alert: tinyint(1)`
- `low_stock_alert`: setter Флаг уведомления о низком запасе.
- `price`: property `ps_product.price: decimal(20,6)`
- `price`: setter Цена товара.
- `wholesale_price`: property `ps_product.wholesale_price: decimal(20,6)`
- `wholesale_price`: setter Оптовая цена.
- `unity`: property `ps_product.unity: varchar(255)`
- `unity`: setter Единица измерения.
- `unit_price_ratio`: property `ps_product.unit_price_ratio: decimal(20,6)`
- `unit_price_ratio`: setter Соотношение цены за единицу.
- `additional_shipping_cost`: property `ps_product.additional_shipping_cost: decimal(20,6)`
- `additional_shipping_cost`: setter Дополнительная стоимость доставки.
- `reference`: property `ps_product.reference: varchar(64)`
- `reference`: setter Артикул товара.
- `supplier_reference`: property `ps_product.supplier_reference: varchar(64)`
- `supplier_reference`: setter Артикул поставщика.
- `location`: property `ps_product.location: varchar(255)`
- `location`: setter Местоположение товара на складе.
- `width`: property `ps_product.width: decimal(20,6)`
- `width`: setter Ширина товара.
- `height`: property `ps_product.height: decimal(20,6)`
- `height`: setter Высота товара.
- `depth`: property `ps_product.depth: decimal(20,6)`
- `depth`: setter Глубина товара.
- `weight`: property `ps_product.weight: decimal(20,6)`
- `weight`: setter Вес товара.
- `volume`: property `ps_product.volume: varchar(100)`
- `volume`: setter Объем товара.
- `out_of_stock`: property `ps_product.out_of_stock: int(10) unsigned`
- `out_of_stock`: setter Действие при отсутствии товара на складе.
- `additional_delivery_times`: property `ps_product.additional_delivery_times: tinyint(1) unsigned`
- `additional_delivery_times`: setter Дополнительное время доставки.
- `quantity_discount`: property `ps_product.quantity_discount: tinyint(1)`
- `quantity_discount`: setter Флаг скидки на количество.
- `customizable`: property `ps_product.customizable: tinyint(2)`
- `customizable`: setter Флаг возможности кастомизации.
- `uploadable_files`: property `ps_product.uploadable_files: tinyint(4)`
- `uploadable_files`: setter Флаг возможности загрузки файлов.
- `text_fields`: property `ps_product.text_fields: tinyint(4)`
- `text_fields`: setter Количество текстовых полей.
- `active`: property `ps_product.active: tinyint(1) unsigned`
- `active`: setter Флаг активности товара.
- `redirect_type`: property `ps_product.redirect_type: enum('404','301-product','302-product','301-category','302-category')`
- `redirect_type`: setter Тип редиректа.
- `id_type_redirected`: property `ps_product.id_type_redirected: int(10) unsigned`
- `id_type_redirected`: setter ID связанного редиректа.
- `available_for_order`: property `ps_product.available_for_order: tinyint(1)`
- `available_for_order`: setter Флаг доступности для заказа.
- `available_date`: property `ps_product.available_date: date`
- `available_date`: setter Дата доступности товара.
- `show_condition`: property `ps_product.show_condition: tinyint(1)`
- `show_condition`: setter Флаг отображения состояния товара.
- `condition`: property `ps_product.condition: enum('new','used','refurbished')`
- `condition`: setter Состояние товара.
- `show_price`: property `ps_product.show_price: tinyint(1)`
- `show_price`: setter Флаг отображения цены.
- `indexed`: property `ps_product.indexed: tinyint(1)`
- `indexed`: setter Флаг индексации товара.
- `visibility`: property `ps_product.visibility: enum('both','catalog','search','none')`
- `visibility`: setter Видимость товара.
- `cache_is_pack`: property `ps_product.cache_is_pack: tinyint(1)`
- `cache_is_pack`: setter Флаг кэширования как пакет товара.
- `cache_has_attachments`: property `ps_product.cache_has_attachments: tinyint(1)`
- `cache_has_attachments`: setter Флаг кэширования вложений.
- `is_virtual`: property `ps_product.is_virtual: tinyint(1)`
- `is_virtual`: setter Флаг виртуального товара.
- `cache_default_attribute`: property `ps_product.cache_default_attribute: int(10) unsigned`
- `cache_default_attribute`: setter ID атрибута по умолчанию для кэширования.
- `date_add`: property `ps_product.date_add: datetime`
- `date_add`: setter Дата добавления товара.
- `date_upd`: property `ps_product.date_upd: datetime`
- `date_upd`: setter Дата обновления товара.
- `advanced_stock_management`: property `ps_product.advanced_stock_management: tinyint(1)`
- `advanced_stock_management`: setter Флаг расширенного управления запасами.
- `pack_stock_type`: property `ps_product.pack_stock_type: int(11) unsigned`
- `pack_stock_type`: setter Тип управления запасами пакета товаров.
- `state`: property `ps_product.state: int(11) unsigned`
- `state`: setter Состояние товара.
- `product_type`: property `ps_product.product_type: enum('standard', 'pack', 'virtual', 'combinations', '')`
- `product_type`: setter Тип товара.
- `name`: property `ps_product_lang.name: varchar(128)`
- `name`: setter Название товара. Мультиязычное поле.
- `description`: property `ps_product_lang.description: text`
- `description`: setter Описание товара. Мультиязычное поле.
- `description_short`: property `ps_product_lang.description_short: text`
- `description_short`: setter Краткое описание товара. Мультиязычное поле.
- `link_rewrite`: property `ps_product_lang.link_rewrite: varchar(128)`
- `link_rewrite`: setter URL товара. Мультиязычное поле.
- `meta_description`: property `ps_product_lang.meta_description: varchar(512)`
- `meta_description`: setter Meta описание товара. Мультиязычное поле.
- `meta_keywords`: property `ps_product_lang.meta_keywords: varchar(255)`
- `meta_keywords`: setter Meta ключевые слова товара. Мультиязычное поле.
- `meta_title`: property `ps_product_lang.meta_title: varchar(128)`
- `meta_title`: setter Meta заголовок товара. Мультиязычное поле.
- `available_now`: property `ps_product_lang.available_now: varchar(255)`
- `available_now`: setter Текст "в наличии". Мультиязычное поле.
- `available_later`: property `ps_product_lang.available_later: varchar(255)`
- `available_later`: setter Текст "ожидается". Мультиязычное поле.
- `delivery_in_stock`: property `ps_product_lang.delivery_in_stock: varchar(255)`
- `delivery_in_stock`: setter Текст доставки при наличии. Мультиязычное поле.
- `delivery_out_stock`: property `ps_product_lang.delivery_out_stock: varchar(255)`
- `delivery_out_stock`: setter Текст доставки при отсутствии. Мультиязычное поле.
- `delivery_additional_message`: property `ps_product_lang.delivery_additional_message: tinytext`
- `delivery_additional_message`: setter Дополнительное сообщение о доставке. Мультиязычное поле.
- `affiliate_short_link`: property `ps_product_lang.affiliate_short_link: tinytext`
- `affiliate_short_link`: setter Короткая ссылка аффилиата. Мультиязычное поле.
- `affiliate_text`: property `ps_product_lang.affiliate_text: tinytext`
- `affiliate_text`: setter Текст аффилиата. Мультиязычное поле.
- `affiliate_summary`: property `ps_product_lang.affiliate_summary: tinytext`
- `affiliate_summary`: setter Краткое описание аффилиата. Мультиязычное поле.
- `affiliate_summary_2`: property `ps_product_lang.affiliate_summary_2: tinytext`
- `affiliate_summary_2`: setter Второе краткое описание аффилиата. Мультиязычное поле.
- `affiliate_image_small`: property `ps_product_lang.affiliate_image_small: varchar(512)`
- `affiliate_image_small`: setter Маленькое изображение аффилиата. Мультиязычное поле.
- `affiliate_image_medium`: property `ps_product_lang.affiliate_image_medium: varchar(512)`
- `affiliate_image_medium`: setter Среднее изображение аффилиата. Мультиязычное поле.
- `affiliate_image_large`: property `ps_product_lang.affiliate_image_large: varchar(512)`
- `affiliate_image_large`: setter Большое изображение аффилиата. Мультиязычное поле.
- `ingredients`: property `ps_product_lang.ingredients: tinytext`
- `ingredients`: setter Список ингридиентов. Мультиязычное поле.
- `specification`: property `ps_product_lang.specification: tinytext`
- `specification`: setter Спецификация товара. Мультиязычное поле.
- `how_to_use`: property `ps_product_lang.how_to_use: tinytext`
- `how_to_use`: setter Как использовать товар. Мультиязычное поле.
- `id_default_image`: property `ps_product.id_default_image: int(10) unsigned`
- `id_default_image`: setter ID изображения по умолчанию.
- `link_to_video`: property `ps_product.link_to_video: varchar(255)`
- `link_to_video`: setter Ссылка на видео.
- `local_image_path`: property Путь к локальному изображению.
- `local_image_path`: setter Устанавливает путь к локальному изображению.
- `local_video_path`: property Путь к локальному видео.
- `local_video_path`: setter Устанавливает путь к локальному видео.
- `_ensure_associations`: Убеждается, что структура associations существует в `presta_fields`.
- `additional_categories`: property
- `additional_category_append`: Добавляет связь с категорией, если ее еще нет.
- `additional_categories_clear`: Очищает все связи с категориями.
- `product_images`: property
- `product_image_append`: Добавляет связь с изображением.
- `product_images_clear`: Очищает все связи с изображениями.
- `images_urls`: property Список URL дополнительных изображений.
- `images_urls_append`: Устанавливает список URL, откуда скачать дополнительные изображения.
- `product_images_clear`: Очищает все связи с изображениями.
- `product_combinations`: property
- `product_combination_append`: Добавляет связь с комбинацией.
- `product_combinations_clear`: Очищает все связи с комбинациями.
- `product_options`: property
- `product_options_append`: Добавляет связь со значением опции продукта.
- `product_options_clear`: Очищает все связи со значениями опций продукта.
- `product_product_features`: property
- `product_features_append`: Добавляет связь с характеристикой продукта.
- `product_features_clear`: Очищает все связи с характеристиками продукта.
- `product_product_tags`: Возвращает список тегов для поисковиков
- `product_tag_append`: Добавляет связь с тегом.
- `product_tags_clear`: Очищает все связи с тегами.
- `product_stock_availables`: property
- `product_stock_available_append`: Добавляет связь с доступностью на складе.
- `product_stock_availables_clear`: Очищает все связи с доступностью на складе.
- `product_attachments`: property
- `product_attachment_append`: Добавляет связь с вложением.
- `product_attachments_clear`: Очищает все связи с вложениями.
- `product_accessories`: property
- `product_accessory_append`: Добавляет связь с аксессуаром.
- `product_accessories_clear`: Очищает все связи с аксессуарами.
- `product_bundle`: property
- `product_bundle_append`: Добавляет связь с бандлом продукта.
- `product_bundle_clear`: Очищает все связи с бандлами продуктов.
- `to_dict`: Преобразует объект `ProductFields` в словарь для PrestaShop API.
- `_format_multilang_value`: Форматирует мультиязычные значения в список словарей для PrestaShop API.

**Параметры**:
- `presta_fields` (SimpleNamespace): Объект, хранящий поля товара.
- `id_lang` (int): ID языка.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
product_fields.name = 'Example Product'
print(product_fields.name)
```

### `EnumRedirect`

**Описание**: Перечисление для типов редиректов.

**Элементы**:
- `ERROR_404 = '404'`
- `REDIRECT_301_PRODUCT = '301-product'`
- `REDIRECT_302_PRODUCT = '302-product'`
- `REDIRECT_301_CATEGORY = '301-category'`
- `REDIRECT_302_CATEGORY = '302-category'`

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
product_fields.redirect_type = ProductFields.EnumRedirect.ERROR_404
print(product_fields.redirect_type)
```

### `EnumCondition`

**Описание**: Перечисление для состояний товара.

**Элементы**:
- `NEW = 'new'`
- `USED = 'used'`
- `REFURBISHED = 'refurbished'`

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
product_fields.condition = ProductFields.EnumCondition.NEW
print(product_fields.condition)
```

### `EnumVisibity`

**Описание**: Перечисление для видимости товара.

**Элементы**:
- `BOTH = 'both'`
- `CATALOG = 'catalog'`
- `SEARCH = 'search'`
- `NONE = 'none'`

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
product_fields.visibility = ProductFields.EnumVisibity.BOTH
print(product_fields.visibility)
```

### `EnumProductType`

**Описание**: Перечисление для типов товаров.

**Элементы**:
- `STANDARD = 'standard'`
- `PACK = 'pack'`
- `VIRTUAL = 'virtual'`
- `COMBINATIONS = 'combinations'`
- `EMPTY = ''`

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
product_fields.product_type = ProductFields.EnumProductType.STANDARD
print(product_fields.product_type)
```

## Функции

### `_payload`

```python
def _payload(self) -> bool:
    """
    Загрузка дефолтных значений полей.
    Returns:
        bool: True, если загрузка прошла успешно, иначе False.
    """
    ...
```

**Описание**: Загружает дефолтные значения полей товара из файла `product_fields_default_values.json` и списка полей из `fields_list.txt`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
result = product_fields._payload()
print(result)
```

### `_set_multilang_value`

```python
def _set_multilang_value(self, field_name: str, value: str, id_lang: Optional[Union[int, str]] = None) -> bool:
    """
    Устанавливает мультиязычное значение для заданного поля.

    Args:
        field_name (str): Имя поля (например, 'name', 'description').
        value (str): Значение для установки.
        id_lang (Optional[Union[int, str]]): ID языка. Если не указан, используется self.id_lan.

    Returns:
        bool: True, если значение успешно установлено, False в случае ошибки.
    """
    ...
```

**Описание**: Устанавливает мультиязычное значение для заданного поля товара.

**Параметры**:
- `field_name` (str): Имя поля (например, `'name'`, `'description'`).
- `value` (str): Значение для установки.
- `id_lang` (Optional[Union[int, str]], optional): ID языка. Если не указан, используется `self.id_lan`.

**Возвращает**:
- `bool`: `True`, если значение успешно установлено, `False` в случае ошибки.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
result = product_fields._set_multilang_value('name', 'Example Product', 2)
print(result)
```

### `to_dict`

```python
def to_dict(self) -> Dict[str, Any]:
    """
    Преобразует объект ProductFields в словарь для PrestaShop API,
    исключая ключи, значения которых равны None или пустой строке,
    и формирует мультиязычные поля в нужном формате. Все поля должны быть представлены как строки.

    Returns:
        Dict[str, Any]: Словарь с полями, готовый для PrestaShop API.
    """
    ...
```

**Описание**: Преобразует объект `ProductFields` в словарь, пригодный для использования в PrestaShop API.

**Возвращает**:
- `Dict[str, Any]`: Словарь с полями товара, готовый для PrestaShop API.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
product_fields = ProductFields()
product_fields.name = 'Example Product'
product_dict = product_fields.to_dict()
print(product_dict)
```