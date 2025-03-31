# Модуль для взаимодействия с товарами в PrestaShop (`product.py`)

## Обзор

Модуль `product.py` предназначен для взаимодействия с товарами в интернет-магазине PrestaShop через API. Он включает в себя классы и функции для получения информации о товарах, добавления новых товаров, а также для работы с категориями товаров.

## Подробнее

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с PrestaShop. Он использует API PrestaShop для выполнения различных операций, связанных с товарами, таких как получение схемы товара, добавление нового товара, получение родительских категорий и т.д. Модуль содержит классы для конфигурации API и для представления товара PrestaShop, а также функции для выполнения запросов к API и обработки ответов.

## Классы

### `Config`

**Описание**: Класс конфигурации для настроек продукта PrestaShop.

**Как работает класс**:
Этот класс определяет параметры конфигурации для взаимодействия с API PrestaShop. Он включает в себя настройки для API-ключа, домена API, формата POST-запросов и режима работы (разработка или продакшн). Класс использует переменные окружения, если `USE_ENV` установлен в `True`, в противном случае используются значения из `gs.credentials`.

- Все комментарии и docstring должны быть на русском языке в формате UTF-8. Если в оригинальном коде текст напюисан на английском - переводи его на русский

**Методы**:
- Отсутствуют

**Параметры**:
- `USE_ENV` (bool): Указывает, использовать ли переменные окружения для конфигурации API. По умолчанию `False`.
- `MODE` (str): Режим работы (например, `'dev'`). По умолчанию `'dev'`.
- `POST_FORMAT` (str): Формат POST-запросов (например, `'XML'`). По умолчанию `'XML'`.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Примеры**:

```python
# Пример использования класса Config
config = Config()
print(config.API_DOMAIN)
print(config.API_KEY)
```

### `PrestaProduct`

**Описание**: Класс для работы с товарами PrestaShop.

**Как работает класс**:
Этот класс наследуется от `PrestaShop` и предоставляет методы для выполнения операций с товарами, таких как получение схемы товара, добавление нового товара и получение информации о товаре. Он использует API PrestaShop для взаимодействия с магазином.

**Методы**:

- `__init__(self, api_key: Optional[str] = '', api_domain: Optional[str] = '', *args, **kwargs) -> None`
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
    **Как работает метод**:
    Инициализирует объект `PrestaProduct`. Он принимает API-ключ и домен API в качестве аргументов и передает их в конструктор родительского класса `PrestaShop`. Если API-ключ или домен API не указаны, используются значения из класса `Config`.

    **Параметры**:
    - `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `''`.
    - `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `''`.
    - `*args`: Произвольные позиционные аргументы.
    - `**kwargs`: Произвольные именованные аргументы.

    **Возвращает**:
    - `None`

- `get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict`
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
    **Как работает метод**:
    Получает схему ресурса продукта из PrestaShop. Он вызывает метод `get_schema` родительского класса `PrestaShop` с параметрами, указывающими на ресурс `products` и запрошенный тип схемы.

    **Параметры**:
    - `resource_id` (Optional[str | int], optional): ID ресурса продукта. По умолчанию `None`.
    - `schema` (Optional[str], optional): Тип схемы. По умолчанию `'blank'`.

    **Возвращает**:
    - `dict`: Схема ресурса продукта.

- `get_parent_category(self, id_category: int) -> Optional[int]`
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
    **Как работает метод**:
    Рекурсивно извлекает родительские категории из PrestaShop для заданной категории. Он вызывает метод `read` для получения информации о категории и возвращает ID родительской категории. Если категория не найдена или происходит ошибка, возвращает `None`.

    **Параметры**:
    - `id_category` (int): ID категории.

    **Возвращает**:
    - `Optional[int]`: ID родительской категории.

- `_add_parent_categories(self, f: ProductFields) -> None`
    ```python
    def _add_parent_categories(self, f: ProductFields) -> None:
        """Calculates and appends all parent categories for a list of category IDs to the ProductFields object.

        Args:
            f (ProductFields): The ProductFields object to append parent categories to.
        """
        ...
    ```
    **Как работает метод**:
    Вычисляет и добавляет все родительские категории для списка ID категорий к объекту `ProductFields`. Он итерируется по дополнительным категориям товара и рекурсивно получает их родительские категории, добавляя их в объект `ProductFields`.

    **Параметры**:
    - `f` (ProductFields): Объект `ProductFields`, к которому нужно добавить родительские категории.

    **Возвращает**:
    - `None`

- `get_product(self, id_product: int, **kwards) -> dict`
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
    **Как работает метод**:
    Возвращает словарь полей товара из магазина PrestaShop. Он вызывает метод `read` для получения информации о товаре по его ID.

    **Параметры**:
    - `id_product` (int): ID товара.
    - `**kwards`: Дополнительные параметры запроса.

    **Возвращает**:
    - `dict`: Словарь полей товара.

- `add_new_product(self, f: ProductFields) -> dict`
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
    **Как работает метод**:
    Добавляет новый товар в PrestaShop. Он преобразует объект `ProductFields` в словарь формата PrestaShop и отправляет его в API PrestaShop.

    Внутри функции происходят следующие действия и преобразования:
    A. Добавление `id_category_default` в поле `additional_categories` для поиска родительских категорий.
    |
    B. Вызов `self._add_parent_categories(f)` для добавления родительских категорий.
    |
    C. Преобразование объекта `ProductFields` в словарь `presta_product_dict`.
    |
    D. Преобразование словаря в XML-формат, если `Config.POST_FORMAT == 'XML'`.
    |
    E. Отправка данных в API PrestaShop с помощью метода `self.create`.
    |
    F. Обработка ответа от API и извлечение `id` добавленного продукта.

    **Параметры**:
    - `f` (ProductFields): Объект `ProductFields`, содержащий информацию о товаре.

    **Возвращает**:
    - `dict`: Объект `ProductFields` с установленным `id_product`, если товар был успешно добавлен, или пустой словарь `{}` в случае ошибки.

**Примеры**:

```python
# Пример создания экземпляра класса PrestaProduct
product = PrestaProduct(api_key='YOUR_API_KEY', api_domain='YOUR_API_DOMAIN')
```

## Функции

### `example_add_new_product() -> None`

```python
def example_add_new_product() -> None:
    """Пример для добавления товара в Prestashop"""
    ...
```

**Как работает функция**:
Это пример функции, демонстрирующий добавление нового товара в PrestaShop. Она создает экземпляр класса `PrestaProduct`, загружает пример данных о товаре из JSON-файла, преобразует их в XML-формат и отправляет запрос на добавление товара в PrestaShop.

Внутри функции происходят следующие действия и преобразования:
    A. Cоздание экземпляра класса `PrestaProduct`.
    |
    B. Загрузка пример данных о товаре из JSON-файла.
    |
    C. Преобразование данных в XML-формат.
    |
    D. Отправка запроса на добавление товара в PrestaShop.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

### `example_get_product(id_product: int, **kwards) -> None`

```python
def example_get_product(id_product: int, **kwards) -> None:
    """ """
    ...
```

**Как работает функция**:
Это пример функции, демонстрирующий получение информации о товаре из PrestaShop по его ID. Она создает экземпляр класса `PrestaProduct`, задает параметры запроса и вызывает метод `get_product` для получения информации о товаре.

Внутри функции происходят следующие действия и преобразования:
    A. Cоздание экземпляра класса `PrestaProduct`.
    |
    B. Задание параметров запроса.
    |
    C. Вызов метода `get_product` для получения информации о товаре.
    |
    D. Сериализация ответа в JSON-файл.

**Параметры**:
- `id_product` (int): ID товара, информацию о котором нужно получить.
- `**kwards`: Дополнительные параметры запроса.

**Возвращает**:
- `None`