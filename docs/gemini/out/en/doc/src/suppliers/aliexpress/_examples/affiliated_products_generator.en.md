# `aliexpress.affiliated_products_generator` Module Documentation

## Overview

This module provides functionality for generating affiliate product data from AliExpress. It allows users to specify ad campaign parameters and a list of product URLs or IDs to retrieve affiliate links, and optionally save associated images and videos.

## Classes

### `AliAffiliatedProducts`

**Description**: This class handles the process of fetching affiliate product data from AliExpress, including affiliate links and image/video saving.

**Methods**:

#### `process_affiliate_products(prod_urls)`

**Description**: Processes a list of product URLs or IDs, retrieving affiliate links, and optionally saving associated images and videos.

**Parameters**:

- `prod_urls` (list): A list of product URLs or IDs (strings).

**Returns**:

- list: A list of `Product` objects containing the affiliate product data. Returns an empty list if no products are found or if there's an error during processing.

**Raises**:

- `APIError`: If there's an error communicating with the AliExpress API.
- `InvalidInputError`: If the input `prod_urls` is invalid (e.g., empty, contains invalid URLs).
- `ImageDownloadError`: If there's an error downloading images.
- `VideoDownloadError`: If there's an error downloading videos.


## Functions

(No functions are present in the provided code snippet)


## Example Usage (from `example_usage.py`)

```python
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # ... (campaign parameters are set) ...

    # Example product URLs or IDs
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)
    products = parser.process_affiliate_products(prod_urls)

    if products:
        print(f"Received {len(products)} affiliate products.")
        for product in products:
            print(f"Product ID: {product.product_id}")
            print(f"Affiliate Link: {product.promotion_link}")
            print(f"Local Image Path: {product.local_image_path}")
            if product.local_video_path:
                print(f"Local Video Path: {product.local_video_path}")
            print()
    else:
        print("No affiliate products found.")

if __name__ == "__main__":
    main()
```


**Note**: This documentation assumes the existence of a `Product` class, which is not defined in the provided code snippet.  Complete documentation would require the definition of that class and any other necessary classes/functions.  The example demonStartes how to use `AliAffiliatedProducts` and interact with the returned `Product` objects.