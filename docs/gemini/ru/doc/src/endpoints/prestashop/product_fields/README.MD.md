# Модуль ProductFields

## Обзор

Модуль `ProductFields` предназначен для управления и структурирования данных о продуктах в формате, требуемом API PrestaShop. Этот класс предоставляет комплексный интерфейс для обработки полей продукта, включая как одноязычные, так и многоязычные поля. Он обеспечивает правильное форматирование и проверку данных перед отправкой в API PrestaShop.

## Подробней

Класс `ProductFields` упрощает процесс создания, обновления и управления данными о продуктах, предоставляя понятный и согласованный интерфейс для взаимодействия с полями продукта. Он особенно полезен для разработчиков, работающих с API PrestaShop, поскольку гарантирует, что все необходимые поля правильно отформатированы и проверены перед отправкой в API.

## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` инкапсулирует структуру и поведение полей продукта в базе данных PrestaShop.

**Методы**:
- `__init__`: Инициализирует класс `ProductFields`, загружая список полей продукта и устанавливая значения по умолчанию.
- `_load_product_fields_list`: Загружает список полей продукта из текстового файла.
- `_payload`: Загружает значения по умолчанию для полей продукта из JSON-файла.

**Параметры**:
- Нет явных параметров для инициализации класса.

**Примеры**
```python
product = ProductFields()
print(product.id_product)
```

## Функции

### `_load_product_fields_list`

```python
def _load_product_fields_list(self) -> List[str]:
    """
    Загружает список полей продукта из текстового файла.

    Args:
        self: Экземпляр класса.

    Returns:
        List[str]: Список полей продукта.

    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: Если возникает ошибка при чтении файла.

    Example:
        >>> product_fields = ProductFields()
        >>> fields_list = product_fields._load_product_fields_list()
        >>> print(fields_list[:5])  # Вывод первых 5 элементов списка
    """
    ...
```

**Описание**: Загружает список полей продукта из текстового файла. Ожидается, что файл содержит одно имя поля на строку.

**Возвращает**:
- `List[str]`: Список полей продукта.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `Exception`: Если возникает ошибка при чтении файла.

**Примеры**:
```python
product_fields = ProductFields()
fields_list = product_fields._load_product_fields_list()
print(fields_list[:5])  # Вывод первых 5 элементов списка
```

### `_payload`

```python
def _payload(self) -> bool:
    """
    Загружает значения по умолчанию для полей продукта из JSON-файла.

    Args:
        self: Экземпляр класса.

    Returns:
        bool: True, если загрузка прошла успешно, иначе False.

    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: Если файл не является корректным JSON.
        Exception: Если возникает ошибка при чтении файла.

    Example:
        >>> product_fields = ProductFields()
        >>> result = product_fields._payload()
        >>> print(result)
    """
    ...
```

**Описание**: Загружает значения по умолчанию для полей продукта из JSON-файла. Если файл не найден или не может быть загружен, регистрируется отладочное сообщение.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `json.JSONDecodeError`: Если файл не является корректным JSON.
- `Exception`: Если возникает ошибка при чтении файла.

**Примеры**:
```python
product_fields = ProductFields()
result = product_fields._payload()
print(result)
```

### `id_product` (property)

```python
@property
def id_product(self) -> Optional[int]:
    """
    Возвращает значение ID продукта.

    Args:
        self: Экземпляр класса.

    Returns:
        Optional[int]: ID продукта.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.id_product = 123
        >>> print(product_fields.id_product)
        123
    """
    ...

@id_product.setter
def id_product(self, value: int = None):
    """
    Устанавливает значение ID продукта.

    Args:
        self: Экземпляр класса.
        value (int, optional): ID продукта. По умолчанию None.

    Raises:
        ProductFieldException: Если возникает ошибка при установке значения.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.id_product = 123
        >>> print(product_fields.id_product)
        123
    """
    ...
```

**Описание**: Управляет значением поля `id_product`.

**Возвращает**:
- `Optional[int]`: ID продукта.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения.

**Примеры**:
```python
product_fields = ProductFields()
product_fields.id_product = 123
print(product_fields.id_product)
```

### `name` (property)

```python
@property
def name(self):
    """
    Возвращает название продукта.

    Args:
        self: Экземпляр класса.

    Returns:
        str: Название продукта.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.name = "Product Name", lang='en'
        >>> print(product_fields.name)
        {'language': [{'attrs': {'id': 1}, 'value': 'Product Name'}]}
    """
    ...

@name.setter
def name(self, value: str, lang:str = 'en') -> bool:
    """
    Устанавливает название продукта на определенном языке.

    Args:
        self: Экземпляр класса.
        value (str): Название продукта.
        lang (str, optional): Язык названия продукта. По умолчанию 'en'.

    Returns:
        bool: True, если установка прошла успешно.

    Raises:
        ProductFieldException: Если возникает ошибка при установке значения.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.name = "Product Name", lang='en'
        >>> print(product_fields.name)
        {'language': [{'attrs': {'id': 1}, 'value': 'Product Name'}]}
    """
    ...
```

**Описание**: Управляет значением поля `name`.

**Возвращает**:
- `str`: Название продукта.

**Вызывает исключения**:
- `ProductFieldException`: Если возникает ошибка при установке значения.

**Примеры**:
```python
product_fields = ProductFields()
product_fields.name = "Product Name", lang='en'
print(product_fields.name)
```

### `associations` (property)

```python
@property
def associations(self) -> Optional[Dict]:
    """
    Возвращает ассоциации продукта.

    Args:
        self: Экземпляр класса.

    Returns:
        Optional[Dict]: Ассоциации продукта.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.associations = {'categories': [{'id': 2}, {'id': 3}]}
        >>> print(product_fields.associations)
        {'categories': [{'id': 2}, {'id': 3}]}
    """
    ...

@associations.setter
def associations(self, value: Dict[str, Optional[str]]):
    """
    Устанавливает ассоциации продукта.

    Args:
        self: Экземпляр класса.
        value (Dict[str, Optional[str]]): Ассоциации продукта.

    Example:
        >>> product_fields = ProductFields()
        >>> product_fields.associations = {'categories': [{'id': 2}, {'id': 3}]}
        >>> print(product_fields.associations)
        {'categories': [{'id': 2}, {'id': 3}]}
    """
    ...
```

**Описание**: Управляет значением поля `associations`.

**Возвращает**:
- `Optional[Dict]`: Ассоциации продукта.

**Примеры**:
```python
product_fields = ProductFields()
product_fields.associations = {'categories': [{'id': 2}, {'id': 3}]}
print(product_fields.associations)
```