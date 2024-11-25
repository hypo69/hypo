# ali_campaign_editor.py

## Overview

This module provides a class `AliCampaignEditor` for managing and editing advertising campaigns on AliExpress. It inherits from `AliPromoCampaign` and facilitates tasks like deleting products, updating product details within categories, updating campaign properties, updating categories in JSON files, retrieving category data, and listing categories.  The module leverages various utility functions for file handling, JSON operations, and data extraction. It also includes error handling and logging mechanisms.


## Classes

### `AliCampaignEditor`

**Description**: This class acts as an editor for AliExpress advertising campaigns. It manages product data, campaign properties, and interactions with Google Sheets (though the Google Sheet functionality is currently commented out).

**Methods**:

#### `__init__`

**Description**: Initializes an `AliCampaignEditor` instance.

**Parameters**:
- `campaign_name` (str): The name of the campaign.
- `language` (Optional[str | dict], optional): The language of the campaign. Defaults to 'EN'.
- `currency` (Optional[str], optional): The currency for the campaign. Defaults to 'USD'.
- `campaign_file` (Optional[str | Path], optional):  A JSON file to load campaign data. Defaults to `None`.

**Raises**:
- `CriticalError`: If neither `campaign_name` nor `campaign_file` is provided.

#### `delete_product`

**Description**: Deletes a product from the campaign's product list.  It checks if the product exists in either a sources.txt or a product-specific file. If the product is found and successfully removed, the updated file is saved.

**Parameters**:
- `product_id` (str): The ID of the product to delete.
- `exc_info` (bool, optional): Whether to include exception details in the log. Defaults to `False`.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")
```

#### `update_product`

**Description**: Updates product details within a specific category.

**Parameters**:
- `category_name` (str): The name of the category containing the product.
- `lang` (str): The language code.
- `product` (dict): A dictionary containing the product details to update.


**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

#### `update_campaign`

**Description**: Updates campaign properties (description, tags, etc.).

#### `update_category`

**Description**: Updates a category in a JSON file.

**Parameters**:
- `json_path` (Path): Path to the JSON file.
- `category` (SimpleNamespace): The category object to update.

**Returns**:
- bool: True if the update was successful, False otherwise.

**Example Usage**:
```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result) # True if successful
```

#### `get_category`

**Description**: Retrieves a category by name.

**Parameters**:
- `category_name` (str): The name of the category to retrieve.

**Returns**:
- Optional[SimpleNamespace]: A `SimpleNamespace` object representing the category, or `None` if not found.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)  # SimpleNamespace or None
```

#### `list_categories`

**Description**: Returns a list of categories in the campaign.

**Returns**:
- Optional[List[str]]: A list of category names, or `None` if no categories are found.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.list_categories
print(categories)  # e.g., ['Electronics', 'Fashion', 'Home']
```


#### `get_category_products`

**Description**: Retrieves product data from JSON files for a given category.

**Parameters**:
- `category_name` (str): The name of the category.


**Returns**:
- Optional[List[SimpleNamespace]]: A list of SimpleNamespace objects representing the products or `None` if no JSON files are found.

**Example Usage**:
```python
products = campaign.get_category_products("Electronics")
print(len(products))
```


## Functions

_(None listed in this module)_


## Exceptions

_(None listed in this module)_