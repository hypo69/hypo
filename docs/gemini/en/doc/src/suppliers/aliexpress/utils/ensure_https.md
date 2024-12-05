# ensure_https.py

## Overview

This module provides a function to ensure that URLs or product IDs are formatted with the `https://` prefix.  It handles both single strings and lists of strings, intelligently determining whether the input is a product ID or a full URL.  If a product ID is detected, it constructs a full URL with the `https://www.aliexpress.com/item/` prefix and the appropriate suffix.


## Functions

### `ensure_https`

**Description**: This function ensures that the provided URL string(s) contain the `https://` prefix. If the input is a product ID, it constructs a full URL with `https://` prefix.

**Parameters**:

- `prod_ids` (str | list[str]): A URL string or a list of URL strings to check and modify if necessary.

**Returns**:

- str | list[str]: The URL string or list of URL strings with the `https://` prefix.

**Raises**:

- `ValueError`: If `prod_ids` is an instance of `WindowsPath`.


### `ensure_https_single`

**Description**: This function ensures a single URL or product ID string has the `https://` prefix.

**Parameters**:

- `prod_id` (str): The URL or product ID string.

**Returns**:

- str: The URL string with the `https://` prefix.

**Raises**:

- `ValueError`: If `prod_id` is an instance of `WindowsPath`.


## Examples

```python
# Example usage for single string input
url = "example_product_id"
url_with_https = ensure_https(url)
print(url_with_https)  # Output: https://www.aliexpress.com/item/example_product_id.html

# Example usage for list input
urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
urls_with_https = ensure_https(urls)
print(urls_with_https)  # Output: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

# Example handling existing https URL
url_https = "https://www.example.com/item/example_product_id"
url_https_output = ensure_https(url_https)
print(url_https_output) #Output: https://www.example.com/item/example_product_id
```


```python
# Example raising a ValueError (if WindowsPath was implemented)
# from pathlib import WindowsPath # Uncomment this line to test error case.
# prod_id = WindowsPath("C:\\example\\path")
# try:
#    ensure_https(prod_id)
# except ValueError as ex:
#    print(f"Caught expected exception: {ex}")


```


```
```