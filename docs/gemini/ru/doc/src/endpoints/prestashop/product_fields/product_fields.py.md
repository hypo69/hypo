# Модуль product_fields.py

## Обзор

Модуль `product_fields.py` предназначен для описания и управления полями товаров в формате, необходимом для API PrestaShop. Он включает в себя классы и методы для определения структуры данных, загрузки значений по умолчанию, установки мультиязычных значений и преобразования данных в формат, пригодный для отправки в API PrestaShop.

## Подробнее

Этот модуль предоставляет класс `ProductFields`, который содержит определения полей товара, используемых в таблицах PrestaShop. Он также включает методы для работы с этими полями, такие как установка значений, получение значений и преобразование объекта в словарь, готовый для отправки в API PrestaShop.
Модуль расположен в структуре проекта по следующему пути: `hypotez/src/endpoints/prestashop/product_fields/product_fields.py`. Это указывает на то, что он является частью подсистемы, отвечающей за взаимодействие с PrestaShop, а именно за определение структуры и формата данных о товарах.

## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` предназначен для представления полей товара в формате, совместимом с API PrestaShop. Он позволяет задавать и получать значения различных полей товара, а также преобразовывать объект в словарь для отправки в API PrestaShop.

**Методы**:

- `__post_init__`: Метод, вызываемый после инициализации объекта.
- `_payload`: Загружает значения полей по умолчанию.
- `_set_multilang_value`: Устанавливает мультиязычное значение для заданного поля.
- Свойства для доступа к полям таблицы `ps_product` (например, `id_product`, `id_supplier`, `price` и т.д.).
- Свойства для доступа к полям таблицы `ps_product_lang` (например, `name`, `description`, `link_rewrite` и т.д.).
- Методы для управления связями товара с другими сущностями (категориями, изображениями, комбинациями и т.д.).
- `to_dict`: Преобразует объект `ProductFields` в словарь, готовый для отправки в API PrestaShop.
- `_format_multilang_value`: Форматирует мультиязычные значения в список словарей для PrestaShop API.

**Параметры**:

- `presta_fields` (SimpleNamespace): Объект, хранящий значения полей товара.
- `id_lang` (int): ID языка. По умолчанию равен 1.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from types import SimpleNamespace

# Создание экземпляра класса ProductFields
product_fields = ProductFields()

# Установка значений полей
product_fields.id_product = 123
product_fields.name = 'Пример товара'
product_fields.price = 99.99

# Преобразование объекта в словарь
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

**Описание**: Загружает значения по умолчанию для полей товара из файлов `fields_list.txt` и `product_fields_default_values.json`.

**Параметры**: Нет

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках чтения файлов или преобразования данных.

**Примеры**:
```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields

product_fields = ProductFields()
result = product_fields._payload()
print(result)  # Вывод: True или False в зависимости от результата загрузки
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

    Описание:
        Функция устанавливает мультиязычное значение для указанного поля объекта.  
        Поле может хранить значения для разных языков.  Значения хранятся в виде списка словарей,
        где каждый словарь представляет собой значение для определенного языка и имеет структуру:

        {'attrs': {'id': 'language_id'}, 'value': 'language_value'}

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

**Описание**: Устанавливает мультиязычное значение для указанного поля объекта `ProductFields`.

**Параметры**:

- `field_name` (str): Имя поля, для которого устанавливается значение.
- `value` (str): Значение, которое необходимо установить.
- `id_lang` (Optional[Union[int, str]]): ID языка. Если не указан, используется `self.id_lang`.

**Возвращает**:

- `bool`: `True`, если значение успешно установлено, `False` в случае ошибки.

**Вызывает исключения**:

- `Exception`: Возникает при попытке установить значение в мультиязычное поле.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields

product_fields = ProductFields()
product_fields.id_lang = 2  # Установка языка
result = product_fields._set_multilang_value('name', 'Новое название', id_lang=2)
print(result) # Вывод: True или False в зависимости от результата установки
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

**Описание**: Преобразует объект `ProductFields` в словарь, пригодный для отправки в API PrestaShop.

**Параметры**: Нет

**Возвращает**:
- `Dict[str, Any]`: Словарь с полями, готовый для PrestaShop API.

**Вызывает исключения**: Нет

**Примеры**:
```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields

product_fields = ProductFields()
product_fields.name = "Товар 1"
product_dict = product_fields.to_dict()
print(product_dict)
```

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

**Описание**: Форматирует мультиязычные значения в список словарей для PrestaShop API.

**Параметры**:
- `data` (Any): Значение поля. Если это словарь, ожидается структура `{'language': [{'attrs': {'id': lang_id}, 'value': value}]}`

**Возвращает**:
- `List[Dict[str, str]]`: Список словарей, где каждый словарь содержит `'id'` и `'value'` (все как строки) для каждого языка.

**Вызывает исключения**: Нет

**Примеры**:
```python
from src.endpoints.prestashop.product_fields.product_fields import ProductFields

product_fields = ProductFields()
data = {'language': [{'attrs': {'id': '1'}, 'value': 'test'}]}
formatted_data = product_fields._format_multilang_value(data)
print(formatted_data)