# Модуль для взаимодействия с PrestaShop API
## Обзор
Модуль `api.py` предоставляет класс `PrestaShop` для взаимодействия с веб-сервисами PrestaShop API, используя JSON и XML для форматирования сообщений. Он поддерживает операции CRUD, поиск и загрузку изображений, с обработкой ошибок для ответов.

## Подробней

Этот модуль обеспечивает взаимодействие с PrestaShop API, позволяя выполнять различные операции, такие как создание, чтение, обновление и удаление данных, а также поиск и загрузку изображений. Класс `PrestaShop` упрощает взаимодействие с API, предоставляя методы для выполнения запросов и обработки ответов.
Модуль использует библиотеки `requests` для отправки HTTP-запросов, `xml.etree.ElementTree` для работы с XML-данными и `json` для работы с JSON-данными.

## Классы

### `PrestaShop`

**Описание**:
Класс для взаимодействия с PrestaShop API.

**Как работает класс**:
Класс `PrestaShop` инициализируется с ключом API, доменом API, форматом данных, языком по умолчанию и флагом отладки. Он предоставляет методы для выполнения HTTP-запросов к API PrestaShop, обработки ответов и выполнения операций CRUD.

**Методы**:
- `__init__`: Инициализирует класс `PrestaShop` с параметрами подключения к API.
- `ping`: Проверяет работоспособность веб-сервиса.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает сообщение об ошибке из ответа PrestaShop API.
- `_prepare_url`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse_response`: Разбирает XML или JSON ответ от API в структуру dict.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Выполняет поиск ресурсов в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `get_schema`: Получает схему заданного ресурса из PrestaShop API.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их.
- `get_apis`: Получает список всех доступных API.
- `upload_image_async`: Асинхронно загружает изображение в PrestaShop API.
- `upload_image_from_url`: Загружает изображение в PrestaShop API.
- `get_product_images`: Получает изображения для продукта.

---
### `__init__`

```python
def __init__(self,
                api_key:str,
                api_domain:str,
                data_format: str = 'JSON',
                default_lang: int = 1,
                debug: bool = False) -> None:
    """Initialize the PrestaShop class.

    :param data_format: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
    :type data_format: str
    :param default_lang: Default language ID. Defaults to 1.
    :type default_lang: int
    :param debug: Activate debug mode. Defaults to True.
    :type debug: bool
    """
```

**Назначение**:
Инициализация класса `PrestaShop`.

**Как работает функция**:
1. Устанавливает значения атрибутов экземпляра класса, такие как `api_domain`, `api_key`, `debug`, `language` и `data_format` на основе переданных аргументов.
2. Добавляет ключ API в параметры аутентификации клиента (`self.client.auth`).
3. Выполняет HEAD-запрос к API для получения версии PrestaShop и проверки соединения.

**Параметры**:
- `api_key` (str): Ключ API, полученный из PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, `https://myPrestaShop.com`).
- `data_format` (str, optional): Формат данных по умолчанию (`'JSON'` или `'XML'`). По умолчанию `'JSON'`.
- `default_lang` (int, optional): ID языка по умолчанию. По умолчанию `1`.
- `debug` (bool, optional): Флаг отладки. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если ключ API неверен или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

**Примеры**:

```python
api = PrestaShop(
    api_key='your_api_key',
    api_domain='https://your-prestashop-domain.com',
    data_format='JSON',
    default_lang=1,
    debug=True
)
```

---
### `ping`

```python
def ping(self) -> bool:
    """Test if the webservice is working perfectly.

    :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    :rtype: bool
    """
```

**Назначение**:
Проверка работоспособности веб-сервиса.

**Как работает функция**:
1. Выполняет HEAD-запрос к API.
2. Проверяет статус код ответа с помощью `_check_response`.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Примеры**:

```python
is_working = api.ping()
if is_working:
    print('Webservice is working')
else:
    print('Webservice is not working')
```

---
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
```

**Назначение**:
Проверка кода состояния ответа и обработка ошибок.

**Как работает функция**:
1. Проверяет, находится ли `status_code` в диапазоне `(200, 201)`.
2. Если `status_code` не равен `200` или `201`, вызывает функцию `_parse_response_error` для обработки ошибки.

**Параметры**:
- `status_code` (int): HTTP код состояния ответа.
- `response` (requests.Response): Объект HTTP ответа.
- `method` (str, optional): HTTP метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния равен `200` или `201`, иначе `False`.

**Примеры**:

```python
status_code = response.status_code
is_ok = self._check_response(status_code, response)
if is_ok:
    print('Request was successful')
else:
    print('Request failed')
```

---
### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
    """Parse the error response from PrestaShop API.

    :param response: HTTP response object from the server.
    :type response: requests.Response
    """
```

**Назначение**:
Разбор сообщения об ошибке из ответа PrestaShop API.

**Как работает функция**:
1. Проверяет формат данных (`self.data_format`).
2. Если формат данных `'JSON'`:
   - Проверяет код состояния ответа (`response.status_code`).
   - Если код состояния не равен `200` или `201`, логирует сообщение об ошибке, содержащее код состояния, URL запроса, заголовки и текст ответа.
3. Если формат данных не `'JSON'`:
   - Вызывает функцию `_parse_response` для разбора XML ответа.
   - Извлекает код и сообщение об ошибке из XML-структуры.
   - Логирует сообщение об ошибке, содержащее код и сообщение об ошибке.

**Параметры**:
- `response` (requests.Response): Объект HTTP ответа от сервера.
- `method` (str, optional): HTTP метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `requests.Response`: Если формат данных `'JSON'`.
- `tuple[str, str]`: Код и сообщение об ошибке, если формат данных `'XML'`.

**Примеры**:

```python
try:
    response = self.client.get('https://your-prestashop-domain.com/api/nonexistent_resource')
    self._check_response(response.status_code, response)
except Exception as ex:
    self._parse_response_error(response)
```

---
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
```

**Назначение**:
Подготовка URL для запроса.

**Как работает функция**:
1. Создает объект `PreparedRequest`.
2. Подготавливает URL с параметрами, используя метод `req.prepare_url(url, params)`.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Примеры**:

```python
base_url = 'https://your-prestashop-domain.com/api/products'
params = {'display': 'full', 'limit': '1'}
prepared_url = self._prepare_url(base_url, params)
print(prepared_url)
```

---
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
```

**Назначение**:
Выполнение HTTP-запроса к PrestaShop API.

**Как работает функция**:
1. Устанавливает уровень отладки HTTP-соединения.
2. Подготавливает URL для запроса, используя `_prepare_url`.
3. Устанавливает заголовки запроса в зависимости от формата данных (`'JSON'` или `'XML'`).
4. Выполняет HTTP-запрос с использованием `self.client.request`.
5. Проверяет ответ с помощью `_check_response`.
6. Разбирает ответ с помощью `_parse_response`.
7. В случае возникновения исключения, логирует ошибку.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `resource_id` (int | str, optional): ID ресурса.
- `resource_ids` (int | Tuple[int], optional): IDs ресурсов.
- `method` (str, optional): HTTP метод (`'GET'`, `'POST'`, `'PUT'`, `'DELETE'`). По умолчанию `'GET'`.
- `data` (dict | str, optional): Данные для отправки в запросе.
- `headers` (dict, optional): Заголовки запроса.
- `search_filter` (str | dict, optional): Фильтр для поиска.
- `display` (str | list, optional): Поля для отображения. По умолчанию `'full'`.
- `schema` (str, optional): Схема данных.
- `sort` (str, optional): Параметр сортировки.
- `limit` (str, optional): Лимит количества возвращаемых записей.
- `language` (int, optional): ID языка.
- `data_format` (str, optional): Формат данных (`'JSON'` или `'XML'`). По умолчанию `'JSON'`.

**Возвращает**:
- `dict | None`: Разобранные данные из ответа или `None` в случае ошибки.

**Примеры**:

```python
resource = 'products'
resource_id = 1
data = api._exec(resource=resource, resource_id=resource_id, method='GET')
print(data)
```

---
### `_parse_response`

```python
def _parse_response(self, response:Response, data_format:Optional[str] = 'JSON' ) -> dict|None:
    """Parse XML or JSON response from the API to dict structure

    :param text: Response text.
    :type text: str

    :return: Parsed data or `False` on failure.
    :rtype: dict 
    """
```

**Назначение**:
Разбор XML или JSON ответа от API в структуру dict.

**Как работает функция**:
1. Проверяет формат данных (`self.data_format`).
2. Если формат данных `'JSON'`:
   - Разбирает JSON ответ с использованием `response.json()`.
3. Если формат данных `'XML'`:
   - Разбирает XML ответ с использованием `xml2dict(response.text)`.

**Параметры**:
- `response` (requests.Response): Объект HTTP ответа.
- `data_format` (str, optional): Формат данных (`'JSON'` или `'XML'`). По умолчанию `'JSON'`.

**Возвращает**:
- `dict | None`: Разобранные данные или `None` в случае ошибки.

**Примеры**:

```python
response = self.client.get('https://your-prestashop-domain.com/api/products?output_format=JSON')
data = self._parse_response(response)
print(data)
```

---
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

**Назначение**:
Создание нового ресурса в PrestaShop API.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметрами `resource`, `method='POST'` и `data`.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Примеры**:

```python
resource = 'products'
data = {
    'product': {
        'name': [{'language': {'id': '1', 'value': 'Test Product'}}],
        'active': 1,
        'price': 10.00
    }
}
response = api.create(resource, data)
print(response)
```

---
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

**Назначение**:
Чтение ресурса из PrestaShop API.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметрами `resource`, `resource_id` и `method='GET'`.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Примеры**:

```python
resource = 'products'
resource_id = 1
response = api.read(resource, resource_id)
print(response)
```

---
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

**Назначение**:
Обновление существующего ресурса в PrestaShop API.

**Как работает функция**:
1. Извлекает ID ресурса из параметра `data` (`data.get('id')`).
2. Вызывает функцию `_exec` с параметрами `resource`, `resource_id`, `method='PUT'` и `data`.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Примеры**:

```python
resource = 'products'
data = {
    'product': {
        'id': 1,
        'name': [{'language': {'id': '1', 'value': 'Updated Product Name'}}],
        'price': 12.00
    }
}
response = api.write(resource, data)
print(response)
```

---
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

**Назначение**:
Удаление ресурса из PrestaShop API.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметрами `resource`, `resource_id` и `method='DELETE'`.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если удаление успешно, `False` в противном случае.

**Примеры**:

```python
resource = 'products'
resource_id = 1
success = api.unlink(resource, resource_id)
if success:
    print('Resource deleted successfully')
else:
    print('Failed to delete resource')
```

---
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

**Назначение**:
Поиск ресурсов в PrestaShop API.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметрами `resource`, `search_filter=filter` и `method='GET'`.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Примеры**:

```python
resource = 'products'
filter = '[name]=%Test%'
products = api.search(resource, filter=filter)
print(products)
```

---
### `create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """Upload a binary file to a PrestaShop API resource."""
```

**Назначение**:
Загрузка бинарного файла в ресурс PrestaShop API.

**Как работает функция**:
1. Открывает файл по указанному пути (`file_path`) в бинарном режиме для чтения.
2. Формирует словарь `files` для передачи файла в запросе.
3. Отправляет POST-запрос к API с использованием `self.client.post`.
4. Проверяет статус ответа на наличие HTTP-ошибок.
5. Разбирает ответ с помощью `self._parse_response`.
6. В случае возникновения исключения, логирует ошибку.

**Параметры**:
- `resource` (str): API ресурс (например, `'images/products/22'`).
- `file_path` (str): Путь к файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:

```python
resource = 'images/products/22'
file_path = 'img.jpeg'
file_name = 'image'
response = api.create_binary(resource, file_path, file_name)
print(response)
```

---
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

**Назначение**:
Получение схемы заданного ресурса из PrestaShop API.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметрами `resource`, `resource_id`, `schema` и `method='GET'`.

**Параметры**:
- `resource` (str, optional): Имя ресурса (например, `'products'`, `'customers'`). Если не указан, возвращается список всех схем сущностей, доступных для API ключа.
- `resource_id` (int, optional): ID ресурса.
- `schema` (str, optional): Схема данных (`'blank'`, `'synopsis'`, `'full'`, `'form'`). По умолчанию `'blank'`.

**Возвращает**:
- `dict | None`: Схема запрошенного ресурса или `None` в случае ошибки.

**Примеры**:

```python
resource = 'products'
schema = 'blank'
response = api.get_schema(resource=resource, schema=schema)
print(response)
```

---
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

**Назначение**:
Получение данных из ресурса PrestaShop API и их сохранение.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметром `resource` и `method='GET'`.

**Параметры**:
- `resource` (str): API ресурс (например, `'products'`).
- `**kwargs`: Дополнительные аргументы для API запроса.

**Возвращает**:
- `dict | None`: Данные из API или `None` в случае ошибки.

**Примеры**:

```python
resource = 'products'
response = api.get_data(resource=resource, display='full')
print(response)
```

---
### `get_apis`

```python
def get_apis(self) -> Optional[dict]:
    """Get a list of all available APIs.

    :return: List of available APIs.
    :rtype: dict
    """
```

**Назначение**:
Получение списка всех доступных API.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметром `'apis'` и `method='GET'`.

**Параметры**:
- `None`

**Возвращает**:
- `dict`: Список доступных API.

**Примеры**:

```python
apis = api.get_apis()
print(apis)
```

---
### `upload_image_async`

```python
def upload_image_async(self, resource: str, resource_id: int, img_url: str,\
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

**Назначение**:
Асинхронная загрузка изображения в PrestaShop API.

**Как работает функция**:
1. Разделяет URL изображения на имя файла и расширение.
2. Формирует имя файла.
3. Сохраняет изображение с использованием `save_image_from_url`.
4. Загружает изображение с использованием `self.create_binary`.
5. Удаляет временный файл изображения.

**Параметры**:
- `resource` (str): API ресурс (например, `'images/products/22'`).
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `None` в случае ошибки.

**Примеры**:

```python
resource = 'images/products/22'
resource_id = 22
img_url = 'https://example.com/image.jpg'
img_name = 'product_image'
response = api.upload_image_async(resource, resource_id, img_url, img_name)
print(response)
```

---
### `upload_image_from_url`

```python
def upload_image_from_url(self, resource: str, resource_id: int, img_url: str,\
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

**Назначение**:
Загрузка изображения в PrestaShop API.

**Как работает функция**:
1. Разделяет URL изображения на имя файла и расширение.
2. Формирует имя файла.
3. Сохраняет изображение с использованием `save_image_from_url`.
4. Загружает изображение с использованием `self.create_binary`.
5. Удаляет временный файл изображения.

**Параметры**:
- `resource` (str): API ресурс (например, `'images/products/22'`).
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `None` в случае ошибки.

**Примеры**:

```python
resource = 'images/products/22'
resource_id = 22
img_url = 'https://example.com/image.jpg'
img_name = 'product_image'
response = api.upload_image_from_url(resource, resource_id, img_url, img_name)
print(response)
```

---
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

**Назначение**:
Получение изображений для продукта.

**Как работает функция**:
1. Вызывает функцию `_exec` с параметром `f'products/{product_id}/images'` и `method='GET'`.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `None` в случае ошибки.

**Примеры**:

```python
product_id = 22
images = api.get_product_images(product_id)
print(images)
```
---
## Функции

### `get`
```python
def get(resource):
    """"""
```

**Назначение**:
Пустая функция get.

**Как работает функция**:
Не выполняет никаких действий, так как тело функции отсутствует.

**Параметры**:
- `resource` (str): Имя ресурса.

**Возвращает**:
- `None`

**Примеры**:
```python
get('products')
```
---

### `main`
```python
def main():
    """"""
```

**Назначение**:
Пустая функция main.

**Как работает функция**:
Не выполняет никаких действий, так как тело функции отсутствует.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Примеры**:
```python
main()
```