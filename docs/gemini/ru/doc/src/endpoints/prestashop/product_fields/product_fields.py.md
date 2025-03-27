# Модуль product_fields

## Обзор

Модуль `product_fields.py` предназначен для описания и управления полями товаров в формате, соответствующем API PrestaShop. Он включает класс `ProductFields`, который позволяет задавать и получать значения различных полей товара, как общих, так и мультиязычных. Модуль также содержит методы для работы с ассоциациями товара, такими как категории, изображения и характеристики.

## Подробней

Этот модуль используется для структурированного представления данных о товарах, подготавливаемых для отправки в PrestaShop API. Он обеспечивает удобный интерфейс для работы с полями товаров, поддерживая мультиязычность и различные типы данных. Класс `ProductFields` позволяет инициализировать поля товара значениями по умолчанию, устанавливать и получать значения отдельных полей, а также формировать словарь, готовый для отправки в API. Расположение файла `/src/endpoints/prestashop/product_fields/product_fields.py` указывает на его роль в подготовке данных для взаимодействия с PrestaShop.

## Классы

### `ProductFields`

**Описание**: Класс, описывающий поля товара в формате API PrestaShop. Позволяет управлять полями товара, включая мультиязычные значения и ассоциации.

**Методы**:
- `__post_init__`: Инициализирует объект класса после создания.
- `_payload`: Загружает дефолтные значения полей из файла.
- `_set_multilang_value`: Устанавливает мультиязычное значение для заданного поля.
- `id_product` (property): Возвращает ID товара.
- `id_supplier` (property): Возвращает ID поставщика.
- `id_manufacturer` (property): Возвращает ID бренда.
- `id_category_default` (property): Возвращает ID главной категории товара.
- `id_shop_default` (property): Возвращает ID магазина по умолчанию.
- `id_shop` (property): Возвращает ID магазина (для multishop).
- `id_tax` (property): Возвращает ID налога.
- `position_in_category` (property): Возвращает позицию товара в категории.
- `on_sale` (property): Возвращает флаг распродажи.
- `online_only` (property): Возвращает флаг "только онлайн".
- `ean13` (property): Возвращает EAN13 код товара.
- `isbn` (property): Возвращает ISBN код товара.
- `upc` (property): Возвращает UPC код товара.
- `mpn` (property): Возвращает MPN код товара.
- `ecotax` (property): Возвращает Эко налог.
- `minimal_quantity` (property): Возвращает минимальное количество товара для заказа.
- `low_stock_threshold` (property): Возвращает пороговое значение для уведомления о низком запасе.
- `low_stock_alert` (property): Возвращает флаг уведомления о низком запасе.
- `price` (property): Возвращает цену товара.
- `wholesale_price` (property): Возвращает оптовую цену.
- `unity` (property): Возвращает единицу измерения.
- `unit_price_ratio` (property): Возвращает соотношение цены за единицу.
- `additional_shipping_cost` (property): Возвращает дополнительную стоимость доставки.
- `reference` (property): Возвращает артикул товара.
- `supplier_reference` (property): Возвращает артикул поставщика.
- `location` (property): Возвращает местоположение товара на складе.
- `width` (property): Возвращает ширину товара.
- `height` (property): Возвращает высоту товара.
- `depth` (property): Возвращает глубину товара.
- `weight` (property): Возвращает вес товара.
- `volume` (property): Возвращает объем товара.
- `out_of_stock` (property): Возвращает действие при отсутствии товара на складе.
- `additional_delivery_times` (property): Возвращает дополнительное время доставки.
- `quantity_discount` (property): Возвращает флаг скидки на количество.
- `customizable` (property): Возвращает флаг возможности кастомизации.
- `uploadable_files` (property): Возвращает флаг возможности загрузки файлов.
- `text_fields` (property): Возвращает количество текстовых полей.
- `active` (property): Возвращает флаг активности товара.
- `redirect_type` (property): Возвращает тип редиректа.
- `id_type_redirected` (property): Возвращает ID связанного редиректа.
- `available_for_order` (property): Возвращает флаг доступности для заказа.
- `available_date` (property): Возвращает дату доступности товара.
- `show_condition` (property): Возвращает флаг отображения состояния товара.
- `condition` (property): Возвращает состояние товара.
- `show_price` (property): Возвращает флаг отображения цены.
- `indexed` (property): Возвращает флаг индексации товара.
- `visibility` (property): Возвращает видимость товара.
- `cache_is_pack` (property): Возвращает флаг кэширования как пакет товара.
- `cache_has_attachments` (property): Возвращает флаг кэширования вложений.
- `is_virtual` (property): Возвращает флаг виртуального товара.
- `cache_default_attribute` (property): Возвращает ID атрибута по умолчанию для кэширования.
- `date_add` (property): Возвращает дату добавления товара.
- `date_upd` (property): Возвращает дату обновления товара.
- `advanced_stock_management` (property): Возвращает флаг расширенного управления запасами.
- `pack_stock_type` (property): Возвращает тип управления запасами пакета товаров.
- `state` (property): Возвращает состояние товара.
- `product_type` (property): Возвращает тип товара.
- `name` (property): Возвращает название товара.
- `description` (property): Возвращает описание товара.
- `description_short` (property): Возвращает краткое описание товара.
- `link_rewrite` (property): Возвращает URL товара.
- `meta_description` (property): Возвращает Meta описание товара.
- `meta_keywords` (property): Возвращает Meta ключевые слова товара.
- `meta_title` (property): Возвращает Meta заголовок товара.
- `available_now` (property): Возвращает текст "в наличии".
- `available_later` (property): Возвращает текст "ожидается".
- `delivery_in_stock` (property): Возвращает текст доставки при наличии.
- `delivery_out_stock` (property): Возвращает текст доставки при отсутствии.
- `delivery_additional_message` (property): Возвращает дополнительное сообщение о доставке.
- `affiliate_short_link` (property): Возвращает короткую ссылку аффилиата.
- `affiliate_text` (property): Возвращает текст аффилиата.
- `affiliate_summary` (property): Возвращает краткое описание аффилиата.
- `affiliate_summary_2` (property): Возвращает второе краткое описание аффилиата.
- `affiliate_image_small` (property): Возвращает маленькое изображение аффилиата.
- `affiliate_image_medium` (property): Возвращает среднее изображение аффилиата.
- `affiliate_image_large` (property): Возвращает большое изображение аффилиата.
- `ingredients` (property): Возвращает список ингридиентов.
- `specification` (property): Возвращает спецификацию товара.
- `how_to_use` (property): Возвращает как использовать товар.
- `id_default_image` (property): Возвращает ID изображения по умолчанию.
- `link_to_video` (property): Возвращает ссылку на видео.
- `local_image_path` (property): Возвращает путь к локальному изображению.
- `local_video_path` (property): Возвращает путь к локальному видео.
- `additional_categories` (property): Возвращает список дополнительных категорий.
- `additional_category_append`: Добавляет связь с категорией, если ее еще нет.
- `additional_categories_clear`: Очищает все связи с категориями.
- `product_images` (property): Возвращает список изображений продукта.
- `product_image_append`: Добавляет связь с изображением.
- `product_images_clear`: Очищает все связи с изображениями.
- `images_urls` (property): Возвращает список URL дополнительных изображений.
- `images_urls_append`: Устанавливает список URL, откуда скачать дополнительные изображения.
- `product_combinations` (property): Возвращает список комбинаций продукта.
- `product_combination_append`: Добавляет связь с комбинацией.
- `product_combinations_clear`: Очищает все связи с комбинациями.
- `product_options` (property): Возвращает список опций продукта.
- `product_options_append`: Добавляет связь со значением опции продукта.
- `product_options_clear`: Очищает все связи со значениями опций продукта.
- `product_product_features` (property): Возвращает список характеристик продукта.
- `product_features_append`: Добавляет связь с характеристикой продукта.
- `product_features_clear`: Очищает все связи с характеристиками продукта.
- `product_product_tags` (property): Возвращает список тегов для поисковиков.
- `product_tag_append`: Добавляет связь с тегом.
- `product_tags_clear`: Очищает все связи с тегами.
- `product_stock_availables` (property): Возвращает список доступностей на складе.
- `product_stock_available_append`: Добавляет связь с доступностью на складе.
- `product_stock_availables_clear`: Очищает все связи с доступностью на складе.
- `product_attachments` (property): Возвращает список вложений продукта.
- `product_attachment_append`: Добавляет связь с вложением.
- `product_attachments_clear`: Очищает все связи с вложениями.
- `product_accessories` (property): Возвращает список аксессуаров продукта.
- `product_accessory_append`: Добавляет связь с аксессуаром.
- `product_accessories_clear`: Очищает все связи с аксессуарами.
- `product_bundle` (property): Возвращает список бандлов продукта.
- `product_bundle_append`: Добавляет связь с бандлом продукта.
- `product_bundle_clear`: Очищает все связи с бандлами продуктов.
- `to_dict`: Преобразует объект ProductFields в словарь для PrestaShop API.
- `_format_multilang_value`: Форматирует мультиязычные значения в список словарей для PrestaShop API.

**Параметры**:
- `presta_fields` (SimpleNamespace): Объект, хранящий поля товара.
- `id_lang` (int): ID языка.

**Примеры**
```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields

# Пример создания объекта ProductFields
product_fields = ProductFields()

# Пример установки значения поля
product_fields.name = 'Новый товар'

# Пример получения значения поля
name = product_fields.name

# Пример преобразования в словарь для API
product_dict = product_fields.to_dict()
```

### `EnumRedirect`

**Описание**: Перечисление для типов редиректов.

**Значения**:
- `ERROR_404`: Редирект на страницу ошибки 404.
- `REDIRECT_301_PRODUCT`: Постоянный редирект на другой товар (301).
- `REDIRECT_302_PRODUCT`: Временный редирект на другой товар (302).
- `REDIRECT_301_CATEGORY`: Постоянный редирект на категорию (301).
- `REDIRECT_302_CATEGORY`: Временный редирект на категорию (302).

### `EnumCondition`

**Описание**: Перечисление для состояний товара.

**Значения**:
- `NEW`: Новый товар.
- `USED`: Бывший в употреблении товар.
- `REFURBISHED`: Восстановленный товар.

### `EnumVisibity`

**Описание**: Перечисление для видимости товара.

**Значения**:
- `BOTH`: Виден в каталоге и при поиске.
- `CATALOG`: Виден только в каталоге.
- `SEARCH`: Виден только при поиске.
- `NONE`: Не виден.

### `EnumProductType`

**Описание**: Перечисление для типов товаров.

**Значения**:
- `STANDARD`: Стандартный товар.
- `PACK`: Пакет товаров.
- `VIRTUAL`: Виртуальный товар.
- `COMBINATIONS`: Товар с комбинациями.
- `EMPTY`: Пустой тип.

## Функции

### `_payload`

```python
def _payload(self) -> bool:
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        bool: `True`, если загрузка прошла успешно, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при загрузке или конвертации данных.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields._payload()
        True
    """
```

**Описание**: Загружает дефолтные значения полей из файлов `fields_list.txt` и `product_fields_default_values.json`.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при загрузке или конвертации данных.

**Примеры**:
```python
product_fields = ProductFields()
success = product_fields._payload()
if success:
    print('Загрузка полей прошла успешно')
else:
    print('Ошибка загрузки полей')
```

### `_set_multilang_value`

```python
def _set_multilang_value(self, field_name: str, value: str) -> bool:
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        field_name (str): Имя поля (например, 'name', 'description').
        value (str): Значение для установки.

    Returns:
        bool: `True`, если установка значения прошла успешно, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при установке значения.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.id_lang = 1
        >>> product_fields._set_multilang_value('name', 'Новый товар')
        True
    """
```

**Описание**: Устанавливает мультиязычное значение для заданного поля.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `field_name` (str): Имя поля (например, `'name'`, `'description'`).
- `value` (str): Значение для установки.

**Возвращает**:
- `bool`: `True`, если установка значения прошла успешно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при установке значения.

**Примеры**:
```python
product_fields = ProductFields()
product_fields.id_lang = 1
success = product_fields._set_multilang_value('name', 'Новый товар')
if success:
    print('Значение установлено успешно')
else:
    print('Ошибка установки значения')
```

### `additional_category_append`

```python
def additional_category_append(self, category_id: int | str):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        category_id (int | str): ID категории для добавления.

    Returns:
        None

    Raises:
        ValueError: Если `category_id` не является числом.
        Exception: Если возникает ошибка при добавлении категории.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.additional_category_append(123)
    """
```

**Описание**: Добавляет связь с категорией, если ее еще нет.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `category_id` (int | str): ID категории для добавления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если `category_id` не является числом.
- `Exception`: Если возникает ошибка при добавлении категории.

**Примеры**:
```python
product_fields = ProductFields()
product_fields.additional_category_append(123)
```

### `additional_categories_clear`

```python
def additional_categories_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.additional_categories_clear()
    """
```

**Описание**: Очищает все связи с категориями.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.additional_categories_clear()
```

### `product_image_append`

```python
def product_image_append(self, image_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        image_id (int): ID изображения для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_image_append(456)
    """
```

**Описание**: Добавляет связь с изображением.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `image_id` (int): ID изображения для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_image_append(456)
```

### `product_images_clear`

```python
def product_images_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_images_clear()
    """
```

**Описание**: Очищает все связи с изображениями.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_images_clear()
```

### `images_urls_append`

```python
def images_urls_append(self, value: List[str] = None):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        value (List[str], optional): Список URL изображений для добавления. По умолчанию `None`.

    Returns:
        None

    Raises:
        Warning: Если `value` не является списком строк.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.images_urls_append(['http://example.com/image1.jpg', 'http://example.com/image2.jpg'])
    """
```

**Описание**: Устанавливает список URL, откуда скачать дополнительные изображения.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `value` (List[str], optional): Список URL изображений для добавления. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Warning`: Если `value` не является списком строк.

**Примеры**:
```python
product_fields = ProductFields()
product_fields.images_urls_append(['http://example.com/image1.jpg', 'http://example.com/image2.jpg'])
```

### `product_combination_append`

```python
def product_combination_append(self, combination_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        combination_id (int): ID комбинации для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_combination_append(789)
    """
```

**Описание**: Добавляет связь с комбинацией.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `combination_id` (int): ID комбинации для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_combination_append(789)
```

### `product_combinations_clear`

```python
def product_combinations_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_combinations_clear()
    """
```

**Описание**: Очищает все связи с комбинациями.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_combinations_clear()
```

### `product_options_append`

```python
def product_options_append(self, product_option_value_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        product_option_value_id (int): ID опции продукта для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_options_append(1011)
    """
```

**Описание**: Добавляет связь со значением опции продукта.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `product_option_value_id` (int): ID опции продукта для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_options_append(1011)
```

### `product_options_clear`

```python
def product_options_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_options_clear()
    """
```

**Описание**: Очищает все связи со значениями опций продукта.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_options_clear()
```

### `product_features_append`

```python
def product_features_append(self, feature_id: int, feature_value_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        feature_id (int): ID характеристики продукта для добавления.
        feature_value_id (int): ID значения характеристики продукта для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_features_append(12, 34)
    """
```

**Описание**: Добавляет связь с характеристикой продукта.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `feature_id` (int): ID характеристики продукта для добавления.
- `feature_value_id` (int): ID значения характеристики продукта для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_features_append(12, 34)
```

### `product_features_clear`

```python
def product_features_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_features_clear()
    """
```

**Описание**: Очищает все связи с характеристиками продукта.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_features_clear()
```

### `product_tag_append`

```python
def product_tag_append(self, tag_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        tag_id (int): ID тега для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_tag_append(56)
    """
```

**Описание**: Добавляет связь с тегом.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `tag_id` (int): ID тега для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_tag_append(56)
```

### `product_tags_clear`

```python
def product_tags_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_tags_clear()
    """
```

**Описание**: Очищает все связи с тегами.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_tags_clear()
```

### `product_stock_available_append`

```python
def product_stock_available_append(self, stock_available_id: int, product_attribute_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        stock_available_id (int): ID доступности на складе для добавления.
        product_attribute_id (int): ID атрибута продукта для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_stock_available_append(78, 90)
    """
```

**Описание**: Добавляет связь с доступностью на складе.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `stock_available_id` (int): ID доступности на складе для добавления.
- `product_attribute_id` (int): ID атрибута продукта для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_stock_available_append(78, 90)
```

### `product_stock_availables_clear`

```python
def product_stock_availables_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_stock_availables_clear()
    """
```

**Описание**: Очищает все связи с доступностью на складе.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_stock_availables_clear()
```

### `product_attachment_append`

```python
def product_attachment_append(self, attachment_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        attachment_id (int): ID вложения для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_attachment_append(1112)
    """
```

**Описание**: Добавляет связь с вложением.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `attachment_id` (int): ID вложения для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_attachment_append(1112)
```

### `product_attachments_clear`

```python
def product_attachments_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_attachments_clear()
    """
```

**Описание**: Очищает все связи с вложениями.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_attachments_clear()
```

### `product_accessory_append`

```python
def product_accessory_append(self, accessory_id: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        accessory_id (int): ID аксессуара для добавления.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_accessory_append(1314)
    """
```

**Описание**: Добавляет связь с аксессуаром.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `accessory_id` (int): ID аксессуара для добавления.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_accessory_append(1314)
```

### `product_accessories_clear`

```python
def product_accessories_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_accessories_clear()
    """
```

**Описание**: Очищает все связи с аксессуарами.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_accessories_clear()
```

### `product_bundle_append`

```python
def product_bundle_append(self, bundle_id: int, product_attribute_id: int, quantity: int):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.
        bundle_id (int): ID бандла продукта для добавления.
        product_attribute_id (int): ID атрибута продукта для добавления.
        quantity (int): Количество продукта в бандле.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_bundle_append(1516, 1718, 2)
    """
```

**Описание**: Добавляет связь с бандлом продукта.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.
- `bundle_id` (int): ID бандла продукта для добавления.
- `product_attribute_id` (int): ID атрибута продукта для добавления.
- `quantity` (int): Количество продукта в бандле.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_bundle_append(1516, 1718, 2)
```

### `product_bundle_clear`

```python
def product_bundle_clear(self):
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        None

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.product_bundle_clear()
    """
```

**Описание**: Очищает все связи с бандлами продуктов.

**Параметры**:
- `self`: Экземпляр класса `ProductFields`.

**Возвращает**:
- `None`

**Примеры**:
```python
product_fields = ProductFields()
product_fields.product_bundle_clear()
```

### `to_dict`

```python
def to_dict(self) -> Dict[str, Any]:
    """
    Args:
        self (ProductFields): Экземпляр класса `ProductFields`.

    Returns:
        Dict[str, Any]: Словарь с полями, готовый для PrestaShop API.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.name = 'Новый товар'
        >>> product_dict = product_fields.to_dict()
        >>> print(product_dict)
        {'name': [{'language': {'id': '1'}, 'value': 'Новый товар'