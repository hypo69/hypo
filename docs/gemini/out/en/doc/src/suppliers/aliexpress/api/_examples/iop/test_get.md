# test_get.py

## Overview

This Python file demonstrates the use of the `iop` library to interact with the AliExpress API. It showcases how to create an API request, set parameters, execute the request, and handle the response.


## Table of Contents

* [Overview](#overview)
* [IopClient](#iopclient)
* [IopRequest](#ioprequest)
* [execute](#execute)
* [Response Handling](#response-handling)


## IopClient

### `IopClient`

**Description**: This class provides the interface for interacting with the Iop API.

**Parameters**:

* `gateway_url` (str): The URL of the API gateway.
* `appkey` (str): The application key for authentication.
* `appSecret` (str): The application secret for authentication.


## IopRequest

### `IopRequest`

**Description**: This class represents an API request.

**Parameters**:

* `api_name` (str): The name of the API to call.
* `method` (str, optional): The HTTP method to use (default is POST).


## execute

### `execute`

**Description**: This method executes the API request and returns the response.

**Parameters**:

* `request` (IopRequest): The request object to execute.
* `correlation_id` (str): A unique identifier for the request.


## Response Handling

**Description**: This section details the handling of the API response.

**Parameters**:

* `response` (IopResponse): The response object.


## Functions

### `print`

**Description**: This function prints the response to the console.

**Parameters**:
- `value`: The value to print