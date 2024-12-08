rst
How to use the request parameters enums
========================================================================================

Description
-------------------------
This code defines three Python classes: `ProductType`, `SortBy`, and `LinkType`.  Each class contains constants representing different values used in filtering and sorting product information from the AliExpress API.

Execution steps
-------------------------
1. **Define Constants:** The code defines a series of named constants (e.g., `ProductType.ALL`, `SortBy.SALE_PRICE_ASC`) within their respective classes. These constants represent different product types, sorting options, and link types.  This improves code readability and maintainability over using raw strings directly.

2. **Create Instances:**  You can use these classes to create specific values for the parameters needed when making calls to the AliExpress API.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.request_parameters import ProductType, SortBy, LinkType

    # Example usage:
    product_type = ProductType.PLAZA
    sort_by = SortBy.SALE_PRICE_DESC
    link_type = LinkType.NORMAL

    # Now you can use these values in your API calls. For example, you might pass them to a function to construct the API request:
    def make_aliexpress_request(product_type, sort_by, link_type):
        # ... (Implementation to construct and send the request using product_type, sort_by, and link_type)
        print(f"Requesting {product_type} products, sorted by {sort_by}, link type: {link_type}")
        # Example to demonstrate the use of the parameters
        return {"product_type": product_type, "sort_by": sort_by, "link_type": link_type}

    request_data = make_aliexpress_request(product_type, sort_by, link_type)
    print(request_data)