```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def valid_config_data():
    """Provides a valid configuration dictionary for testing."""
    return {
      "max_requests": 10,
      "headless": True,
      "browser_type": "chromium",
      "options": [
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-gpu"
      ],
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
      "proxy": {
        "enabled": False,
        "server": "http://proxy.example.com:8080",
        "username": "user",
        "password": "password"
      },
      "viewport": {
        "width": 1280,
        "height": 720
      },
      "timeout": 30000,
      "ignore_https_errors": False
    }


@pytest.fixture
def invalid_config_data():
    """Provides an invalid configuration dictionary for testing."""
    return {
      "max_requests": "invalid",
      "headless": "not a bool",
      "browser_type": 123,
      "options": "--not-a-list",
      "user_agent": None,
      "proxy": "not a dict",
      "viewport": "not a dict",
      "timeout": "string",
      "ignore_https_errors": 1
    }


def test_valid_config_loading(valid_config_data):
    """Checks that valid config data loads without errors."""
    config = valid_config_data
    assert isinstance(config, dict)
    assert config["max_requests"] == 10
    assert config["headless"] is True
    assert config["browser_type"] == "chromium"
    assert isinstance(config["options"], list)
    assert config["user_agent"] == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    assert isinstance(config["proxy"], dict)
    assert config["proxy"]["enabled"] is False
    assert config["viewport"]["width"] == 1280
    assert config["timeout"] == 30000
    assert config["ignore_https_errors"] is False


def test_invalid_config_loading(invalid_config_data):
    """Checks that invalid config data raises type errors or is handled correctly."""
    config = invalid_config_data
    assert isinstance(config, dict)
    assert isinstance(config["max_requests"], str)
    assert isinstance(config["headless"], str)
    assert isinstance(config["browser_type"], int)
    assert isinstance(config["options"], str)
    assert config["user_agent"] is None
    assert isinstance(config["proxy"], str)
    assert isinstance(config["viewport"], str)
    assert isinstance(config["timeout"], str)
    assert isinstance(config["ignore_https_errors"], int)


def test_config_with_missing_keys():
    """Checks that behavior is graceful when some keys are missing."""
    config = {
        "max_requests": 20,
        "browser_type": "firefox",
         "options": [ "--disable-gpu"]
    }
    assert "max_requests" in config
    assert "browser_type" in config
    assert "options" in config
    assert "headless" not in config
    assert "user_agent" not in config
    assert "proxy" not in config
    assert "viewport" not in config
    assert "timeout" not in config
    assert "ignore_https_errors" not in config
    assert len(config.keys())==3


def test_empty_config():
  """Checks loading with an empty config dict."""
  config = {}
  assert len(config) == 0
```