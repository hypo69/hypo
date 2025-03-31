# Документация по классу `ProductFields`

## Обзор

Класс `ProductFields` предназначен для управления и структурирования данных товаров в формате, требуемом API PrestaShop. Этот класс предоставляет комплексный интерфейс для работы с полями товаров, включая как одноязычные, так и многоязычные поля. Он гарантирует, что данные будут правильно отформатированы и проверены перед отправкой в API PrestaShop.

## Подробнее

Этот класс упрощает процесс создания, обновления и управления данными товаров, предоставляя четкий и последовательный интерфейс для взаимодействия с полями товаров. Он особенно полезен для разработчиков, работающих с API PrestaShop, так как гарантирует, что все обязательные поля будут правильно отформатированы и проверены перед отправкой в API.
<инструкция для модели gemini:Класс `ProductFields` используется для представления и управления полями товаров в системе PrestaShop. Он предоставляет удобный интерфейс для работы с данными товаров, обеспечивая их соответствие требованиям API PrestaShop. Класс позволяет устанавливать и получать значения полей товаров, а также обрабатывать ошибки и устанавливать значения по умолчанию. Это упрощает интеграцию с API PrestaShop и обеспечивает консистентность данных.>

## Содержание

1. [Инициализация класса](#инициализация-класса)
2. [Поля товара](#поля-товара)
   - [Одноязычные поля](#одноязычные-поля)
   - [Многоязычные поля](#многоязычные-поля)
3. [Ассоциации](#ассоциации)

## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` инкапсулирует структуру и поведение полей товаров в базе данных PrestaShop.

**Как работает класс**:
Класс `ProductFields` предоставляет интерфейс для работы с полями товаров, позволяя устанавливать значения для одноязычных и многоязычных полей, а также управлять ассоциациями товаров. Класс загружает список полей товаров из файла, устанавливает значения по умолчанию и обеспечивает обработку ошибок при работе с данными.

#### Метод `__init__`

```python
def __init__(self):
    self.product_fields_list = self._load_product_fields_list()
    self.language = {'en': 1, 'he': 2, 'ru': 3}
    self.presta_fields = SimpleNamespace(**{key: None for key in self.product_fields_list})
    self.assist_fields_dict = {
        'default_image_url': '', 
        'images_urls': []
    }
    self._payload()
```

**Описание**: Инициализирует класс `ProductFields`, загружая список полей товаров и настраивая значения по умолчанию для полей.

**Как работает метод**:
- `self.product_fields_list = self._load_product_fields_list()`: Загружает список полей товаров, используя метод `_load_product_fields_list`.
- `self.language = {'en': 1, 'he': 2, 'ru': 3}`: Инициализирует словарь `language`, который содержит соответствия между кодами языков и их идентификаторами.
- `self.presta_fields = SimpleNamespace(**{key: None for key in self.product_fields_list})`: Создает объект `SimpleNamespace` с атрибутами, соответствующими полям товаров, и устанавливает их значения в `None`.
- `self.assist_fields_dict = {'default_image_url': '', 'images_urls': []}`: Инициализирует словарь `assist_fields_dict` для хранения дополнительных полей товаров, таких как URL изображений.
- `self._payload()`: Загружает значения по умолчанию для полей товаров, используя метод `_payload`.

#### Метод `_load_product_fields_list`

```python
def _load_product_fields_list(self) -> List[str]:
    return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)
```

**Описание**: Загружает список полей товаров из текстового файла.

**Как работает метод**:
Метод считывает содержимое файла `fields_list.txt`, расположенного в директории `src/product/product_fields`, и возвращает список строк, где каждая строка представляет собой имя поля товара.

**Возвращает**:
- `List[str]`: Список полей товаров.

#### Метод `_payload`

```python
def _payload(self) -> bool:
    data = j_loads(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json'))
    if not data:
        logger.debug(f"Ошибка загрузки полей из файла {gs.path.src}/product/product_fields/product_fields_default_values.json")
        return False
    for name, value in data.items():
        setattr(self, name, value)
    return True
```

**Описание**: Загружает значения по умолчанию для полей товаров из JSON-файла.

**Как работает метод**:
- `data = j_loads(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json'))`: Пытается загрузить данные из файла `product_fields_default_values.json`.
- `if not data`: Проверяет, удалось ли загрузить данные. Если не удалось, записывает сообщение об ошибке в лог и возвращает `False`.
- `for name, value in data.items()`: Перебирает все пары ключ-значение в загруженных данных.
- `setattr(self, name, value)`: Устанавливает значение атрибута класса с именем `name` равным `value`.
- Возвращает `True`, если загрузка и установка значений прошли успешно.

**Возвращает**:
- `bool`: `True`, если значения по умолчанию успешно загружены и установлены, `False` в случае ошибки.

#### Свойство `id_product`

```python
@property
def id_product(self) -> Optional[int]:
    return self.presta_fields.id_product

@id_product.setter
def id_product(self, value: int = None):
    try:
        self.presta_fields.id_product = value
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: \'ID\' данными {value}\n        Ошибка: """, ex)
        return
```

**Описание**: Позволяет получить и установить значение поля `id_product`.

**Как работает**:
- `@property def id_product(self) -> Optional[int]`: Геттер возвращает текущее значение `id_product` из `self.presta_fields`.
- `@id_product.setter def id_product(self, value: int = None)`: Сеттер устанавливает значение `id_product` в `self.presta_fields`. Если возникает исключение `ProductFieldException`, оно логируется, и функция завершается.

**Параметры**:
- `value` (int, optional): Значение для установки поля `id_product`. По умолчанию `None`.

**Возвращает**:
- `Optional[int]`: Текущее значение `id_product`.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения поля.

#### Свойство `name`

```python
@property
def name(self):
    return self.presta_fields.name or ''

@name.setter
def name(self, value: str, lang:str = 'en') -> bool:
    try:
        self.presta_fields.name: dict = {'language':
                                                    [
                                                        {'attrs':{'id':self.language[lang]}, 'value': value},
                                                    ]
                                                 }
        return True
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: \'name\' данными {value}\n        Ошибка: """, ex)
        return
```

**Описание**: Позволяет получить и установить значение многоязычного поля `name`.

**Как работает**:
- `@property def name(self)`: Геттер возвращает текущее значение `name` из `self.presta_fields` или пустую строку, если значение отсутствует.
- `@name.setter def name(self, value: str, lang:str = 'en') -> bool`: Сеттер устанавливает значение `name` в `self.presta_fields` для указанного языка `lang`. Если возникает исключение `ProductFieldException`, оно логируется, и функция завершается.

**Параметры**:
- `value` (str): Значение для установки поля `name`.
- `lang` (str, optional): Код языка для установки значения. По умолчанию `'en'`.

**Возвращает**:
- `bool`: `True`, если значение успешно установлено.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения поля.

#### Свойство `associations`

```python
@property
def associations(self) -> Optional[Dict]:
    return self.presta_fields.associations or None

@associations.setter
def associations(self, value: Dict[str, Optional[str]]):
    self.presta_fields.associations = value
```

**Описание**: Позволяет получить и установить ассоциации товара с другими сущностями.

**Как работает**:
- `@property def associations(self) -> Optional[Dict]`: Геттер возвращает текущие ассоциации товара из `self.presta_fields` или `None`, если ассоциации отсутствуют.
- `@associations.setter def associations(self, value: Dict[str, Optional[str]])`: Сеттер устанавливает ассоциации товара в `self.presta_fields`.

**Параметры**:
- `value` (Dict[str, Optional[str]]): Словарь ассоциаций для установки.

**Возвращает**:
- `Optional[Dict]`: Текущие ассоциации товара.

## Примеры использования

### Пример 1: Установка одноязычного поля

```python
product = ProductFields()
product.id_product = 123
print(product.id_product)
```

### Пример 2: Установка многоязычного поля

```python
product = ProductFields()
product.name = "Product Name", lang='en'
print(product.name)
```

### Пример 3: Установка ассоциаций

```python
product = ProductFields()
product.associations = {'categories': [{'id': 2}, {'id': 3}]}
print(product.associations)
```