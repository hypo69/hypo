# ProductFields Класс Документация

## Обзор

Класс `ProductFields` предназначен для управления и структурирования данных о продукте в формате, требуемом PrestaShop API. Этот класс предоставляет всесторонний интерфейс для обработки полей продукта, включая поля как с одним языком, так и с несколькими языками. Он гарантирует, что данные правильно отформатированы и проверены, прежде чем будут отправлены в PrestaShop API.

## Содержание

1.  [Введение](#введение)
2.  [Инициализация Класса](#инициализация-класса)
3.  [Поля Продукта](#поля-продукта)
    -   [Поля с Одним Языком](#поля-с-одним-языком)
    -   [Поля с Несколькими Языками](#поля-с-несколькими-языками)
4.  [Ассоциации](#ассоциации)
5.  [Значения по Умолчанию](#значения-по-умолчанию)
6.  [Обработка Ошибок](#обработка-ошибок)
7.  [Примеры Использования](#примеры-использования)
8.  [Заключение](#заключение)

## Введение

Класс `ProductFields` - это класс Python, который инкапсулирует структуру и поведение полей продукта в базе данных PrestaShop. Он разработан, чтобы упростить процесс создания, обновления и управления данными продукта, предоставляя четкий и последовательный интерфейс для взаимодействия с полями продукта.

Класс особенно полезен для разработчиков, работающих с PrestaShop API, так как он гарантирует, что все необходимые поля правильно отформатированы и проверены перед отправкой в API.

## Инициализация Класса

### `__init__` Метод

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

### `_load_product_fields_list` Метод

Этот метод загружает список полей продукта из текстового файла. Ожидается, что файл будет содержать одно имя поля на строку.

```python
def _load_product_fields_list(self) -> List[str]:
    return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)
```

### `_payload` Метод

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

## Поля Продукта

### Поля с Одним Языком

Поля с одним языком - это поля, которые не требуют перевода и хранятся на одном языке. Примеры включают `id_product`, `id_supplier`, `id_manufacturer` и т.д.

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
        logger.error(f"""Ошибка заполнения поля: \'ID\' данными {value}
        Ошибка: """, ex)
        return
```

### Поля с Несколькими Языками

Поля с несколькими языками - это поля, которые требуют перевода и хранятся на нескольких языках. Примеры включают `name`, `description`, `meta_title` и т.д.

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
        logger.error(f"""Ошибка заполнения поля: \'name\' данными {value}
        Ошибка: """, ex)
        return
```

## Ассоциации

Ассоциации используются для связи продуктов с другими сущностями, такими как категории, производители и поставщики. Свойство `associations` позволяет устанавливать и получать эти ассоциации.

#### Пример: `associations`

```python
@property
def associations(self) -> Optional[Dict]:
    return self.presta_fields.associations or None

@associations.setter
def associations(self, value: Dict[str, Optional[str]]):
    self.presta_fields.associations = value
```

## Значения по Умолчанию

Значения по умолчанию для полей продукта можно загрузить из JSON-файла с помощью метода `_payload`. Этот метод гарантирует, что все поля имеют значение по умолчанию, которое можно переопределить при необходимости.

## Обработка Ошибок

Класс включает надежную обработку ошибок для перехвата и регистрации любых исключений, которые возникают во время установки полей продукта. Это гарантирует, что любые проблемы регистрируются и могут быть устранены разработчиком.

#### Пример: Обработка Ошибок в `id_product`

```python
@id_product.setter
def id_product(self, value: int = None):
    try:
        self.presta_fields.id_product = value
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: \'ID\' данными {value}
        Ошибка: """, ex)
        return
```

## Примеры Использования

### Пример 1: Установка Поля с Одним Языком

```python
product = ProductFields()
product.id_product = 123
print(product.id_product)  # Output: 123
```

### Пример 2: Установка Поля с Несколькими Языками

```python
product = ProductFields()
product.name = "Product Name", lang='en'
print(product.name)  # Output: {'language': [{'attrs': {'id': 1}, 'value': 'Product Name'}]}
```

### Пример 3: Установка Ассоциаций

```python
product = ProductFields()
product.associations = {'categories': [{'id': 2}, {'id': 3}]}
print(product.associations)  # Output: {'categories': [{'id': 2}, {'id': 3}]}
```

## Заключение

Класс `ProductFields` - это мощный инструмент для управления данными о продукте в PrestaShop API. Он предоставляет четкий и последовательный интерфейс для обработки как полей с одним языком, так и с несколькими языками, гарантируя, что данные правильно отформатированы и проверены перед отправкой в API. Благодаря надежной обработке ошибок и поддержке значений по умолчанию класс упрощает процесс работы с данными о продукте в PrestaShop.