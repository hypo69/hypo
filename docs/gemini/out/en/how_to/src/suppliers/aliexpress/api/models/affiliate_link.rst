How to use the `AffiliateLink` class
========================================================================================

Description
-------------------------
The `AffiliateLink` class defines a data structure for storing affiliate link information.  It contains attributes for the promotion link (`promotion_link`) and the source value (`source_value`). This class likely represents a model for storing data related to affiliate links from AliExpress.


Execution steps
-------------------------
1. **Define an `AffiliateLink` object:**  Create an instance of the `AffiliateLink` class, providing values for the `promotion_link` and `source_value` attributes.

2. **Access attributes:** Retrieve the values of the `promotion_link` and `source_value` attributes of the `AffiliateLink` object as needed.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink

    # Create an AffiliateLink object
    affiliate_link = AffiliateLink(
        promotion_link="https://example.com/affiliate/link1",
        source_value="Direct Listing",
    )

    # Access the attributes
    promotion_link = affiliate_link.promotion_link
    source_value = affiliate_link.source_value

    print(f"Promotion Link: {promotion_link}")
    print(f"Source Value: {source_value}")