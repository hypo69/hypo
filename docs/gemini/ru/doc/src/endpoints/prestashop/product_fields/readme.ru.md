# Документация по классу `ProductFields`

## Обзор

Класс `ProductFields` предназначен для управления и структурирования данных товаров в формате, требуемом API PrestaShop. Этот класс предоставляет комплексный интерфейс для работы с полями товаров, включая как одноязычные, так и многоязычные поля. Он гарантирует, что данные будут правильно отформатированы и проверены перед отправкой в API PrestaShop.

## Содержание

1.  [Введение](#введение)
2.  [Инициализация класса](#инициализация-класса)
    - [Метод `__init__`](#__init__)
    - [Метод `_load_product_fields_list`](#_load_product_fields_list)
    - [Метод `_payload`](#_payload)
3.  [Поля товара](#поля-товара)
    -   [Одноязычные поля](#одноязычные-поля)
        -   [Пример: `id_product`](#id_product)
    -   [Многоязычные поля](#многоязычные-поля)
        -   [Пример: `name`](#name)
4.  [Ассоциации](#ассоциации)
    -   [Пример: `associations`](#associations)
5.  [Значения по умолчанию](#значения-по-умолчанию)
6.  [Обработка ошибок](#обработка-ошибок)
    -   [Пример: Обработка ошибок в `id_product`](#пример-обработка-ошибок-в-id_product)
7.  [Примеры использования](#примеры-использования)
    -   [Пример 1: Установка одноязычного поля](#пример-1-установка-одноязычного-поля)
    -   [Пример 2: Установка многоязычного поля](#пример-2-установка-многоязычного-поля)
    -   [Пример 3: Установка ассоциаций](#пример-3-установка-ассоциаций)
8.  [Заключение](#заключение)

## Введение

Класс `ProductFields` — это Python-класс, который инкапсулирует структуру и поведение полей товаров в базе данных PrestaShop. Он разработан для упрощения процесса создания, обновления и управления данными товаров, предоставляя четкий и последовательный интерфейс для взаимодействия с полями товаров.

Класс особенно полезен для разработчиков, работающих с API PrestaShop, так как он гарантирует, что все обязательные поля будут правильно отформатированы и проверены перед отправкой в API.

## Инициализация класса

### Метод `__init__`

Метод `__init__` инициализирует класс `ProductFields`, загружая список полей товаров и настраивая значения по умолчанию для полей. Он также инициализирует объект `SimpleNamespace` для хранения полей товаров и вспомогательный словарь для дополнительных полей.

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

### Метод `_load_product_fields_list`

Этот метод загружает список полей товаров из текстового файла. Файл должен содержать одно имя поля на строку.

```python
def _load_product_fields_list(self) -> List[str]:
    return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)
```

**Возвращает:**

- `List[str]`: Список полей товара.

### Метод `_payload`

Этот метод загружает значения по умолчанию для полей товаров из JSON-файла. Если файл не найден или не может быть загружен, выводится сообщение об ошибке.

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

**Возвращает:**

- `bool`: `True`, если значения по умолчанию успешно загружены, `False` в противном случае.

## Поля товара

### Одноязычные поля

Одноязычные поля — это поля, которые не требуют перевода и хранятся на одном языке. Примеры включают `id_product`, `id_supplier`, `id_manufacturer` и т.д.

#### Пример: `id_product`

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

**Свойство `id_product`**

**Описание**:
- Свойство для получения и установки ID продукта.

**Параметры:**
- `value` (int, optional): ID продукта. По умолчанию `None`.

**Возвращает:**
- `Optional[int]`: ID продукта, либо `None` если значение не установлено.

**Вызывает исключения:**
- `ProductFieldException`: Если возникает ошибка при установке ID продукта.

### Многоязычные поля

Многоязычные поля — это поля, которые требуют перевода и хранятся на нескольких языках. Примеры включают `name`, `description`, `meta_title` и т.д.

#### Пример: `name`

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

**Свойство `name`**

**Описание:**
- Свойство для получения и установки имени продукта, поддерживающее многоязычность.

**Параметры:**
- `value` (str): Имя продукта.
- `lang` (str, optional): Язык, на котором задано имя продукта. По умолчанию `'en'`.

**Возвращает:**
- `dict`: Словарь, содержащий имя продукта на указанном языке.

**Вызывает исключения:**
- `ProductFieldException`: Если возникает ошибка при установке имени продукта.

## Ассоциации

Ассоциации используются для связывания товаров с другими сущностями, такими как категории, производители и поставщики. Свойство `associations` позволяет устанавливать и получать эти ассоциации.

#### Пример: `associations`

```python
@property
def associations(self) -> Optional[Dict]:
    return self.presta_fields.associations or None

@associations.setter
def associations(self, value: Dict[str, Optional[str]]):
    self.presta_fields.associations = value
```

**Свойство `associations`**

**Описание**:
- Свойство для получения и установки ассоциаций продукта.

**Параметры:**
- `value` (Dict[str, Optional[str]]): Словарь ассоциаций, где ключ - тип ассоциации (например, 'categories'), а значение - список ID связанных сущностей.

**Возвращает:**
- `Optional[Dict]`: Словарь ассоциаций, либо `None` если значение не установлено.

## Значения по умолчанию

Значения по умолчанию для полей товаров могут быть загружены из JSON-файла с помощью метода `_payload`. Этот метод гарантирует, что все поля имеют значение по умолчанию, которое можно переопределить по необходимости.

## Обработка ошибок

Класс включает надежную обработку ошибок для перехвата и регистрации любых исключений, возникающих при установке полей товаров. Это гарантирует, что любые проблемы будут зарегистрированы и могут быть устранены разработчиком.

#### Пример: Обработка ошибок в `id_product`

```python
@id_product.setter
def id_product(self, value: int = None):
    try:
        self.presta_fields.id_product = value
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: \'ID\' данными {value}\n        Ошибка: """, ex)
        return
```

## Примеры использования

### Пример 1: Установка одноязычного поля

```python
product = ProductFields()
product.id_product = 123
print(product.id_product)  # Вывод: 123
```

### Пример 2: Установка многоязычного поля

```python
product = ProductFields()
product.name = "Product Name", lang='en'
print(product.name)  # Вывод: {'language': [{'attrs': {'id': 1}, 'value': 'Product Name'}]}
```

### Пример 3: Установка ассоциаций

```python
product = ProductFields()
product.associations = {'categories': [{'id': 2}, {'id': 3}]}
print(product.associations)  # Вывод: {'categories': [{'id': 2}, {'id': 3}]}
```

## Заключение

Класс `ProductFields` — это мощный инструмент для управления данными товаров в API PrestaShop. Он предоставляет четкий и последовательный интерфейс для работы как с одноязычными, так и с многоязычными полями, гарантируя, что данные будут правильно отформатированы и проверены перед отправкой в API. Благодаря надежной обработке ошибок и поддержке значений по умолчанию, класс упрощает процесс работы с данными товаров в PrestaShop.