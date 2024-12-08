rst
How to use the PrestaProduct class
========================================================================================

Description
-------------------------
This code defines a `PrestaProduct` class that interacts with a PrestaShop API.  It inherits from the `PrestaShop` base class and provides methods for checking product availability, performing advanced searches, and retrieving product information. The class handles authentication parameters and raises a `ValueError` if necessary authentication information is missing.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports essential modules like `SimpleNamespace`, `Optional`, `header`, `logger`, `pprint`, and `PrestaShop` for the required functionality.
2. **Define the `PrestaProduct` class:** This class inherits from the `PrestaShop` class, which likely handles the API interaction specifics.
3. **`__init__` method:** Initializes the `PrestaProduct` object. It takes optional credentials as a dictionary or `SimpleNamespace` object for authentication parameters.  It validates that `api_domain` and `api_key` are provided, either from the `credentials` or directly as parameters. If not present, it raises a `ValueError`.
4. **`check` method:** (Documented in the class) Checks if a product exists in the database based on the provided `product_reference`. It interacts with the PrestaShop API to retrieve the product data.
5. **`search` method:** (Documented in the class) Performs a search within the PrestaShop database based on the provided `filter` and `value`. It queries the API for matching products.
6. **`get` method:** (Documented in the class) Retrieves information about a product based on its `id_product`. This method will likely interact with the PrestaShop API to retrieve the product details.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.product import PrestaProduct
    import simplejson as json

    # Example credentials (replace with your actual credentials)
    credentials = {
        'api_domain': 'your_api_domain',
        'api_key': 'your_api_key'
    }
    
    try:
        product_api = PrestaProduct(credentials=credentials)
        
        # Check for a product by its reference
        product_data = product_api.check(product_reference='your_product_reference')
        if product_data:
            print("Product found:")
            pprint(json.dumps(product_data, indent=4, ensure_ascii=False))
        else:
            print("Product not found.")
            
        # Example of a search (replace with your filter and value)
        search_results = product_api.search(filter='name', value='dress')
        print("Search results:")
        pprint(json.dumps(search_results, indent=4, ensure_ascii=False))

        # Get a product by its ID
        product_info = product_api.get(id_product=123)
        print("Product info:")
        pprint(json.dumps(product_info, indent=4, ensure_ascii=False))
    except ValueError as e:
        print(f"Error: {e}")