# AliexpressApi Module

## Overview

This module provides a Python wrapper for the AliExpress Open Platform API. It simplifies the process of retrieving product information, affiliate links, and categories.

## Table of Contents

* [AliexpressApi](#aliexpressapi-class)
    * [retrieve_product_details](#retrieve_product_details)
    * [get_affiliate_links](#get_affiliate_links)
    * [get_hotproducts](#get_hotproducts)
    * [get_categories](#get_categories)
    * [get_parent_categories](#get_parent_categories)
    * [get_child_categories](#get_child_categories)

## Classes

### `AliexpressApi`

**Description**: This class provides methods for interacting with the AliExpress API.

**Parameters**:

- `key` (str): Your API key.
- `secret` (str): Your API secret.
- `language` (model_Language): Language code. Defaults to EN.
- `currency` (model_Currency): Currency code. Defaults to USD.
- `tracking_id` (str, optional): The tracking ID for link generation. Defaults to None.
- `app_signature` (str, optional):  Application signature. Defaults to None.
- `**kwargs` (optional): Other keyword arguments.

**Methods**:

#### `retrieve_product_details`

**Description**: Retrieves product information.

**Parameters**:

- `product_ids` (str | list[str]): One or more product IDs or URLs.
- `fields` (str | list[str], optional): Fields to include in the results. Defaults to all fields.
- `country` (str, optional): Filter products by country.  Defaults to None.

**Returns**:

- list[model_Product]: A list of product objects.

**Raises**:

- `ProductsNotFoudException`: If no products are found for the given parameters.
- `InvalidArgumentException`: If invalid parameters are provided.
- `ApiRequestException`: If there is an error during the API request.
- `ApiRequestResponseException`: If there is an error in processing the API response.


#### `get_affiliate_links`

**Description**: Converts a list of links to affiliate links.

**Parameters**:

- `links` (str | list[str]): One or more links to convert.
- `link_type` (model_LinkType, optional): The type of link to generate (e.g., NORMAL, HOTLINK). Defaults to NORMAL.

**Returns**:

- list[model_AffiliateLink]: A list of affiliate links.

**Raises**:

- `InvalidArgumentException`: If invalid parameters are provided.
- `InvalidTrackingIdException`: If the tracking ID is missing.
- `ProductsNotFoudException`: If affiliate links are not available.
- `ApiRequestException`: If there is an error during the API request.
- `ApiRequestResponseException`: If there is an error in processing the API response.


#### `get_hotproducts`

**Description**: Searches for affiliated products with high commissions.

**Parameters**:
(Detailed parameters are listed in the method definition within the provided code)

**Returns**:

- model_HotProductsResponse: Contains response information and the list of products.

**Raises**:

- `ProductsNotFoudException`: If no products are found for the given parameters.
- `ApiRequestException`: If there is an error during the API request.
- `ApiRequestResponseException`: If there is an error in processing the API response.



#### `get_categories`

**Description**: Retrieves all available categories (parent and child).

**Returns**:

- list[model_Category | model_ChildCategory]: A list of categories.

**Raises**:

- `CategoriesNotFoudException`: If no categories are found.
- `ApiRequestException`: If there is an error during the API request.
- `ApiRequestResponseException`: If there is an error in processing the API response.



#### `get_parent_categories`

**Description**: Retrieves all parent categories.

**Parameters**:

- `use_cache` (bool, optional): Whether to use cached categories. Defaults to True.

**Returns**:

- list[model_Category]: A list of parent categories.

**Raises**:

- `CategoriesNotFoudException`: If no categories are found.
- `ApiRequestException`: If there is an error during the API request.
- `ApiRequestResponseException`: If there is an error in processing the API response.


#### `get_child_categories`

**Description**: Retrieves child categories for a specific parent category.

**Parameters**:

- `parent_category_id` (int): The ID of the parent category.
- `use_cache` (bool, optional): Whether to use cached categories. Defaults to True.


**Returns**:

- list[model_ChildCategory]: A list of child categories.

**Raises**:

- `CategoriesNotFoudException`: If no categories are found.
- `ApiRequestException`: If there is an error during the API request.
- `ApiRequestResponseException`: If there is an error in processing the API response.