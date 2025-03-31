# Модуль для взаимодействия с товарами в PrestaShop

## Обзор

Модуль `product.py` предназначен для работы с товарами в PrestaShop. Он предоставляет классы и функции для получения информации о товарах, добавления новых товаров и управления категориями товаров.

## Подробней

Модуль содержит класс `PrestaProduct`, который наследует от класса `PrestaShop` и реализует методы для взаимодействия с API PrestaShop для управления товарами.

## Классы

### `Config`

**Описание**: Класс конфигурации для настроек продукта PrestaShop.

**Как работает класс**:
Класс `Config` содержит статические атрибуты, определяющие параметры подключения к API PrestaShop, такие как домен API, ключ API и формат данных для запросов (XML или JSON). Он также определяет, использовать ли переменные окружения или параметры из `keepass`.

**Атрибуты**:

- `USE_ENV` (bool): Указывает, использовать ли переменные окружения для конфигурации. По умолчанию `False`.
- `MODE` (str): Режим работы (например, `dev`, `dev8`). По умолчанию `dev`.
- `POST_FORMAT` (str): Формат данных для отправки запросов (XML или JSON). По умолчанию `XML`.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Примеры**:

```python
config = Config()
print(config.API_DOMAIN)
print(config.API_KEY)
```

### `PrestaProduct`

**Описание**: Класс для работы с товарами в PrestaShop.

**Как работает класс**:
Класс `PrestaProduct` наследуется от класса `PrestaShop` и предоставляет методы для получения схемы товара, добавления новых товаров, получения родительских категорий и т.д. Он использует API PrestaShop для выполнения этих операций.

**Методы**:

- `__init__(self, api_key: Optional[str] = '', api_domain: Optional[str] = '', *args, **kwargs) -> None`
- `get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict`
- `get_parent_category(self, id_category: int) -> Optional[int]`
- `_add_parent_categories(self, f: ProductFields) -> None`
- `get_product(self, id_product: int, **kwards) -> dict`
- `add_new_product(self, f: ProductFields) -> dict`

#### `__init__`

```python
def __init__(self, api_key: Optional[str] = '', api_domain: Optional[str] = '', *args, **kwargs) -> None:
    """Initializes a Product object.

    Args:
        api_key (Optional[str], optional): PrestaShop API key. Defaults to ''.
        api_domain (Optional[str], optional): PrestaShop API domain. Defaults to ''.

    Returns:
        None
    """
    ...
```

**Назначение**: Инициализирует объект `PrestaProduct`.

**Как работает функция**:
Функция `__init__` является конструктором класса `PrestaProduct`. Она принимает ключ API и домен API PrestaShop в качестве аргументов и инициализирует базовый класс `PrestaShop` с этими параметрами. Если ключ API и домен API не переданы, используются значения по умолчанию из класса `Config`.

**Параметры**:

- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `' '`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `' '`.
- `*args`: Произвольные позиционные аргументы, передаваемые в базовый класс.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в базовый класс.

**Возвращает**:

- `None`

#### `get_product_schema`

```python
def get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict:
    """Get the schema for the product resource from PrestaShop.

    Args:
        resource_id (Optional[str  |  int], optional): The ID of the product resource. Defaults to None.
        schema (Optional[str], optional): The schema type. Defaults to 'blank'.

    Returns:
        dict: The schema for the product resource.
    """
    ...
```

**Назначение**: Получает схему ресурса продукта из PrestaShop.

**Как работает функция**:
Функция `get_product_schema` вызывает метод `get_schema` базового класса `PrestaShop` для получения схемы ресурса продукта из API PrestaShop. Она принимает идентификатор ресурса продукта и тип схемы в качестве аргументов и возвращает схему ресурса продукта в виде словаря.

**Параметры**:

- `resource_id` (Optional[str | int], optional): Идентификатор ресурса продукта. По умолчанию `None`.
- `schema` (Optional[str], optional): Тип схемы. По умолчанию `'blank'`.

**Возвращает**:

- `dict`: Схема ресурса продукта.

#### `get_parent_category`

```python
def get_parent_category(self, id_category: int) -> Optional[int]:
    """Retrieve parent categories from PrestaShop for a given category recursively.

    Args:
        id_category (int): The category ID.

    Returns:
        Optional[int]: parent category id (int).
    """
    ...
```

**Назначение**: Извлекает родительские категории из PrestaShop для заданной категории рекурсивно.

**Как работает функция**:
Функция `get_parent_category` получает родительскую категорию для заданной категории из API PrestaShop. Она принимает идентификатор категории в качестве аргумента и возвращает идентификатор родительской категории. Если категория не найдена или произошла ошибка, функция возвращает `None`.
Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `read` для получения информации о категории из PrestaShop API.
|
B. Обработка ответа API. Извлечение `id_parent` из полученных данных.
|
C. Обработка исключений. В случае ошибки логируется сообщение об ошибке и возвращается `None`.

**Параметры**:

- `id_category` (int): Идентификатор категории.

**Возвращает**:

- `Optional[int]`: Идентификатор родительской категории (int).

**Вызывает исключения**:

- `Exception`: Если возникает ошибка при получении категории.

#### `_add_parent_categories`

```python
def _add_parent_categories(self, f: ProductFields) -> None:
    """Calculates and appends all parent categories for a list of category IDs to the ProductFields object.

    Args:
        f (ProductFields): The ProductFields object to append parent categories to.
    """
    ...
```

**Назначение**: Вычисляет и добавляет все родительские категории для списка идентификаторов категорий в объект `ProductFields`.

**Как работает функция**:
Функция `_add_parent_categories` принимает объект `ProductFields` в качестве аргумента и добавляет в него все родительские категории для каждой категории, указанной в `f.additional_categories`. Она использует метод `get_parent_category` для получения родительских категорий рекурсивно.

**Параметры**:

- `f` (ProductFields): Объект `ProductFields`, в который добавляются родительские категории.

**Возвращает**:

- `None`

#### `get_product`

```python
def get_product(self, id_product: int, **kwards) -> dict:
    """Возваращает словарь полей товара из магазина Prestasop

    Args:
        id_product (int): значение поля ID в таблице `product` Preastashop

    Returns:
        dict:
        {
            'product':
                {... product fields}
        }
    """
    ...
```

**Назначение**: Возвращает словарь полей товара из магазина PrestaShop.

**Как работает функция**:
Функция `get_product` принимает идентификатор товара в качестве аргумента и возвращает словарь, содержащий поля товара из API PrestaShop.

**Параметры**:

- `id_product` (int): Значение поля ID в таблице `product` PrestaShop.

**Возвращает**:

```
dict:
{
    'product':
        {... product fields}
}
```

#### `add_new_product`

```python
def add_new_product(self, f: ProductFields) -> dict:
    """Add a new product to PrestaShop.

    Преобразовывает объект `ProducFields` в словарь формата `Prestashop` и отрапавлет его в API Престашоп

    Args:
        f (ProductFields): An instance of the ProductFields data class containing the product information.

    Returns:
        dict: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
    """
    ...
```

**Назначение**: Добавляет новый товар в PrestaShop.

**Как работает функция**:
Функция `add_new_product` принимает объект `ProductFields`, преобразует его в словарь формата PrestaShop и отправляет его в API PrestaShop для добавления нового товара. Она также загружает изображение товара в PrestaShop.

Внутри функции происходят следующие действия и преобразования:
A. Добавление `id_category_default` в поле `additional_categories` для поиска её родительских категорий.
|
B. Вызов функции `_add_parent_categories` для добавления родительских категорий.
|
C. Преобразование объекта `ProductFields` в словарь `presta_product_dict`.
|
D. Преобразование словаря `presta_product_dict` в XML-формат для отправки в API PrestaShop.
|
E. Отправка данных в API PrestaShop с использованием метода `create`.
|
F. Загрузка изображения товара в PrestaShop с использованием метода `create_binary`.
|
G. Обработка ответа от API PrestaShop и логирование информации о добавленном товаре.

**Параметры**:

- `f` (ProductFields): Экземпляр класса данных `ProductFields`, содержащий информацию о товаре.

**Возвращает**:

- `dict`: Возвращает объект `ProductFields` с установленным `id_product`, если товар был успешно добавлен, иначе `{}`.

**Вызывает исключения**:

- `KeyError`, `TypeError`: Если возникает ошибка при разборе ответа от сервера.

## Функции

### `example_add_new_product`

```python
def example_add_new_product() -> None:
    """Пример для добавления товара в Prestashop"""
    ...
```

**Назначение**: Пример добавления товара в PrestaShop.

**Как работает функция**:
Функция `example_add_new_product` создает экземпляр класса `PrestaProduct` и использует его для добавления нового товара в PrestaShop. Она загружает пример данных о товаре из JSON-файла, преобразует их в XML-формат и отправляет в API PrestaShop.

### `example_get_product`

```python
def example_get_product(id_product: int, **kwards) -> None:
    """"""
    ...
```

**Назначение**: Пример получения товара из PrestaShop.

**Как работает функция**:
Функция `example_get_product` создает экземпляр класса `PrestaProduct` и использует его для получения информации о товаре из PrestaShop. Она принимает идентификатор товара в качестве аргумента и выводит информацию о товаре в формате JSON.

**Параметры**:

- `id_product` (int): Идентификатор товара.
- `**kwards`: Дополнительные параметры для запроса.