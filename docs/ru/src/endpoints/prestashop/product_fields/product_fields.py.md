# Модуль product_fields

## Обзор

Модуль `product_fields` предназначен для описания и управления полями товаров в формате, требуемом для API PrestaShop. Он содержит класс `ProductFields`, который позволяет загружать, устанавливать и форматировать значения полей товаров, включая мультиязычные значения и связи с другими сущностями, такими как категории и изображения.

## Подробней

Этот модуль обеспечивает абстракцию для работы с данными о товарах, используемыми PrestaShop. Он определяет структуру данных и методы для управления этими данными, что упрощает взаимодействие с API PrestaShop.

## Классы

### `ProductFields`

**Описание**: Класс для представления полей товара в формате API PrestaShop.
Индексы языков, которые устанавливаются в БД PrestaShop:
1. Английский
2. Иврит
3. Русский

**Принцип работы**:
Класс `ProductFields` предназначен для хранения и управления полями товара, необходимыми для API PrestaShop. Он инициализируется с предопределенными полями и предоставляет методы для установки и получения значений этих полей. Класс также обеспечивает поддержку мультиязычных значений и связей с другими сущностями, такими как категории и изображения.

**Атрибуты**:
- `presta_fields` (SimpleNamespace): Объект, содержащий поля товара. Инициализируется в методе `__post_init__`.
- `id_lang` (int): ID языка, используемый по умолчанию. По умолчанию равен 1.

**Методы**:

- `__post_init__()`: Инициализирует объект `ProductFields` после создания экземпляра класса.
- `_payload()`: Загружает значения полей товара из файлов конфигурации.
- `_set_multilang_value(field_name: str, value: str, id_lang: Optional[int | str] = None) -> bool`: Устанавливает мультиязычное значение для заданного поля.
- `id_product` (property): Управляет полем `id_product` (ID товара).
- `id_supplier` (property): Управляет полем `id_supplier` (ID поставщика).
- `id_manufacturer` (property): Управляет полем `id_manufacturer` (ID производителя).
- `id_category_default` (property): Управляет полем `id_category_default` (ID категории по умолчанию).
- `id_shop_default` (property): Управляет полем `id_shop_default` (ID магазина по умолчанию).
- `id_shop` (property): Управляет полем `id_shop` (ID магазина).
- `id_tax` (property): Управляет полем `id_tax` (ID налога).
- `position_in_category` (property): Управляет полем `position_in_category` (позиция в категории).
- `on_sale` (property): Управляет полем `on_sale` (флаг распродажи).
- `online_only` (property): Управляет полем `online_only` (флаг "только онлайн").
- `ean13` (property): Управляет полем `ean13` (код EAN13).
- `isbn` (property): Управляет полем `isbn` (код ISBN).
- `upc` (property): Управляет полем `upc` (код UPC).
- `mpn` (property): Управляет полем `mpn` (код MPN).
- `ecotax` (property): Управляет полем `ecotax` (экологический налог).
- `minimal_quantity` (property): Управляет полем `minimal_quantity` (минимальное количество).
- `low_stock_threshold` (property): Управляет полем `low_stock_threshold` (порог низкого запаса).
- `low_stock_alert` (property): Управляет полем `low_stock_alert` (уведомление о низком запасе).
- `price` (property): Управляет полем `price` (цена).
- `wholesale_price` (property): Управляет полем `wholesale_price` (оптовая цена).
- `unity` (property): Управляет полем `unity` (единица измерения).
- `unit_price_ratio` (property): Управляет полем `unit_price_ratio` (соотношение цены за единицу).
- `additional_shipping_cost` (property): Управляет полем `additional_shipping_cost` (дополнительная стоимость доставки).
- `reference` (property): Управляет полем `reference` (артикул).
- `supplier_reference` (property): Управляет полем `supplier_reference` (артикул поставщика).
- `location` (property): Управляет полем `location` (местоположение на складе).
- `width` (property): Управляет полем `width` (ширина).
- `height` (property): Управляет полем `height` (высота).
- `depth` (property): Управляет полем `depth` (глубина).
- `weight` (property): Управляет полем `weight` (вес).
- `volume` (property): Управляет полем `volume` (объем).
- `out_of_stock` (property): Управляет полем `out_of_stock` (действие при отсутствии на складе).
- `additional_delivery_times` (property): Управляет полем `additional_delivery_times` (дополнительное время доставки).
- `quantity_discount` (property): Управляет полем `quantity_discount` (скидка за количество).
- `customizable` (property): Управляет полем `customizable` (возможность кастомизации).
- `uploadable_files` (property): Управляет полем `uploadable_files` (возможность загрузки файлов).
- `text_fields` (property): Управляет полем `text_fields` (количество текстовых полей).
- `active` (property): Управляет полем `active` (активность товара).
- `redirect_type` (property): Управляет полем `redirect_type` (тип редиректа).
- `id_type_redirected` (property): Управляет полем `id_type_redirected` (ID связанного редиректа).
- `available_for_order` (property): Управляет полем `available_for_order` (доступность для заказа).
- `available_date` (property): Управляет полем `available_date` (дата доступности).
- `show_condition` (property): Управляет полем `show_condition` (отображение состояния).
- `condition` (property): Управляет полем `condition` (состояние товара).
- `show_price` (property): Управляет полем `show_price` (отображение цены).
- `indexed` (property): Управляет полем `indexed` (индексация).
- `visibility` (property): Управляет полем `visibility` (видимость).
- `cache_is_pack` (property): Управляет полем `cache_is_pack` (кэширование как пакет).
- `cache_has_attachments` (property): Управляет полем `cache_has_attachments` (кэширование вложений).
- `is_virtual` (property): Управляет полем `is_virtual` (виртуальный товар).
- `cache_default_attribute` (property): Управляет полем `cache_default_attribute` (атрибут по умолчанию для кэширования).
- `date_add` (property): Управляет полем `date_add` (дата добавления).
- `date_upd` (property): Управляет полем `date_upd` (дата обновления).
- `advanced_stock_management` (property): Управляет полем `advanced_stock_management` (расширенное управление запасами).
- `pack_stock_type` (property): Управляет полем `pack_stock_type` (тип управления запасами пакета).
- `state` (property): Управляет полем `state` (состояние).
- `product_type` (property): Управляет полем `product_type` (тип товара).
- `name` (property): Управляет полем `name` (название).
- `description` (property): Управляет полем `description` (описание).
- `description_short` (property): Управляет полем `description_short` (краткое описание).
- `link_rewrite` (property): Управляет полем `link_rewrite` (URL).
- `meta_description` (property): Управляет полем `meta_description` (мета-описание).
- `meta_keywords` (property): Управляет полем `meta_keywords` (мета-ключевые слова).
- `meta_title` (property): Управляет полем `meta_title` (мета-заголовок).
- `available_now` (property): Управляет полем `available_now` (текст "в наличии").
- `available_later` (property): Управляет полем `available_later` (текст "ожидается").
- `delivery_in_stock` (property): Управляет полем `delivery_in_stock` (текст доставки при наличии).
- `delivery_out_stock` (property): Управляет полем `delivery_out_stock` (текст доставки при отсутствии).
- `delivery_additional_message` (property): Управляет полем `delivery_additional_message` (дополнительное сообщение о доставке).
- `affiliate_short_link` (property): Управляет полем `affiliate_short_link` (короткая ссылка аффилиата).
- `affiliate_text` (property): Управляет полем `affiliate_text` (текст аффилиата).
- `affiliate_summary` (property): Управляет полем `affiliate_summary` (краткое описание аффилиата).
- `affiliate_summary_2` (property): Управляет полем `affiliate_summary_2` (второе краткое описание аффилиата).
- `affiliate_image_small` (property): Управляет полем `affiliate_image_small` (маленькое изображение аффилиата).
- `affiliate_image_medium` (property): Управляет полем `affiliate_image_medium` (среднее изображение аффилиата).
- `affiliate_image_large` (property): Управляет полем `affiliate_image_large` (большое изображение аффилиата).
- `ingredients` (property): Управляет полем `ingredients` (список ингредиентов).
- `specification` (property): Управляет полем `specification` (спецификация товара).
- `how_to_use` (property): Управляет полем `how_to_use` (как использовать товар).
- `id_default_image` (property): Управляет полем `id_default_image` (ID изображения по умолчанию).
- `link_to_video` (property): Управляет полем `link_to_video` (ссылка на видео).
- `local_image_path` (property): Управляет полем `local_image_path` (путь к локальному изображению).
- `local_video_path` (property): Управляет полем `local_video_path` (путь к локальному видео).
- `additional_categories` (property): Возвращает дополнительные категории товара.
- `additional_category_append` (method): Добавляет связь с категорией, если её ещё нет.
- `additional_categories_clear` (method): Очищает все связи с категориями.
- `product_images` (property): Возвращает список изображений продукта.
- `product_image_append` (method): Добавляет связь с изображением продукта.
- `product_images_clear` (method): Очищает все связи с изображениями продукта.
- `images_urls` (property): Возвращает список URL дополнительных изображений.
- `images_urls_append` (method): Устанавливает список URL, откуда скачать дополнительные изображения.
- `product_images_clear` (method): Очищает все связи с изображениями.
- `product_combinations` (property): Возвращает список комбинаций продукта.
- `product_combination_append` (method): Добавляет связь с комбинацией продукта.
- `product_combinations_clear` (method): Очищает все связи с комбинациями продукта.
- `product_options` (property): Возвращает список опций продукта.
- `product_options_append` (method): Добавляет связь со значением опции продукта.
- `product_options_clear` (method): Очищает все связи со значениями опций продукта.
- `product_product_features` (property): Возвращает список характеристик продукта.
- `product_features_append` (method): Добавляет связь с характеристикой продукта.
- `product_features_clear` (method): Очищает все связи с характеристиками продукта.
- `product_product_tags` (property): Возвращает список тегов продукта.
- `product_tag_append` (method): Добавляет связь с тегом продукта.
- `product_tags_clear` (method): Очищает все связи с тегами продукта.
- `product_stock_availables` (property): Возвращает список доступностей на складе.
- `product_stock_available_append` (method): Добавляет связь с доступностью на складе.
- `product_stock_availables_clear` (method): Очищает все связи с доступностью на складе.
- `product_attachments` (property): Возвращает список вложений продукта.
- `product_attachment_append` (method): Добавляет связь с вложением продукта.
- `product_attachments_clear` (method): Очищает все связи с вложениями продукта.
- `product_accessories` (property): Возвращает список аксессуаров продукта.
- `product_accessory_append` (method): Добавляет связь с аксессуаром продукта.
- `product_accessories_clear` (method): Очищает все связи с аксессуарами продукта.
- `product_bundle` (property): Возвращает список бандлов продукта.
- `product_bundle_append` (method): Добавляет связь с бандлом продукта.
- `product_bundle_clear` (method): Очищает все связи с бандлами продукта.
- `to_dict()`: Преобразует объект `ProductFields` в словарь для PrestaShop API.
- `_format_multilang_value(data: Any) -> List[Dict[str, str]]`: Форматирует мультиязычные значения в список словарей для PrestaShop API.

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

**Назначение**:
Функция `_payload` предназначена для загрузки значений полей товара по умолчанию из файлов конфигурации. Она считывает список полей из файла `fields_list.txt` и значения по умолчанию из файла `product_fields_default_values.json`.

**Как работает функция**:

1. **Определение базового пути**:
   - Определяет базовый путь к директории с файлами конфигурации (`fields_list.txt` и `product_fields_default_values.json`).
2. **Чтение списка полей**:
   - Считывает список полей из файла `fields_list.txt` и сохраняет его в переменной `presta_fields_list`.
   - Если файл не удалось прочитать, функция логирует ошибку и возвращает `False`.
3. **Создание объекта SimpleNamespace**:
   - Преобразует список полей в объект `SimpleNamespace`, где каждому полю присваивается значение `None`.
   - Если происходит ошибка при конвертации, функция логирует ошибку и возвращает `None`.
4. **Загрузка значений по умолчанию**:
   - Загружает значения по умолчанию из файла `product_fields_default_values.json` и сохраняет их в словаре `data_dict`.
   - Если файл не удалось загрузить, функция логирует предупреждение и возвращает `False`.
5. **Установка значений по умолчанию**:
   - Устанавливает значения по умолчанию для каждого поля в объекте `self.presta_fields`.
   - Если происходит ошибка при установке значений, функция логирует ошибку и возвращает `False`.

**ASCII flowchart**:

```
A[Определение базового пути]
|
B[Чтение списка полей из fields_list.txt]
|
C[Создание объекта SimpleNamespace с полями из списка]
|
D[Загрузка значений по умолчанию из product_fields_default_values.json]
|
E[Установка значений по умолчанию для полей в self.presta_fields]
|
F[Возврат True при успешной загрузке, False при ошибке]
```

**Примеры**:

```python
product_fields = ProductFields()
result = product_fields._payload()
print(result)  # Вывод: True или False в зависимости от результата загрузки
```

### `_set_multilang_value`

```python
def _set_multilang_value(self, field_name: str, value: str, id_lang: Optional[int | str] = None) -> bool:
    """
    Устанавливает мультиязычное значение для заданного поля.

    Args:
        field_name (str): Имя поля (например, 'name', 'description').
        value (str): Значение для установки.
        id_lang (Optional[Union[int, str]]): ID языка. Если не указан, используется self.id_lan.

    Описание:
        Функция устанавливает мультиязычное значение для указанного поля объекта.  
        Поле может хранить значения для разных языков.  Значения хранятся в виде списка словарей,
        где каждый словарь представляет собой значение для определенного языка и имеет структуру:

        {'attrs': {'id': 'language_id'}, 'value': 'language_value'}
         {'id': 'language_id'}, 'value': 'language_value'}

        - 'attrs': Словарь, содержащий атрибуты значения.  В данном случае, обязательным атрибутом является 'id',
                   который представляет собой идентификатор языка.
        - 'value': Значение поля для указанного языка.

        Если поле с указанным именем не существует, оно создается. Если поле существует, но не имеет
        ожидаемой структуры (словарь с ключом 'language', содержащим список), поле перезаписывается.
        Если поле существует и имеет правильную структуру, функция пытается обновить значение для
        указанного языка. Если язык уже существует в списке, его значение обновляется. Если язык
        не существует, добавляется новая запись в список.

    Returns:
        bool: True, если значение успешно установлено, False в случае ошибки.
    """
    ...
```

**Назначение**:
Функция `_set_multilang_value` устанавливает мультиязычное значение для указанного поля объекта `ProductFields`.

**Параметры**:
- `field_name` (str): Имя поля, для которого устанавливается значение (например, `'name'`, `'description'`).
- `value` (str): Значение, которое необходимо установить для указанного поля.
- `id_lang` (Optional[int | str], optional): ID языка, для которого устанавливается значение. Если не указан, используется `self.id_lang`. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если значение успешно установлено, `False` в случае ошибки.

**Как работает функция**:

1. **Определение ID языка**:
   - Преобразует `id_lang` в целое число, если оно предоставлено, иначе использует `self.id_lang`.
2. **Формирование данных языка**:
   - Создает словарь `lang_data` с атрибутом `@id`, содержащим ID языка, и атрибутом `#text`, содержащим значение для установки.
3. **Обработка поля**:
   - Пытается получить текущее значение поля `field_name` из `self.presta_fields`. Если поле не существует, устанавливает его в `None`.
4. **Создание или обновление языковых данных**:
   - Если поле не существует (`field is None`), создает словарь с ключом `'language'`, содержащим `lang_data`.
   - Если поле существует, проверяет, является ли оно словарем с ключом `'language'`, содержащим список. Если структура поля не соответствует ожидаемой, поле перезаписывается, и создается словарь с ключом `'language'`, содержащим `lang_data`.
   - Если поле существует и имеет правильную структуру, функция пытается найти существующую запись для указанного языка и обновляет её значение. Если запись для языка не найдена, `lang_data` добавляется в список языков.
5. **Обработка исключений**:
   - В случае возникновения исключения, функция логирует ошибку и возвращает `False`.

**ASCII flowchart**:

```
A[Получение ID языка]
|
B[Формирование данных языка (lang_data)]
|
C[Получение текущего значения поля (field)]
|
D[Проверка существования поля (field is None)]
|
E[Создание нового поля с языковыми данными]
|
F[Проверка структуры существующего поля]
|
G[Обновление или добавление языковых данных в существующее поле]
|
H[Обработка исключений]
|
I[Возврат True при успехе, False при ошибке]
```

**Примеры**:

```python
product_fields = ProductFields()
result = product_fields._set_multilang_value('name', 'Новый продукт', id_lang=2)
print(result)  # Вывод: True или False в зависимости от результата
```

### Дополнительные методы класса `ProductFields`

Класс `ProductFields` содержит большое количество property-сеттеров для различных полей товара. Каждый сеттер отвечает за установку значения соответствующего поля в объекте `self.presta_fields`.

#### Общая структура property-сеттеров

```python
    @property
    def some_field(self) -> Optional[type]:
        """ property `ps_table.some_field: field_type` """
        return self.presta_fields.some_field

    @some_field.setter
    def some_field(self, value: type = None):
        """ setter Описание назначения поля. """
        try:
            self.presta_fields.some_field = value
        except Exception as ex:
            logger.error(f"Ошибка при установке some_field:",ex)
```

- **Назначение**:
  - Getter возвращает текущее значение поля `some_field` из `self.presta_fields`.
  - Setter устанавливает новое значение для поля `some_field` в `self.presta_fields`.
- **Параметры**:
  - `value` (type, optional): Новое значение для поля. Тип зависит от поля. По умолчанию `None`.
- **Возвращает**:
  - Getter возвращает значение поля.
  - Setter ничего не возвращает.
- **Как работает**:
  - Getter просто возвращает текущее значение поля.
  - Setter пытается установить новое значение для поля и логирует ошибку, если происходит исключение.

#### Примеры

```python
product_fields = ProductFields()
product_fields.id_product = 123  # Установка ID продукта
print(product_fields.id_product)  # Вывод: 123

product_fields.name = "Example Product" # Установка имени продукта
print(product_fields.name) # Вывод: None (так как это мультиязычное поле, которое требует особого форматирования)
```

## EnumRedirect

```python
    class EnumRedirect(Enum):
        """Перечисление для типов редиректов."""
        ERROR_404 = '404'
        REDIRECT_301_PRODUCT = '301-product'
        REDIRECT_302_PRODUCT = '302-product'
        REDIRECT_301_CATEGORY = '301-category'
        REDIRECT_302_CATEGORY = '302-category'
```

**Описание**:
Перечисление `EnumRedirect` определяет возможные типы редиректов для продукта.

**Элементы перечисления**:
- `ERROR_404`: Указывает на ошибку 404 (страница не найдена).
- `REDIRECT_301_PRODUCT`: Указывает на постоянный редирект (301) на другой продукт.
- `REDIRECT_302_PRODUCT`: Указывает на временный редирект (302) на другой продукт.
- `REDIRECT_301_CATEGORY`: Указывает на постоянный редирект (301) на категорию.
- `REDIRECT_302_CATEGORY`: Указывает на временный редирект (302) на категорию.

## EnumCondition

```python
    class EnumCondition(Enum):
        """Перечисление для состояний товара."""
        NEW = 'new'
        USED = 'used'
        REFURBISHED = 'refurbished'
```

**Описание**:
Перечисление `EnumCondition` определяет возможные состояния товара.

**Элементы перечисления**:
- `NEW`: Указывает на новое состояние товара.
- `USED`: Указывает на бывшее в употреблении состояние товара.
- `REFURBISHED`: Указывает на восстановленное состояние товара.

## EnumVisibity

```python
    class EnumVisibity(Enum):
        """Перечисление для видимости товара."""
        BOTH = 'both'
        CATALOG = 'catalog'
        SEARCH = 'search'
        NONE = 'none'
```

**Описание**:
Перечисление `EnumVisibity` определяет возможные варианты видимости товара.

**Элементы перечисления**:
- `BOTH`: Указывает, что товар виден и в каталоге, и в поиске.
- `CATALOG`: Указывает, что товар виден только в каталоге.
- `SEARCH`: Указывает, что товар виден только в поиске.
- `NONE`: Указывает, что товар не виден ни в каталоге, ни в поиске.

## EnumProductType

```python
    class EnumProductType(Enum):
        """Перечисление для типов товаров."""
        STANDARD = 'standard'
        PACK = 'pack'
        VIRTUAL = 'virtual'
        COMBINATIONS = 'combinations'
        EMPTY = ''
```

**Описание**:
Перечисление `EnumProductType` определяет возможные типы товаров.

**Элементы перечисления**:
- `STANDARD`: Указывает на стандартный товар.
- `PACK`: Указывает на набор товаров (pack).
- `VIRTUAL`: Указывает на виртуальный товар.
- `COMBINATIONS`: Указывает на товар с комбинациями.
- `EMPTY`: Указывает на пустой тип товара.