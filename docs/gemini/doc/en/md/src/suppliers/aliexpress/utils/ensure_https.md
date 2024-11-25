# ensure_https.py

## Overview

This module provides a function to ensure that provided URL strings or lists of strings contain the "https://" prefix.  If the input is a product ID, it constructs a full URL with the https:// prefix.


## Functions

### `ensure_https`

**Description**: This function checks if the input `prod_ids` is a string or a list of strings.  If it's a string, it attempts to extract a product ID and construct a full URL with the "https://" prefix. If it's a list, it processes each item in the list using an inner function (`ensure_https_single`).

**Parameters**:

- `prod_ids` (str | list[str]): A URL string or a list of URL strings to check and modify if necessary.

**Returns**:

- str | list[str]: The URL string or list of URL strings with the https:// prefix.

**Raises**:

- `ValueError`: If `prod_ids` is an instance of `WindowsPath`.


### `ensure_https_single`

**Description**: This function ensures a single URL or product ID string has the "https://" prefix.

**Parameters**:

- `prod_id` (str): The URL or product ID string.

**Returns**:

- str: The URL string with the https:// prefix.

**Raises**:

- `ValueError`: If `prod_id` is an instance of `WindowsPath`.

**Example Usage (from the docstring):**

```python
# Example usage
url = "example_product_id"
url_with_https = ensure_https(url)
print(url_with_https)  # Output: https://www.aliexpress.com/item/example_product_id.html

urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
urls_with_https = ensure_https(urls)
print(urls_with_https)  # Output: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']
```


## Module Variables

### `MODE`

**Description**:  Stores the current mode, likely for development or production. Its value is currently set to 'dev'.


## Dependencies

### `extract_prod_ids`

- From `src.suppliers.aliexpress.utils`. Used to extract product IDs from URLs or product IDs.

### `logger`

- From `src.logger`. Used for logging.


## Error Handling

The `ensure_https` function uses `logger.error` to log errors, ensuring that invalid product IDs or URLs are recorded, but the program continues execution.


```