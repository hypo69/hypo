# Документация по классу `ProductFields`

## Обзор

Класс `ProductFields` предназначен для управления и структурирования данных товаров в формате, требуемом API PrestaShop. Этот класс предоставляет комплексный интерфейс для работы с полями товаров, включая как одноязычные, так и многоязычные поля. Он гарантирует, что данные будут правильно отформатированы и проверены перед отправкой в API PrestaShop.

## Содержание

1. [Введение](#введение)
2. [Инициализация класса](#инициализация-класса)
3. [Поля товара](#поля-товара)
   - [Одноязычные поля](#одноязычные-поля)
   - [Многоязычные поля](#многоязычные-поля)
4. [Ассоциации](#ассоциации)
5. [Значения по умолчанию](#значения-по-умолчанию)
6. [Обработка ошибок](#обработка-ошибок)
7. [Примеры использования](#примеры-использования)
8. [Заключение](#заключение)

## Введение

Класс `ProductFields` — это Python-класс, который инкапсулирует структуру и поведение полей товаров в базе данных PrestaShop. Он разработан для упрощения процесса создания, обновления и управления данными товаров, предоставляя четкий и последовательный интерфейс для взаимодействия с полями товаров.

Класс особенно полезен для разработчиков, работающих с API PrestaShop, так как он гарантирует, что все обязательные поля будут правильно отформатированы и проверены перед отправкой в API.

## Инициализация класса

### Метод `__init__`

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

**Описание**: Метод `__init__` инициализирует класс `ProductFields`, загружая список полей товаров и настраивая значения по умолчанию для полей. Он также инициализирует объект `SimpleNamespace` для хранения полей товаров и вспомогательный словарь для дополнительных полей.

**Параметры**:
- Отсутствуют

**Возвращает**:
- Отсутствует

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
product = ProductFields()
print(product.language)
```

### Метод `_load_product_fields_list`

```python
def _load_product_fields_list(self) -> List[str]:
    return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)
```

**Описание**: Этот метод загружает список полей товаров из текстового файла. Файл должен содержать одно имя поля на строку.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `List[str]`: Список полей товаров.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
product = ProductFields()
fields = product._load_product_fields_list()
print(fields[:5])
```

### Метод `_payload`

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

**Описание**: Этот метод загружает значения по умолчанию для полей товаров из JSON-файла. Если файл не найден или не может быть загружен, выводится сообщение об ошибке.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
product = ProductFields()
result = product._payload()
print(result)
```

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
        logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}
        Ошибка: """, ex)
        return
```

**Описание**: Свойство `id_product` позволяет получить или установить идентификатор товара.

**Параметры**:
- `value` (int, optional): Идентификатор товара. По умолчанию `None`.

**Возвращает**:
- `Optional[int]`: Идентификатор товара или `None`, если значение не установлено.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения.

**Примеры**:

```python
product = ProductFields()
product.id_product = 123
print(product.id_product)
```

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
        logger.error(f"""Ошибка заполнения поля: 'name' данными {value}
        Ошибка: """, ex)
        return
```

**Описание**: Свойство `name` позволяет получить или установить имя товара на определенном языке.

**Параметры**:
- `value` (str): Имя товара.
- `lang` (str, optional): Язык, на котором устанавливается имя товара. По умолчанию `'en'`.

**Возвращает**:
- `bool`: `True`, если установка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения.

**Примеры**:

```python
product = ProductFields()
product.name = "Product Name", lang='en'
print(product.name)
```

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

**Описание**: Свойство `associations` позволяет получить или установить ассоциации товара с другими сущностями.

**Параметры**:
- `value` (Dict[str, Optional[str]]): Словарь ассоциаций.

**Возвращает**:
- `Optional[Dict]`: Словарь ассоциаций или `None`, если значение не установлено.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
product = ProductFields()
product.associations = {'categories': [{'id': 2}, {'id': 3}]}
print(product.associations)
```

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
        logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}
        Ошибка: """, ex)
        return
```

**Описание**: В блоке `try...except` происходит попытка установить значение поля `id_product`. Если во время этой операции возникает исключение `ProductFieldException`, оно перехватывается, и в лог записывается сообщение об ошибке.

**Параметры**:
- `value` (int, optional): Идентификатор товара. По умолчанию `None`.

**Возвращает**:
- Отсутствует

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения.

**Примеры**:

```python
product = ProductFields()
try:
    product.id_product = "abc"  # Попытка установить некорректное значение
except Exception as e:
    print(f"Произошла ошибка: {e}")
```

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

## Заключение

Класс `ProductFields` — это мощный инструмент для управления данными товаров в API PrestaShop. Он предоставляет четкий и последовательный интерфейс для работы как с одноязычными, так и с многоязычными полями, гарантируя, что данные будут правильно отформатированы и проверены перед отправкой в API. Благодаря надежной обработке ошибок и поддержке значений по умолчанию, класс упрощает процесс работы с данными товаров в PrestaShop.