```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
import sys
from types import SimpleNamespace
from src.credentials import set_project_root, singleton, ProgramSettings
from pytest import raises
from unittest.mock import MagicMock
from pykeepass import PyKeePass
import getpass
import logging

logger = logging.getLogger(__name__)

# Fixture for a mock Path object
@pytest.fixture
def mock_path(tmp_path):
    """Provides a mock Path object and creates necessary directory structure."""
    
    def _mock_path(file_exists=False, dir_exists=False, is_file=False, is_dir=False, read_text_result = ""):
        mock = MagicMock(spec=Path)
        mock.exists.return_value = file_exists or dir_exists
        mock.is_file.return_value = is_file
        mock.is_dir.return_value = is_dir
        mock.read_text.return_value = read_text_result

        def _exists_side_effect(path):
             if str(path).endswith("pyproject.toml") or str(path).endswith("requirements.txt") or str(path).endswith(".git"):
                return file_exists or dir_exists
             return False
        mock.exists.side_effect = _exists_side_effect
        
        def _resolve():
            return mock
        mock.resolve.return_value = mock
        
        def _parent():
            return mock
        mock.parent.return_value = mock
        
        mock.__truediv__.side_effect = lambda x: _mock_path()
        mock.__str__.return_value = str(tmp_path)
        return mock
    
    return _mock_path



# Fixture for a mock PyKeePass object
@pytest.fixture
def mock_pykeepass():
    """Provides a mock PyKeePass object."""
    mock = MagicMock(spec=PyKeePass)
    return mock

# Fixture for a mock config
@pytest.fixture
def mock_config():
    config = SimpleNamespace(
        author = SimpleNamespace(name="Test Author", email="test@example.com"),
        modes = ["dev", "debug", "test", "prod"],
        paths = SimpleNamespace(
            logs = "logs",
            tmp = "tmp",
            external = "external",
            gdrive = "gdrive"
        ),
        project = SimpleNamespace(name = "test_project",version="0.1.0",release_date="2023-11-25 10:27:16")
    )
    return config


# Tests for set_project_root
def test_set_project_root_finds_root(mock_path):
    """Checks if set_project_root finds the project root when marker file exists."""
    mocked_path = mock_path(file_exists=True)
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.sys') as mocked_sys:

        root_path = set_project_root()
        assert root_path == mocked_path
        mocked_sys.path.insert.assert_called_once()

def test_set_project_root_no_root_found(mock_path):
    """Checks if set_project_root returns current directory when no marker file is found."""
    mocked_path = mock_path()
    with patch('src.credentials.Path', return_value=mocked_path), \
        patch('src.credentials.sys') as mocked_sys:
        root_path = set_project_root()
        assert root_path == mocked_path
        mocked_sys.path.insert.assert_called_once()
        
def test_set_project_root_with_custom_markers(mock_path):
    """Checks if set_project_root finds root with custom marker files."""
    mocked_path = mock_path(file_exists=True)
    with patch('src.credentials.Path', return_value=mocked_path), \
            patch('src.credentials.sys') as mocked_sys:
        marker_files = ('custom_marker.txt',)
        root_path = set_project_root(marker_files)
        assert root_path == mocked_path
        mocked_sys.path.insert.assert_called_once()

def test_set_project_root_empty_markers_list(mock_path):
    """Checks if set_project_root returns current directory when no markers passed."""
    mocked_path = mock_path()
    with patch('src.credentials.Path', return_value=mocked_path), \
            patch('src.credentials.sys') as mocked_sys:
        root_path = set_project_root(marker_files=tuple())
        assert root_path == mocked_path
        mocked_sys.path.insert.assert_called_once()



# Tests for singleton decorator
def test_singleton_returns_same_instance():
    """Checks if singleton returns the same instance of a class."""
    @singleton
    class TestClass:
        def __init__(self):
            self.value = 1

    instance1 = TestClass()
    instance2 = TestClass()
    assert instance1 is instance2
    assert instance1.value == instance2.value == 1

# Tests for ProgramSettings class

def test_program_settings_initializes_config_and_paths(mock_path, mock_config):
    """Checks if ProgramSettings correctly loads config and sets up paths."""
    mocked_path = mock_path(dir_exists = True)
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.j_loads_ns', return_value = mock_config), \
         patch('src.credentials.ProgramSettings._load_credentials', return_value = None),\
         patch('src.credentials.check_latest_release', return_value = None):
        settings = ProgramSettings()
        assert settings.base_dir == mocked_path
        assert settings.config == mock_config
        assert settings.config.project_name == str(mocked_path).split("/")[-1]
        
        assert settings.path.logs == mocked_path / "logs"
        assert settings.path.tmp == mocked_path / "tmp"
        assert settings.path.external == mocked_path / "external"
        assert settings.path.gdrive == mocked_path / "gdrive"
        assert settings.path.secrets == mocked_path / "secrets"

def test_program_settings_handles_config_load_error(mock_path):
    """Checks if ProgramSettings handles config load error correctly."""
    mocked_path = mock_path(dir_exists = True)
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.j_loads_ns', return_value=None), \
         patch('src.credentials.logger') as mock_logger:

        settings = ProgramSettings()
        mock_logger.error.assert_called_with('Error loading settings')
        assert settings.config is None

@patch('src.credentials.getpass.getpass', return_value = "test_password")
def test_program_settings_loads_credentials_dev_mode(mock_getpass, mock_path, mock_pykeepass):
    """Checks if ProgramSettings loads credentials using password from the file."""

    mocked_path = mock_path(file_exists=True, is_file = True, read_text_result="test_password")
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.PyKeePass', return_value=mock_pykeepass), \
        patch('src.credentials.j_loads_ns', return_value=MagicMock()),\
        patch('src.credentials.check_latest_release', return_value = None), \
         patch('src.credentials.ProgramSettings._load_aliexpress_credentials', return_value=True),\
          patch('src.credentials.ProgramSettings._load_openai_credentials', return_value=True),\
           patch('src.credentials.ProgramSettings._load_gemini_credentials', return_value=True),\
            patch('src.credentials.ProgramSettings._load_telegram_credentials', return_value=True),\
             patch('src.credentials.ProgramSettings._load_discord_credentials', return_value=True),\
               patch('src.credentials.ProgramSettings._load_PrestaShop_credentials', return_value=True),\
                  patch('src.credentials.ProgramSettings._load_presta_translations_credentials', return_value=True),\
                   patch('src.credentials.ProgramSettings._load_smtp_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_facebook_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_gapi_credentials', return_value=True):

        settings = ProgramSettings()
        mock_pykeepass.assert_called_with(str(mocked_path), password='test_password')
        
        assert settings.credentials is not None
        assert settings.credentials.aliexpress is not None
        assert settings.credentials.openai is not None
        assert settings.credentials.gemini is not None
        assert settings.credentials.telegram is not None
        assert settings.credentials.discord is not None
        assert settings.credentials.presta is not None
        assert settings.credentials.presta.translations is not None
        assert settings.credentials.smtp is not None
        assert settings.credentials.facebook is not None
        assert settings.credentials.gapi is not None
        
@patch('src.credentials.getpass.getpass', return_value = "test_password")
def test_program_settings_loads_credentials_prod_mode(mock_getpass,mock_path, mock_pykeepass):
    """Checks if ProgramSettings loads credentials using password prompt in production mode."""
    mocked_path = mock_path(file_exists=False, is_file = True)
    with patch('src.credentials.Path', return_value=mocked_path), \
        patch('src.credentials.PyKeePass', return_value=mock_pykeepass),\
        patch('src.credentials.j_loads_ns', return_value=MagicMock()), \
        patch('src.credentials.check_latest_release', return_value = None), \
        patch('src.credentials.ProgramSettings._load_aliexpress_credentials', return_value=True),\
          patch('src.credentials.ProgramSettings._load_openai_credentials', return_value=True),\
           patch('src.credentials.ProgramSettings._load_gemini_credentials', return_value=True),\
            patch('src.credentials.ProgramSettings._load_telegram_credentials', return_value=True),\
             patch('src.credentials.ProgramSettings._load_discord_credentials', return_value=True),\
               patch('src.credentials.ProgramSettings._load_PrestaShop_credentials', return_value=True),\
                  patch('src.credentials.ProgramSettings._load_presta_translations_credentials', return_value=True),\
                   patch('src.credentials.ProgramSettings._load_smtp_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_facebook_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_gapi_credentials', return_value=True):
         
        settings = ProgramSettings()
        mock_getpass.assert_called_once()
        mock_pykeepass.assert_called_with(str(mocked_path), password='test_password')
        assert settings.credentials is not None

def test_program_settings_kp_open_fail_with_retry(mock_path, mock_pykeepass):
    """Checks if ProgramSettings retries opening KeePass on failure."""
    mocked_path = mock_path()
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.PyKeePass', side_effect=Exception("Failed to open")), \
          patch('src.credentials.logger') as mock_logger, \
            patch('src.credentials.j_loads_ns', return_value=MagicMock()),\
            patch('src.credentials.check_latest_release', return_value = None), \
            patch('src.credentials.sys') as mock_sys:
        with raises(SystemExit):
           ProgramSettings()
        assert mock_logger.critical.call_count == 1
        assert mock_sys.exit.call_count == 1
        
def test_program_settings_kp_open_fail_on_first_attempt(mock_path, mock_pykeepass):
    """Checks if ProgramSettings retries opening KeePass on failure and succeeds."""
    mocked_path = mock_path(file_exists=True, is_file = True, read_text_result="test_password")
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.PyKeePass', side_effect=[Exception("Failed to open"), mock_pykeepass]),\
          patch('src.credentials.logger') as mock_logger,\
          patch('src.credentials.j_loads_ns', return_value=MagicMock()), \
            patch('src.credentials.check_latest_release', return_value = None), \
             patch('src.credentials.ProgramSettings._load_aliexpress_credentials', return_value=True),\
          patch('src.credentials.ProgramSettings._load_openai_credentials', return_value=True),\
           patch('src.credentials.ProgramSettings._load_gemini_credentials', return_value=True),\
            patch('src.credentials.ProgramSettings._load_telegram_credentials', return_value=True),\
             patch('src.credentials.ProgramSettings._load_discord_credentials', return_value=True),\
               patch('src.credentials.ProgramSettings._load_PrestaShop_credentials', return_value=True),\
                  patch('src.credentials.ProgramSettings._load_presta_translations_credentials', return_value=True),\
                   patch('src.credentials.ProgramSettings._load_smtp_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_facebook_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_gapi_credentials', return_value=True):
        settings = ProgramSettings()
        assert mock_logger.critical.call_count == 0
        assert settings.credentials is not None

def test_load_credentials(mock_path, mock_pykeepass):
    """Tests the _load_credentials method"""
    mocked_path = mock_path(file_exists=True, is_file = True, read_text_result="test_password")
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.PyKeePass', return_value=mock_pykeepass),\
        patch('src.credentials.j_loads_ns', return_value=MagicMock()),\
        patch('src.credentials.check_latest_release', return_value = None), \
         patch('src.credentials.ProgramSettings._load_aliexpress_credentials', return_value=True),\
          patch('src.credentials.ProgramSettings._load_openai_credentials', return_value=True),\
           patch('src.credentials.ProgramSettings._load_gemini_credentials', return_value=True),\
            patch('src.credentials.ProgramSettings._load_telegram_credentials', return_value=True),\
             patch('src.credentials.ProgramSettings._load_discord_credentials', return_value=True),\
               patch('src.credentials.ProgramSettings._load_PrestaShop_credentials', return_value=True),\
                  patch('src.credentials.ProgramSettings._load_presta_translations_credentials', return_value=True),\
                   patch('src.credentials.ProgramSettings._load_smtp_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_facebook_credentials', return_value=True),\
                    patch('src.credentials.ProgramSettings._load_gapi_credentials', return_value=True):
        settings = ProgramSettings()
        assert settings.credentials.aliexpress is not None
        assert settings.credentials.openai is not None
        assert settings.credentials.gemini is not None
        assert settings.credentials.telegram is not None
        assert settings.credentials.discord is not None
        assert settings.credentials.presta is not None
        assert settings.credentials.presta.translations is not None
        assert settings.credentials.smtp is not None
        assert settings.credentials.facebook is not None
        assert settings.credentials.gapi is not None


def test_load_aliexpress_credentials(mock_pykeepass):
    """Tests the _load_aliexpress_credentials method"""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(username='test_user',password='test_password',fields = {"api_key":"test_api_key", "secret":"test_secret", "tracking_id":"test_tracking_id", "email": "test_email"})]

    settings = ProgramSettings()
    settings._load_aliexpress_credentials(mock_kp)

    assert settings.credentials.aliexpress.api_key == "test_api_key"
    assert settings.credentials.aliexpress.secret == "test_secret"
    assert settings.credentials.aliexpress.tracking_id == "test_tracking_id"
    assert settings.credentials.aliexpress.email == "test_email"
    assert settings.credentials.aliexpress.password == "test_password"
    
def test_load_openai_credentials(mock_pykeepass):
    """Tests the _load_openai_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.side_effect = [
        [MagicMock(fields={"api_key": "test_openai_api_key"})],
        [MagicMock(fields={"assistant_id": "test_assistant_id"})],
    ]

    settings = ProgramSettings()
    settings._load_openai_credentials(mock_kp)

    assert settings.credentials.openai.api_key == "test_openai_api_key"
    assert settings.credentials.openai.assistant_id == "test_assistant_id"

def test_load_gemini_credentials(mock_pykeepass):
    """Tests the _load_gemini_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"api_key": "test_gemini_api_key"})]

    settings = ProgramSettings()
    settings._load_gemini_credentials(mock_kp)

    assert settings.credentials.gemini.api_key == "test_gemini_api_key"
    
def test_load_telegram_credentials(mock_pykeepass):
    """Tests the _load_telegram_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"token": "test_telegram_token"})]

    settings = ProgramSettings()
    settings._load_telegram_credentials(mock_kp)

    assert settings.credentials.telegram.token == "test_telegram_token"

def test_load_discord_credentials(mock_pykeepass):
    """Tests the _load_discord_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"application_id": "test_discord_app_id", "public_key": "test_discord_public_key", "bot_token": "test_discord_bot_token"})]

    settings = ProgramSettings()
    settings._load_discord_credentials(mock_kp)

    assert settings.credentials.discord.application_id == "test_discord_app_id"
    assert settings.credentials.discord.public_key == "test_discord_public_key"
    assert settings.credentials.discord.bot_token == "test_discord_bot_token"

def test_load_presta_credentials(mock_pykeepass):
    """Tests the _load_PrestaShop_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.side_effect = [
        [MagicMock(fields={"api_key": "test_presta_api_key", "api_domain":"test_presta_api_domain", "db_server":"test_presta_db_server", "db_user":"test_presta_db_user", "db_password":"test_presta_db_password"})],
        [MagicMock(fields={"api_key": "test_presta_client_api_key", "api_domain":"test_presta_client_api_domain", "db_server":"test_presta_client_db_server", "db_user":"test_presta_client_db_user", "db_password":"test_presta_client_db_password"})]
    ]


    settings = ProgramSettings()
    settings._load_PrestaShop_credentials(mock_kp)

    assert settings.credentials.presta.api_key == "test_presta_api_key"
    assert settings.credentials.presta.api_domain == "test_presta_api_domain"
    assert settings.credentials.presta.db_server == "test_presta_db_server"
    assert settings.credentials.presta.db_user == "test_presta_db_user"
    assert settings.credentials.presta.db_password == "test_presta_db_password"

    assert settings.credentials.presta.client.api_key == "test_presta_client_api_key"
    assert settings.credentials.presta.client.api_domain == "test_presta_client_api_domain"
    assert settings.credentials.presta.client.db_server == "test_presta_client_db_server"
    assert settings.credentials.presta.client.db_user == "test_presta_client_db_user"
    assert settings.credentials.presta.client.db_password == "test_presta_client_db_password"

def test_load_presta_translations_credentials(mock_pykeepass):
    """Tests the _load_presta_translations_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"server": "test_presta_translations_server", "port":"test_presta_translations_port", "database":"test_presta_translations_database", "user":"test_presta_translations_user", "password":"test_presta_translations_password"})]

    settings = ProgramSettings()
    settings._load_presta_translations_credentials(mock_kp)

    assert settings.credentials.presta.translations.server == "test_presta_translations_server"
    assert settings.credentials.presta.translations.port == "test_presta_translations_port"
    assert settings.credentials.presta.translations.database == "test_presta_translations_database"
    assert settings.credentials.presta.translations.user == "test_presta_translations_user"
    assert settings.credentials.presta.translations.password == "test_presta_translations_password"

def test_load_smtp_credentials(mock_pykeepass):
    """Tests the _load_smtp_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"server": "test_smtp_server", "port":"test_smtp_port", "user":"test_smtp_user", "password":"test_smtp_password"})]

    settings = ProgramSettings()
    settings._load_smtp_credentials(mock_kp)

    assert settings.credentials.smtp.server == "test_smtp_server"
    assert settings.credentials.smtp.port == "test_smtp_port"
    assert settings.credentials.smtp.user == "test_smtp_user"
    assert settings.credentials.smtp.password == "test_smtp_password"
    
def test_load_facebook_credentials(mock_pykeepass):
    """Tests the _load_facebook_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"app_id": "test_facebook_app_id", "app_secret":"test_facebook_app_secret", "access_token":"test_facebook_access_token"})]

    settings = ProgramSettings()
    settings._load_facebook_credentials(mock_kp)

    assert settings.credentials.facebook.app_id == "test_facebook_app_id"
    assert settings.credentials.facebook.app_secret == "test_facebook_app_secret"
    assert settings.credentials.facebook.access_token == "test_facebook_access_token"

def test_load_gapi_credentials(mock_pykeepass):
    """Tests the _load_gapi_credentials method."""
    mock_kp = mock_pykeepass
    mock_kp.find_entries.return_value = [MagicMock(fields={"api_key": "test_gapi_api_key"})]

    settings = ProgramSettings()
    settings._load_gapi_credentials(mock_kp)

    assert settings.credentials.gapi.api_key == "test_gapi_api_key"

def test_now(mock_path, mock_config):
    """Tests the now method."""
    mocked_path = mock_path(dir_exists=True)
    mock_config.time_format = '%Y-%m-%d %H:%M:%S'
    with patch('src.credentials.Path', return_value=mocked_path), \
         patch('src.credentials.j_loads_ns', return_value = mock_config), \
        patch('src.credentials.ProgramSettings._load_credentials', return_value = None),\
        patch('src.credentials.check_latest_release', return_value = None), \
        patch('src.credentials.datetime') as mock_datetime:

        mock_datetime.now.return_value.strftime.return_value = "2024-01-01 12:00:00"
        settings = ProgramSettings()
        assert settings.now() == "2024-01-01 12:00:00"
```