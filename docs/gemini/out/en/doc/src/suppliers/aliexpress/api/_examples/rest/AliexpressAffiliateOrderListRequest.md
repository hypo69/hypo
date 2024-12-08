# AliexpressAffiliateOrderListRequest

## Overview

This module defines the `AliexpressAffiliateOrderListRequest` class, which is used to interact with the AliExpress Affiliate Order List API. It inherits from the `RestApi` base class.

## Table of Contents

* [AliexpressAffiliateOrderListRequest](#aliexpressaffiliateorderlistrequest)
    * [Class Description](#class-description)
    * [Methods](#methods)
        * [`getapiname()`](#getapiname)

## Classes

### `AliexpressAffiliateOrderListRequest`

**Description**: This class handles requests to the AliExpress Affiliate Order List API.

**Methods**

#### `getapiname()`

**Description**: Returns the API name for the request.

**Returns**:
- `str`: The API name (`aliexpress.affiliate.order.list`).


```python
def getapiname(self):
    """
    Returns the API name for the request.

    Returns:
        str: The API name ("aliexpress.affiliate.order.list").
    """
    return 'aliexpress.affiliate.order.list'
```


```python
class AliexpressAffiliateOrderListRequest(RestApi):
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Initializes the AliexpressAffiliateOrderListRequest object.

        Args:
            domain (str, optional): The domain for the API request. Defaults to "api-sg.aliexpress.com".
            port (int, optional): The port for the API request. Defaults to 80.

        """
        RestApi.__init__(self,domain, port)
        self.app_signature = None
        self.end_time = None
        self.fields = None
        self.locale_site = None
        self.page_no = None
        self.page_size = None
        self.start_time = None
        self.status = None
```