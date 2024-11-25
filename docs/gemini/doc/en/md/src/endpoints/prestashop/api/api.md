# hypotez/src/endpoints/prestashop/api/api.py

## Overview

This module provides a Python class, `PrestaShop`, for interacting with the PrestaShop API.  It allows for creating, reading, updating, deleting (CRUD) operations, searching, and uploading images.  The class handles communication with the API, including error handling and parsing JSON or XML responses.

## Table of Contents

* [PrestaShop Class](#prestashop-class)
    * [\_\_init\_\_](#__init__)
    * [ping](#ping)
    * [_check\_response](#_check_response)
    * [_parse\_response\_error](#_parse_response_error)
    * [_prepare](#_prepare)
    * [_exec](#_exec)
    * [_parse](#_parse)
    * [create](#create)
    * [read](#read)
    * [write](#write)
    * [unlink](#unlink)
    * [search](#search)
    * [create\_binary](#create_binary)
    * [_save](#_save)
    * [get\_data](#get_data)
    * [remove\_file](#remove_file)
    * [get\_apis](#get_apis)
    * [get\_languages\_schema](#get_languages_schema)
    * [upload\_image\_async](#upload_image_async)
    * [upload\_image](#upload_image)
    * [get\_product\_images](#get_product_images)
* [Format Enum](#format-enum)


## Format Enum

### `Format`

**Description**: An enumeration defining data types for the API response (JSON or XML).

**Details**:
- This is deprecated in favor of JSON.
- The enum has two values: `JSON` and `XML`.


## PrestaShop Class

### `PrestaShop`

**Description**: This class interacts with the PrestaShop web service API, supporting both JSON and XML data formats.

**Parameters**:
- `API_DOMAIN` (str): The domain of the PrestaShop shop.
- `API_KEY` (str): The API key for authentication.
- `data_format` (str, optional): Data format ('JSON' or 'XML'). Defaults to 'JSON'.
- `default_lang` (int, optional): Default language ID. Defaults to 1.
- `debug` (bool, optional): Activate debug mode. Defaults to True.

**Raises**:
- `PrestaShopAuthenticationError`: If the API key is invalid or missing.
- `PrestaShopException`: For generic PrestaShop API errors.


### `__init__`

**Description**: Initializes the `PrestaShop` object.

**Parameters**:
- `data_format` (str, optional): Default data format. Defaults to 'JSON'.
- `default_lang` (int, optional): Default language ID. Defaults to 1.
- `debug` (bool, optional): Activate debug mode. Defaults to True.

**Returns**:
- None

### `ping`

**Description**: Tests the connection to the PrestaShop webservice.

**Parameters**:
- None

**Returns**:
- bool: True if the connection is successful, False otherwise.


### `_check_response`

**Description**: Checks the HTTP response status code and handles errors.

**Parameters**:
- `status_code` (int): The HTTP status code.
- `response` (requests.Response): The HTTP response object.
- `method` (str, optional): The HTTP method used.
- `url` (str, optional): The URL of the request.
- `headers` (dict, optional): Request headers.
- `data` (dict, optional): Request data.

**Returns**:
- bool: True if the status code is 200 or 201, False otherwise.


### `_parse_response_error`

**Description**: Parses the error response from the PrestaShop API.

**Parameters**:
- `response` (requests.Response): The HTTP response object.
- `method` (str, optional): The HTTP method.
- `url` (str, optional): The URL.
- `headers` (dict, optional): Request headers.
- `data` (dict, optional): Request data.

**Returns**:
- None

### `_prepare`

**Description**: Prepares the URL for the request, including parameters.

**Parameters**:
- `url` (str): The base URL.
- `params` (dict): Parameters for the request.

**Returns**:
- str: The prepared URL.


### `_exec`

**Description**: Executes an HTTP request to the PrestaShop API.

**Parameters**:
- `resource` (str): API resource.
- `resource_id` (int | str, optional): Resource ID.
- `resource_ids` (int | tuple, optional): Multiple resource IDs.
- `method` (str, optional): HTTP method (e.g., 'GET', 'POST'). Defaults to 'GET'.
- `data` (dict, optional): Data to send with the request.
- `headers` (dict, optional): Request headers.
- `search_filter` (str | dict, optional): Search filter.
- `display` (str | list, optional): Fields to display.
- `schema` (str | None, optional): Schema for the data.
- `sort` (str, optional): Sorting parameter.
- `limit` (str, optional): Limit for results.
- `language` (int, optional): Language ID.
- `io_format` (str, optional): Data format ('JSON' or 'XML'). Defaults to 'JSON'.

**Returns**:
- dict | None: The response from the API or `False` on failure.



### `_parse`

**Description**: Parses the response from the API (XML or JSON).

**Parameters**:
- `text` (str): Response text.

**Returns**:
- dict | ElementTree.Element | bool: Parsed data or `False` on failure.


### `create`

**Description**: Creates a new resource on the PrestaShop API.


**Parameters**:
- `resource` (str): API resource.
- `data` (dict): Data for the new resource.


**Returns**:
- dict: The API response.



### `read`, `write`, `unlink`, `search`, `create_binary`, `_save`, `get_data`, `remove_file`, `get_apis`, `get_languages_schema`, `upload_image_async`, `upload_image`, `get_product_images`

**(See function signatures for parameters and return values in the original code)**