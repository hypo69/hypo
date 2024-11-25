# Module: hypotez/src/suppliers/kualastyle/via_webdriver.py

## Overview

This module provides functions for interacting with the Kualastyle website via a webdriver, specifically for retrieving product URLs from category pages.  It utilizes the `gs` and `logger` modules for data handling and logging, respectively.


## Functions

### `get_list_products_in_category`

**Description**: Retrieves a list of product URLs from a given category page on the Kualastyle website.

**Parameters**:

- `s` (object): An object representing the supplier, likely containing driver and locator information.

**Returns**:

- `list[str, str, None]`: A list of product URLs. Returns `None` if there's an error.

**Raises**:

- `Exception`:  Any exception that occurs during the process of scrolling or locating elements on the website.