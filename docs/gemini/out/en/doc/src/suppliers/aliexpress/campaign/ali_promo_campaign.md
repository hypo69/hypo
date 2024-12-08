# Module: ali_promo_campaign.py

## Overview

This module provides functionality for managing advertising campaigns on the AliExpress platform. It handles data processing for categories and products, creation and editing of JSON files containing campaign information, and utilizes AI for generating campaign data.  The `AliPromoCampaign` class facilitates data loading, processing, category/product management, and AI-powered data generation.  The module supports various languages and currencies for campaign customization.


## Classes

### `AliPromoCampaign`

**Description**:  This class manages an advertising campaign. It loads campaign data, handles categories and products, and incorporates AI for generating data.

**Methods**:

#### `__init__`

**Description**: Initializes an `AliPromoCampaign` object for a given campaign.

**Parameters**:
- `campaign_name` (str): The name of the advertising campaign.
- `language` (Optional[str], optional): The language used in the campaign. Defaults to None.
- `currency` (Optional[str], optional): The currency used in the campaign. Defaults to None.
- `model` (str, optional): The AI model to use, defaults to 'openai'.

**Returns**:
- `SimpleNamespace`: The initialized campaign object.

**Raises**:
- `Exception`: If there's an error during initialization.

#### `process_campaign`

**Description**: Iterates through campaign categories, processes product data using the affiliate product generator, and handles AI category processing.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- `Exception`: If an error occurs during campaign processing.

#### `process_category_products`

**Description**: Processes products within a specific category.  Uses an affiliated products generator to get details of products.

**Parameters**:
- `category_name` (str): The name of the category to process.

**Returns**:
- Optional[List[SimpleNamespace]]: A list of product data (`SimpleNamespace` objects) if products are found, otherwise `None`.

**Raises**:
- `Exception`: If an error occurs during product processing.


#### `process_ai_category`

**Description**: Processes AI-generated data for a specific category or all categories, updating or creating category details.

**Parameters**:
- `category_name` (Optional[str], optional):  The name of the category to process. Defaults to None (all categories if omitted).


**Returns**:
- None

**Raises**:
- `Exception`: If an error occurs during AI category processing.

#### `process_new_campaign`

**Description**: Creates a new advertising campaign by initializing categories from directories, processing product data, and generating AI data.

**Parameters**:
- `campaign_name` (str): The name of the new campaign.
- `language` (Optional[str], optional): Language for the campaign. Defaults to None.
- `currency` (Optional[str], optional): Currency for the campaign. Defaults to None.

**Returns**:
- `List[Tuple[str, Any]]`: List of tuples, each containing a category name and its processed results. Returns an empty list if no processing is needed.

**Raises**:
- `Exception`: If an error occurs during new campaign creation.


#### `set_categories_from_directories`

**Description**: Sets the campaign categories based on the directories found in the 'category' directory. Converts each directory name to a `SimpleNamespace` object.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- `Exception`: If an error occurs during directory processing.

#### `generate_output`

**Description**: Saves product data in various formats (JSON, HTML), generating links for products in the specified category.

**Parameters**:
- `campaign_name` (str): The name of the campaign.
- `category_path` (Path): The path to the category directory.
- `products_list` (list[SimpleNamespace] | SimpleNamespace): A list of products to save or a single product.

**Returns**:
- None

**Raises**:
- `Exception`: If an error occurs during file saving or data processing.


#### `generate_html_for_campaign`

**Description**: Generates HTML pages for the specified campaign, including category and campaign overview pages.

**Parameters**:
- `campaign_name` (str): The name of the campaign.

**Returns**:
- None

**Raises**:
- `Exception`: If an error occurs during HTML generation or file saving.



## Functions

(These are documented implicitly through the class methods, but are included for completeness)


## Modules Used


This module utilizes various external modules, including:

- `asyncio`
- `time`
- `copy`
- `html`
- `pathlib`
- `typing` (for type hints)
- `header` (likely a custom module)
- `gs` (likely a custom module for Google Drive interaction)
- `src.suppliers.aliexpress.*`
- `src.ai`
- `src.logger`
- `src.utils.file`
- `src.utils.jjson`
- `src.utils.convertors.csv`
- `src.utils.printer`
- `datetime`  (implied use)