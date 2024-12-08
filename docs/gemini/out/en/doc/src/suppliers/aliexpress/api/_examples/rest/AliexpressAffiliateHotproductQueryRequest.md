# AliexpressAffiliateHotproductQueryRequest

## Overview

This module defines the `AliexpressAffiliateHotproductQueryRequest` class, which is used to interact with the AliExpress Affiliate API to query hot products. It inherits from the `RestApi` base class.  This class provides methods for setting various query parameters to filter and retrieve product data.

## Table of Contents

* [AliexpressAffiliateHotproductQueryRequest](#aliexpressaffiliatehotproductqueryrequest)
    * [Overview](#overview)
    * [Classes](#classes)
        * [AliexpressAffiliateHotproductQueryRequest](#aliexpressaffiliatehotproductqueryrequest-1)
            * [__init__](#init)
            * [getapiname](#getapiname)


## Classes

### `AliexpressAffiliateHotproductQueryRequest`

**Description**: This class handles requests to the AliExpress Affiliate API for querying hot products.  It allows setting parameters to refine the search criteria.

#### `__init__`

**Description**: Initializes the `AliexpressAffiliateHotproductQueryRequest` object.

**Parameters**:
- `domain` (str, optional): The domain name of the API endpoint. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The port number for the API endpoint. Defaults to 80.

**Raises**:
- `Exception`: If there's an issue during initialization.

#### `getapiname`

**Description**: Returns the API name for the query operation.

**Returns**:
- str: The API name "aliexpress.affiliate.hotproduct.query".


```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Initializes the AliexpressAffiliateHotproductQueryRequest object.

    Args:
        domain (str, optional): The domain name of the API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port number for the API endpoint. Defaults to 80.

    Raises:
        Exception: If there's an issue during initialization.
    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.category_ids = None
    self.delivery_days = None
    self.fields = None
    self.keywords = None
    self.max_sale_price = None
    self.min_sale_price = None
    self.page_no = None
    self.page_size = None
    self.platform_product_type = None
    self.ship_to_country = None
    self.sort = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None


def getapiname(self):
    """
    Returns the API name for the query operation.

    Returns:
        str: The API name "aliexpress.affiliate.hotproduct.query".
    """
    return 'aliexpress.affiliate.hotproduct.query'
```