rst
How to use the argument helpers
========================================================================================

Description
-------------------------
This Python code defines two functions, `get_list_as_string` and `get_product_ids`, for handling input arguments related to product IDs.  `get_list_as_string` converts a list of strings to a comma-separated string or returns the string value directly if the input is a string. `get_product_ids` extracts product IDs from a list or comma-separated string and validates the input type. It uses the `get_product_id` function (assumed to be defined elsewhere) to retrieve actual product IDs.  Both functions raise `InvalidArgumentException` for invalid input types or values.

Execution steps
-------------------------
1. **`get_list_as_string(value)` function:**
    - Takes a `value` as input.
    - Checks if the input is `None`. If it is, it returns `None`.
    - Checks if the input is a string. If it is, it returns the string directly.
    - Checks if the input is a list. If it is, it joins the elements of the list with commas and returns the resulting string.
    - Otherwise, it raises `InvalidArgumentException` indicating that the input should be a list or a string.

2. **`get_product_ids(values)` function:**
    - Takes a `values` parameter.
    - Checks if the input `values` is a string. If it is, splits the string into a list of strings using commas as delimiters.
    - Checks if the input `values` is a list. If not, raises `InvalidArgumentException`.
    - Initializes an empty list `product_ids`.
    - Iterates through each `value` in the input `values` list.
    - Calls the `get_product_id(value)` function for each `value` to retrieve the product ID. Appends the returned product ID to the `product_ids` list.
    - Returns the `product_ids` list.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers.arguments import get_list_as_string, get_product_ids
    from hypotez.src.suppliers.aliexpress.api.helpers.errors import InvalidArgumentException  # Assuming this error class exists

    # Example usage for get_list_as_string
    string_result = get_list_as_string(["apple", "banana", "orange"])
    print(f"String Result: {string_result}")  # Output: String Result: apple,banana,orange

    list_result = get_list_as_string("grape")
    print(f"List Result: {list_result}")  # Output: List Result: grape

    invalid_result = get_list_as_string(123)  # Raises InvalidArgumentException
    # print(f"Invalid Result: {invalid_result}")


    # Example usage for get_product_ids
    product_list = get_product_ids(["123", "456", "789"])
    print(f"Product IDs: {product_list}") # Output: Product IDs: [<product_id_123>, <product_id_456>, <product_id_789>]


    product_string = get_product_ids("101,202,303")
    print(f"Product IDs from string: {product_string}") # Output: Product IDs from string: [<product_id_101>, <product_id_202>, <product_id_303>]

    invalid_product = get_product_ids(123) # Raises InvalidArgumentException
    # print(f"Invalid Product IDs: {invalid_product}")