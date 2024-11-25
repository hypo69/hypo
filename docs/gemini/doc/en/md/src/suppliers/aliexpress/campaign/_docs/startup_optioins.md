# Prepare AliExpress Campaigns

## Overview

This module prepares materials for advertising campaigns on AliExpress.  It handles initialization, creating directories, saving campaign configurations, collecting product data, creating promotional materials, and reviewing the campaign before publishing.  The process is designed to be modular, allowing for individual steps to be performed or skipped as needed.  The script uses command-line arguments for flexibility in managing campaigns, categories, languages, and currencies.


## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`update_category`](#update_category)
    * [`process_campaign_category`](#process-campaign-category)
    * [`process_campaign`](#process-campaign)
* [Asynchronous Function](#asynchronous-function)
    * [`main`](#main)
* [Example Usage and Testing](#example-usage-and-testing)



## Functions

### `update_category`

**Description**: Updates a category in a JSON file.

**Parameters**:
- `json_path` (Path): Path to the JSON file.
- `category` (SimpleNamespace): Category object to be updated.


**Returns**:
- `bool`: `True` if the update is successful, `False` otherwise.

**Raises**:
- `Exception`: Any exception encountered during file handling or JSON processing.


### `process_campaign_category`

**Description**: Processes a specific category within a campaign.

**Parameters**:
- `campaign_name` (str): Name of the campaign.
- `category_name` (str): Name of the category.
- `language` (str): Language of the campaign.
- `currency` (str): Currency of the campaign.
- `force` (bool, optional): If `True`, forces update of the category. Defaults to `False`.


**Returns**:
- `Optional[bool]`: `True` if the category processing is successful, `False` otherwise.

**Raises**:
- `Exception`: If there's an error during the process.


### `process_campaign`

**Description**: Processes an entire campaign for all categories.

**Parameters**:
- `campaign_name` (str): Name of the advertising campaign.
- `categories` (List[str] | None, optional): List of categories for the campaign. Defaults to processing all categories found.
- `language` (str, optional): Language for the campaign. Defaults to 'EN'.
- `currency` (str, optional): Currency for the campaign. Defaults to 'USD'.
- `force` (bool, optional): If `True`, forces update of the categories. Defaults to `False`.


**Returns**:
- `None`: Returns `None`.

**Raises**:
- `Exception`: If there's an error processing the campaign.


## Asynchronous Function

### `main`

**Description**: Asynchronous main function to process a campaign.

**Parameters**:
- `campaign_name` (str): Name of the advertising campaign.
- `categories` (List[str]): List of categories for the campaign.
- `language` (str): Language for the campaign.
- `currency` (str): Currency for the campaign.
- `force` (bool, optional): If `True`, forces update of the categories. Defaults to `False`.


**Returns**:
- `None`: Returns `None`.

**Raises**:
- `Exception`: Any exception encountered during asynchronous operations.


## Example Usage and Testing

1. **Creating a new campaign with specific categories:**

   ```bash
   python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD -f
   ```

2. **Processing multiple categories:**

   ```bash
   python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics fashion -l EN -cu USD -f
   ```