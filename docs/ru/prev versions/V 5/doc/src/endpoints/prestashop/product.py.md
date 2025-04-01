# Модуль для взаимодействия с товарами в PrestaShop (`product.py`)

## Обзор

Модуль `src.endpoints.prestashop.product` предназначен для взаимодействия с товарами в PrestaShop. Он предоставляет классы и функции для получения информации о товарах, добавления новых товаров, а также для работы с категориями товаров. Модуль использует API PrestaShop для выполнения этих задач.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с PrestaShop для управления товарами. Он включает в себя:

-   Класс `Config` для хранения конфигурационных параметров API PrestaShop.
-   Класс `PrestaProduct` для работы с товарами через API PrestaShop, включая получение и добавление товаров.
-   Вспомогательные функции для преобразования данных и выполнения запросов к API.

## Классы

### `Config`

**Описание**: Класс конфигурации для настроек PrestaShop API.

**Как работает класс**:
Этот класс содержит статические параметры конфигурации, такие как ключи API и домен PrestaShop. Он определяет, использовать ли переменные окружения или значения по умолчанию для настроек API. В зависимости от значения `MODE` выбираются различные учетные данные PrestaShop.

**Параметры**:

-   `USE_ENV` (bool): Указывает, использовать ли переменные окружения для конфигурации API. По умолчанию `False`.
-   `MODE` (str): Режим работы (`dev`, `dev8` или другой). Влияет на выбор учетных данных API. По умолчанию `dev`.
-   `POST_FORMAT` (str): Формат отправки данных (например, `JSON`). По умолчанию `'JSON'`.
-   `API_DOMAIN` (str): Домен PrestaShop API.
-   `API_KEY` (str): Ключ PrestaShop API.

**Примеры**:

```python
config = Config()
print(config.API_DOMAIN)
print(config.API_KEY)
```

### `PrestaProduct`

**Описание**: Класс для работы с товарами в PrestaShop.

**Как работает класс**:
Класс `PrestaProduct` наследуется от класса `PrestaShop` и предоставляет методы для выполнения различных операций с товарами через API PrestaShop. Он включает методы для получения схемы товара, добавления новых товаров, получения родительских категорий и т.д.

**Методы**:

-   `__init__`: Инициализирует объект `PrestaProduct`, вызывая конструктор родительского класса `PrestaShop` с параметрами API.
-   `get_product_schema`: Получает схему ресурса товара из PrestaShop.
-   `get_parent_category`: Рекурсивно получает родительские категории для заданной категории из PrestaShop.
-   `_add_parent_categories`: Вычисляет и добавляет все родительские категории для списка ID категорий в объект `ProductFields`.
-   `get_product`: Возвращает словарь полей товара из магазина PrestaShop.
-   `add_new_product`: Добавляет новый товар в PrestaShop.

**Примеры**:

```python
product = PrestaProduct(api_key=Config.API_KEY, api_domain=Config.API_DOMAIN)
product_data = product.get_product(id_product=2191)
print(product_data)
```

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
```

**Описание**: Инициализирует объект `PrestaProduct`.

**Как работает функция**:
Конструктор класса `PrestaProduct` принимает ключ API и домен PrestaShop в качестве аргументов и передает их в конструктор родительского класса `PrestaShop`. Если аргументы не переданы, используются значения из класса `Config`.

**Параметры**:

-   `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `''`.
-   `api_domain` (Optional[str], optional): Домен PrestaShop API. По умолчанию `''`.

**Возвращает**:

-   `None`

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
```

**Описание**: Получает схему ресурса товара из PrestaShop.

**Как работает функция**:
Метод `get_product_schema` вызывает метод `get_schema` родительского класса `PrestaShop` с параметрами, указывающими на ресурс "products" и запрошенный тип схемы.

**Параметры**:

-   `resource_id` (Optional[str | int], optional): ID ресурса товара. По умолчанию `None`.
-   `schema` (Optional[str], optional): Тип схемы. По умолчанию `'blank'`.

**Возвращает**:

-   `dict`: Схема ресурса товара.

#### `get_parent_category`

```python
def get_parent_category(self, id_category: int) -> Optional[int]:
    """Retrieve parent categories from PrestaShop for a given category recursively.

    Args:
        id_category (int): The category ID.

    Returns:
        Optional[int]: parent category id (int).
    """
```

**Описание**: Рекурсивно получает родительские категории для заданной категории из PrestaShop.

**Как работает функция**:
Метод `get_parent_category` выполняет запрос к API PrestaShop для получения информации о категории по её ID. Затем он извлекает ID родительской категории из ответа API. Если категория не найдена или произошла ошибка, возвращает `None`.

**Параметры**:

-   `id_category` (int): ID категории.

**Возвращает**:

-   `Optional[int]`: ID родительской категории. Возвращает `None`, если категория не найдена или произошла ошибка.

**Вызывает исключения**:

-   `Exception`: Если возникает ошибка при получении категории.

#### `_add_parent_categories`

```python
def _add_parent_categories(self, f: ProductFields) -> None:
    """Calculates and appends all parent categories for a list of category IDs to the ProductFields object.

    Args:
        f (ProductFields): The ProductFields object to append parent categories to.
    """
```

**Описание**: Вычисляет и добавляет все родительские категории для списка ID категорий в объект `ProductFields`.

**Как работает функция**:
Метод `_add_parent_categories` перебирает дополнительные категории товара и добавляет их родительские категории в объект `ProductFields`. Он использует метод `get_parent_category` для получения родительских категорий рекурсивно.

**Параметры**:

-   `f` (ProductFields): Объект `ProductFields`, к которому нужно добавить родительские категории.

**Возвращает**:

-   `None`

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
```

**Описание**: Возвращает словарь полей товара из магазина PrestaShop.

**Как работает функция**:
Метод `get_product` вызывает метод `read` родительского класса `PrestaShop` с параметрами, указывающими на ресурс "products" и запрошенный ID товара.

**Параметры**:

-   `id_product` (int): ID товара.

**Возвращает**:

-   `dict`: Словарь с полями товара.

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
```

**Описание**: Добавляет новый товар в PrestaShop.

**Как работает функция**:
Метод `add_new_product` преобразует объект `ProductFields` в словарь, добавляет родительские категории и отправляет данные в API PrestaShop для создания нового товара.

**Параметры**:

-   `f` (ProductFields): Объект `ProductFields`, содержащий информацию о товаре.

**Возвращает**:

-   `dict`: Объект `ProductFields` с установленным `id_product`, если товар успешно добавлен, иначе `None`.

## Функции

### `example_add_new_product`

```python
def example_add_new_product() -> None:
    """Пример для добавления товара в Prestashop"""
```

**Описание**: Пример добавления товара в PrestaShop.

**Как работает функция**:
Функция `example_add_new_product` создает экземпляр класса `PrestaProduct`, загружает пример данных о товаре из JSON-файла, преобразует их в формат XML и отправляет запрос к API PrestaShop для добавления нового товара.

**Параметры**:

-   Нет

**Возвращает**:

-   `None`

### `example_get_product`

```python
def example_get_product(id_product: int, **kwards) -> None:
    """"""
```

**Описание**: Пример получения товара из PrestaShop.

**Как работает функция**:
Функция `example_get_product` создает экземпляр класса `PrestaProduct`, устанавливает параметры запроса и вызывает метод `get_product` для получения информации о товаре с заданным ID. Результат сохраняется в JSON-файл.

**Параметры**:

-   `id_product` (int): ID товара.
-   `kwards` (dict): Дополнительные параметры запроса.

**Возвращает**:

-   `None`