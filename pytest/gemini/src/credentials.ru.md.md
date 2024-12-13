```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from types import SimpleNamespace
import sys
import getpass
from keePass import PyKeePass
from src.credentials import set_project_root, singleton, ProgramSettings


# Fixture to mock the config.json loading
@pytest.fixture
def mock_config_json(tmp_path):
    config_data = {
        "author": {"name": "Test Author"},
        "modes": ["dev", "prod"],
        "paths": {"logs": "test_logs", "temp": "test_temp"},
        "project": {"name": "Test Project", "version": "1.0.0"},
        "time_format": "%Y-%m-%d %H:%M:%S"
    }
    config_file = tmp_path / "src" / "config.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    import json
    with open(config_file, 'w') as f:
        json.dump(config_data, f)
    return config_file



@pytest.fixture
def mock_keepass_file(tmp_path):
    secrets_dir = tmp_path / "src" / "secrets"
    secrets_dir.mkdir(parents=True, exist_ok=True)
    keepass_file = secrets_dir / "credentials.kdbx"
    
    # Create a dummy KeePass file using PyKeePass
    kp = PyKeePass(str(keepass_file), password="test_password")
    group = kp.add_group(kp.root_group, "suppliers")
    group_aliexpress = kp.add_group(group, "aliexpress")
    group_api = kp.add_group(group_aliexpress, "api")
    entry = kp.add_entry(group_api, "Aliexpress API credentials",
                        username="test_aliexpress_user",
                        password="test_aliexpress_password")
    
    group = kp.add_group(kp.root_group, "openai")
    entry_keys = kp.add_entry(group, "OpenAI API keys",
                            username="test_openai_user",
                            password="test_openai_password")
    group_assistants = kp.add_group(group, "assistants")
    entry_assistants = kp.add_entry(group_assistants, "OpenAI assistant IDs",
                                   username="test_openai_assistant_id")
    
    group = kp.add_group(kp.root_group, "gemini")
    entry_keys = kp.add_entry(group, "GoogleAI credentials",
                            username="test_gemini_user",
                            password="test_gemini_password")
    
    group = kp.add_group(kp.root_group, "telegram")
    entry_keys = kp.add_entry(group, "Telegram credentials",
                            username="test_telegram_token")
    
    group = kp.add_group(kp.root_group, "discord")
    entry_keys = kp.add_entry(group, "Discord credentials",
                            username="test_discord_application_id", 
                            password="test_discord_public_key",
                            notes="test_discord_bot_token")
    
    group = kp.add_group(kp.root_group, "prestashop")
    entry_keys = kp.add_entry(group, "PrestaShop credentials",
                            username="test_presta_api_key",
                            password="test_presta_api_domain",
                            notes="test_presta_db_server;test_presta_db_user;test_presta_db_password")
    group_clients = kp.add_group(group, "clients")
    entry_clients = kp.add_entry(group_clients, "PrestaShop client credentials",
                             username="test_presta_client_api_key",
                             password="test_presta_client_api_domain",
                            notes="test_presta_client_db_server;test_presta_client_db_user;test_presta_client_db_password")
    group_translations = kp.add_group(group, "translation")
    entry_translations = kp.add_entry(group_translations, "PrestaShop translation credentials",
                            username="test_presta_translations_server",
                             password="test_presta_translations_port",
                            notes="test_presta_translations_database;test_presta_translations_user;test_presta_translations_password")
    
    group = kp.add_group(kp.root_group, "smtp")
    entry_keys = kp.add_entry(group, "SMTP credentials",
                            username="test_smtp_server",
                             password="test_smtp_port",
                            notes="test_smtp_user;test_smtp_password")
    
    group = kp.add_group(kp.root_group, "facebook")
    entry_keys = kp.add_entry(group, "Facebook credentials",
                            username="test_facebook_app_id",
                            password="test_facebook_app_secret",
                            notes="test_facebook_access_token")
    
    group = kp.add_group(kp.root_group, "google")
    group_gapi = kp.add_group(group, "gapi")
    entry_gapi = kp.add_entry(group_gapi, "Google API credentials",
                            username="test_gapi_api_key")


    kp.close()
    
    return keepass_file


@pytest.fixture
def mock_password_file(tmp_path):
    password_file = tmp_path / "src" / "secrets" / "password.txt"
    password_file.parent.mkdir(parents=True, exist_ok=True)
    with open(password_file, 'w') as f:
        f.write("test_password")
    return password_file


def test_set_project_root_with_marker_file(tmp_path):
    """Test that set_project_root correctly identifies the project root when a marker file exists."""
    marker_file = tmp_path / "pyproject.toml"
    marker_file.touch()
    
    # Ensure that the path is actually in the sys.path
    root_path = set_project_root(marker_files=("pyproject.toml",))
    assert root_path == tmp_path
    assert str(tmp_path) in sys.path
    
def test_set_project_root_no_marker_file(tmp_path):
    """Test that set_project_root returns the script's parent directory when no marker file is found."""
    # Create a subdirectory to simulate the script being located in a subdirectory
    script_dir = tmp_path / "src"
    script_dir.mkdir()
    
    with patch("src.credentials.Path", return_value = script_dir):
        root_path = set_project_root()
    
    assert root_path == script_dir
    assert str(script_dir) in sys.path
    

def test_singleton_decorator():
    """Test the singleton decorator to ensure only one instance of a class is created."""

    @singleton
    class TestClass:
        def __init__(self):
            self.value = 1

    instance1 = TestClass()
    instance2 = TestClass()

    assert instance1 is instance2
    assert instance1.value == 1
    assert instance2.value == 1


def test_programsettings_init_loads_config(mock_config_json, tmp_path):
    """Test that ProgramSettings correctly loads the config from a JSON file."""
    # Ensure that the script path and sys path are correctly set
    with patch("src.credentials.Path", return_value = tmp_path / "src"):
        
            settings = ProgramSettings()
    
    assert settings.config.author.name == "Test Author"
    assert settings.config.project.name == "Test Project"
    assert settings.config.project_name == tmp_path.name
    assert settings.MODE in settings.config.modes

def test_programsettings_init_no_config(tmp_path, caplog):
    """Test that ProgramSettings handles the case where the config.json file is missing."""
    
    with patch("src.credentials.Path", return_value = tmp_path / "src"), \
         patch("src.credentials.j_loads_ns", return_value = None):
        with pytest.raises(SystemExit) as excinfo:
                ProgramSettings()
                
        assert excinfo.type == SystemExit
        assert "Ошибка при загрузке настроек" in caplog.text



def test_programsettings_load_credentials_with_password_file(mock_config_json, mock_keepass_file, mock_password_file, tmp_path):
        """Test that ProgramSettings loads credentials from KeePass with a password file."""
        
        with patch("src.credentials.Path", return_value = tmp_path / "src"):
                settings = ProgramSettings()
                
        assert settings.credentials.aliexpress.api_key
        assert settings.credentials.openai.api_key
        assert settings.credentials.openai.assistant_id
        assert settings.credentials.gemini.api_key
        assert settings.credentials.telegram.token
        assert settings.credentials.discord.application_id
        assert settings.credentials.discord.bot_token
        assert settings.credentials.presta.client.api_key
        assert settings.credentials.presta.translations.server
        assert settings.credentials.smtp.server
        assert settings.credentials.facebook.app_id
        assert settings.credentials.gapi.api_key
        

def test_programsettings_load_credentials_no_password_file(mock_config_json, mock_keepass_file, tmp_path, monkeypatch):
        """Test that ProgramSettings loads credentials with getpass prompt when no password file exists."""
        
        monkeypatch.setattr(getpass, 'getpass', lambda x: 'test_password') #mock getpass
        
        with patch("src.credentials.Path", return_value = tmp_path / "src"):
            settings = ProgramSettings()

        assert settings.credentials.aliexpress.api_key
        assert settings.credentials.openai.api_key
        assert settings.credentials.openai.assistant_id
        assert settings.credentials.gemini.api_key
        assert settings.credentials.telegram.token
        assert settings.credentials.discord.application_id
        assert settings.credentials.discord.bot_token
        assert settings.credentials.presta.client.api_key
        assert settings.credentials.presta.translations.server
        assert settings.credentials.smtp.server
        assert settings.credentials.facebook.app_id
        assert settings.credentials.gapi.api_key

def test_programsettings_load_credentials_invalid_password(mock_config_json, mock_keepass_file, tmp_path, monkeypatch, caplog):
        """Test that ProgramSettings handles incorrect password input for KeePass database."""
        monkeypatch.setattr(getpass, 'getpass', lambda x: 'wrong_password')
        with patch("src.credentials.Path", return_value = tmp_path / "src"), pytest.raises(SystemExit) as excinfo:
            ProgramSettings()
        
        assert excinfo.type == SystemExit
        assert "Не удалось открыть базу данных KeePass" in caplog.text

def test_programsettings_now(mock_config_json, tmp_path):
    """Test the now method to ensure the correct time format is returned."""
    with patch("src.credentials.Path", return_value = tmp_path / "src"):
                settings = ProgramSettings()
    
    current_time = settings.now()
    import datetime
    try:
        datetime.datetime.strptime(current_time, settings.config.time_format)
    except ValueError:
        pytest.fail("time format does not match")

def test_global_programsettings_instance(mock_config_json, mock_keepass_file, mock_password_file, tmp_path):
    """Test the global instance of ProgramSettings"""
    from src.credentials import gs
    with patch("src.credentials.Path", return_value = tmp_path / "src"):
        
        assert gs
        assert gs.config.author.name == "Test Author"
        assert gs.credentials.aliexpress.api_key
        
def test_programsettings_open_kp_retry(mock_config_json, mock_keepass_file, tmp_path, monkeypatch, caplog):
    """Test the _open_kp method for retry logic."""
    monkeypatch.setattr(getpass, 'getpass', lambda x: 'wrong_password') # mock getpass to fail
    with patch("src.credentials.Path", return_value = tmp_path / "src"):
      settings = ProgramSettings()
      
      with pytest.raises(SystemExit) as excinfo:
        settings._open_kp(retry=2)
      assert excinfo.type == SystemExit
      assert "Не удалось открыть базу данных KeePass" in caplog.text
      assert "осталось попыток: 1" in caplog.text
      

def test_programsettings_open_kp_success(mock_config_json, mock_keepass_file, mock_password_file, tmp_path):
    """Test the _open_kp method for successful KeePass database opening."""
    with patch("src.credentials.Path", return_value = tmp_path / "src"):
      settings = ProgramSettings()
      kp = settings._open_kp()
      assert isinstance(kp, PyKeePass)

def test_programsettings_open_kp_no_password(mock_config_json, mock_keepass_file, tmp_path, monkeypatch):
        """Test that ProgramSettings opens the database with getpass if no password is available."""
        monkeypatch.setattr(getpass, 'getpass', lambda x: 'test_password') # mock getpass
        with patch("src.credentials.Path", return_value = tmp_path / "src"):
          settings = ProgramSettings()
          kp = settings._open_kp()
          assert isinstance(kp, PyKeePass)

def test_programsettings_load_credentials_with_notes(mock_config_json, mock_keepass_file, mock_password_file, tmp_path):
    """Test that ProgramSettings correctly load credentials with additional information in the notes field."""
    with patch("src.credentials.Path", return_value = tmp_path / "src"):
        settings = ProgramSettings()
            
    assert settings.credentials.presta.client.db_server
    assert settings.credentials.presta.translations.database
    assert settings.credentials.smtp.user
    assert settings.credentials.facebook.access_token
    
    assert settings.credentials.presta.client.db_server == 'test_presta_db_server'
    assert settings.credentials.presta.translations.database == 'test_presta_translations_database'
    assert settings.credentials.smtp.user == 'test_smtp_user'
    assert settings.credentials.facebook.access_token == 'test_facebook_access_token'
    
```