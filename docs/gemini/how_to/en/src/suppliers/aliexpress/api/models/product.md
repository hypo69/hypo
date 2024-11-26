# Usage Guide for `Product` Class in `aliexpress/api/models/product.py`

This document outlines how to use the `Product` class defined in the `aliexpress/api/models/product.py` file.  This class represents product data retrieved from AliExpress API.

## Class Structure

The `Product` class contains various attributes representing different aspects of a product.  These attributes are crucial for extracting and processing the product information.

```python
from typing import List

class Product:
    app_sale_price: str
    app_sale_price_currency: str
    commission_rate: str
    discount: str
    evaluate_rate: str
    first_level_category_id: int
    first_level_category_name: str
    lastest_volume: int
    hot_product_commission_rate: str
    lastest_volume: int  # Duplicate.  Likely a typo; should be renamed
    original_price: str
    original_price_currency: str
    product_detail_url: str
    product_id: int
    product_main_image_url: str
    product_small_image_urls: List[str]
    product_title: str
    product_video_url: str
    promotion_link: str
    relevant_market_commission_rate: str
    sale_price: str
    sale_price_currency: str
    second_level_category_id: int
    second_level_category_name: str
    shop_id: int
    shop_url: str
    target_app_sale_price: str
    target_app_sale_price_currency: str
    target_original_price: str
    target_original_price_currency: str
    target_sale_price: str
    target_sale_price_currency: str
```

**Important Note:** The attribute `lastest_volume` is listed twice.  This is likely a typo; one instance should be removed or renamed.  Please double-check the original data source and adjust the code accordingly.

## How to Use

To use a `Product` object, you first need to instantiate it with the data.  This assumes you have already retrieved the data from the API.

```python
import json

# Example JSON data representing a product
product_data = {
    "app_sale_price": "10.99",
    # ... other attributes
}

# Deserialize the JSON into a dictionary
product_dict = json.loads(json.dumps(product_data))  # Better for handling potential nested types

# Create a Product object
product_object = Product(**product_dict)


# Accessing attributes
print(product_object.product_title)
print(product_object.sale_price)
print(product_object.product_small_image_urls)

#Check for existence of attributes before using them to avoid errors if a field is not present in the API response.  Critical for production code
if hasattr(product_object, 'product_title'):
    print(product_object.product_title)

#Iterating through list of image URLs
if hasattr(product_object, 'product_small_image_urls') and product_object.product_small_image_urls:
    for image_url in product_object.product_small_image_urls:
        print(image_url)

```

This example demonstrates how to create a `Product` object and access its attributes.  Remember to handle potential errors, such as missing or malformed data, to ensure robustness.  Critically, check for the existence of attributes before using them to avoid `AttributeError` exceptions.


## Potential Errors and Best Practices

* **Missing Data:**  The API might not provide all attributes for every product.  Always check if an attribute exists before trying to access it using `hasattr()`.
* **Data Types:** The data types (`str`, `int`, `List`) should be handled carefully. For example, if `sale_price` is intended to be a float, convert it accordingly.
* **Error Handling:** Implement proper error handling to manage potential exceptions (e.g., `json.JSONDecodeError`) during the data parsing process.  Check for invalid data types.

By following these guidelines, you can effectively work with the `Product` class to process product data from AliExpress API. Remember to address the duplicate `lastest_volume` attribute.