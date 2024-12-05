rst
How to use the url.py module
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/utils/string/url.py`) provides functions for working with URLs. It includes a function to extract query parameters from a URL string and another to validate if a given string is a valid URL.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `urlparse`, `parse_qs` from the `urllib.parse` module and `validators` for URL validation.

2. **`extract_url_params(url: str) -> dict | None` function:**
    - Takes a URL string as input.
    - Uses `urlparse` to parse the URL string into components (scheme, netloc, path, params, query, fragment).
    - Extracts the query string using `parsed_url.query`.
    - Parses the query string into a dictionary using `parse_qs`.
    - Handles cases where a parameter has only one value by converting the list value to a string.
    - Returns the dictionary of query parameters or `None` if the URL has no query parameters.

3. **`is_url(text: str) -> bool` function:**
    - Takes a string as input.
    - Uses the `validators.url()` function to check if the input string is a valid URL.
    - Returns `True` if the string is a valid URL, `False` otherwise.

4. **Main execution block (`if __name__ == "__main__":`)**:
    - Prompts the user to enter a URL.
    - Calls `is_url()` to check if the input is a valid URL.
    - If the URL is valid:
        - Calls `extract_url_params()` to extract the parameters.
        - Prints the extracted parameters if available.
        - If no parameters are found, prints a message indicating this.
    - If the URL is invalid, prints an appropriate message.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.utils.string import url

    # Example usage:
    url_string = "https://example.com/path?param1=value1&param2=value2&param3="
    validated_url = url.is_url(url_string)
    if validated_url:
        params = url.extract_url_params(url_string)
        if params:
            print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}
        else:
            print("No parameters found.")
    else:
        print("Invalid URL")


    invalid_url = "invalid_url_example"
    validated_url = url.is_url(invalid_url)
    if validated_url:
        params = url.extract_url_params(invalid_url)
        if params:
            print(params)
        else:
            print("No parameters found.")
    else:
        print("Invalid URL")