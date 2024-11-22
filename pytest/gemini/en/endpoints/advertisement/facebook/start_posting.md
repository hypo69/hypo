```python
import pytest
import copy
import time
import json
from unittest.mock import patch
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.webdriver import Driver, Chrome
from src.logger import logger


# Mock the Driver class and its methods
@pytest.fixture
def mock_driver():
    """Mocks the Driver class for testing."""
    class MockDriver:
        def __init__(self, browser):
            self.browser = browser

        def get_url(self, url):
            pass  # Mock the get_url method
        def close(self):
          pass

    return MockDriver(Chrome)

# Mock logger for testing
@pytest.fixture
def mock_logger():
    """Mock the logger."""
    mock_logger = patch('src.logger.logger', autospec=True)
    return mock_logger


# Mock file reading (crucial for real testing, but omitted from prompt example)
@pytest.fixture
def mock_files(monkeypatch):
    def _mock_json_read(filename):
        # Simulate different files' content (or empty files for invalid cases)
        if filename == "usa.json":
            return {"groups": [{"group_id": 1, "target": "USA"}]}
        elif filename == "he_ils.json":
            return {"groups": [{"group_id": 2, "target": "Israel"}]}
        else:
            return {}
    monkeypatch.setattr('builtins.open', lambda *args: _mock_json_read(*args))
    return _mock_json_read

@pytest.mark.parametrize('valid_campaigns', [
    ['brands'],
    ['brands', 'mom_and_baby']
])
def test_run_campaigns_valid_input(mock_driver, valid_campaigns, mock_files):
    """Tests run_campaigns with valid input and mocked data."""
    promoter = FacebookPromoter(mock_driver, group_file_paths=["usa.json"], no_video=True)

    promoter.run_campaigns(campaigns=valid_campaigns, group_file_paths=["usa.json"])
    # Add assertions to check if the mock methods were called correctly
    # ...


@pytest.mark.parametrize('invalid_campaigns', [
    ['invalid_campaign_name'],
    []
])
def test_run_campaigns_invalid_campaigns(mock_driver, invalid_campaigns, mock_files):
    """Tests run_campaigns with invalid campaign names."""
    promoter = FacebookPromoter(mock_driver, group_file_paths=["usa.json"], no_video=True)
    with pytest.raises(ValueError):
        promoter.run_campaigns(campaigns=invalid_campaigns, group_file_paths=["usa.json"])

    # Ensure no exceptions are raised
    # ...



def test_run_campaigns_no_files(mock_driver, mock_files):
  """Tests run_campaigns with no files."""
  promoter = FacebookPromoter(mock_driver, group_file_paths=[], no_video=True)

  with pytest.raises(ValueError) as e:
    promoter.run_campaigns(campaigns=['brands'], group_file_paths=[])
  assert "No file paths provided" in str(e.value)

# Test for the while loop.  These can't be properly tested with mocks in this situation.
# def test_while_loop(mock_driver):  # Mocking in this context won't be realistic.
#     # ...


@pytest.mark.parametrize('error_filename', ['invalid_file.json']) # Simulate a bad file
def test_run_campaigns_invalid_file(mock_driver, error_filename, mock_files):
  """Tests run_campaigns with an invalid file."""
  promoter = FacebookPromoter(mock_driver, group_file_paths=[error_filename], no_video=True)
  with pytest.raises(FileNotFoundError) as e:
    promoter.run_campaigns(campaigns=['brands'], group_file_paths=[error_filename])
  assert f"File not found: {error_filename}" in str(e.value)
```

**Explanation and Improvements:**

1. **Mocking:** Crucially, the code now mocks the `Driver` class and the `open` function to read JSON files. This is essential for testing the `FacebookPromoter` class without actually interacting with the Facebook API.  The `mock_files` fixture is particularly important for mocking different JSON file contents.


2. **Parameterization:** Using `pytest.mark.parametrize` makes tests more concise and organized, especially when testing different valid/invalid campaign lists.


3. **Comprehensive Test Cases:** The tests cover valid inputs, missing files, and error handling, including `ValueError` for incorrect campaign names and `FileNotFoundError` for missing files.


4. **Clearer Assertions (Placeholder):**  The comments include placeholders (`# ...`) where you'd add assertions to verify that the mocked functions were called correctly.  In a real-world scenario, these would be crucial for testing the logic.


5. **`pytest.raises` for Exceptions:**  The code now effectively uses `pytest.raises` to check for expected exceptions, such as `ValueError` when an invalid campaign is passed.


6. **Realistic File Handling (partial):** The `mock_files` fixture simulates different JSON file contents, which is very important for testing different cases. You need to expand this based on your actual data structure.


7. **`while True` loop:**  The `while True` loop is difficult to mock directly, but the tests are now more focused on testing `run_campaigns`'s correct logic, which is what you can and should test in a mock environment.  The `KeyboardInterrupt` is not testable with mocks, but you will need a test that simulates the loop for real-world scenarios.


**How to Run:**

1.  Make sure you have `pytest` installed (`pip install pytest`).
2.  Save the test code and the mocked `facebook.py` example code in a folder together.
3.  Run `pytest` in your terminal from the directory containing the test file.

**Critical Next Steps:**

- **Real File Handling (Crucial):**  Instead of the mocked `_mock_json_read`, implement a mechanism to read the actual data from your input JSON files. This will make the tests much more realistic.  
- **Complete the `test_run_campaigns_valid_input` assertions** to verify that the internal calls within `run_campaigns` are behaving as expected.
- **Testing with `KeyboardInterrupt`:**  Handle the `KeyboardInterrupt` case separately with an integration test (not a mock test). Create a test case to simulate `KeyboardInterrupt` and ensure the cleanup mechanism (if any) is working correctly.
- **Testing Data Structure:** Add tests to verify that the data is being parsed correctly from your JSON files.


This revised solution provides a solid foundation for testing `FacebookPromoter`. Remember to adapt the assertions to match your actual code's logic, making them complete and rigorous.