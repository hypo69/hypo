```python
import pytest
import base64
import requests
from unittest.mock import patch

# This file doesn't contain any code to directly test, but it outlines the usage of PrestaShop API.
# Therefore, the tests will focus on verifying the API usage examples described in the document.
# For the purpose of this test, we will mock the requests library for API call.
# Note: This approach assumes that the system handles API credentials correctly, which is not covered in the code.

# Fixture to mock API key (for demonstration purposes)
@pytest.fixture
def mock_api_key():
    """Provides a dummy API key for testing."""
    return "test_api_key"


# Fixture to mock base URL
@pytest.fixture
def mock_base_url():
    """Provides a dummy Base URL for testing."""
    return "https://test-site.com"


@patch('requests.get')
def test_api_call_with_valid_credentials(mock_get, mock_api_key, mock_base_url):
    """
    Tests a valid API call to a PrestaShop endpoint, mimicking the provided example.
    Checks if the authorization header is correctly set.
    """
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response.json = lambda: {"products": []}
    mock_get.return_value = mock_response

    endpoint = "products"
    api_key_encoded = base64.b64encode(f"{mock_api_key}:".encode()).decode()
    expected_headers = {"Authorization": f"Basic {api_key_encoded}"}
    url = f"{mock_base_url}/api/{endpoint}"
    
    response = requests.get(url, headers = expected_headers)

    mock_get.assert_called_once_with(url, headers=expected_headers)
    assert response.status_code == 200
    assert response.json() == {"products": []}



@patch('requests.get')
def test_api_call_with_invalid_endpoint(mock_get,mock_api_key, mock_base_url):
    """
     Tests an API call to a non-existent PrestaShop endpoint.
    """
    mock_response = requests.Response()
    mock_response.status_code = 404  # Simulate a "Not Found" response
    mock_get.return_value = mock_response
    
    endpoint = "invalid_endpoint"
    api_key_encoded = base64.b64encode(f"{mock_api_key}:".encode()).decode()
    expected_headers = {"Authorization": f"Basic {api_key_encoded}"}
    url = f"{mock_base_url}/api/{endpoint}"

    response = requests.get(url, headers = expected_headers)

    mock_get.assert_called_once_with(url, headers = expected_headers)
    assert response.status_code == 404

@patch('requests.get')
def test_api_call_with_no_api_key(mock_get, mock_base_url):
    """
    Tests API call without an API key, simulating a bad credentials error.
    """

    mock_response = requests.Response()
    mock_response.status_code = 401  # Unauthorized response
    mock_get.return_value = mock_response

    endpoint = "products"
    url = f"{mock_base_url}/api/{endpoint}"

    response = requests.get(url, headers = {}) # Empty headers.

    mock_get.assert_called_once_with(url, headers={})
    assert response.status_code == 401

def test_base64_encoding_api_key(mock_api_key):
    """Tests if the base64 encoding is correctly applied to the API key."""
    api_key_encoded = base64.b64encode(f"{mock_api_key}:".encode()).decode()
    expected_encoded_key = base64.b64encode("test_api_key:".encode()).decode()
    assert api_key_encoded == expected_encoded_key
```