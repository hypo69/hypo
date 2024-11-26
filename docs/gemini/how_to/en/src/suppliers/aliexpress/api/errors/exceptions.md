# Usage Guide for `hypotez/src/suppliers/aliexpress/api/errors/exceptions.py`

This module defines custom exception classes for handling errors that might occur when interacting with the AliExpress API.  It's crucial for robust error handling in your application.


## Exception Classes

The module provides a hierarchy of exceptions, inheriting from a base `AliexpressException`. This allows for specific error handling based on the type of issue encountered.

* **`AliexpressException`**:
    * The base class for all AliExpress API exceptions.
    * Takes a `reason` string as an argument in the constructor, which provides details about the error.
    * The `__str__` method returns the reason string for easier error reporting.

* **`InvalidArgumentException`**:
    * Raised when the arguments provided to an API method are incorrect.

* **`ProductIdNotFoundException`**:
    * Raised if the provided product ID does not exist in the AliExpress system.

* **`ApiRequestException`**:
    * Raised when a request to the AliExpress API fails (e.g., network issue, server error).

* **`ApiRequestResponseException`**:
    * Raised when the response received from the AliExpress API is not in the expected format or contains an error.

* **`ProductsNotFoudException`**:
    * Raised if no products are found matching the search criteria.

* **`CategoriesNotFoudException`**:
    * Raised if no categories are found matching the search criteria.

* **`InvalidTrackingIdException`**:
    * Raised if the provided tracking ID is invalid or missing.


## How to Use

To handle exceptions raised by AliExpress API calls, use a `try...except` block:

```python
from hypotez.src.suppliers.aliexpress.api.errors.exceptions import AliexpressException, InvalidArgumentException, ProductIdNotFoundException  # Import the necessary exceptions

try:
    # Your AliExpress API call here
    result = aliexpress_api.get_product_details(product_id)
    # ... process the result ...
except InvalidArgumentException as e:
    print(f"Invalid argument: {e}")
except ProductIdNotFoundException as e:
    print(f"Product ID not found: {e}")
except AliexpressException as e:
    print(f"An error occurred: {e}") # Catch all other aliexpress exceptions
except Exception as e:  # Important: catch generic exceptions after the specific ones
    print(f"An unexpected error occurred: {e}")
```

**Explanation:**

1.  Import the specific exception classes you expect to handle.
2.  Enclose your API call within a `try...except` block.
3.  Catch specific exceptions (e.g., `InvalidArgumentException`) first, then the more general `AliexpressException`.
4. **Crucially**, handle the generic `Exception` last, to catch errors not related to AliExpress API calls. This prevents unexpected crashes.

**Example Handling:**

```python
try:
    # ... your API call
except AliexpressException as e:
    if isinstance(e, ProductIdNotFoundException):
        print("Product not found; taking alternative action...")
        # Handle the case where the product is not found
    else:
        print(f"General AliExpress API error: {e}")
```


This example demonstrates how to differentiate between different types of `AliexpressException` and handle them appropriately.  This improves the robustness and maintainability of your code. Remember to replace `aliexpress_api` and `get_product_details` with your actual API object and method.