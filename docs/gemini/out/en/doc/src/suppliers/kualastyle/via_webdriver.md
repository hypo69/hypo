# Module: hypotez/src/suppliers/kualastyle/via_webdriver.py

## Overview

This module provides functions for parsing product data from the Kualastyle website using a webdriver.  It utilizes the `src.logger` and `src.gs` modules for logging and other helper functions. The module aims to extract product URLs from a category page.


## Functions

### `get_list_products_in_category`

**Description**: This function retrieves a list of product URLs from a given category page.

**Parameters**:

- `s` (Suplier): An object representing the supplier containing driver and locators information.

**Returns**:

- `list[str, str, None]`: A list of product URLs, or `None` if no products are found or an error occurs.

**Raises**:

- `Exception`: Any exception that might occur during the execution of the function, such as issues with the webdriver or locating elements.  This covers issues with `s.driver`, `s.locators.get('category')`, or `d.execute_locator`.


```python
def get_list_products_in_category(s) -> list[str, str, None]:
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
    d = s.driver
    l: dict = s.locators.get('category')
    d.scroll(scroll_count=10, direction="forward")

    _ = d.execute_locator
    list_products_in_category = _(l['product_links'])
    #pprint(list_products_in_category)
    return list_products_in_category
```


```