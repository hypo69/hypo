# hypotez/src/suppliers/aliexpress/api/_examples/iop/base.py

## Overview

This module provides a base Iop client for interacting with APIs. It handles API signing, request execution, and error logging.  It includes classes for building requests, handling responses, and managing connections to the API.

## Table of Contents

* [Classes](#classes)
    * [IopRequest](#ioprequest)
    * [IopResponse](#iopresponse)
    * [IopClient](#iopclient)
* [Functions](#functions)
    * [sign](#sign)
    * [mixStr](#mixstr)
    * [logApiError](#logapierror)


## Classes

### IopRequest

**Description**: This class represents an API request.  It allows the user to build the request, including parameters and file uploads, and optionally set format and simplify options.

**Methods**:

- **`add_api_param(self, key, value)`**: Adds an API parameter to the request.
- **`add_file_param(self, key, value)`**: Adds a file parameter (for file uploads) to the request.
- **`set_simplify(self)`**: Sets the `simplify` parameter to "true" for the request.
- **`set_format(self, value)`**: Sets the `format` parameter for the request.


### IopResponse

**Description**: This class represents an API response. It stores information about the response, including the `type`, `code`, `message`, `request_id`, and the JSON response body.

**Methods**:
- **`__str__(self, *args, **kwargs)`**: Returns a string representation of the response, including its status code and message.


### IopClient

**Description**: This class acts as a client for interacting with the API. It handles the communication with the server, including signing the request and handling errors.

**Methods**:

- **`execute(self, request, access_token=None)`**: Executes an API request.
    * **Parameters**:
        * `request` (IopRequest): The request to be executed.
        * `access_token` (str, optional): The access token for authentication. Defaults to None.
    * **Returns**:
        * `IopResponse`: The response from the API.
    * **Raises**:
        * `Exception`: If there's an error during the request execution (network error, API error).  Details about the error are logged.


## Functions

### sign

**Description**: This function calculates the HMAC SHA256 signature for a given API request.

**Parameters**:
- `secret` (str): The secret key.
- `api` (str): The API endpoint.
- `parameters` (dict): The parameters of the request.

**Returns**:
- `str`: The hexadecimal representation of the calculated HMAC SHA256 signature.

**Raises**:
- `Exception`: If there's an issue with the input data.

### mixStr

**Description**: Converts input values to strings, handling `str` and `unicode` types, and potentially other types that are castable to strings.

**Parameters**:
- `pstr`: Input value to convert.

**Returns**:
- `str`: The string representation of the input.

**Raises**:
- `Exception`: None.

### logApiError

**Description**: Logs API errors, including the app key, SDK version, timestamp, request URL, error code, and error message, to an error log file.

**Parameters**:
- `appkey` (str): The application key.
- `sdkVersion` (str): The SDK version.
- `requestUrl` (str): The API request URL.
- `code` (str): The error code.
- `message` (str): The error message.

**Returns**:
- None.

**Raises**:
- `Exception`: None. (It's intended to log errors, not throw exceptions)