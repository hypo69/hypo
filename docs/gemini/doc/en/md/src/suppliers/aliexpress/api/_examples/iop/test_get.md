# Module: hypotez/src/suppliers/aliexpress/api/_examples/iop/test_get.py

## Overview

This module contains an example of using the `iop` library to interact with the AliExpress API for getting logistics seller addresses. It demonstrates creating an `IopClient`, an `IopRequest`, adding parameters, executing the request, and handling the response.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [`IopClient`](#iopclient)
    * [`IopRequest`](#ioprequest)
* [Functions](#functions)
    * [`test_get`](#test_get)


## Classes

### `IopClient`

**Description**: Represents a client for interacting with the iop API.

**Methods**

- `execute(request: IopRequest, data: str) -> IopResponse`: Executes the given request and returns the response.

### `IopRequest`

**Description**: Represents an API request.


**Methods**

- `set_simplify() -> None`: Sets the request to use simplified data types.
- `add_api_param(name: str, value: str) -> None`: Adds an API parameter to the request.


## Functions

### `test_get`

**Description**: This function demonstrates a GET request to the AliExpress logistics API.

**Parameters:**

- None

**Returns:**

- None


**Raises:**


- None

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api._examples.iop """

import iop


# params 1 : gateway url
# params 2 : appkey
# params 3 : appSecret
def test_get():
    """
    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    client = iop.IopClient(
        'https://api-pre.aliexpress.com/sync',
        '33505222',
        'e1fed6b34feb26aabc391d187732af93',
    )

    # create a api request set GET mehotd
    # default http method is POST
    request = iop.IopRequest(
        'aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST'
    )
    request.set_simplify()
    # simple type params ,Number ,String
    request.add_api_param('seller_address_query', 'pickup')

    data = "50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL"
    response = client.execute(request, data)

    # response type nil,ISP,ISV,SYSTEM
    # nil ：no error
    # ISP : API Service Provider Error
    # ISV : API Request Client Error
    # SYSTEM : Iop platform Error
    print(response.type)

    # response code, 0 is no error
    print(response.code)

    # response error message
    print(response.message)

    # response unique id
    print(response.request_id)

    # full response
    print(response.body)