```python
import pytest
import requests
from unittest.mock import patch
from types import SimpleNamespace
from hypotez.src.endpoints.prestashop.category import PrestaCategory
from src.logger import logger  # Assuming this is from your provided code


# Mock the requests library for testing
@pytest.fixture
def mock_get(mocker):
    mock_response = mocker.MagicMock(status_code=200)
    mock_response.json.return_value = {'category': {'id': 11259, 'id_parent': 11248}}  # Example JSON response
    mocker.patch('requests.get', return_value=mock_response)
    return mock_response


@pytest.fixture
def presta_category(mock_get):
    credentials = SimpleNamespace(api_domain='test_domain', api_key='test_key')
    return PrestaCategory(credentials=credentials)

# Tests for get_parent_categories_list
def test_get_parent_categories_list_valid_input(presta_category, mock_get):
    """Tests with valid input."""
    parent_categories_list = []
    result = presta_category.get_parent_categories_list(11259, parent_categories_list)
    assert result == [11248]


def test_get_parent_categories_list_valid_recursive(presta_category, mock_get):
    """Test recursive calls for valid input."""
    parent_categories_list = []
    mock_response2 = mock_get.return_value
    mock_response2.json.return_value = {'category': {'id': 11248, 'id_parent': 100}}
    result = presta_category.get_parent_categories_list(11259, parent_categories_list)
    assert result == [11248, 100]



def test_get_parent_categories_list_root_category(presta_category, mock_get):
    """Tests when the input category is a root category."""
    parent_categories_list = []
    mock_response = mock_get.return_value
    mock_response.json.return_value = {'category': {'id': 100, 'id_parent': 2}}  # id_parent = 2, which is root category

    result = presta_category.get_parent_categories_list(100, parent_categories_list)
    assert result == [2]

def test_get_parent_categories_list_invalid_input(presta_category, mock_get):
    """Tests with invalid input: empty ID."""
    parent_categories_list = []
    with pytest.raises(ValueError):
        presta_category.get_parent_categories_list(None, parent_categories_list)



def test_get_parent_categories_list_empty_response(presta_category, mocker):
    """Tests with empty response from the API."""
    mock_response = mocker.MagicMock(status_code=200)
    mock_response.json.return_value = {}
    mocker.patch('requests.get', return_value=mock_response)


    parent_categories_list = []
    with patch.object(logger, 'error') as mock_logger:
        presta_category.get_parent_categories_list(123, parent_categories_list)
        mock_logger.assert_called_once_with('Что-то не так с категориями')

```

**Explanation and Improvements:**

* **Mocking `requests.get`:** The `mock_get` fixture now properly mocks the `requests.get` function, returning a mock response.  Crucially, it returns a *meaningful* JSON response, making the test more robust.

* **Clearer Test Cases:**  The test names are more descriptive (e.g., `test_get_parent_categories_list_valid_recursive`).

* **Edge Case Tests:** The code includes tests for a root category (`test_get_parent_categories_list_root_category`), and importantly, a test for an empty response (`test_get_parent_categories_list_empty_response`), mimicking a scenario where the requested category doesn't exist on the server.

* **Error Handling:** The `test_get_parent_categories_list_invalid_input` now correctly uses `pytest.raises` to assert that the ValueError is raised when `id_category` is `None`.  This is critical for testing exception handling.

* **Using `patch` for Logging:** The `test_get_parent_categories_list_empty_response` now uses `patch` to effectively mock the `logger.error` call, and verify that it was called with the expected error message. This prevents the test from depending on the actual behavior of the logger.

* **Data Driven Tests:**  For completeness, consider adding tests with more complex scenarios if data is provided that dictates multiple calls to itself or an error case.

* **Input Validation:** Added test for `None` input.

* **Correct Return Value Assertions:**  Returns are verified to match expected behavior


**How to Run the Tests:**

1.  Make sure you have `pytest` installed: `pip install pytest`
2.  Save the tests in a file (e.g., `test_category.py`) alongside your `category.py` file.
3.  Run the tests from your terminal: `pytest test_category.py`


This improved solution provides a much more comprehensive set of tests for the `PrestaCategory` class, covering valid input, edge cases, and crucial error handling. Remember to adapt the example JSON responses to match your actual API responses for full test coverage. Remember to replace `from src.logger import logger` with the correct import path to the `logger` module.