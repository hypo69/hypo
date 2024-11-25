# Affiliated Products Generator

## Overview

This module provides functionality for generating affiliated product links from AliExpress. It uses a `AliAffiliatedProducts` class to process product URLs or IDs, returning a list of products with affiliated promotion links and optionally local image and video paths.


## Classes

### `AliAffiliatedProducts`

**Description**: This class handles the generation of affiliate links for products from AliExpress. It takes campaign details and a list of product URLs or IDs as input, and returns a list of product objects containing the affiliate links and other relevant information.

**Methods**:

- `process_affiliate_products(prod_urls)`:
    **Description**: This method processes a list of product URLs or IDs, retrieves affiliate links for each product, and returns a list of `Product` objects containing the generated affiliate links and other information. If no affiliate link is found or there's an error during the process, relevant error information will be recorded.

    **Parameters**:
    - `prod_urls` (list): A list of product URLs or IDs from AliExpress.

    **Returns**:
    - list: A list of `Product` objects, each containing affiliate information. Returns an empty list if no affiliate links are generated or if an error occurs during the process.



## Functions

### `main`

**Description**: This function demonstrates the usage of the `AliAffiliatedProducts` class. It sets campaign parameters, creates an instance of the class, processes a list of product URLs, and prints the results.

**Parameters**:
- None

**Returns**:
- None


**Example Usage (in `main`):**


```python
campaign_name = "summer_sale_2024"
campaign_category = "electronics"  
language = "EN"
currency = "USD"

parser = AliAffiliatedProducts(
    campaign_name,
    campaign_category,
    language,
    currency
)

prod_urls = [
    '123',
    'https://www.aliexpress.com/item/123.html',
    '456',
    'https://www.aliexpress.com/item/456.html',
]

products = parser.process_affiliate_products(prod_urls)

if products:
    print(f"Получено {len(products)} аффилированных продуктов.")
    for product in products:
        print(f"Продукт ID: {product.product_id}")
        print(f"Аффилированная ссылка: {product.promotion_link}")
        print(f"Локальный путь к изображению: {product.local_saved_image}")
        if product.local_saved_video:
            print(f"Локальный путь к видео: {product.local_saved_video}")
        print()
else:
    print("Не удалось получить аффилированные продукты.")

```


```
```
```
```
```


```
```

```
```


```
```
```

```
```

```
```
```
```


```
```


```
```


```
```

```
```
```
```

```
```