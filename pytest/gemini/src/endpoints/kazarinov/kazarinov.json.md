```python
import pytest
import json

# Assuming the JSON config is loaded into a dictionary, we can represent it as a fixture
@pytest.fixture
def config_data():
    """Provides the configuration data as a dictionary."""
    return {
        "mode": "test",
        "webdriver_name": "firefox",
        "webdriver_options": [],
        "system_instruction": "system_instruction.txt",
        "questions_list_path": "kazarinov/prompts/train_data/q",
        "url_handlers": {
            "suppliers": [
                "https://morlevi.co.il",
                "https://www.morlevi.co.il",
                "https://grandadvance.co.il",
                "https://www.grandadvance.co.il",
                "https://ksp.co.il",
                "https://www.ksp.co.il",
                "https://ivory.co.il",
                "https://www.ivory.co.il"
            ],
            "onetab": [
                "https://www.one-tab.com"
            ]
        },
        "generation_config": {
            "response_mime_type": "text/plain"
        },
        "telegram": {
            "bot_name": "hypo69_kazarinov_bot",
            "log_path": "bot_logs/<user_id>/<timestamp>.txt"
        },
        "storage": "external_storage",
        "avaiable_storages": [ "data", "google_drive", "external_storage" ]
    }

def test_config_mode(config_data):
    """Checks that the mode is correctly set to "test"."""
    assert config_data["mode"] == "test"

def test_config_webdriver_name(config_data):
    """Checks that the webdriver name is correctly set to "firefox"."""
    assert config_data["webdriver_name"] == "firefox"

def test_config_webdriver_options(config_data):
    """Checks that the webdriver options are an empty list."""
    assert isinstance(config_data["webdriver_options"], list)
    assert not config_data["webdriver_options"]

def test_config_system_instruction(config_data):
    """Checks that the system instruction path is a string."""
    assert isinstance(config_data["system_instruction"], str)
    assert config_data["system_instruction"] == "system_instruction.txt"

def test_config_questions_list_path(config_data):
    """Checks that the question list path is a string."""
    assert isinstance(config_data["questions_list_path"], str)
    assert config_data["questions_list_path"] == "kazarinov/prompts/train_data/q"

def test_config_url_handlers_suppliers(config_data):
    """Checks that the suppliers URLs are correctly configured as a list of strings."""
    assert isinstance(config_data["url_handlers"]["suppliers"], list)
    for url in config_data["url_handlers"]["suppliers"]:
        assert isinstance(url, str)
        assert url.startswith("https://")

def test_config_url_handlers_onetab(config_data):
    """Checks that the onetab URLs are correctly configured as a list of strings."""
    assert isinstance(config_data["url_handlers"]["onetab"], list)
    for url in config_data["url_handlers"]["onetab"]:
        assert isinstance(url, str)
        assert url.startswith("https://")

def test_config_generation_config_mime_type(config_data):
    """Checks that the response mime type is correctly configured."""
    assert config_data["generation_config"]["response_mime_type"] == "text/plain"

def test_config_telegram_bot_name(config_data):
    """Checks that the telegram bot name is a non-empty string."""
    assert isinstance(config_data["telegram"]["bot_name"], str)
    assert config_data["telegram"]["bot_name"] == "hypo69_kazarinov_bot"

def test_config_telegram_log_path(config_data):
    """Checks that the telegram log path is a string with placeholders."""
    assert isinstance(config_data["telegram"]["log_path"], str)
    assert config_data["telegram"]["log_path"] == "bot_logs/<user_id>/<timestamp>.txt"

def test_config_storage(config_data):
    """Checks that the storage is correctly set to "external_storage"."""
    assert config_data["storage"] == "external_storage"

def test_config_available_storages(config_data):
    """Checks that the available storages is a list containing specific strings."""
    assert isinstance(config_data["avaiable_storages"], list)
    assert "data" in config_data["avaiable_storages"]
    assert "google_drive" in config_data["avaiable_storages"]
    assert "external_storage" in config_data["avaiable_storages"]

def test_config_invalid_key_access(config_data):
     """Checks if accessing a non existent key will raise a KeyError."""
     with pytest.raises(KeyError):
         config_data["non_existent_key"]
```