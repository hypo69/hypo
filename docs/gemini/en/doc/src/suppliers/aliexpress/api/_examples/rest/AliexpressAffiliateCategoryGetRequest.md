# AliexpressAffiliateCategoryGetRequest

## Overview

This module defines the `AliexpressAffiliateCategoryGetRequest` class, which is a subclass of the `RestApi` class. This class provides methods for making API requests to the AliExpress affiliate category endpoint.

## Table of Contents

- [AliexpressAffiliateCategoryGetRequest](#aliexpressaffiliatecategorygetrequest)
    - [Overview](#overview)
    - [Classes](#classes)
        - [AliexpressAffiliateCategoryGetRequest](#aliexpressaffiliatecategorygetrequest-1)
            - [__init__](#__init__)
            - [getapiname](#getapiname)

## Classes

### AliexpressAffiliateCategoryGetRequest

**Description**: This class handles requests to the AliExpress affiliate category API endpoint.

**Methods**

#### __init__

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): The domain for the API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port for the API endpoint. Defaults to 80.

    Returns:
        None

    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None

```

#### getapiname

```python
def getapiname(self):
    """
    Returns:
        str: The API name for the request.

    """
    return 'aliexpress.affiliate.category.get'
```