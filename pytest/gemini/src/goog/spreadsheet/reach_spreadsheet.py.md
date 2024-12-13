```python
import pytest
import httplib2
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from unittest.mock import MagicMock, patch
from hypotez.src.goog.spreadsheet.reach_spreadsheet import ReachSpreadsheet, SpreadsheetError, SpreadsheetNotSetError, SheetNotSetError, htmlColorToJSON
import json


# Fixture for a mock service account credentials object
@pytest.fixture
def mock_credentials():
    mock_cred = MagicMock(spec=ServiceAccountCredentials)
    mock_cred.authorize.return_value = MagicMock(spec=httplib2.Http)
    return mock_cred


# Fixture for a mock googleapiclient service
@pytest.fixture
def mock_service():
    mock_service = MagicMock()
    return mock_service

@pytest.fixture
def mock_drive_service():
    mock_drive_service = MagicMock()
    return mock_drive_service

# Fixture for a ReachSpreadsheet instance with mocked service
@pytest.fixture
def reach_spreadsheet_instance(mock_credentials, mock_service, mock_drive_service):
    with patch('hypotez.src.goog.spreadsheet.reach_spreadsheet.ServiceAccountCredentials.from_json_keyfile_name', return_value=mock_credentials):
        with patch('hypotez.src.goog.spreadsheet.reach_spreadsheet.googleapiclient.discovery.build', side_effect=[mock_service, mock_drive_service]):
            spreadsheet = ReachSpreadsheet(debugMode=True)
            spreadsheet.service = mock_service
            spreadsheet.driveService = mock_drive_service
            return spreadsheet



def test_htmlColorToJSON_valid_hex():
    """Test htmlColorToJSON with a valid hex color code."""
    assert htmlColorToJSON("#FF0000") == {"red": 1.0, "green": 0.0, "blue": 0.0}
    assert htmlColorToJSON("#00FF00") == {"red": 0.0, "green": 1.0, "blue": 0.0}
    assert htmlColorToJSON("#0000FF") == {"red": 0.0, "green": 0.0, "blue": 1.0}
    assert htmlColorToJSON("#FFFFFF") == {"red": 1.0, "green": 1.0, "blue": 1.0}
    assert htmlColorToJSON("#000000") == {"red": 0.0, "green": 0.0, "blue": 0.0}
    assert htmlColorToJSON("FF0000") == {"red": 1.0, "green": 0.0, "blue": 0.0}

def test_create_spreadsheet(reach_spreadsheet_instance):
    """Test creating a new spreadsheet."""
    mock_execute = MagicMock(return_value={'spreadsheetId': 'test_id', 'sheets': [{'properties': {'sheetId': 123, 'title': 'test_sheet'}}]})
    reach_spreadsheet_instance.service.spreadsheets().create().execute = mock_execute
    reach_spreadsheet_instance.create("Test Title", "Test Sheet")
    assert reach_spreadsheet_instance.spreadsheetId == 'test_id'
    assert reach_spreadsheet_instance.sheetId == 123
    assert reach_spreadsheet_instance.sheetTitle == 'test_sheet'

def test_create_spreadsheet_debug_mode(reach_spreadsheet_instance, capsys):
    """Test creating a new spreadsheet with debug mode enabled."""
    mock_execute = MagicMock(return_value={'spreadsheetId': 'test_id', 'sheets': [{'properties': {'sheetId': 123, 'title': 'test_sheet'}}]})
    reach_spreadsheet_instance.service.spreadsheets().create().execute = mock_execute
    reach_spreadsheet_instance.create("Test Title", "Test Sheet")
    captured = capsys.readouterr()
    assert "spreadsheetId" in captured.out


def test_share_spreadsheet_no_id(reach_spreadsheet_instance):
    """Test sharing a spreadsheet when spreadsheetId is not set."""
    reach_spreadsheet_instance.spreadsheetId = None
    with pytest.raises(SpreadsheetNotSetError):
        reach_spreadsheet_instance.share({"type": "user", "role": "reader", "emailAddress": "test@example.com"})

def test_share_spreadsheet(reach_spreadsheet_instance):
    """Test sharing a spreadsheet with valid input."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value={'id': 'permission_id'})
    reach_spreadsheet_instance.driveService.permissions().create().execute = mock_execute
    reach_spreadsheet_instance.share({"type": "user", "role": "reader", "emailAddress": "test@example.com"})
    reach_spreadsheet_instance.driveService.permissions().create.assert_called_once()

def test_share_spreadsheet_debug_mode(reach_spreadsheet_instance, capsys):
    """Test sharing a spreadsheet with debug mode enabled."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value={'id': 'permission_id'})
    reach_spreadsheet_instance.driveService.permissions().create().execute = mock_execute
    reach_spreadsheet_instance.share({"type": "user", "role": "reader", "emailAddress": "test@example.com"})
    captured = capsys.readouterr()
    assert "id" in captured.out

def test_share_with_email_for_reading(reach_spreadsheet_instance):
    """Test sharing a spreadsheet with email for reading."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value={'id': 'permission_id'})
    reach_spreadsheet_instance.driveService.permissions().create().execute = mock_execute
    reach_spreadsheet_instance.shareWithEmailForReading("test@example.com")
    reach_spreadsheet_instance.driveService.permissions().create.assert_called_once()


def test_share_with_email_for_writing(reach_spreadsheet_instance):
    """Test sharing a spreadsheet with email for writing."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value={'id': 'permission_id'})
    reach_spreadsheet_instance.driveService.permissions().create().execute = mock_execute
    reach_spreadsheet_instance.shareWithEmailForWriting("test@example.com")
    reach_spreadsheet_instance.driveService.permissions().create.assert_called_once()


def test_share_with_anybody_for_reading(reach_spreadsheet_instance):
    """Test sharing a spreadsheet with anybody for reading."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value={'id': 'permission_id'})
    reach_spreadsheet_instance.driveService.permissions().create().execute = mock_execute
    reach_spreadsheet_instance.shareWithAnybodyForReading()
    reach_spreadsheet_instance.driveService.permissions().create.assert_called_once()

def test_share_with_anybody_for_writing(reach_spreadsheet_instance):
    """Test sharing a spreadsheet with anybody for writing."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value={'id': 'permission_id'})
    reach_spreadsheet_instance.driveService.permissions().create().execute = mock_execute
    reach_spreadsheet_instance.shareWithAnybodyForWriting()
    reach_spreadsheet_instance.driveService.permissions().create.assert_called_once()


def test_get_sheet_url_no_spreadsheet_id(reach_spreadsheet_instance):
    """Test getting sheet URL when spreadsheetId is not set."""
    reach_spreadsheet_instance.spreadsheetId = None
    with pytest.raises(SpreadsheetNotSetError):
        reach_spreadsheet_instance.getSheetURL()


def test_get_sheet_url_no_sheet_id(reach_spreadsheet_instance):
    """Test getting sheet URL when sheetId is not set."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.sheetId = None
    with pytest.raises(SheetNotSetError):
         reach_spreadsheet_instance.getSheetURL()


def test_get_sheet_url_valid(reach_spreadsheet_instance):
    """Test getting sheet URL with valid IDs."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.sheetId = 123
    expected_url = 'https://docs.google.com/spreadsheets/d/test_id/edit#gid=123'
    assert reach_spreadsheet_instance.getSheetURL() == expected_url


def test_set_spreadsheet_by_id(reach_spreadsheet_instance):
    """Test setting spreadsheet by ID."""
    mock_execute = MagicMock(return_value={'spreadsheetId': 'test_id', 'sheets': [{'properties': {'sheetId': 123, 'title': 'test_sheet'}}]})
    reach_spreadsheet_instance.service.spreadsheets().get().execute = mock_execute
    reach_spreadsheet_instance.setSpreadsheetById('test_id')
    assert reach_spreadsheet_instance.spreadsheetId == 'test_id'
    assert reach_spreadsheet_instance.sheetId == 123
    assert reach_spreadsheet_instance.sheetTitle == 'test_sheet'

def test_set_spreadsheet_by_id_debug_mode(reach_spreadsheet_instance, capsys):
    """Test setting spreadsheet by ID with debug mode enabled."""
    mock_execute = MagicMock(return_value={'spreadsheetId': 'test_id', 'sheets': [{'properties': {'sheetId': 123, 'title': 'test_sheet'}}]})
    reach_spreadsheet_instance.service.spreadsheets().get().execute = mock_execute
    reach_spreadsheet_instance.setSpreadsheetById('test_id')
    captured = capsys.readouterr()
    assert "spreadsheetId" in captured.out

def test_run_prepared_no_spreadsheet_id(reach_spreadsheet_instance):
    """Test runPrepared when spreadsheetId is not set."""
    reach_spreadsheet_instance.spreadsheetId = None
    with pytest.raises(SpreadsheetNotSetError):
        reach_spreadsheet_instance.runPrepared()


def test_run_prepared_no_requests_or_values(reach_spreadsheet_instance):
    """Test runPrepared with no requests or valueRanges."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    replies, responses = reach_spreadsheet_instance.runPrepared()
    assert replies == []
    assert responses == []


def test_run_prepared_with_requests(reach_spreadsheet_instance):
    """Test runPrepared with requests."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.requests = [{"addSheet": {"properties": {"title": "new_sheet"}}}]
    mock_execute = MagicMock(return_value={'replies': ['reply']})
    reach_spreadsheet_instance.service.spreadsheets().batchUpdate().execute = mock_execute
    replies, responses = reach_spreadsheet_instance.runPrepared()
    assert replies == ['reply']
    assert responses == []
    assert reach_spreadsheet_instance.requests == []
    assert reach_spreadsheet_instance.valueRanges == []


def test_run_prepared_with_value_ranges(reach_spreadsheet_instance):
    """Test runPrepared with valueRanges."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.valueRanges = [{"range": "A1:B2", "values": [[1, 2], [3, 4]]}]
    mock_execute = MagicMock(return_value={'responses': ['response']})
    reach_spreadsheet_instance.service.spreadsheets().values().batchUpdate().execute = mock_execute
    replies, responses = reach_spreadsheet_instance.runPrepared()
    assert replies == []
    assert responses == ['response']
    assert reach_spreadsheet_instance.requests == []
    assert reach_spreadsheet_instance.valueRanges == []


def test_run_prepared_with_requests_and_values(reach_spreadsheet_instance):
    """Test runPrepared with requests and valueRanges."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.requests = [{"addSheet": {"properties": {"title": "new_sheet"}}}]
    reach_spreadsheet_instance.valueRanges = [{"range": "A1:B2", "values": [[1, 2], [3, 4]]}]
    mock_execute1 = MagicMock(return_value={'replies': ['reply']})
    mock_execute2 = MagicMock(return_value={'responses': ['response']})
    reach_spreadsheet_instance.service.spreadsheets().batchUpdate().execute = mock_execute1
    reach_spreadsheet_instance.service.spreadsheets().values().batchUpdate().execute = mock_execute2
    replies, responses = reach_spreadsheet_instance.runPrepared()
    assert replies == ['reply']
    assert responses == ['response']
    assert reach_spreadsheet_instance.requests == []
    assert reach_spreadsheet_instance.valueRanges == []

def test_run_prepared_with_requests_debug_mode(reach_spreadsheet_instance, capsys):
    """Test runPrepared with requests and debug mode enabled."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.requests = [{"addSheet": {"properties": {"title": "new_sheet"}}}]
    mock_execute = MagicMock(return_value={'replies': ['reply']})
    reach_spreadsheet_instance.service.spreadsheets().batchUpdate().execute = mock_execute
    reach_spreadsheet_instance.runPrepared()
    captured = capsys.readouterr()
    assert "replies" in captured.out

def test_run_prepared_with_values_debug_mode(reach_spreadsheet_instance, capsys):
    """Test runPrepared with values and debug mode enabled."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    reach_spreadsheet_instance.valueRanges = [{"range": "A1:B2", "values": [[1, 2], [3, 4]]}]
    mock_execute = MagicMock(return_value={'responses': ['response']})
    reach_spreadsheet_instance.service.spreadsheets().values().batchUpdate().execute = mock_execute
    reach_spreadsheet_instance.runPrepared()
    captured = capsys.readouterr()
    assert "responses" in captured.out

def test_prepare_add_sheet(reach_spreadsheet_instance):
    """Test preparing to add a sheet."""
    reach_spreadsheet_instance.prepare_addSheet("New Sheet", 500, 10)
    assert reach_spreadsheet_instance.requests == [{"addSheet": {"properties": {"title": "New Sheet", 'gridProperties': {'rowCount': 500, 'columnCount': 10}}}}]

def test_add_sheet_no_spreadsheet_id(reach_spreadsheet_instance):
    """Test adding sheet when spreadsheetId is not set."""
    reach_spreadsheet_instance.spreadsheetId = None
    with pytest.raises(SpreadsheetNotSetError):
        reach_spreadsheet_instance.addSheet("New Sheet")

def test_add_sheet_valid(reach_spreadsheet_instance):
    """Test adding a sheet with valid input."""
    reach_spreadsheet_instance.spreadsheetId = 'test_id'
    mock_execute = MagicMock(return_value=({'replies': [{'addSheet': {'properties': {'sheetId': 456, 'title': 'New Sheet'}}}]}))
    reach_spreadsheet_instance.service.spreadsheets().batchUpdate().execute = mock_execute
    sheet_id = reach_spreadsheet_instance.addSheet("New Sheet")
    assert sheet_id == 456
    assert reach_spreadsheet_instance.sheetId == 456
    assert reach_spreadsheet_instance.sheetTitle == 'New Sheet'


def test_to_grid_range_no_sheet_id(reach_spreadsheet_instance):
    """Test toGridRange when sheetId is not set."""
    reach_spreadsheet_instance.sheetId = None
    with pytest.raises(SheetNotSetError):
        reach_spreadsheet_instance.toGridRange("A1:B2")

def test_to_grid_range_valid_with_row_and_col(reach_spreadsheet_instance):
    """Test toGridRange with a valid range including row and column."""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange("A3:B4")
    assert grid_range == {"sheetId": 123, "startRowIndex": 2, "endRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2}


def test_to_grid_range_valid_with_row(reach_spreadsheet_instance):
    """Test toGridRange with a valid range including only row."""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange("A5:B")
    assert grid_range == {"sheetId": 123, "startRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2}


def test_to_grid_range_valid_with_col(reach_spreadsheet_instance):
    """Test toGridRange with a valid range including only column."""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange("A:B")
    assert grid_range == {"sheetId": 123, "startColumnIndex": 0, "endColumnIndex": 2}

def test_to_grid_range_valid_with_col_2_chars(reach_spreadsheet_instance):
    """Test toGridRange with a valid range including only column with 2 chars."""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange("AA1:AB2")
    assert grid_range == {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 26, "endColumnIndex": 28}

def test_to_grid_range_valid_with_col_2_chars_and_row(reach_spreadsheet_instance):
    """Test toGridRange with a valid range including column with 2 chars and only row."""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange("AA1:AB")
    assert grid_range == {"sheetId": 123, "startRowIndex": 0, "startColumnIndex": 26, "endColumnIndex": 28}

def test_to_grid_range_valid_with_col_2_chars_and_col(reach_spreadsheet_instance):
    """Test toGridRange with a valid range including column with 2 chars and only column."""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange("AA:AB")
    assert grid_range == {"sheetId": 123, "startColumnIndex": 26, "endColumnIndex": 28}

def test_to_grid_range_already_gridrange(reach_spreadsheet_instance):
    """Test toGridRange with a valid GridRange"""
    reach_spreadsheet_instance.sheetId = 123
    grid_range = reach_spreadsheet_instance.toGridRange({"startRowIndex": 2, "endRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2})
    assert grid_range == {"sheetId": 123, "startRowIndex": 2, "endRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2}

def test_prepare_set_dimension_pixel_size_no_sheet_id(reach_spreadsheet_instance):
    """Test prepare_setDimensionPixelSize when sheetId is not set."""
    reach_spreadsheet_instance.sheetId = None
    with pytest.raises(SheetNotSetError):
        reach_spreadsheet_instance.prepare_setDimensionPixelSize("COLUMNS", 0, 2, 100)


def test_prepare_set_dimension_pixel_size_valid(reach_spreadsheet_instance):
    """Test prepare_setDimensionPixelSize with valid input."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setDimensionPixelSize("COLUMNS", 0, 2, 100)
    expected_request = {
        "updateDimensionProperties": {
            "range": {
                "sheetId": 123,
                "dimension": "COLUMNS",
                "startIndex": 0,
                "endIndex": 2
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    }
    assert reach_spreadsheet_instance.requests == [expected_request]


def test_prepare_set_columns_width(reach_spreadsheet_instance):
    """Test prepare_setColumnsWidth."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setColumnsWidth(0, 2, 100)
    expected_request = {
        "updateDimensionProperties": {
            "range": {
                "sheetId": 123,
                "dimension": "COLUMNS",
                "startIndex": 0,
                "endIndex": 3
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    }
    assert reach_spreadsheet_instance.requests == [expected_request]

def test_prepare_set_column_width(reach_spreadsheet_instance):
    """Test prepare_setColumnWidth."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setColumnWidth(1, 100)
    expected_request = {
        "updateDimensionProperties": {
            "range": {
                "sheetId": 123,
                "dimension": "COLUMNS",
                "startIndex": 1,
                "endIndex": 2
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    }
    assert reach_spreadsheet_instance.requests == [expected_request]


def test_prepare_set_rows_height(reach_spreadsheet_instance):
    """Test prepare_setRowsHeight."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setRowsHeight(0, 2, 100)
    expected_request = {
        "updateDimensionProperties": {
            "range": {
                "sheetId": 123,
                "dimension": "ROWS",
                "startIndex": 0,
                "endIndex": 3
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    }
    assert reach_spreadsheet_instance.requests == [expected_request]


def test_prepare_set_row_height(reach_spreadsheet_instance):
    """Test prepare_setRowHeight."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setRowHeight(1, 100)
    expected_request = {
        "updateDimensionProperties": {
            "range": {
                "sheetId": 123,
                "dimension": "ROWS",
                "startIndex": 1,
                "endIndex": 2
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    }
    assert reach_spreadsheet_instance.requests == [expected_request]

def test_prepare_set_values_no_sheet_title(reach_spreadsheet_instance):
    """Test prepare_setValues when sheetTitle is not set."""
    reach_spreadsheet_instance.sheetTitle = None
    with pytest.raises(SheetNotSetError):
        reach_spreadsheet_instance.prepare_setValues("A1:B2", [[1, 2], [3, 4]])

def test_prepare_set_values_valid(reach_spreadsheet_instance):
    """Test prepare_setValues with valid input."""
    reach_spreadsheet_instance.sheetTitle = 'test_sheet'
    reach_spreadsheet_instance.prepare_setValues("A1:B2", [[1, 2], [3, 4]], "ROWS")
    expected_value_range = {"range": "test_sheet!A1:B2", "majorDimension": "ROWS", "values": [[1, 2], [3, 4]]}
    assert reach_spreadsheet_instance.valueRanges == [expected_value_range]

def test_prepare_set_values_default_major_dimension(reach_spreadsheet_instance):
    """Test prepare_setValues with default majorDimension."""
    reach_spreadsheet_instance.sheetTitle = 'test_sheet'
    reach_spreadsheet_instance.prepare_setValues("A1:B2", [[1, 2], [3, 4]])
    expected_value_range = {"range": "test_sheet!A1:B2", "majorDimension": "ROWS", "values": [[1, 2], [3, 4]]}
    assert reach_spreadsheet_instance.valueRanges == [expected_value_range]


def test_prepare_merge_cells(reach_spreadsheet_instance):
    """Test prepare_mergeCells."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_mergeCells("A1:B2", "MERGE_COLUMNS")
    expected_request = {"mergeCells": {"range": {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 2}, "mergeType": "MERGE_COLUMNS"}}
    assert reach_spreadsheet_instance.requests == [expected_request]

def test_prepare_merge_cells_default_type(reach_spreadsheet_instance):
    """Test prepare_mergeCells with default mergeType."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_mergeCells("A1:B2")
    expected_request = {"mergeCells": {"range": {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 2}, "mergeType": "MERGE_ALL"}}
    assert reach_spreadsheet_instance.requests == [expected_request]

def test_prepare_set_cell_string_formatter(reach_spreadsheet_instance):
    """Test prepare_setCellStringFormatterormat."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setCellStringFormatterormat("A1:B2", {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat")
    expected_request = {"repeatCell": {"range": {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 2}, "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}}, "fields": "userEnteredFormat.textFormat"}}
    assert reach_spreadsheet_instance.requests == [expected_request]


def test_prepare_set_cell_string_formatter_default_fields(reach_spreadsheet_instance):
    """Test prepare_setCellStringFormatterormat with default fields."""
    reach_spreadsheet_instance.sheetId = 123
    reach_spreadsheet_instance.prepare_setCellStringFormatterormat("A1:B2", {"textFormat": {"bold": True}})
    expected_request = {"repeatCell": {"range": {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 2}, "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}}, "fields": "userEnteredFormat"}}
    assert reach_spreadsheet_instance.requests == [expected_request]


def test_prepare_set_cell_string_formatters(reach_spreadsheet_instance):
    """Test prepare_setCellStringFormatterormats."""
    reach_spreadsheet_instance.sheetId = 123
    formats = [[{"textFormat": {"bold": True}}, {"textFormat": {"italic": True}}],
               [{"textFormat": {"underline": True}}, {"textFormat": {"strikethrough": True}}]]
    reach_spreadsheet_instance.prepare_setCellStringFormatterormats("A1:B2", formats, "userEnteredFormat.textFormat")
    expected_request = {"updateCells": {"range": {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 2},
                                              "rows": [{"values": [{"userEnteredFormat": cellFormat} for cellFormat in rowFormats]} for rowFormats in formats],
                                              "fields": "userEnteredFormat.textFormat"}}
    assert reach_spreadsheet_instance.requests == [expected_request]

def test_prepare_set_cell_string_formatters_default_fields(reach_spreadsheet_instance):
    """Test prepare_setCellStringFormatterormats with default fields."""
    reach_spreadsheet_instance.sheetId = 123
    formats = [[{"textFormat": {"bold": True}}, {"textFormat": {"italic": True}}],
               [{"textFormat": {"underline": True}}, {"textFormat": {"strikethrough": True}}]]
    reach_spreadsheet_instance.prepare_setCellStringFormatterormats("A1:B2", formats)
    expected_request = {"updateCells": {"range": {"sheetId": 123, "startRowIndex": 0, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 2},
                                              "rows": [{"values": [{"userEnteredFormat": cellFormat} for cellFormat in rowFormats]} for rowFormats in formats],
                                              "fields": "userEnteredFormat"}}
    assert reach_spreadsheet_instance.requests == [expected_request]
```