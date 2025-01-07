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
from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException
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
                logger.critical(f"""response status code: {status_code}
                    url: {response.request.url}
                    --------------
                    headers: {response.headers}
                    --------------
                    response text: {response.text}""")
            return response
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
            logger.error(f'XML response error: {message} \n Code: {code}')
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

        :return: The response from the API or `False` on failure.
        :rtype: dict | None
        """
        if self.debug:
            import sys
            original_stderr = sys.stderr
            f = open('stderr.log', 'w')
            sys.stderr = f

            response = self.client.request(
                method=method,
                url=self._prepare(f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}',
                                  {'filter': search_filter,
                                   'display': display,
                                   'schema': schema,
                                   'sort': sort,
                                   'limit': limit,
                                   'language': language,
                                   'output_format': io_format}),
                data=dict2xml(data) if data and io_format == 'XML' else data,
                headers=headers,
            )

            sys.stderr = original_stderr

        if not self._check_response(response.status_code, response, method, url, headers, data):
            return False

        if io_format == 'JSON':
            return response.json()
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
                data = response.json()
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
        with open(file_path, 'rb') as file:
            headers = {'Content-Type': 'application/octet-stream'}
            response = self.client.post(
                url=f'{self.API_DOMAIN}{resource}',
                headers=headers,
                data=file.read()
            )
            return response.json()

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

        :return: Data from the API or `False` on failure.
        :rtype: dict | None
        """
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
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
            return

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
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = save_image_from_url(img_url, filename)
        response = self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

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
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = save_image_from_url(img_url, filename)
        response = self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

    def get_product_images(self, product_id: int) -> Optional[dict]:
        """Get images for a product.

        :param product_id: Product ID.
        :type product_id: int

        :return: List of product images or `False` on failure.
        :rtype: dict | None
        """
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)