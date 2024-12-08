# AliexpressAffiliateProductdetailGetRequest

## Overview

This module defines the `AliexpressAffiliateProductdetailGetRequest` class, which is a subclass of `RestApi`, allowing interaction with the AliExpress Affiliate API for retrieving product details.

## Classes

### `AliexpressAffiliateProductdetailGetRequest`

**Description**: This class provides methods for interacting with the AliExpress Affiliate API to retrieve product details. It inherits from the `RestApi` base class.

**Methods**:

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateProductdetailGetRequest` class.

**Parameters**:

- `domain` (str, optional): The domain of the AliExpress Affiliate API endpoint. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The port of the AliExpress Affiliate API endpoint. Defaults to 80.

**Raises**:
-  No exceptions documented in the provided code.

#### `getapiname`

**Description**: Returns the API name for this request.

**Returns**:
- str: The API name "aliexpress.affiliate.productdetail.get".


```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): The domain of the AliExpress Affiliate API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port of the AliExpress Affiliate API endpoint. Defaults to 80.

    Raises:
        None
    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.country = None
    self.fields = None
    self.product_ids = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None


def getapiname(self):
    """
    Returns:
        str: The API name "aliexpress.affiliate.productdetail.get".
    
    Raises:
        None
    """
    return 'aliexpress.affiliate.productdetail.get'
```