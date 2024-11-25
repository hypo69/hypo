# AliexpressAffiliateOrderListbyindexRequest

## Overview

This module defines the `AliexpressAffiliateOrderListbyindexRequest` class, which is a subclass of `RestApi`, providing functionality for retrieving affiliate order lists from AliExpress. It allows for filtering orders based on various criteria.

## Table of Contents

* [AliexpressAffiliateOrderListbyindexRequest](#aliexpressaffiliateorderlistbyindexrequest)
    * [Overview](#overview)
    * [Class `AliexpressAffiliateOrderListbyindexRequest`](#class-aliexpressaffiliateorderlistbyindexrequest)
        * [__init__](#init)
        * [getapiname](#getapiname)


## Class `AliexpressAffiliateOrderListbyindexRequest`

**Description**: This class handles requests for retrieving affiliate order lists from AliExpress via its API.  It inherits from `RestApi`.


### `__init__`

**Description**: Initializes an `AliexpressAffiliateOrderListbyindexRequest` object.

**Parameters**:

- `domain` (str, optional): The domain to use for the API request. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The port to use for the API request. Defaults to 80.

**Raises**:

- No specific exceptions are documented in the code.



### `getapiname`

**Description**: Returns the API name for this request.

**Parameters**:

- None

**Returns**:

- `str`: The API name "aliexpress.affiliate.order.listbyindex"

**Raises**:

- No specific exceptions are documented in the code.


```python
from ..base import RestApi
class AliexpressAffiliateOrderListbyindexRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.end_time = None
		self.fields = None
		self.page_size = None
		self.start_query_index_id = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'aliexpress.affiliate.order.listbyindex'
```