rst
How to use the AliexpressAffiliateCategoryGetRequest class
========================================================================================

Description
-------------------------
This Python code defines a class `AliexpressAffiliateCategoryGetRequest` that inherits from the `RestApi` class.  It's designed for making API requests to the AliExpress affiliate platform to retrieve category information. The class handles the necessary setup for interacting with the AliExpress API, including specifying the API endpoint and name.

Execution steps
-------------------------
1. **Import the class:** Import the `AliexpressAffiliateCategoryGetRequest` class from the specified module.

2. **Initialize the class:** Create an instance of the `AliexpressAffiliateCategoryGetRequest` class, optionally providing the domain and port.  The default values are `api-sg.aliexpress.com` for the domain and `80` for the port.

3. **Get the API name:** The `getapiname()` method returns the name of the specific API endpoint to be used for the category retrieval request, which is `aliexpress.affiliate.category.get`. This is crucial for the API request.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateCategoryGetRequest

    # Initialize the request object.  No arguments for default values
    request = AliexpressAffiliateCategoryGetRequest()
    
    # Optionally, initialize with specific domain and port if needed
    # request = AliexpressAffiliateCategoryGetRequest(domain="your-aliexpress-domain", port=443)

    # Get the API endpoint name
    api_name = request.getapiname()
    print(f"API endpoint name: {api_name}")