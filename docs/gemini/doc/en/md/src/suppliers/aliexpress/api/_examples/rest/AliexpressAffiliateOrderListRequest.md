# AliexpressAffiliateOrderListRequest

## Overview

This module defines the `AliexpressAffiliateOrderListRequest` class, which is part of the AliExpress Affiliate API. It provides a way to request a list of affiliate orders.


## Table of Contents

- [AliexpressAffiliateOrderListRequest](#aliexpressaffiliateorderlistrequest)
    - [Methods](#methods)
        - [`getapiname`](#getapiname)


## Classes

### `AliexpressAffiliateOrderListRequest`

**Description**: This class handles requests for a list of affiliate orders from the AliExpress Affiliate API. It inherits from the `RestApi` class.

**Methods**

#### `getapiname`

**Description**: Returns the API name for the order list request.

**Returns**:
- `str`: The name of the API method (`aliexpress.affiliate.order.list`).


```python
def getapiname(self):
    """
    Returns the API name for the order list request.

    Returns:
        str: The name of the API method ("aliexpress.affiliate.order.list").
    """
    return 'aliexpress.affiliate.order.list'
```