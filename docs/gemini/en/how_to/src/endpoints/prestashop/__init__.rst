rst
How to use the prestashop module
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/endpoints/prestashop/__init__.py`) provides access to various PrestaShop APIs.  It imports and exposes classes for interacting with PrestaShop entities like products, suppliers, categories, warehouses, languages, shops, price lists, and customers.  The module initializes a 'MODE' variable to 'dev' potentially signifying the environment.

Execution steps
-------------------------
1. The module initializes a global variable `MODE` to the string 'dev'. This likely represents the operational mode for the PrestaShop interactions (e.g., development, staging, production).

2. The module imports specific classes from submodules within the `prestashop` package: `PrestaShop`, `PrestaProduct`, `PrestaSupplier`, `PrestaCategory`, `PrestaWarehouse`, `PrestaLanguage`, `PrestaShopShop`, `PriceListRequester`, and `PrestaCustomer`. These are likely classes for interacting with the corresponding PrestaShop resources.

3. The module makes these imported classes available for use in other parts of the application.  This allows modules in the system to access and utilize functions defined in the respective classes for interacting with PrestaShop data.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop import PrestaProduct

    # Example usage to fetch product details
    try:
        product_details = PrestaProduct.get_product(product_id=123)
        print(product_details)
    except Exception as e:
        print(f"Error fetching product details: {e}")


    # Example usage to create a product (replace with appropriate data)
    try:
        new_product_data = {
            'name': 'Example Product',
            'description': 'Example Product Description'
        }
        created_product = PrestaProduct.create_product(new_product_data)
        print(f"Product created: {created_product}")
    except Exception as e:
        print(f"Error creating product: {e}")