rst
How to use the hypotez/src/suppliers/aliexpress/api/models/__init__.py module
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/suppliers/aliexpress/api/models/__init__.py`) provides access to various data models used for interacting with the AliExpress API.  It imports classes from different modules within the same directory, exposing objects like languages, currencies, product types, sorting options, affiliate links, hot product responses, products, and categories.

Execution steps
-------------------------
1. **Import necessary models:** The module imports various models from other files within the `hypotez/src/suppliers/aliexpress/api/models` directory. This step is implicitly performed when you import the `__init__.py` file.  You'll then have access to these models in your codebase.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models import (
        Language,
        Currency,
        ProductType,
        SortBy,
        LinkType,
        AffiliateLink,
        HotProductsResponse,
        Product,
        Category,
        ChildCategory
    )

    # Example usage: Get a list of available languages.
    # Note: You would typically get this information from a separate API call.
    available_languages = [lang for lang in Language.get_all_languages() ]
    print(f"Available Languages: {available_languages}")


    # Example usage (Illustrative - actual API interaction would require a call):
    # Assuming you've got an 'aliexpress_client' that can query product data.
    response = aliexpress_client.get_hot_products(product_type=ProductType.ELECTRONICS, sort_by=SortBy.NEWEST)
    hot_products = response.products

    # Example usage - Accessing a product in the response
    if hot_products and hot_products[0]:
        product = hot_products[0]
        print(f"Product Title: {product.title}")
        print(f"Product Price: {product.price}")