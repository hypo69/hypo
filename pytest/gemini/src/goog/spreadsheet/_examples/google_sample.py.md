```python
import pytest
import os
from pathlib import Path
from unittest.mock import patch, mock_open
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

# Assuming the code is in a file named google_sample.py
from hypotez.src.goog.spreadsheet._examples import google_sample

# Fixture for a mock credentials object
@pytest.fixture
def mock_credentials():
    return Credentials(
        token='test_token',
        refresh_token='test_refresh_token',
        token_uri='https://test.example.com/token',
        client_id='test_client_id',
        client_secret='test_client_secret',
        scopes=google_sample.SCOPES
    )


# Fixture for a mock google sheets service object
@pytest.fixture
def mock_sheets_service():
    class MockValues:
        def get(self, spreadsheetId, range):
            class MockExecute:
                def execute(self):
                   return {'values': [['Alice', 'Math'], ['Bob', 'Science']]}
            return MockExecute()

    class MockSpreadsheets:
        def values(self):
            return MockValues()

    class MockService:
        def spreadsheets(self):
            return MockSpreadsheets()

    return MockService()

# Fixture for a mock google sheets service object with no data
@pytest.fixture
def mock_sheets_service_no_data():
    class MockValues:
        def get(self, spreadsheetId, range):
            class MockExecute:
                def execute(self):
                   return {'values': []}
            return MockExecute()

    class MockSpreadsheets:
        def values(self):
            return MockValues()

    class MockService:
        def spreadsheets(self):
            return MockSpreadsheets()

    return MockService()

# Fixture for a mock google sheets service object raising HttpError
@pytest.fixture
def mock_sheets_service_http_error():
    class MockValues:
        def get(self, spreadsheetId, range):
            class MockExecute:
                def execute(self):
                    raise HttpError(resp=None, content=b'error')
            return MockExecute()

    class MockSpreadsheets:
        def values(self):
            return MockValues()

    class MockService:
        def spreadsheets(self):
            return MockSpreadsheets()

    return MockService()


def test_main_no_credentials_file(monkeypatch, mock_sheets_service, mock_credentials):
    """Test case where no token.json file exists.
    
       This test mocks the credentials loading process and verifies that
       the Google Sheets API is called correctly.
    """

    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    monkeypatch.setattr(google_sample.Credentials, 'from_authorized_user_file', lambda x, y: None)

    # Mock the InstalledAppFlow to avoid browser interaction
    class MockInstalledAppFlow:
       @staticmethod
       def from_client_secrets_file(credentials_json, scopes):
            return MockInstalledAppFlow()
       def run_local_server(self, port):
           return mock_credentials
    monkeypatch.setattr(google_sample, 'InstalledAppFlow', MockInstalledAppFlow)

    monkeypatch.setattr(google_sample, 'build', lambda x, y, credentials: mock_sheets_service)

    captured_output = []
    monkeypatch.setattr("sys.stdout", open(os.devnull, "w"))  # Redirect stdout to null to avoid printing in tests
    monkeypatch.setattr("sys.stdout", type("myclass", (), {"write": captured_output.append})) # Capture output

    google_sample.main()

    assert "Name, Major:" in " ".join(captured_output)
    assert "Alice, Math" in " ".join(captured_output)
    assert "Bob, Science" in " ".join(captured_output)


def test_main_with_credentials_file(monkeypatch, mock_sheets_service, mock_credentials):
    """Test case where a valid token.json file exists.
    
       This test mocks the credentials loading process and verifies that
       the Google Sheets API is called correctly.
    """
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(google_sample.Credentials, 'from_authorized_user_file', lambda x, y: mock_credentials)
    monkeypatch.setattr(google_sample.Credentials, 'valid', True)
    monkeypatch.setattr(google_sample, 'build', lambda x, y, credentials: mock_sheets_service)

    captured_output = []
    monkeypatch.setattr("sys.stdout", open(os.devnull, "w"))  # Redirect stdout to null to avoid printing in tests
    monkeypatch.setattr("sys.stdout", type("myclass", (), {"write": captured_output.append})) # Capture output

    google_sample.main()
    assert "Name, Major:" in " ".join(captured_output)
    assert "Alice, Math" in " ".join(captured_output)
    assert "Bob, Science" in " ".join(captured_output)

def test_main_no_data_from_spreadsheet(monkeypatch, mock_sheets_service_no_data, mock_credentials):
    """
    Test case where the spreadsheet returns no data.

    This test verifies that the function correctly handles an empty
    spreadsheet response.
    """
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(google_sample.Credentials, 'from_authorized_user_file', lambda x, y: mock_credentials)
    monkeypatch.setattr(google_sample.Credentials, 'valid', True)
    monkeypatch.setattr(google_sample, 'build', lambda x, y, credentials: mock_sheets_service_no_data)
    
    captured_output = []
    monkeypatch.setattr("sys.stdout", open(os.devnull, "w"))  # Redirect stdout to null to avoid printing in tests
    monkeypatch.setattr("sys.stdout", type("myclass", (), {"write": captured_output.append})) # Capture output

    google_sample.main()

    assert "No data found." in " ".join(captured_output)

def test_main_http_error(monkeypatch, mock_sheets_service_http_error, mock_credentials):
    """Test case where an HttpError occurs.
    
       This test verifies that HttpError is caught.
    """

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(google_sample.Credentials, 'from_authorized_user_file', lambda x, y: mock_credentials)
    monkeypatch.setattr(google_sample.Credentials, 'valid', True)
    monkeypatch.setattr(google_sample, 'build', lambda x, y, credentials: mock_sheets_service_http_error)

    captured_output = []
    monkeypatch.setattr("sys.stdout", open(os.devnull, "w"))  # Redirect stdout to null to avoid printing in tests
    monkeypatch.setattr("sys.stdout", type("myclass", (), {"write": captured_output.append})) # Capture output

    google_sample.main()
    assert "error" in " ".join(captured_output)

def test_main_credentials_expired(monkeypatch, mock_sheets_service, mock_credentials):
    """
    Test case where credentials have expired and need to be refreshed.

     This test mocks the credentials loading process and verifies that
     the refresh token process works when the token is expired.
    """
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(google_sample.Credentials, 'from_authorized_user_file', lambda x, y: mock_credentials)
    monkeypatch.setattr(google_sample.Credentials, 'valid', False)
    monkeypatch.setattr(google_sample.Credentials, 'expired', True)
    monkeypatch.setattr(google_sample.Credentials, 'refresh_token', True)
    monkeypatch.setattr(google_sample.Credentials, 'refresh', lambda x: None)
    monkeypatch.setattr(google_sample, 'build', lambda x, y, credentials: mock_sheets_service)

    captured_output = []
    monkeypatch.setattr("sys.stdout", open(os.devnull, "w"))  # Redirect stdout to null to avoid printing in tests
    monkeypatch.setattr("sys.stdout", type("myclass", (), {"write": captured_output.append})) # Capture output

    google_sample.main()

    assert "Name, Major:" in " ".join(captured_output)
    assert "Alice, Math" in " ".join(captured_output)
    assert "Bob, Science" in " ".join(captured_output)

def test_main_credentials_expired_no_refresh_token(monkeypatch, mock_sheets_service, mock_credentials):
    """Test case where credentials have expired and no refresh token is available.
    
       This test mocks the credentials loading process, simulating a situation
       where credentials are invalid and a new auth flow needs to be initiated.
    """
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(google_sample.Credentials, 'from_authorized_user_file', lambda x, y: mock_credentials)
    monkeypatch.setattr(google_sample.Credentials, 'valid', False)
    monkeypatch.setattr(google_sample.Credentials, 'expired', True)
    monkeypatch.setattr(google_sample.Credentials, 'refresh_token', False)
    monkeypatch.setattr(google_sample, 'build', lambda x, y, credentials: mock_sheets_service)

        # Mock the InstalledAppFlow to avoid browser interaction
    class MockInstalledAppFlow:
       @staticmethod
       def from_client_secrets_file(credentials_json, scopes):
            return MockInstalledAppFlow()
       def run_local_server(self, port):
           return mock_credentials
    monkeypatch.setattr(google_sample, 'InstalledAppFlow', MockInstalledAppFlow)
    
    captured_output = []
    monkeypatch.setattr("sys.stdout", open(os.devnull, "w"))  # Redirect stdout to null to avoid printing in tests
    monkeypatch.setattr("sys.stdout", type("myclass", (), {"write": captured_output.append})) # Capture output

    google_sample.main()
    assert "Name, Major:" in " ".join(captured_output)
    assert "Alice, Math" in " ".join(captured_output)
    assert "Bob, Science" in " ".join(captured_output)
```