rst
How to use the `products.py` module
========================================================================================

Description
-------------------------
This module contains functions for processing product data.  Specifically, `parse_product` modifies a single product object, and `parse_products` processes a list of product objects, applying the `parse_product` function to each one.  The core change is to convert the `product_small_image_urls` attribute, which is initially a `BeautifulSoup` object, into a string.

Execution steps
-------------------------
1. **`parse_product(product)` function:**
   - Takes a single `product` object as input.
   - Extracts the value from the `product.product_small_image_urls` attribute, which is expected to be a `BeautifulSoup` object containing the URLs.
   - Converts the `BeautifulSoup` object to a string.
   - Returns the modified `product` object.

2. **`parse_products(products)` function:**
   - Takes a list of `product` objects (`products`) as input.
   - Initializes an empty list `new_products`.
   - Iterates through each `product` in the input `products` list.
   - Calls the `parse_product` function for each product, passing the product object as an argument.
   - Appends the modified `product` object returned by `parse_product` to the `new_products` list.
   - Returns the `new_products` list, which contains the processed product objects.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers.products import parse_product, parse_products
    # Assuming you have a product object (example)
    import bs4
    example_product = type('Product', (), {'product_small_image_urls': bs4.element.Tag(), 'other_details': 'Some details'})
    example_product.product_small_image_urls = bs4.element.Tag(name='a', attrs={'href': 'http://example.com'})

    # Example list of products (use a suitable method to get this)
    example_products = [example_product, example_product]

    # Use parse_product to process a single product
    modified_product = parse_product(example_product)
    print(modified_product.product_small_image_urls)  # Output: <a href="http://example.com">

    # Use parse_products to process the list
    modified_products = parse_products(example_products)
    print(modified_products[0].product_small_image_urls) # Output: <a href="http://example.com">