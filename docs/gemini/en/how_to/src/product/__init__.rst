rst
How to use the `hypotez/src/product/__init__.py` module
=========================================================================================

Description
-------------------------
This module (`hypotez/src/product/__init__.py`) serves as an initial entry point for accessing components related to products. It imports necessary classes and functions from submodules within the `product` package, providing a way to utilize the `Product`, `ProductFields`, and `translate_presta_fields_dict` functionality.  It also defines a global `MODE` variable.

Execution steps
-------------------------
1. Imports the `Product` class from the `.product` module.
2. Imports the `ProductFields` class from the `.product_fields.product_fields` module.
3. Imports the `translate_presta_fields_dict` function from `.product_fields.product_fields_translator`.
4. Sets the global variable `MODE` to the string 'dev'.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.product import Product, ProductFields, translate_presta_fields_dict

    # Example usage (assuming you have initialized a Product instance):
    my_product = Product(...)  # Replace with appropriate initialization code

    # Access product fields using ProductFields
    product_fields = ProductFields(my_product.presta_product_id)

    # Translate multilingual fields
    translated_fields = translate_presta_fields_dict(product_fields, target_lang='en')


    # Access the translated fields
    print(translated_fields)