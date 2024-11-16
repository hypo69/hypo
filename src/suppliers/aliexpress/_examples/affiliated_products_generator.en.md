## \file hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.en.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress._examples """
MODE = 'debug'
Here's the example file for the `affiliated_products_generator.py` module in English. This file demonstrates how to use the `AliAffiliatedProducts` class to gather product data and handle affiliate links.

### Example Usage of `AliAffiliatedProducts`

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Set up the ad campaign parameters
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # You can set this to None if you don't need a category
    language = "EN"  # Language for the campaign
    currency = "USD"  # Currency for the campaign

    # Create an instance of the AliAffiliatedProducts class
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Example product URLs or IDs
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Process the products and get a list of products with affiliate links and saved images
    products = parser.process_affiliate_products(prod_urls)

    # Check the results
    if products:
        print(f"Received {len(products)} affiliate products.")
        for product in products:
            print(f"Product ID: {product.product_id}")
            print(f"Affiliate Link: {product.promotion_link}")
            print(f"Local Image Path: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Local Video Path: {product.local_saved_video}")
            print()
    else:
        print("No affiliate products found.")

if __name__ == "__main__":
    main()
```

### Explanation of the Example

- **Creating an Instance of `AliAffiliatedProducts`**:
  ```python
  parser = AliAffiliatedProducts(
      campaign_name,
      campaign_category,
      language,
      currency
  )
  ```
  Here, we create an `AliAffiliatedProducts` object with the ad campaign parameters.

- **List of Product URLs or IDs**:
  ```python
  prod_urls = [
      '123',
      'https://www.aliexpress.com/item/123.html',
      '456',
      'https://www.aliexpress.com/item/456.html',
  ]
  ```
  This is an example list of product URLs or IDs. You can provide either just the IDs or full URLs.

- **Processing Products**:
  ```python
  products = parser.process_affiliate_products(prod_urls)
  ```
  We call the `process_affiliate_products` method to process the products, retrieve affiliate links, and save images and videos.

- **Checking Results**:
  ```python
  if products:
      print(f"Received {len(products)} affiliate products.")
      for product in products:
          print(f"Product ID: {product.product_id}")
          print(f"Affiliate Link: {product.promotion_link}")
          print(f"Local Image Path: {product.local_saved_image}")
          if product.local_saved_video:
              print(f"Local Video Path: {product.local_saved_video}")
          print()
  else:
      print("No affiliate products found.")
  ```
  We check if there are any processed products and print details about each product.

### Full Example File

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Set up the ad campaign parameters
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # You can set this to None if you don't need a category
    language = "EN"  # Language for the campaign
    currency = "USD"  # Currency for the campaign

    # Create an instance of the AliAffiliatedProducts class
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Example product URLs or IDs
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Process the products and get a list of products with affiliate links and saved images
    products = parser.process_affiliate_products(prod_urls)

    # Check the results
    if products:
        print(f"Received {len(products)} affiliate products.")
        for product in products:
            print(f"Product ID: {product.product_id}")
            print(f"Affiliate Link: {product.promotion_link}")
            print(f"Local Image Path: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Local Video Path: {product.local_saved_video}")
            print()
    else:
        print("No affiliate products found.")

if __name__ == "__main__":
    main()
```

This file can be used as a template for testing the functionality of the `AliAffiliatedProducts` class and its methods. You can adapt it to fit your specific needs and add more functionality as required.