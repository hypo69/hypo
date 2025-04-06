# Модуль для взаимодействия с PrestaShop API

## Обзор

Модуль `src.endpoints.prestashop.api` предоставляет класс `PrestaShop` для взаимодействия с PrestaShop webservice API. Он использует JSON и XML для форматирования сообщений и поддерживает CRUD операции, поиск и загрузку изображений.

## Подробнее

Этот модуль предназначен для упрощения взаимодействия с API PrestaShop, предоставляя удобный интерфейс для выполнения различных операций, таких как создание, чтение, обновление и удаление данных, а также загрузка изображений. Модуль обеспечивает обработку ошибок и поддержку различных форматов данных (JSON и XML).

## Классы

### `Config`

**Описание**: Класс конфигурации для API PrestaShop.

**Принцип работы**: Класс `Config` определяет параметры конфигурации, такие как язык, версия PrestaShop, режим работы (разработка, продакшн), формат данных, домен API и ключ API. Он использует переменные окружения, если `USE_ENV` установлен в `True`, в противном случае использует значения по умолчанию в зависимости от режима работы.

**Аттрибуты**:

- `language` (str): Язык.
- `ps_version` (str): Версия PrestaShop (по умолчанию \'\').
- `MODE` (str): Определяет конечную точку API (`dev`, `dev8`, `prod`).
- `POST_FORMAT` (str): Формат POST запросов (по умолчанию \'XML\').
- `API_DOMAIN` (str): Домен API.
- `API_KEY` (str): Ключ API.

### `PrestaShop`

**Описание**: Класс для взаимодействия с PrestaShop webservice API.

**Принцип работы**: Класс `PrestaShop` инициализируется с использованием ключа API, домена API, формата данных, идентификатора языка по умолчанию и флага отладки. Он предоставляет методы для выполнения HTTP-запросов к API PrestaShop, обработки ответов и разбора данных. Поддерживает CRUD операции, поиск и загрузку изображений.

**Аттрибуты**:

- `client` (Session): HTTP клиентская сессия.
- `debug` (bool): Флаг отладки.
- `language` (Optional[int]): Идентификатор языка.
- `data_format` (str): Формат данных ('JSON' или 'XML').
- `ps_version` (str): Версия PrestaShop.
- `api_domain` (str): Домен API.
- `api_key` (str): Ключ API.

**Методы**:

- `__init__(api_key: str, api_domain: str, data_format: str = 'JSON', default_lang: int = 1, debug: bool = False) -> None`: Инициализация класса `PrestaShop`.
- `ping() -> bool`: Проверяет работоспособность веб-сервиса.
- `_check_response(status_code: int, response: requests.Response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None) -> bool`: Проверяет код состояния HTTP-ответа и обрабатывает ошибки.
- `_parse_response_error(response: requests.Response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None) -> None`: Разбирает ответ об ошибке от API PrestaShop.
- `_prepare_url(url: str, params: dict) -> str`: Подготавливает URL для запроса.
- `_exec(resource: str, resource_id: Optional[int  |  str] = None, resource_ids: Optional[int  |  Tuple[int]] = None, method: str = 'GET', data: Optional[dict  |  str] = None, headers: Optional[dict] = None, search_filter: Optional[str  |  dict] = None, display: Optional[str  |  list] = 'full', schema: Optional[str] = None, sort: Optional[str] = None, limit: Optional[str] = None, language: Optional[int] = None, data_format: str = 'JSON') -> Optional[dict]`: Выполняет HTTP-запрос к API PrestaShop.
- `_parse_response(response: Response, data_format: Optional[str] = 'JSON') -> dict  |  None`: Разбирает ответ XML или JSON от API в структуру dict.
- `create(resource: str, data: dict, *args, **kwards) -> Optional[dict]`: Создает новый ресурс в API PrestaShop.
- `read(resource: str, resource_id: int  |  str, **kwargs) -> Optional[dict]`: Читает ресурс из API PrestaShop.
- `write(resource: str, data: dict) -> Optional[dict]`: Обновляет существующий ресурс в API PrestaShop.
- `unlink(resource: str, resource_id: int  |  str) -> bool`: Удаляет ресурс из API PrestaShop.
- `search(resource: str, filter: Optional[str  |  dict] = None, **kwargs) -> List[dict]`: Поиск ресурсов в API PrestaShop.
- `create_binary(resource: str, file_path: str, file_name: str) -> dict`: Загружает бинарный файл в ресурс API PrestaShop.
- `get_schema(resource: Optional[str] = None, resource_id: Optional[int] = None, schema: Optional[str] = 'blank', **kwards) -> dict  |  None`: Получает схему данного ресурса из API PrestaShop.
- `get_data(resource: str, **kwargs) -> Optional[dict]`: Извлекает данные из ресурса API PrestaShop и сохраняет их.
- `get_apis() -> Optional[dict]`: Получает список всех доступных API.
- `upload_image_async(resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]`: Асинхронно загружает изображение в API PrestaShop.
- `upload_image_from_url(resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]`: Загружает изображение в API PrestaShop.
- `get_product_images(product_id: int) -> Optional[dict]`: Получает изображения для продукта.

## Функции

### `main`

```python
def main() -> None:
    """Проверка сущностей Prestashop"""
```

**Назначение**: Функция `main` предназначена для проверки функциональности API PrestaShop.

**Как работает функция**:
1. **Определение данных для создания налога**:
   - Создается словарь `data`, представляющий структуру данных для налога (tax) с указанием ставки, активности и наименования.
2. **Инициализация API PrestaShop**:
   - Создается экземпляр класса `PrestaShop` с использованием параметров конфигурации из класса `Config`, таких как домен API и ключ API.
3. **Создание и запись налога**:
   - Вызываются методы `api.create()` и `api.write()` для создания и записи данных о налоге в PrestaShop.

**Примеры**:
```python
    data: dict = {
        'tax': {
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax',
                }
            },
        }
    }
    api: PrestaShop = PrestaShop(
        api_domain = Config.API_DOMAIN,
        api_key = Config.API_KEY,
        default_lang = 1,
        debug = True,
        data_format = Config.POST_FORMAT,
    )
    api.create('taxes', data)
    api.write('taxes', data)
```

### `PrestaShop.__init__`

```python
def __init__(
        self,
        api_key: str,
        api_domain: str,
        data_format: str = 'JSON',
        default_lang: int = 1,
        debug: bool = False,
    ) -> None:
        """Initialize the PrestaShop class.

        Args:
            data_format (str): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
            default_lang (int): Default language ID. Defaults to 1.
            debug (bool): Activate debug mode. Defaults to True.
        """
```

**Назначение**: Инициализирует класс `PrestaShop` с заданными параметрами.

**Как работает функция**:
1. **Инициализация атрибутов**:
   - Устанавливает значения атрибутов экземпляра класса `api_domain`, `api_key`, `debug`, `language` и `data_format` на основе переданных аргументов.
2. **Аутентификация клиента**:
   - Если HTTP клиентская сессия не аутентифицирована, устанавливает аутентификацию клиента, используя API ключ.
3. **Проверка соединения**:
   - Выполняет HEAD-запрос к API домену для проверки соединения. Логирует ошибку, если соединение отсутствует.
4. **Получение версии PrestaShop**:
   - Получает версию PrestaShop из заголовков ответа.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
```

### `PrestaShop.ping`

```python
def ping(self) -> bool:
        """Test if the webservice is working perfectly.

        Returns:
            bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        """
```

**Назначение**: Проверяет, работает ли веб-сервис.

**Как работает функция**:

1. **Выполнение HEAD-запроса**:
   - Выполняет HEAD-запрос к API домену.
2. **Проверка ответа**:
   - Вызывает метод `_check_response` для проверки статуса ответа. Возвращает `True`, если статус код 200 или 201, иначе `False`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
api.ping()
```

### `PrestaShop._check_response`

```python
def _check_response(
        self,
        status_code: int,
        response: requests.Response,
        method: Optional[str] = None,
        url: Optional[str] = None,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
    ) -> bool:
        """Check the response status code and handle errors.

        Args:
            status_code (int): HTTP response status code.
            response (requests.Response): HTTP response object.
            method (Optional[str]): HTTP method used for the request.
            url (Optional[str]): The URL of the request.
            headers (Optional[dict]): The headers used in the request.
            data (Optional[dict]): The data sent in the request.

        Returns:
            bool: `True` if the status code is 200 or 201, otherwise `False`.
        """
```

**Назначение**: Проверяет код состояния HTTP-ответа и обрабатывает ошибки.

**Как работает функция**:

1. **Проверка статуса кода**:
   - Проверяет, входит ли `status_code` в список (200, 201). Если да, возвращает `True`.
2. **Обработка ошибок**:
   - Если `status_code` не входит в список (200, 201), вызывает метод `_parse_response_error` для разбора ответа об ошибке и возвращает `False`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
response = api.client.request(method='GET', url=api.api_domain)
api._check_response(response.status_code, response)
```

### `PrestaShop._parse_response_error`

```python
def _parse_response_error(
        self,
        response: requests.Response,
        method: Optional[str] = None,
        url: Optional[str] = None,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
    ) -> None:
        """Parse the error response from PrestaShop API.

        Args:
            response (requests.Response): HTTP response object from the server.
        """
```

**Назначение**: Разбирает ответ об ошибке от API PrestaShop.

**Как работает функция**:

1. **Обработка JSON формата**:
   - Если `data_format` равен `'JSON'`, получает `status_code` и, если он не равен 200 или 201, логирует сообщение об ошибке, содержащее информацию о статусе коде, URL, заголовках и теле ответа.
2. **Обработка XML формата**:
   - Если `data_format` не равен `'JSON'`, вызывает метод `_parse_response` для разбора ответа. Извлекает код и сообщение об ошибке из XML структуры и логирует их.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
response = api.client.request(method='GET', url=api.api_domain + '/nonexistent_resource')
api._parse_response_error(response)
```

### `PrestaShop._prepare_url`

```python
def _prepare_url(self, url: str, params: dict) -> str:
        """Prepare the URL for the request.

        Args:
            url (str): The base URL.
            params (dict): The parameters for the request.

        Returns:
            str: The prepared URL with parameters.
        """
```

**Назначение**: Подготавливает URL для запроса, добавляя параметры к базовому URL.

**Как работает функция**:
1. **Создание объекта PreparedRequest**:
   - Создает экземпляр класса `PreparedRequest`.
2. **Подготовка URL**:
   - Вызывает метод `prepare_url` объекта `PreparedRequest` для добавления параметров к базовому URL.
3. **Возврат подготовленного URL**:
   - Возвращает подготовленный URL.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
url = api.api_domain + '/products'
params = {'display': 'full', 'limit': '1'}
prepared_url = api._prepare_url(url, params)
print(prepared_url)
```

### `PrestaShop._exec`

```python
def _exec(
        self,
        resource: str,
        resource_id: Optional[int  |  str] = None,
        resource_ids: Optional[int  |  Tuple[int]] = None,
        method: str = 'GET',
        data: Optional[dict  |  str] = None,
        headers: Optional[dict] = None,
        search_filter: Optional[str  |  dict] = None,
        display: Optional[str  |  list] = 'full',
        schema: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[str] = None,
        language: Optional[int] = None,
        data_format: str = 'JSON',
    ) -> Optional[dict]:
        """Execute an HTTP request to the PrestaShop API."""
```

**Назначение**: Выполняет HTTP-запрос к API PrestaShop.

**Как работает функция**:

1. **Настройка уровня отладки HTTP соединения**:
   - Устанавливает уровень отладки HTTP соединения на основе атрибута `debug`.
2. **Подготовка URL**:
   - Подготавливает URL для запроса, используя метод `_prepare_url`.
3. **Определение заголовков запроса**:
   - Определяет заголовки запроса в зависимости от формата данных (`JSON` или `XML`).
4. **Выполнение запроса**:
   - Выполняет HTTP-запрос с использованием метода `client.request`.
5. **Проверка ответа**:
   - Проверяет ответ, используя метод `_check_response`. В случае ошибки логирует информацию об ошибке и возвращает `False`.
6. **Разбор ответа**:
   - Разбирает ответ, используя метод `_parse_response`, и возвращает результат.
7. **Обработка исключений**:
   - Перехватывает исключения и логирует их.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
response = api._exec(resource=resource, method='GET')
print(response)
```

### `PrestaShop._parse_response`

```python
def _parse_response(self, response: Response, data_format: Optional[str] = 'JSON') -> dict  |  None:
        """Parse XML or JSON response from the API to dict structure

        Args:
            text (str): Response text.

        Returns:
            dict: Parsed data or `False` on failure.
        """
```

**Назначение**: Разбирает ответ XML или JSON от API в структуру dict.

**Как работает функция**:

1. **Определение формата данных**:
   - Определяет формат данных, используя атрибут `data_format`.
2. **Разбор ответа**:
   - Если формат данных `'JSON'`, разбирает JSON ответ с помощью метода `response.json()`.
   - Если формат данных `'XML'`, разбирает XML ответ с помощью функции `xml2dict`.
3. **Извлечение данных**:
   - Извлекает данные из структуры, используя ключ `'prestashop'`, если он присутствует.
4. **Обработка исключений**:
   - Перехватывает исключения и логирует их. Возвращает пустой словарь `{}` в случае ошибки.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
response = api.client.request(method='GET', url=api.api_domain + '/products')
parsed_data = api._parse_response(response)
print(parsed_data)
```

### `PrestaShop.create`

```python
def create(self, resource: str, data: dict, *args, **kwards) -> Optional[dict]:
        """Create a new resource in PrestaShop API.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the new resource.

        Returns:
            dict: Response from the API.
        """
```

**Назначение**: Создает новый ресурс в API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource`, `method='POST'` и `data`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
data = {'product': {'name': 'New Product'}}
response = api.create(resource=resource, data=data)
print(response)
```

### `PrestaShop.read`

```python
def read(self, resource: str, resource_id: int  |  str, **kwargs) -> Optional[dict]:
        """Read a resource from the PrestaShop API.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            dict: Response from the API.
        """
```

**Назначение**: Читает ресурс из API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource`, `resource_id` и `method='GET'`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
resource_id = 1
response = api.read(resource=resource, resource_id=resource_id)
print(response)
```

### `PrestaShop.write`

```python
def write(self, resource: str, data: dict) -> Optional[dict]:
        """Update an existing resource in the PrestaShop API.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the resource.

        Returns:
            dict: Response from the API.
        """
```

**Назначение**: Обновляет существующий ресурс в API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource`, `resource_id`, `method='PUT'`, `data` и `data_format`. `resource_id` извлекается из входного параметра `data`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
data = {'id': 1, 'product': {'name': 'Updated Product'}}
response = api.write(resource=resource, data=data)
print(response)
```

### `PrestaShop.unlink`

```python
def unlink(self, resource: str, resource_id: int  |  str) -> bool:
        """Delete a resource from the PrestaShop API.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            bool: `True` if successful, `False` otherwise.
        """
```

**Назначение**: Удаляет ресурс из API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource`, `resource_id` и `method='DELETE'`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
resource_id = 1
response = api.unlink(resource=resource, resource_id=resource_id)
print(response)
```

### `PrestaShop.search`

```python
def search(self, resource: str, filter: Optional[str  |  dict] = None, **kwargs) -> List[dict]:
        """Search for resources in the PrestaShop API.

        Args:
            resource (str): API resource (e.g., 'products').
            filter (Optional[str  |  dict]): Filter for the search.

        Returns:
            List[dict]: List of resources matching the search criteria.
        """
```

**Назначение**: Ищет ресурсы в API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource`, `search_filter=filter` и `method='GET'`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
filter = '[name]=%Product%'
response = api.search(resource=resource, filter=filter)
print(response)
```

### `PrestaShop.create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
        """Upload a binary file to a PrestaShop API resource."""
```

**Назначение**: Загружает бинарный файл в ресурс API PrestaShop.

**Как работает функция**:

1. **Открытие файла**:
   - Открывает файл по указанному пути `file_path` в режиме чтения байтов.
2. **Формирование данных для запроса**:
   - Формирует словарь `files`, содержащий имя файла, содержимое файла и MIME-тип.
3. **Выполнение POST-запроса**:
   - Выполняет POST-запрос к API с использованием `client.post`, передавая URL, `files` и аутентификацию.
4. **Проверка статуса ответа**:
   - Проверяет статус ответа с помощью `response.raise_for_status()`, что вызывает исключение в случае HTTP-ошибки.
5. **Разбор ответа**:
   - Разбирает ответ, используя метод `_parse_response`, и возвращает результат.
6. **Обработка исключений**:
   - Перехватывает исключения `RequestException` и логирует их. Возвращает словарь с информацией об ошибке.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'images/products/1'
file_path = 'img.jpeg'
file_name = 'image'
response = api.create_binary(resource=resource, file_path=file_path, file_name=file_name)
print(response)
```

### `PrestaShop.get_schema`

```python
def get_schema(
        self, resource: Optional[str] = None, resource_id: Optional[int] = None, schema: Optional[str] = 'blank', **kwards
    ) -> dict  |  None:
        """Retrieve the schema of a given resource from PrestaShop API.

        Args:
            resource (str): The name of the resource (e.g., 'products', 'customers').
                Если не указана - вернется список всех схем сущностей доступных для API ключа
            resource_id (Optinal[str]):
            schema (Optional[str]): обычно подразумеваются следующие опции:
                - blank: (Самая распространенная опция, как и в вашем коде)
                    Возвращает пустую схему ресурса. Это полезно для определения минимального набора полей,
                    необходимых для создания нового объекта. То есть возвращает структуру XML или JSON с пустыми полями,
                    которые можно заполнить данными.
                - synopsis (или simplified): В некоторых версиях и для некоторых ресурсов может существовать опция,
                    возвращающая упрощенную схему. Она может содержать только основные поля ресурса и их типы.
                    Это может быть удобнее, чем полная схема, если вам не нужны все детали.
                - full (или без указания schema): Часто, если параметр schema не указан,
                    или если он указан как full, возвращается полная схема ресурса. Она включает все поля, их типы,
                    возможные значения, описания и другие метаданные. Это самый подробный вид схемы.
                - form (или что-то подобное): Реже, но может быть опция, возвращающая схему,
                    оптимизированную для отображения в форме редактирования. Она может включать информацию о валидации
                    полей, порядке отображения и т.п.

        Returns:
            dict  |  None: The schema of the requested resource or `None` in case of an error.
        """
```

**Назначение**: Получает схему данного ресурса из API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource`, `resource_id`, `schema` и `method="GET"`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
schema = 'blank'
response = api.get_schema(resource=resource, schema=schema)
print(response)
```

### `PrestaShop.get_data`

```python
def get_data(self, resource: str, **kwargs) -> Optional[dict]:
        """Fetch data from a PrestaShop API resource and save it.

        Args:
            resource (str): API resource (e.g., 'products').
            **kwargs: Additional arguments for the API request.

        Returns:
            dict | None: Data from the API or `False` on failure.
        """
```

**Назначение**: Извлекает данные из ресурса API PrestaShop.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `resource` и `method='GET'`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'products'
response = api.get_data(resource=resource)
print(response)
```

### `PrestaShop.get_apis`

```python
def get_apis(self) -> Optional[dict]:
        """Get a list of all available APIs.

        Returns:
            dict: List of available APIs.
        """
```

**Назначение**: Получает список всех доступных API.

**Как работает функция**:

1. **Вызов `_exec`**:
   - Вызывает метод `_exec` с параметрами `'apis'`, `method='GET'` и `data_format=self.data_format`.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
response = api.get_apis()
print(response)
```

### `PrestaShop.upload_image_async`

```python
def upload_image_async(
        self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None
    ) -> Optional[dict]:
        """Upload an image to PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'images/products/22').
            resource_id (int): Resource ID.
            img_url (str): URL of the image.
            img_name (Optional[str]): Name of the image file, defaults to None.

        Returns:
            dict | None: Response from the API or `False` on failure.
        """
```

**Назначение**: Асинхронно загружает изображение в API PrestaShop.

**Как работает функция**:

1. **Разделение URL изображения**:
   - Разделяет URL изображения на части до и после расширения.
2. **Формирование имени файла**:
   - Формирует имя файла на основе `resource_id` и `img_name`.
3. **Сохранение изображения**:
   - Вызывает функцию `save_image_from_url` для сохранения изображения по URL и получения пути к файлу.
4. **Загрузка изображения**:
   - Вызывает метод `create_binary` для загрузки изображения в API PrestaShop.
5. **Удаление файла**:
   - Вызывает метод `remove_file` для удаления временного файла.
6. **Возврат ответа**:
   - Возвращает ответ от API.

**Примеры**:

```python
api: PrestaShop = PrestaShop(
    api_domain = Config.API_DOMAIN,
    api_key = Config.API_KEY,
    default_lang = 1,
    debug = True,
    data_format = Config.POST_FORMAT,
)
resource = 'images/products/1'
resource_id = 1
img_url = 'https://example.com/image.jpg'
img_name = 'product_image'
response = api.upload_image_async(resource=resource, resource_id=resource_id, img_url=img_url, img_name=img_name)
print(response)
```

### `PrestaShop.upload_image_from_url`

```python
def upload_image_from_url(
        self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None
    ) -> Optional[dict]:
        """Upload an image to PrestaShop API.

        Args:
            resource (str): API resource (