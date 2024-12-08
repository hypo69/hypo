# AliexpressAffiliateFeaturedpromoProductsGetRequest

## Overview

This module defines the `AliexpressAffiliateFeaturedpromoProductsGetRequest` class, which is used to interact with the AliExpress Affiliate API to retrieve featured promotion products. It inherits from the `RestApi` base class.


## Classes

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Description**: This class provides methods for interacting with the AliExpress Affiliate API to retrieve featured promotion products.


**Methods**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Description**: Initializes the `AliexpressAffiliateFeaturedpromoProductsGetRequest` object.
    **Parameters**:
    - `domain` (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".
    - `port` (int, optional): The port of the API endpoint. Defaults to 80.
    **Raises**: None


- `getapiname(self)`:
    **Description**: Returns the API name for the request.
    **Parameters**:
    None
    **Returns**:
    - str: The API name.
    **Raises**:
    None


**Attributes**:

- `app_signature`:
- `category_id`:
- `country`:
- `fields`:
- `page_no`:
- `page_size`:
- `promotion_end_time`:
- `promotion_name`:
- `promotion_start_time`:
- `sort`:
- `target_currency`:
- `target_language`:
- `tracking_id`:


## Functions

### None

This module does not contain any functions besides the class methods.


## Usage Examples

```python
# Example usage (assuming you have the necessary API credentials and configurations)

from ..base import RestApi
from .AliexpressAffiliateFeaturedpromoProductsGetRequest import AliexpressAffiliateFeaturedpromoProductsGetRequest

# Initialize the request object
request = AliexpressAffiliateFeaturedpromoProductsGetRequest()
request.app_signature = "your_app_signature"  # Replace with your app signature
request.category_id = "your_category_id" # Replace with your category id
# ... set other parameters as needed ...

# Make the API call
response = request.getResponse()

# Check the response for errors and extract the data
# ... process the response ...
```

**Note**: Replace placeholders like `"your_app_signature"` and `"your_category_id"` with your actual API credentials and values. This example demonstrates a basic usage.  Full implementation requires setting the appropriate parameters, handling potential errors, and processing the response data accordingly. Remember to consult the AliExpress Affiliate API documentation for the most up-to-date details and parameters.