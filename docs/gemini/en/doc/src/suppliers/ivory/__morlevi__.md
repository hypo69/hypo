# Module: hypotez/src/suppliers/ivory/__morlevi__.py

## Overview

This module provides functions for interacting with the Morlevi website, including login, product information retrieval, and pagination through product listings.  It leverages Selenium, requests, pandas, and other libraries for web scraping and data manipulation.  The module also integrates with settings and custom classes for data formatting and storage.

## Classes

(No classes are defined in the provided code.)

## Functions

### `login`

**Description**: This function attempts to log in to the Morlevi website. It handles potential login failures and pop-up windows encountered during the process.

**Parameters**:
- `supplier` (object): An object representing the supplier, likely containing driver and locator information.

**Returns**:
- `bool`: `True` if login is successful, `None` if unsuccessful.


**Raises**:
- `Exception`: A general exception if errors occur during the login process.  More specific exception types are not specified within the provided code, so a generic exception handler should be assumed.


### `_login`

**Description**: This function handles the actual login process. It tries to locate and interact with login elements on the website.

**Parameters**:
- `_s` (object): An object representing the supplier, likely containing driver and locator information.

**Returns**:
- `bool`: `True` if login is successful, `None` otherwise


**Raises**:
- `Exception`: A general exception if errors occur during the login process.


### `grab_product_page`

**Description**: This function retrieves product information from a product page on the Morlevi website.

**Parameters**:
- `s` (object): An object representing the supplier, containing driver and locator information.

**Returns**:
- `Product`: An object representing the product with extracted information.


**Raises**:
- `Exception`: A general exception if errors occur during the product page retrieval process.


### `list_products_in_category_from_pagination`

**Description**: This function retrieves a list of product URLs within a given category by handling pagination.

**Parameters**:
- `supplier` (object): An object representing the supplier, likely containing driver and locator information.


**Returns**:
- `list`: A list of product URLs.  Returns an empty list if no products are found.


**Raises**:
- `Exception`: A general exception if errors occur during the pagination and product listing retrieval process.


### `get_list_products_in_category`

**Description**: This function retrieves a list of product URLs within a category, with additional parameters.

**Parameters**:
- `s` (Supplier): The supplier object.
- `scenario` (JSON): A JSON object containing scenario-specific data.
- `presath` (PrestaShopWebServiceDict): PrestaShop web service data.


**Returns**:
- `list`: A list of product URLs


**Raises**:
- `Exception`: A general exception if errors occur during the product listing retrieval process.


### `get_list_categories_from_site`

**Description**: This function retrieves a list of categories from the Morlevi website.

**Parameters**:
- `s`: The supplier object.
- `scenario_file`: Path to the scenario file.
- `brand` (str, optional): The brand to filter by (default is '').


**Returns**:
- ... (No return value is clearly defined in the provided code.)


**Raises**:
- `Exception`: A general exception if errors occur during category retrieval.


## Modules Imported

The following modules are imported and used:

- `pathlib`
- `requests`
- `pandas` as `pd`
- `selenium.webdriver.remote.webelement`
- `selenium.webdriver.common.keys`
- `settings`
- `gs` (appears to be a custom module)
- `src.suppliers.Product`
- `src.settings`


## Notes

- The provided code heavily relies on custom classes and functions not defined within the snippet.  The documentation assumes the existence of a `Product` class and `settings` module containing relevant components, including `StringFormatter`, `json_loads`, and `logger`.
- Error handling is present but could be improved by specifying more specific exception types.
- The code contains several `TODO` comments, indicating tasks that need to be implemented, such as handling product delivery details and specifications.
- The function `_s.save_and_send_via_ftp` and the `via_ftp` parameter in `set_images` suggest FTP integration.
- The documentation for some functions (e.g., `get_list_categories_from_site`) is incomplete because the return type and detailed operation aren't documented.
- The comments within the code are not consistently formatted for documentation purposes.  Improvements in code style and consistency would result in better documentation.