# aliexpress/api.py

## Overview

This module provides a Python wrapper for the AliExpress Open Platform API. It allows easier access to product information and affiliate links.

## Table of Contents

* [AliexpressApi](#aliexpressapi)
    * [retrieve_product_details](#retrieve_product_details)
    * [get_affiliate_links](#get_affiliate_links)
    * [get_hotproducts](#get_hotproducts)
    * [get_categories](#get_categories)
    * [get_parent_categories](#get_parent_categories)
    * [get_child_categories](#get_child_categories)


## Classes

### `AliexpressApi`

**Description**:  Provides methods to interact with the AliExpress API using your API credentials.

**Constructor**:

```python
def __init__(self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs):
    """
    Args:
        key (str): Your API key.
        secret (str): Your API secret.
        language (model_Language): Language code.
        currency (model_Currency): Currency code.
        tracking_id (str, optional): The tracking ID for link generator. Defaults to None.
        app_signature (str, optional): App signature. Defaults to None.
    """
```

**Methods**:

#### `retrieve_product_details`

```python
def retrieve_product_details(self,
    product_ids: str | list,
    fields: str | list = None,
    country: str = None,
    **kwargs) -> List[model_Product]:
    """ Get products information.

    Args:
        product_ids (str | list[str]): One or more links or product IDs.
        fields (str | list[str], optional): The fields to include in the results. Defaults to all.
        country (str, optional): Filter products that can be sent to that country. Returns the price
            according to the country's tax rate policy.

    Returns:
        list[model_Product]: A list of products.

    Raises:
        ProductsNotFoudException: If no products are found.
        InvalidArgumentException: For invalid input parameters.
        ApiRequestException: For errors during API request.
        ApiRequestResponseException: For errors in the API response.
    """
```

#### `get_affiliate_links`

```python
def get_affiliate_links(self,
    links: str | list,
    link_type: model_LinkType = model_LinkType.NORMAL,
    **kwargs) -> List[model_AffiliateLink]:
    """ Converts a list of links in affiliate links.
    Args:
        links (str | list[str]): One or more links to convert.
        link_type (model_LinkType, optional): Choose between normal link with standard commission
            or hot link with hot product commission. Defaults to NORMAL.

    Returns:
        list[model_AffiliateLink]: A list containing the affiliate links.

    Raises:
        InvalidArgumentException: For invalid input parameters.
        InvalidTrackingIdException: If the tracking ID is missing.
        ProductsNotFoudException: If no products are found.
        ApiRequestException: For errors during API request.
        ApiRequestResponseException: For errors in the API response.
    """
```

#### `get_hotproducts`

```python
def get_hotproducts(self,
    category_ids: str | list = None,
    delivery_days: int = None,
    fields: str | list = None,
    keywords: str = None,
    max_sale_price: int = None,
    min_sale_price: int = None,
    page_no: int = None,
    page_size: int = None,
    platform_product_type: model_ProductType = None,
    ship_to_country: str = None,
    sort: model_SortBy = None,
    **kwargs) -> model_HotProductsResponse:
    """Search for affiliated products with high commission.

    Args:
        See method signature.

    Returns:
        model_HotProductsResponse: Contains response information and the list of products.


    Raises:
        ProductsNotFoudException: If no products are found.
        ApiRequestException: For errors during API request.
        ApiRequestResponseException: For errors in the API response.
    """
```

#### `get_categories`

```python
def get_categories(self, **kwargs) -> List[model_Category | model_ChildCategory]:
    """Get all available categories, both parent and child.

    Returns:
        list[model_Category | model_ChildCategory]: A list of categories.

    Raises:
        CategoriesNotFoudException: If no categories are found.
        ApiRequestException: For errors during API request.
        ApiRequestResponseException: For errors in the API response.
    """
```

#### `get_parent_categories`

```python
def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
    """Get all available parent categories.

    Args:
        use_cache (bool): Uses cached categories to reduce API requests.

    Returns:
        list[model_Category]: A list of parent categories.

    Raises:
        CategoriesNotFoudException: If no categories are found.
        ApiRequestException: For errors during API request.
        ApiRequestResponseException: For errors in the API response.
    """
```

#### `get_child_categories`

```python
def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
    """Get all available child categories for a specific parent category.

    Args:
        parent_category_id (int): The parent category id.
        use_cache (bool, optional): Uses cached categories to reduce API requests. Defaults to True.

    Returns:
        list[model_ChildCategory]: A list of child categories.

    Raises:
        CategoriesNotFoudException: If no categories are found.
        ApiRequestException: For errors during API request.
        ApiRequestResponseException: For errors in the API response.
    """
```