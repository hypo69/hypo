```python
import pytest
import json

# Fixture to load the configuration from the provided JSON
@pytest.fixture
def playwright_config():
    """Loads and returns the Playwright configuration from the JSON."""
    config_json = """
    {
      "browser_type": "chromium",
      "headless": true,
      "options": [
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-gpu"
      ],
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
      "proxy": {
        "enabled": false,
        "server": "http://proxy.example.com:8080",
        "username": "user",
        "password": "password"
      },
      "viewport": {
        "width": 1280,
        "height": 720
      },
      "timeout": 30000,
      "ignore_https_errors": false
    }
    """
    return json.loads(config_json)


def test_config_browser_type(playwright_config):
    """Checks if the browser type is correctly loaded."""
    assert playwright_config["browser_type"] == "chromium"

def test_config_headless_mode(playwright_config):
    """Checks if the headless mode is set to true."""
    assert playwright_config["headless"] is True

def test_config_options(playwright_config):
    """Checks if the options are loaded correctly."""
    expected_options = ["--disable-dev-shm-usage", "--no-sandbox", "--disable-gpu"]
    assert playwright_config["options"] == expected_options

def test_config_user_agent(playwright_config):
    """Checks if the user agent is loaded correctly."""
    expected_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    assert playwright_config["user_agent"] == expected_user_agent

def test_config_proxy_enabled(playwright_config):
    """Checks if the proxy enabled property is false by default."""
    assert playwright_config["proxy"]["enabled"] is False


def test_config_proxy_settings(playwright_config):
    """Checks if the proxy settings are loaded correctly."""
    expected_proxy = {
        "enabled": False,
        "server": "http://proxy.example.com:8080",
        "username": "user",
        "password": "password"
    }
    assert playwright_config["proxy"] == expected_proxy


def test_config_viewport_dimensions(playwright_config):
    """Checks if the viewport dimensions are loaded correctly."""
    expected_viewport = {"width": 1280, "height": 720}
    assert playwright_config["viewport"] == expected_viewport


def test_config_timeout(playwright_config):
    """Checks if the timeout value is loaded correctly."""
    assert playwright_config["timeout"] == 30000


def test_config_ignore_https_errors(playwright_config):
    """Checks if the ignore_https_errors is set to false by default."""
    assert playwright_config["ignore_https_errors"] is False


def test_config_invalid_input():
    """Checks if an invalid json will raise error during parsing"""
    invalid_config = "invalid json string"

    with pytest.raises(json.JSONDecodeError):
       json.loads(invalid_config)
    
def test_config_empty_json():
    """Checks if an empty JSON input will not raise any errors"""
    empty_config = "{}"
    assert json.loads(empty_config) == {}
```