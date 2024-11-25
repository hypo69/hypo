```markdown
# hypotez/src/suppliers/aliexpress/campaign/gsheet.py

## Overview

This module provides a class `AliCampaignGoogleSheet` for interacting with Google Sheets within AliExpress campaigns. It inherits from the `SpreadSheet` class and offers methods for managing worksheets, recording category and product data, and formatting the sheets.  The module utilizes the gspread library for Google Sheets interaction and includes error handling using `try...except` blocks and logging via the `logger` module.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [`AliCampaignGoogleSheet`](#alicampaigngooglesheet)
        * [`__init__`](#init)
        * [`clear`](#clear)
        * [`delete_products_worksheets`](#delete_products_worksheets)
        * [`set_campaign_worksheet`](#set_campaign_worksheet)
        * [`set_products_worksheet`](#set_products_worksheet)
        * [`set_categories_worksheet`](#set_categories_worksheet)
        * [`get_categories`](#get_categories)
        * [`set_category_products`](#set_category_products)
        * [`_format_categories_worksheet`](#_format_categories_worksheet)
        * [`_format_category_products_worksheet`](#_format_category_products_worksheet)


## Classes

### `AliCampaignGoogleSheet`

**Description**: A class for managing Google Sheets within AliExpress campaigns.  It inherits from the `SpreadSheet` class and provides additional methods for specific campaign-related tasks.

**Attributes**:

- `spreadsheet_id`: (str) The ID of the Google Sheets spreadsheet.
- `spreadsheet`: (SpreadSheet) The initialized SpreadSheet object.
- `worksheet`: (Worksheet) The active worksheet object.


**Methods**:

#### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None) -> None:
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
```

#### `clear`

```python
def clear(self) -> None:
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

#### `delete_products_worksheets`

```python
def delete_products_worksheets(self) -> None:
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
```


#### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace) -> None:
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
```

#### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str) -> None:
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
```


#### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace) -> None:
    """ Write data from a SimpleNamespace object with categories to Google Sheets.
    @param categories `SimpleNamespace`: Object where keys are categories with data to write.
    """
```


#### `get_categories`

```python
def get_categories(self) -> list:
    """ Retrieve data from the 'categories' Google Sheets worksheet.
    @return Data from the worksheet as a list of dictionaries.
    """
```


#### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict) -> None:
    """ Write product data to a new Google Sheets worksheet.
    @param category_name Name of the category.
    @param products Dictionary with product data.
    """
```

#### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet) -> None:
    """ Format the 'categories' worksheet.
    @param ws Google Sheets worksheet to format.
    """
```

#### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet) -> None:
    """ Format the category products worksheet.
    @param ws Google Sheets worksheet to format.
    """
```


```
```
**Note:**  The code includes extensive error handling and logging, which is very important for production-level applications, but not detailed in the original description.