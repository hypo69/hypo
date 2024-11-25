# aliexpress.affiliate.product.smartmatch Request

## Overview

This module defines the `AliexpressAffiliateProductSmartmatchRequest` class, which is used to interact with the AliExpress affiliate product smartmatch API.  It inherits from the base `RestApi` class and provides methods for constructing and sending requests to the API.


## Classes

### `AliexpressAffiliateProductSmartmatchRequest`

**Description**: This class handles requests to the AliExpress affiliate product smartmatch API. It allows setting various parameters to filter and retrieve product information.

**Methods**

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateProductSmartmatchRequest` class.

**Parameters**:

- `domain` (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The port of the API endpoint. Defaults to 80.

**Raises**:

- `Exception`:  If there's an issue initializing the parent `RestApi` class.

#### `getapiname`

**Description**: Returns the API name used for this request.

**Returns**:

- str: The API name ("aliexpress.affiliate.product.smartmatch").


## Attributes

* `app`:  (Optional): Description of the `app` parameter if needed.
* `app_signature`: (Optional): Description of the `app_signature` parameter if needed.
* `country`: (Optional): Description of the `country` parameter if needed.
* `device`: (Optional): Description of the `device` parameter if needed.
* `device_id`: (Optional): Description of the `device_id` parameter if needed.
* `fields`: (Optional): Description of the `fields` parameter if needed.
* `keywords`: (Optional): Description of the `keywords` parameter if needed.
* `page_no`: (Optional): Description of the `page_no` parameter if needed.
* `product_id`: (Optional): Description of the `product_id` parameter if needed.
* `site`: (Optional): Description of the `site` parameter if needed.
* `target_currency`: (Optional): Description of the `target_currency` parameter if needed.
* `target_language`: (Optional): Description of the `target_language` parameter if needed.
* `tracking_id`: (Optional): Description of the `tracking_id` parameter if needed.
* `user`: (Optional): Description of the `user` parameter if needed.


**Note**: The documentation is incomplete as there are no parameter descriptions provided in the Python code.  To make this documentation complete, parameter descriptions should be added to the Python code's docstrings.