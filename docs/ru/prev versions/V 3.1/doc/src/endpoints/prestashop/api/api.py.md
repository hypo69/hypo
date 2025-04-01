# Модуль api.py

## Обзор

Модуль `api.py` предоставляет класс `PrestaShop` для взаимодействия с API PrestaShop. Он использует JSON и XML для форматирования сообщений и поддерживает CRUD операции, поиск и загрузку изображений. Модуль также включает обработку ошибок.

## Подробней

Этот модуль позволяет взаимодействовать с PrestaShop webservice API, используя класс `PrestaShop`. Он поддерживает операции CRUD, поиск и загрузку изображений, а также предоставляет обработку ошибок для ответов.
Класс `PrestaShop` инициализируется с ключом API, доменом API, форматом данных, языком по умолчанию и режимом отладки. Он предоставляет методы для выполнения HTTP-запросов к API PrestaShop, обработки ответов и разбора данных.

Расположение файла в проекте: `hypotez/src/endpoints/prestashop/api/api.py` указывает, что этот модуль отвечает за взаимодействие с API PrestaShop и является частью подсистемы, отвечающей за интеграцию с PrestaShop.

## Классы

### `PrestaShop`

**Описание**: Класс для взаимодействия с PrestaShop webservice API, использующий JSON и XML для обмена сообщениями.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShop`.
- `ping`: Проверяет, работает ли веб-сервис.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от PrestaShop API.
- `_prepare_url`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse_response`: Разбирает XML или JSON ответ от API в структуру dict.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Ищет ресурсы в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `get_schema`: Получает схему заданного ресурса из PrestaShop API.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их.
- `get_apis`: Получает список всех доступных API.
- `upload_image_async`: Асинхронно загружает изображение в PrestaShop API.
- `upload_image_from_url`: Загружает изображение в PrestaShop API.
- `get_product_images`: Получает изображения для продукта.

**Параметры**:
- `api_key` (str): Ключ API, полученный из PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию `False`.

**Примеры**:
```python
from src.endpoints.prestashop.api.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)
```

## Функции

### `ping`

```python
def ping(self) -> bool:
    """Test if the webservice is working perfectly.

    :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    :rtype: bool
    """
    ...
```

**Описание**: Проверяет, работает ли веб-сервис.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
is_working = api.ping()
print(is_working)
```

### `_check_response`

```python
def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
                    headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
    """Check the response status code and handle errors.

    :param status_code: HTTP response status code.
    :type status_code: int
    :param response: HTTP response object.
    :type response: requests.Response
    :param method: HTTP method used for the request.
    :type method: str, optional
    :param url: The URL of the request.
    :type url: str, optional
    :param headers: The headers used in the request.
    :type headers: dict, optional
    :param data: The data sent in the request.
    :type data: dict, optional

    :return: `True` if the status code is 200 or 201, otherwise `False`.
    :rtype: bool
    """
    ...
```

**Описание**: Проверяет код состояния ответа и обрабатывает ошибки.

**Параметры**:
- `status_code` (int): HTTP код состояния ответа.
- `response`: Объект HTTP ответа.
- `method` (Optional[str], optional): HTTP метод, использованный для запроса.
- `url` (Optional[str], optional): URL запроса.
- `headers` (Optional[dict], optional): Заголовки, использованные в запросе.
- `data` (Optional[dict], optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = requests.get('https://your-prestashop-domain.com/api/')
is_ok = api._check_response(response.status_code, response)
print(is_ok)
```

### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                          headers: Optional[dict] = None, data: Optional[dict] = None):
    """Parse the error response from PrestaShop API.

    :param response: HTTP response object from the server.
    :type response: requests.Response
    """
    ...
```

**Описание**: Разбирает ответ об ошибке от PrestaShop API.

**Параметры**:
- `response`: Объект HTTP ответа от сервера.
- `method` (Optional[str], optional): HTTP метод, использованный для запроса.
- `url` (Optional[str], optional): URL запроса.
- `headers` (Optional[dict], optional): Заголовки, использованные в запросе.
- `data` (Optional[dict], optional): Данные, отправленные в запросе.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = requests.get('https://your-prestashop-domain.com/api/')
api._parse_response_error(response)
```

### `_prepare_url`

```python
def _prepare_url(self, url: str, params: dict) -> str:
    """Prepare the URL for the request.

    :param url: The base URL.
    :type url: str
    :param params: The parameters for the request.
    :type params: dict

    :return: The prepared URL with parameters.
    :rtype: str
    """
    ...
```

**Описание**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
url = 'https://your-prestashop-domain.com/api/products'
params = {'display': 'full', 'limit': '3'}
prepared_url = api._prepare_url(url, params)
print(prepared_url)
```

### `_exec`

```python
def _exec(self,
      resource: str,
      resource_id: Optional[int| str] = None,
      resource_ids: Optional[int | Tuple[int]] = None,
      method: str = 'GET',
      data: Optional[dict | str] = None,
      headers: Optional[dict] = None,
      search_filter: Optional[str | dict] = None,
      display: Optional[str | list] = 'full',
      schema: Optional[str] = None,
      sort: Optional[str] = None,
      limit: Optional[str] = None,
      language: Optional[int] = None,
      data_format: str = 'JSON') -> Optional[dict]:
    """Execute an HTTP request to the PrestaShop API."""
    ...
```

**Описание**: Выполняет HTTP-запрос к PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (Optional[int  |  str], optional): ID ресурса.
- `resource_ids` (Optional[int | Tuple[int]], optional): IDs ресурсов.
- `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE). По умолчанию 'GET'.
- `data` (Optional[dict | str], optional): Данные для отправки.
- `headers` (Optional[dict], optional): Заголовки запроса.
- `search_filter` (Optional[str | dict], optional): Фильтр для поиска.
- `display` (Optional[str | list], optional): Поля для отображения. По умолчанию 'full'.
- `schema` (Optional[str], optional): Схема ресурса.
- `sort` (Optional[str], optional): Параметр сортировки.
- `limit` (Optional[str], optional): Лимит количества возвращаемых записей.
- `language` (Optional[int], optional): ID языка.
- `data_format` (str, optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
data = api._exec(resource=resource, method='GET', limit='3')
print(data)
```

### `_parse_response`

```python
def _parse_response(self, response:Response, data_format:Optional[str] = 'JSON' ) -> dict|None:
    """Parse XML or JSON response from the API to dict structure

    :param text: Response text.
    :type text: str

    :return: Parsed data or `False` on failure.
    :rtype: dict 
    """
    ...
```

**Описание**: Разбирает XML или JSON ответ от API в структуру dict.

**Параметры**:
- `response` (Response): Объект HTTP ответа.
- `data_format` (Optional[str], optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `dict|None`: Разобранные данные.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = requests.get('https://your-prestashop-domain.com/api/products')
data = api._parse_response(response)
print(data)
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
    ...
```

**Описание**: Создает новый ресурс в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'taxes'
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
response = api.create(resource, data)
print(response)
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
    ...
```

**Описание**: Читает ресурс из PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
resource_id = 1
response = api.read(resource, resource_id)
print(response)
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
    ...
```

**Описание**: Обновляет существующий ресурс в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'taxes'
data = {
    'tax': {
        'id': '1',
        'rate': 5.000,
        'active': '1',
        'name': {
            'language': {
                'attrs': {'id': '1'},
                'value': '5% tax'
            }
        }
    }
}
response = api.write(resource, data)
print(response)
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
    ...
```

**Описание**: Удаляет ресурс из PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'taxes'
resource_id = 1
success = api.unlink(resource, resource_id)
print(success)
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
    ...
```

**Описание**: Ищет ресурсы в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (Optional[str | dict], optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'taxes'
filter = '[name]=%[5]%'
results = api.search(resource, filter=filter, limit='3')
print(results)
```

### `create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """Upload a binary file to a PrestaShop API resource."""
    ...
```

**Описание**: Загружает бинарный файл в ресурс PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'images/products/22'
file_path = 'img.jpeg'
file_name = 'image'
response = api.create_binary(resource, file_path, file_name)
print(response)
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
    ...
```

**Описание**: Получает схему заданного ресурса из PrestaShop API.

**Параметры**:
- `resource` (Optional[str], optional): Имя ресурса (например, 'products', 'customers'). Если не указан - вернется список всех схем сущностей, доступных для API ключа.
- `resource_id` (Optional[int], optional): ID ресурса.
- `schema` (Optional[str], optional): Схема ресурса ('blank', 'synopsis', 'full', 'form'). По умолчанию 'blank'.

**Возвращает**:
- `dict | None`: Схема запрошенного ресурса или `None` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
schema = api.get_schema(resource=resource, schema='blank')
print(schema)
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
    ...
```

**Описание**: Получает данные из ресурса PrestaShop API и сохраняет их.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API запроса.

**Возвращает**:
- `dict | None`: Данные из API или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
data = api.get_data(resource=resource, limit='3')
print(data)
```

### `get_apis`

```python
def get_apis(self) -> Optional[dict]:
    """Get a list of all available APIs.

    :return: List of available APIs.
    :rtype: dict
    """
    ...
```

**Описание**: Получает список всех доступных API.

**Возвращает**:
- `dict`: Список доступных API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
apis = api.get_apis()
print(apis)
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
    ...
```

**Описание**: Асинхронно загружает изображение в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'images/products/22'
resource_id = 22
img_url = 'https://example.com/image.jpg'
response = api.upload_image_async(resource, resource_id, img_url)
print(response)
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
    ...
```

**Описание**: Загружает изображение в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'images/products/22'
resource_id = 22
img_url = 'https://example.com/image.jpg'
response = api.upload_image_from_url(resource, resource_id, img_url)
print(response)
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
    ...
```

**Описание**: Получает изображения для продукта.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
product_id = 22
images = api.get_product_images(product_id)
print(images)