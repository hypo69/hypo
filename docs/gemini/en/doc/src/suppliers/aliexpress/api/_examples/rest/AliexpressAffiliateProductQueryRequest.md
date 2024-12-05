# AliexpressAffiliateProductQueryRequest

## Overview

This module defines the `AliexpressAffiliateProductQueryRequest` class, which is used to query affiliate products on AliExpress.  It extends the `RestApi` base class and provides methods for constructing and executing the query.


## Classes

### `AliexpressAffiliateProductQueryRequest`

**Description**: This class handles the request for querying affiliate products on AliExpress. It inherits from the `RestApi` class.

**Methods**:

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateProductQueryRequest` class.

**Parameters**:

- `domain` (str, optional): The domain name for the API endpoint. Defaults to `"api-sg.aliexpress.com"`.
- `port` (int, optional): The port number for the API endpoint. Defaults to `80`.

**Raises**:
-  No exceptions are explicitly documented.


#### `getapiname`

**Description**: Returns the API name for the request.

**Parameters**:
- None

**Returns**:
- str: The API name `"aliexpress.affiliate.product.query"`.

**Raises**:
- No exceptions are explicitly documented.


## Attributes

The class has the following attributes:

- `app_signature`:
- `category_ids`:
- `delivery_days`:
- `fields`:
- `keywords`:
- `max_sale_price`:
- `min_sale_price`:
- `page_no`:
- `page_size`:
- `platform_product_type`:
- `ship_to_country`:
- `sort`:
- `target_currency`:
- `target_language`:
- `tracking_id`:

These attributes likely represent parameters that can be set for the product query request.  The absence of detailed descriptions in the source code makes it difficult to provide precise explanations for each. More context or external documentation is needed.