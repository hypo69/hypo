rst
How to use the aliexpress API helpers
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/suppliers/aliexpress/api/helpers/__init__.py`) provides helper functions for interacting with the AliExpress API.  It encapsulates common tasks, like making API requests, parsing product data, handling arguments, and filtering categories.

Execution steps
-------------------------
1. **Import necessary functions:** The module exports several functions, making them available for use in other parts of your project.  To use the functions, import them from the `hypotez.src.suppliers.aliexpress.api.helpers` module.  Import example: `from hypotez.src.suppliers.aliexpress.api.helpers import api_request, get_product_ids, parse_products`.

2. **Use `api_request` for API calls:** The `api_request` function facilitates making requests to the AliExpress API. It likely handles parameters, headers, and potential errors. You'll provide the necessary API endpoint, parameters, and headers.

3. **Process arguments using `get_list_as_string` or `get_product_ids`:** The `get_list_as_string` function is likely used to convert a list of items (e.g., product IDs) into a string format compatible with the API. `get_product_ids` function is designed to validate and potentially filter product IDs.

4. **Use `parse_products` to interpret API responses:** This function takes the response from the API and extracts the product information. It likely transforms the raw data into a structured format (e.g., a list of dictionaries representing products).

5. **Filter categories using `filter_parent_categories` or `filter_child_categories`:**  These functions allow you to selectively choose specific categories based on parent or child relationships within the AliExpress category structure.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers import api_request, get_product_ids, parse_products

    # Example usage (replace with your actual values):
    product_ids = [123, 456, 789]
    product_ids_string = get_product_ids(product_ids)  #Converts the product IDs list to a string

    headers = {"X-API-Key": "your_api_key"} # Replace with your key
    url = "https://aliexpress-api.com/products" # Replace with the appropriate URL


    try:
        response = api_request(url, method='GET', params={"product_ids": product_ids_string}, headers=headers)
        parsed_products = parse_products(response.json())
        # Print parsed products.  
        # Note that the specific format of parsed_products depends on the implementation of parse_products.
        for product in parsed_products:
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")