How to use the `arguments` module in the AliExpress API helper functions.

This module, located in `hypotez/src/suppliers/aliexpress/api/helpers/arguments.py`, provides functions for handling input arguments, specifically for getting product IDs and converting lists to strings.

**1. `get_list_as_string(value)`:**

* **Purpose:** Converts a list or string into a comma-separated string.  Handles `None` input gracefully.
* **Input:**
    * `value`: A list or string.  Can be `None`.
* **Output:**
    * A comma-separated string if the input is a list; the original string if the input is a string; `None` if input is `None`.
* **Raises:** `InvalidArgumentException` if the input is neither a list nor a string.
* **Example Usage:**

```python
from hypotez.src.suppliers.aliexpress.api.helpers.arguments import get_list_as_string

# List to string
my_list = ["product1", "product2"]
result = get_list_as_string(my_list)  # result = "product1,product2"

# String input
my_string = "product3"
result = get_list_as_string(my_string)  # result = "product3"

# None input
result = get_list_as_string(None)  # result = None

# Invalid input (integer)
try:
    result = get_list_as_string(123)
except InvalidArgumentException as e:
    print(f"Error: {e}")  # Output: Error: Argument should be a list or string: 123
```


**2. `get_product_ids(values)`:**

* **Purpose:** Extracts product IDs from a list or comma-separated string of product identifiers.  Uses the `get_product_id` function to standardize.
* **Input:**
    * `values`: A list or a comma-separated string of product identifiers.
* **Output:**
    * A list of product IDs (integers).
* **Raises:**
    * `InvalidArgumentException` if the input is neither a list nor a string.
* **Example Usage:**

```python
from hypotez.src.suppliers.aliexpress.api.helpers.arguments import get_product_ids
from hypotez.src.suppliers.aliexpress.api.helpers.errors import InvalidArgumentException

# Example assuming get_product_id is defined elsewhere. For demonstration purposes:
def get_product_id(value):
    try:
        return int(value)
    except ValueError:
        raise InvalidArgumentException("Invalid product ID format")


# String input
product_strings = "123,456,789"
product_ids = get_product_ids(product_strings)  # product_ids = [123, 456, 789]

# List input
product_strings = ["101", "202"]
product_ids = get_product_ids(product_strings)  # product_ids = [101, 202]


# Invalid input
try:
    product_ids = get_product_ids(123)  # raises InvalidArgumentException
except InvalidArgumentException as e:
   print(f"Error: {e}")  # Example output: Error: Argument product_ids should be a list or string

# Invalid product id
try:
   product_strings = "abc,def"
   product_ids = get_product_ids(product_strings)
except InvalidArgumentException as e:
   print(f"Error: {e}")  # Example output: Error: Invalid product ID format
```

**Important Considerations:**

* **Error Handling:** The functions include `InvalidArgumentException` to handle cases where the input data is not in the expected format.  Make sure to have `InvalidArgumentException` defined in the appropriate file (e.g., `errors.exceptions`).
* **`get_product_id` Function:**  The `get_product_ids` function relies on the `get_product_id` function (from `..tools.get_product_id`) to convert input into product IDs.  Ensure `get_product_id` is defined and handles potential errors (e.g., invalid product ID formats) appropriately.


This guide provides clear instructions on how to utilize the `arguments` module functions effectively within your AliExpress API code. Remember to adapt the example usages to your specific needs and data structures.