# Модуль `api_async.py`

## Обзор

Модуль `api_async.py` предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с API PrestaShop. Он поддерживает выполнение CRUD-операций, поиск данных и загрузку изображений. Класс обеспечивает обработку ошибок и удобные методы для работы с данными API в форматах JSON и XML.

## Подробней

Этот модуль предназначен для асинхронного взаимодействия с API PrestaShop. Он позволяет выполнять запросы к API, получать данные, создавать, обновлять и удалять записи, а также загружать изображения. Использование асинхронных методов позволяет эффективно работать с API, не блокируя основной поток выполнения программы.

## Классы

### `Format`

**Описание**:
Перечисление, определяющее форматы данных (JSON, XML).

**Параметры**:
- `Enum` (int): 1 => JSON, 2 => XML

### `PrestaShopAsync`

**Описание**:
Асинхронный класс для взаимодействия с API PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса асинхронно.
- `_check_response`: Проверяет статус код ответа и обрабатывает ошибки асинхронно.
- `_parse_response_error`: Разбирает ответ об ошибке от API PrestaShop асинхронно.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к API PrestaShop асинхронно.
- `_parse`: Разбирает XML или JSON ответ от API асинхронно.
- `create`: Создает новый ресурс в API PrestaShop асинхронно.
- `read`: Читает ресурс из API PrestaShop асинхронно.
- `write`: Обновляет существующий ресурс в API PrestaShop асинхронно.
- `unlink`: Удаляет ресурс из API PrestaShop асинхронно.
- `search`: Ищет ресурсы в API PrestaShop асинхронно.
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

**Примеры**
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

### `__init__`

```python
    def __init__(self,
                api_domain: str,
                api_key: str,
                data_format: str = 'JSON',
                debug: bool = True) -> None:
        """! Initialize the PrestaShopAsync class.

        Args:
            data_format (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
            default_lang (int, optional): Default language ID. Defaults to 1.
            debug (bool, optional): Activate debug mode. Defaults to True.

        Raises:
            PrestaShopAuthenticationError: When the API key is wrong or does not exist.
            PrestaShopException: For generic PrestaShop WebServices errors.
        """
```

**Описание**:
Инициализирует класс `PrestaShopAsync` с заданными параметрами.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Активировать режим отладки. По умолчанию `True`.

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если API-ключ неверен или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

**Примеры**:
```python
api = PrestaShopAsync(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    data_format='JSON',
    debug=True
)
```

### `ping`

```python
    async def ping(self) -> bool:
        """! Test if the webservice is working perfectly asynchronously.

        Returns:
            bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        """
```

**Описание**:
Проверяет работоспособность веб-сервиса асинхронно.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    result = await api.ping()
    print(f"Ping result: {result}")
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
```

**Описание**:
Проверяет код состояния ответа и обрабатывает ошибки асинхронно.

**Параметры**:
- `status_code` (int): Код состояния HTTP-ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    async with aiohttp.ClientSession() as session:
        async with session.get('https://your-prestashop-domain.com/api') as response:
            result = api._check_response(response.status, response)
            print(f"Response check result: {result}")
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
```

**Описание**:
Разбирает ответ об ошибке от API PrestaShop асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа от сервера.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    async with aiohttp.ClientSession() as session:
        async with session.get('https://your-prestashop-domain.com/api?ws_key=invalid') as response:
            api._parse_response_error(response)
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
```

**Описание**:
Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Примеры**:
```python
api = PrestaShopAsync(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key'
)
url = 'https://your-prestashop-domain.com/api/products'
params = {'display': 'full', 'limit': '1'}
prepared_url = api._prepare(url, params)
print(f"Prepared URL: {prepared_url}")
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
```

**Описание**:
Выполняет HTTP-запрос к API PrestaShop асинхронно.

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

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    products = await api._exec(resource='products', method='GET', limit='5')
    print(f"Products: {products}")
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
```

**Описание**:
Разбирает XML или JSON ответ от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShopAsync(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key'
)
text = '{"PrestaShop":{"products":[]}}'
data = api._parse(text)
print(f"Parsed data: {data}")
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
```

**Описание**:
Создает новый ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    data = {'product': {'name': 'Test Product', 'price': 10}}
    response = await api.create(resource='products', data=data)
    print(f"Create response: {response}")
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
```

**Описание**:
Читает ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    response = await api.read(resource='products', resource_id=1)
    print(f"Read response: {response}")
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
```

**Описание**:
Обновляет существующий ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    data = {'id': 1, 'product': {'name': 'Updated Product', 'price': 12}}
    response = await api.write(resource='products', data=data)
    print(f"Write response: {response}")
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
```

**Описание**:
Удаляет ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    response = await api.unlink(resource='products', resource_id=1)
    print(f"Unlink response: {response}")
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
```

**Описание**:
Ищет ресурсы в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    response = await api.search(resource='products', filter='[name]=%Test%')
    print(f"Search response: {response}")
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
```

**Описание**:
Загружает бинарный файл в ресурс API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    # Create a dummy image file for testing
    with open('test_image.jpg', 'wb') as f:
        f.write(b'dummy image data')
    response = await api.create_binary(resource='images/products/1', file_path='test_image.jpg', file_name='test_image')
    print(f"Create binary response: {response}")
```

### `_save`

```python
    def _save(self, file_name: str, data: dict):
        """! Save data to a file.

        Args:
            file_name (str): Name of the file.
            data (dict): Data to be saved.
        """
```

**Описание**:
Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

**Примеры**:
```python
api = PrestaShopAsync(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key'
)
data = {'products': []}
api._save(file_name='products.json', data=data)
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
```

**Описание**:
Получает данные из ресурса API PrestaShop и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API-запроса.

**Возвращает**:
- `dict | None`: Данные из API или `False` в случае ошибки.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    data = await api.get_data(resource='products', limit='5')
    print(f"Get data response: {data}")
```

### `remove_file`

```python
    def remove_file(self, file_path: str):
        """! Remove a file from the filesystem.

        Args:
            file_path (str): Path to the file.
        """
```

**Описание**:
Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

**Примеры**:
```python
api = PrestaShopAsync(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key'
)
# Create a dummy file for testing
with open('test_file.txt', 'w') as f:
    f.write('test data')
api.remove_file(file_path='test_file.txt')
```

### `get_apis`

```python
    async def get_apis(self) -> Optional[dict]:
        """! Get a list of all available APIs asynchronously.

        Returns:
             dict: List of available APIs.
        """
```

**Описание**:
Получает список всех доступных API асинхронно.

**Возвращает**:
- `dict`: Список доступных API.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    apis = await api.get_apis()
    print(f"Available APIs: {apis}")
```

### `get_languages_schema`

```python
    async def get_languages_schema(self) -> Optional[dict]:
        """! Get the schema for languages asynchronously.

        Returns:
            dict: Language schema or `None` on failure.
        """
```

**Описание**:
Получает схему для языков асинхронно.

**Возвращает**:
- `dict`: Схема языков или `None` в случае ошибки.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    schema = await api.get_languages_schema()
    print(f"Languages schema: {schema}")
```

### `upload_image_async`

```python
    async def upload_image_async(self, resource: str, resource_id: int, img_url: str,
                           img_name: Optional[str] = None) -> Optional[dict]:
        """! Upload an image to PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'images/products/22').
            resource_id (int): Resource ID.
            img_url (str): URL of the image.
            img_name (str, optional): Name of the image file, defaults to None.

        Returns:
            dict | None: Response from the API or `False` on failure.
        """
```

**Описание**:
Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    # Replace with a valid image URL
    img_url = 'https://example.com/image.jpg'
    response = await api.upload_image_async(resource='images/products/1', resource_id=1, img_url=img_url, img_name='test_image')
    print(f"Upload image async response: {response}")
```

### `upload_image`

```python
    async def upload_image(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]:
        """! Upload an image to PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'images/products/22').
            resource_id (int): Resource ID.
            img_url (str): URL of the image.
            img_name (str, optional): Name of the image file, defaults to None.

        Returns:
            dict | None: Response from the API or `False` on failure.
        """
```

**Описание**:
Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    # Replace with a valid image URL
    img_url = 'https://example.com/image.jpg'
    response = await api.upload_image(resource='images/products/1', resource_id=1, img_url=img_url, img_name='test_image')
    print(f"Upload image response: {response}")
```

### `get_product_images`

```python
    async def get_product_images(self, product_id: int) -> Optional[dict]:
        """! Get images for a product asynchronously.

        Args:
            product_id (int): Product ID.

        Returns:
            dict | None: List of product images or `False` on failure.
        """
```

**Описание**:
Получает изображения для продукта асинхронно.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае ошибки.

**Примеры**:
```python
async def main():
    api = PrestaShopAsync(
        api_domain='https://your-prestashop-domain.com',
        api_key='your_api_key'
    )
    images = await api.get_product_images(product_id=1)
    print(f"Product images: {images}")