rst
How to use the AliexpressAffiliateProductdetailGetRequest class
=================================================================

Description
-------------------------
This Python code defines a class `AliexpressAffiliateProductdetailGetRequest` that inherits from a `RestApi` class.  It's designed to make a REST API call to AliExpress for affiliate product detail information.  The class initializes parameters for the API request, like the application signature, country, specific product fields, product IDs, target currency, language, and tracking ID.  Crucially, it defines the API endpoint name for the request.

Execution steps
-------------------------
1. **Initialization:** The `__init__` method of the class initializes the `RestApi` parent class with the API domain (`api-sg.aliexpress.com`) and port (80). It also initializes several attributes to store parameters for the AliExpress product detail request.  These parameters will be set later by the user when they use the class.

2. **API Endpoint Definition:** The `getapiname` method returns the name of the AliExpress API endpoint to be used for the product detail request (`aliexpress.affiliate.productdetail.get`). This string is vital for directing the request to the correct API.

3. **Parameter Setting (by the user):** The class defines attributes for various parameters that will need to be passed when the class instance is used.  The user must set these attributes before making the request.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.base import RestApi # Correct import path assumed
    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateProductdetailGetRequest

    # Create an instance of the class
    request = AliexpressAffiliateProductdetailGetRequest()

    # Set the parameters for the request
    request.app_signature = "your_app_signature"
    request.country = "US"
    request.product_ids = ["12345", "67890"]  # List of product IDs
    request.target_currency = "USD"
    request.target_language = "en"
    request.tracking_id = "unique_tracking_id"


    #  (Crucial) Now, you would typically use the 'request' object with the RestApi methods to send the request.
    #   The complete code and correct usage example is outside the scope of the provided code snippet.


    # Example of getting the API name (for verification)
    api_name = request.getapiname()
    print(f"API Name: {api_name}")