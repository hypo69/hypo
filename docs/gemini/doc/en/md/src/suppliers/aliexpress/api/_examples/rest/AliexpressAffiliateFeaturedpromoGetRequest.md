# AliexpressAffiliateFeaturedpromoGetRequest

## Overview

This module defines the `AliexpressAffiliateFeaturedpromoGetRequest` class, which is a subclass of `RestApi`. It provides functionality for making API requests to fetch featured promotions from AliExpress.


## Table of Contents

* [AliexpressAffiliateFeaturedpromoGetRequest](#aliexpressaffiliatefeaturedpromogetrequest)
    * [Class Description](#class-description)
    * [Methods](#methods)
        * [`__init__`](#init)
        * [`getapiname`](#getapiname)


## Classes

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Description**: This class handles requests to the AliExpress API for fetching featured promotions. It extends the `RestApi` class, inheriting its general API interaction capabilities.

**Methods**:

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): The domain of the AliExpress API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port number of the AliExpress API endpoint. Defaults to 80.

    Returns:
        None
    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.fields = None
```

#### `getapiname`

```python
def getapiname(self):
    """
    Returns the API name for the featured promotion retrieval.

    Returns:
        str: The API name.
    """
    return 'aliexpress.affiliate.featuredpromo.get'
```


**Note:** This documentation assumes that the `RestApi` class is defined elsewhere and handles the low-level details of API communication.  The provided code snippet does not include the `RestApi` class definition, so a complete understanding of the functionality is limited.