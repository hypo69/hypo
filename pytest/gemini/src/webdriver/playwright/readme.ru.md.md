```python
import pytest
import json
from unittest.mock import patch, mock_open
from playwright.sync_api import sync_playwright
from src.webdriver.playwright import Playwrid
from src.logger import logger  # Assuming logger is used


@pytest.fixture
def default_config():
    """Provides a default configuration for testing."""
    return {
        "browser_type": "chromium",
        "headless": True,
        "options": ["--disable-dev-shm-usage", "--no-sandbox", "--disable-gpu"],
        "user_agent": "Test User Agent",
        "proxy": {"enabled": False, "server": "http://test.proxy:8080", "username": "user", "password": "password"},
        "viewport": {"width": 1024, "height": 768},
        "timeout": 10000,
        "ignore_https_errors": False,
    }


@pytest.fixture
def mock_playwright():
    """Mocks the playwright.sync_api.sync_playwright context manager."""
    with patch("src.webdriver.playwright.sync_playwright") as mock:
        yield mock


def test_playwrid_init_with_default_config(default_config, mock_playwright):
    """
    Test that Playwrid initializes correctly with default configuration from file.
    It checks if the settings are properly loaded from a JSON config file.
    """
    config_str = json.dumps(default_config)
    with patch("builtins.open", mock_open(read_data=config_str)):
        browser = Playwrid()

    assert browser.config == default_config, "Configuration should match the loaded data."
    assert browser.browser_type == default_config["browser_type"], "Browser type should match the loaded config."
    assert browser.headless == default_config["headless"], "Headless mode should match the loaded config."
    assert browser.user_agent == default_config["user_agent"], "User agent should match the loaded config."
    assert browser.proxy == default_config["proxy"], "Proxy settings should match the loaded config."
    assert browser.viewport == default_config["viewport"], "Viewport settings should match the loaded config."
    assert browser.timeout == default_config["timeout"], "Timeout should match the loaded config."
    assert browser.ignore_https_errors == default_config["ignore_https_errors"], "Ignore https errors should match the loaded config."
    mock_playwright.assert_called()
    mock_playwright.return_value.__enter__.assert_called()
    mock_playwright.return_value.__enter__.return_value.chromium.launch.assert_called()
    mock_playwright.return_value.__enter__.return_value.chromium.launch.assert_called_with(
        headless=default_config["headless"],
        args=default_config["options"],
        user_agent=default_config["user_agent"],
        proxy=None,
        ignore_https_errors=default_config["ignore_https_errors"]
    )


def test_playwrid_init_with_custom_options(default_config, mock_playwright):
    """
    Test initializing Playwrid with custom options.
    It verifies that user-provided options override defaults.
    """
    config_str = json.dumps(default_config)
    with patch("builtins.open", mock_open(read_data=config_str)):
        browser = Playwrid(options=["--start-maximized"], headless=False, user_agent="Custom User Agent")

    assert browser.headless == False, "Headless mode should be overridden by custom option."
    assert browser.user_agent == "Custom User Agent", "User agent should be overridden by custom option."
    mock_playwright.return_value.__enter__.return_value.chromium.launch.assert_called_with(
        headless=False,
        args=["--start-maximized"],
        user_agent="Custom User Agent",
        proxy=None,
        ignore_https_errors=default_config["ignore_https_errors"]
    )


def test_playwrid_init_with_invalid_config_file(mock_playwright, caplog):
    """
    Test handling of invalid JSON config file.
    It ensures proper logging of errors when the config file is invalid.
    """
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with pytest.raises(json.JSONDecodeError):
             Playwrid()
    
    assert "Ошибка в файле playwrid.json" in caplog.text, "Error log should be present when config file loading fails"



def test_playwrid_init_with_no_config_file(mock_playwright, caplog):
    """
    Test handling of missing config file.
    It validates that the system falls back to default if file is missing and log an error message.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        browser = Playwrid()

    assert browser.config == {}, "Config should be empty"
    assert "Не найден файл конфигурации playwrid.json" in caplog.text, "Error log should be present when config file not found"
    mock_playwright.return_value.__enter__.return_value.chromium.launch.assert_called() # Default browser should launch


def test_playwrid_start(default_config, mock_playwright):
    """
    Test the start method of Playwrid.
    It checks if a new page is created and navigates to the correct URL.
    """
    config_str = json.dumps(default_config)
    with patch("builtins.open", mock_open(read_data=config_str)):
        browser = Playwrid()
    
    test_url = "https://test.example.com"
    browser.start(test_url)

    mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.assert_called()
    mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value.goto.assert_called_with(test_url, timeout=default_config["timeout"])


def test_playwrid_start_with_custom_timeout(default_config, mock_playwright):
    """
    Test start method with custom timeout passed to it.
    It should override the default timeout from config.
    """
    config_str = json.dumps(default_config)
    with patch("builtins.open", mock_open(read_data=config_str)):
        browser = Playwrid()
    
    test_url = "https://test.example.com"
    custom_timeout = 5000
    browser.start(test_url, timeout=custom_timeout)

    mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value.goto.assert_called_with(test_url, timeout=custom_timeout)


def test_playwrid_start_with_exception(default_config, mock_playwright, caplog):
    """
    Test start method with an exception.
    It should log the exception.
    """
    config_str = json.dumps(default_config)
    with patch("builtins.open", mock_open(read_data=config_str)):
        browser = Playwrid()

    mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value.goto.side_effect = Exception("Test exception")
    test_url = "https://test.example.com"

    browser.start(test_url)

    assert "Ошибка при переходе на страницу" in caplog.text, "Error log should be present when page navigation fails"
    

def test_playwrid_with_proxy_enabled(default_config, mock_playwright):
    """
    Test Playwrid with proxy enabled.
    It should launch browser with proxy settings.
    """
    default_config["proxy"]["enabled"] = True
    config_str = json.dumps(default_config)

    with patch("builtins.open", mock_open(read_data=config_str)):
      browser = Playwrid()
    
    mock_playwright.return_value.__enter__.return_value.chromium.launch.assert_called_with(
      headless=default_config["headless"],
      args=default_config["options"],
      user_agent=default_config["user_agent"],
      proxy=default_config["proxy"],
      ignore_https_errors=default_config["ignore_https_errors"]
    )


def test_playwrid_close(default_config, mock_playwright):
    """
    Test close method.
    It should call the browser context close method.
    """
    config_str = json.dumps(default_config)
    with patch("builtins.open", mock_open(read_data=config_str)):
        browser = Playwrid()

    browser.close()

    mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value.close.assert_called()
```