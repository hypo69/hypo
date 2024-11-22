## \file hypotez/src/endpoints/prestashop/api/api.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.prestashop.api 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'


import os
import sys
from enum import Enum
from http.client import HTTPConnection
from requests import Session
from requests.models import PreparedRequest
from typing import Dict, List
from pathlib import Path
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

import header
from src import gs
from src.utils.file import save_text_file
from src.utils.convertors import dict2xml, xml2dict, base64_to_tmpfile
from src.utils.image import save_png_from_url
from src.utils.printer import pprint
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger
from src.logger.exceptions import PrestaShopException, PrestaShopAuthenticationError


class Format(Enum):
    """Data types return (JSON, XML)

    @details
    @param Enum (int): 1 => JSON, 2 => XML
    @deprecated - я предпочитаю JSON 👍 :))
    """
    JSON = 'JSON'
    XML = 'XML'


class PrestaShop:
    """ Interact with PrestaShop webservice API, using JSON and XML for message

    @details
    This class provides methods to interact with the PrestaShop API, allowing for CRUD operations, searching, and uploading images.
    It also provides error handling for responses and methods to handle the API's data.

    @param API_KEY `str`: The API key generated from PrestaShop.
    @param API_DOMAIN `str`: The domain of the PrestaShop shop (e.g., https://myPrestaShop.com).
    @param data_format `str`: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
    @param default_lang `int`: Default language ID. Defaults to 1.
    @param debug `bool`: Activate debug mode. Defaults to True.

    @throws PrestaShopAuthenticationError: When the API key is wrong or does not exist.
    @throws PrestaShopException: For generic PrestaShop WebServices errors.

    Example usage:
    @code
    from PrestaShop import PrestaShop, Format

    api = PrestaShop(
        API_DOMAIN = "https://myPrestaShop.com",
        API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
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
    @endcode
    """
    client: Session = Session()
    debug = True
    language = None
    data_format = 'JSON'
    ps_version = ''

    def __init__(self,
                 data_format: str = 'JSON',
                 default_lang: int = 1,
                 debug: bool = True) -> None:
        """ Initialize the PrestaShop class.

        @param API_DOMAIN `str`: The API domain of your PrestaShop shop (e.g., https://myPrestaShop.com).
        @param API_KEY `str`: The API key generated from PrestaShop.
        @param data_format `str`: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
        @param default_lang `int`: Default language ID. Defaults to 1.
        @param debug `bool`: Activate debug mode. Defaults to True.

        @return `None`
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
        """ Test if the webservice is working perfectly.

        @return `bool`: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
        """
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )

        return self._check_response(response.status_code, response)

    def _check_response(self, status_code, response, method=None, url=None, headers=None, data=None) -> bool:
        """ Check the response status code and handle errors.

        @param status_code `int`: HTTP response status code.
        @param response `requests.Response`: HTTP response object.
        @param method `str`: HTTP method used for the request.
        @param url `str`: The URL of the request.
        @param headers `dict`: The headers used in the request.
        @param data `dict`: The data sent in the request.

        @return `bool`: `True` if the status code is 200 or 201, otherwise `False`.
        """
        if status_code in (200, 201):
            return True
        else:
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(self, response, method=None, url=None, headers=None, data=None):
        """ Parse the error response from PrestaShop API.

        @param response `requests.Response`: HTTP response object from the server.
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
            logger.error(f"XML response error: {message} \n Code: {code}")
            return code, message

    def _prepare(self, url, params):
        """ Prepare the URL for the request.

        @param url `str`: The base URL.
        @param params `dict`: The parameters for the request.

        @return `str`: The prepared URL with parameters.
        """
        req = PreparedRequest()
        req.prepare_url(url, params)
        return req.url

    def _exec(self,
              resource: str,
              resource_id: int |  str = None,
              resource_ids: int | tuple = None,
              method: str = 'GET',
              data: dict = None,
              headers: dict = {},
              search_filter = None,
              display: str | list = 'full',
              schema: str | None = None,
              sort: str = None,
              limit: str = None,
              language: int = None,
              io_format: str = 'JSON') -> dict | None:
        """ Execute an HTTP request to the PrestaShop API.

        @param resource `str`: The API resource (e.g., 'products', 'categories').
        @param resource_id `int |  str`: The ID of the resource.
        @param resource_ids `int | tuple`: The IDs of multiple resources.
        @param method `str`: The HTTP method (GET, POST, PUT, DELETE).
        @param data `dict`: The data to be sent with the request.
        @param headers `dict`: Additional headers for the request.
        @param search_filter `str | dict`: Filter for the request.
        @param display `str | list`: Fields to display in the response.
        @param schema `str | None`: The schema of the data.
        @param sort `str`: Sorting parameter for the request.
        @param limit `str`: Limit of results for the request.
        @param language `int`: The language ID for the request.
        @param io_format `str`: The data format ('JSON' or 'XML').

        @return `dict | None`: The response from the API or `False` on failure.
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

    def _parse(self, text: str) -> dict | ElementTree.Element | bool:
        """ Parse XML or JSON response from the API.

        @param text `str`: Response text.

        @return `dict | ElementTree.Element | bool`: Parsed data or `False` on failure.
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

    def create(self, resource: str, data: dict) -> dict:
        """ Create a new resource in PrestaShop API.

        @param resource `str`: API resource (e.g., 'products').
        @param data `dict`: Data for the new resource.

        @return `dict`: Response from the API.
        """
        return self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    def read(self, resource: str, resource_id: int |  str, **kwargs) -> dict:
        """ Read a resource from the PrestaShop API.

        @param resource `str`: API resource (e.g., 'products').
        @param resource_id `int |  str`: Resource ID.

        @return `dict`: Response from the API.
        """
        return self._exec(resource=resource, resource_id=resource_id, method='GET', io_format=self.data_format, **kwargs)

    def write(self, resource: str, data: dict) -> dict:
        """ Update an existing resource in the PrestaShop API.

        @param resource `str`: API resource (e.g., 'products').
        @param data `dict`: Data for the resource.

        @return `dict`: Response from the API.
        """
        return self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data, io_format=self.data_format)

    def unlink(self, resource: str, resource_id: int |  str) -> bool:
        """ Delete a resource from the PrestaShop API.

        @param resource `str`: API resource (e.g., 'products').
        @param resource_id `int |  str`: Resource ID.

        @return `bool`: `True` if successful, `False` otherwise.
        """
        return self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    def search(self, resource: str, filter: str | dict = None, **kwargs) -> List[dict]:
        """ Search for resources in the PrestaShop API.

        @param resource `str`: API resource (e.g., 'products').
        @param filter `str | dict`: Filter for the search.

        @return `List[dict]`: List of resources matching the search criteria.
        """
        return self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)

    def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
        """ Upload a binary file to a PrestaShop API resource.

        @param resource `str`: API resource (e.g., 'images/products/22').
        @param file_path `str`: Path to the binary file.
        @param file_name `str`: File name.

        @return `dict`: Response from the API.
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
        """ Save data to a file.

        @param file_name `str`: Name of the file.
        @param data `dict`: Data to be saved.
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    def get_data(self, resource: str, **kwargs) -> dict | None:
        """ Fetch data from a PrestaShop API resource and save it.

        @param resource `str`: API resource (e.g., 'products').
        @param **kwargs: Additional arguments for the API request.

        @return `dict | None`: Data from the API or `False` on failure.
        """
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False

    def remove_file(self, file_path: str):
        """ Remove a file from the filesystem.

        @param file_path `str`: Path to the file.
        """
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f"Error removing file {file_path}: {e}")

    def get_apis(self) -> dict:
        """ Get a list of all available APIs.

        @return `dict`: List of available APIs.
        """
        return self._exec('apis', method='GET', io_format=self.data_format)

    def get_languages_schema(self) -> dict:
        """ Get the schema for languages.

        @return `dict`: Language schema or `None` on failure.
        """
        try:
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            logger.error(f"Error: {ex}")
            return

    def upload_image_async(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> dict | None:
        """ Upload an image to PrestaShop API asynchronously.

        @param resource `str`: API resource (e.g., 'images/products/22').
        @param resource_id `int`: Resource ID.
        @param img_url `str`: URL of the image.
        @param img_name `str`, optional: Name of the image file.

        @return `dict | None`: Response from the API or `False` on failure.
        """
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = save_png_from_url(img_url, filename)
        response = self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

    def upload_image(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> dict | None:
        """ Upload an image to PrestaShop API.

        @param resource `str`: API resource (e.g., 'images/products/22').
        @param resource_id `int`: Resource ID.
        @param img_url `str`: URL of the image.
        @param img_name `str`, optional: Name of the image file.

        @return `dict | None`: Response from the API or `False` on failure.
        """
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = save_png_from_url(img_url, filename)
        response = self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

    def get_product_images(self, product_id: int) -> dict | None:
        """ Get images for a product.

        @param product_id `int`: Product ID.

        @return `dict | None`: List of product images or `False` on failure.
        """
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)

