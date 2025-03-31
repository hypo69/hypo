# Модуль `api_async`

## Обзор

Модуль `api_async` предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с API PrestaShop, используя JSON и XML. Этот класс обеспечивает асинхронные методы для выполнения CRUD-операций, поиска и загрузки изображений. Также, в классе реализована обработка ошибок и методы для управления данными API.

## Подробнее

Модуль предназначен для асинхронного взаимодействия с API PrestaShop, что позволяет выполнять запросы не блокируя основной поток выполнения. Это особенно полезно для приложений, требующих высокой производительности и отзывчивости.

## Содержание

- [Классы](#Классы)
    - [Format](#Format)
    - [PrestaShopAsync](#PrestaShopAsync)
- [Функции](#Функции)

## Классы

### `Format`

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

**Описание**:
Перечисление, определяющее форматы данных, возвращаемые API (JSON, XML).

### `PrestaShopAsync`

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

    async def create(self, resource: str, data: dict) -> Optional[dict]:
        """! Create a new resource in PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the new resource.

        Returns:
             dict: Response from the API.
        """
        return await self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
        """! Read a resource from the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            dict: Response from the API.
        """
        return await self._exec(resource=resource, resource_id=resource_id, method='GET', io_format= self.data_format)

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

    async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
        """! Delete a resource from the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            bool: `True` if successful, `False` otherwise.
        """
        return await self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
        """! Search for resources in the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            filter (str | dict, optional): Filter for the search.

        Returns:
             List[dict]: List of resources matching the search criteria.
        """
        return await self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)

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

    def _save(self, file_name: str, data: dict):
        """! Save data to a file.

        Args:
            file_name (str): Name of the file.
            data (dict): Data to be saved.
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

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

    def remove_file(self, file_path: str):
        """! Remove a file from the filesystem.

        Args:
            file_path (str): Path to the file.
        """
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f'Error removing file {file_path}: {e}')

    async def get_apis(self) -> Optional[dict]:
        """! Get a list of all available APIs asynchronously.

        Returns:
             dict: List of available APIs.
        """
        return await self._exec('apis', method='GET', io_format=self.data_format)

    async def get_languages_schema(self) -> Optional[dict]:
        """! Get the schema for languages asynchronously.

        Returns:
            dict: Language schema or `None` on failure.
        """
        try:
            response = await self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f'Error: {ex}')
            return

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
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = await save_image_from_url(img_url, filename)
        response = await self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

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
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = await save_image_from_url(img_url, filename)
        response = await self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

    async def get_product_images(self, product_id: int) -> Optional[dict]:
        """! Get images for a product asynchronously.

        Args:
            product_id (int): Product ID.

        Returns:
            dict | None: List of product images or `False` on failure.
        """
        return await self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)
```

**Описание**:
Асинхронный класс для взаимодействия с API PrestaShop.

**Как работает класс**:

1.  **Инициализация**:
    *   При инициализации класса `PrestaShopAsync` задаются основные параметры для работы с API PrestaShop, такие как домен API, ключ API, формат данных и режим отладки.
    *   Создается клиентская сессия `ClientSession` для выполнения асинхронных запросов с использованием аутентификации на основе API-ключа.
2.  **Основные методы**:
    *   `ping`: Проверяет доступность веб-сервиса PrestaShop.
    *   `create`, `read`, `write`, `unlink`: Выполняют CRUD-операции (создание, чтение, обновление, удаление) ресурсов PrestaShop.
    *   `search`: Поиск ресурсов в PrestaShop API с использованием фильтров.
    *   `create_binary`: Загружает бинарные файлы (например, изображения) в API PrestaShop.
    *   `get_data`: Получает данные из API PrestaShop и сохраняет их в файл.
    *   `upload_image`, `upload_image_async`: Загружает изображения в API PrestaShop.
3.  **Внутренние методы**:
    *   `_exec`: Выполняет HTTP-запросы к API PrestaShop. Поддерживает различные HTTP-методы, форматы данных и параметры запросов.
    *   `_prepare`: Подготавливает URL для запроса, добавляя параметры.
    *   `_check_response`: Проверяет статус ответа от API и обрабатывает ошибки.
    *   `_parse_response_error`: Разбирает ошибки, полученные от API PrestaShop, и логирует их.
    *   `_parse`: Разбирает XML или JSON ответы от API.

**Методы**:

*   `__init__(self, api_domain: str, api_key: str, data_format: str = 'JSON', debug: bool = True) -> None`

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
    Инициализирует класс `PrestaShopAsync`.

    **Как работает метод**:

    1.  Присваивает значения атрибутам экземпляра класса на основе переданных аргументов: `api_domain`, `api_key`, `debug` и `data_format`.
    2.  Создает экземпляр `ClientSession` из библиотеки `aiohttp` для асинхронных HTTP-запросов. В `ClientSession` устанавливается базовая аутентификация с использованием API-ключа и таймаут для запросов.

    **Параметры**:

    *   `api_domain` (str): Домен API PrestaShop.
    *   `api_key` (str): Ключ API для аутентификации.
    *   `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
    *   `debug` (bool, optional): Включает режим отладки. По умолчанию `True`.

    **Вызывает исключения**:

    *   `PrestaShopAuthenticationError`: Если API-ключ неверен или не существует.
    *   `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

*   `ping(self) -> bool`

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
    Проверяет работоспособность веб-сервиса асинхронно.

    **Как работает метод**:

    1.  Отправляет `HEAD` запрос к домену API, используя асинхронный клиент `self.client`.
    2.  Вызывает метод `self._check_response` для проверки статуса ответа.
    3.  Возвращает `True`, если веб-сервис работает, иначе `False`.

    **Возвращает**:

    *   `bool`: Результат проверки веб-сервиса. Возвращает `True`, если веб-сервис работает, иначе `False`.

*   `_check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None) -> bool`

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
    Проверяет код состояния HTTP-ответа и обрабатывает ошибки асинхронно.

    **Как работает метод**:

    1.  Проверяет, находится ли код состояния HTTP-ответа (`status_code`) в диапазоне успешных кодов (200 или 201).
    2.  Если код состояния успешен, возвращает `True`.
    3.  В противном случае вызывает метод `self._parse_response_error` для обработки ошибки и возвращает `False`.

    **Параметры**:

    *   `status_code` (int): Код состояния HTTP-ответа.
    *   `response`: Объект HTTP-ответа.
    *   `method` (str, optional): HTTP-метод, использованный для запроса.
    *   `url` (str, optional): URL запроса.
    *   `headers` (dict, optional): Заголовки запроса.
    *   `data` (dict, optional): Данные, отправленные в запросе.

    **Возвращает**:

    *   `bool`: `True`, если код состояния 200 или 201, иначе `False`.

*   `_parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None)`

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
    Асинхронно разбирает ответ об ошибке от API PrestaShop.

    **Как работает метод**:

    1.  Проверяет формат данных (`self.data_format`).
    2.  Если формат данных `JSON`:
        *   Получает код состояния HTTP-ответа.
        *   Если код состояния не 200 и не 201, получает текст ответа и логирует критическую информацию, такую как код состояния, URL, заголовки и текст ответа.
        *   Возвращает объект ответа.
    3.  Если формат данных не `JSON` (предположительно `XML`):
        *   Вызывает метод `self._parse` для разбора текста ответа.
        *   Если результат разбора является словарем, извлекает код и сообщение об ошибке из структуры ответа.
        *   Если результат разбора является элементом `ElementTree`, извлекает код и сообщение об ошибке из XML-структуры.
        *   Логирует сообщение об ошибке и код.
        *   Возвращает код и сообщение об ошибке.

    **Параметры**:

    *   `response`: Объект HTTP-ответа от сервера.
    *   `method` (str, optional): HTTP-метод, использованный для запроса.
    *   `url` (str, optional): URL запроса.
    *   `headers` (dict, optional): Заголовки запроса.
    *   `data` (dict, optional): Данные, отправленные в запросе.

*   `_prepare(self, url: str, params: dict) -> str`

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
    Подготавливает URL для запроса.

    **Как работает метод**:

    1.  Создает объект `PreparedRequest`.
    2.  Использует метод `prepare_url` объекта `PreparedRequest` для добавления параметров к базовому URL.
    3.  Возвращает подготовленный URL.

    **Параметры**:

    *   `url` (str): Базовый URL.
    *   `params` (dict): Параметры для запроса.

    **Возвращает**:

    *   `str`: