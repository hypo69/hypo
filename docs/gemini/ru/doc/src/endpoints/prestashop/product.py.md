# Модуль для взаимодействия с товарами в PrestaShop (`product.py`)

## Обзор

Модуль `product.py` предназначен для взаимодействия с API PrestaShop, в частности, для управления товарами. Он включает в себя классы и функции для получения информации о товарах, добавления новых товаров, а также вспомогательные методы для работы с категориями и конфигурацией.

## Подробнее

Этот модуль является частью проекта `hypotez` и отвечает за автоматизацию работы с товарами в PrestaShop. Он использует API PrestaShop для выполнения различных операций, таких как получение данных о товарах, добавление новых товаров и обновление существующих. Модуль предоставляет удобный интерфейс для работы с API PrestaShop, абстрагируя детали реализации и упрощая процесс интеграции с другими частями проекта.

## Содержание

1.  [Классы](#классы)
    *   [Config](#config)
    *   [PrestaProduct](#prestaproduct)
2.  [Функции](#функции)
    *   [example\_add\_new\_product](#example_add_new_product)
    *   [example\_get\_product](#example_get_product)

## Классы

### `Config`

**Описание**: Класс конфигурации для настроек продукта PrestaShop.

**Принцип работы**:
Класс `Config` содержит статические параметры конфигурации, необходимые для взаимодействия с API PrestaShop. Он определяет, использовать ли переменные окружения или параметры из `keepass` для получения данных для подключения к API, а также содержит значения домена API и ключа API. В зависимости от значения `USE_ENV` и `MODE` класс выбирает соответствующие параметры для подключения к API.

**Атрибуты**:

*   `USE_ENV` (bool): Определяет, использовать ли переменные окружения для конфигурации. По умолчанию `False`.
*   `MODE` (str): Режим работы (например, 'dev', 'dev8'). По умолчанию `'dev'`.
*   `POST_FORMAT` (str): Формат отправляемых данных (XML). По умолчанию `'XML'`.
*   `API_DOMAIN` (str): Домен API PrestaShop.
*   `API_KEY` (str): Ключ API PrestaShop.

### `PrestaProduct`

**Описание**: Класс для манипуляций с товарами в PrestaShop.

**Наследует**:
`PrestaShop`: Класс `PrestaProduct` наследует функциональность класса `PrestaShop`, расширяя его возможностями для работы с товарами.

**Принцип работы**:

Класс `PrestaProduct` предназначен для работы с товарами в PrestaShop. Он предоставляет методы для получения схемы товара, добавления новых товаров, получения родительских категорий и т.д. Класс использует API PrestaShop для выполнения этих операций.

**Методы**:

*   `__init__(self, api_key: Optional[str] = '', api_domain: Optional[str] = '', *args, **kwargs) -> None`
*   `get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict`
*   `get_parent_category(self, id_category: int) -> Optional[int]`
*   `_add_parent_categories(self, f: ProductFields) -> None`
*   `get_product(self, id_product: int, **kwards) -> dict`
*   `add_new_product(self, f: ProductFields) -> dict`

#### `__init__`

```python
def __init__(self, api_key: Optional[str] = '', api_domain: Optional[str] = '', *args, **kwargs) -> None
```

**Назначение**: Инициализирует объект `PrestaProduct`.

**Параметры**:

*   `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию ''.
*   `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию ''.
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает конструктор родительского класса `PrestaShop` с переданными параметрами или значениями по умолчанию из класса `Config`.
2.  Инициализирует объект `PrestaProduct` с заданным ключом API и доменом API.

#### `get_product_schema`

```python
def get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict:
```

**Назначение**: Получает схему ресурса продукта из PrestaShop.

**Параметры**:

*   `resource_id` (Optional[str | int], optional): Идентификатор ресурса продукта. По умолчанию `None`.
*   `schema` (Optional[str], optional): Тип схемы. По умолчанию `'blank'`.

**Возвращает**:

*   `dict`: Схема ресурса продукта.

**Как работает функция**:

1.  Вызывает метод `get_schema` родительского класса `PrestaShop` с указанием ресурса `'products'` и переданными параметрами.
2.  Возвращает полученную схему.

ASCII схема работы функции:

```
    get_product_schema
    │
    └───> get_schema (из PrestaShop)
         │
         └───>  Возвращает схему ресурса продукта
```

**Примеры**:

```python
product = PrestaProduct()
schema = product.get_product_schema(resource_id=2191)
print(schema)
```

#### `get_parent_category`

```python
def get_parent_category(self, id_category: int) -> Optional[int]:
```

**Назначение**: Извлекает родительские категории из PrestaShop для заданной категории рекурсивно.

**Параметры**:

*   `id_category` (int): Идентификатор категории.

**Возвращает**:

*   `Optional[int]`: Идентификатор родительской категории (int).

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка при получении категории.

**Как работает функция**:

1.  Пытается получить данные о категории из PrestaShop по её ID.
2.  Извлекает `id_parent` из ответа.
3.  Возвращает `id_parent` как целое число.
4.  Если происходит ошибка, логирует её и возвращает `None`.
5.  Если категория не найдена, логирует ошибку и возвращает `None`.

ASCII схема работы функции:

```
    get_parent_category
    │
    └───> read (из PrestaShop)
         │
         ├───> Успешное получение данных о категории
         │    │
         │    └───> Извлечение id_parent
         │    │
         │    └───> Возврат id_parent
         │
         └───> Ошибка при получении данных
              │
              └───> Логирование ошибки
              │
              └───> Возврат None
```

**Примеры**:

```python
product = PrestaProduct()
parent_category_id = product.get_parent_category(id_category=10)
print(parent_category_id)
```

#### `_add_parent_categories`

```python
def _add_parent_categories(self, f: ProductFields) -> None:
```

**Назначение**: Вычисляет и добавляет все родительские категории для списка идентификаторов категорий в объект `ProductFields`.

**Параметры**:

*   `f` (ProductFields): Объект `ProductFields`, к которому нужно добавить родительские категории.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Перебирает все дополнительные категории в объекте `ProductFields`.
2.  Извлекает идентификатор категории.
3.  Если идентификатор категории равен 1 или 2, пропускает его (корневые категории PrestaShop).
4.  В цикле получает родительскую категорию для текущей категории, пока не достигнет корневой категории или не произойдет ошибка.
5.  Добавляет идентификатор родительской категории в список дополнительных категорий объекта `ProductFields`.

ASCII схема работы функции:

```
    _add_parent_categories
    │
    └───> Перебор дополнительных категорий
         │
         ├───> cat_id == 1 or cat_id == 2?
         │    │
         │    └───> Да: Пропуск
         │    │
         │    └───> Нет:
         │         │
         │         └───> Цикл (пока cat_id > 2)
         │              │
         │              └───> get_parent_category
         │              │
         │              └───> Добавление родительской категории
         │
         └───> Завершение
```

**Примеры**:

```python
from src.endpoints.prestashop.product_fields import ProductFields

product = PrestaProduct()
f = ProductFields()
f.additional_categories = [{'id': '10'}, {'id': '11'}]
product._add_parent_categories(f)
print(f.additional_categories)
```

#### `get_product`

```python
def get_product(self, id_product: int, **kwards) -> dict:
```

**Назначение**: Возвращает словарь полей товара из магазина PrestaShop.

**Параметры**:

*   `id_product` (int): Значение поля ID в таблице `product` PrestaShop.
*   `**kwards`: Дополнительные параметры запроса.

**Возвращает**:

*   `dict`: Словарь с информацией о продукте.

**Как работает функция**:

1.  Формирует словарь с параметром `data_format`: `'JSON'`.
2.  Вызывает метод `read` родительского класса `PrestaShop` с указанием ресурса `'products'`, идентификатора продукта и сформированным словарем параметров.
3.  Возвращает полученный словарь.

ASCII схема работы функции:

```
    get_product
    │
    └───> Формирование параметров
    │
    └───> read (из PrestaShop)
         │
         └───> Возврат данных о продукте
```

**Примеры**:

```python
product = PrestaProduct()
product_data = product.get_product(id_product=2191)
print(product_data)
```

#### `add_new_product`

```python
def add_new_product(self, f: ProductFields) -> dict:
```

**Назначение**: Добавляет новый продукт в PrestaShop.

**Параметры**:

*   `f` (ProductFields): Экземпляр класса `ProductFields`, содержащий информацию о продукте.

**Возвращает**:

*   `dict`: Объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, иначе `None`.

**Как работает функция**:

1.  Добавляет `id_category_default` в поле `additional_categories` для поиска родительских категорий.
2.  Вызывает метод `_add_parent_categories` для добавления родительских категорий.
3.  Преобразует объект `ProductFields` в словарь формата PrestaShop.
4.  В зависимости от формата `Config.POST_FORMAT` (XML или JSON) преобразует данные в XML или оставляет в формате JSON.
5.  Отправляет данные в API PrestaShop с помощью метода `create`.
6.  Загружает изображение продукта в PrestaShop.
7.  В случае успеха возвращает объект `ProductFields` с установленным `id_product`, иначе возвращает `None`.

ASCII схема работы функции:

```
    add_new_product
    │
    ├───> Добавление id_category_default в additional_categories
    │
    ├───> _add_parent_categories
    │
    ├───> to_dict (ProductFields -> dict)
    │
    ├───> POST_FORMAT == 'XML'?
    │    │
    │    ├───> Да: presta_fields_to_xml
    │    │
    │    └───> Нет: оставляет как JSON
    │
    ├───> create (PrestaShop API)
    │
    ├───> create_binary (upload image)
    │
    └───> Возврат ProductFields или None
```

**Примеры**:

```python
from src.endpoints.prestashop.product_fields import ProductFields

product = PrestaProduct()
f = ProductFields()
f.name = [{'language': 2, 'value': 'Test Product'}]
f.id_category_default = 2
f.price = 10.0
f.quantity = 100
f.local_image_path = 'path/to/image.png'
new_product = product.add_new_product(f)
print(new_product)
```

## Функции

### `example_add_new_product`

```python
def example_add_new_product() -> None:
```

**Назначение**: Пример добавления товара в PrestaShop.

**Параметры**:

*   Нет

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Создает экземпляр класса `PrestaProduct`.
2.  Загружает пример данных из JSON-файла.
3.  Преобразует данные в XML-формат.
4.  Отправляет данные в API PrestaShop с помощью метода `create`.
5.  Выводит ответ от API.

ASCII схема работы функции:

```
    example_add_new_product
    │
    ├───> Создание экземпляра PrestaProduct
    │
    ├───> Загрузка данных из JSON
    │
    ├───> Преобразование в XML
    │
    ├───> create (PrestaShop API)
    │
    └───> Вывод ответа
```

**Примеры**:

```python
example_add_new_product()
```

### `example_get_product`

```python
def example_get_product(id_product: int, **kwards) -> None:
```

**Назначение**: Пример получения товара из PrestaShop.

**Параметры**:

*   `id_product` (int): Идентификатор товара.
*   `**kwards`: Дополнительные параметры запроса.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Создает экземпляр класса `PrestaProduct`.
2.  Формирует словарь с параметрами запроса.
3.  Получает данные о товаре из PrestaShop с помощью метода `get_product`.
4.  Сохраняет данные о товаре в JSON-файл.

ASCII схема работы функции:

```
    example_get_product
    │
    ├───> Создание экземпляра PrestaProduct
    │
    ├───> Формирование параметров
    │
    ├───> get_product
    │
    └───> Сохранение в JSON
```

**Примеры**:

```python
example_get_product(id_product=2191)