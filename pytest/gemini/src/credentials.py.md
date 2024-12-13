```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from types import SimpleNamespace
import getpass
import socket
import sys
import os
import warnings
from pykeepass import PyKeePass

from src.credentials import ProgramSettings, set_project_root, singleton
from src.logger.exceptions import (
    BinaryError,
    CredentialsError,
    DefaultSettingsException,
    HeaderChecksumError,
    KeePassException,
    PayloadChecksumError,
    UnableToSendToRecycleBin,
)


# Mock the logger to avoid actual logging during tests
class MockLogger:
    def __init__(self):
        self.error_messages = []
        self.critical_messages = []

    def error(self, message):
        self.error_messages.append(message)

    def critical(self, message, exc_info=False):
        self.critical_messages.append((message, exc_info))

# Replace logger with mock object
from src.logger import logger
logger = MockLogger()


@pytest.fixture
def mock_base_dir(tmp_path):
    """Provides a mock base directory for testing."""
    (tmp_path / "src").mkdir()
    (tmp_path / "bin").mkdir()
    (tmp_path / "secrets").mkdir()
    (tmp_path / "log").mkdir()
    (tmp_path / "tmp").mkdir()
    (tmp_path / "data").mkdir()
    (tmp_path / "google_drive").mkdir()
    (tmp_path / "external_storage").mkdir()
    (tmp_path / "toolbox").mkdir()

    (tmp_path / "src" / "config.json").write_text('{"path": {"log": "log", "tmp": "tmp", "data": "data", "google_drive": "google_drive", "external_storage": "external_storage"}, "mode": "test_mode", "timestamp_format": "%y_%m_%d_%H_%M_%S_%f", "git": "test_git", "git_user": "test_user"}')
    (tmp_path / "secrets" / "password.txt").write_text("test_password")
    (tmp_path / "secrets" / "credentials.kdbx").write_text("test_kdbx")
    return tmp_path


@pytest.fixture
def mock_keepass():
    """Provides a mock PyKeePass object."""
    kp_mock = MagicMock(spec=PyKeePass)
    kp_mock.find_groups.return_value = MagicMock(entries=[MagicMock(custom_properties={'api_key': 'test_api_key', 'secret': 'test_secret', 'tracking_id': 'test_tracking_id', 'email': 'test_email', 'project_api':'test_project_api', 'assistant_id': 'test_assistant_id', 'application_id':'test_application_id', 'public_key':'test_public_key','bot_token':'test_bot_token', 'server':'test_server','port':'test_port', 'user':'test_user','database':'test_database', 'app_id':'test_app_id','app_secret':'test_app_secret','access_token':'test_access_token', 'token':'test_token'}, password="test_password")])
    kp_mock.find_groups.side_effect = lambda path: MagicMock(entries=[MagicMock(title='test_title',custom_properties={'api_key': 'test_api_key', 'secret': 'test_secret', 'tracking_id': 'test_tracking_id', 'email': 'test_email', 'project_api':'test_project_api', 'assistant_id': 'test_assistant_id', 'application_id':'test_application_id', 'public_key':'test_public_key','bot_token':'test_bot_token', 'server':'test_server','port':'test_port', 'user':'test_user','database':'test_database', 'app_id':'test_app_id','app_secret':'test_app_secret','access_token':'test_access_token','token':'test_token'}, password="test_password")])
    return kp_mock


def test_set_project_root_with_marker_file(tmp_path):
    """Checks if the project root is correctly identified when marker files exist."""
    (tmp_path / "pyproject.toml").touch()
    assert set_project_root() == tmp_path


def test_set_project_root_without_marker_file(tmp_path):
    """Checks if the project root is the current file directory when no marker files are found."""
    current_dir = Path(__file__).resolve().parent
    assert set_project_root() == current_dir


def test_singleton():
    """Verifies the singleton decorator functionality."""
    @singleton
    class TestClass:
        def __init__(self, value):
            self.value = value
    
    instance1 = TestClass(1)
    instance2 = TestClass(2)
    
    assert instance1 is instance2
    assert instance1.value == 1 #The value should not be overwritten with new constructor call
    assert instance2.value == 1


@patch("src.credentials.PyKeePass", autospec=True)
def test_program_settings_initialization(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests the initialization of ProgramSettings with mocked dependencies."""

    mock_keepass_cls.return_value = mock_keepass

    gs = ProgramSettings()

    assert gs.MODE == 'test_mode'
    assert gs.base_dir == mock_base_dir
    assert gs.config.project_name == mock_base_dir.name
    assert gs.path.root == mock_base_dir
    assert gs.path.bin == mock_base_dir / 'bin'
    assert gs.path.src == mock_base_dir / 'src'
    assert gs.path.endpoints == mock_base_dir / 'src' / 'endpoints'
    assert gs.path.secrets == mock_base_dir / 'secrets'
    assert gs.path.toolbox == mock_base_dir / 'toolbox'
    assert gs.path.log == mock_base_dir / 'log'
    assert gs.path.tmp == mock_base_dir / 'tmp'
    assert gs.path.data == mock_base_dir / 'data'
    assert gs.path.google_drive == mock_base_dir / 'google_drive'
    assert gs.path.external_storage == mock_base_dir / 'external_storage'

    mock_keepass_cls.assert_called_once()


@patch("src.credentials.PyKeePass", autospec=True)
def test_program_settings_load_credentials(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests the loading of various credentials from KeePass."""
    mock_keepass_cls.return_value = mock_keepass

    gs = ProgramSettings()

    assert gs.credentials.aliexpress.api_key == 'test_api_key'
    assert gs.credentials.aliexpress.secret == 'test_secret'
    assert gs.credentials.aliexpress.tracking_id == 'test_tracking_id'
    assert gs.credentials.aliexpress.email == 'test_email'
    assert gs.credentials.aliexpress.password == 'test_password'

    assert gs.credentials.openai.test_title == 'test_project_api' # type: ignore
    assert gs.credentials.openai.assistant_id.test_title == 'test_assistant_id' # type: ignore

    assert gs.credentials.gemini.test_title == 'test_api_key' # type: ignore

    assert gs.credentials.discord.application_id == 'test_application_id'
    assert gs.credentials.discord.public_key == 'test_public_key'
    assert gs.credentials.discord.bot_token == 'test_bot_token'
    
    assert gs.credentials.telegram.test_title == 'test_token' # type: ignore

    assert len(gs.credentials.presta.client) > 1  # default SimpleNamespace in list + loaded one

    assert gs.credentials.presta.translations.server == 'test_server'
    assert gs.credentials.presta.translations.port == 'test_port'
    assert gs.credentials.presta.translations.user == 'test_user'
    assert gs.credentials.presta.translations.database == 'test_database'
    assert gs.credentials.presta.translations.password == 'test_password'

    assert len(gs.credentials.smtp) > 0

    assert len(gs.credentials.facebook) > 0
    assert gs.credentials.gapi['api_key'] == 'test_api_key'

@patch("src.credentials.getpass.getpass", return_value="test_password")
@patch("src.credentials.PyKeePass", autospec=True)
def test_open_kp_success(mock_keepass_cls, mock_getpass, mock_base_dir, mock_keepass):
    """Tests successful opening of KeePass database."""
    mock_keepass_cls.return_value = mock_keepass
    gs = ProgramSettings()
    kp = gs._open_kp()
    assert kp is not None
    mock_keepass_cls.assert_called_once()


@patch("src.credentials.getpass.getpass", return_value="test_password")
@patch("src.credentials.PyKeePass", autospec=True)
def test_open_kp_failure(mock_keepass_cls, mock_getpass, mock_base_dir):
    """Tests failure to open KeePass database with multiple retries."""
    mock_keepass_cls.side_effect = Exception("Failed to open")
    gs = ProgramSettings()
    with pytest.raises(SystemExit):
        gs._open_kp(retry=3)
    assert logger.critical_messages
    mock_keepass_cls.assert_called()
    assert len(mock_keepass_cls.mock_calls) == 3


def test_now_property(mock_base_dir):
    """Verifies the functionality of the now property."""
    gs = ProgramSettings()
    assert isinstance(gs.now, str)
    assert len(gs.now) == 17


@patch("src.credentials.PyKeePass", autospec=True)
def test_load_aliexpress_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load Aliexpress credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_aliexpress_credentials(mock_keepass) is None


@patch("src.credentials.PyKeePass", autospec=True)
def test_load_openai_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load OpenAI credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_openai_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_gemini_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load GoogleAI credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_gemini_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_telegram_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load Telegram credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_telegram_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_discord_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load Discord credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_discord_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_prestashop_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load PrestaShop credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_PrestaShop_credentials(mock_keepass) is None


@patch("src.credentials.PyKeePass", autospec=True)
def test_load_presta_translations_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load Translations credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_presta_translations_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_smtp_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load SMTP credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_smtp_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_facebook_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load Facebook credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_facebook_credentials(mock_keepass) is None

@patch("src.credentials.PyKeePass", autospec=True)
def test_load_gapi_credentials_failure(mock_keepass_cls, mock_base_dir, mock_keepass):
    """Tests failure to load GAPI credentials when KeePass entry is not found."""
    mock_keepass_cls.return_value = mock_keepass
    mock_keepass.find_groups.return_value = MagicMock(entries=[])
    gs = ProgramSettings()
    assert gs._load_gapi_credentials(mock_keepass) is None
```