# ProductFields Class Documentation

## Обзор

Класс `ProductFields` предназначен для управления и структурирования данных о продуктах в формате, требуемом API PrestaShop. Этот класс предоставляет комплексный интерфейс для работы с полями продукта, включая поля как для одного, так и для нескольких языков. Он гарантирует, что данные правильно отформатированы и проверены перед отправкой в ​​API PrestaShop.

## Содержание

1.  [Введение](#введение)
2.  [Инициализация класса](#инициализация-класса)
3.  [Поля продукта](#поля-продукта)
    -   [Поля на одном языке](#поля-на-одном-языке)
    -   [Поля на нескольких языках](#поля-на-нескольких-языках)
4.  [Ассоциации](#ассоциации)
5.  [Значения по умолчанию](#значения-по-умолчанию)
6.  [Обработка ошибок](#обработка-ошибок)
7.  [Примеры использования](#примеры-использования)
8.  [Заключение](#заключение)

## Введение

Класс `ProductFields` — это класс Python, который инкапсулирует структуру и поведение полей продукта в базе данных PrestaShop. Он предназначен для упрощения процесса создания, обновления и управления данными о продуктах, предоставляя четкий и согласованный интерфейс для взаимодействия с полями продукта.

Класс особенно полезен для разработчиков, работающих с API PrestaShop, поскольку он гарантирует, что все необходимые поля правильно отформатированы и проверены перед отправкой в ​​API.

## Инициализация класса

### Метод `__init__`

Метод `__init__` инициализирует класс `ProductFields`, загружая список полей продукта и устанавливая значения по умолчанию для полей. Он также инициализирует объект `SimpleNamespace` для хранения полей продукта и вспомогательный словарь для дополнительных полей.

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

Этот метод загружает список полей продукта из текстового файла. Ожидается, что файл будет содержать одно имя поля в строке.

```python
def _load_product_fields_list(self) -> List[str]:
    return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)
```

### Метод `_payload`

Этот метод загружает значения по умолчанию для полей продукта из JSON-файла. Если файл не найден или не может быть загружен, регистрируется отладочное сообщение.

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

## Поля продукта

### Поля на одном языке

Поля на одном языке — это поля, которые не требуют перевода и хранятся на одном языке. Примеры включают `id_product`, `id_supplier`, `id_manufacturer` и т. д.

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

### Поля на нескольких языках

Поля на нескольких языках — это поля, которые требуют перевода и хранятся на нескольких языках. Примеры включают `name`, `description`, `meta_title` и т. д.

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

## Ассоциации

Ассоциации используются для связывания продуктов с другими сущностями, такими как категории, производители и поставщики. Свойство `associations` позволяет устанавливать и получать эти ассоциации.

#### Пример: `associations`

```python
@property
def associations(self) -> Optional[Dict]:
    return self.presta_fields.associations or None

@associations.setter
def associations(self, value: Dict[str, Optional[str]]):
    self.presta_fields.associations = value
```

## Значения по умолчанию

Значения по умолчанию для полей продукта можно загрузить из JSON-файла с помощью метода `_payload`. Этот метод гарантирует, что все поля имеют значение по умолчанию, которое можно переопределить при необходимости.

## Обработка ошибок

Класс включает надежную обработку ошибок для перехвата и регистрации любых исключений, которые возникают во время настройки полей продукта. Это гарантирует, что любые проблемы будут зарегистрированы и могут быть решены разработчиком.

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

## Примеры использования

### Пример 1: Установка поля на одном языке

```python
product = ProductFields()
product.id_product = 123
print(product.id_product)  # Вывод: 123
```

### Пример 2: Установка поля на нескольких языках

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

Класс `ProductFields` — мощный инструмент для управления данными о продуктах в API PrestaShop. Он предоставляет четкий и согласованный интерфейс для работы с полями как для одного, так и для нескольких языков, гарантируя, что данные правильно отформатированы и проверены перед отправкой в ​​API. Благодаря надежной обработке ошибок и поддержке значений по умолчанию, класс упрощает процесс работы с данными о продуктах в PrestaShop.