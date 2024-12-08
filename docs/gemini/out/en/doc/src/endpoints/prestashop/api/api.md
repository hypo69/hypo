# PrestaShop API Module Documentation

## Overview

This module provides a Python class, `PrestaShop`, for interacting with the PrestaShop web service API. It handles various operations such as creating, reading, updating, deleting resources, searching, and uploading images.  The module uses JSON and XML for data exchange, although JSON is the preferred format. Error handling is implemented to manage potential issues during API interactions.

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

**Description**: An enumeration defining data types for API responses (JSON or XML).  JSON is currently preferred.

**Details**:
- Contains two values: `JSON` and `XML`.


## PrestaShop Class

### `PrestaShop`

**Description**: This class facilitates interactions with the PrestaShop web service API.  It supports various operations for CRUD, search, and image uploading.

**Parameters**:

- `API_DOMAIN` (str): The domain of the PrestaShop shop (e.g., https://myPrestaShop.com).
- `API_KEY` (str): The API key for authentication.
- `data_format` (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
- `default_lang` (int, optional): Default language ID. Defaults to 1.
- `debug` (bool, optional): Activate debug mode. Defaults to `True`.

**Raises**:
- `PrestaShopAuthenticationError`: Raised if the API key is invalid or missing.
- `PrestaShopException`: Raised for generic PrestaShop WebServices errors.


### `__init__`

**Description**: Initializes the `PrestaShop` object.

**Parameters**:

- `data_format` (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
- `default_lang` (int, optional): Default language ID. Defaults to 1.
- `debug` (bool, optional): Activate debug mode. Defaults to `True`.


**Returns**:

- `None`


### `ping`

**Description**: Tests the connectivity of the PrestaShop web service.

**Returns**:

- `bool`: `True` if the service is reachable, `False` otherwise.


### `_check_response`

**Description**: Checks the HTTP response status code and handles errors.

**Parameters**:

- `status_code` (int): HTTP response status code.
- `response` (requests.Response): HTTP response object.
- `method` (str, optional): HTTP method used for the request.
- `url` (str, optional): The URL of the request.
- `headers` (dict, optional): The headers used in the request.
- `data` (dict, optional): The data sent in the request.


**Returns**:

- `bool`: `True` if the status code is 200 or 201, `False` otherwise.


### `_parse_response_error`

**Description**: Parses the error response from the PrestaShop API.

**Parameters**:

- `response` (requests.Response): HTTP response object.


**Returns**:
- `None`


### `_prepare`

**Description**: Prepares the URL for an API request by adding parameters.

**Parameters**:

- `url` (str): The base URL.
- `params` (dict): The parameters to be appended to the URL.


**Returns**:

- `str`: The prepared URL.


### `_exec`

**Description**: Executes an HTTP request to the PrestaShop API.

**Parameters**: (Many parameters, see docstring in the code)

**Returns**:

- `dict | None`: The parsed API response as a dictionary, or `False` on failure.


### `_parse`

**Description**: Parses the API response (XML or JSON).

**Parameters**:

- `text` (str): The response text.


**Returns**:

- `dict | ElementTree.Element | bool`: The parsed data, or `False` if parsing fails.


### `create`

**Description**: Creates a new resource on the PrestaShop API.

**Parameters**:

- `resource` (str): The API resource.
- `data` (dict): The data to create the resource with.


**Returns**:

- `dict`: The API response.


### `read`

**Description**: Reads an existing resource from the PrestaShop API.

**Parameters**:

- `resource` (str): The API resource.
- `resource_id` (int | str): The ID of the resource to read.

**Returns**:

- `dict`: The API response.


### `write`

**Description**: Updates an existing resource on the PrestaShop API.

**Parameters**:

- `resource` (str): The API resource.
- `data` (dict): The updated data.


**Returns**:

- `dict`: The API response.


### `unlink`

**Description**: Deletes a resource from the PrestaShop API.

**Parameters**:

- `resource` (str): The API resource.
- `resource_id` (int | str): The ID of the resource to delete.


**Returns**:

- `bool`: `True` if the deletion was successful, `False` otherwise.


### `search`

**Description**: Searches for resources on the PrestaShop API.

**Parameters**:

- `resource` (str): The API resource.
- `filter` (str | dict, optional): The search filter.


**Returns**:

- `List[dict]`: A list of resources matching the search criteria.


### `create_binary`

**Description**: Uploads a binary file (e.g., image) to the PrestaShop API.

**Parameters**:

- `resource` (str): The API resource (often for image uploads).
- `file_path` (str): Path to the file to upload.
- `file_name` (str): File name.


**Returns**:

- `dict`: The API response.


### `_save`

**Description**: Saves data to a file.

**Parameters**:

- `file_name` (str): File name.
- `data` (dict): Data to save.


**Returns**:

- `None`


### `get_data`

**Description**: Fetches data from the PrestaShop API and saves it to a file.

**Parameters**:

- `resource` (str): The API resource.
- `**kwargs`: Additional keyword arguments for the API request.


**Returns**:

- `dict | None`: The fetched data or `False` on failure.


### `remove_file`

**Description**: Removes a file from the file system.

**Parameters**:

- `file_path` (str): Path to the file.


**Returns**:

- `None`


### `get_apis`

**Description**: Retrieves a list of available APIs.

**Returns**:

- `dict`: A list of available APIs.


### `get_languages_schema`

**Description**: Retrieves the schema for languages.

**Returns**:

- `dict`: The language schema or `None` on failure.


### `upload_image_async`

**Description**: Asynchronously uploads an image to the PrestaShop API.

**Parameters**:

- `resource` (str): API resource (often for image uploads).
- `resource_id` (int): Resource ID.
- `img_url` (str): URL of the image.
- `img_name` (str, optional): Name of the image file.


**Returns**:

- `dict | None`: The API response or `None` on failure.


### `upload_image`

**Description**: Uploads an image to the PrestaShop API.

**Parameters**:

- `resource` (str): API resource (often for image uploads).
- `resource_id` (int): Resource ID.
- `img_url` (str): URL of the image.
- `img_name` (str, optional): Name of the image file.


**Returns**:

- `dict | None`: The API response or `None` on failure.


### `get_product_images`

**Description**: Retrieves images for a specific product.

**Parameters**:

- `product_id` (int): The ID of the product.


**Returns**:

- `dict | None`: A list of product images or `False` on failure.