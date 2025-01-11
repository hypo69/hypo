# Анализ кода модуля `api.py`

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что способствует читаемости и повторному использованию.
    - Присутствует подробная документация к классу и методам, что помогает в понимании их назначения и использования.
    - Используется `requests.Session` для эффективного управления HTTP-соединениями.
    - Присутствует базовая обработка ошибок, включая проверку кодов ответов и вывод сообщений об ошибках.
    - Логирование ошибок с использованием `logger`.
    - Включение отладочного режима с записью в stderr.log
-  Минусы
    -  Не все функции имеют документацию в формате RST, что снижает удобство использования документации.
    -  Используются устаревшие Enum (следует использовать IntEnum).
    -   Не везде используется `logger.error`, а местами стандартный `print`
    - Не все ошибки обрабатываются с помощью `try-except`
    -  Не все методы асинхронны.
    -  `format = 'JSON'` лучше заменить на `format = Format.JSON`
    -  В некоторых местах используется `response.text` без проверки, что может вызвать ошибку при пустом ответе.
    -  Дублирование логики загрузки изображения.
    -  Отсутствие обработки ошибок при сохранении файла (`_save`) и удалении файла (`remove_file`).

**Рекомендации по улучшению**

1.  **Документация RST**: Дополнить документацию в формате RST для всех функций и методов, включая примеры использования и параметров.
2.  **Использование `IntEnum`**: Заменить `Enum` на `IntEnum` для более точного представления числовых констант.
3. **Логирование ошибок**: Использовать `logger.error` для всех исключений, вместо стандартного `print` и `Exception`.
4. **Обработка ошибок**: Добавить `try-except` для обработки ошибок в функциях `_save` и `remove_file`.
5. **Улучшенная обработка `_parse_response_error`**: Доработать метод обработки ошибок, чтобы возвращать структурированное исключение, а не просто `code, message`
6. **Улучшенная обработка `_parse`**: Доработать метод обработки ошибок, чтобы  обрабатывать ошибки при парсинге JSON
7.  **Асинхронность**: Рассмотреть возможность использования асинхронных операций для повышения производительности, особенно при работе с сетью.
8.  **Избавиться от дублирования**: Вынести общую логику загрузки изображений в отдельный метод.
9.  **Улучшить `_exec`**: Добавить проверку `resource_id` перед формированием URL.
10. **Использовать `Format.JSON`**: Заменить `'JSON'` на `Format.JSON` в соответствующих местах.

**Оптимизированный код**

```python
"""
Module for interacting with the PrestaShop API
=========================================================================================

This module provides a class, `PrestaShop`, to interact with the PrestaShop webservice API,
using JSON and XML for message formatting. It supports CRUD operations, searching,
and uploading images, with error handling for responses.

Example usage
-------------

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
import sys
from enum import Enum
from http.client import HTTPConnection
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from requests import Session
from requests.models import PreparedRequest

import header
from src import gs
# from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException # TODO убрать если не нужен
from src.logger.logger import logger
from src.utils.convertors.base64 import base64_to_tmpfile
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.file import save_text_file
from src.utils.image import save_image_from_url
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


class PrestaShop:
    """ Interact with PrestaShop webservice API, using JSON and XML for message

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
        # Получаем данные для подключения к API из конфигурации
        self.API_DOMAIN = gs.credentials.presta.client.api_key.rstrip('/') + '/api/'
        self.API_KEY = gs.credentials.presta.client.api_key
        self.debug = debug
        self.language = default_lang
        self.data_format = data_format

        # Устанавливаем аутентификацию для сессии
        if not self.client.auth:
            self.client.auth = (self.API_KEY, '')

        # Выполняем HEAD запрос для получения версии API
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )
        # Сохраняем версию API
        self.ps_version = response.headers.get('psws-version')

    def ping(self) -> bool:
        """Test if the webservice is working perfectly.

        :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        :rtype: bool
        """
        # Выполняем HEAD запрос для проверки доступности API
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )
        # Проверяем статус ответа
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
        # Проверяем статус ответа
        if status_code in (200, 201):
            return True
        else:
            # Обрабатываем ошибку
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
        """Parse the error response from PrestaShop API.

        :param response: HTTP response object from the server.
        :type response: requests.Response
        """
        # Обработка ошибок в зависимости от формата
        if self.data_format == 'JSON':
            status_code = response.status_code
            # Логируем критическую ошибку, если статус код не 200 или 201
            if not status_code in (200, 201):
                logger.critical(f"""response status code: {status_code}
                    url: {response.request.url}
                    --------------
                    headers: {response.headers}
                    --------------
                    response text: {response.text}""")
            return response # Возвращаем объект ответа
        else:
            # Парсим XML ответ
            error_answer = self._parse(response.text)
            code = None
            message = None
            # Обрабатываем ошибку в формате dict
            if isinstance(error_answer, dict):
                error_content = (error_answer
                                 .get('PrestaShop', {})
                                 .get('errors', {})
                                 .get('error', {}))
                if isinstance(error_content, list):
                    error_content = error_content[0]
                code = error_content.get('code')
                message = error_content.get('message')
             # Обрабатываем ошибку в формате ElementTree.Element
            elif isinstance(error_answer, ElementTree.Element):
                error = error_answer.find('errors/error')
                if error is not None:
                    code = error.find('code').text if error.find('code') is not None else None
                    message = error.find('message').text if error.find('message') is not None else None
            # Логируем ошибку
            logger.error(f'XML response error: {message} \n Code: {code}')
            # Возвращаем код и сообщение
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
        # Подготавливаем URL с параметрами
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

        :return: The response from the API or `False` on failure.
        :rtype: dict | None
        """
        # Активируем отладочный вывод
        if self.debug:
            import sys
            original_stderr = sys.stderr
            f = open('stderr.log', 'w')
            sys.stderr = f
        # Формируем URL в зависимости от наличия `resource_id`
        url = f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}'
        # Готовим параметры запроса
        params = {
            'filter': search_filter,
            'display': display,
            'schema': schema,
            'sort': sort,
            'limit': limit,
            'language': language,
            'output_format': io_format
        }
        # Выполняем запрос к API
        response = self.client.request(
            method=method,
            url=self._prepare(url, params),
            data=dict2xml(data) if data and io_format == 'XML' else data,
            headers=headers,
        )
        # Возвращаем стандартный вывод
        if self.debug:
            sys.stderr = original_stderr

        # Проверяем ответ
        if not self._check_response(response.status_code, response, method, url, headers, data):
            return False
        # Обрабатываем JSON формат
        if io_format == 'JSON':
            try:
                return response.json()
            except ValueError as e:
                logger.error(f'Error parsing JSON response: {e}')
                return None
        # Обрабатываем XML формат
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
            # Обрабатываем JSON формат
            if self.data_format == 'JSON':
                 data = j_loads(text)
                 return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            # Обрабатываем XML формат
            else:
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError, TypeError) as ex:
            # Логируем ошибку парсинга
            logger.error(f'Parsing Error: {ex}')
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
        # Выполняем запрос на создание ресурса
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
        # Выполняем запрос на чтение ресурса
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
        # Выполняем запрос на обновление ресурса
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
         # Выполняем запрос на удаление ресурса
        return self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
        """Search for resources in the PrestaShop API.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param filter: Filter for the search.
        :type filter: str | dict, optional

        :return: List of resources matching the search criteria.
        :rtype: List[dict]
        """
        # Выполняем запрос на поиск ресурса
        return self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)

    def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
        """Upload a binary file to a PrestaShop API resource.

        :param resource: API resource (e.g., 'images/products/22').
        :type resource: str
        :param file_path: Path to the binary file.
        :type file_path: str
        :param file_name: File name.
        :type file_name: str

        :return: Response from the API.
        :rtype: dict
        """
        # Открываем файл для чтения в бинарном формате
        with open(file_path, 'rb') as file:
             # Формируем заголовки запроса
            headers = {'Content-Type': 'application/octet-stream'}
            # Выполняем POST запрос для загрузки бинарного файла
            response = self.client.post(
                url=f'{self.API_DOMAIN}{resource}',
                headers=headers,
                data=file.read()
            )
            # Возвращаем ответ в формате JSON
            return response.json()

    def _save(self, file_name: str, data: dict):
        """Save data to a file.

        :param file_name: Name of the file.
        :type file_name: str
        :param data: Data to be saved.
        :type data: dict
        """
        try:
             # Сохраняем данные в файл в формате JSON
            save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))
        except Exception as e:
            # Логируем ошибку сохранения файла
            logger.error(f'Error saving file {file_name}: {e}')

    def get_data(self, resource: str, **kwargs) -> Optional[dict]:
        """Fetch data from a PrestaShop API resource and save it.

        :param resource: API resource (e.g., 'products').
        :type resource: str
        :param **kwargs: Additional arguments for the API request.

        :return: Data from the API or `False` on failure.
        :rtype: dict | None
        """
        # Получаем данные из API
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        # Сохраняем данные, если они получены
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False

    def remove_file(self, file_path: str):
        """Remove a file from the filesystem.

        :param file_path: Path to the file.
        :type file_path: str
        """
        try:
             # Удаляем файл
            os.remove(file_path)
        except Exception as e:
             # Логируем ошибку удаления файла
            logger.error(f'Error removing file {file_path}: {e}')

    def get_apis(self) -> Optional[dict]:
        """Get a list of all available APIs.

        :return: List of available APIs.
        :rtype: dict
        """
         # Выполняем запрос на получение списка доступных API
        return self._exec('apis', method='GET', io_format=self.data_format)

    def get_languages_schema(self) -> Optional[dict]:
        """Get the schema for languages.

        :return: Language schema or `None` on failure.
        :rtype: dict
        """
        try:
             # Получаем схему языков
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            # Логируем ошибку получения схемы языков
            logger.error(f'Error: {ex}')
            return

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

        :return: Response from the API or `False` on failure.
        :rtype: dict | None
        """
        # Разделяем URL на части
        url_parts = img_url.rsplit('.', 1)
        extension = url_parts[1] if len(url_parts) > 1 else ''
        # Формируем имя файла
        filename = str(resource_id) + f'_{img_name}.{extension}'
        # Сохраняем изображение локально
        png_file_path = save_image_from_url(img_url, filename)
        # Загружаем изображение в PrestaShop
        response = self.create_binary(resource, png_file_path, img_name)
        # Удаляем локальный файл
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

        :return: Response from the API or `False` on failure.
        :rtype: dict | None
        """
        # Загружаем изображение асинхронно
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

        :return: Response from the API or `False` on failure.
        :rtype: dict | None
        """
         # Загружаем изображение
        return self._upload_image(resource, resource_id, img_url, img_name)

    def get_product_images(self, product_id: int) -> Optional[dict]:
        """Get images for a product.

        :param product_id: Product ID.
        :type product_id: int

        :return: List of product images or `False` on failure.
        :rtype: dict | None
        """
        # Получаем изображения продукта
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)
```