rst
How to use the AliexpressAffiliateHotproductQueryRequest class
=================================================================

Description
-------------------------
This Python code defines a class `AliexpressAffiliateHotproductQueryRequest` that inherits from the `RestApi` class.  This class is designed to send a request to the AliExpress Affiliate API to query hot products.  It allows setting various parameters to refine the query, such as category IDs, price ranges, keywords, and more.

Execution steps
-------------------------
1. **Initialization:** The class is initialized with a `domain` (defaulting to "api-sg.aliexpress.com") and a `port` (defaulting to 80).  This establishes the connection point for the API request.


2. **Parameter Setting:**  The class provides numerous attributes (`app_signature`, `category_ids`, `delivery_days`, `fields`, `keywords`, etc.) that can be set to customize the query. Setting these attributes defines the criteria for the hot product search.  


3. **API Name Retrieval:** The `getapiname` method returns the specific API endpoint name for the AliExpress Affiliate Hot Product Query: "aliexpress.affiliate.hotproduct.query."


4. **Making the Request:**  (Not explicitly shown in this snippet)  The `RestApi` parent class, likely implementing the actual API call logic, would utilize the parameters (set in steps 1 and 2) to craft and send the request to the AliExpress Affiliate API endpoint returned by `getapiname`.  The response from the API would be processed by the `RestApi` class.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.base import RestApi  # Assuming this is in the same directory
    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateHotproductQueryRequest


    # Create an instance of the request class, setting some parameters
    request = AliexpressAffiliateHotproductQueryRequest()
    request.keywords = "dress"
    request.category_ids = [1234, 5678]
    request.min_sale_price = 10
    request.max_sale_price = 50

    # Example usage (crucial to have the RestApi class correctly implemented):
    #  (Note: This part is missing from the snippet.)
    # response = request.request()  #This assumes the request method exists in RestApi
    # print(response)  # Process and print the response

    # Now you can access the response data and process it as needed.