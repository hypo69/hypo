rst
How to use the AliexpressAffiliateFeaturedpromoProductsGetRequest class
=======================================================================

Description
-------------------------
This Python code defines a class `AliexpressAffiliateFeaturedpromoProductsGetRequest` that interacts with an AliExpress API endpoint. It allows you to retrieve featured promotional product information. The class inherits from a `RestApi` base class, likely handling API communication details.  It accepts various parameters to filter and specify the desired data, such as category IDs, countries, and time ranges for promotions.  The class encapsulates the necessary parameters for making a request to the AliExpress affiliate API.

Execution steps
-------------------------
1. **Initialization:** The class constructor (`__init__`) is called to create an instance of `AliexpressAffiliateFeaturedpromoProductsGetRequest`.  It takes optional `domain` and `port` parameters, defaulting to "api-sg.aliexpress.com" and 80 respectively. This establishes the API connection details.


2. **Parameter Setting:**  The instance properties (`app_signature`, `category_id`, `country`, `fields`, `page_no`, `page_size`, `promotion_end_time`, `promotion_name`, `promotion_start_time`, `sort`, `target_currency`, `target_language`, `tracking_id`) are assigned values to control the specifics of the API call. These values determine what data you want to retrieve from the API.


3. **API Endpoint Determination:** The `getapiname` method returns the name of the API endpoint ("aliexpress.affiliate.featuredpromo.products.get"). This step identifies the correct API method to use.


4. **(Implicit) API Request:** The class inherits from `RestApi`, which presumably has methods for making HTTP requests.  Calling methods on this object, outside of what's shown, would trigger the actual API request using the previously set parameters.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.base import RestApi
    # Assuming the import from the rest of the codebase for AliexpressAffiliateFeaturedpromoProductsGetRequest works (likely another file)
    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateFeaturedpromoProductsGetRequest  

    # Create an instance of the class, specifying parameters.
    request = AliexpressAffiliateFeaturedpromoProductsGetRequest(
        domain="api-sg.aliexpress.com",
        # Replace with actual values
        category_id=123,
        country="US",
        promotion_start_time="2023-10-26",
        promotion_end_time="2023-10-27",
        page_no=1,
        page_size=10,
    )

    # Call the method to execute the API request (not shown here because it's implied by inheritance)
    # response = request.execute()  # Placeholder - the actual request is implicit within the RestApi methods
    # ... process the response from the request