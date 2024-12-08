rst
How to use the AliexpressApi class
========================================================================================

Description
-------------------------
This code defines the `AliexpressApi` class, a Python wrapper for the AliExpress Open Platform API.  It provides methods for retrieving product details, generating affiliate links, finding hot products, and fetching categories.  The class handles API requests, parsing responses, and integrates with various helper functions for data manipulation.


Execution steps
-------------------------
1. **Import necessary modules**: Import the required modules from the specified locations, including models, helper functions, and error handling classes.


2. **Instantiate the `AliexpressApi` object**: Create an instance of the `AliexpressApi` class, passing in your API key, secret, language, currency, tracking ID (if needed), and any other required parameters.


3. **Choose a method to execute**: Select the desired method for interaction with the API, such as `retrieve_product_details`, `get_affiliate_links`, `get_hotproducts`, `get_categories`, `get_parent_categories`, or `get_child_categories`.


4. **Prepare the input arguments**: Provide the necessary parameters for the selected method (e.g., product IDs, links, category IDs, etc.) according to the method's documentation.  Pay close attention to the data types expected (strings, lists, integers, enums) and the format required.  Note that some input parameters use specific types for better code clarity (e.g., `model_Language` from the provided `models` module).


5. **Execute the chosen method**: Call the chosen method, providing the input parameters.


6. **Process the returned data**: The method will return the results of the API call in a specific format (e.g., a list of `model_Product` objects). The code handles potential errors during API calls and provides logging for error messages.


7. **Handle potential errors**: The provided code includes exception handling (`try...except` blocks) to catch and log potential errors during API requests, preventing your application from crashing. Review error handling in the provided methods for specific exceptions.


8. **Iterate or use data**: Process the returned data as needed for your application's logic.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api import AliexpressApi
    from hypotez.src.suppliers.aliexpress.api.models import model_Language, model_Currency, model_LinkType

    # Replace with your actual API key and secret
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    # Initialize the AliExpress API object
    aliexpress_api = AliexpressApi(
        key=api_key,
        secret=api_secret,
        language=model_Language.EN,
        currency=model_Currency.USD,
        tracking_id="YOUR_TRACKING_ID"  # Required for affiliate links
    )

    # Example: Retrieving product details
    product_ids = ["12345", "67890"]
    try:
        products = aliexpress_api.retrieve_product_details(product_ids=product_ids)
        for product in products:
            pprint(product.title)  # Print the title of each product
    except Exception as e:
        print(f"Error retrieving product details: {e}")

    # Example: Generating affiliate links
    links = ["https://www.aliexpress.com/item/12345.html"]
    try:
        affiliate_links = aliexpress_api.get_affiliate_links(links=links)
        for link in affiliate_links:
            print(link.affiliate_link) # Example accessing affiliate link
    except Exception as e:
        print(f"Error generating affiliate links: {e}")