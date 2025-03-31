# Модуль product_fields.py

## Обзор

Модуль `product_fields.py` предназначен для описания полей товара, используемых в таблицах PrestaShop. Он содержит класс `ProductFields`, который предоставляет структуру данных для представления и управления информацией о товарах, включая мультиязычные значения и связи с другими сущностями PrestaShop, такими как категории, изображения и характеристики.

## Подробней

Этот модуль играет важную роль в процессе интеграции данных о товарах в PrestaShop, обеспечивая стандартизированный способ представления информации, который соответствует требованиям API PrestaShop. Модуль содержит функциональность для загрузки значений полей по умолчанию, установки мультиязычных значений и преобразования объекта в формат, пригодный для отправки в API PrestaShop.

## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` предназначен для представления полей товара в формате, совместимом с API PrestaShop. Он позволяет удобно управлять данными о товаре, включая основные атрибуты, мультиязычные описания и связи с другими сущностями PrestaShop.

**Как работает класс**:

1.  **Инициализация**: При создании экземпляра класса происходит загрузка значений полей товара по умолчанию.
2.  **Управление полями**: Класс предоставляет свойства (properties) для доступа и изменения значений отдельных полей товара. Для мультиязычных полей предусмотрен специальный метод `_set_multilang_value`, который обеспечивает правильное форматирование данных для разных языков.
3.  **Преобразование в словарь**: Метод `to_dict` преобразует объект `ProductFields` в словарь, готовый для отправки в API PrestaShop. При этом исключаются поля с пустыми значениями и формируются мультиязычные поля в требуемом формате.
4. **Поддержка связей**: Реализована поддержка связей с другими сущностями PrestaShop (категории, изображения, характеристики и т.д.) через механизм `associations`.

**Методы**:

*   `__post_init__`: Вызывается после инициализации объекта. Запускает процесс загрузки значений полей.
*   `_payload`: Загружает значения полей товара по умолчанию из файлов `fields_list.txt` и `product_fields_default_values.json`.
*   `_set_multilang_value`: Устанавливает мультиязычное значение для заданного поля.
*   `to_dict`: Преобразует объект `ProductFields` в словарь для PrestaShop API.
*   `_format_multilang_value`: Форматирует мультиязычные значения в список словарей для PrestaShop API.
*    `_ensure_associations`: Убеждается, что структура associations существует в presta_fields.
*   `additional_category_append`: Добавляет связь с категорией, если ее еще нет.
*   `additional_categories_clear`: Очищает все связи с категориями.
*    `product_image_append`: Добавляет связь с изображением.
*   `product_images_clear`: Очищает все связи с изображениями.
*    `images_urls_append`: Устанавливает список URL, откуда скачать дополнительные изображения.
*    `product_combination_append`: Добавляет связь с комбинацией.
*   `product_combinations_clear`: Очищает все связи с комбинациями.
*    `product_options_append`: Добавляет связь со значением опции продукта.
*   `product_options_clear`: Очищает все связи со значениями опций продукта.
*   `product_features_append`: Добавляет связь с характеристикой продукта.
*   `product_features_clear`: Очищает все связи с характеристиками продукта.
*    `product_tag_append`: Добавляет связь с тегом.
*   `product_tags_clear`: Очищает все связи с тегами.
*   `product_stock_available_append`: Добавляет связь с доступностью на складе.
*   `product_stock_availables_clear`: Очищает все связи с доступностью на складе.
*   `product_attachment_append`: Добавляет связь с вложением.
*   `product_attachments_clear`: Очищает все связи с вложениями.
*   `product_accessory_append`: Добавляет связь с аксессуаром.
*   `product_accessories_clear`: Очищает все связи с аксессуарами.
*   `product_bundle_append`: Добавляет связь с бандлом продукта.
*   `product_bundle_clear`: Очищает все связи с бандлами продуктов.

**Параметры**:

*   `presta_fields` (SimpleNamespace): Объект, хранящий поля товара. Инициализируется в методе `__post_init__`.
*   `id_lang` (int): ID языка, используемый по умолчанию для мультиязычных полей.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields

# Создание экземпляра класса
product_fields = ProductFields()

# Установка значения поля
product_fields.name = 'Новый товар'

# Установка мультиязычного значения
product_fields._set_multilang_value('description', 'Описание товара на русском', id_lang=3)

# Преобразование в словарь
product_dict = product_fields.to_dict()
print(product_dict)
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

**Назначение**: Загружает значения полей товара по умолчанию из файлов `fields_list.txt` и `product_fields_default_values.json`.

**Как работает функция**:

1.  Определяет базовый путь к файлам конфигурации.
2.  Считывает список полей из файла `fields_list.txt`.
3.  Инициализирует атрибут `presta_fields` объектом `SimpleNamespace` с ключами из списка полей и значениями `None`.
4.  Загружает словарь с значениями по умолчанию из файла `product_fields_default_values.json`.
5.  Устанавливает значения по умолчанию для соответствующих полей в атрибуте `presta_fields`.

**Параметры**:

*   Нет

**Возвращает**:

*   `bool`: `True`, если загрузка прошла успешно, `False` в случае ошибки.

**Вызывает исключения**:

*   `Exception`: В случае ошибки при чтении файлов или конвертации данных.

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

**Назначение**: Устанавливает мультиязычное значение для указанного поля объекта `ProductFields`.

**Как работает функция**:

1.  Принимает имя поля (`field_name`), значение (`value`) и опциональный ID языка (`id_lang`).
2.  Формирует структуру данных для представления значения на определенном языке.
3.  Проверяет, существует ли поле с указанным именем в `self.presta_fields`.
4.  Если поле не существует, создает его и устанавливает значение для указанного языка.
5.  Если поле существует, но не имеет ожидаемой структуры, перезаписывает поле с новым значением для указанного языка.
6.  Если поле существует и имеет правильную структуру, обновляет значение для указанного языка или добавляет новую запись, если язык не найден.

**Параметры**:

*   `field_name` (str): Имя поля, для которого устанавливается значение.
*   `value` (str): Значение поля.
*   `id_lang` (Optional[int  |  str], optional): ID языка. Если не указан, используется `self.id_lang`. По умолчанию `None`.

**Возвращает**:

*   `bool`: `True`, если значение успешно установлено, `False` в случае ошибки.

**Вызывает исключения**:

*   `Exception`: В случае ошибки при установке значения.

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

**Назначение**: Преобразует объект `ProductFields` в словарь, пригодный для отправки в API PrestaShop.

**Как работает функция**:

1.  Создает пустой словарь `product_dict`.
2.  Итерируется по всем атрибутам объекта `ProductFields`.
3.  Для каждого атрибута проверяет его значение на `None` или пустую строку.
4.  Если значение не пустое, добавляет его в словарь `product_dict`, преобразуя в строку.
5.  Для мультиязычных полей использует метод `_format_multilang_value` для форматирования данных.
6.  Возвращает словарь `product_dict`.

**Параметры**:

*   Нет

**Возвращает**:

*   `Dict[str, Any]`: Словарь с полями, готовый для PrestaShop API.

### `_format_multilang_value`

```python
def _format_multilang_value(self, data: Any) -> List[Dict[str, str]]:
    """
    Форматирует мультиязычные значения в список словарей для PrestaShop API. Все значения представляются как строки.

    Args:
        data (Any): Значение поля. Если это словарь, ожидается структура {'language': [{'attrs': {'id': lang_id}, 'value': value}]}

    Returns:
        List[Dict[str, str]]: Список словарей, где каждый словарь содержит 'id' и 'value' (все как строки) для каждого языка.
    """
    ...
```

**Назначение**: Форматирует мультиязычные значения в список словарей для PrestaShop API.

**Как работает функция**:

1.  Принимает значение поля `data`.
2.  Проверяет, является ли `data` словарем и содержит ли ключ `'language'`.
3.  Если да, то итерируется по списку языков в `data['language']`.
4.  Для каждого языка создает словарь с ключами `'id'` и `'value'`, преобразуя значения в строки.
5.  Добавляет словарь в результирующий список.
6.  Если `data` не соответствует ожидаемой структуре, создает список с одним элементом для текущего языка.
7.  Возвращает результирующий список.

**Параметры**:

*   `data` (Any): Значение поля. Если это словарь, ожидается структура `{'language': [{'attrs': {'id': lang_id}, 'value': value}]}`

**Возвращает**:

*   `List[Dict[str, str]]`: Список словарей, где каждый словарь содержит `'id'` и `'value'` (все как строки) для каждого языка.

### `additional_category_append`

```python
def additional_category_append(self, category_id: int | str):
    """Добавляет связь с категорией, если ее еще нет."""
    ...
```

**Назначение**: Добавляет связь с категорией, если ее еще нет.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Преобразует `category_id` в целое число. Если преобразование не удалось, логирует ошибку и завершает работу.
3.  Проверяет, существует ли ключ `'categories'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['categories']`.
4.  Преобразует `category_id` в строку.
5.  Проверяет, существует ли уже категория с таким `id` в списке `self.presta_fields.associations['categories']`.
6.  Если категория не найдена, добавляет новую запись в список `self.presta_fields.associations['categories']` с `id`, равным строковому представлению `category_id`.

**Параметры**:

*   `category_id` (int | str): ID категории для добавления.

### `additional_categories_clear`

```python
def additional_categories_clear(self):
    """Очищает все связи с категориями."""
    ...
```

**Назначение**: Очищает все связи с категориями.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'categories'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'categories'` из `self.presta_fields.associations`.

### `product_image_append`

```python
def product_image_append(self, image_id: int):
    """Добавляет связь с изображением."""
    ...
```

**Назначение**: Добавляет связь с изображением.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'images'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['images']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['images']` с `id`, равным строковому представлению `image_id`.

**Параметры**:

*   `image_id` (int): ID изображения для добавления.

### `product_images_clear`

```python
def product_images_clear(self):
    """Очищает все связи с изображениями."""
    ...
```

**Назначение**: Очищает все связи с изображениями.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'images'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'images'` из `self.presta_fields.associations`.

### `images_urls_append`

```python
def images_urls_append(self, value: List[str] = None):
    """Устанавливает список URL, откуда скачать дополнительные изображения."""
    ...
```

**Назначение**: Устанавливает список URL, откуда скачивать дополнительные изображения.

**Как работает функция**:

1.  Проверяет, передан ли список URL (`value`). Если `value` равен `None`, завершает работу.
2.  Проверяет, является ли `value` списком. Если нет, логирует предупреждение и завершает работу.
3.  Фильтрует список `value`, оставляя только валидные URL (строки, не являющиеся пустыми).
4.  Проверяет, существует ли ключ `'images_urls'` в `self.assist_fields_dict`. Если нет, создает пустой список `self.presta_fields.images_urls`.
5.  Добавляет каждый валидный URL в список `self.presta_fields.images_urls`, предварительно проверив его на уникальность.

**Параметры**:

*   `value` (List[str], optional): Список URL изображений. По умолчанию `None`.

### `product_combinations_clear`

```python
def product_combinations_clear(self):
    """Очищает все связи с комбинациями."""
    ...
```

**Назначение**: Очищает все связи с комбинациями.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'combinations'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'combinations'` из `self.presta_fields.associations`.

### `product_combination_append`

```python
def product_combination_append(self, combination_id: int):
    """Добавляет связь с комбинацией."""
    ...
```

**Назначение**: Добавляет связь с комбинацией.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'combinations'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['combinations']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['combinations']` с `id`, равным строковому представлению `combination_id`.

**Параметры**:

*   `combination_id` (int): ID комбинации для добавления.

### `product_options_append`

```python
def product_options_append(self, product_option_value_id: int):
    """Добавляет связь со значением опции продукта."""
    ...
```

**Назначение**: Добавляет связь со значением опции продукта.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'product_option_values'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['product_option_values']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['product_option_values']` с `id`, равным строковому представлению `product_option_value_id`.

**Параметры**:

*   `product_option_value_id` (int): ID значения опции продукта для добавления.

### `product_options_clear`

```python
def product_options_clear(self):
    """Очищает все связи со значениями опций продукта."""
    ...
```

**Назначение**: Очищает все связи со значениями опций продукта.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'product_option_values'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'product_option_values'` из `self.presta_fields.associations`.

### `product_features_append`

```python
 def product_features_append(self, feature_id: int, feature_value_id: int):
        """Добавляет связь с характеристикой продукта."""
        self._ensure_associations()
        if \'product_features\' not in self.presta_fields.associations:
            self.presta_fields.associations[\'product_features\'] = []
        self.presta_fields.associations[\'product_features\'].append(
            {\'id\': str(feature_id), \'id_feature_value\': str(feature_value_id)}\n        )
```

**Назначение**: Добавляет связь с характеристикой продукта.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'product_features'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['product_features']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['product_features']` с `id`, равным строковому представлению `feature_id`, и `id_feature_value`, равным строковому представлению `feature_value_id`.

**Параметры**:

*   `feature_id` (int): ID характеристики продукта для добавления.
*   `feature_value_id` (int): ID значения характеристики продукта для добавления.

### `product_features_clear`

```python
def product_features_clear(self):
    """Очищает все связи с характеристиками продукта."""
    ...
```

**Назначение**: Очищает все связи с характеристиками продукта.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'product_features'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'product_features'` из `self.presta_fields.associations`.

### `product_tag_append`

```python
def product_tag_append(self, tag_id: int):
    """Добавляет связь с тегом."""
    ...
```

**Назначение**: Добавляет связь с тегом.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'tags'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['tags']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['tags']` с `id`, равным строковому представлению `tag_id`.

**Параметры**:

*   `tag_id` (int): ID тега для добавления.

### `product_tags_clear`

```python
def product_tags_clear(self):
    """Очищает все связи с тегами."""
    ...
```

**Назначение**: Очищает все связи с тегами.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'tags'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'tags'` из `self.presta_fields.associations`.

### `product_stock_available_append`

```python
def product_stock_available_append(self, stock_available_id: int, product_attribute_id: int):
    """Добавляет связь с доступностью на складе."""
    ...
```

**Назначение**: Добавляет связь с доступностью на складе.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'stock_availables'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['stock_availables']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['stock_availables']` с `id`, равным строковому представлению `stock_available_id`, и `id_product_attribute`, равным строковому представлению `product_attribute_id`.

**Параметры**:

*   `stock_available_id` (int): ID доступности на складе для добавления.
*   `product_attribute_id` (int): ID атрибута продукта для добавления.

### `product_stock_availables_clear`

```python
def product_stock_availables_clear(self):
    """Очищает все связи с доступностью на складе."""
    ...
```

**Назначение**: Очищает все связи с доступностью на складе.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'stock_availables'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'stock_availables'` из `self.presta_fields.associations`.

### `product_attachment_append`

```python
def product_attachment_append(self, attachment_id: int):
    """Добавляет связь с вложением."""
    ...
```

**Назначение**: Добавляет связь с вложением.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'attachments'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['attachments']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['attachments']` с `id`, равным строковому представлению `attachment_id`.

**Параметры**:

*   `attachment_id` (int): ID вложения для добавления.

### `product_attachments_clear`

```python
def product_attachments_clear(self):
    """Очищает все связи с вложениями."""
    ...
```

**Назначение**: Очищает все связи с вложениями.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'attachments'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'attachments'` из `self.presta_fields.associations`.

### `product_accessory_append`

```python
def product_accessory_append(self, accessory_id: int):
    """Добавляет связь с аксессуаром."""
    ...
```

**Назначение**: Добавляет связь с аксессуаром.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'accessories'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['accessories']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['accessories']` с `id`, равным строковому представлению `accessory_id`.

**Параметры**:

*   `accessory_id` (int): ID аксессуара для добавления.

### `product_accessories_clear`

```python
def product_accessories_clear(self):
    """Очищает все связи с аксессуарами."""
    ...
```

**Назначение**: Очищает все связи с аксессуарами.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'accessories'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'accessories'` из `self.presta_fields.associations`.

### `product_bundle_append`

```python
def product_bundle_append(self, bundle_id: int, product_attribute_id: int, quantity: int):
    """Добавляет связь с бандлом продукта."""
    ...
```

**Назначение**: Добавляет связь с бандлом продукта.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'product_bundle'` в `self.presta_fields.associations`. Если нет, создает пустой список `self.presta_fields.associations['product_bundle']`.
3.  Добавляет новую запись в список `self.presta_fields.associations['product_bundle']` с `id`, равным строковому представлению `bundle_id`, `id_product_attribute`, равным строковому представлению `product_attribute_id`, и `quantity`, равным строковому представлению `quantity`.

**Параметры**:

*   `bundle_id` (int): ID бандла продукта для добавления.
*   `product_attribute_id` (int): ID атрибута продукта для добавления.
*   `quantity` (int): Количество продуктов в бандле.

### `product_bundle_clear`

```python
def product_bundle_clear(self):
    """Очищает все связи с бандлами продуктов."""
    ...
```

**Назначение**: Очищает все связи с бандлами продуктов.

**Как работает функция**:

1.  Вызывает `_ensure_associations()` для гарантии существования структуры `associations` в `presta_fields`.
2.  Проверяет, существует ли ключ `'product_bundle'` в `self.presta_fields.associations`.
3.  Если да, удаляет ключ `'product_bundle'` из `self.presta_fields.associations`.