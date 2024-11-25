# html_generators.py

## Overview

This module provides classes for generating HTML content for advertising campaigns. It handles generating HTML for individual products, categories of products, and the overall campaign overview.  The generated HTML uses Bootstrap for styling.

## Table of Contents

* [ProductHTMLGenerator](#producthtmlgenerator)
* [CategoryHTMLGenerator](#categoryhtmlgenerator)
* [CampaignHTMLGenerator](#campaignhtmlgenerator)


## Classes

### `ProductHTMLGenerator`

**Description**: This class is responsible for creating HTML files for individual products.

**Methods**

#### `set_product_html`

**Description**: Generates and saves HTML content for a single product.

**Parameters**

* `product` (SimpleNamespace): The product details (must be a `SimpleNamespace` object) containing data to include in the HTML.
* `category_path` (str | Path): The path to the directory where the HTML file should be saved.

**Raises**:
* No exceptions explicitly raised, but `save_text_file` from `src.utils.file` could raise exceptions related to file handling (e.g., `IOError`).


### `CategoryHTMLGenerator`

**Description**: This class is responsible for creating HTML files for product categories.

**Methods**

#### `set_category_html`

**Description**: Generates and saves HTML content for a category of products.

**Parameters**

* `products_list` (list[SimpleNamespace] | SimpleNamespace): A list of product details (`SimpleNamespace` objects) to include in the category page or a single product (`SimpleNamespace` object) if it is a single product.
* `category_path` (str | Path): The path to the directory where the HTML file should be saved.


**Raises**:
* No exceptions explicitly raised, but `save_text_file` from `src.utils.file` could raise exceptions related to file handling (e.g., `IOError`).


### `CampaignHTMLGenerator`

**Description**: This class is responsible for creating HTML files for the overall campaign, listing all the categories.

**Methods**

#### `set_campaign_html`

**Description**: Generates and saves the HTML content for the campaign overview, listing all categories.

**Parameters**

* `categories` (list[str]): A list of category names (strings).
* `campaign_path` (str | Path): The path to the directory where the HTML file should be saved for the campaign.


**Raises**:
* No exceptions explicitly raised, but `save_text_file` from `src.utils.file` could raise exceptions related to file handling (e.g., `IOError`).


## Functions (None)

```