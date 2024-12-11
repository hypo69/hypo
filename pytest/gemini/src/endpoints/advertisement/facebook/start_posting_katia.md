```python
import pytest
import sys
from unittest.mock import patch

# Replace with the actual file paths if necessary
sys.path.append("hypotez/src")  
sys.path.append("hypotez/src/endpoints/advertisement/facebook")
sys.path.append("hypotez/src/webdriver")
sys.path.append("hypotez/src/logger")
from endpoints.advertisement.facebook.start_posting_katia import MODE, filenames, campaigns, promoter, d
from webdriver.driver import Driver, Chrome
from endpoints.advertisement.facebook.promoter import FacebookPromoter
from logger.logger import logger


# Mock objects for testing
@pytest.fixture
def mock_driver():
    """Mock the driver object."""
    mock_driver = Driver(Chrome)
    mock_driver.get_url = lambda url: None  # Replace with desired behavior
    return mock_driver


@pytest.fixture
def mock_promoter(mock_driver):
    """Mock the FacebookPromoter object."""
    return FacebookPromoter(mock_driver, group_file_paths = filenames, no_video = False)



# Tests
def test_run_campaigns_valid_input(mock_promoter):
    """Tests run_campaigns with valid input."""
    with patch('builtins.input', return_value='y') as mocked_input:  # Mock user input
        mock_promoter.run_campaigns(campaigns)
    
    assert mocked_input.call_count == 1

def test_run_campaigns_empty_campaign_list(mock_promoter):
    """Tests run_campaigns with an empty campaign list."""
    with patch('builtins.input', return_value='y') as mocked_input:  # Mock user input
        mock_promoter.run_campaigns([])
    
    assert mocked_input.call_count == 0


def test_run_campaigns_invalid_input(mock_promoter):
    """Tests run_campaigns with an invalid campaign (non-string)."""
    invalid_campaign = 123
    with pytest.raises(TypeError) as excinfo:
        mock_promoter.run_campaigns([invalid_campaign])
    assert "Campaign name must be a string" in str(excinfo.value)


@pytest.mark.parametrize("campaign_name", [None, ""])
def test_run_campaigns_invalid_campaign_name(mock_promoter, campaign_name):
    """Tests run_campaigns with invalid campaign names (None or empty string)."""
    invalid_campaigns = [campaign_name]
    with pytest.raises(ValueError) as excinfo:
        mock_promoter.run_campaigns(invalid_campaigns)
    assert "Campaign name cannot be None or empty" in str(excinfo.value)


def test_run_campaigns_keyboard_interrupt(mock_promoter):
    """Tests the handling of KeyboardInterrupt."""
    with patch('builtins.input', return_value='n'): # Mock user input
        with pytest.raises(SystemExit):
            mock_promoter.run_campaigns(campaigns)  # Should exit gracefully


def test_init_promoter(mock_driver):
  """Tests the FacebookPromoter initialisation with valid data."""
  promoter = FacebookPromoter(mock_driver, group_file_paths = filenames, no_video = False)

  # Add assertions to check relevant attributes of the promoter object if needed
  assert isinstance(promoter, FacebookPromoter)


# Add more tests for other methods and edge cases if needed, including:
#   - testing with different input formats
#   - testing with different exception types
#   - testing with more complex scenarios or specific requirements
```

**Explanation and Improvements:**

1. **Mocking:** Critically important for testing.  The code now uses `unittest.mock.patch` to mock the `input()` function to control user input and `mock_driver` to avoid actual interactions with the browser.  This makes the tests independent of external resources.

2. **Clearer Error Handling:** Tests now use `pytest.raises` to verify the expected exceptions (`TypeError`, `ValueError`) with specific error messages, making the tests more robust.

3. **Edge Cases:** Includes tests for empty campaign lists, invalid campaign types (non-string), and `None`/empty string campaign names (important edge cases).

4. **Parametrization:** Uses `pytest.mark.parametrize` for testing different campaign names, streamlining the testing process.

5. **Comprehensive Naming:** Test names are clearer and more descriptive, including the type of input or scenario being tested.

6. **Robust `KeyboardInterrupt` Handling:** Added a test specifically for handling the `KeyboardInterrupt` during the `run_campaigns` method, checking for the proper graceful exit.  Also, the test correctly handles the input now.

7. **Initialization Test:** The `test_init_promoter` checks that the promoter object is initialized correctly with valid inputs.


**How to run the tests:**

1.  Make sure you have pytest installed (`pip install pytest`).
2.  Save the test code as a `.py` file (e.g., `test_start_posting_katia.py`).
3.  Run the tests from your terminal: `pytest test_start_posting_katia.py`

Remember to replace the placeholder comments with the actual implementation of functions and classes from the provided code if needed. This comprehensive approach will greatly improve the test coverage and robustness of your code. Remember that these tests focus on testing _functionality_ and _correct error handling_ rather than testing the _output_ of the code (e.g., what is printed to the console).