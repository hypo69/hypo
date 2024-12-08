rst
How to use the exceptions module
========================================================================================

Description
-------------------------
This module defines custom exception classes for handling errors encountered during interactions with the AliExpress API.  It provides a hierarchy of exceptions, inheriting from a common base class `AliexpressException`,  allowing for specific error handling based on the type of issue.

Execution steps
-------------------------
1. **Exception Creation:**  When an error occurs during AliExpress API interaction (e.g., invalid arguments, missing product IDs, API request failures), the appropriate exception class (e.g., `InvalidArgumentException`, `ProductIdNotFoundException`, `ApiRequestException`) is instantiated.  The `reason` for the exception is provided as a string argument to the constructor.

2. **Exception Handling:**  The exception is then raised, and other parts of the code can catch and handle it using `try...except` blocks.  The `__str__` method of each exception class returns the `reason` string, providing details about the specific error.  This allows for specific error handling based on the exception type.

3. **Exception Types:** The module defines various specific exception types to allow for better-targeted error handling, including but not limited to `InvalidArgumentException`, `ProductIdNotFoundException`, `ApiRequestException`, `ApiRequestResponseException`, `ProductsNotFoudException`, `CategoriesNotFoudException`, and `InvalidTrackingIdException`.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.errors.exceptions import (
        AliexpressException,
        ProductIdNotFoundException,
        ApiRequestException,
    )

    try:
        # ... Code that interacts with the AliExpress API ...
        # Example:
        product_id = "invalid_id"
        # ...
        # Assuming the following function raises an exception
        get_product_details(product_id)

    except ProductIdNotFoundException as e:
        print(f"Error: Product ID not found - {e}")
    except ApiRequestException as e:
        print(f"Error: API request failed - {e}")
    except AliexpressException as e:
        print(f"General error with AliExpress API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")