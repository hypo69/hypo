# Module: hypotez/src/suppliers/chat_gpt/gsheet.py

## Overview

This module provides a class `GptGs` for managing Google Sheets related to AliExpress campaigns. It inherits from `SpreadSheet` and allows for operations such as writing campaign data, category data, product data, clearing sheets, and retrieving data from various sheets. It also handles error handling and logging using the `logger` module.


## Table of Contents

* [Classes](#classes)
    * [GptGs](#gptgs)
* [Functions](#functions)
    * [clear](#clear)
    * [update_chat_worksheet](#update_chat_worksheet)
    * [get_campaign_worksheet](#get_campaign_worksheet)
    * [set_category_worksheet](#set_category_worksheet)
    * [get_category_worksheet](#get_category_worksheet)
    * [set_categories_worksheet](#set_categories_worksheet)
    * [get_categories_worksheet](#get_categories_worksheet)
    * [set_product_worksheet](#set_product_worksheet)
    * [get_product_worksheet](#get_product_worksheet)
    * [set_products_worksheet](#set_products_worksheet)
    * [delete_products_worksheets](#delete_products_worksheets)
    * [save_categories_from_worksheet](#save_categories_from_worksheet)
    * [save_campaign_from_worksheet](#save_campaign_from_worksheet)


## Classes

### `GptGs`

**Description**: This class manages Google Sheets for AliExpress campaigns, inheriting from `SpreadSheet` to handle spreadsheet operations. It allows writing and retrieving data from various campaign-related worksheets.

**Methods**:

* **`__init__(self, campaign_name: str, category_name: str, language: str, currency: str)`**:
    **Description**: Initializes the `GptGs` object.
    **Parameters**:
        - `campaign_name` (str): The name of the campaign.
        - `category_name` (str): The name of the category.
        - `language` (str): The language for the campaign.
        - `currency` (str): The currency for the campaign.
    **Raises**:
        - `TypeError`: If the input types are incorrect.


* **`clear(self)`**:
    **Description**: Clears contents of specified sheets (categories, campaign, etc.).
    **Parameters**:
        None
    **Raises**:
        - `Exception`: If an error occurs during sheet clearing.


* **`update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name: str, language: str = None, currency: str = None)`**:
    **Description**: Writes campaign data to a Google Sheets worksheet.
    **Parameters**:
        - `data` (SimpleNamespace | dict | list): SimpleNamespace object with campaign data.
        - `conversation_name` (str): The name of the sheet.
        - `language` (str, optional): The language for the campaign (defaults to None).
        - `currency` (str, optional): The currency for the campaign (defaults to None).
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during writing.


* **`get_campaign_worksheet(self)`**:
    **Description**: Reads campaign data from the 'campaign' worksheet.
    **Parameters**:
        None
    **Returns**:
        `SimpleNamespace`: SimpleNamespace object with campaign data fields.
    **Raises**:
        - `ValueError`: If the 'campaign' worksheet is not found.
        - `Exception`: If an error occurs during reading.

* **`set_category_worksheet(self, category: SimpleNamespace | str)`**:
    **Description**: Writes category data to the 'category' worksheet vertically.
    **Parameters**:
        - `category` (SimpleNamespace): SimpleNamespace object containing category data.
    **Returns**:
        None.
    **Raises**:
        - `TypeError`: If the input is not a SimpleNamespace object.
        - `Exception`: If an error occurs during writing.


* **`get_category_worksheet(self)`**:
    **Description**: Reads category data from the 'category' worksheet.
    **Parameters**:
        None
    **Returns**:
        `SimpleNamespace`: SimpleNamespace object with category data fields.
    **Raises**:
        - `ValueError`: If the 'category' worksheet is not found.
        - `Exception`: If an error occurs during reading.


* **`set_categories_worksheet(self, categories: SimpleNamespace)`**:
    **Description**: Writes data from a SimpleNamespace object to the 'categories' worksheet.
    **Parameters**:
        - `categories` (SimpleNamespace): SimpleNamespace object containing category data.
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during writing.



* **`get_categories_worksheet(self)`**:
    **Description**: Reads category data from the 'categories' worksheet.
    **Parameters**:
        None
    **Returns**:
        List[List[str]]: List of rows with data from columns A to E.
    **Raises**:
        - `ValueError`: If the 'categories' worksheet is not found.
        - `Exception`: If an error occurs during reading.


* **`set_product_worksheet(self, product: SimpleNamespace | str, category_name: str)`**:
    **Description**: Writes product data to a new Google Sheets worksheet.
    **Parameters**:
        - `product` (SimpleNamespace): SimpleNamespace object containing product data.
        - `category_name` (str): The category name for the new product sheet.
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during writing.



* **`get_product_worksheet(self)`**:
    **Description**: Reads product data from the 'products' worksheet.
    **Parameters**:
        None
    **Returns**:
        `SimpleNamespace`: SimpleNamespace object with product data fields.
    **Raises**:
        - `ValueError`: If the 'products' worksheet is not found.
        - `Exception`: If an error occurs during reading.


* **`set_products_worksheet(self, category_name: str)`**:
    **Description**: Writes product data to the 'products' worksheet in the given category.
    **Parameters**:
        - `category_name` (str): The name of the category.
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during writing.


* **`delete_products_worksheets(self)`**:
    **Description**: Deletes all sheets except 'categories' and 'product_template'.
    **Parameters**:
        None
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during deletion.


* **`save_categories_from_worksheet(self, update: bool = False)`**:
    **Description**: Saves category data from the worksheet.
    **Parameters**:
        - `update` (bool, optional): Whether to update the campaign after saving (defaults to False).
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during saving.



* **`save_campaign_from_worksheet(self)`**:
    **Description**: Saves campaign data from the worksheet.
    **Parameters**:
        None.
    **Returns**:
        None.
    **Raises**:
        - `Exception`: If an error occurs during saving.




## Functions

(No functions defined outside of class methods in this module.)