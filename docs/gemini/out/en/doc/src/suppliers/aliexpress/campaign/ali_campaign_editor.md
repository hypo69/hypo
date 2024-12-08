# AliCampaignEditor Module Documentation

## Overview

This module provides the `AliCampaignEditor` class for managing advertising campaigns on AliExpress.  It facilitates operations like deleting products, updating product and campaign details, and handling interactions with Google Sheets (via the `AliCampaignGoogleSheet` class).  It leverages data structures like `SimpleNamespace` and `dict` for data representation and manipulation.  The module also includes utility functions for file I/O, JSON handling, and data extraction.

## Table of Contents

* [Classes](#classes)
    * [AliCampaignEditor](#alicampaigneditor)
* [Functions (Utility)](#functions-utility)
    * [N/A]


## Classes

### `AliCampaignEditor`

**Description**: This class extends the `AliPromoCampaign` class and provides methods for managing campaign data, interacting with files, and updating data in categories.

**Methods**:

#### `__init__`

**Description**: Initializes the `AliCampaignEditor` object with campaign details.

**Parameters**:
- `campaign_name` (str): The name of the campaign.
- `language` (Optional[str | dict], optional): The language of the campaign. Defaults to 'EN'.
- `currency` (Optional[str], optional): The currency of the campaign. Defaults to 'USD'.
- `campaign_file` (Optional[str | Path], optional): Optionally load a `<lang>_<currency>.json` file from the campaign root folder. Defaults to `None`.


**Raises**:
- `CriticalError`: If neither `campaign_name` nor `campaign_file` is provided.

#### `delete_product`

**Description**: Deletes a product from the campaign's product list.  If the product file is not found, it renames the file to add an underscore (e.g., 'product.html' -> 'product_.html')


**Parameters**:
- `product_id` (str): The ID of the product to delete.
- `exc_info` (bool, optional): Whether to include exception information in the log. Defaults to `False`.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")
```

#### `update_product`

**Description**: Updates product details within a specified category.

**Parameters**:
- `category_name` (str): The name of the category to update.
- `lang` (str): The language of the campaign.
- `product` (dict): A dictionary containing the product details to update.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

#### `update_campaign`

**Description**: Updates campaign properties like description and tags.

#### `update_category`

**Description**: Updates a category in a JSON file.

**Parameters**:
- `json_path` (Path): Path to the JSON file.
- `category` (SimpleNamespace): Category object to update.

**Returns**:
- bool: `True` if the update is successful, `False` otherwise.

**Example Usage**:
```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)  # True if successful
```

#### `get_category`

**Description**: Retrieves a category from the campaign.

**Parameters**:
- `category_name` (str): The name of the category to retrieve.

**Returns**:
- Optional[SimpleNamespace]: The category object if found, otherwise `None`.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)  # SimpleNamespace or None
```

#### `list_categories`

**Description**: Retrieves a list of category names.

**Returns**:
- Optional[List[str]]: A list of category names or `None` if no categories are found.

**Example Usage**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.list_categories
print(categories)  # ['Electronics', 'Fashion', 'Home']
```

#### `get_category_products`

**Description**: Retrieves product data for a given category.


**Parameters**:
- `category_name` (str): The name of the category.

**Returns**:
- Optional[List[SimpleNamespace]]: A list of SimpleNamespace objects representing products, or None if no matching JSON files are found.


**Example Usage**:
```python
products = campaign.get_category_products("Electronics")
print(len(products))  # Output: 15
```


## Functions (Utility)


N/A