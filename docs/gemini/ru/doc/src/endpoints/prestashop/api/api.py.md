# Модуль для взаимодействия с PrestaShop API

## Обзор

Модуль `api.py` предоставляет класс `PrestaShop` для взаимодействия с API PrestaShop. Он поддерживает операции CRUD, поиск и загрузку изображений, используя JSON и XML для форматирования сообщений.

## Подробней

Этот модуль позволяет взаимодействовать с PrestaShop API для управления различными аспектами интернет-магазина, такими как товары, категории, клиенты и т.д. Класс `PrestaShop` предоставляет методы для выполнения основных операций, таких как создание, чтение, обновление и удаление данных, а также для поиска и загрузки изображений. Модуль также содержит обработку ошибок и обеспечивает удобный интерфейс для работы с API PrestaShop.

## Классы

### `PrestaShop`

**Описание**: Класс для взаимодействия с PrestaShop API.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShop`.
- `ping`: Проверяет работоспособность веб-сервиса.
- `_check_response`: Проверяет статус ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от PrestaShop API.
- `_prepare_url`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse_response`: Разбирает XML или JSON ответ от API в структуру словаря.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Выполняет поиск ресурсов в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `get_schema`: Получает схему данного ресурса из PrestaShop API.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их.
- `get_apis`: Получает список всех доступных API.
- `upload_image_async`: Асинхронно загружает изображение в PrestaShop API.
- `upload_image_from_url`: Загружает изображение в PrestaShop API.
- `get_product_images`: Получает изображения для продукта.

**Параметры**:
- `api_key` (str): API ключ, сгенерированный в PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию `False`.

**Примеры**
```python
    from src.endpoints.prestashop.api.api import PrestaShop

    api = PrestaShop(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key',
        default_lang=1,
        debug=True,
        data_format='JSON',
    )

    api.ping()

    data = {
        'tax': {
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }

    # Create tax record
    rec = api.create('taxes', data)

    # Update the same tax record
    update_data = {
        'tax': {
            'id': str(rec['id']),
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }

    update_rec = api.write('taxes', update_data)

    # Remove this tax
    api.unlink('taxes', str(rec['id']))

    # Search the first 3 taxes with '5' in the name
    import pprint
    recs = api.search('taxes', filter='[name]=%[5]%', limit='3')

    for rec in recs:
        pprint(rec)

    # Create binary (product image)
    api.create_binary('images/products/22', 'img.jpeg', 'image')
```

## Функции

### `ping`

```python
def ping(self) -> bool:
    """Test if the webservice is working perfectly.

    :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    :rtype: bool
    """
```

**Описание**: Проверяет работоспособность веб-сервиса.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.ping()
```

### `create`

```python
def create(self, resource: str, data: dict, *args, **kwards) -> Optional[dict]:
    """Create a new resource in PrestaShop API.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param data: Data for the new resource.
    :type data: dict

    :return: Response from the API.
    :rtype: dict
    """
```

**Описание**: Создает новый ресурс в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
data = {'product': {'name': 'Новый продукт'}}
api.create('products', data)
```

### `read`

```python
def read(self, resource: str, resource_id: int | str, **kwargs) -> Optional[dict]:
    """Read a resource from the PrestaShop API.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param resource_id: Resource ID.
    :type resource_id: int | str

    :return: Response from the API.
    :rtype: dict
    """
```

**Описание**: Читает ресурс из PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.read('products', 123)
```

### `write`

```python
def write(self, resource: str, data: dict) -> Optional[dict]:
    """Update an existing resource in the PrestaShop API.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param data: Data for the resource.
    :type data: dict

    :return: Response from the API.
    :rtype: dict
    """
```

**Описание**: Обновляет существующий ресурс в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
data = {'id': 123, 'product': {'name': 'Измененный продукт'}}
api.write('products', data)
```

### `unlink`

```python
def unlink(self, resource: str, resource_id: int | str) -> bool:
    """Delete a resource from the PrestaShop API.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param resource_id: Resource ID.
    :type resource_id: int | str

    :return: `True` if successful, `False` otherwise.
    :rtype: bool
    """
```

**Описание**: Удаляет ресурс из PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.unlink('products', 123)
```

### `search`

```python
def search(self, resource: str, filter: Optional[str | dict] = None, **kwargs) -> List[dict]:
    """Search for resources in the PrestaShop API.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param filter: Filter for the search.
    :type filter: str | dict, optional

    :return: List of resources matching the search criteria.
    :rtype: List[dict]
    """
```

**Описание**: Выполняет поиск ресурсов в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.search('products', filter='[name]=%[keyword]%')
```

### `create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """Upload a binary file to a PrestaShop API resource."""
```

**Описание**: Загружает бинарный файл в ресурс PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.create_binary('images/products/22', 'img.jpeg', 'image')
```

### `get_schema`

```python
def get_schema(self, resource: Optional[str] = None, resource_id: Optional[int] = None, schema:Optional[str] = 'blank', **kwards) -> dict | None:
    """! Retrieve the schema of a given resource from PrestaShop API.

    Args:
        `resource` (str): The name of the resource (e.g., 'products', 'customers').
        Если не указана - вернется список всех схем сущностей доступных для API ключа

        `resource_id` (Optinal[str]): 

        `schema` (Optional[str]): обычно подразумеваются следующие опции:

            -   blank: (Самая распространенная опция, как и в вашем коде) 
            Возвращает пустую схему ресурса. Это полезно для определения минимального набора полей, 
            необходимых для создания нового объекта. То есть возвращает структуру XML или JSON с пустыми полями, 
            которые можно заполнить данными.

            -   synopsis (или simplified): В некоторых версиях и для некоторых ресурсов может существовать опция, 
            возвращающая упрощенную схему. Она может содержать только основные поля ресурса и их типы. 
            Это может быть удобнее, чем полная схема, если вам не нужны все детали.

            -   full (или без указания schema): Часто, если параметр schema не указан, 
            или если он указан как full, возвращается полная схема ресурса. Она включает все поля, их типы, 
            возможные значения, описания и другие метаданные. Это самый подробный вид схемы.

            -   form (или что-то подобное): Реже, но может быть опция, возвращающая схему,  
            оптимизированную для отображения в форме редактирования. Она может включать информацию о валидации 
            полей, порядке отображения и т.п.

    Returns:
        dict | None: The schema of the requested resource or `None` in case of an error.
    """
```

**Описание**: Получает схему данного ресурса из PrestaShop API.

**Параметры**:
- `resource` (str, optional): Имя ресурса (например, 'products', 'customers'). Если не указан, возвращается список всех схем сущностей, доступных для API ключа.
- `resource_id` (str, optional): ID ресурса.
- `schema` (str, optional): Тип схемы. Возможные значения: 'blank', 'synopsis', 'full', 'form'. По умолчанию 'blank'.

**Возвращает**:
- `dict | None`: Схема запрошенного ресурса или `None` в случае ошибки.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.get_schema('products', schema='blank')
```

### `get_data`

```python
def get_data(self, resource: str, **kwargs) -> Optional[dict]:
    """Fetch data from a PrestaShop API resource and save it.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param **kwargs: Additional arguments for the API request.

    :return: Data from the API or `False` on failure.
    :rtype: dict | None
    """
```

**Описание**: Получает данные из ресурса PrestaShop API и сохраняет их.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API запроса.

**Возвращает**:
- `dict | None`: Данные от API или `False` в случае неудачи.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.get_data('products', limit='10')
```

### `get_apis`

```python
def get_apis(self) -> Optional[dict]:
    """Get a list of all available APIs.

    :return: List of available APIs.
    :rtype: dict
    """
```

**Описание**: Получает список всех доступных API.

**Возвращает**:
- `dict`: Список доступных API.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.get_apis()
```

### `upload_image_async`

```python
def upload_image_async(self, resource: str, resource_id: int, img_url: str,
                           img_name: Optional[str] = None) -> Optional[dict]:
    """Upload an image to PrestaShop API asynchronously.

    :param resource: API resource (e.g., 'images/products/22').
    :type resource: str
    :param resource_id: Resource ID.
    :type resource_id: int
    :param img_url: URL of the image.
    :type img_url: str
    :param img_name: Name of the image file, defaults to None.
    :type img_name: str, optional

    :return: Response from the API or `False` on failure.
    :rtype: dict | None
    """
```

**Описание**: Асинхронно загружает изображение в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.upload_image_async('images/products/22', 123, 'https://example.com/image.jpg', 'image')
```

### `upload_image_from_url`

```python
def upload_image_from_url(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]:
    """Upload an image to PrestaShop API.

    :param resource: API resource (e.g., 'images/products/22').
    :type resource: str
    :param resource_id: Resource ID.
    :type resource_id: int
    :param img_url: URL of the image.
    :type img_url: str
    :param img_name: Name of the image file, defaults to None.
    :type img_name: str, optional

    :return: Response from the API or `False` on failure.
    :rtype: dict | None
    """
```

**Описание**: Загружает изображение в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.upload_image_from_url('images/products/22', 123, 'https://example.com/image.jpg', 'image')
```

### `get_product_images`

```python
def get_product_images(self, product_id: int) -> Optional[dict]:
    """Get images for a product.

    :param product_id: Product ID.
    :type product_id: int

    :return: List of product images or `False` on failure.
    :rtype: dict | None
    """
```

**Описание**: Получает изображения для продукта.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае неудачи.

**Пример**:
```python
api = PrestaShop(api_key='ключ', api_domain='https://domain.com')
api.get_product_images(123)