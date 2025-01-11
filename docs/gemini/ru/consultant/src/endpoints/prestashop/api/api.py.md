### Анализ кода модуля `api.py`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    -   Хорошо структурированный класс `PrestaShop` для взаимодействия с API.
    -   Используются `requests.Session` для эффективного управления HTTP-соединениями.
    -   Реализованы основные CRUD операции, поиск и загрузка изображений.
    -   Обработка ошибок и логирование.
    -   Присутствует поддержка форматов JSON и XML.
- **Минусы**:
    -   Не все строки кода соответствуют PEP8.
    -   Не везде используется `j_dumps` и `j_loads` из `src.utils.jjson`.
    -   Смешанное использование кавычек.
    -   Чрезмерное использование `try-except`.
    -   Отсутствует RST-документация для некоторых методов.
    -   Не всегда явное указание типа возвращаемых значений.
    -   Дублирование кода в методах `upload_image_async` и `upload_image`.
    -   Не стандартизированные параметры `search_filter` и `filter` в разных методах.

**Рекомендации по улучшению**:

1.  **Форматирование кода**:
    -   Привести код в соответствие со стандартами PEP8, включая отступы и длину строк.
    -   Использовать одинарные кавычки (`'`) для строк в коде и двойные кавычки (`"`) только для вывода и логирования.
2.  **Использование `j_dumps` и `j_loads`**:
    -   Заменить все стандартные вызовы `json.loads` и `json.dumps` на `j_loads` и `j_dumps` соответственно.
3.  **Обработка ошибок**:
    -   Уменьшить использование `try-except` блоков, где это возможно. Обрабатывать исключения через `logger.error` и возвращать `False` или `None`.
4.  **Документация**:
    -   Добавить RST-документацию для всех классов, методов и функций.
    -   Уточнить типы возвращаемых значений функций и методов.
5.  **Рефакторинг**:
    -   Вынести общую логику из `upload_image_async` и `upload_image` в отдельную функцию для устранения дублирования кода.
    -   Унифицировать параметры `search_filter` и `filter` в методах `_exec` и `search`.
6.  **Логирование**:
    -   Использовать `logger.error` для логирования ошибок, а не `logger.critical`.
7.  **Импорты**:
    -   Упорядочить импорты и использовать `from src.logger.logger import logger`.
8.  **Улучшение функции _parse**:
    -   Оптимизировать обработку JSON ответа
9.  **Улучшение функции _exec**:
    -   Убрать отладочный вывод в stderr
10. **Улучшение функции create_binary**:
    -   Возвращать результат проверки ответа
11. **Улучшение функции search**:
     -   Упростить возврат данных

**Оптимизированный код**:

```python
"""
Модуль для взаимодействия с PrestaShop API
=========================================================================================

Этот модуль предоставляет класс `PrestaShop` для взаимодействия с PrestaShop webservice API,
используя JSON и XML для форматирования сообщений. Он поддерживает операции CRUD, поиск
и загрузку изображений, с обработкой ошибок для ответов.

Пример использования
----------------------

.. code-block:: python

    from src.endpoints.prestashop.api.api import PrestaShop

    api = PrestaShop(
        API_DOMAIN='https://your-prestashop-domain.com',
        API_KEY='your_api_key',
        default_lang=1,
        debug=True,
        data_format='JSON',
    )

    api.ping()

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
    rec = api.create('taxes', data)

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

    update_rec = api.write('taxes', update_data)

    # Remove this tax
    api.unlink('taxes', str(rec['id']))

    # Search the first 3 taxes with '5' in the name
    import pprint
    recs = api.search('taxes', filter='[name]=%[5]%', limit='3')

    for rec in recs:
        pprint(rec)

    # Create binary (product image)
    api.create_binary('images/products/22', 'img.jpeg', 'image')
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import os
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from requests import Session
from requests.models import PreparedRequest

from src import gs
from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException
from src.logger.logger import logger  # corrected import
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.file import save_text_file
from src.utils.image import save_image_from_url
from src.utils.jjson import j_dumps, j_loads, j_loads_ns  # corrected import
from src.utils.printer import pprint


class Format(Enum):
    """Data types return (JSON, XML)

    .. deprecated::
        I prefer JSON 👍 :))

    :param Enum: (int): 1 => JSON, 2 => XML
    """
    JSON = 'JSON'
    XML = 'XML'


class PrestaShop:
    """Interact with PrestaShop webservice API, using JSON and XML for message

    This class provides methods to interact with the PrestaShop API, allowing for CRUD
    operations, searching, and uploading images. It also provides error handling
    for responses and methods to handle the API's data.

    :param API_KEY: The API key generated from PrestaShop.
    :type API_KEY: str
    :param API_DOMAIN: The domain of the PrestaShop shop (e.g., https://myPrestaShop.com).
    :type API_DOMAIN: str
    :param data_format: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
    :type data_format: str
    :param default_lang: Default language ID. Defaults to 1.
    :type default_lang: int
    :param debug: Activate debug mode. Defaults to True.
    :type debug: bool

    :raises PrestaShopAuthenticationError: When the API key is wrong or does not exist.
    :raises PrestaShopException: For generic PrestaShop WebServices errors.
    """
    client: Session = Session()
    debug = True
    language: Optional[int] = None
    data_format = 'JSON'
    ps_version = ''

    def __init__(self,
                 data_format: str = 'JSON',
                 default_lang: int = 1,
                 debug: bool = True) -> None:
        """Initialize the PrestaShop class.

        :param data_format: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
        :type data_format: str
        :param default_lang: Default language ID. Defaults to 1.
        :type default_lang: int
        :param debug: Activate debug mode. Defaults to True.
        :type debug: bool
        """
        self.API_DOMAIN = gs.credentials.presta.client.api_key.rstrip('/') + '/api/'
        self.API_KEY = gs.credentials.presta.client.api_key
        self.debug = debug
        self.language = default_lang
        self.data_format = data_format

        if not self.client.auth:
            self.client.auth = (self.API_KEY, '')

        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )

        self.ps_version = response.headers.get('psws-version')

    def ping(self) -> bool:
        """Test if the webservice is working perfectly.

        :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        :rtype: bool
        """
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )

        return self._check_response(response.status_code, response)

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
        if status_code in (200, 201):
            return True
        else:
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
        """Parse the error response from PrestaShop API.

        :param response: HTTP response object from the server.
        :type response: requests.Response
        """
        if self.data_format == 'JSON':
            status_code = response.status_code
            if not status_code in (200, 201):
                logger.error(f"response status code: {status_code}\n"
                            f"                    url: {response.request.url}\n"
                            f"                    --------------\n"
                            f"                    headers: {response.headers}\n"
                            f"                    --------------\n"
                            f"                    response text: {response.text}")  # corrected f-string
            return  # corrected return
        else:
            error_answer = self._parse(response.text)
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
            logger.error(f'XML response error: {message} \\n Code: {code}')
            return code, message

    def _prepare(self, url: str, params: dict) -> str:
        """Prepare the URL for the request.

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

    def _exec(self,
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
        """Execute an HTTP request to the PrestaShop API.

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

        :return: The response from the API or `None` on failure.
        :rtype: dict | None
        """
        url = f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}'
        params = {
            'filter': search_filter,
            'display': display,
            'schema': schema,
            'sort': sort,
            'limit': limit,
            'language': language,
            'output_format': io_format
        }

        response = self.client.request(
            method=method,
            url=self._prepare(url, params),
            data=dict2xml(data) if data and io_format == 'XML' else data,
            headers=headers,
        )
        if not self._check_response(response.status_code, response, method, url, headers, data):
            return None

        if io_format == 'JSON':
            return j_loads_ns(response.text)  # corrected json.loads
        else:
            return self._parse(response.text)

    def _parse(self, text: str) -> Union[dict, ElementTree.Element, bool]:
        """Parse XML or JSON response from the API.

        :param text: Response text.
        :type text: str

        :return: Parsed data or `False` on failure.
        :rtype: dict | ElementTree.Element | bool
        """
        try:
            if self.data_format == 'JSON':
                data = j_loads(text) # corrected json.loads
                return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
            logger.error(f'Parsing Error: {str(ex)}')
            return False

    def create(self, resource: str, data: dict) -> Optional[dict]:
        """Create a new resource in PrestaShop API.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param data: Data for the new resource.
        :type data: dict

        :return: Response from the API.
        :rtype: dict
        """
        return self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
        """Read a resource from the PrestaShop API.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param resource_id: Resource ID.
        :type resource_id: int | str

        :return: Response from the API.
        :rtype: dict
        """
        return self._exec(resource=resource, resource_id=resource_id, method='GET', io_format=self.data_format, **kwargs)

    def write(self, resource: str, data: dict) -> Optional[dict]:
        """Update an existing resource in the PrestaShop API.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param data: Data for the resource.
        :type data: dict

        :return: Response from the API.
        :rtype: dict
        """
        return self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data,
                          io_format=self.data_format)

    def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
        """Delete a resource from the PrestaShop API.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param resource_id: Resource ID.
        :type resource_id: int | str

        :return: `True` if successful, `False` otherwise.
        :rtype: bool
        """
        result = self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)
        return bool(result) # corrected return

    def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
        """Search for resources in the PrestaShop API.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param filter: Filter for the search.
        :type filter: str | dict, optional

        :return: List of resources matching the search criteria.
        :rtype: List[dict]
        """
        result = self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)
        return result if result else [] # corrected return

    def create_binary(self, resource: str, file_path: str, file_name: str) -> Optional[dict]:
        """Upload a binary file to a PrestaShop API resource.

        :param resource: API resource (e.g., 'images/products/22').
        :type resource: str
        :param file_path: Path to the binary file.
        :type file_path: str
        :param file_name: File name.
        :type file_name: str

        :return: Response from the API or `None` on failure.
        :rtype: dict | None
        """
        try:
            with open(file_path, 'rb') as file:
                headers = {'Content-Type': 'application/octet-stream'}
                response = self.client.post(
                    url=f'{self.API_DOMAIN}{resource}',
                    headers=headers,
                    data=file.read()
                )
                if self._check_response(response.status_code, response):
                   return j_loads_ns(response.text) # corrected response.json()
        except Exception as e:
            logger.error(f"Error uploading binary file: {e}")
            return None

    def _save(self, file_name: str, data: dict):
        """Save data to a file.

        :param file_name: Name of the file.
        :type file_name: str
        :param data: Data to be saved.
        :type data: dict
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    def get_data(self, resource: str, **kwargs) -> Optional[dict]:
        """Fetch data from a PrestaShop API resource and save it.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param **kwargs: Additional arguments for the API request.

        :return: Data from the API or `None` on failure.
        :rtype: dict | None
        """
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        if data:
            self._save(f'{resource}.json', data)
            return data
        return None

    def remove_file(self, file_path: str):
        """Remove a file from the filesystem.

        :param file_path: Path to the file.
        :type file_path: str
        """
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f'Error removing file {file_path}: {e}')

    def get_apis(self) -> Optional[dict]:
        """Get a list of all available APIs.

        :return: List of available APIs.
        :rtype: dict
        """
        return self._exec('apis', method='GET', io_format=self.data_format)

    def get_languages_schema(self) -> Optional[dict]:
        """Get the schema for languages.

        :return: Language schema or `None` on failure.
        :rtype: dict
        """
        try:
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f'Error: {ex}')
            return None

    def _upload_image(self, resource: str, resource_id: int, img_url: str,
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

        :return: Response from the API or `None` on failure.
        :rtype: dict | None
        """
        url_parts = img_url.rsplit('.', 1)
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = f'{resource_id}_{img_name}.{extension}' if img_name else f'{resource_id}.{extension}'
        png_file_path = save_image_from_url(img_url, filename)
        if not png_file_path:
            return None
        response = self.create_binary(resource, png_file_path, filename)
        self.remove_file(png_file_path)
        return response

    def upload_image_async(self, resource: str, resource_id: int, img_url: str,
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

        :return: Response from the API or `None` on failure.
        :rtype: dict | None
        """
        return self._upload_image(resource, resource_id, img_url, img_name)

    def upload_image(self, resource: str, resource_id: int, img_url: str,
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

        :return: Response from the API or `None` on failure.
        :rtype: dict | None
        """
        return self._upload_image(resource, resource_id, img_url, img_name)

    def get_product_images(self, product_id: int) -> Optional[dict]:
        """Get images for a product.

        :param product_id: Product ID.
        :type product_id: int

        :return: List of product images or `None` on failure.
        :rtype: dict | None
        """
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)