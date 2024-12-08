How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `extract_prod_ids` that extracts product IDs from URLs or directly validates IDs.  It utilizes regular expressions to find product IDs within URLs and handles both single URLs and lists of URLs as input. The function also validates if the input is already a valid product ID.

Execution steps
-------------------------
1. **Input Validation:** The code first checks if the input `urls` is a list or a single string.
2. **List Handling:** If `urls` is a list, it iterates through each element in the list.
3. **ID Extraction (for URLs):** For each item in the list, it calls the internal `extract_id` function to extract the product ID from the URL.
4. **Validation:** Inside the `extract_id` function, it first checks if the input string is a valid integer representing the product ID. If so, the input string itself is returned as a product ID.
5. **Regular Expression Match:** If the input is not a valid ID, a regular expression is used to find the product ID within the URL string. If a match is found, the matched product ID is extracted and returned.  If no match is found, `None` is returned.
6. **Result Handling:**  If the input is a list, the extracted IDs are collected in a new list and returned. If there are no valid IDs found, `None` is returned. If the input is a single URL, the result of the `extract_id` function is directly returned.


Usage example
-------------------------
.. code-block:: python

    import re
    from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids

    # Example with a single URL
    url = "https://www.aliexpress.com/item/123456.html"
    product_id = extract_prod_ids(url)
    print(f"Product ID from single URL: {product_id}")  # Output: Product ID from single URL: 123456

    # Example with a list of URLs
    urls = [
        "https://www.aliexpress.com/item/123456.html",
        "https://www.example.com/item/7891011.html",
        "https://www.wrongsite.com/item/abcdef.html",
        "12345"
    ]
    product_ids = extract_prod_ids(urls)
    print(f"Product IDs from list of URLs: {product_ids}")  # Output: Product IDs from list of URLs: ['123456', '7891011', '12345']

    # Example with a valid product ID string as input
    product_id_str = "987654321"
    extracted_id = extract_prod_ids(product_id_str)
    print(f"Product ID from valid ID string: {extracted_id}") # Output: Product ID from valid ID string: 987654321

    # Example showing None return if no valid IDs found
    invalid_urls = ["https://www.wrongsite.com/item/abcdef.html", "anotherwrongsite.com/item/123456.html"]
    extracted_ids = extract_prod_ids(invalid_urls)
    print(f"Product IDs from list of invalid URLs: {extracted_ids}")  # Output: Product IDs from list of invalid URLs: None