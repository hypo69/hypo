rst
How to use the AliexpressAffiliateLinkGenerateRequest class
========================================================================================

Description
-------------------------
This Python code defines a class `AliexpressAffiliateLinkGenerateRequest` which inherits from the `RestApi` class. This class is designed to generate affiliate links on AliExpress using the AliExpress API. It allows setting parameters like the application signature, promotion link type, source values, and tracking ID.  Critically, it defines the API endpoint name.

Execution steps
-------------------------
1. **Initialization:** The `__init__` method initializes the `RestApi` object with the domain ("api-sg.aliexpress.com") and port (80).  It also initializes internal variables (`app_signature`, `promotion_link_type`, `source_values`, `tracking_id`) to `None`.

2. **API Endpoint Definition:** The `getapiname` method returns the specific API endpoint name required for the AliExpress affiliate link generation, which is `"aliexpress.affiliate.link.generate"`. This is crucial for communicating with the AliExpress API.

3. **Parameter Setting:** The class attributes (`app_signature`, `promotion_link_type`, `source_values`, `tracking_id`) allow you to set parameters for the affiliate link generation request.  You would set these before invoking the actual API call.

4. **API Call (Implicit):**  This class is part of a larger API framework (`RestApi`).  To actually use this API call, you'd need to invoke methods from the base `RestApi` class (inherited by `AliexpressAffiliateLinkGenerateRequest`). These methods would handle the actual API communication.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.base import RestApi # Assuming this is the correct import path
    from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateLinkGenerateRequest

    # Instantiate the request object, supplying the necessary information
    request = AliexpressAffiliateLinkGenerateRequest()

    # Set parameters (replace with your actual values)
    request.app_signature = "YOUR_APPLICATION_SIGNATURE"
    request.promotion_link_type = "YOUR_PROMOTION_LINK_TYPE"
    request.source_values = "YOUR_SOURCE_VALUES"
    request.tracking_id = "YOUR_TRACKING_ID"


    # Now, you would typically use a method from RestApi
    # to make the actual API call, such as 'execute'.
    #  Example (assuming RestApi has an execute method):
    # response = request.execute() # This is where the API call is performed.
    # print(response)  # Process the API response

    #  Important:  The provided example does not demonstrate how to handle
    # the actual API call, since the complete `RestApi` implementation is missing.