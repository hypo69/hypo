### Анализ кода модуля `api_async`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Асинхронная работа с API.
    - Разделение на методы для различных операций с API.
    - Обработка ошибок с использованием логгера.
    - Использование `j_loads` и `j_dumps` для работы с JSON.
    - Использование `aiohttp` для асинхронных запросов.
- **Минусы**:
    - Дублирование кода в методах `upload_image_async` и `upload_image`.
    - Непоследовательное использование `logger.error` и `raise Exception`.
    - Избыточное использование `try-except` в некоторых местах.
    - Жестко заданные форматы данных (JSON, XML) вместо использования enum.
    - Присутствие закомментированного кода и неиспользуемых импортов.
    - Не все функции и методы имеют полную RST документацию.
    - Не всегда используются f-строки для форматирования логов.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Отсутствуют проверки на валидность входных данных.

**Рекомендации по улучшению**:

-  Удалить дублирование кода в методах `upload_image_async` и `upload_image`, вынеся общий функционал в отдельный метод.
-  Заменить использование `try-except` на более точное логирование ошибок через `logger.error` или `logger.critical` с последующим возвращением `False`.
-  Использовать enum для форматов данных `JSON` и `XML`.
-  Удалить неиспользуемые импорты, такие как `header`.
-  Добавить RST-документацию для всех методов и классов, в том числе с примерами использования.
-  Использовать f-строки для форматирования сообщений в логах.
-  Использовать `from src.logger.logger import logger` для импорта логгера.
-  Добавить проверку на валидность входных данных, где это необходимо.
-  Улучшить обработку ошибок: вместо возврата кортежей `(code, message)` возвращать `False` после логирования ошибки.
-  Удалить закомментированный код.
-  Форматирование кода с использованием PEP8.
-  В методе `_parse_response_error` в случае `self.data_format == 'JSON'` не возвращать `response`, а логировать и возвращать `False`.

**Оптимизированный код**:

```python
import os
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

import aiohttp
from aiohttp import ClientSession, ClientTimeout
from requests.models import PreparedRequest

from src import gs  # Сохраняем импорт gs
from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException
from src.logger.logger import logger
from src.utils.convertors.dict import dict2xml
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.file import save_text_file
from src.utils.image import save_image_from_url

class Format(Enum):
    """Data types return (JSON, XML)

    .. deprecated::
        I prefer JSON 👍 :))

    :param Enum: (int): 1 => JSON, 2 => XML
    """
    JSON = 'JSON'
    XML = 'XML'


class PrestaShopAsync:
    """! Async Class for interacting with the PrestaShop API using JSON and XML.

    This class provides asynchronous methods to interact with the PrestaShop API,
    allowing for CRUD operations, searching, and uploading images. It also provides
    error handling for responses and methods to handle the API’s data.

    Example usage:

    .. code-block:: python

        async def main():
            api = PrestaShopAsync(
                API_DOMAIN='https://your-prestashop-domain.com',
                API_KEY='your_api_key',
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
            import asyncio
            asyncio.run(main())

    """
    client: ClientSession = None
    debug = True
    lang_index: Optional[int] = 1
    data_format: str = 'JSON'
    ps_version = ''
    API_DOMAIN: str = None
    API_KEY: str = None

    def __init__(self,
                 api_domain: str,
                 api_key: str,
                 data_format: str = 'JSON',
                 debug: bool = True) -> None:
        """! Initialize the PrestaShopAsync class.

        :param api_domain: The domain of the PrestaShop API.
        :type api_domain: str
        :param api_key: The API key for authentication.
        :type api_key: str
        :param data_format: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
        :type data_format: str, optional
        :param debug: Activate debug mode. Defaults to True.
        :type debug: bool, optional
        :raises PrestaShopAuthenticationError: When the API key is wrong or does not exist.
        :raises PrestaShopException: For generic PrestaShop WebServices errors.

        Example:
            >>> api = PrestaShopAsync(api_domain='https://your-prestashop.com', api_key='your_api_key', data_format='JSON', debug=True)
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

        :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        :rtype: bool

        Example:
            >>> api = PrestaShopAsync(api_domain='https://your-prestashop.com', api_key='your_api_key', data_format='JSON', debug=True)
            >>> result = await api.ping()
            >>> print(result)
            True
        """
        async with self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        ) as response:
            return await self._check_response(response.status, response)

    async def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
                        headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
        """! Check the response status code and handle errors asynchronously.

        :param status_code: HTTP response status code.
        :type status_code: int
        :param response: HTTP response object.
        :type response: aiohttp.ClientResponse
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
        if status_code in (200, 201):
            return True
        else:
            await self._parse_response_error(response, method, url, headers, data)
            return False

    async def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
        """! Parse the error response from PrestaShop API asynchronously.

        :param response: HTTP response object from the server.
        :type response: aiohttp.ClientResponse
        :param method: HTTP method used for the request.
        :type method: str, optional
        :param url: The URL of the request.
        :type url: str, optional
        :param headers: The headers used in the request.
        :type headers: dict, optional
        :param data: The data sent in the request.
        :type data: dict, optional
        :return: `False` after logging the error.
        :rtype: bool
        """
        if self.data_format == 'JSON':
            status_code = response.status
            if not status_code in (200, 201):
                text = await response.text()
                logger.critical(f'response status code: {status_code}\n'
                                f'url: {response.request_info.url}\n'
                                f'--------------\n'
                                f'headers: {response.headers}\n'
                                f'--------------\n'
                                f'response text: {text}')
            return False
        else:
            error_answer = await self._parse(await response.text())
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
                if error is not None:
                    code = error.find('code').text
                    message = error.find('message').text
                else:
                     logger.error(f'XML response error: Cannot parse error')
                     return False
            else:
                 logger.error(f'XML response error: Cannot parse error')
                 return False
            logger.error(f'XML response error: {message} \n Code: {code}')
            return False

    def _prepare(self, url: str, params: dict) -> str:
        """! Prepare the URL for the request.

        :param url: The base URL.
        :type url: str
        :param params: The parameters for the request.
        :type params: dict
        :return: The prepared URL with parameters.
        :rtype: str
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

        :param resource: The API resource (e.g., 'products', 'categories').
        :type resource: str
        :param resource_id: The ID of the resource.
        :type resource_id: int | str, optional
        :param resource_ids: The IDs of multiple resources.
        :type resource_ids: int | tuple, optional
        :param method: The HTTP method (GET, POST, PUT, DELETE).
        :type method: str, optional
        :param data: The data to be sent with the request.
        :type data: dict, optional
        :param headers: Additional headers for the request.
        :type headers: dict, optional
        :param search_filter: Filter for the request.
        :type search_filter: str | dict, optional
        :param display: Fields to display in the response.
        :type display: str | list, optional
        :param schema: The schema of the data.
        :type schema: str, optional
        :param sort: Sorting parameter for the request.
        :type sort: str, optional
        :param limit: Limit of results for the request.
        :type limit: str, optional
        :param language: The language ID for the request.
        :type language: int, optional
        :param io_format: The data format ('JSON' or 'XML').
        :type io_format: str, optional
        :return: The response from the API or `False` on failure.
        :rtype: dict | None
        """
        prepared_url = self._prepare(f'{self.API_DOMAIN}/api/{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}/api/{resource}',
                                  {'filter': search_filter,
                                   'display': display,
                                   'schema': schema,
                                   'sort': sort,
                                   'limit': limit,
                                   'language': language,
                                   'output_format': io_format})

        request_data = dict2xml(data) if data and io_format == 'XML' else data
        try:
          if self.debug:
              import sys
              original_stderr = sys.stderr
              f = open('stderr.log', 'w')
              sys.stderr = f


              async with self.client.request(
                  method=method,
                  url=prepared_url,
                  data=request_data,
                  headers=headers,
              ) as response:
                  sys.stderr = original_stderr
                  if not await self._check_response(response.status, response, method, prepared_url, headers, request_data):
                      return False

                  if io_format == 'JSON':
                      return await response.json()
                  else:
                      return await self._parse(await response.text())
          else:

              async with self.client.request(
                  method=method,
                  url=prepared_url,
                  data=request_data,
                  headers=headers,
              ) as response:
                  if not await self._check_response(response.status, response, method, prepared_url, headers, request_data):
                      return False

                  if io_format == 'JSON':
                      return await response.json()
                  else:
                      return await self._parse(await response.text())
        except Exception as e:
            logger.error(f'Error during API request: {e}')
            return False


    async def _parse(self, text: str) -> Union[dict, ElementTree.Element, bool]:
        """! Parse XML or JSON response from the API asynchronously.

        :param text: Response text.
        :type text: str
        :return: Parsed data or `False` on failure.
        :rtype: dict | ElementTree.Element | bool
        """
        try:
            if self.data_format == 'JSON':
              data = await j_loads(text)
              return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
            logger.error(f'Parsing Error: {ex}')
            return False

    async def create(self, resource: str, data: dict) -> Optional[dict]:
        """! Create a new resource in PrestaShop API asynchronously.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param data: Data for the new resource.
        :type data: dict
        :return: Response from the API or `False` on failure.
        :rtype: dict
        """
        return await self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
        """! Read a resource from the PrestaShop API asynchronously.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param resource_id: Resource ID.
        :type resource_id: int | str
        :return: Response from the API or `False` on failure.
        :rtype: dict
        """
        return await self._exec(resource=resource, resource_id=resource_id, method='GET', io_format= self.data_format, **kwargs)

    async def write(self, resource: str, data: dict) -> Optional[dict]:
        """! Update an existing resource in the PrestaShop API asynchronously.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param data: Data for the resource.
        :type data: dict
        :return: Response from the API or `False` on failure.
        :rtype: dict
        """
        if 'id' not in data:
            logger.error('Error: \'id\' key not found in data for update operation')
            return False
        return await self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data,
                          io_format=self.data_format)

    async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
        """! Delete a resource from the PrestaShop API asynchronously.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param resource_id: Resource ID.
        :type resource_id: int | str
        :return: `True` if successful, `False` otherwise.
        :rtype: bool
        """
        return await self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
        """! Search for resources in the PrestaShop API asynchronously.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param filter: Filter for the search.
        :type filter: str | dict, optional
        :return: List of resources matching the search criteria.
        :rtype: List[dict]
        """
        return await self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)

    async def create_binary(self, resource: str, file_path: str, file_name: str) -> Optional[dict]:
        """! Upload a binary file to a PrestaShop API resource asynchronously.

        :param resource: API resource (e.g., 'images/products/22').
        :type resource: str
        :param file_path: Path to the binary file.
        :type file_path: str
        :param file_name: File name.
        :type file_name: str
        :return: Response from the API or `False` on failure.
        :rtype: dict
        """
        try:
            with open(file_path, 'rb') as file:
                headers = {'Content-Type': 'application/octet-stream'}
                async with self.client.post(
                    url=f'{self.API_DOMAIN}{resource}',
                    headers=headers,
                    data=file.read()
                ) as response:
                    if response.status in (200, 201):
                        return await response.json()
                    else:
                        logger.error(f'Error during binary upload, Status code: {response.status}')
                        return False
        except Exception as e:
            logger.error(f'Error during binary upload: {e}')
            return False

    def _save(self, file_name: str, data: dict) -> None:
        """! Save data to a file.

        :param file_name: Name of the file.
        :type file_name: str
        :param data: Data to be saved.
        :type data: dict
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
        """! Fetch data from a PrestaShop API resource and save it asynchronously.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param **kwargs: Additional arguments for the API request.
        :type **kwargs: dict
        :return: Data from the API or `False` on failure.
        :rtype: dict | None
        """
        data = await self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False

    def remove_file(self, file_path: str) -> None:
        """! Remove a file from the filesystem.

        :param file_path: Path to the file.
        :type file_path: str
        """
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f'Error removing file {file_path}: {e}')

    async def get_apis(self) -> Optional[dict]:
        """! Get a list of all available APIs asynchronously.

        :return: List of available APIs or `False` on failure.
        :rtype: dict | None
        """
        return await self._exec('apis', method='GET', io_format=self.data_format)

    async def get_languages_schema(self) -> Optional[dict]:
        """! Get the schema for languages asynchronously.

        :return: Language schema or `False` on failure.
        :rtype: dict | None
        """
        try:
            response = await self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f'Error: {ex}')
            return False

    async def _upload_image(self, resource: str, resource_id: int, img_url: str,
                           img_name: Optional[str] = None) -> Optional[dict]:
        """! Upload an image to PrestaShop API asynchronously.

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
        try:
            url_parts = img_url.rsplit('.', 1)
            extension = url_parts[1] if len(url_parts) > 1 else ''
            filename = f'{resource_id}_{img_name}.{extension}' if img_name else f'{resource_id}.{extension}'
            png_file_path = await save_image_from_url(img_url, filename)
            if png_file_path:
                response = await self.create_binary(resource, png_file_path, filename)
                self.remove_file(png_file_path)
                return response
            else:
                 return False
        except Exception as e:
            logger.error(f'Error uploading image: {e}')
            return False

    async def upload_image_async(self, resource: str, resource_id: int, img_url: str,
                           img_name: Optional[str] = None) -> Optional[dict]:
        """! Upload an image to PrestaShop API asynchronously.

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
        return await self._upload_image(resource, resource_id, img_url, img_name)


    async def upload_image(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]:
        """! Upload an image to PrestaShop API asynchronously.

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
        return await self._upload_image(resource, resource_id, img_url, img_name)

    async def get_product_images(self, product_id: int) -> Optional[dict]:
        """! Get images for a product asynchronously.

        :param product_id: Product ID.
        :type product_id: int
        :return: List of product images or `False` on failure.
        :rtype: dict | None
        """
        return await self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)