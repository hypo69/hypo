## Usage Guide for `hypotez/src/suppliers/aliexpress/api/models/request_parameters.py`

This file defines enums for various parameters used in requests to the AliExpress API.  It's crucial for constructing correct API calls, ensuring compatibility with the AliExpress data structure.

**Classes:**

* **`ProductType`:**  Specifies the type of products to retrieve.

    * **`ALL`:**  Returns all product types.
    * **`PLAZA`:**  Returns products from the PLAZA platform.
    * **`TMALL`:**  Returns products from the TMALL platform.

* **`SortBy`:**  Specifies the criteria for sorting product results.

    * **`SALE_PRICE_ASC`:**  Sorts by sale price in ascending order.
    * **`SALE_PRICE_DESC`:**  Sorts by sale price in descending order.
    * **`LAST_VOLUME_ASC`:**  Sorts by the last volume of sales in ascending order.
    * **`LAST_VOLUME_DESC`:**  Sorts by the last volume of sales in descending order.

* **`LinkType`:**  Specifies the type of link.

    * **`NORMAL`:**  Represents a standard link (value 0).
    * **`HOTLINK`:**  Represents a hotlink (value 2).

**How to use:**

To use these enums in your code, import the module and then use the defined constants.

```python
from hypotez.src.suppliers.aliexpress.api.models.request_parameters import ProductType, SortBy, LinkType

# Example usage:

product_type = ProductType.PLAZA
sort_by = SortBy.SALE_PRICE_DESC
link_type = LinkType.HOTLINK

# Now use these variables in your API request functions to specify product type and sorting criteria:
# ... (your API call code here) ...
```

**Important Considerations:**

* **Case Sensitivity:**  The enum values (`ALL`, `PLAZA`, etc.) are case-sensitive.  Ensure you use the correct casing when assigning or retrieving them.
* **Error Handling:**  Your code should include error handling to check if the provided `ProductType`, `SortBy`, or `LinkType` values are valid.  This prevents unexpected behavior or errors when making API calls.  For instance, checking if the `sort_by` value is one of the defined constants in the `SortBy` enum.
* **API Documentation:** Always refer to the official AliExpress API documentation for the most up-to-date and complete information on parameters and their valid values.  The values defined here might represent a subset of the total allowed parameters in the API.

This usage guide provides a clear understanding of the purpose and use of each enum.  By following these guidelines, you can effectively use these enums to construct correct and reliable API calls to the AliExpress API. Remember to replace the placeholder comments with your actual API call code.