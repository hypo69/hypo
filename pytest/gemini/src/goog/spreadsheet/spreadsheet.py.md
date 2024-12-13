```python
import pytest
import gspread
from gspread import Spreadsheet, Worksheet
from unittest.mock import MagicMock, patch
from pathlib import Path
import pandas as pd
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from oauth2client.service_account import ServiceAccountCredentials
from src.logger.logger import logger


# Fixture for creating a mock credentials object
@pytest.fixture
def mock_credentials():
    return MagicMock(spec=ServiceAccountCredentials)

# Fixture for creating a mock gspread client
@pytest.fixture
def mock_client():
    return MagicMock(spec=gspread.Client)

# Fixture for creating a mock spreadsheet
@pytest.fixture
def mock_spreadsheet():
    return MagicMock(spec=Spreadsheet)

# Fixture for creating a mock worksheet
@pytest.fixture
def mock_worksheet():
    return MagicMock(spec=Worksheet)

# Fixture for creating a dummy CSV file
@pytest.fixture
def dummy_csv_file(tmp_path):
    file_path = tmp_path / "test_data.csv"
    with open(file_path, "w") as f:
        f.write("col1,col2\n1,2\n3,4")
    return file_path

# Test cases for the SpreadSheet class

def test_spreadsheet_init_existing_spreadsheet(mock_credentials, mock_client, mock_spreadsheet):
    """Test initializing SpreadSheet with an existing spreadsheet ID."""
    mock_client.open_by_key.return_value = mock_spreadsheet
    
    spreadsheet_id = 'test_id'
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials', return_value=mock_credentials), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client', return_value=mock_client):
        spreadsheet_handler = SpreadSheet(spreadsheet_id=spreadsheet_id)
    
    assert spreadsheet_handler.spreadsheet_id == spreadsheet_id
    mock_client.open_by_key.assert_called_with(spreadsheet_id)
    assert spreadsheet_handler.spreadsheet == mock_spreadsheet
    assert spreadsheet_handler.client == mock_client

def test_spreadsheet_init_spreadsheet_not_found(mock_credentials, mock_client):
    """Test initializing SpreadSheet with a non-existent spreadsheet ID."""
    mock_client.open_by_key.side_effect = gspread.exceptions.SpreadsheetNotFound
    
    spreadsheet_id = 'invalid_id'
    
    with pytest.raises(gspread.exceptions.SpreadsheetNotFound), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials', return_value=mock_credentials), \
            patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client', return_value=mock_client):
        SpreadSheet(spreadsheet_id=spreadsheet_id)
        
def test_create_credentials_success(mock_credentials):
    """Test successful creation of credentials."""
    with patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name', return_value=mock_credentials), \
        patch('src.goog.spreadsheet.spreadsheet.gs.path.secrets', return_value=Path('.')):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        credentials = spreadsheet_handler._create_credentials()

    assert credentials == mock_credentials


def test_create_credentials_failure():
    """Test failure during credentials creation."""
    with patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name', side_effect=Exception("Test exception")), \
        patch('src.goog.spreadsheet.spreadsheet.gs.path.secrets', return_value=Path('.')):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        with pytest.raises(Exception, match="Test exception"):
             spreadsheet_handler._create_credentials()


def test_authorize_client_success(mock_credentials, mock_client):
    """Test successful client authorization."""
    with patch('gspread.authorize', return_value=mock_client):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.credentials = mock_credentials
        client = spreadsheet_handler._authorize_client()

    assert client == mock_client


def test_authorize_client_failure(mock_credentials):
    """Test failure during client authorization."""
    with patch('gspread.authorize', side_effect=Exception("Test exception")):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.credentials = mock_credentials
        with pytest.raises(Exception, match="Test exception"):
            spreadsheet_handler._authorize_client()

def test_get_worksheet_existing(mock_spreadsheet, mock_worksheet):
    """Test getting an existing worksheet."""
    mock_spreadsheet.worksheet.return_value = mock_worksheet
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.spreadsheet = mock_spreadsheet
        worksheet_name = 'existing_sheet'
        worksheet = spreadsheet_handler.get_worksheet(worksheet_name)
        
    mock_spreadsheet.worksheet.assert_called_with(worksheet_name)
    assert worksheet == mock_worksheet
    
def test_get_worksheet_not_found_create(mock_spreadsheet, mock_worksheet):
    """Test getting a non-existent worksheet and creating it."""
    mock_spreadsheet.worksheet.side_effect = gspread.exceptions.WorksheetNotFound
    mock_spreadsheet.add_worksheet.return_value = mock_worksheet
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.spreadsheet = mock_spreadsheet
        worksheet_name = 'new_sheet'
        worksheet = spreadsheet_handler.get_worksheet(worksheet_name)
    
    mock_spreadsheet.add_worksheet.assert_called_with(title=worksheet_name, rows=100, cols=10)
    assert worksheet == mock_worksheet


def test_create_worksheet_success(mock_spreadsheet, mock_worksheet):
    """Test successful worksheet creation."""
    mock_spreadsheet.add_worksheet.return_value = mock_worksheet
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.spreadsheet = mock_spreadsheet
        new_sheet_name = 'new_sheet'
        dims = {'rows': 50, 'cols': 5}
        worksheet = spreadsheet_handler.create_worksheet(new_sheet_name, dims)
    
    mock_spreadsheet.add_worksheet.assert_called_with(title=new_sheet_name, rows=dims['rows'], cols=dims['cols'])
    assert worksheet == mock_worksheet

def test_create_worksheet_failure(mock_spreadsheet):
    """Test failure during worksheet creation."""
    mock_spreadsheet.add_worksheet.side_effect = Exception("Test exception")
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.spreadsheet = mock_spreadsheet
        with pytest.raises(Exception, match="Test exception"):
           spreadsheet_handler.create_worksheet('new_sheet')


def test_copy_worksheet(mock_spreadsheet, mock_worksheet):
    """Test copying an existing worksheet."""
    mock_spreadsheet.worksheet.return_value = mock_worksheet
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.spreadsheet = mock_spreadsheet
        from_sheet_name = 'from_sheet'
        to_sheet_name = 'to_sheet'
        worksheet = spreadsheet_handler.copy_worksheet(from_sheet_name, to_sheet_name)

    mock_spreadsheet.worksheet.assert_called_with(from_sheet_name)
    mock_worksheet.duplicate.assert_called_with(new_sheet_name=to_sheet_name)
    assert worksheet == mock_worksheet

def test_upload_data_to_sheet_success(mock_spreadsheet, mock_worksheet, dummy_csv_file):
    """Test successful upload of data to a sheet."""
    mock_worksheet.update.return_value = None
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.worksheet = mock_worksheet
        spreadsheet_handler.data_file = dummy_csv_file
        spreadsheet_handler.upload_data_to_sheet()
    
    mock_worksheet.update.assert_called_once()

def test_upload_data_to_sheet_no_file(mock_worksheet):
    """Test upload data when no data file exists."""
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.worksheet = mock_worksheet
        spreadsheet_handler.data_file = None
        with pytest.raises(ValueError, match="Data file path is not set or the file does not exist."):
            spreadsheet_handler.upload_data_to_sheet()
            
def test_upload_data_to_sheet_file_not_exist(mock_worksheet, tmp_path):
    """Test upload data when data file does not exist."""
    non_existent_file = tmp_path / "non_existent.csv"
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.worksheet = mock_worksheet
        spreadsheet_handler.data_file = non_existent_file
        with pytest.raises(ValueError, match="Data file path is not set or the file does not exist."):
            spreadsheet_handler.upload_data_to_sheet()

def test_upload_data_to_sheet_error(mock_worksheet, dummy_csv_file):
    """Test error during data upload."""
    mock_worksheet.update.side_effect = Exception("Test upload error")
    
    with patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._create_credentials'), \
        patch('src.goog.spreadsheet.spreadsheet.SpreadSheet._authorize_client'):
        spreadsheet_handler = SpreadSheet(spreadsheet_id='test_id')
        spreadsheet_handler.worksheet = mock_worksheet
        spreadsheet_handler.data_file = dummy_csv_file
        with pytest.raises(Exception, match="Test upload error"):
            spreadsheet_handler.upload_data_to_sheet()
```