# AliExpress Campaign Management Module

## Overview

This module provides functionalities for managing and editing promotional campaigns within the AliExpress system.  It interacts with Google Sheets for data retrieval and manipulation, and prepares campaign data for use.  The module leverages various utilities for file operations, JSON handling, and data conversion.


## Table of Contents

* [AliPromoCampaign](#alipromocampaign)
* [Functions](#functions)


## AliPromoCampaign Class

### `AliPromoCampaign`

**Description**:  Manages a single AliExpress promotional campaign.  It fetches data from Google Sheets, initializes campaign details, and prepares product information.

**Constructor Parameters**:

* `campaign_name` (str): Name of the campaign.
* `category_name` (str): Name of the campaign category.
* `language` (str): Language of the campaign.
* `currency` (str): Currency of the campaign.
* `force_update` (bool, optional):  If `True`, forces an update of the campaign data from Google Sheets, overriding any cached data. Defaults to `False`.

**Methods**:

* `__init__(campaign_name, category_name, language, currency, force_update)`: Initializes the campaign object, loads campaign data, retrieves category data, and prepares product information.
* `initialize_campaign()`: Loads campaign data and initializes internal attributes (`self.campaign`, `self.title`, `self.category`, `self.category.products`).
* `get_category_from_campaign()`: Retrieves the category data from the loaded campaign data.
* `get_category_products(force_update)`: Retrieves product data for the specified category.
* `create_product_namespace(**kwargs)`: Creates a `SimpleNamespace` object to represent a product.
* `create_campaign_namespace(**kwargs)`: Creates a `SimpleNamespace` object to represent a campaign.
* `prepare_products()`: Prepares product data for use in other parts of the system, including interactions with affiliate product generators, file processing, and CSV data conversion.


## Functions

### `process_campaign_category`

**Description**: Processes a single campaign category.

**Parameters**:
- `category_name` (str): Name of the category to process.
- `campaign_name` (str): Name of the campaign associated with the category.
- `language` (str): Language of the campaign.
- `currency` (str): Currency of the campaign.
- `force` (bool, optional): If `True`, forces an update of the category data. Defaults to `False`.

**Returns**:
- `None`


### `process_campaign`

**Description**: Processes a specific campaign.

**Parameters**:
- `campaign_name` (str): Name of the campaign to process.
- `categories` (List[str], optional): List of categories to include in the processing. Defaults to all categories.
- `language` (str): Language of the campaign.
- `currency` (str): Currency of the campaign.
- `force` (bool, optional): If `True`, forces an update of the campaign data. Defaults to `False`.

**Returns**:
- `None`

### `process_all_campaigns`

**Description**: Processes all campaigns.

**Parameters**:
- `language` (str): Language of the campaigns.
- `currency` (str): Currency of the campaigns.
- `force` (bool, optional): If `True`, forces an update of all campaign data. Defaults to `False`.

**Returns**:
- `None`