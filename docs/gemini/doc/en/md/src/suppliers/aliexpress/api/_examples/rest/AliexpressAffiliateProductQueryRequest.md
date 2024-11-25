# AliexpressAffiliateProductQueryRequest

## Overview

This module defines the `AliexpressAffiliateProductQueryRequest` class, which is used to interact with the AliExpress Affiliate API to query product information. It inherits from the `RestApi` base class.


## Classes

### `AliexpressAffiliateProductQueryRequest`

**Description**: This class handles the API requests for querying affiliate products on AliExpress.

**Methods**

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateProductQueryRequest` class.

**Parameters**:

- `domain` (str, optional): The domain name for the API endpoint. Defaults to `"api-sg.aliexpress.com"`.
- `port` (int, optional): The port number for the API endpoint. Defaults to `80`.

**Raises**:

- No specific exceptions documented.


#### `getapiname`

**Description**: Returns the API name for the request.

**Returns**:

- str: The name of the API method, `"aliexpress.affiliate.product.query"`.


```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): The domain name for the API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port number for the API endpoint. Defaults to 80.

    Raises:
        None
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
    Returns:
        str: The name of the API method, "aliexpress.affiliate.product.query".

    Raises:
        None
    """
    return 'aliexpress.affiliate.product.query'
```


**Attributes**:

- `app_signature`:  (NoneType)
- `category_ids`: (NoneType)
- `delivery_days`: (NoneType)
- `fields`: (NoneType)
- `keywords`: (NoneType)
- `max_sale_price`: (NoneType)
- `min_sale_price`: (NoneType)
- `page_no`: (NoneType)
- `page_size`: (NoneType)
- `platform_product_type`: (NoneType)
- `ship_to_country`: (NoneType)
- `sort`: (NoneType)
- `target_currency`: (NoneType)
- `target_language`: (NoneType)
- `tracking_id`: (NoneType)


## Functions

*None*


## Examples

```python
# Example usage (requires importing the class and RestApi)
# ... (import statements)

request = AliexpressAffiliateProductQueryRequest()
# Set parameters for the request
request.keywords = "dress"
request.page_size = 10
# ... set other parameters
try:
    response = request.getResponse()  # Call getResponse() method
    # Process the response
    print(response)
excecept Exception as ex:
  print(f"Error: {ex}")

```


**Note**: This example assumes the existence of a `getResponse` method within the `RestApi` class.  A complete example would need to include the necessary imports and the implementation of the `getResponse` method.