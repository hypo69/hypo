# AliexpressAffiliateHotproductDownloadRequest

## Overview

This module defines the `AliexpressAffiliateHotproductDownloadRequest` class, which is used to interact with the AliExpress Affiliate API to download hot product data.  It inherits from the `RestApi` base class.


## Classes

### `AliexpressAffiliateHotproductDownloadRequest`

**Description**: This class handles requests to the AliExpress Affiliate API endpoint for downloading hot product data.  It allows setting various parameters to customize the request.

**Methods**:

#### `__init__`

**Description**: Initializes the `AliexpressAffiliateHotproductDownloadRequest` object.

**Parameters**:

- `domain` (str, optional): The domain of the AliExpress Affiliate API endpoint. Defaults to `"api-sg.aliexpress.com"`.
- `port` (int, optional): The port of the AliExpress Affiliate API endpoint. Defaults to `80`.

**Raises**:
  - `TypeError`: If `domain` is not a string or `port` is not an integer.

#### `getapiname`

**Description**: Returns the API name for the request.

**Parameters**:

- None

**Returns**:
- str: The name of the API endpoint, `"aliexpress.affiliate.hotproduct.download"`.


```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Initializes the AliexpressAffiliateHotproductDownloadRequest object.

    Args:
        domain (str, optional): The domain of the AliExpress Affiliate API endpoint. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The port of the AliExpress Affiliate API endpoint. Defaults to 80.

    Raises:
        TypeError: If domain is not a string or port is not an integer.
    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.category_id = None
    self.country = None
    self.fields = None
    self.scenario_language_site = None
    self.page_no = None
    self.page_size = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None


def getapiname(self):
    """
    Returns the API name for the request.

    Returns:
        str: The name of the API endpoint, "aliexpress.affiliate.hotproduct.download".
    """
    return 'aliexpress.affiliate.hotproduct.download'
```


**Attributes:**

- `app_signature`:  (Optional):  Application signature.
- `category_id`: (Optional):  Category ID.
- `country`: (Optional):  Country code.
- `fields`: (Optional):  Fields to include in the response.
- `scenario_language_site`: (Optional):  Scenario language and site.
- `page_no`: (Optional):  Page number for pagination.
- `page_size`: (Optional):  Page size for pagination.
- `target_currency`: (Optional):  Target currency.
- `target_language`: (Optional):  Target language.
- `tracking_id`: (Optional):  Tracking ID.


This documentation assumes `RestApi` is defined elsewhere in a separate module.  If not, you'd need to provide that class's definition for a complete, usable document.