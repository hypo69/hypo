# aliexpress.affiliate.productdetail.get

## Overview

This module defines the `AliexpressAffiliateProductdetailGetRequest` class, which is used to interact with the AliExpress affiliate product detail API. It extends the `RestApi` class, providing a base for making API requests.  The class allows specifying various parameters for retrieving product details, such as product IDs, desired fields, and more.


## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [AliexpressAffiliateProductdetailGetRequest](#aliexpressaffiliateproductdetailgetrequest)
        * [__init__](#__init__)
        * [getapiname](#getapiname)


## Classes

### AliexpressAffiliateProductdetailGetRequest

**Description**: This class handles requests to the AliExpress affiliate product detail API. It inherits from `RestApi` and provides methods to set parameters for the request and retrieve API endpoints.

**Methods**

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port of the API endpoint. Defaults to 80.

    """
    RestApi.__init__(self,domain, port)
    self.app_signature = None
    self.country = None
    self.fields = None
    self.product_ids = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None
```

#### `getapiname`

```python
def getapiname(self):
    """
    Returns:
        str: The name of the API endpoint.
    """
    return 'aliexpress.affiliate.productdetail.get'
```

**Parameters**:

* None

**Returns**:
  * str: The API endpoint name ('aliexpress.affiliate.productdetail.get').


**Raises**:
* None


## Functions

(No functions are defined in this module)


**Note**: This module is generated automatically, so further documentation may be needed for a complete understanding of the expected parameters and return values of the `AliexpressAffiliateProductdetailGetRequest` class.  The specific meanings of parameters like `fields`, `product_ids`, `target_currency`, and `target_language` require consultation with the AliExpress API documentation.