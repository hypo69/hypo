# html_generators.py

## Overview

This module provides classes for generating HTML content for AliExpress advertising campaigns. It allows generating HTML for individual products, product categories, and the campaign overview.  The generated HTML files incorporate Bootstrap styling and link to external CSS files for improved presentation.

## Table of Contents

* [ProductHTMLGenerator](#producthtmlgenerator)
* [CategoryHTMLGenerator](#categoryhtmlgenerator)
* [CampaignHTMLGenerator](#campaignhtmlgenerator)

## Classes

### `ProductHTMLGenerator`

**Description**: This class is responsible for generating HTML content for individual products.  It creates and saves HTML files containing product details.

**Methods**

#### `set_product_html`

**Description**: Generates an HTML file containing product information.

**Parameters**
- `product` (SimpleNamespace): An object containing the product details (e.g., title, price, image URL, etc.).
- `category_path` (str | Path): The path to the directory where the HTML file should be saved.

**Returns**
- None

**Raises**
- `TypeError`: If `product` is not a SimpleNamespace object, or `category_path` is an unsupported type.
- `FileNotFoundError`: If the image file specified in `product.local_image_path` does not exist.


### `CategoryHTMLGenerator`

**Description**: This class generates HTML content for product categories. It creates an HTML file listing all the products within a specific category.

**Methods**

#### `set_category_html`

**Description**: Generates an HTML file for the specified category containing product listings.

**Parameters**
- `products_list` (list[SimpleNamespace] | SimpleNamespace): A list of SimpleNamespace objects representing product details, or a single SimpleNamespace object representing a product if only one product is in a category.
- `category_path` (str | Path): Path to the directory where the HTML file should be saved.


**Returns**
- None

**Raises**
- `TypeError`: If `products_list` is not a list or a SimpleNamespace object, or `category_path` is an unsupported type.


### `CampaignHTMLGenerator`

**Description**: This class generates an HTML file that provides an overview of the campaign by listing all categories.

**Methods**

#### `set_campaign_html`

**Description**: Generates an HTML file outlining all the categories included in the campaign.

**Parameters**
- `categories` (list[str]): A list of category names.
- `campaign_path` (str | Path): The path to the directory where the campaign overview HTML file should be saved.

**Returns**
- None


**Raises**
- `TypeError`: If `categories` is not a list of strings, or `campaign_path` is an unsupported type.