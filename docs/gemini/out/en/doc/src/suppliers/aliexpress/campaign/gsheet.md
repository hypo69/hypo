# hypotez/src/suppliers/aliexpress/campaign/gsheet.py

## Overview

This module provides a class `AliCampaignGoogleSheet` for interacting with Google Sheets in the context of AliExpress campaigns. It inherits from `SpreadSheet` and offers methods for managing Google Sheets worksheets, recording category and product data, and formatting sheets.  It handles data from `SimpleNamespace` objects, which likely contain campaign, category, and product data.  The module also includes error handling using `try...except` blocks and logging using the `logger`.


## Classes

### `AliCampaignGoogleSheet`

**Description**: This class provides methods for interacting with Google Sheets specific to AliExpress campaigns.  It manages campaigns, categories, and products within the spreadsheet.

**Methods**:

#### `__init__`

**Description**: Initializes an instance of `AliCampaignGoogleSheet`.

**Parameters**:
- `campaign_name` (str): The name of the campaign.
- `language` (str | dict, optional): The language for the campaign. Defaults to `None`.
- `currency` (str, optional): The currency for the campaign. Defaults to `None`.

**Raises**:
- No exceptions are explicitly defined in the docstring.


#### `clear`

**Description**: Clears the contents of the spreadsheet by deleting all product sheets while preserving the 'categories' and 'product_template' sheets.

**Raises**:
- `Exception`:  A generic exception in case of an error during clearing. Error details are logged.


#### `delete_products_worksheets`

**Description**: Deletes all worksheets from the Google Sheets spreadsheet except 'categories', 'product', 'category', and 'campaign'.

**Raises**:
- `Exception`: Raised if there is an error during worksheet deletion. Error details are logged.


#### `set_campaign_worksheet`

**Description**: Writes campaign data to the 'campaign' worksheet.

**Parameters**:
- `campaign` (SimpleNamespace | str): SimpleNamespace object containing campaign data.

**Raises**:
- `Exception`:  Raised for errors during writing campaign data. Error details are logged.


#### `set_products_worksheet`

**Description**: Writes product data from a list of `SimpleNamespace` objects to a new sheet for a specific category.

**Parameters**:
- `category_name` (str): The name of the category to write products for.


**Raises**:
- `Exception`:  A generic exception for errors while writing product data. Error details are logged.


#### `set_categories_worksheet`

**Description**: Writes category data from a `SimpleNamespace` object to the 'categories' worksheet.  Clears the existing worksheet before writing.

**Parameters**:
- `categories` (SimpleNamespace): Object containing category data.


**Raises**:
- `Exception`:  Raised for errors during writing category data. Error details are logged.


#### `get_categories`

**Description**: Retrieves category data from the 'categories' worksheet.

**Returns**:
- list of dict:  A list of dictionaries, where each dictionary represents a category from the worksheet.

**Raises**:
- No exceptions are explicitly defined in the docstring.


#### `set_category_products`

**Description**: Writes product data to a new worksheet for a specific category.

**Parameters**:
- `category_name` (str): The name of the category.
- `products` (dict): Dictionary containing product data.

**Raises**:
- `Exception`: Raised for errors during writing products data. Error details are logged.


#### `_format_categories_worksheet`

**Description**: Formats the 'categories' worksheet by setting column widths and formatting headers.

**Parameters**:
- `ws` (Worksheet): The worksheet to format.

**Raises**:
- `Exception`: Raised for formatting errors. Error details are logged.


#### `_format_category_products_worksheet`

**Description**: Formats the worksheet containing product data for a specific category by setting column widths and formatting headers.

**Parameters**:
- `ws` (Worksheet): The worksheet to format.

**Raises**:
- `Exception`: Raised for formatting errors. Error details are logged.


## Functions

No functions are present in this file.