```python
import pytest
import base64

# No Python code to test was provided in the input.
# This example creates dummy functions and test cases.
# Replace these with the actual functions from your code.

def get_api_key(website_url, credentials_file="credentials.kdbx"):
    """
    Retrieves the API key for a given website URL from a credentials file.
    
    Args:
        website_url: The URL of the website.
        credentials_file: The path to the credentials file.
        
    Returns:
        The API key as a string, or None if not found.
    """
    # Replace this with actual logic to read from credentials file.
    if website_url == "e-cat.co.il":
        return "YOUR_API_KEY_ENC"
    elif website_url == "emil-design.com":
        return "YOUR_API_KEY_2_ENC"
    else:
        return None

def construct_api_request(website_url, endpoint, api_key):
    """
    Constructs the API request string.

    Args:
        website_url: The URL of the website.
        endpoint: The API endpoint.
        api_key: The API key.
        
    Returns:
        The API request string, or None if invalid inputs.

    Raises:
        TypeError: If input types are incorrect.
    """
    if not isinstance(website_url, str) or not isinstance(endpoint, str) or not isinstance(api_key, str):
        raise TypeError("Input types must be strings.")
    encoded_key = base64.b64encode(api_key.encode()).decode()
    request_string = f"curl -X GET 'https://{website_url}/api/{endpoint}' \\\n-H 'Authorization: Basic {encoded_key}'"
    return request_string

# Test cases
def test_get_api_key_valid_input():
    api_key = get_api_key("e-cat.co.il")
    assert api_key is not None, "API key not found for e-cat.co.il"

def test_get_api_key_invalid_input():
    api_key = get_api_key("invalid_url")
    assert api_key is None, "API key should not be found for invalid URL"

def test_construct_api_request_valid_input():
    api_key = "TEST_API_KEY"
    request_string = construct_api_request("e-cat.co.il", "products", api_key)
    assert isinstance(request_string, str), "API request should be a string"

def test_construct_api_request_invalid_key_type():
  with pytest.raises(TypeError):
    construct_api_request("e-cat.co.il", "products", 123)

#Example Usage (replace with your actual function calls)
# api_key = get_api_key("e-cat.co.il")
# request = construct_api_request("e-cat.co.il", "products", api_key)
```

**Explanation and Improvements:**

1. **Dummy Functions:** The provided code had no Python functions to test.  This example creates placeholder functions `get_api_key` and `construct_api_request` with basic functionality.  Crucially, replace these with your actual functions.

2. **`pytest.raises` for Exception Handling:** Added a test `test_construct_api_request_invalid_key_type` to demonstrate how to test for the `TypeError` raised by `construct_api_request` when input is not a string.

3. **Clearer Test Names:** Test function names are more descriptive (e.g., `test_get_api_key_valid_input`).

4. **Edge Cases:**  `test_get_api_key_invalid_input` tests for a non-existent website.

5. **Type Handling:** The `construct_api_request` function now includes input validation to raise a `TypeError` if the input types are incorrect, and the test case `test_construct_api_request_invalid_key_type` demonstrates how to check for that error.

6. **Assertions:** Assertions are used to check for expected outputs (e.g., `api_key is not None`).


**To use these tests:**

1.  **Replace the placeholder functions** with your actual PrestaShop functions.
2.  **Add `import pytest` at the beginning.**
3.  **Modify `credentials.kdbx`** (or the way you read data from it) to have example API keys for testing.


Remember to install the `pytest` library if you haven't already: `pip install pytest`.  Then run the tests from your terminal: `pytest your_test_file.py` (replace `your_test_file.py` with the name of your test file). Remember to install the `base64` module: `pip install base64` if you don't have it.