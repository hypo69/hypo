# Модуль `api_async`

## Обзор

Модуль `api_async` предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с API PrestaShop, используя JSON и XML. Он обеспечивает асинхронные методы для выполнения CRUD-операций, поиска и загрузки изображений. Модуль также включает обработку ошибок и методы для управления данными API.

## Подробней

Этот модуль разработан для упрощения взаимодействия с API PrestaShop в асинхронном режиме. Класс `PrestaShopAsync` позволяет выполнять запросы к API, обрабатывать ответы и управлять ресурсами PrestaShop. Он поддерживает форматы данных JSON и XML и предоставляет методы для обработки ошибок и преобразования данных.

## Классы

### `Format`

**Описание**: Перечисление для определения типов данных возврата (JSON, XML).

**Параметры**:
- `Enum`: (int): 1 => JSON, 2 => XML

### `PrestaShopAsync`

**Описание**: Асинхронный класс для взаимодействия с API PrestaShop.

**Методы**:
- `__init__`: Инициализирует класс `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса асинхронно.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки асинхронно.
- `_parse_response_error`: Разбирает ответ об ошибке от API PrestaShop асинхронно.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к API PrestaShop асинхронно.
- `_parse`: Разбирает XML или JSON ответ от API асинхронно.
- `create`: Создает новый ресурс в API PrestaShop асинхронно.
- `read`: Читает ресурс из API PrestaShop асинхронно.
- `write`: Обновляет существующий ресурс в API PrestaShop асинхронно.
- `unlink`: Удаляет ресурс из API PrestaShop асинхронно.
- `search`: Выполняет поиск ресурсов в API PrestaShop асинхронно.
- `create_binary`: Загружает бинарный файл в ресурс API PrestaShop асинхронно.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из ресурса API PrestaShop и сохраняет их асинхронно.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API асинхронно.
- `get_languages_schema`: Получает схему для языков асинхронно.
- `upload_image_async`: Загружает изображение в API PrestaShop асинхронно.
- `upload_image`: Загружает изображение в API PrestaShop асинхронно.
- `get_product_images`: Получает изображения для продукта асинхронно.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Активировать режим отладки. По умолчанию `True`.
- `resource` (str): API resource (e.g., 'products', 'categories').
- `resource_id` (int | str, optional): The ID of the resource.
- `resource_ids` (int | tuple, optional): The IDs of multiple resources.
- `method` (str, optional): The HTTP method (GET, POST, PUT, DELETE).
- `data` (dict, optional): The data to be sent with the request.
- `headers` (dict, optional): Additional headers for the request.
- `search_filter` (str | dict, optional): Filter for the request.
- `display` (str | list, optional): Fields to display in the response.
- `schema` (str, optional): The schema of the data.
- `sort` (str, optional): Sorting parameter for the request.
- `limit` (str, optional): Limit of results for the request.
- `language` (int, optional): The language ID for the request.
- `io_format` (str, optional): The data format ('JSON' or 'XML').
- `file_path` (str): Path to the binary file.
- `file_name` (str): File name.
- `img_url` (str): URL of the image.
- `img_name` (str, optional): Name of the image file, defaults to None.
- `product_id` (int): Product ID.

**Примеры**:

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

## Функции

### `ping`

```python
async def ping(self) -> bool:
    """Test if the webservice is working perfectly asynchronously.

    Returns:
        bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    """
    ...
```

**Описание**: Проверяет, работает ли веб-сервис асинхронно.

**Возвращает**:
- `bool`: Результат проверки связи. Возвращает `True`, если веб-сервис работает, иначе `False`.

### `_check_response`

```python
def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
                        headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
    """Check the response status code and handle errors asynchronously.

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

**Описание**: Проверяет код состояния ответа и обрабатывает ошибки асинхронно.

**Параметры**:
- `status_code` (int): Код состояния HTTP-ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
    """Parse the error response from PrestaShop API asynchronously.

    Args:
        response (aiohttp.ClientResponse): HTTP response object from the server.
        method (str, optional): HTTP method used for the request.
        url (str, optional): The URL of the request.
        headers (dict, optional): The headers used in the request.
        data (dict, optional): The data sent in the request.
    """
    ...
```

**Описание**: Разбирает ответ об ошибке от API PrestaShop асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа от сервера.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

### `_prepare`

```python
def _prepare(self, url: str, params: dict) -> str:
    """Prepare the URL for the request.

    Args:
        url (str): The base URL.
        params (dict): The parameters for the request.

    Returns:
        str: The prepared URL with parameters.
    """
    ...
```

**Описание**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

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
    """Execute an HTTP request to the PrestaShop API asynchronously.

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

**Описание**: Выполняет HTTP-запрос к API PrestaShop асинхронно.

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
- `dict | None`: Ответ от API или `False` в случае неудачи.

### `_parse`

```python
def _parse(self, text: str) -> dict | ElementTree.Element | bool:
    """Parse XML or JSON response from the API asynchronously.

    Args:
        text (str): Response text.

    Returns:
        dict | ElementTree.Element | bool: Parsed data or `False` on failure.
    """
    ...
```

**Описание**: Разбирает XML или JSON ответ от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае неудачи.

### `create`

```python
async def create(self, resource: str, data: dict) -> Optional[dict]:
    """Create a new resource in PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the new resource.

    Returns:
         dict: Response from the API.
    """
    ...
```

**Описание**: Создает новый ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

### `read`

```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
    """Read a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Описание**: Читает ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

### `write`

```python
async def write(self, resource: str, data: dict) -> Optional[dict]:
    """Update an existing resource in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the resource.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Описание**: Обновляет существующий ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

### `unlink`

```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
    """Delete a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        bool: `True` if successful, `False` otherwise.
    """
    ...
```

**Описание**: Удаляет ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, `False` иначе.

### `search`

```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
    """Search for resources in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        filter (str | dict, optional): Filter for the search.

    Returns:
         List[dict]: List of resources matching the search criteria.
    """
    ...
```

**Описание**: Выполняет поиск ресурсов в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

### `create_binary`

```python
async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """Upload a binary file to a PrestaShop API resource asynchronously.

    Args:
        resource (str): API resource (e.g., 'images/products/22').
        file_path (str): Path to the binary file.
        file_name (str): File name.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Описание**: Загружает бинарный файл в ресурс API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

### `_save`

```python
def _save(self, file_name: str, data: dict):
    """Save data to a file.

    Args:
        file_name (str): Name of the file.
        data (dict): Data to be saved.
    """
    ...
```

**Описание**: Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

### `get_data`

```python
async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
    """Fetch data from a PrestaShop API resource and save it asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        **kwargs: Additional arguments for the API request.

    Returns:
        dict | None: Data from the API or `False` on failure.
    """
    ...
```

**Описание**: Получает данные из ресурса API PrestaShop и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API запроса.

**Возвращает**:
- `dict | None`: Данные от API или `False` в случае неудачи.

### `remove_file`

```python
def remove_file(self, file_path: str):
    """Remove a file from the filesystem.

    Args:
        file_path (str): Path to the file.
    """
    ...
```

**Описание**: Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

### `get_apis`

```python
async def get_apis(self) -> Optional[dict]:
    """Get a list of all available APIs asynchronously.

    Returns:
         dict: List of available APIs.
    """
    ...
```

**Описание**: Получает список всех доступных API асинхронно.

**Возвращает**:
- `dict`: Список доступных API.

### `get_languages_schema`

```python
async def get_languages_schema(self) -> Optional[dict]:
    """Get the schema for languages asynchronously.

    Returns:
        dict: Language schema or `None` on failure.
    """
    ...
```

**Описание**: Получает схему для языков асинхронно.

**Возвращает**:
- `dict`: Схема языка или `None` в случае неудачи.

### `upload_image_async`

```python
async def upload_image_async(self, resource: str, resource_id: int, img_url: str,
                           img_name: Optional[str] = None) -> Optional[dict]:
    """Upload an image to PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'images/products/22').
        resource_id (int): Resource ID.
        img_url (str): URL of the image.
        img_name (str, optional): Name of the image file, defaults to None.

    Returns:
        dict | None: Response from the API or `False` on failure.
    """
    ...
```

**Описание**: Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

### `upload_image`

```python
async def upload_image(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]:
    """Upload an image to PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'images/products/22').
        resource_id (int): Resource ID.
        img_url (str): URL of the image.
        img_name (str, optional): Name of the image file, defaults to None.

    Returns:
        dict | None: Response from the API or `False` on failure.
    """
    ...
```

**Описание**: Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

### `get_product_images`

```python
async def get_product_images(self, product_id: int) -> Optional[dict]:
    """Get images for a product asynchronously.

    Args:
        product_id (int): Product ID.

    Returns:
        dict | None: List of product images or `False` on failure.
    """
    ...
```

**Описание**: Получает изображения для продукта асинхронно.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае неудачи.