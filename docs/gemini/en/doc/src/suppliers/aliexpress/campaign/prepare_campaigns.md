# Module: prepare_campaigns.py

## Overview

This module prepares AliExpress campaigns by processing categories, handling campaign data, and generating promotional materials.  It provides functions for processing individual campaigns, all campaigns, and specific categories within a campaign.  The module leverages the `AliCampaignEditor` class for campaign-specific operations and utilizes `locales` for language and currency handling.


## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`process_campaign_category`](#process-campaign-category)
    * [`process_campaign`](#process-campaign)
    * [`process_all_campaigns`](#process-all-campaigns)
    * [`main_process`](#main-process)
    * [`main`](#main)


## Functions

### `process_campaign_category`

**Description**: Processes a specific category within a campaign for a given language and currency.  This function is designed to be called by `main_process` when specific categories are required within a campaign.

**Parameters**:
* `campaign_name` (str): Name of the advertising campaign.
* `category_name` (str): Category for the campaign.
* `language` (str): Language for the campaign.
* `currency` (str): Currency for the campaign.

**Returns**:
* `List[str]`: List of product titles within the category.

**Example Usage**:

```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)
```

### `process_campaign`

**Description**: Processes a campaign and handles the campaign's setup and processing. It iterates through the defined locales and processes the campaign for each locale.

**Parameters**:
* `campaign_name` (str): Name of the advertising campaign.
* `language` (Optional[str], optional): Language for the campaign. If not provided, processes for all locales. Defaults to `None`.
* `currency` (Optional[str], optional): Currency for the campaign. If not provided, processes for all locales. Defaults to `None`.
* `campaign_file` (Optional[str], optional): Optional path to a specific campaign file. Defaults to `None`.

**Returns**:
* `bool`: True if campaign processed, else False.  Returns `True` to indicate successful processing.


### `process_all_campaigns`

**Description**: Processes all campaigns in the 'campaigns' directory for the specified language and currency. Iterates through all campaign directories, processing campaigns for each defined locale.


**Parameters**:
* `language` (Optional[str], optional): Language for the campaigns. Defaults to None.
* `currency` (Optional[str], optional): Currency for the campaigns. Defaults to None.


**Example Usage**:

```python
process_all_campaigns("EN", "USD")
```

### `main_process`

**Description**: Main function to process a campaign, handling both single-category processing and entire campaign processing based on provided categories.

**Parameters**:
* `campaign_name` (str): Name of the advertising campaign.
* `categories` (List[str] | str): List of categories for the campaign. If empty, processes the entire campaign.
* `language` (Optional[str]): Language for the campaign. Defaults to `None`.
* `currency` (Optional[str]): Currency for the campaign. Defaults to `None`.


**Example Usage**:

```python
main_process("summer_sale", ["electronics"], "EN", "USD")
main_process("summer_sale", [], "EN", "USD")
```


### `main`

**Description**: Main function to parse command-line arguments and initiate the processing of campaigns. Parses arguments for campaign name, categories, language, and currency to call appropriate functions.  Handles the case for processing all campaigns.

**Parameters**:
   None (Parses arguments from command line)

**Example Usage**:

```
python prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
python prepare_campaigns.py --all -l EN -cu USD
```


## Classes (if any)

(No classes defined in this module)


```
```