# Модуль для взаимодействия с API PrestaShop

## Обзор

Модуль предоставляет класс `PrestaShop` для взаимодействия с API PrestaShop, используя JSON и XML для форматирования сообщений. Он поддерживает операции CRUD, поиск и загрузку изображений, а также обработку ошибок для ответов.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с PrestaShop API. Он предоставляет удобные методы для выполнения различных операций, таких как создание, чтение, обновление и удаление ресурсов, а также для поиска и загрузки изображений. Класс `PrestaShop` абстрагирует детали реализации API, позволяя разработчикам сосредоточиться на бизнес-логике.

## Классы

### `PrestaShop`

**Описание**: Класс для взаимодействия с API PrestaShop.

**Как работает класс**: Класс инициализируется с использованием ключа API, домена API, формата данных, языка по умолчанию и режима отладки. Он предоставляет методы для выполнения различных операций с API PrestaShop, таких как создание, чтение, обновление и удаление ресурсов, а также для поиска и загрузки изображений. Класс также обрабатывает ошибки API и возвращает соответствующие ответы.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShop`.
- `ping`: Проверяет, работает ли веб-сервис.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от API PrestaShop.
- `_prepare_url`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к API PrestaShop.
- `_parse_response`: Разбирает ответ XML или JSON от API в структуру dict.
- `create`: Создает новый ресурс в API PrestaShop.
- `read`: Читает ресурс из API PrestaShop.
- `write`: Обновляет существующий ресурс в API PrestaShop.
- `unlink`: Удаляет ресурс из API PrestaShop.
- `search`: Выполняет поиск ресурсов в API PrestaShop.
- `create_binary`: Загружает двоичный файл в ресурс API PrestaShop.
- `get_schema`: Получает схему данного ресурса из API PrestaShop.
- `get_data`: Извлекает данные из ресурса API PrestaShop и сохраняет их.
- `get_apis`: Получает список всех доступных API.
- `upload_image_async`: Асинхронно загружает изображение в API PrestaShop.
- `upload_image_from_url`: Загружает изображение в API PrestaShop.
- `get_product_images`: Получает изображения для продукта.

**Параметры**:
- `api_key` (str): Ключ API, сгенерированный из PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): Идентификатор языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию `False`.
- `client` (Session): HTTP клиент сессии для выполнения запросов.

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

**Как работает функция**: Функция выполняет HTTP-запрос `HEAD` к домену API и проверяет код состояния ответа. Если код состояния 200 или 201, функция возвращает `True`, что указывает на то, что веб-сервис работает. В противном случае функция возвращает `False`.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
if api.ping():
    print('Веб-сервис работает')
else:
    print('Веб-сервис не работает')
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

**Как работает функция**: Функция проверяет, находится ли код состояния HTTP ответа в диапазоне 200 или 201. Если это так, функция возвращает `True`, что указывает на то, что запрос был успешным. В противном случае функция вызывает `_parse_response_error` для обработки ошибки и возвращает `False`.

**Параметры**:
- `status_code` (int): Код состояния HTTP ответа.
- `response` (requests.Response): Объект HTTP ответа.
- `method` (Optional[str], optional): HTTP метод, использованный для запроса.
- `url` (Optional[str], optional): URL запроса.
- `headers` (Optional[dict], optional): Заголовки, использованные в запросе.
- `data` (Optional[dict], optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.client.get('https://your-prestashop-domain.com/api/products')
if api._check_response(response.status_code, response):
    print('Запрос успешен')
else:
    print('Произошла ошибка')
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

**Описание**: Разбирает ответ об ошибке от API PrestaShop.

**Как работает функция**: Функция разбирает ответ об ошибке от API PrestaShop, извлекая код ошибки и сообщение об ошибке. Если формат данных JSON, функция извлекает информацию об ошибке из JSON-ответа. Если формат данных XML, функция использует `xml2dict` для преобразования XML-ответа в словарь, а затем извлекает информацию об ошибке. Затем функция регистрирует сообщение об ошибке, используя модуль `logger`.

**Параметры**:
- `response` (requests.Response): Объект HTTP ответа от сервера.
- `method` (Optional[str], optional): HTTP метод, использованный для запроса.
- `url` (Optional[str], optional): URL запроса.
- `headers` (Optional[dict], optional): Заголовки, использованные в запросе.
- `data` (Optional[dict], optional): Данные, отправленные в запросе.

**Примеры**:

```python
from src.logger.logger import logger
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.client.get('https://your-prestashop-domain.com/api/nonexistent_resource')
try:
    api._check_response(response.status_code, response)
except Exception as ex:
    logger.error('Ошибка при разборе ответа', ex, exc_info=True)
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

**Как работает функция**: Функция принимает базовый URL и словарь параметров. Она использует `PreparedRequest` из библиотеки `requests` для подготовки URL с параметрами. Подготовленный URL возвращается в виде строки.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
url = 'https://your-prestashop-domain.com/api/products'
params = {'display': 'full', 'limit': '1'}
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

**Описание**: Выполняет HTTP-запрос к API PrestaShop.

**Как работает функция**: Функция выполняет HTTP-запрос к API PrestaShop, используя указанные параметры. Она принимает ресурс, идентификатор ресурса, метод HTTP, данные, заголовки, фильтр поиска, параметры отображения, схему, параметры сортировки, лимит, язык и формат данных. Функция подготавливает URL, устанавливает заголовки запроса и выполняет запрос, используя HTTP-клиент. Затем функция проверяет ответ и разбирает его, возвращая данные в виде словаря.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (Optional[int | str], optional): Идентификатор ресурса.
- `resource_ids` (Optional[int | Tuple[int]], optional): Идентификаторы ресурсов.
- `method` (str, optional): HTTP метод (например, 'GET', 'POST', 'PUT', 'DELETE'). По умолчанию 'GET'.
- `data` (Optional[dict | str], optional): Данные для отправки в запросе.
- `headers` (Optional[dict], optional): Заголовки запроса.
- `search_filter` (Optional[str | dict], optional): Фильтр для поиска.
- `display` (Optional[str | list], optional): Параметры отображения. По умолчанию 'full'.
- `schema` (Optional[str], optional): Схема ресурса.
- `sort` (Optional[str], optional): Параметры сортировки.
- `limit` (Optional[str], optional): Лимит количества возвращаемых ресурсов.
- `language` (Optional[int], optional): Идентификатор языка.
- `data_format` (str, optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `Optional[dict]`: Данные ответа в виде словаря или `None` в случае ошибки.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
resource_id = 1
data = api._exec(resource=resource, resource_id=resource_id, method='GET')
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

**Описание**: Разбирает ответ XML или JSON от API в структуру dict.

**Как работает функция**: Функция принимает текст ответа и пытается разобрать его как JSON или XML, в зависимости от формата данных. Если формат данных JSON, функция использует `json.loads` для разбора текста. Если формат данных XML, функция использует `xml2dict` для преобразования XML в словарь. Затем функция возвращает разобранные данные.

**Параметры**:
- `response` (Response): Объект ответа HTTP.
- `data_format` (Optional[str], optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `dict | None`: Разобранные данные или `False` в случае неудачи.

**Примеры**:

```python
import requests
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = requests.get('https://your-prestashop-domain.com/api/products?output_format=JSON')
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

**Описание**: Создает новый ресурс в API PrestaShop.

**Как работает функция**: Функция принимает ресурс и данные для нового ресурса. Затем она вызывает метод `_exec` с методом 'POST' для создания нового ресурса в API PrestaShop.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
data = {
    'product': {
        'name': [{'language': {'id': '1', 'value': 'Новый продукт'}}],
        'active': '1',
        'price': '10.00',
        'id_category_default': '2'
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

**Описание**: Читает ресурс из API PrestaShop.

**Как работает функция**: Функция принимает ресурс и идентификатор ресурса. Затем она вызывает метод `_exec` с методом 'GET' для чтения ресурса из API PrestaShop.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): Идентификатор ресурса.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

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

**Описание**: Обновляет существующий ресурс в API PrestaShop.

**Как работает функция**: Функция принимает ресурс и данные для ресурса. Затем она вызывает метод `_exec` с методом 'PUT' для обновления ресурса в API PrestaShop.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
data = {
    'product': {
        'id': '1',
        'name': [{'language': {'id': '1', 'value': 'Обновленный продукт'}}],
        'active': '1',
        'price': '12.00',
        'id_category_default': '2'
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

**Описание**: Удаляет ресурс из API PrestaShop.

**Как работает функция**: Функция принимает ресурс и идентификатор ресурса. Затем она вызывает метод `_exec` с методом 'DELETE' для удаления ресурса из API PrestaShop.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): Идентификатор ресурса.

**Возвращает**:
- `bool`: `True`, если удаление успешно, `False` иначе.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
resource_id = 1
response = api.unlink(resource, resource_id)
print(response)
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

**Описание**: Выполняет поиск ресурсов в API PrestaShop.

**Как работает функция**: Функция принимает ресурс и фильтр для поиска. Затем она вызывает метод `_exec` с методом 'GET' и фильтром поиска для выполнения поиска в API PrestaShop.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (Optional[str | dict], optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
filter = '[name]=%Новый%'
response = api.search(resource, filter=filter)
print(response)
```

### `create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """Upload a binary file to a PrestaShop API resource."""
    ...
```

**Описание**: Загружает двоичный файл в ресурс API PrestaShop.

**Как работает функция**: Функция принимает ресурс, путь к файлу и имя файла. Затем она открывает файл в двоичном режиме и отправляет его в API PrestaShop с использованием метода POST.

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
file_name = 'img.jpeg'
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

**Описание**: Получает схему данного ресурса из API PrestaShop.

**Как работает функция**: Функция отправляет запрос к API PrestaShop для получения схемы указанного ресурса. В зависимости от значения параметра `schema`, функция может вернуть пустую схему, упрощенную схему или полную схему ресурса.

**Параметры**:
- `resource` (Optional[str], optional): Имя ресурса (например, 'products', 'customers'). Если не указано, возвращается список всех схем сущностей, доступных для ключа API.
- `resource_id` (Optional[int], optional): Идентификатор ресурса.
- `schema` (Optional[str], optional): Тип схемы ('blank', 'synopsis', 'full'). По умолчанию 'blank'.

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

**Описание**: Извлекает данные из ресурса API PrestaShop и сохраняет их.

**Как работает функция**: Функция отправляет GET-запрос к API PrestaShop для получения данных из указанного ресурса.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API-запроса.

**Возвращает**:
- `dict | None`: Данные из API или `False` в случае неудачи.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
resource = 'products'
data = api.get_data(resource=resource, display='full')
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

**Как работает функция**: Функция отправляет GET-запрос к API PrestaShop для получения списка всех доступных API.

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

**Описание**: Асинхронно загружает изображение в API PrestaShop.

**Как работает функция**: Функция асинхронно загружает изображение в API PrestaShop, используя URL изображения.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): Идентификатор ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

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

**Описание**: Загружает изображение в API PrestaShop.

**Как работает функция**: Функция загружает изображение в API PrestaShop, используя URL изображения.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): Идентификатор ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

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

**Как работает функция**: Функция получает изображения для продукта, используя идентификатор продукта.

**Параметры**:
- `product_id` (int): Идентификатор продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае неудачи.

**Примеры**:

```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
product_id = 22
images = api.get_product_images(product_id)
print(images)