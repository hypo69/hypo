# Модуль для асинхронного взаимодействия с PrestaShop API
=========================================================

Модуль содержит класс `PrestaShopAsync`, который предоставляет асинхронные методы для взаимодействия с PrestaShop API,
позволяя выполнять CRUD-операции, поиск и загрузку изображений. Также обеспечивает обработку ошибок и методы для работы с данными API.

Пример использования
----------------------

```python
async def main():
    api = PrestaShopAsync(
        API_DOMAIN='https://your-prestashop-domain.com',
        API_KEY='your_api_key',
        default_lang=1,
        debug=True,
        data_format='JSON',
    )

    await api.ping()

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
    rec = await api.create('taxes', data)

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

    update_rec = await api.write('taxes', update_data)

    # Remove this tax
    await api.unlink('taxes', str(rec['id']))

    # Search the first 3 taxes with '5' in the name
    import pprint
    recs = await api.search('taxes', filter='[name]=%[5]%', limit='3')

    for rec in recs:
        pprint(rec)

    # Create binary (product image)
    await api.create_binary('images/products/22', 'img.jpeg', 'image')

if __name__ == "__main__":
    asyncio.run(main())
```

## Обзор

Модуль предназначен для асинхронного взаимодействия с PrestaShop API. Он позволяет выполнять операции CRUD (создание, чтение, обновление, удаление) над ресурсами PrestaShop, а также осуществлять поиск и загрузку изображений. Модуль предоставляет класс `PrestaShopAsync`, который инкапсулирует всю логику взаимодействия с API.

## Подробнее

Этот модуль предоставляет асинхронные методы для работы с PrestaShop API, что позволяет выполнять запросы к API без блокировки основного потока выполнения. Это особенно полезно для приложений, требующих высокой производительности и отзывчивости.

## Классы

### `PrestaShopAsync`

**Описание**: Асинхронный класс для взаимодействия с PrestaShop API.

**Принцип работы**:
Класс `PrestaShopAsync` инициализируется с параметрами подключения к API (домен, ключ API, формат данных, режим отладки). Он предоставляет методы для выполнения различных операций с API, такие как создание, чтение, обновление, удаление и поиск ресурсов. Все методы являются асинхронными и используют библиотеку `aiohttp` для выполнения HTTP-запросов.

**Атрибуты**:
- `client` (ClientSession): Асинхронная HTTP-сессия для выполнения запросов.
- `debug` (bool): Флаг, определяющий, включен ли режим отладки.
- `lang_index` (Optional[int]): Индекс языка по умолчанию.
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML').
- `ps_version` (str): Версия PrestaShop.
- `API_DOMAIN` (str): Домен API.
- `API_KEY` (str): Ключ API.

**Методы**:
- `__init__`: Инициализирует класс `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса.
- `_check_response`: Проверяет статус ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от PrestaShop API.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse`: Разбирает XML или JSON ответ от API.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Ищет ресурсы в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API.
- `get_languages_schema`: Получает схему для языков.
- `upload_image_async`: Загружает изображение в PrestaShop API асинхронно.
- `upload_image`: Загружает изображение в PrestaShop API асинхронно.
- `get_product_images`: Получает изображения для продукта.

## Функции

### `__init__`

```python
def __init__(self, api_domain: str, api_key: str, data_format: str = 'JSON', debug: bool = True) -> None:
    """! Initialize the PrestaShopAsync class.

    Args:
        data_format (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
        default_lang (int, optional): Default language ID. Defaults to 1.
        debug (bool, optional): Activate debug mode. Defaults to True.

    Raises:
        PrestaShopAuthenticationError: When the API key is wrong or does not exist.
        PrestaShopException: For generic PrestaShop WebServices errors.
    """
    ...
```

**Назначение**: Инициализирует класс `PrestaShopAsync` с параметрами подключения к API.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Флаг, определяющий, включен ли режим отладки. По умолчанию `True`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если ключ API неверный или не существует.
- `PrestaShopException`: При возникновении общих ошибок веб-сервисов PrestaShop.

**Как работает функция**:
1. Функция принимает домен API, ключ API, формат данных и флаг отладки в качестве аргументов.
2. Сохраняет значения аргументов в атрибуты экземпляра класса.
3. Инициализирует асинхронную HTTP-сессию (`ClientSession`) с использованием ключа API для аутентификации.
4. Устанавливает таймаут для сессии равным 60 секундам.

```
  Инициализация_класса
  │
  ├── Сохранение_параметров
  │   │
  │   ├── api_domain
  │   ├── api_key
  │   ├── debug
  │   └── data_format
  │
  └── Инициализация_ClientSession
      │
      └── Установка_таймаута
```

**Примеры**:

```python
api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key', data_format='JSON', debug=True)
```

### `ping`

```python
async def ping(self) -> bool:
    """! Test if the webservice is working perfectly asynchronously.

    Returns:
        bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    """
    ...
```

**Назначение**: Проверяет, работает ли веб-сервис асинхронно.

**Параметры**:
- `self`

**Возвращает**:
- `bool`: Результат проверки. Возвращает `True`, если веб-сервис работает, иначе `False`.

**Как работает функция**:
1. Функция выполняет HEAD-запрос к домену API.
2. Проверяет статус ответа с помощью метода `_check_response`.
3. Возвращает `True`, если статус ответа 200 или 201, иначе `False`.

```
  Выполнение_HEAD_запроса
  │
  └── Проверка_статуса_ответа
      │
      └── Возврат_результата
```

**Примеры**:

```python
result = await api.ping()
print(result)
```

### `_check_response`

```python
def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
                        headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
    """! Check the response status code and handle errors asynchronously.

    Args:
        status_code (int): HTTP response status code.
        response (aiohttp.ClientResponse): HTTP response object.
        method (str, optional): HTTP method used for the request.
        url (str, optional): The URL of the request.
        headers (dict, optional): The headers used in the request.
        data (dict, optional): The data sent in the request.

    Returns:
        bool: `True` if the status code is 200 or 201, otherwise `False`.
    """
    ...
```

**Назначение**: Проверяет код статуса ответа и обрабатывает ошибки асинхронно.

**Параметры**:
- `status_code` (int): Код статуса HTTP-ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код статуса 200 или 201, иначе `False`.

**Как работает функция**:
1. Функция проверяет, является ли код статуса 200 или 201.
2. Если код статуса не 200 и не 201, вызывает метод `_parse_response_error` для обработки ошибки.
3. Возвращает `True`, если код статуса 200 или 201, иначе `False`.

```
  Проверка_кода_статуса
  │
  └── Обработка_ошибки (если код не 200 или 201)
      │
      └── Возврат_результата
```

**Примеры**:

```python
result = api._check_response(status_code=200, response=response)
print(result)
```

### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
    """! Parse the error response from PrestaShop API asynchronously.

    Args:
        response (aiohttp.ClientResponse): HTTP response object from the server.
        method (str, optional): HTTP method used for the request.
        url (str, optional): The URL of the request.
        headers (dict, optional): The headers used in the request.
        data (dict, optional): The data sent in the request.
    """
    ...
```

**Назначение**: Разбирает ответ об ошибке от PrestaShop API асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа от сервера.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция проверяет формат данных (`data_format`).
2. Если формат данных JSON, извлекает код статуса и текст ответа, затем логирует критическую ошибку, содержащую код статуса, URL, заголовки и текст ответа.
3. Если формат данных XML, разбирает XML-ответ и извлекает код и сообщение об ошибке, затем логирует ошибку, содержащую сообщение и код ошибки.

```
  Проверка_формата_данных
  │
  ├── JSON
  │   │
  │   ├── Извлечение_кода_статуса
  │   ├── Извлечение_текста_ответа
  │   └── Логирование_критической_ошибки
  │
  └── XML
      │
      ├── Разбор_XML
      ├── Извлечение_кода_и_сообщения
      └── Логирование_ошибки
```

**Примеры**:

```python
api._parse_response_error(response=response, method='GET', url='https://your-prestashop-domain.com/api/products', headers={}, data={})
```

### `_prepare`

```python
def _prepare(self, url: str, params: dict) -> str:
    """! Prepare the URL for the request.

    Args:
        url (str): The base URL.
        params (dict): The parameters for the request.

    Returns:
        str: The prepared URL with parameters.
    """
    ...
```

**Назначение**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Как работает функция**:
1. Функция создает объект `PreparedRequest`.
2. Подготавливает URL с использованием базового URL и параметров.
3. Возвращает подготовленный URL.

```
  Создание_PreparedRequest
  │
  └── Подготовка_URL
      │
      └── Возврат_подготовленного_URL
```

**Примеры**:

```python
prepared_url = api._prepare(url='https://your-prestashop-domain.com/api/products', params={'display': 'full'})
print(prepared_url)
```

### `_exec`

```python
async def _exec(self,
              resource: str,
              resource_id: Optional[Union[int, str]] = None,
              resource_ids: Optional[Union[int, Tuple[int]]] = None,
              method: str = 'GET',
              data: Optional[dict] = None,
              headers: Optional[dict] = None,
              search_filter: Optional[Union[str, dict]] = None,
              display: Optional[Union[str, list]] = 'full',
              schema: Optional[str] = None,
              sort: Optional[str] = None,
              limit: Optional[str] = None,
              language: Optional[int] = None,
              io_format: str = 'JSON') -> Optional[dict]:
    """! Execute an HTTP request to the PrestaShop API asynchronously.

    Args:
        resource (str): The API resource (e.g., 'products', 'categories').
        resource_id (int | str, optional): The ID of the resource.
        resource_ids (int | tuple, optional): The IDs of multiple resources.
        method (str, optional): The HTTP method (GET, POST, PUT, DELETE).
        data (dict, optional): The data to be sent with the request.
        headers (dict, optional): Additional headers for the request.
        search_filter (str | dict, optional): Filter for the request.
        display (str | list, optional): Fields to display in the response.
        schema (str, optional): The schema of the data.
        sort (str, optional): Sorting parameter for the request.
        limit (str, optional): Limit of results for the request.
        language (int, optional): The language ID for the request.
        io_format (str, optional): The data format ('JSON' or 'XML').

    Returns:
        dict | None: The response from the API or `False` on failure.
    """
    ...
```

**Назначение**: Выполняет HTTP-запрос к PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products', 'categories').
- `resource_id` (int | str, optional): ID ресурса.
- `resource_ids` (int | tuple, optional): ID нескольких ресурсов.
- `method` (str, optional): HTTP-метод (GET, POST, PUT, DELETE).
- `data` (dict, optional): Данные для отправки с запросом.
- `headers` (dict, optional): Дополнительные заголовки для запроса.
- `search_filter` (str | dict, optional): Фильтр для запроса.
- `display` (str | list, optional): Поля для отображения в ответе.
- `schema` (str, optional): Схема данных.
- `sort` (str, optional): Параметр сортировки для запроса.
- `limit` (str, optional): Лимит результатов для запроса.
- `language` (int, optional): ID языка для запроса.
- `io_format` (str, optional): Формат данных ('JSON' или 'XML').

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Как работает функция**:
1.  Собирает URL для запроса, используя `API_DOMAIN`, `resource` и `resource_id`.
2.  Добавляет параметры запроса (`filter`, `display`, `schema`, `sort`, `limit`, `language`, `output_format`) к URL.
3.  Если формат данных XML, преобразует данные запроса в XML с использованием `dict2xml`.
4.  Выполняет HTTP-запрос с использованием `aiohttp.ClientSession`.
5.  Проверяет статус ответа с помощью `_check_response`. Если статус не успешный, возвращает `False`.
6.  Разбирает ответ в формате JSON или XML с помощью `response.json()` или `_parse`.
7.  Возвращает разобранные данные.

```
  Подготовка_URL
  │
  ├── Формирование_URL_ресурса
  │
  ├── Добавление_параметров_запроса
  │
  └── Преобразование_данных_в_XML (если io_format == 'XML')
  │
  Выполнение_HTTP_запроса
  │
  └── Проверка_статуса_ответа
  │
  └── Разбор_ответа
  │
  Возврат_результата
```

**Примеры**:

```python
result = await api._exec(resource='products', method='GET', io_format='JSON')
print(result)
```

### `_parse`

```python
def _parse(self, text: str) -> dict | ElementTree.Element | bool:
    """! Parse XML or JSON response from the API asynchronously.

    Args:
        text (str): Response text.

    Returns:
        dict | ElementTree.Element | bool: Parsed data or `False` on failure.
    """
    ...
```

**Назначение**: Разбирает XML или JSON ответ от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае ошибки.

**Как работает функция**:
1. Функция проверяет формат данных (`data_format`).
2. Если формат данных JSON, разбирает текст с использованием `j_loads` и возвращает данные из ключа `PrestaShop`, если он присутствует, иначе возвращает разобранные данные.
3. Если формат данных XML, разбирает текст с использованием `ElementTree.fromstring` и возвращает дерево элементов.
4. В случае возникновения ошибки при разборе, логирует ошибку и возвращает `False`.

```
  Проверка_формата_данных
  │
  ├── JSON
  │   │
  │   ├── Разбор_JSON
  │   └── Возврат_данных_из_ключа_PrestaShop (если есть)
  │
  └── XML
      │
      └── Разбор_XML
  │
  Обработка_ошибки
  │
  └── Логирование_ошибки
  │
  Возврат_результата
```

**Примеры**:

```python
data = api._parse(text='{"PrestaShop": {"products": [...]}}')
print(data)
```

### `create`

```python
async def create(self, resource: str, data: dict) -> Optional[dict]:
    """! Create a new resource in PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the new resource.

    Returns:
         dict: Response from the API.
    """
    ...
```

**Назначение**: Создает новый ресурс в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `resource`, `method='POST'`, `data` и `io_format=self.data_format`.
2. Возвращает результат выполнения метода `_exec`.

```
  Выполнение_запроса_на_создание
  │
  └── Вызов__exec
  │
  Возврат_результата
```

**Примеры**:

```python
data = {'product': {'name': 'New Product'}}
result = await api.create(resource='products', data=data)
print(result)
```

### `read`

```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
    """! Read a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Назначение**: Читает ресурс из PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `resource`, `resource_id`, `method='GET'` и `io_format=self.data_format`.
2. Возвращает результат выполнения метода `_exec`.

```
  Выполнение_запроса_на_чтение
  │
  └── Вызов__exec
  │
  Возврат_результата
```

**Примеры**:

```python
result = await api.read(resource='products', resource_id=1)
print(result)
```

### `write`

```python
async def write(self, resource: str, data: dict) -> Optional[dict]:
    """! Update an existing resource in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the resource.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Назначение**: Обновляет существующий ресурс в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `resource`, `resource_id=data.get('id')`, `method='PUT'`, `data` и `io_format=self.data_format`.
2. Возвращает результат выполнения метода `_exec`.

```
  Выполнение_запроса_на_обновление
  │
  └── Вызов__exec
  │
  Возврат_результата
```

**Примеры**:

```python
data = {'id': 1, 'product': {'name': 'Updated Product'}}
result = await api.write(resource='products', data=data)
print(result)
```

### `unlink`

```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
    """! Delete a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        bool: `True` if successful, `False` otherwise.
    """
    ...
```

**Назначение**: Удаляет ресурс из PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если удаление выполнено успешно, `False` в противном случае.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `resource`, `resource_id`, `method='DELETE'` и `io_format=self.data_format`.
2. Возвращает результат выполнения метода `_exec`.

```
  Выполнение_запроса_на_удаление
  │
  └── Вызов__exec
  │
  Возврат_результата
```

**Примеры**:

```python
result = await api.unlink(resource='products', resource_id=1)
print(result)
```

### `search`

```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
    """! Search for resources in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        filter (str | dict, optional): Filter for the search.

    Returns:
         List[dict]: List of resources matching the search criteria.
    """
    ...
```

**Назначение**: Ищет ресурсы в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `resource`, `search_filter=filter`, `method='GET'`, `io_format=self.data_format` и дополнительными аргументами `kwargs`.
2. Возвращает результат выполнения метода `_exec`.

```
  Выполнение_запроса_на_поиск
  │
  └── Вызов__exec
  │
  Возврат_результата
```

**Примеры**:

```python
result = await api.search(resource='products', filter='[name]=%Product%')
print(result)
```

### `create_binary`

```python
async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """! Upload a binary file to a PrestaShop API resource asynchronously.

    Args:
        resource (str): API resource (e.g., 'images/products/22').
        file_path (str): Path to the binary file.
        file_name (str): File name.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Назначение**: Загружает бинарный файл в ресурс PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Функция открывает файл по указанному пути в бинарном режиме.
2. Устанавливает заголовок `Content-Type` в значение `application/octet-stream`.
3. Выполняет POST-запрос к API с использованием содержимого файла в качестве данных запроса.
4. Возвращает JSON-ответ от API.

```
  Чтение_бинарного_файла
  │
  └── Установка_заголовков
  │
  └── Выполнение_POST_запроса
  │
  Возврат_JSON_ответа
```

**Примеры**:

```python
result = await api.create_binary(resource='images/products/22', file_path='img.jpg', file_name='image')
print(result)
```

### `_save`

```python
def _save(self, file_name: str, data: dict):
    """! Save data to a file.

    Args:
        file_name (str): Name of the file.
        data (dict): Data to be saved.
    """
    ...
```

**Назначение**: Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

**Как работает функция**:
1. Функция вызывает функцию `save_text_file` для сохранения данных в файл.
2. Данные преобразуются в JSON-формат с отступами и отключенной поддержкой ASCII с помощью `j_dumps`.

```
  Преобразование_данных_в_JSON
  │
  └── Сохранение_данных_в_файл
```

**Примеры**:

```python
api._save(file_name='products.json', data={'products': [...]})
```

### `get_data`

```python
async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
    """! Fetch data from a PrestaShop API resource and save it asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        **kwargs: Additional arguments for the API request.

    Returns:
        dict | None: Data from the API or `False` on failure.
    """
    ...
```

**Назначение**: Получает данные из ресурса PrestaShop API и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API запроса.

**Возвращает**:
- `dict | None`: Данные из API или `False` в случае ошибки.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `resource`, `method='GET'`, `io_format=self.data_format` и дополнительными аргументами `kwargs`.
2. Если данные получены успешно, вызывает метод `_save` для сохранения данных в файл.
3. Возвращает полученные данные или `False` в случае ошибки.

```
  Выполнение_запроса_на_получение_данных
  │
  └── Сохранение_данных_в_файл (если данные получены успешно)
  │
  Возврат_результата
```

**Примеры**:

```python
data = await api.get_data(resource='products', display='full')
print(data)
```

### `remove_file`

```python
def remove_file(self, file_path: str):
    """! Remove a file from the filesystem.

    Args:
        file_path (str): Path to the file.
    """
    ...
```

**Назначение**: Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

**Как работает функция**:
1. Функция пытается удалить файл по указанному пути с помощью `os.remove`.
2. В случае возникновения ошибки при удалении, логирует ошибку.

```
  Удаление_файла
  │
  Обработка_ошибки
  │
  └── Логирование_ошибки (если возникла ошибка)
```

**Примеры**:

```python
api.remove_file(file_path='temp.txt')
```

### `get_apis`

```python
async def get_apis(self) -> Optional[dict]:
    """! Get a list of all available APIs asynchronously.

    Returns:
         dict: List of available APIs.
    """
    ...
```

**Назначение**: Получает список всех доступных API асинхронно.

**Параметры**:
- `self`

**Возвращает**:
- `dict`: Список доступных API.

**Как работает функция**:
1. Функция вызывает метод `_exec` с параметрами `'apis'`, `method='GET'` и `io_format=self.data_format`.
2. Возвращает результат выполнения метода `_exec`.

```
  Выполнение_запроса_на_получение_списка_API
  │
  └── Вызов__exec
  │
  Возврат_результата
```

**Примеры**:

```python
result = await api.get_apis()
print(result)
```

### `get_languages_schema`

```python
async def get_languages_schema(self) -> Optional[dict]:
    """! Get the schema for languages asynchronously.

    Returns:
        dict: Language schema or `None` on failure.
    """
    ...
```

**Назначение**: Получает схему для языков асин