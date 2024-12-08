rst
How to use the `retrieve_product_details_as_dict` method
=========================================================================================

Description
-------------------------
This method retrieves product details from AliExpress for a given list of product IDs.  It sends a request to the AliExpress API, receives the data, and converts the result from a list of `SimpleNamespace` objects to a list of dictionaries.  This conversion is crucial for easier data manipulation and use within the application.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the required modules for API interaction, data manipulation, and logging.

2. **Create an `AliApi` instance:** An instance of the `AliApi` class is initialized, likely with necessary parameters like language and currency.

3. **Define a list of product IDs:** A list named `product_ids` containing the IDs of the products whose details are to be retrieved is created.

4. **Call `retrieve_product_details_as_dict`:** The `retrieve_product_details_as_dict` method is called with the `product_ids` list as input.  This method internally uses `retrieve_product_details` to communicate with the AliExpress API and receive product details.

5. **Convert to dictionary format:** The returned data from the `retrieve_product_details` method is a list of `SimpleNamespace` objects.  The code iterates through this list and converts each `SimpleNamespace` object into a dictionary using the `vars()` function.

6. **Return the list of dictionaries:** The method returns the list of dictionaries containing the product details.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.aliapi import AliApi
    from types import SimpleNamespace

    # Sample product IDs (replace with actual IDs)
    product_ids = [12345, 67890, 11111]

    # Initialize AliApi instance (replace with your initialization)
    api = AliApi(language='en', currency='usd')

    try:
        # Retrieve product details as dictionaries
        product_details = api.retrieve_product_details_as_dict(product_ids)

        if product_details:
            for product in product_details:
                print(product)  # Print each product's details
        else:
            print("No product details retrieved.")
    except Exception as e:
        print(f"Error retrieving product details: {e}")