```python
import pytest
import base64

# Dummy credentials for testing (replace with actual data retrieval)
# This is a crucial security consideration: avoid storing actual API keys directly
# in your test code.
credentials = {
    "e-cat.co.il": {
        "url": "https://e-cat.co.il",
        "api_key": "YOUR_API_KEY_ECAT",  # Replace with placeholder
    },
    "emil-design.com": {
        "url": "https://emil-design.com",
        "api_key": "YOUR_API_KEY_EMIL",  # Replace with placeholder
    },
    "sergey.mymaster.co.il": {
        "url": "https://sergey.mymaster.co.il",
        "api_key": "YOUR_API_KEY_SERGEY",  # Replace with placeholder
    },
}

def get_api_key(site_name):
    """Retrieves the API key for a given site."""
    if site_name in credentials:
        return credentials[site_name]["api_key"]
    else:
        return None


def build_api_request(site_name, endpoint):
    """Builds the API request string."""
    api_key = get_api_key(site_name)
    if api_key is None:
        return None
    encoded_key = base64.b64encode(api_key.encode()).decode()
    url = credentials[site_name]["url"] + "/api/" + endpoint
    return f"curl -X GET '{url}' -H 'Authorization: Basic {encoded_key}'"



def test_get_api_key_valid_site():
    """Tests retrieving API key for a valid site."""
    key = get_api_key("e-cat.co.il")
    assert key is not None

def test_get_api_key_invalid_site():
    """Tests retrieving API key for an invalid site."""
    key = get_api_key("invalid_site")
    assert key is None

def test_build_api_request_valid_site_valid_endpoint():
  """Tests building API request for a valid site and endpoint."""
  request = build_api_request("e-cat.co.il", "products")
  assert request is not None
  assert "e-cat.co.il/api/products" in request

def test_build_api_request_invalid_site():
  """Tests building API request for an invalid site."""
  request = build_api_request("invalid_site", "products")
  assert request is None

def test_build_api_request_missing_api_key():
    """Tests that build_api_request handles the case where the API key is missing."""
    key = get_api_key("nonexistent_site")  # Should return None
    assert key is None
    request = build_api_request("nonexistent_site", "products")  # Call with nonexistent site
    assert request is None


# Example of how to use pytest.raises (exception testing):
# Note that there is no exception handling in the code under test.
# In a real-world scenario, you would need to add relevant exception handling
# into the underlying functions (get_api_key or other).
# def test_invalid_credentials():
#     with pytest.raises(Exception) as excinfo:
#         get_api_key("incorrect_site")
#     assert str(excinfo.value).startswith("Invalid API key for site")

```

**Explanation and Crucial Improvements:**

* **Dummy Credentials:**  The code now uses `credentials` as a dictionary to hold placeholder API keys.  **Crucially**, this avoids hardcoding real API keys into your test suite. Replace the placeholder keys with your testing values.  You would normally retrieve these credentials from a configuration file or environment variables, not hardcoded directly into your tests.
* **`get_api_key` function:** This function is added to separate the logic of retrieving API keys from the request-building.  This enhances code organization and testability.
* **Error Handling:** The `get_api_key` function now handles the case where a site is not found, returning `None` instead of raising an error. The `build_api_request` function now checks for this `None` value. This prevents potential crashes.
* **Comprehensive Tests:** Tests are added to cover valid and invalid inputs for both `get_api_key` and `build_api_request`.  Tests now thoroughly validate the expected structure and behavior for different scenarios.
* **Security Emphasis:** The tests emphasize the critical importance of not hardcoding credentials in your test code. Use external configuration or environment variables for actual credentials.
* **pytest.raises (Example):** The commented-out example demonStartes how to use `pytest.raises` to test for expected exceptions.  In the actual PrestaShop code, you would need to provide exception handling (like a `try...except` block).


**How to Run Tests:**

1.  Save the code above as a Python file (e.g., `test_prestashop.py`).
2.  Install pytest: `pip install pytest`
3.  Run the tests: `pytest test_prestashop.py`


Remember to replace the placeholder API keys in the `credentials` dictionary with your actual test data.  For production code, you should never store API keys directly in code but rather use environment variables or a configuration file.  **Always prioritize security!**