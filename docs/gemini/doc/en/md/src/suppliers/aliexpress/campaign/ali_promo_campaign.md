# Module: hypotez/src/suppliers/aliexpress/campaign/ali_promo_campaign.py

## Overview

This module provides functionalities for managing advertising campaigns on the AliExpress platform. It handles data about categories and products, creates and edits JSON files containing campaign information, and utilizes AI for generating campaign data. The `AliPromoCampaign` class facilitates downloading, processing, and managing campaign data, categories, and products, employing AI to generate descriptions and other relevant data. The module supports various languages and currencies, offering flexibility in campaign customization.


## Classes

### `AliPromoCampaign`

**Description**: This class manages advertising campaigns on AliExpress. It handles various tasks including campaign initialization, data processing, AI integration, and file handling.

**Methods**:

#### `__init__`

**Description**: Initializes an `AliPromoCampaign` object for a given campaign.

**Parameters**:
- `campaign_name` (str): The name of the advertising campaign.
- `language` (Optional[str], optional): The language of the campaign. Defaults to None.
- `currency` (Optional[str], optional): The currency of the campaign. Defaults to None.
- `model` (str, optional): The model to use for AI tasks. Defaults to 'openai'.

**Returns**:
- `SimpleNamespace`: An object representing the campaign.


#### `process_campaign`

**Description**: Iterates through campaign categories, processes products within each category using affiliated product generators, and utilizes AI to process category data.

**Example**:
```python
campaign.process_campaign()
```


#### `process_category_products`

**Description**: Processes products in a specific category, leveraging affiliated product generators.

**Parameters**:
- `category_name` (str): The name of the category to process.

**Returns**:
- `Optional[List[SimpleNamespace]]`: A list of `SimpleNamespace` objects representing products, or `None` if no products are found.


#### `process_ai_category`

**Description**: Processes AI-generated data for a specified category.

**Parameters**:
- `category_name` (Optional[str], optional): The name of the category to process. If omitted, all categories are processed.

**Example**:
```python
campaign.process_ai_category("Electronics")
```


#### `process_new_campaign`

**Description**: Creates a new advertising campaign.

**Parameters**:
- `campaign_name` (str): The name of the new campaign.
- `language` (Optional[str], optional): The language of the campaign. Defaults to None.
- `currency` (Optional[str], optional): The currency of the campaign. Defaults to None.

**Returns**:
- `List[Tuple[str, Any]]`: A list of tuples containing category names and their processed results.


#### `dump_category_products_files`

**Description**: Saves product data to JSON files for each product in a category.

**Parameters**:
- `category_name` (str): The name of the category.
- `products` (List[SimpleNamespace]): A list of `SimpleNamespace` objects representing the products.


#### `set_categories_from_directories`

**Description**: Sets campaign categories from directory names within the "category" directory.

**Example**:
```python
campaign.set_categories_from_directories()
```


#### `generate_output`

**Description**: Saves product data in JSON, text, and HTML formats, handling different data formats, including title, promotion links, and category information.



#### `generate_html`


**Description**: Creates HTML files for each category and a root index file.


**Parameters**:
    - `campaign_name` (str): Campaign name.
    - `category_path` (str | Path): Path to save HTML files.
    - `products_list` (list[SimpleNamespace] | SimpleNamespace): List of products to include in HTML.

**Returns**:
    - None

**Example**:
```python
products_list = [
    # ... (product data)
]
category_path = Path("/path/to/category")
await campaign.generate_html("CampaignName", category_path, products_list)
```



#### `generate_html_for_campaign`


**Description**: Generates HTML pages for the entire campaign.



**Parameters**:
    - `campaign_name` (str): Name of the campaign.

**Example**:
```python
campaign.generate_html_for_campaign("HolidaySale")
```


## Functions

(No functions are listed other than those inside the class.)

```