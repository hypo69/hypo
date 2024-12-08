rst
How to use the AliexpressAffiliateHotproductDownloadRequest class
========================================================================================

Description
-------------------------
This Python code defines a class `AliexpressAffiliateHotproductDownloadRequest` that inherits from a `RestApi` class.  It's designed to make a request to the AliExpress affiliate API endpoint to download hot product data.  The class initializes with various parameters that can be specified to filter and shape the downloaded data (e.g., category, country, fields, etc.). The `getapiname` method returns the API endpoint name.

Execution steps
-------------------------
1. **Initialization:**  The class is initialized with a `domain` (defaulting to "api-sg.aliexpress.com") and `port` (defaulting to 80).  This initializes the underlying RestApi object.

2. **Parameter Setting:**  The class allows setting various parameters to refine the API request, including:
    * `app_signature`:  An application signature, likely for authentication.
    * `category_id`:  To filter by a specific category ID.
    * `country`:  To filter by a specific country.
    * `fields`:  To specify which fields to retrieve in the response.
    * `scenario_language_site`:  For setting language and site details.
    * `page_no`: Page number for pagination.
    * `page_size`: Page size for pagination.
    * `target_currency`: Target currency for the response.
    * `target_language`: Target language for the response.
    * `tracking_id`: A tracking identifier.

3. **API Endpoint Determination:** The `getapiname` method provides the name of the API endpoint that will be used, in this case, `aliexpress.affiliate.hotproduct.download`.

4. **(Implicit) API Call:**  This class is part of a larger system; it's likely that an instantiation of this class, with appropriate parameters set, would ultimately be used to call the AliExpress API, but the actual API call is not explicitly shown within this class definition.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateHotproductDownloadRequest

    # Create an instance of the request class, setting parameters
    request = AliexpressAffiliateHotproductDownloadRequest(
        domain="my-custom-domain",  # Override default domain.
        app_signature="your_app_signature",
        category_id=123,
        country="US",
        fields=["product_name", "price"],
        page_no=1,
        page_size=10
    )

    # Get the API endpoint name.
    api_endpoint_name = request.getapiname()
    print(f"API Endpoint Name: {api_endpoint_name}")

    # Note: Further code would be needed to actually make the API call using the 'request' object.  This example shows how to set parameters.