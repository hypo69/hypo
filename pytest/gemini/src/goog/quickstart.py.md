```python
import pytest
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path
import json
from google.oauth2.credentials import Credentials
from googleapiclient import errors

# Assuming the code to be tested is in a file named quickstart.py
# from quickstart import main, SCOPES, SAMPLE_CODE, SAMPLE_MANIFEST # this import needs adjustment
from hypotez.src.goog.quickstart import main, SCOPES, SAMPLE_CODE, SAMPLE_MANIFEST

@pytest.fixture
def mock_credentials():
    """Creates a mock Credentials object."""
    return MagicMock(spec=Credentials)

@pytest.fixture
def mock_service():
    """Creates a mock Google API service object."""
    service = MagicMock()
    projects_mock = MagicMock()
    service.projects.return_value = projects_mock
    return service

@pytest.fixture
def mock_installed_app_flow():
    """Creates a mock InstalledAppFlow object."""
    flow_mock = MagicMock()
    return flow_mock


def test_main_no_token_file(mock_credentials, mock_service, mock_installed_app_flow):
    """Tests the main function when no token.json file exists, forcing new auth."""
    with patch('hypotez.src.goog.quickstart.Path.exists', return_value=False), \
            patch('hypotez.src.goog.quickstart.Credentials.from_authorized_user_file', return_value=None), \
            patch('hypotez.src.goog.quickstart.InstalledAppFlow.from_client_secrets_file', return_value=mock_installed_app_flow), \
            patch('hypotez.src.goog.quickstart.build', return_value=mock_service), \
            patch('hypotez.src.goog.quickstart.Path.open', mock_open()) as mock_file, \
             patch('hypotez.src.goog.quickstart.gs.path.tmp', Path('/tmp')):
        
        mock_installed_app_flow.run_local_server.return_value = mock_credentials
        mock_credentials.to_json.return_value = '{"token": "test_token"}'
        mock_service.projects().create.return_value.execute.return_value = {'scriptId': 'test_script_id'}
        mock_service.projects().updateContent.return_value.execute.return_value = {'scriptId': 'test_script_id'}

        main()
        mock_installed_app_flow.from_client_secrets_file.assert_called_once_with('credentials.json', SCOPES)
        mock_installed_app_flow.run_local_server.assert_called_once_with(port=0)
        mock_file().write.assert_called_once_with('{"token": "test_token"}')
        mock_service.projects().create.assert_called_once()
        mock_service.projects().updateContent.assert_called_once()


def test_main_token_file_exists_and_valid(mock_credentials, mock_service):
    """Tests when token.json exists and credentials are valid."""
    mock_credentials.valid = True
    with patch('hypotez.src.goog.quickstart.Path.exists', return_value=True), \
            patch('hypotez.src.goog.quickstart.Credentials.from_authorized_user_file', return_value=mock_credentials), \
            patch('hypotez.src.goog.quickstart.build', return_value=mock_service), \
            patch('hypotez.src.goog.quickstart.gs.path.tmp', Path('/tmp')):
        mock_service.projects().create.return_value.execute.return_value = {'scriptId': 'test_script_id'}
        mock_service.projects().updateContent.return_value.execute.return_value = {'scriptId': 'test_script_id'}
        main()
        mock_service.projects().create.assert_called_once()
        mock_service.projects().updateContent.assert_called_once()


def test_main_token_file_exists_but_expired(mock_credentials, mock_service, mock_installed_app_flow):
    """Tests when token.json exists, but credentials are expired and need refreshing."""
    mock_credentials.valid = False
    mock_credentials.expired = True
    mock_credentials.refresh_token = 'test_refresh_token'

    with patch('hypotez.src.goog.quickstart.Path.exists', return_value=True), \
            patch('hypotez.src.goog.quickstart.Credentials.from_authorized_user_file', return_value=mock_credentials), \
            patch('hypotez.src.goog.quickstart.build', return_value=mock_service), \
            patch('hypotez.src.goog.quickstart.InstalledAppFlow.from_client_secrets_file', return_value=mock_installed_app_flow), \
           patch('hypotez.src.goog.quickstart.Path.open', mock_open()) as mock_file, \
             patch('hypotez.src.goog.quickstart.gs.path.tmp', Path('/tmp')):
        mock_credentials.to_json.return_value = '{"token": "test_token"}'
        mock_service.projects().create.return_value.execute.return_value = {'scriptId': 'test_script_id'}
        mock_service.projects().updateContent.return_value.execute.return_value = {'scriptId': 'test_script_id'}
        main()
        mock_credentials.refresh.assert_called_once()
        mock_service.projects().create.assert_called_once()
        mock_service.projects().updateContent.assert_called_once()
        mock_file().write.assert_called_once_with('{"token": "test_token"}')

def test_main_token_file_exists_but_invalid_no_refresh_token(mock_credentials, mock_service, mock_installed_app_flow):
    """Tests when token.json exists, credentials invalid with no refresh token requiring new auth."""
    mock_credentials.valid = False
    mock_credentials.expired = False
    mock_credentials.refresh_token = None

    with patch('hypotez.src.goog.quickstart.Path.exists', return_value=True), \
            patch('hypotez.src.goog.quickstart.Credentials.from_authorized_user_file', return_value=mock_credentials), \
            patch('hypotez.src.goog.quickstart.InstalledAppFlow.from_client_secrets_file', return_value=mock_installed_app_flow), \
            patch('hypotez.src.goog.quickstart.build', return_value=mock_service),\
           patch('hypotez.src.goog.quickstart.Path.open', mock_open()) as mock_file,\
             patch('hypotez.src.goog.quickstart.gs.path.tmp', Path('/tmp')):
        
        mock_installed_app_flow.run_local_server.return_value = mock_credentials
        mock_credentials.to_json.return_value = '{"token": "test_token"}'
        mock_service.projects().create.return_value.execute.return_value = {'scriptId': 'test_script_id'}
        mock_service.projects().updateContent.return_value.execute.return_value = {'scriptId': 'test_script_id'}

        main()

        mock_installed_app_flow.from_client_secrets_file.assert_called_once_with('credentials.json', SCOPES)
        mock_installed_app_flow.run_local_server.assert_called_once_with(port=0)
        mock_service.projects().create.assert_called_once()
        mock_service.projects().updateContent.assert_called_once()
        mock_file().write.assert_called_once_with('{"token": "test_token"}')


def test_main_api_error(mock_credentials, mock_service):
    """Tests the main function when the Apps Script API call throws an error."""
    with patch('hypotez.src.goog.quickstart.Path.exists', return_value=True), \
            patch('hypotez.src.goog.quickstart.Credentials.from_authorized_user_file', return_value=mock_credentials), \
            patch('hypotez.src.goog.quickstart.build', return_value=mock_service), \
            patch('hypotez.src.goog.quickstart.gs.path.tmp', Path('/tmp')), \
            patch('builtins.print') as mock_print:
        error_mock = errors.HttpError(resp=MagicMock(status=400), content=b'{"error": "Test Error"}')
        mock_service.projects().create.return_value.execute.side_effect = error_mock
        
        main()
        mock_print.assert_called_with(b'{"error": "Test Error"}')


def test_sample_code_is_not_empty():
    """Checks if the SAMPLE_CODE is not empty."""
    assert SAMPLE_CODE

def test_sample_manifest_is_not_empty():
    """Checks if the SAMPLE_MANIFEST is not empty."""
    assert SAMPLE_MANIFEST

def test_sample_manifest_is_valid_json():
    """Checks if the SAMPLE_MANIFEST is valid json"""
    json.loads(SAMPLE_MANIFEST)
```