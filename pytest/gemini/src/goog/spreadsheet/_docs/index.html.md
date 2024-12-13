```python
import pytest
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Fixture to create a mock service object for testing
@pytest.fixture
def mock_service():
    class MockService:
        def __init__(self):
            self.spreadsheets_mock = MockSpreadsheets()
            self.values_mock = MockValues()

        def spreadsheets(self):
            return self.spreadsheets_mock

        def drive_mock(self):
            return MockDrive()

        def values(self):
            return self.values_mock

    class MockValues:
        def batchUpdate(self, spreadsheetId, body):
            return MockBatchUpdateResponse()

    class MockBatchUpdateResponse:
      def execute(self):
        return {'responses': [], 'replies': []}

    class MockSpreadsheets:
        def create(self, body):
            return MockCreateResponse(body)
        def batchUpdate(self, spreadsheetId, body):
          return MockBatchUpdateResponse()

    class MockCreateResponse:
      def __init__(self, body):
        self.body = body
      def execute(self):
        return {
            'properties': {'title': self.body['properties']['title'], 'locale': self.body['properties']['locale']},
            'sheets': self.body['sheets'],
            'spreadsheetId': 'test_spreadsheet_id'
          }

    class MockDrive:
        def permissions(self):
            return MockPermissions()

    class MockPermissions:
        def create(self, fileId, body, fields):
            return MockPermissionsCreateResponse()

    class MockPermissionsCreateResponse:
        def execute(self):
            return {'id': 'test_permission_id'}


    return MockService()

@pytest.fixture
def mock_credentials():
    class MockCredentials:
      def authorize(self, http):
        return http
    return MockCredentials()

# Assuming that Spreadsheet class is in a file named spreadsheet.py
# from src.goog.spreadsheet import spreadsheet
from hypotez.src.goog.spreadsheet._docs.spreadsheet import Spreadsheet  # Import the Spreadsheet class

def test_spreadsheet_creation(mock_service, mock_credentials):
    """Test the spreadsheet creation with valid input."""
    ss = Spreadsheet(mock_service, mock_credentials)
    spreadsheet_id = ss.create(title='Test Spreadsheet', locale='ru_RU')
    assert spreadsheet_id == 'test_spreadsheet_id'

def test_spreadsheet_create_with_empty_title(mock_service, mock_credentials):
    """Test the spreadsheet creation with an empty title."""
    ss = Spreadsheet(mock_service, mock_credentials)
    with pytest.raises(KeyError):
        ss.create(locale='ru_RU')  # Missing title, should raise an error


def test_prepare_set_column_width(mock_service, mock_credentials):
    """Test prepare_setColumnWidth method."""
    ss = Spreadsheet(mock_service, mock_credentials)
    ss.prepare_setColumnWidth(0, 317)
    assert len(ss.requests) == 1
    assert ss.requests[0]['updateDimensionProperties']['range']['startIndex'] == 0
    assert ss.requests[0]['updateDimensionProperties']['range']['endIndex'] == 1
    assert ss.requests[0]['updateDimensionProperties']['properties']['pixelSize'] == 317

def test_prepare_set_columns_width(mock_service, mock_credentials):
    """Test prepare_setColumnsWidth method."""
    ss = Spreadsheet(mock_service, mock_credentials)
    ss.prepare_setColumnsWidth(2, 3, 165)
    assert len(ss.requests) == 1
    assert ss.requests[0]['updateDimensionProperties']['range']['startIndex'] == 2
    assert ss.requests[0]['updateDimensionProperties']['range']['endIndex'] == 4
    assert ss.requests[0]['updateDimensionProperties']['properties']['pixelSize'] == 165

def test_prepare_set_dimension_pixel_size(mock_service, mock_credentials):
  """Test prepare_setDimensionPixelSize method"""
  ss = Spreadsheet(mock_service, mock_credentials)
  ss.prepare_setDimensionPixelSize("COLUMNS", 0, 1, 100)
  assert len(ss.requests) == 1
  assert ss.requests[0]['updateDimensionProperties']['range']['dimension'] == "COLUMNS"
  assert ss.requests[0]['updateDimensionProperties']['range']['startIndex'] == 0
  assert ss.requests[0]['updateDimensionProperties']['range']['endIndex'] == 1
  assert ss.requests[0]['updateDimensionProperties']['properties']['pixelSize'] == 100

def test_prepare_set_values(mock_service, mock_credentials):
    """Test prepare_setValues method."""
    ss = Spreadsheet(mock_service, mock_credentials, sheet_title='Test Sheet')
    ss.prepare_setValues("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])
    assert len(ss.valueRanges) == 1
    assert ss.valueRanges[0]['range'] == "Test Sheet!B2:C3"
    assert ss.valueRanges[0]['values'] == [["This is B2", "This is C2"], ["This is B3", "This is C3"]]


def test_prepare_set_values_with_columns_dimension(mock_service, mock_credentials):
    """Test prepare_setValues method with COLUMNS dimension."""
    ss = Spreadsheet(mock_service, mock_credentials, sheet_title='Test Sheet')
    ss.prepare_setValues("D5:E6", [["This is D5", "This is D6"], ["This is E5", "=5+5"]], majorDimension='COLUMNS')
    assert len(ss.valueRanges) == 1
    assert ss.valueRanges[0]['range'] == "Test Sheet!D5:E6"
    assert ss.valueRanges[0]['majorDimension'] == 'COLUMNS'
    assert ss.valueRanges[0]['values'] == [["This is D5", "This is D6"], ["This is E5", "=5+5"]]


def test_run_prepared_with_no_requests(mock_service, mock_credentials):
  """Test runPrepared method when there are no requests"""
  ss = Spreadsheet(mock_service, mock_credentials)
  replies, responses = ss.runPrepared()
  assert len(replies) == 0
  assert len(responses) == 0
  assert len(ss.requests) == 0
  assert len(ss.valueRanges) == 0

def test_run_prepared_with_requests(mock_service, mock_credentials):
  """Test runPrepared method when there are requests"""
  ss = Spreadsheet(mock_service, mock_credentials)
  ss.prepare_setColumnWidth(0, 100)
  replies, responses = ss.runPrepared()
  assert len(replies) == 0
  assert len(responses) == 0
  assert len(ss.requests) == 0
  assert len(ss.valueRanges) == 0


def test_run_prepared_with_values(mock_service, mock_credentials):
  """Test runPrepared method when there are values"""
  ss = Spreadsheet(mock_service, mock_credentials)
  ss.prepare_setValues("A1", [["test"]])
  replies, responses = ss.runPrepared()
  assert len(replies) == 0
  assert len(responses) == 0
  assert len(ss.requests) == 0
  assert len(ss.valueRanges) == 0


def test_run_prepared_with_requests_and_values(mock_service, mock_credentials):
    """Test runPrepared with requests and values"""
    ss = Spreadsheet(mock_service, mock_credentials, sheet_title='Test Sheet')
    ss.prepare_setColumnWidth(0, 100)
    ss.prepare_setValues("A1", [["test"]])
    replies, responses = ss.runPrepared()
    assert len(replies) == 0
    assert len(responses) == 0
    assert len(ss.requests) == 0
    assert len(ss.valueRanges) == 0



def test_prepare_merge_cells(mock_service, mock_credentials):
    """Test prepare_mergeCells method."""
    ss = Spreadsheet(mock_service, mock_credentials, sheet_title='Test Sheet')
    ss.prepare_mergeCells('A1:E1')
    assert len(ss.requests) == 1
    merge_req = ss.requests[0]['mergeCells']
    assert merge_req['range']['startRowIndex'] == 0
    assert merge_req['range']['endRowIndex'] == 1
    assert merge_req['range']['startColumnIndex'] == 0
    assert merge_req['range']['endColumnIndex'] == 5
    assert merge_req['mergeType'] == 'MERGE_ALL'

def test_prepare_set_cells_format(mock_service, mock_credentials):
    """Test prepare_setCellsFormat method."""
    ss = Spreadsheet(mock_service, mock_credentials, sheet_title='Test Sheet')
    ss.prepare_setCellsFormat('A3:E3', {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
    assert len(ss.requests) == 1
    repeat_req = ss.requests[0]['repeatCell']
    assert repeat_req['range']['startRowIndex'] == 2
    assert repeat_req['range']['endRowIndex'] == 3
    assert repeat_req['range']['startColumnIndex'] == 0
    assert repeat_req['range']['endColumnIndex'] == 5
    assert repeat_req['cell']['userEnteredFormat']['horizontalAlignment'] == 'CENTER'
    assert repeat_req['cell']['userEnteredFormat']['textFormat']['bold'] == True
    assert repeat_req['fields'] == 'userEnteredFormat'

def test_prepare_set_cells_formats(mock_service, mock_credentials):
  """Test prepare_setCellsFormats method."""
  ss = Spreadsheet(mock_service, mock_credentials)
  ss.prepare_setCellsFormats('B4:C5', [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}}, {'backgroundColor': {'red': 0, 'green': 1, 'blue': 0}}],
                                     [{'backgroundColor': {'red': 0, 'green': 0, 'blue': 1}}, {'backgroundColor': {'red': 1, 'green': 1, 'blue': 0}}]])
  assert len(ss.requests) == 1
  update_req = ss.requests[0]['updateCells']
  assert update_req['range']['startRowIndex'] == 3
  assert update_req['range']['endRowIndex'] == 5
  assert update_req['range']['startColumnIndex'] == 1
  assert update_req['range']['endColumnIndex'] == 3
  assert update_req['rows'][0]['values'][0]['userEnteredFormat']['backgroundColor'] == {'red': 1, 'green': 0, 'blue': 0}
  assert update_req['rows'][0]['values'][1]['userEnteredFormat']['backgroundColor'] == {'red': 0, 'green': 1, 'blue': 0}
  assert update_req['rows'][1]['values'][0]['userEnteredFormat']['backgroundColor'] == {'red': 0, 'green': 0, 'blue': 1}
  assert update_req['rows'][1]['values'][1]['userEnteredFormat']['backgroundColor'] == {'red': 1, 'green': 1, 'blue': 0}
  assert update_req['fields'] == 'userEnteredFormat'


def test_prepare_set_borders(mock_service, mock_credentials):
    """Test prepare_setBorders method."""
    ss = Spreadsheet(mock_service, mock_credentials)
    ss.prepare_setBorders('A3:E3', bottom={'style': 'SOLID', 'width': 1, 'color': {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1}})
    assert len(ss.requests) == 1
    border_req = ss.requests[0]['updateBorders']
    assert border_req['range']['startRowIndex'] == 2
    assert border_req['range']['endRowIndex'] == 3
    assert border_req['range']['startColumnIndex'] == 0
    assert border_req['range']['endColumnIndex'] == 5
    assert border_req['bottom']['style'] == 'SOLID'
    assert border_req['bottom']['width'] == 1
    assert border_req['bottom']['color'] == {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1}

def test_to_grid_range(mock_service, mock_credentials):
    """Test toGridRange method."""
    ss = Spreadsheet(mock_service, mock_credentials, sheet_id=5)
    grid_range = ss.toGridRange('A1:B2')
    assert grid_range['sheetId'] == 5
    assert grid_range['startRowIndex'] == 0
    assert grid_range['endRowIndex'] == 2
    assert grid_range['startColumnIndex'] == 0
    assert grid_range['endColumnIndex'] == 2


def test_get_sheet_id_from_range(mock_service, mock_credentials):
  """Test get_sheet_id_from_range"""
  ss = Spreadsheet(mock_service, mock_credentials, sheet_id=5)
  assert ss.get_sheet_id_from_range("Test!A1:B2") == 5
  assert ss.get_sheet_id_from_range("A1:B2") == 0
```