# AliexpressAffiliateOrderListbyindexRequest

## Overview

This module defines the `AliexpressAffiliateOrderListbyindexRequest` class, which is part of the AliExpress Affiliate API. It allows for retrieving order lists by index.


## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [AliexpressAffiliateOrderListbyindexRequest](#aliexpressaffiliateorderlistbyindexrequest)
        * [__init__](#__init__)
        * [getapiname](#getapiname)


## Classes

### `AliexpressAffiliateOrderListbyindexRequest`

**Description**: This class handles requests to the AliExpress Affiliate API for retrieving order lists by index.  It extends the base `RestApi` class.

**Methods**

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateOrderListbyindexRequest` class.

**Parameters**:

- `domain` (str): The domain of the AliExpress API endpoint. Defaults to "api-sg.aliexpress.com".
- `port` (int): The port of the AliExpress API endpoint. Defaults to 80.

**Raises**:

- No exceptions documented in the provided code.  


#### `getapiname`

**Description**: Returns the API name for this request.

**Parameters**:

- None

**Returns**:

- str: The name of the API method, "aliexpress.affiliate.order.listbyindex".


```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str): The domain of the AliExpress API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int): The port of the AliExpress API endpoint. Defaults to 80.

    Raises:
        No exceptions documented.
    """
    RestApi.__init__(self,domain, port)
    self.app_signature = None
    self.end_time = None
    self.fields = None
    self.page_size = None
    self.start_query_index_id = None
    self.start_time = None
    self.status = None


def getapiname(self):
    """
    Returns the API name for this request.

    Returns:
        str: The name of the API method, "aliexpress.affiliate.order.listbyindex".
    """
    return 'aliexpress.affiliate.order.listbyindex'
```