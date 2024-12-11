```python
import pytest
from unittest.mock import Mock
from goog.spreadsheet.bberyakov.grender import GSRender, CellFormat, Color, TextFormat, ConditionalFormatRule, BooleanRule, BooleanCondition, GridRange
from spread import Spreadsheet, Worksheet

# Mock objects for testing
@pytest.fixture
def mock_worksheet():
    """Provides a mock Worksheet object."""
    mock_ws = Mock(spec=Worksheet)
    mock_ws.id = 123  # Example sheet ID
    mock_ws.get_all_values.return_value = [[]]
    mock_ws.col_values.return_value = []
    mock_ws.append_row.return_value = None
    mock_ws.merge_cells.return_value = None
    return mock_ws


@pytest.fixture
def mock_spreadsheet():
    """Provides a mock Spreadsheet object."""
    mock_sh = Mock(spec=Spreadsheet)
    mock_sh.batch_update.return_value = None
    return mock_sh


def test_render_header_valid_input(mock_worksheet):
    """Tests render_header with valid input and formatting."""
    renderer = GSRender()
    renderer.render_header(mock_worksheet, "Test Header", range="A1:Z1")
    mock_worksheet.append_row.assert_called_once()
    mock_worksheet.merge_cells.assert_called_once()
    mock_worksheet.merge_cells.assert_called_with("A1:Z1", "MERGE_ALL")


def test_render_header_invalid_range(mock_worksheet):
    """Tests render_header with an invalid range."""
    renderer = GSRender()
    with pytest.raises(ValueError, match="Invalid range"):
        renderer.render_header(mock_worksheet, "Test Header", range="A1:B")  # Invalid range


def test_merge_range_valid_input(mock_worksheet):
    """Tests merge_range with valid input."""
    renderer = GSRender()
    renderer.merge_range(mock_worksheet, "A1:Z1", "MERGE_ALL")
    mock_worksheet.merge_cells.assert_called_once_with("A1:Z1", "MERGE_ALL")


def test_merge_range_invalid_merge_type(mock_worksheet):
    """Tests merge_range with an invalid merge type."""
    renderer = GSRender()
    with pytest.raises(ValueError, match="Invalid merge type"):
        renderer.merge_range(mock_worksheet, "A1:Z1", "INVALID_MERGE")


def test_set_worksheet_direction_valid_input(mock_spreadsheet, mock_worksheet):
    """Tests set_worksheet_direction with valid input."""
    renderer = GSRender()
    renderer.set_worksheet_direction(mock_spreadsheet, mock_worksheet, "ltr")
    mock_spreadsheet.batch_update.assert_called_once()


def test_header_valid_input(mock_worksheet):
    """Tests header with a valid list input."""
    renderer = GSRender()
    renderer.header(mock_worksheet, ["Header 1", "Header 2"], row=2)
    mock_worksheet.append_row.assert_called_once()

def test_header_invalid_input_type(mock_worksheet):
    """Tests header with invalid input type."""
    renderer = GSRender()
    with pytest.raises(TypeError, match="ws_header must be a str or list"):
        renderer.header(mock_worksheet, 123)


def test_get_first_empty_row_empty_worksheet(mock_worksheet):
    """Tests get_first_empty_row with an empty worksheet."""
    renderer = GSRender()
    mock_worksheet.get_all_values.return_value = []
    result = renderer.get_first_empty_row(mock_worksheet)
    assert result == 1

def test_get_first_empty_row_non_empty_worksheet(mock_worksheet):
    """Tests get_first_empty_row with a non-empty worksheet."""
    renderer = GSRender()
    mock_worksheet.get_all_values.return_value = [["a", "b"], ["c", "d"]]
    result = renderer.get_first_empty_row(mock_worksheet)
    assert result == 3


# Add more test cases for other methods as needed, covering various scenarios
# ... (add tests for other methods) ...
```

**Explanation and Improvements:**

- **Mocking:** Uses `unittest.mock.Mock` to create mock objects for `Worksheet` and `Spreadsheet`. This isolates the tests from the actual Google Sheets API and allows for controlled input.  Critically, mock methods are now asserted upon.
- **Clearer Error Handling:**  Uses `pytest.raises` for exception testing with helpful error messages.
- **Edge Case Testing:**  The `test_get_first_empty_row` cases explicitly test both empty and non-empty worksheet scenarios.
- **Type Handling:** The `test_header_invalid_input_type` test case demonStartes how to check for incorrect data types.
- **Comprehensive Tests:**  The tests are designed to be more comprehensive, now covering more cases for the methods.



**How to Run Tests:**

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Save the test code (e.g., `test_grender.py`) in the same directory as your `grender.py` file.**

3.  **Run the tests:**
    ```bash
    pytest test_grender.py
    ```

Remember to adapt the tests to your specific needs.  The `mock` methods should precisely match what `grender.py` does with the objects to allow for appropriate verification.  Adding test cases for other methods is also a critical step in thorough testing.