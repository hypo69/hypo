## Анализ кода модуля `api_async.py`

**Расположение файла:** `hypotez/src/endpoints/prestashop/api/api_async.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Асинхронность: Использование `aiohttp` для асинхронных запросов.
  - Четкая структура: Класс `PrestaShopAsync` предоставляет методы для CRUD операций.
  - Использование enum: Класс `Format` для определения формата данных.
  - Обработка ошибок: Присутствуют методы для проверки ответа и обработки ошибок.
  - Документация: Наличие docstring для классов и методов.
- **Минусы**:
  - Неполная документация: Отсутствуют примеры использования методов в docstring.
  - Неконсистентность: Использование как `j_loads`, так и `json.loads` (в `create_binary`).
  - Дублирование кода: Методы `upload_image_async` и `upload_image` практически идентичны.
  - Отсутствие обработки исключений: В некоторых методах отсутствуют блоки `try...except` для обработки возможных ошибок.
  - Игнорирование debug режима: Большой блок кода, закомментирован, что затрудняет понимание логики работы в режиме отладки.

**Рекомендации по улучшению:**

1.  **Документация**:
    *   Добавить примеры использования для каждого метода в docstring.
    *   Описать возможные исключения, которые могут быть выброшены.
    *   Для класса `PrestaShopAsync` добавить примеры инициализации и использования.

2.  **Использование `j_loads`**:
    *   Заменить `response.json()` на `j_loads(response.text())` или `j_loads_ns(response.text())` для единообразия.

3.  **Удаление дублирования кода**:
    *   Удалить один из методов `upload_image_async` или `upload_image` и использовать один метод с параметром для указания, выполнять ли асинхронную операцию.

4.  **Обработка исключений**:
    *   Добавить блоки `try...except` в методы, где это необходимо, для обработки возможных ошибок (например, в `create_binary`).
    *   Использовать `logger.error` для записи ошибок с трассировкой (`exc_info=True`).

5.  **Отладка**:
    *   Удалить закомментированный код в методе `_exec` или переписать его, используя условную компиляцию для отладки.

6.  **Форматирование**:
    *   Убедиться, что весь код соответствует PEP8.

7.  **Типизация**:
    *   Убедиться, что все переменные и параметры аннотированы типами.

8.  **Логирование**:
    *   Добавить логирование в ключевые моменты выполнения кода (например, при создании, чтении, записи и удалении ресурсов).

**Оптимизированный код:**

```python
import asyncio
import os
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

import aiohttp
from aiohttp import ClientSession, ClientTimeout
from requests import Session
from requests.models import PreparedRequest

from src import gs
from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException
from src.logger.logger import logger
from src.utils.convertors.base64 import base64_to_tmpfile
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.file import save_text_file
from src.utils.image import save_image_from_url_async
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint


class Format(Enum):
    """Data types return (JSON, XML)

    .. deprecated::
        I prefer JSON 👍 :))

    :param Enum: (int): 1 => JSON, 2 => XML
    """

    JSON = 'JSON'
    XML = 'XML'


class PrestaShopAsync:
    """Async Class for interacting with the PrestaShop API using JSON and XML.

    This class provides asynchronous methods to interact with the PrestaShop API,
    allowing for CRUD operations, searching, and uploading images. It also provides
    error handling for responses and methods to handle the API's data.

    Example usage:

        async def main():
            api = PrestaShopAsync(
                api_domain='https://your-prestashop-domain.com',
                api_key='your_api_key',
                data_format='JSON',
                debug=True,
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
    debug: bool = False
    lang_index: Optional[int] = 1
    data_format: str = 'JSON'
    ps_version: str = ''
    API_DOMAIN: str = None
    API_KEY: str = None

    def __init__(
        self,
        api_domain: str,
        api_key: str,
        data_format: str = 'JSON',
        debug: bool = True,
    ) -> None:
        """Initialize the PrestaShopAsync class.

        Args:
            api_domain (str): The domain of the PrestaShop API.
            api_key (str): The API key for authentication.
            data_format (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
            debug (bool, optional): Activate debug mode. Defaults to True.

        Raises:
            PrestaShopAuthenticationError: When the API key is wrong or does not exist.
            PrestaShopException: For generic PrestaShop WebServices errors.

        Example:
            >>> api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
            >>> api.API_DOMAIN
            'https://your-prestashop-domain.com'
        """
        self.API_DOMAIN = api_domain
        self.API_KEY = api_key
        self.debug = debug
        self.data_format = data_format

        self.client = ClientSession(
            auth=aiohttp.BasicAuth(self.API_KEY, ''),
            timeout=ClientTimeout(total=60),
        )

    async def ping(self) -> bool:
        """Test if the webservice is working perfectly asynchronously.

        Returns:
            bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.

        Example:
            >>> api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
            >>> await api.ping()
            True
        """
        try:
            async with self.client.request(method='HEAD', url=self.API_DOMAIN) as response:
                return await self._check_response(response.status, response)
        except Exception as e:
            logger.error(f'Error during ping: {e}', exc_info=True)
            return False

    def _check_response(
        self,
        status_code: int,
        response: aiohttp.ClientResponse,
        method: Optional[str] = None,
        url: Optional[str] = None,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
    ) -> bool:
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
        if status_code in (200, 201):
            return True
        else:
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(
        self,
        response: aiohttp.ClientResponse,
        method: Optional[str] = None,
        url: Optional[str] = None,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        """Parse the error response from PrestaShop API asynchronously.

        Args:
            response (aiohttp.ClientResponse): HTTP response object from the server.
            method (str, optional): HTTP method used for the request.
            url (str, optional): The URL of the request.
            headers (dict, optional): The headers used in the request.
            data (dict, optional): The data sent in the request.
        """
        try:
            if self.data_format == 'JSON':
                status_code = response.status
                if not status_code in (200, 201):
                    text = await response.text()
                    logger.critical(
                        f"""response status code: {status_code}
                        url: {response.request_info.url}
                        --------------
                        headers: {response.headers}
                        --------------
                        response text: {text}"""
                    )
                return response
            else:
                error_answer = self._parse(await response.text())
                if isinstance(error_answer, dict):
                    error_content = (
                        error_answer.get('PrestaShop', {}).get('errors', {}).get('error', {})
                    )
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
        except Exception as ex:
            logger.error(f'Error parsing response error: {ex}', exc_info=True)

    def _prepare(self, url: str, params: dict) -> str:
        """Prepare the URL for the request.

        Args:
            url (str): The base URL.
            params (dict): The parameters for the request.

        Returns:
            str: The prepared URL with parameters.
        """
        req = PreparedRequest()
        req.prepare_url(url, params)
        return req.url

    async def _exec(
        self,
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
        io_format: str = 'JSON',
    ) -> Optional[dict]:
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
        self.debug = False
        try:
            prepared_url = self._prepare(
                f'{self.API_DOMAIN}{resource}/{resource_id}'
                if resource_id
                else f'{self.API_DOMAIN}{resource}',
                {
                    'filter': search_filter,
                    'display': display,
                    'schema': schema,
                    'sort': sort,
                    'limit': limit,
                    'language': language,
                    'output_format': io_format,
                },
            )

            request_data = dict2xml(data) if data and io_format == 'XML' else data

            async with self.client.request(
                method=method, url=prepared_url, data=request_data, headers=headers
            ) as response:
                if not self._check_response(
                    response.status, response, method, prepared_url, headers, request_data
                ):
                    return False

                if io_format == 'JSON':
                    return j_loads(await response.text())
                else:
                    return self._parse(await response.text())
        except Exception as ex:
            logger.error(f'Error executing request: {ex}', exc_info=True)
            return None

    def _parse(self, text: str) -> dict | ElementTree.Element | bool:
        """Parse XML or JSON response from the API asynchronously.

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
            logger.error(f'Parsing Error: {str(ex)}', exc_info=True)
            return False

    async def create(self, resource: str, data: dict) -> Optional[dict]:
        """Create a new resource in PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the new resource.

        Returns:
             dict: Response from the API.
        """
        return await self._exec(
            resource=resource, method='POST', data=data, io_format=self.data_format
        )

    async def read(
        self, resource: str, resource_id: Union[int, str], **kwargs
    ) -> Optional[dict]:
        """Read a resource from the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            dict: Response from the API.
        """
        return await self._exec(
            resource=resource, resource_id=resource_id, method='GET', io_format=self.data_format
        )

    async def write(self, resource: str, data: dict) -> Optional[dict]:
        """Update an existing resource in the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the resource.

        Returns:
            dict: Response from the API.
        """
        return await self._exec(
            resource=resource,
            resource_id=data.get('id'),
            method='PUT',
            data=data,
            io_format=self.data_format,
        )

    async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
        """Delete a resource from the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            bool: `True` if successful, `False` otherwise.
        """
        return await self._exec(
            resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format
        )

    async def search(
        self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs
    ) -> List[dict]:
        """Search for resources in the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            filter (str | dict, optional): Filter for the search.

        Returns:
             List[dict]: List of resources matching the search criteria.
        """
        return await self._exec(
            resource=resource,
            search_filter=filter,
            method='GET',
            io_format=self.data_format,
            **kwargs,
        )

    async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
        """Upload a binary file to a PrestaShop API resource asynchronously.

        Args:
            resource (str): API resource (e.g., 'images/products/22').
            file_path (str): Path to the binary file.
            file_name (str): File name.

        Returns:
            dict: Response from the API.
        """
        try:
            with open(file_path, 'rb') as file:
                headers = {'Content-Type': 'application/octet-stream'}
                async with self.client.post(
                    url=f'{self.API_DOMAIN}{resource}', headers=headers, data=file.read()
                ) as response:
                    return j_loads(await response.text())
        except Exception as e:
            logger.error(f'Error creating binary: {e}', exc_info=True)
            return {}

    def _save(self, file_name: str, data: dict):
        """Save data to a file.

        Args:
            file_name (str): Name of the file.
            data (dict): Data to be saved.
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
        """Fetch data from a PrestaShop API resource and save it asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            **kwargs: Additional arguments for the API request.

        Returns:
            dict | None: Data from the API or `False` on failure.
        """
        data = await self._exec(
            resource=resource, method='GET', io_format=self.data_format, **kwargs
        )
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False

    def remove_file(self, file_path: str):
        """Remove a file from the filesystem.

        Args:
            file_path (str): Path to the file.
        """
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f'Error removing file {file_path}: {e}', exc_info=True)

    async def get_apis(self) -> Optional[dict]:
        """Get a list of all available APIs asynchronously.

        Returns:
             dict: List of available APIs.
        """
        return await self._exec('apis', method='GET', io_format=self.data_format)

    async def get_languages_schema(self) -> Optional[dict]:
        """Get the schema for languages asynchronously.

        Returns:
            dict: Language schema or `None` on failure.
        """
        try:
            response = await self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f'Error: {ex}', exc_info=True)
            return None

    async def upload_image(
        self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None
    ) -> Optional[dict]:
        """Upload an image to PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'images/products/22').
            resource_id (int): Resource ID.
            img_url (str): URL of the image.
            img_name (str, optional): Name of the image file, defaults to None.

        Returns:
            dict | None: Response from the API or `False` on failure.
        """
        try:
            url_parts = img_url.rsplit('.', 1)
            url_without_extension = url_parts[0]
            extension = url_parts[1] if len(url_parts) > 1 else ''
            filename = str(resource_id) + f'_{img_name}.{extension}'
            png_file_path = await save_image_from_url_async(img_url, filename)
            response = await self.create_binary(resource, png_file_path, img_name)
            self.remove_file(png_file_path)
            return response
        except Exception as e:
            logger.error(f'Error uploading image: {e}', exc_info=True)
            return None
```