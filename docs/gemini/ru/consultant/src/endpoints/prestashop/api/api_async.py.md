# Анализ кода модуля `api_async.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на методы, что облегчает его понимание и поддержку.
    - Используется асинхронный подход с `asyncio` и `aiohttp`, что обеспечивает неблокирующее выполнение сетевых запросов.
    - Присутствует обработка ошибок с помощью `try-except` и логирование, что повышает надежность кода.
    - Наличие документации для класса и методов в формате docstring.
-  Минусы
    - Некоторые комментарии после `#` не несут полезной информации.
    - В некоторых методах есть дублирование логики, например, в методах `upload_image_async` и `upload_image`.
    - Избыточное использование `try-except` в некоторых местах, что можно заменить на проверку условий.
    - Не везде используется `logger.error` для логирования ошибок.
    - Не все функции имеют docstring.

**Рекомендации по улучшению**

1. **Улучшить документацию**:
    - Добавить описание модуля в начале файла.
    - Добавить документацию для каждой функции, метода и переменной.
    - Следовать стандартам оформления docstring в Python (для Sphinx).
2. **Упростить обработку ошибок**:
    - Избегать избыточного использования `try-except`.
    - Использовать `logger.error` для логирования ошибок.
3. **Устранить дублирование кода**:
    - Вынести общую логику из `upload_image_async` и `upload_image` в отдельный метод.
4.  **Улучшить форматирование**:
    - Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
5.  **Добавить проверки**:
    -  Проверять `response.status` до `await response.json()` и `await response.text()`, чтобы избежать ошибок.
6.  **Использовать константы**:
     - Вынести магические строки, такие как 'JSON' и 'XML', в константы.
7. **Улучшить логирование**:
    - Добавить подробное логирование ошибок, включая URL, метод, заголовки и данные запроса.

**Оптимизированный код**

```python
"""
Модуль для асинхронного взаимодействия с PrestaShop API.
=========================================================================================

Этот модуль предоставляет класс :class:`PrestaShopAsync`, который позволяет асинхронно взаимодействовать с PrestaShop API,
используя JSON или XML для обмена данными. Поддерживаются CRUD-операции, поиск и загрузка изображений.

Пример использования:

.. code-block:: python

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
import os
import sys
from enum import Enum
from http.client import HTTPConnection
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from requests import Session
from requests.models import PreparedRequest

import header # импорт модуля header
from src import gs # импорт модуля gs
from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException # импорт исключений
from src.logger.logger import logger # импорт logger
from src.utils.convertors.base64 import base64_to_tmpfile # импорт base64_to_tmpfile
from src.utils.convertors.dict import dict2xml # импорт dict2xml
from src.utils.convertors.xml2dict import xml2dict # импорт xml2dict
from src.utils.file import save_text_file # импорт save_text_file
from src.utils.image import save_image_from_url # импорт save_image_from_url
from src.utils.jjson import j_dumps, j_loads, j_loads_ns # импорт j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint # импорт pprint

import asyncio
import aiohttp
from aiohttp import ClientSession, ClientTimeout

_JSON = 'JSON' # Константа для JSON
_XML = 'XML' # Константа для XML


class Format(Enum):
    """Data types return (JSON, XML)

    .. deprecated::
        I prefer JSON 👍 :))

    :param Enum: (int): 1 => JSON, 2 => XML
    """
    JSON = _JSON
    XML = _XML


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
    debug = True
    lang_index: Optional[int] = 1
    data_format:str = _JSON
    ps_version = ''
    API_DOMAIN:str = None
    API_KEY:str = None

    def __init__(self,
                api_domain:str,
                api_key:str,
                data_format: str = _JSON,
                debug: bool = True) -> None:
        """! Initialize the PrestaShopAsync class.

        Args:
            api_domain (str): The domain of the PrestaShop API.
            api_key (str): The API key for authentication.
            data_format (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
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
            # Проверка статуса ответа
            return await self._check_response(response.status, response)

    async def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
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
            # Обработка ошибки ответа
            await self._parse_response_error(response, method, url, headers, data)
            return False

    async def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
        """! Parse the error response from PrestaShop API asynchronously.

        Args:
            response (aiohttp.ClientResponse): HTTP response object from the server.
            method (str, optional): HTTP method used for the request.
            url (str, optional): The URL of the request.
            headers (dict, optional): The headers used in the request.
            data (dict, optional): The data sent in the request.
        """
        status_code = response.status # Получение статуса ответа
        if self.data_format == _JSON:
             # Если формат JSON
            if not status_code in (200, 201):
                text = await response.text()
                logger.critical(f"""response status code: {status_code}\n
                    url: {response.request_info.url}\n
                    --------------\n
                    headers: {response.headers}\n
                    --------------\n
                    response text: {text}""")
            return response
        else:
            # Если формат XML
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
                if error:
                    code = error.find('code').text
                    message = error.find('message').text
                else:
                    code = 'Unknown'
                    message = 'Unknown error'
            else:
                  code = 'Unknown'
                  message = 'Unknown error'
            logger.error(f'XML response error: {message} \\n Code: {code}')
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
              io_format: str = _JSON) -> Optional[dict]:
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
        prepared_url = self._prepare(f'{self.API_DOMAIN}/api/{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}/api/{resource}',
                                  {'filter': search_filter,
                                   'display': display,
                                   'schema': schema,
                                   'sort': sort,
                                   'limit': limit,
                                   'language': language,
                                   'output_format': io_format})

        request_data = dict2xml(data) if data and io_format == _XML else data
        if self.debug:
            # Логирование запроса и ответа при debug=True
            original_stderr = sys.stderr
            with open('stderr.log', 'w') as f:
                sys.stderr = f
                try:
                   async with self.client.request(
                        method=method,
                        url=prepared_url,
                        data=request_data,
                        headers=headers,
                    ) as response:
                        sys.stderr = original_stderr
                        if not await self._check_response(response.status, response, method, prepared_url, headers, request_data):
                             return False
                        if io_format == _JSON:
                            return await response.json()
                        else:
                            return await self._parse(await response.text())
                except Exception as ex:
                     sys.stderr = original_stderr
                     logger.error(f'Error in _exec debug mode: {ex}')
                     return None

        else:
             try:
               async with self.client.request(
                    method=method,
                    url=prepared_url,
                    data=request_data,
                    headers=headers,
                ) as response:
                  if not await self._check_response(response.status, response, method, prepared_url, headers, request_data):
                     return False

                  if io_format == _JSON:
                      return await response.json()
                  else:
                      return await self._parse(await response.text())
             except Exception as ex:
                  logger.error(f'Error in _exec: {ex}')
                  return None


    async def _parse(self, text: str) -> Union[dict, ElementTree.Element, bool]:
        """! Parse XML or JSON response from the API asynchronously.

        Args:
            text (str): Response text.

        Returns:
            dict | ElementTree.Element | bool: Parsed data or `False` on failure.
        """
        try:
            if self.data_format == _JSON:
                # Пытается загрузить JSON и вернуть данные
                data = await j_loads(text)
                return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                # Пытается распарсить XML и вернуть дерево элементов
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
             # Логирование ошибки парсинга
            logger.error(f'Parsing Error: {ex}')
            return False

    async def create(self, resource: str, data: dict) -> Optional[dict]:
        """! Create a new resource in PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the new resource.

        Returns:
             dict: Response from the API.
        """
        # Выполнение запроса POST для создания ресурса
        return await self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
        """! Read a resource from the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            resource_id (int | str): Resource ID.

        Returns:
            dict: Response from the API.
        """
        # Выполнение запроса GET для чтения ресурса
        return await self._exec(resource=resource, resource_id=resource_id, method='GET', io_format= self.data_format, **kwargs)

    async def write(self, resource: str, data: dict) -> Optional[dict]:
        """! Update an existing resource in the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            data (dict): Data for the resource.

        Returns:
            dict: Response from the API.
        """
        # Выполнение запроса PUT для обновления ресурса
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
        # Выполнение запроса DELETE для удаления ресурса
        return await self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
        """! Search for resources in the PrestaShop API asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            filter (str | dict, optional): Filter for the search.

        Returns:
             List[dict]: List of resources matching the search criteria.
        """
        # Выполнение запроса GET с фильтром для поиска ресурсов
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
        # Открытие файла в бинарном режиме и отправка данных через POST запрос
        with open(file_path, 'rb') as file:
            headers = {'Content-Type': 'application/octet-stream'}
            async with self.client.post(
                url=f'{self.API_DOMAIN}{resource}',
                headers=headers,
                data=file.read()
            ) as response:
               return await response.json()

    def _save(self, file_name: str, data: dict):
        """! Save data to a file.

        Args:
            file_name (str): Name of the file.
            data (dict): Data to be saved.
        """
        # Сохранение данных в файл в формате JSON
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
        """! Fetch data from a PrestaShop API resource and save it asynchronously.

        Args:
            resource (str): API resource (e.g., 'products').
            **kwargs: Additional arguments for the API request.

        Returns:
            dict | None: Data from the API or `False` on failure.
        """
        # Получение данных и сохранение их в файл
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
        # Удаление файла, если он существует
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f'Error removing file {file_path}: {e}')

    async def get_apis(self) -> Optional[dict]:
        """! Get a list of all available APIs asynchronously.

        Returns:
             dict: List of available APIs.
        """
        # Получение списка доступных API
        return await self._exec('apis', method='GET', io_format=self.data_format)

    async def get_languages_schema(self) -> Optional[dict]:
        """! Get the schema for languages asynchronously.

        Returns:
            dict: Language schema or `None` on failure.
        """
        # Получение схемы языков
        try:
            response = await self._exec('languages', display='full', io_format=_JSON)
            return response
        except Exception as ex:
            logger.error(f'Error: {ex}')
            return

    async def _upload_image(self, resource: str, resource_id: int, img_url: str,
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
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}' if img_name else f'{resource_id}.{extension}'
        png_file_path = await save_image_from_url(img_url, filename)
        response = await self.create_binary(resource, png_file_path, filename)
        self.remove_file(png_file_path)
        return response


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
       # Загрузка изображения, используя общий метод
       return await self._upload_image(resource, resource_id, img_url, img_name)


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
       # Загрузка изображения, используя общий метод
       return await self._upload_image(resource, resource_id, img_url, img_name)

    async def get_product_images(self, product_id: int) -> Optional[dict]:
        """! Get images for a product asynchronously.

        Args:
            product_id (int): Product ID.

        Returns:
            dict | None: List of product images or `False` on failure.
        """
        # Получение изображений продукта
        return await self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)
```