# Usage Guide for AliexpressAffiliateHotproductQueryRequest

This guide explains how to use the `AliexpressAffiliateHotproductQueryRequest` class to query hot products on AliExpress.  This class is part of the `aliexpress` API, specifically for affiliate marketing.

**File:** `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py`

**Class:** `AliexpressAffiliateHotproductQueryRequest`

**Purpose:**  Retrieves hot product information from AliExpress.  This is likely for use in affiliate marketing applications, allowing you to display trending products to users.


**How to Use:**

1. **Import the Class:**

```python
from hypotez.src.suppliers.aliexpress.api._examples.rest import AliexpressAffiliateHotproductQueryRequest
```

2. **Initialize the Request Object:**

   This creates an instance of the `AliexpressAffiliateHotproductQueryRequest` class.  You can optionally specify the domain and port (often not needed unless you're using a custom server).

```python
request = AliexpressAffiliateHotproductQueryRequest()
# or, for a different domain:
request = AliexpressAffiliateHotproductQueryRequest(domain="custom-api.aliexpress.com")
```


3. **Set Query Parameters:**

   Populate the various attributes to refine your search for hot products.  These parameters allow you to filter and order the results.


```python
request.app_signature = "YOUR_APP_SIGNATURE" #  **CRITICAL**: Replace with your actual signature
request.category_ids = [123, 456]  # Filter by category IDs
request.keywords = "winter jacket" #Search by keywords
request.max_sale_price = 50.00
request.min_sale_price = 10.00
request.page_no = 1
request.page_size = 20
# ... (set other parameters as needed)
```

**Important Parameter Descriptions:**

*   `app_signature`:  Your application signature.  **This is crucial and must be provided.**
*   `category_ids`:  Filter by category IDs (list).
*   `keywords`:  Search using keywords.
*   `max_sale_price`, `min_sale_price`: Price range filter.
*   `page_no`, `page_size`:  Pagination.

4. **Call the `getData()` Method:**

   This method sends the request to the AliExpress API and returns the retrieved data.

```python
response = request.getData()
```

5. **Process the Response:**

   The `response` object contains the data returned by the API.  The exact format and structure will depend on the API's response.  You need to handle the response according to the API documentation to extract the relevant product information.

```python
# Example of accessing results (assuming a structured response):
if response.err_msg:
   print(f"Error: {response.err_msg}")
else:
    for product in response.get_product_list(): # Assume get_product_list exists
        print(product.title)
        print(product.price)
```

**Error Handling:**

The `response` object also contains error information (`err_msg`) that should be checked before proceeding. This crucial step prevents unexpected behavior.

**Further Considerations:**

* **API Documentation:** Consult the official AliExpress API documentation to understand the specific data formats and available parameters.  The specific return values and how to work with them will be present in the API documentation.
* **Authentication:** The `app_signature` is a critical authentication factor.  Failure to properly provide it will likely result in errors.
* **Pagination:** Use `page_no` and `page_size` for handling large result sets.


This detailed guide aims to help you integrate with the AliExpress Affiliate Hot Product API effectively. Remember to replace placeholders with your actual values. Remember to adapt the code to properly handle the data returned by the API and to include appropriate error handling.