# AliexpressAffiliateLinkGenerateRequest

## Overview

This module defines the `AliexpressAffiliateLinkGenerateRequest` class, which is used to generate affiliate links on AliExpress. It inherits from the `RestApi` base class.


## Classes

### `AliexpressAffiliateLinkGenerateRequest`

**Description**: This class handles the generation of affiliate links on AliExpress using the corresponding API endpoint. It allows setting parameters such as application signature, promotion link type, source values, and tracking ID.

**Methods**:

- `__init__`: Initializes the `AliexpressAffiliateLinkGenerateRequest` object.

    ```python
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.promotion_link_type = None
        self.source_values = None
        self.tracking_id = None

    ```

    **Parameters**:
    - `domain` (str): The domain of the AliExpress API endpoint. Defaults to "api-sg.aliexpress.com".
    - `port` (int): The port of the AliExpress API endpoint. Defaults to 80.

    **Returns**:
    - None

- `getapiname`: Returns the API name for generating affiliate links.

    ```python
    def getapiname(self):
        return 'aliexpress.affiliate.link.generate'
    ```

    **Returns**:
    - str: The name of the API endpoint, "aliexpress.affiliate.link.generate".


## Attributes

- `app_signature`:  Application signature.  (Type: `None`)
- `promotion_link_type`: Promotion link type. (Type: `None`)
- `source_values`: Source values. (Type: `None`)
- `tracking_id`: Tracking ID. (Type: `None`)


## Function Summary

This file primarily defines a class for interacting with the AliExpress affiliate link generation API.  It does not contain standalone functions.