# hypotez/src/suppliers/chat_gpt/gsheet.py

## Overview

This module provides a class `GptGs` for managing Google Sheets related to AliExpress campaigns. It inherits from `SpreadSheet` and allows for writing category and product data, clearing data, and formatting sheets.  The class interacts with Google Sheets to update and retrieve campaign, category, and product information.

## Table of Contents

- [Classes](#classes)
    - [`GptGs`](#gptgs)
- [Functions](#functions)
    - [`clear`](#clear)
    - [`update_chat_worksheet`](#update_chat_worksheet)
    - [`get_campaign_worksheet`](#get_campaign_worksheet)
    - [`set_category_worksheet`](#set_category_worksheet)
    - [`get_category_worksheet`](#get_category_worksheet)
    - [`set_categories_worksheet`](#set_categories_worksheet)
    - [`get_categories_worksheet`](#get_categories_worksheet)
    - [`set_product_worksheet`](#set_product_worksheet)
    - [`get_product_worksheet`](#get_product_worksheet)
    - [`set_products_worksheet`](#set_products_worksheet)
    - [`delete_products_worksheets`](#delete_products_worksheets)
    - [`save_categories_from_worksheet`](#save_categories_from_worksheet)
    - [`save_campaign_from_worksheet`](#save_campaign_from_worksheet)


## Classes

### `GptGs`

**Description**: This class manages Google Sheets for AliExpress campaigns, handling data input, output, and worksheet management.

**Methods**:

- [`__init__`](#init)
- [`clear`](#clear)
- [`update_chat_worksheet`](#update_chat_worksheet)
- [`get_campaign_worksheet`](#get_campaign_worksheet)
- [`set_category_worksheet`](#set_category_worksheet)
- [`get_category_worksheet`](#get_category_worksheet)
- [`set_categories_worksheet`](#set_categories_worksheet)
- [`get_categories_worksheet`](#get_categories_worksheet)
- [`set_product_worksheet`](#set_product_worksheet)
- [`get_product_worksheet`](#get_product_worksheet)
- [`set_products_worksheet`](#set_products_worksheet)
- [`delete_products_worksheets`](#delete_products_worksheets)
- [`save_categories_from_worksheet`](#save_categories_from_worksheet)
- [`save_campaign_from_worksheet`](#save_campaign_from_worksheet)

#### `__init__(self, campaign_name: str, category_name: str, language: str = None, currency: str = None)`

**Description**: Initializes the `GptGs` object with the Google Sheets spreadsheet ID and optional campaign parameters.

**Parameters**:

- `campaign_name` (str): The name of the campaign.
- `category_name` (str): The name of the category.
- `language` (str, optional): The language for the campaign. Defaults to `None`.
- `currency` (str, optional): The currency for the campaign. Defaults to `None`.


#### `clear(self)`

**Description**: Clears data in specified sheets, deleting product sheets and clearing data in the category and campaign sheets.

**Raises**:
- `Exception`: An exception if any error occurs during sheet deletion or clearing.


#### `update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None)`

**Description**: Writes campaign data to a Google Sheets worksheet.

**Parameters**:
- `data` (SimpleNamespace|dict|list): Data object containing campaign information.
- `conversation_name` (str): The name of the conversation worksheet.
- `language` (str, optional): Language parameter, defaults to `None`.

**Raises**:
- `Exception`: Error writing campaign data to the worksheet


#### `get_campaign_worksheet(self) -> SimpleNamespace`

**Description**: Reads campaign data from the 'campaign' worksheet.


**Returns**:
- SimpleNamespace: A SimpleNamespace object containing campaign data.


**Raises**:
- `ValueError`: If the 'campaign' worksheet is not found.
- `Exception`: An exception if any error occurs during data retrieval.

#### `set_category_worksheet(self, category: SimpleNamespace | str)`

**Description**: Writes category data to the 'category' worksheet.

**Parameters**:

- `category` (SimpleNamespace): Data object containing category information.


**Raises**:
- `TypeError`: If `category` is not a `SimpleNamespace` object.
- `Exception`: An exception if any error occurs during data writing.

#### `get_category_worksheet(self) -> SimpleNamespace`

**Description**: Reads category data from the 'category' worksheet.

**Returns**:
- `SimpleNamespace`: A SimpleNamespace object containing category data.

**Raises**:
- `ValueError`: If the 'category' worksheet is not found.
- `Exception`: An exception if any error occurs during data retrieval.

#### `set_categories_worksheet(self, categories: SimpleNamespace)`

**Description**: Writes multiple category data entries from `categories` to the 'categories' worksheet.



**Parameters**:
- `categories` (SimpleNamespace): Object containing multiple category data entries.


**Raises**:
- `Exception`: An exception if any error occurs during data writing.



#### `get_categories_worksheet(self) -> List[List[str]]`

**Description**: Reads category data from the 'categories' worksheet, starting from row 2.

**Returns**:
- `List[List[str]]`: A list of lists containing category data.

**Raises**:
- `ValueError`: If the 'categories' worksheet is not found.
- `Exception`: An exception if any error occurs during data retrieval.


#### `set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`


**Description**: Writes product data to a new worksheet, copying from the 'product_template'.


**Parameters**:
- `category_name` (str): Name of the category.
- `product` (SimpleNamespace): Object containing product information.


**Raises**:
- `Exception`: An exception if any error occurs during data writing.


#### `get_product_worksheet(self) -> SimpleNamespace`

**Description**: Reads product data from the 'products' worksheet.

**Returns**:
- SimpleNamespace: A SimpleNamespace object containing product data.

**Raises**:
- `ValueError`: If the 'products' worksheet is not found.
- `Exception`: An exception if any error occurs during data retrieval.


#### `set_products_worksheet(self, category_name:str)`

**Description**: Writes product data to the worksheet corresponding to the given category name.


**Parameters**:
- `category_name` (str): Name of the category


**Raises**:
- `Exception`: An exception if any error occurs during data writing.


#### `delete_products_worksheets(self)`


**Description**: Deletes all worksheets except 'categories', 'product', 'category', and 'campaign'.


**Raises**:
- `Exception`: An exception if any error occurs during sheet deletion.


#### `save_categories_from_worksheet(self, update:bool=False)`

**Description**: Saves the edited categories data from the worksheet. Updates the `self.campaign.category` attribute.


**Parameters**:
- `update` (bool, optional): If True, updates the campaign. Defaults to False.



#### `save_campaign_from_worksheet(self)`

**Description**: Saves the campaign data from the worksheet. Updates the `self.campaign` attribute.


**Raises**:
- `Exception`: If any error occurs during data saving.


## Functions

No functions are listed outside of class methods.