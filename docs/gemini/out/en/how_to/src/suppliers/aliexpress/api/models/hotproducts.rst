rst
How to use the HotProductsResponse class
========================================================================================

Description
-------------------------
This code defines a Python class named `HotProductsResponse`.  This class represents the structure of a response from an API endpoint that retrieves hot products (likely from AliExpress).  It stores information about the current page, the number of records on that page, the total number of records, and a list of `Product` objects.

Execution steps
-------------------------
1. The class `HotProductsResponse` is defined.
2. It includes attributes to store data related to the API response. These attributes are:
    - `current_page_no`: An integer representing the current page number being retrieved.
    - `current_record_count`: An integer representing the number of products on the current page.
    - `total_record_count`: An integer representing the total number of products in the dataset.
    - `products`: A list of `Product` objects.  Each `Product` object likely represents a single product. The `Product` class is presumed to be defined elsewhere (e.g., in a separate file).

3. The class is designed to encapsulate the structured data that might be returned from an external API, making it suitable for handling the results of API calls.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.hotproducts import HotProductsResponse
    from hypotez.src.suppliers.aliexpress.api.models.product import Product  # Assuming Product is defined

    # Example data (replace with actual data from API call)
    product1 = Product(id=1, name="Product A", price=10.99)
    product2 = Product(id=2, name="Product B", price=25.50)
    products_list = [product1, product2]

    response = HotProductsResponse(
        current_page_no=1,
        current_record_count=2,
        total_record_count=10,
        products=products_list
    )

    print(response.current_page_no)  # Output: 1
    print(response.total_record_count) # Output: 10
    print(response.products[0].name) # Output: Product A