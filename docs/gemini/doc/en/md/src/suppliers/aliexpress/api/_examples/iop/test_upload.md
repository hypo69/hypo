# test_upload.py

## Overview

This module contains an example of interacting with the Iop API for file uploads. It demonstrates how to create an API request, add parameters (including file uploads), and process the response from the API.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`IopClient`](#iopclient)
    * [`IopRequest`](#ioprequest)
    * [`execute`](#execute)


## Functions

### `IopClient`

**Description**: Creates an Iop client instance.

**Parameters**:
- `gateway_url` (str): The base URL of the Iop API gateway.
- `app_key` (str): The application key for authentication.
- `app_secret` (str): The application secret for authentication.

**Returns**:
- `IopClient`: An instance of the Iop client.


### `IopRequest`

**Description**: Creates an Iop API request.

**Parameters**:
- `path` (str): The API endpoint path.


**Returns**:
- `IopRequest`: An instance of the Iop request.


### `execute`

**Description**: Executes the API request and handles the response.

**Parameters**:
- `request` (IopRequest): The API request object to execute.
- `access_token` (Optional[str | dict | str], optional): The access token for authentication. Defaults to `None`.


**Returns**:
- `IopResponse`: The response from the API.  Returns a `None` if an exception occurs.


**Raises**:
- `APIError`: For issues with the API response.
- `IOError`: For issues with file access.


### `add_api_param`

**Description**: Adds a simple parameter to the API request.

**Parameters**:
- `param_name` (str): The name of the parameter.
- `param_value` (str): The value of the parameter.


**Returns**:
- `None`



### `add_file_param`

**Description**: Adds a file parameter to the API request.

**Parameters**:
- `param_name` (str): The name of the parameter.
- `file_content` (str): The content of the file to upload.


**Returns**:
- `None`