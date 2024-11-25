# prepare_campaigns.py

## Overview

This module prepares AliExpress campaigns by processing categories, handling campaign data, and generating promotional materials.  It utilizes the `AliCampaignEditor` class to interact with campaign data and offers options for processing individual campaigns or all campaigns in a directory.  Command-line arguments are used for flexibility in specifying the campaign name, categories, language, and currency.

## Table of Contents

* [process_campaign_category](#process-campaign-category)
* [process_campaign](#process-campaign)
* [process_all_campaigns](#process-all-campaigns)
* [main_process](#main-process)
* [main](#main)


## Functions

### `process_campaign_category`

**Description**: This function processes a specific category within a campaign, given the campaign name, category name, language, and currency. It returns a list of product titles within the specified category.

**Parameters**:
- `campaign_name` (str): Name of the advertising campaign.
- `category_name` (str): Category for the campaign.
- `language` (str): Language for the campaign.
- `currency` (str): Currency for the campaign.

**Returns**:
- `List[str]`: List of product titles within the category.

**Example Usage**:
```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)
```


### `process_campaign`

**Description**: Processes a single campaign and handles the campaign's setup and processing. This includes fetching data and possibly creating promotional materials.

**Parameters**:
- `campaign_name` (str): Name of the advertising campaign.
- `language` (Optional[str], optional): Language for the campaign. Defaults to None, meaning all available languages will be considered.
- `currency` (Optional[str], optional): Currency for the campaign. Defaults to None, meaning all available currencies will be considered.
- `campaign_file` (Optional[str], optional): Optional path to a specific campaign file. Defaults to None.

**Returns**:
- `bool`: True if the campaign is processed successfully, else False.

**Example Usage**:

```python
res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
```

### `process_all_campaigns`

**Description**: Processes all campaigns in the specified directory (`campaigns_directory`).

**Parameters**:
- `language` (Optional[str], optional): Language for the campaigns. Defaults to None.
- `currency` (Optional[str], optional): Currency for the campaigns. Defaults to None.

**Example Usage**:
```python
process_all_campaigns("EN", "USD")
```


### `main_process`

**Description**: Main function to process a single campaign, handling either all categories or a specific list of categories.

**Parameters**:
- `campaign_name` (str): Name of the advertising campaign.
- `categories` (List[str]): List of categories to process.  If empty, all categories are processed.
- `language` (Optional[str], optional): Language for the campaign. Defaults to None.
- `currency` (Optional[str], optional): Currency for the campaign. Defaults to None.


**Example Usage**:
```python
main_process("summer_sale", ["electronics"], "EN", "USD")  # Process electronics category
main_process("summer_sale", [], "EN", "USD") #Process all categories
```



### `main`

**Description**: Parses command-line arguments to determine which campaigns to process and calls the appropriate processing functions.

**Parameters**: None

**Example Usage**:
```python
python prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
python prepare_campaigns.py --all -l EN -cu USD
```

## Classes


### `AliCampaignEditor`


**Description**: This class is likely responsible for handling the actual campaign data processing, such as retrieving product information from AliExpress or other API calls. (Not shown in this documentation fragment as details of `AliCampaignEditor` are not available.)


```