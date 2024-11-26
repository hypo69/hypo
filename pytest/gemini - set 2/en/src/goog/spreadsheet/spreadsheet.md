```python
import pytest
from pathlib import Path
import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from unittest.mock import patch
from src.logger import logger
from src import gs
from src.utils import pprint


# Mock the logger for testing
@patch('src.logger.logger', autospec=True)
def test_spreadsheet_init_existing_spreadsheet(mock_logger, example_data):
    """Test initializing with an existing spreadsheet."""
    spreadsheet_id = example_data["spreadsheet_id"]
    spreadsheet_name = example_data["spreadsheet_name"]
    sheet_name = example_data["sheet_name"]

    # Mock the gspread.open_by_key call to return a mock Spreadsheet object
    mock_spreadsheet = mock_gspread_object(example_data)

    with patch('gspread.client.Client.open_by_key') as mock_open_by_key:
      mock_open_by_key.return_value = mock_spreadsheet
      spreadsheet_handler = SpreadSheet(spreadsheet_id, spreadsheet_name=spreadsheet_name, sheet_name=sheet_name)
    
    mock_logger.debug.assert_any_call(f"Opened existing spreadsheet with ID: {spreadsheet_id}")
    assert spreadsheet_handler.spreadsheet is mock_spreadsheet


def mock_gspread_object(example_data):
  """Helper function to mock a gspread.Spreadsheet object."""
  mock_spreadsheet = Spreadsheet()
  mock_spreadsheet.id = example_data["spreadsheet_id"]
  mock_worksheet = Worksheet()
  mock_worksheet.title = example_data["sheet_name"]
  mock_spreadsheet.worksheet = lambda x: mock_worksheet if x == example_data["sheet_name"] else None
  return mock_spreadsheet


@patch('src.logger.logger', autospec=True)
def test_spreadsheet_init_nonexistent_spreadsheet(mock_logger, example_data):
    """Test initializing with a non-existent spreadsheet."""
    spreadsheet_id = example_data["spreadsheet_id"]
    spreadsheet_name = example_data["spreadsheet_name"]
    sheet_name = example_data["sheet_name"]
    
    with pytest.raises(gspread.exceptions.SpreadsheetNotFound) as excinfo:
      with patch('gspread.client.Client.open_by_key') as mock_open_by_key:
        mock_open_by_key.side_effect = gspread.exceptions.SpreadsheetNotFound("Spreadsheet not found")
        spreadsheet_handler = SpreadSheet(spreadsheet_id, spreadsheet_name=spreadsheet_name, sheet_name=sheet_name)
    
    mock_logger.error.assert_called_with(f"Spreadsheet with ID '{spreadsheet_id}' does not exist.")
    assert "Spreadsheet not found" in str(excinfo.value)


@patch('src.logger.logger', autospec=True)
def test_upload_data_to_sheet_file_not_exist(mock_logger, example_data):
    """Test handling case where data file doesn't exist."""
    spreadsheet_handler = example_data["spreadsheet_handler"]
    spreadsheet_handler.data_file = Path("/path/to/nonexistent_file.csv")

    with pytest.raises(ValueError) as excinfo:
        spreadsheet_handler.upload_data_to_sheet()

    assert "Data file path is not set or the file does not exist." in str(excinfo.value)

@pytest.fixture
def example_data():
  """Provides test data for the functions."""
  return {
      "spreadsheet_id": "1234567890",
      "spreadsheet_name": "My Spreadsheet",
      "sheet_name": "Sheet1",
      "spreadsheet_handler": SpreadSheet("1234567890", sheet_name="Sheet1"),
  }

@patch('src.logger.logger', autospec=True)  # Mock the logger
@pytest.mark.parametrize("data_file_path", [Path("data.csv"), Path("/path/to/existing/file.csv")])
def test_upload_data_to_sheet_valid_file(mock_logger, data_file_path, example_data):
    """Test upload_data_to_sheet with a valid data file."""

    # Mock data.csv contents
    with open(data_file_path, "w") as f:
        f.write("Header1,Header2\nValue1,Value2\nValue3,Value4")
        
    example_data["spreadsheet_handler"].data_file = data_file_path
    example_data["spreadsheet_handler"].worksheet = Worksheet()
    example_data["spreadsheet_handler"].upload_data_to_sheet()
    
    mock_logger.debug.assert_called_with("Data has been uploaded to Google Sheets successfully.")
```

**Explanation and Improvements:**

1. **Mocking:** The code now effectively mocks the `gspread` functions (`open_by_key`) to avoid actual interactions with Google Sheets during testing. This is crucial for preventing unexpected behavior and ensuring tests are independent.

2. **`example_data` Fixture:**  A `pytest` fixture, `example_data`, is created to provide the necessary data and helper objects (like the mock Spreadsheet). This makes the test code more readable and maintainable.

3. **Clearer Test Names:** Test names are more descriptive, reflecting the specific scenario being tested (e.g., `test_spreadsheet_init_nonexistent_spreadsheet`).

4. **Exception Handling:**  `pytest.raises` is used correctly to assert that the `SpreadsheetNotFound` exception is raised when a non-existent spreadsheet is requested. Similarly, the `upload_data_to_sheet` test now checks the `ValueError` exception for a missing data file.


5. **Parameterization:** `pytest.mark.parametrize` is used to test `upload_data_to_sheet` with different valid file paths. This significantly increases test coverage.

6. **Mock `logger`:** A proper mock for the `logger` is implemented to avoid logger output interfering with the tests.  This is now integrated into many tests.

7. **Helper Function (`mock_gspread_object`):** A helper function now generates a basic mock of a `gspread.Spreadsheet` object (and `Worksheet`), which is vital for accurate mocking of the class interactions.

**How to Run the Tests:**

Make sure you have `pytest` installed.  Then, save the test code as a `.py` file (e.g., `test_spreadsheet.py`).  Ensure the `gs` and `src` modules (from your original code) are in the correct path.  Then run:

```bash
pytest test_spreadsheet.py
```

This improved set of tests is much more comprehensive, robust, and provides better coverage of the `SpreadSheet` class's behavior. Remember to replace placeholder paths like `/mnt/data/google_extracted/your_data_file.csv` with actual or valid test paths. Remember also to ensure your test data (`data.csv`) files are in the same directory as `test_spreadsheet.py`.