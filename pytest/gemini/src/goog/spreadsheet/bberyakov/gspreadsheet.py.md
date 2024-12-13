```python
import pytest
from unittest.mock import MagicMock, patch
import json
from hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet
from global_settingspread import Spreadsheet

# Fixture definitions
@pytest.fixture
def mock_gspread_client():
    """Mocks the gspread client for testing."""
    mock_client = MagicMock()
    mock_client.open_by_key = MagicMock(return_value=MagicMock(title='Test Spreadsheet'))
    mock_client.openall = MagicMock(return_value=[MagicMock(title='Existing Spreadsheet')])
    mock_client.create = MagicMock(return_value=MagicMock(id='123', title='New Spreadsheet'))
    return mock_client


@pytest.fixture
def mock_service_account(mock_gspread_client):
    """Mocks the service_account function."""
    with patch('hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.service_account', return_value=mock_gspread_client) as mock:
        yield mock

@pytest.fixture
def gspreadsheet_instance(mock_service_account):
    """Creates a GSpreadsheet instance for testing."""
    return GSpreadsheet()


def test_gspreadsheet_init_with_id(mock_service_account, mock_gspread_client):
    """Checks if the gsh is set correctly when initialized with an id."""
    gs = GSpreadsheet(s_id='123')
    mock_service_account.assert_called_once()
    mock_gspread_client.open_by_key.assert_called_with('1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')
    assert gs.gsh is not None


def test_gspreadsheet_init_with_title(mock_service_account, mock_gspread_client):
    """Checks if the gsh is set correctly when initialized with a title."""
    gs = GSpreadsheet(s_title='Test Spreadsheet')
    mock_service_account.assert_called_once()
    assert gs.gsh is not None


def test_get_project_spreadsheets_dict(gspreadsheet_instance):
    """Checks if the method returns the correct dictionary loaded from the json file."""
    expected_dict = json.loads('{"test": "value"}')
    with patch("builtins.open", unittest.mock.mock_open(read_data='{"test": "value"}')):
        actual_dict = gspreadsheet_instance.get_project_spreadsheets_dict()
    assert actual_dict == expected_dict


def test_get_by_title_creates_new_spreadsheet(mock_service_account, mock_gspread_client):
    """Checks if a new spreadsheet is created when it doesn't exist."""
    gs = GSpreadsheet()
    gs.get_by_title('New Spreadsheet')
    mock_gspread_client.create.assert_called_with('New Spreadsheet')
    assert gs.gsh is not None


def test_get_by_title_opens_existing_spreadsheet(mock_service_account, mock_gspread_client, capsys):
    """Checks if an existing spreadsheet is opened by title."""
    gs = GSpreadsheet()
    gs.gsh = mock_gspread_client
    gs.get_by_title('Existing Spreadsheet')
    captured = capsys.readouterr()
    assert "Spreadsheet Existing Spreadsheet already exist" in captured.out
    assert gs.gsh is not None

def test_get_by_id(mock_service_account, mock_gspread_client):
    """Checks if the correct spreadsheet is opened by id."""
    gs = GSpreadsheet()
    sh_id = 'test_id'
    result = gs.get_by_id(sh_id)
    mock_gspread_client.open_by_key.assert_called_with(sh_id)
    assert result == mock_gspread_client.open_by_key()

def test_get_all_spreadsheets_for_current_account(mock_service_account, mock_gspread_client):
    """Checks if all spreadsheets are opened for the current account."""
    gs = GSpreadsheet()
    gs.gsh = mock_gspread_client
    all_spreadsheets = gs.get_all_spreadsheets_for_current_account()
    mock_gspread_client.openall.assert_called_once()
    assert all_spreadsheets == mock_gspread_client.openall()
```