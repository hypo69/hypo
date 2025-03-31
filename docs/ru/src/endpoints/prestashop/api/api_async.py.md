# Модуль `api_async.py`

## Обзор

Модуль предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с API PrestaShop.
Он поддерживает операции CRUD, поиск и загрузку изображений. Модуль включает обработку ошибок и методы для работы с данными API.

## Подробней

Этот модуль предназначен для упрощения асинхронного взаимодействия с API PrestaShop. Он предоставляет методы для выполнения различных операций, таких как создание, чтение, обновление и удаление ресурсов, а также для поиска и загрузки изображений.

## Классы

### `Format`

**Описание**:
Перечисление, определяющее типы данных, возвращаемые API (JSON, XML).

```python
class Format(Enum):
    """Data types return (JSON, XML)

    .. deprecated::
        I prefer JSON 👍 :))

    :param Enum: (int): 1 => JSON, 2 => XML
    """
    JSON = 'JSON'
    XML = 'XML'
```

**Как работает класс**:

Перечисление `Format` определяет два возможных формата данных: `JSON` и `XML`. Формат `XML` помечен как устаревший.

### `PrestaShopAsync`

**Описание**:
Асинхронный класс для взаимодействия с API PrestaShop с использованием JSON и XML.

```python
class PrestaShopAsync:
    """! Async Class for interacting with the PrestaShop API using JSON and XML.

    This class provides asynchronous methods to interact with the PrestaShop API,
    allowing for CRUD operations, searching, and uploading images. It also provides
    error handling for responses and methods to handle the API's data.

    Example usage:

    .. code-block:: python

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

    """
    client: ClientSession = None
    debug = False
    lang_index: Optional[int] = 1
    data_format:str = 'JSON'
    ps_version = ''
    API_DOMAIN:str = None
    API_KEY:str = None
```

**Как работает класс**:

Класс `PrestaShopAsync` предоставляет асинхронные методы для взаимодействия с API PrestaShop.
Он позволяет выполнять операции CRUD (создание, чтение, обновление, удаление), поиск и загрузку изображений.
Класс включает обработку ошибок и методы для обработки данных API.

**Атрибуты**:

-   `client` (ClientSession): Асинхронный клиент сессии для выполнения HTTP-запросов.
-   `debug` (bool): Флаг для активации режима отладки.
-   `lang_index` (Optional[int]): Индекс языка по умолчанию.
-   `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML').
-   `ps_version` (str): Версия PrestaShop.
-   `API_DOMAIN` (str): Домен API PrestaShop.
-   `API_KEY` (str): Ключ API PrestaShop.

**Методы**:

-   `__init__`: Инициализирует класс `PrestaShopAsync`.
-   `ping`: Проверяет работоспособность веб-сервиса асинхронно.
-   `_check_response`: Проверяет статус код ответа и обрабатывает ошибки асинхронно.
-   `_parse_response_error`: Разбирает ответ об ошибке от API PrestaShop асинхронно.
-   `_prepare`: Подготавливает URL для запроса.
-   `_exec`: Выполняет HTTP-запрос к API PrestaShop асинхронно.
-   `_parse`: Разбирает XML или JSON ответ от API асинхронно.
-   `create`: Создает новый ресурс в API PrestaShop асинхронно.
-   `read`: Читает ресурс из API PrestaShop асинхронно.
-   `write`: Обновляет существующий ресурс в API PrestaShop асинхронно.
-   `unlink`: Удаляет ресурс из API PrestaShop асинхронно.
-   `search`: Ищет ресурсы в API PrestaShop асинхронно.
-   `create_binary`: Загружает бинарный файл в ресурс API PrestaShop асинхронно.
-   `_save`: Сохраняет данные в файл.
-   `get_data`: Получает данные из ресурса API PrestaShop и сохраняет их асинхронно.
-   `remove_file`: Удаляет файл из файловой системы.
-   `get_apis`: Получает список всех доступных API асинхронно.
-   `get_languages_schema`: Получает схему для языков асинхронно.
-   `upload_image_async`: Загружает изображение в API PrestaShop асинхронно.
-   `upload_image`: Загружает изображение в API PrestaShop асинхронно.
-   `get_product_images`: Получает изображения для продукта асинхронно.

## Функции

### `__init__`

```python
    def __init__(self,
                api_domain:str,
                api_key:str,
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
        self.API_DOMAIN = api_domain
        self.API_KEY = api_key
        self.debug = debug
        self.data_format = data_format

        self.client = ClientSession(
            auth=aiohttp.BasicAuth(self.API_KEY, ''),
            timeout=ClientTimeout(total=60)
        )
```

**Назначение**:
Инициализация класса `PrestaShopAsync`.

**Как работает функция**:

1.  Сохраняет значения переданных аргументов `api_domain`, `api_key`, `debug` и `data_format` в атрибуты экземпляра класса.
2.  Инициализирует асинхронную сессию `ClientSession` с использованием ключа API для аутентификации. Устанавливает общее время ожидания для запросов в 60 секунд.

**Параметры**:

-   `api_domain` (str): Домен API PrestaShop.
-   `api_key` (str): Ключ API PrestaShop.
-   `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
-   `debug` (bool, optional): Флаг для активации режима отладки. По умолчанию `True`.

**Вызывает исключения**:

-   `PrestaShopAuthenticationError`: Если ключ API неверен или не существует.
-   `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

### `ping`

```python
    async def ping(self) -> bool:
        """! Test if the webservice is working perfectly asynchronously.

        Returns:
            bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        """
        async with self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        ) as response:
            return await self._check_response(response.status, response)
```

**Назначение**:
Проверка работоспособности веб-сервиса асинхронно.

**Как работает функция**:

1.  Выполняет `HEAD` запрос к домену API.
2.  Передает статус код ответа и сам ответ в метод `_check_response` для проверки.
3.  Возвращает результат проверки, который показывает, работает ли веб-сервис.

**Возвращает**:

-   `bool`: `True`, если веб-сервис работает, иначе `False`.

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
        if status_code in (200, 201):
            return True
        else:
            self._parse_response_error(response, method, url, headers, data)
            return False
```

**Назначение**:
Проверка статус кода ответа и обработка ошибок асинхронно.

**Как работает функция**:

1.  Проверяет, находится ли статус код ответа в диапазоне 200-201 (успешные коды).
2.  Если статус код не успешный, вызывает метод `_parse_response_error` для обработки ошибки.
3.  Возвращает `True`, если статус код успешный, иначе `False`.

**Параметры**:

-   `status_code` (int): HTTP статус код ответа.
-   `response` (aiohttp.ClientResponse): Объект HTTP ответа.
-   `method` (str, optional): HTTP метод, использованный для запроса.
-   `url` (str, optional): URL запроса.
-   `headers` (dict, optional): Заголовки запроса.
-   `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:

-   `bool`: `True`, если статус код 200 или 201, иначе `False`.

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
        if self.data_format == 'JSON':
            status_code = response.status
            if not status_code in (200, 201):
                text = response.text()
                logger.critical(f"""response status code: {status_code}
                    url: {response.request_info.url}
                    --------------
                    headers: {response.headers}
                    --------------
                    response text: {text}""")
            return response
        else:
            error_answer = self._parse(response.text())
            if isinstance(error_answer, dict):
                error_content = (error_answer
                                 .get('PrestaShop', {})
                                 .get('errors', {})
                                 .get('error', {}))
                if isinstance(error_content, list):
                    error_content = error_content[0]
                code = error_content.get('code')
                message = error_content.get('message')
            elif isinstance(error_answer, ElementTree.Element):
                error = error_answer.find('errors/error')
                code = error.find('code').text
                message = error.find('message').text
            logger.error(f'XML response error: {message} \n Code: {code}')
            return code, message
```

**Назначение**:
Разбор ответа об ошибке от API PrestaShop асинхронно.

**Как работает функция**:

1.  Проверяет формат данных (`data_format`).
2.  Если формат `JSON`:
    *   Получает статус код ответа.
    *   Если статус код не успешный, извлекает текст ответа и регистрирует критическое сообщение с информацией о статус коде, URL, заголовках и тексте ответа.
    *   Возвращает объект ответа.
3.  Если формат `XML`:
    *   Разбирает текст ответа с помощью метода `_parse`.
    *   Извлекает код и сообщение об ошибке из разобранного ответа.
    *   Регистрирует сообщение об ошибке с кодом и сообщением.
    *   Возвращает код и сообщение об ошибке.

**Параметры**:

-   `response` (aiohttp.ClientResponse): Объект HTTP ответа от сервера.
-   `method` (str, optional): HTTP метод, использованный для запроса.
-   `url` (str, optional): URL запроса.
-   `headers` (dict, optional): Заголовки запроса.
-   `data` (dict, optional): Данные, отправленные в запросе.

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
        req = PreparedRequest()
        req.prepare_url(url, params)
        return req.url
```

**Назначение**:
Подготовка URL для запроса.

**Как работает функция**:

1.  Создает объект `PreparedRequest`.
2.  Подготавливает URL с параметрами с помощью метода `prepare_url`.
3.  Возвращает подготовленный URL.

**Параметры**:

-   `url` (str): Базовый URL.
-   `params` (dict): Параметры для запроса.

**Возвращает**:

-   `str`: Подготовленный URL с параметрами.

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
        self.debug = False
        if self.debug:
            # import sys
            # original_stderr = sys.stderr
            # f = open('stderr.log', 'w')
            # sys.stderr = f

            # prepared_url = self._prepare(f'{self.API_DOMAIN}/api/{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}/api/{resource}',
            #                       {'filter': search_filter,
            #                        'display': display,
            #                        'schema': schema,
            #                        'sort': sort,
            #                        'limit': limit,
            #                        'language': language,
            #                        'output_format': io_format})

            # request_data = dict2xml(data) if data and io_format == 'XML' else data

            # with self.client.request(
            #     method=method,
            #     url=prepared_url,
            #     data=request_data,
            #     headers=headers,
            # ) as response:

            #     sys.stderr = original_stderr

            #     if not self._check_response(response.status, response, method, prepared_url, headers, request_data):
            #         return False

            #     if io_format == 'JSON':
            #         return response.json()
            #     else:
            #         return self._parse(await response.text())
            ...
        else:
            prepared_url = self._prepare(f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}',
                                  {'filter': search_filter,
                                   'display': display,
                                   'schema': schema,
                                   'sort': sort,
                                   'limit': limit,
                                   'language': language,
                                   'output_format': io_format})
            
            request_data = dict2xml(data) if data and io_format == 'XML' else data
            
            with self.client.request(
                method=method,
                url=prepared_url,
                data=request_data,
                headers=headers,
            ) as response:

                if not self._check_response(response.status, response, method, prepared_url, headers, request_data):
                    return False

                if io_format == 'JSON':
                    return response.json()
                else:
                    return self._parse(await response.text())
```

**Назначение**:
Выполнение HTTP-запроса к API PrestaShop асинхронно.

**Как работает функция**:

1.  Отключает режим отладки (`self.debug = False`).
2.  Подготавливает URL запроса, используя метод `_prepare`, с учетом указанных параметров, таких как фильтры, схема, сортировка, лимит и язык.
3.  Преобразует данные запроса в формат XML, если указан формат XML (`io_format == 'XML'`).
4.  Выполняет HTTP-запрос с использованием асинхронного клиента `self.client.request` с указанным методом, URL, данными и заголовками.
5.  Проверяет статус ответа с помощью метода `_check_response`. Если статус не успешный, возвращает `False`.
6.  В зависимости от формата ответа (`io_format`) возвращает JSON или разбирает XML с помощью метода `_parse`.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products', 'categories').
-   `resource_id` (int | str, optional): ID ресурса.
-   `resource_ids` (int | tuple, optional): ID нескольких ресурсов.
-   `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE).
-   `data` (dict, optional): Данные для отправки с запросом.
-   `headers` (dict, optional): Дополнительные заголовки для запроса.
-   `search_filter` (str | dict, optional): Фильтр для запроса.
-   `display` (str | list, optional): Поля для отображения в ответе.
-   `schema` (str, optional): Схема данных.
-   `sort` (str, optional): Параметр сортировки для запроса.
-   `limit` (str, optional): Лимит результатов для запроса.
-   `language` (int, optional): ID языка для запроса.
-   `io_format` (str, optional): Формат данных ('JSON' или 'XML').

**Возвращает**:

-   `dict | None`: Ответ от API или `False` в случае неудачи.

### `_parse`

```python
    def _parse(self, text: str) -> dict | ElementTree.Element | bool:
        """! Parse XML or JSON response from the API asynchronously.

        Args:
            text (str): Response text.

        Returns:
            dict | ElementTree.Element | bool: Parsed data or `False` on failure.
        """
        try:
            if self.data_format == 'JSON':
              data = j_loads(text)
              return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
            logger.error(f'Parsing Error: {str(ex)}')
            return False
```

**Назначение**:
Разбор XML или JSON ответа от API асинхронно.

**Как работает функция**:

1.  Пытается разобрать текст ответа в зависимости от формата данных (`data_format`).
2.  Если формат `JSON`:
    *   Использует `j_loads` для разбора JSON.
    *   Если в данных есть ключ 'PrestaShop', возвращает значение этого ключа, иначе возвращает данные целиком.
3.  Если формат `XML`:
    *   Использует `ElementTree.fromstring` для разбора XML.
    *   Возвращает дерево элементов.
4.  В случае ошибки разбора регистрирует ошибку и возвращает `False`.

**Параметры**:

-   `text` (str): Текст ответа.

**Возвращает**:

-   `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае неудачи.

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
        return await self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)
```

**Назначение**:
Создание нового ресурса в API PrestaShop асинхронно.

**Как работает функция**:

1.  Вызывает метод `_exec` с указанием ресурса, метода `POST`, данных и формата данных.
2.  Возвращает ответ от API.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products').
-   `data` (dict): Данные для нового ресурса.

**Возвращает**:

-   `dict`: Ответ от API.

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
        return await self._exec(resource=resource, resource_id=resource_id, method='GET', io_format= self.data_format)
```

**Назначение**:
Чтение ресурса из API PrestaShop асинхронно.

**Как работает функция**:

1.  Вызывает метод `_exec` с указанием ресурса, ID ресурса, метода `GET` и формата данных.
2.  Возвращает ответ от API.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products').
-   `resource_id` (int | str): ID ресурса.

**Возвращает**:

-   `dict`: Ответ от API.

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
        return await self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data,
                          io_format=self.data_format)
```

**Назначение**:
Обновление существующего ресурса в API PrestaShop асинхронно.

**Как работает функция**:

1.  Вызывает метод `_exec` с указанием ресурса, ID ресурса (из данных), метода `PUT`, данных и формата данных.
2.  Возвращает ответ от API.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products').
-   `data` (dict): Данные для ресурса.

**Возвращает**:

-   `dict`: Ответ от API.

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
        return await self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)
```

**Назначение**:
Удаление ресурса из API PrestaShop асинхронно.

**Как работает функция**:

1.  Вызывает метод `_exec` с указанием ресурса, ID ресурса, метода `DELETE` и формата данных.
2.  Возвращает `True`, если удаление успешно, иначе `False`.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products').
-   `resource_id` (int | str): ID ресурса.

**Возвращает**:

-   `bool`: `True`, если успешно, `False` иначе.

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
        return await self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)
```

**Назначение**:
Поиск ресурсов в API PrestaShop асинхронно.

**Как работает функция**:

1.  Вызывает метод `_exec` с указанием ресурса, фильтра поиска, метода `GET`, формата данных и дополнительных аргументов.
2.  Возвращает список ресурсов, соответствующих критериям поиска.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products').
-   `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:

-   `List[dict]`: Список ресурсов, соответствующих критериям поиска.

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
        with open(file_path, 'rb') as file:
            headers = {'Content-Type': 'application/octet-stream'}
            async with self.client.post(
                url=f'{self.API_DOMAIN}{resource}',
                headers=headers,
                data=file.read()
            ) as response:

               return response.json()
```

**Назначение**:
Загрузка бинарного файла в ресурс API PrestaShop асинхронно.

**Как работает функция**:

1.  Открывает файл в бинарном режиме для чтения.
2.  Устанавливает заголовок `Content-Type` как `application/octet-stream`.
3.  Выполняет `POST` запрос к указанному ресурсу API с телом файла.
4.  Возвращает JSON ответ от API.

**Параметры**:

-   `resource` (str): API ресурс (например, 'images/products/22').
-   `file_path` (str): Путь к бинарному файлу.
-   `file_name` (str): Имя файла.

**Возвращает**:

-   `dict`: Ответ от API.

### `_save`

```python
    def _save(self, file_name: str, data: dict):
        """! Save data to a file.

        Args:
            file_name (str): Name of the file.
            data (dict): Data to be saved.
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))
```

**Назначение**:
Сохранение данных в файл.

**Как работает функция**:

1.  Сохраняет данные в файл с указанным именем, используя `j_dumps` для преобразования данных в JSON с отступами и отключенным ASCII.
2.  Использует функцию `save_text_file` для сохранения текста в файл.

**Параметры**:

-   `file_name` (str): Имя файла.
-   `data` (dict): Данные для сохранения.

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
        data = await self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False
```

**Назначение**:
Получение данных из ресурса API PrestaShop и сохранение их асинхронно.

**Как работает функция**:

1.  Вызывает метод `_exec` для получения данных из API.
2.  Если данные получены, сохраняет их в файл с именем `{resource}.json` с помощью метода `_save`.
3.  Возвращает полученные данные.
4.  Если данные не получены, возвращает `False`.

**Параметры**:

-   `resource` (str): API ресурс (например, 'products').
-   `**kwargs`: Дополнительные аргументы для API запроса.

**Возвращает**:

-   `dict | None`: Данные из API или `False` в случае неудачи.

### `remove_file`

```python
    def remove_file(self, file_path: str):
        """! Remove a file from the filesystem.

        Args:
            file_path (str): Path to the file.
        """
        try:
            os.remove(file_path)
        except Exception as ex:
            logger.error(f'Error removing file {file_path}: {ex}')
```

**Назначение**:
Удаление файла из файловой системы.

**Как работает функция**:

1.  Пытается удалить файл по указанному пути с помощью `os.remove`.
2.  В случае ошибки регистрирует ошибку с использованием