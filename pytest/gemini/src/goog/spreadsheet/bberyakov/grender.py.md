```python
import pytest
from unittest.mock import MagicMock, patch
from spread import Worksheet, Spreadsheet
from src.goog.spreadsheet.bberyakov.grender import GSRender, CellFormat, Color, TextFormat, ConditionalFormatRule, BooleanRule, BooleanCondition, GridRange
from spread_formatting import set_row_height, format_cell_range

@pytest.fixture
def mock_worksheet():
    """Provides a mock Worksheet object for testing."""
    mock_ws = MagicMock(spec=Worksheet)
    mock_ws.id = 123
    return mock_ws

@pytest.fixture
def mock_spreadsheet():
    """Provides a mock Spreadsheet object for testing."""
    mock_sh = MagicMock(spec=Spreadsheet)
    return mock_sh

@pytest.fixture
def gs_render():
    """Provides an instance of GSRender for testing."""
    return GSRender()

def test_gsrender_init(gs_render):
    """Checks if GSRender initializes without errors."""
    assert isinstance(gs_render, GSRender)
    # Additional assertions can be added based on the class's __init__ method,
    # for example, if it initializes internal properties or uses passed parameters.

def test_render_header_valid_input(gs_render, mock_worksheet):
    """Checks correct header rendering with valid input."""
    gs_render.render_header(mock_worksheet, "Test Header")
    mock_worksheet.merge_cells.assert_called_once()
    format_cell_range.assert_called_once()
    set_row_height.assert_called_once()

def test_render_header_with_custom_range(gs_render, mock_worksheet):
    """Checks header rendering with a custom range."""
    gs_render.render_header(mock_worksheet, "Custom Header", range="B2:D2")
    mock_worksheet.merge_cells.assert_called_once_with("B2:D2", 'MERGE_ALL')
    format_cell_range.assert_called_once()
    set_row_height.assert_called_once()

def test_render_header_with_merge_type(gs_render, mock_worksheet):
     """Checks header rendering with a specified merge type."""
     gs_render.render_header(mock_worksheet, "Header", merge_type='MERGE_COLUMNS')
     mock_worksheet.merge_cells.assert_called_once_with('A1:Z1', 'MERGE_COLUMNS')
     format_cell_range.assert_called_once()
     set_row_height.assert_called_once()

def test_merge_range_valid_input(gs_render, mock_worksheet):
    """Checks correct merging of cell range."""
    gs_render.merge_range(mock_worksheet, "A1:B2")
    mock_worksheet.merge_cells.assert_called_once_with("A1:B2", 'MERGE_ALL')

def test_merge_range_with_merge_type(gs_render, mock_worksheet):
    """Checks cell merging with a specific merge type."""
    gs_render.merge_range(mock_worksheet, "C3:D4", merge_type="MERGE_ROWS")
    mock_worksheet.merge_cells.assert_called_once_with("C3:D4", "MERGE_ROWS")


def test_set_worksheet_direction_rtl(gs_render, mock_spreadsheet, mock_worksheet):
    """Checks worksheet direction setting to RTL."""
    gs_render.set_worksheet_direction(mock_spreadsheet, mock_worksheet, 'rtl')
    mock_spreadsheet.batch_update.assert_called_once()
    
    #Get the call arguments and make sure that it's true
    args, kwarfs = mock_spreadsheet.batch_update.call_args
    assert args[0]["requests"][0]["updateSheetProperties"]["properties"]["rightToLeft"] == True
    
    #Get the sheet ID
    assert args[0]["requests"][0]["updateSheetProperties"]["properties"]["sheetId"] == 123

def test_set_worksheet_direction_ltr(gs_render, mock_spreadsheet, mock_worksheet):
    """Checks worksheet direction setting to LTR."""
    gs_render.set_worksheet_direction(mock_spreadsheet, mock_worksheet, 'ltr')
    mock_spreadsheet.batch_update.assert_called_once()

    #Get the call arguments and make sure that it's false
    args, kwarfs = mock_spreadsheet.batch_update.call_args
    assert args[0]["requests"][0]["updateSheetProperties"]["properties"]["rightToLeft"] == True
    
     #Get the sheet ID
    assert args[0]["requests"][0]["updateSheetProperties"]["properties"]["sheetId"] == 123

def test_header_str_input(gs_render, mock_worksheet):
    """Checks header creation with a string input."""
    mock_worksheet.col_values.return_value = []
    gs_render.header(mock_worksheet, "Single Header")
    mock_worksheet.append_row.assert_called_once_with(values = ["Single Header"], table_range = 'A1')
    mock_worksheet.merge_cells.assert_called()
    format_cell_range.assert_called_once()

def test_header_list_input(gs_render, mock_worksheet):
    """Checks header creation with a list input."""
    mock_worksheet.col_values.return_value = []
    gs_render.header(mock_worksheet, ["Header 1", "Header 2"])
    mock_worksheet.append_row.assert_called_once_with(values = ["Header 1", "Header 2"], table_range = 'A1')
    mock_worksheet.merge_cells.assert_called()
    format_cell_range.assert_called_once()

def test_header_with_row(gs_render, mock_worksheet):
    """Checks header creation with a specified row."""
    mock_worksheet.col_values.return_value = []
    gs_render.header(mock_worksheet, "Row Header", row=3)
    mock_worksheet.append_row.assert_called_once_with(values = ["Row Header"], table_range = 'A3')
    mock_worksheet.merge_cells.assert_called()
    format_cell_range.assert_called_once()

def test_write_category_title_str_input(gs_render, mock_worksheet):
    """Checks writing category title with a string input."""
    gs_render.write_category_title(mock_worksheet, "Category Title", row=2)
    mock_worksheet.append_row.assert_called_once_with(values = ["Category Title"], table_range = 'B2')
    mock_worksheet.merge_cells.assert_called_once_with('B2:E2', 'MERGE_ALL')

def test_write_category_title_list_input(gs_render, mock_worksheet):
    """Checks writing category title with a list input."""
    gs_render.write_category_title(mock_worksheet, ["Cat 1", "Cat 2"], row=4)
    mock_worksheet.append_row.assert_called_once_with(values = ["Cat 1", "Cat 2"], table_range = 'B4')
    mock_worksheet.merge_cells.assert_called_once_with('B4:E4', 'MERGE_ALL')

def test_get_first_empty_row_empty_sheet(gs_render, mock_worksheet):
    """Checks getting the first empty row in an empty sheet."""
    mock_worksheet.col_values.return_value = []
    assert gs_render.get_first_empty_row(mock_worksheet) == 1
    mock_worksheet.get_all_values.assert_called_once()

def test_get_first_empty_row_with_data(gs_render, mock_worksheet):
    """Checks getting the first empty row in a sheet with data."""
    mock_worksheet.col_values.return_value = ["data1", "data2", "data3"]
    assert gs_render.get_first_empty_row(mock_worksheet, by_col=1) == 4
    mock_worksheet.col_values.assert_called_once_with(1)
```