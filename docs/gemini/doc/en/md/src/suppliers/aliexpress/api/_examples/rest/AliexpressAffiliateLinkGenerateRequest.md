# AliexpressAffiliateLinkGenerateRequest

## Overview

This module defines the `AliexpressAffiliateLinkGenerateRequest` class, which is used to generate affiliate links on AliExpress. It inherits from the `RestApi` class and provides methods for interacting with the AliExpress API.

## Table of Contents

* [AliexpressAffiliateLinkGenerateRequest](#aliexpressaffiliatelinkgeneraterequest)
    * [__init__](#init)
    * [getapiname](#getapiname)


## Classes

### `AliexpressAffiliateLinkGenerateRequest`

**Description**: This class is used to generate affiliate links on AliExpress. It handles the API request and response.

**Methods**

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateLinkGenerateRequest` class.

**Parameters**

- `domain` (str, optional): The domain name for the AliExpress API. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The port number for the AliExpress API. Defaults to 80.

**Raises**

- No exceptions are explicitly raised in the `__init__` method.

#### `getapiname`

**Description**: Returns the API name for the request.

**Parameters**:

- None

**Returns**:
- str: The API name 'aliexpress.affiliate.link.generate'.

**Raises**:
- No exceptions are explicitly raised in the `getapiname` method.