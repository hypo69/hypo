rst
How to use the get_product_id function
========================================================================================
Description
-------------------------
This Python function extracts a product ID from a given string.  It leverages the `extract_prod_ids` function from a different module to achieve this.  Crucially, it handles cases where no valid product ID is found by raising a custom exception, `ProductIdNotFoundException`.  It replaces previous attempts at regex-based extraction of product IDs from potentially complex strings, and directly leverages an external function to find the product id.


Execution steps
-------------------------
1. The function `get_product_id` takes a single string argument, `raw_product_id`, representing the input text potentially containing a product ID.
2. It calls the `extract_prod_ids` function, passing the `raw_product_id` as input.
3. `extract_prod_ids` is expected to return the extracted product ID as a string.
4. The `get_product_id` function returns the product ID.  If `extract_prod_ids` is unable to extract a valid product ID, it will not return anything; instead, an exception will be raised.
5. If the input string `raw_product_id` does not contain any valid product id according to `extract_prod_ids`, the function will raise a `ProductIdNotFoundException` exception containing the error message and the original `raw_product_id`.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
    from hypotez.src.suppliers.aliexpress.api.tools.errors import ProductIdNotFoundException


    # Example usage
    valid_product_id_string = "abc123456"

    try:
        product_id = get_product_id(valid_product_id_string)
        print(f"Extracted product ID: {product_id}")

    except ProductIdNotFoundException as e:
        print(f"Error: {e}")


    invalid_product_id_string = "This string does not have a product ID"

    try:
        product_id = get_product_id(invalid_product_id_string)
        print(f"Extracted product ID: {product_id}")
    except ProductIdNotFoundException as e:
        print(f"Error: {e}")