```python
import pytest
import json
from pathlib import Path
import os

# Define a helper function to load JSON configurations
def load_json_config(file_path):
    """Loads a JSON configuration file."""
    try:
         with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# Test cases for Firefox WebDriver configurations
def test_firefox_config_valid():
    """Checks if firefox.json loads successfully and has the expected keys."""
    config_path = Path("bin/webdrivers/firefox/firefox.json") # Assumes a path relative to current test script, update if needed
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    
    config = load_json_config(config_path)
    assert config is not None, "Failed to load firefox.json config"

    expected_keys = ["options", "profile_directory", "executable_path", "headers", "proxy_enabled"]
    for key in expected_keys:
      assert key in config, f"Missing key: {key} in firefox config"

def test_firefox_config_invalid_path():
     """Checks if load_json_config returns None for a non-existent file."""
     config = load_json_config("nonexistent_firefox.json")
     assert config is None, "Should return None for non-existent file"

def test_firefox_config_invalid_json():
      """Checks if load_json_config returns None for an invalid JSON file."""
      # Create a dummy file with invalid JSON content
      invalid_json_file = "invalid_firefox.json"
      with open(invalid_json_file, 'w') as f:
          f.write("this is not a json")
          
      config = load_json_config(invalid_json_file)
      assert config is None, "Should return None for invalid JSON"
      os.remove(invalid_json_file) # Clean up the dummy file
      
def test_firefox_config_profile_directory():
      """Checks the structure of 'profile_directory' within the firefox.json."""
      config_path = Path("bin/webdrivers/firefox/firefox.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load firefox.json config"
      
      assert "profile_directory" in config, "Missing profile_directory key"
      assert "os" in config["profile_directory"], "Missing 'os' key in profile_directory"
      assert "internal" in config["profile_directory"], "Missing 'internal' key in profile_directory"
      
def test_firefox_config_executable_path():
      """Checks the structure of 'executable_path' within the firefox.json."""
      config_path = Path("bin/webdrivers/firefox/firefox.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load firefox.json config"
      
      assert "executable_path" in config, "Missing executable_path key"
      assert "firefox_binary" in config["executable_path"], "Missing 'firefox_binary' key in executable_path"
      assert "geckodriver" in config["executable_path"], "Missing 'geckodriver' key in executable_path"
      
def test_firefox_config_headers():
      """Checks the structure of 'headers' within the firefox.json."""
      config_path = Path("bin/webdrivers/firefox/firefox.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load firefox.json config"
      
      assert "headers" in config, "Missing headers key"
      assert "User-Agent" in config["headers"], "Missing 'User-Agent' key in headers"
      assert "Accept" in config["headers"], "Missing 'Accept' key in headers"
      

# Test cases for Chrome WebDriver configurations
def test_chrome_config_valid():
    """Checks if chrome.json loads successfully and has the expected keys."""
    config_path = Path("bin/webdrivers/chrome/chrome.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    
    config = load_json_config(config_path)
    assert config is not None, "Failed to load chrome.json config"

    expected_keys = ["options", "profile_directory", "executable_path", "headers", "proxy_enabled"]
    for key in expected_keys:
      assert key in config, f"Missing key: {key} in chrome config"

def test_chrome_config_profile_directory():
      """Checks the structure of 'profile_directory' within the chrome.json."""
      config_path = Path("bin/webdrivers/chrome/chrome.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load chrome.json config"
      
      assert "profile_directory" in config, "Missing profile_directory key"
      assert "os" in config["profile_directory"], "Missing 'os' key in profile_directory"
      assert "internal" in config["profile_directory"], "Missing 'internal' key in profile_directory"
      
def test_chrome_config_executable_path():
      """Checks the structure of 'executable_path' within the chrome.json."""
      config_path = Path("bin/webdrivers/chrome/chrome.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load chrome.json config"
      
      assert "executable_path" in config, "Missing executable_path key"
      assert "chrome_binary" in config["executable_path"], "Missing 'chrome_binary' key in executable_path"
      assert "chromedriver" in config["executable_path"], "Missing 'chromedriver' key in executable_path"
      
def test_chrome_config_headers():
      """Checks the structure of 'headers' within the chrome.json."""
      config_path = Path("bin/webdrivers/chrome/chrome.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load chrome.json config"
      
      assert "headers" in config, "Missing headers key"
      assert "User-Agent" in config["headers"], "Missing 'User-Agent' key in headers"
      assert "Accept" in config["headers"], "Missing 'Accept' key in headers"


# Test cases for Edge WebDriver configurations
def test_edge_config_valid():
    """Checks if edge.json loads successfully and has the expected keys."""
    config_path = Path("bin/webdrivers/edge/edge.json")
    if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
    
    config = load_json_config(config_path)
    assert config is not None, "Failed to load edge.json config"

    expected_keys = ["options", "profiles", "executable_path", "headers", "proxy_enabled"]
    for key in expected_keys:
        assert key in config, f"Missing key: {key} in edge config"

def test_edge_config_profiles():
    """Checks the structure of 'profiles' within the edge.json."""
    config_path = Path("bin/webdrivers/edge/edge.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load edge.json config"
    
    assert "profiles" in config, "Missing profiles key"
    assert "os" in config["profiles"], "Missing 'os' key in profiles"
    assert "internal" in config["profiles"], "Missing 'internal' key in profiles"

def test_edge_config_executable_path():
    """Checks the structure of 'executable_path' within the edge.json."""
    config_path = Path("bin/webdrivers/edge/edge.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load edge.json config"
    
    assert "executable_path" in config, "Missing executable_path key"
    assert "edge_binary" in config["executable_path"], "Missing 'edge_binary' key in executable_path"
    assert "edgedriver" in config["executable_path"], "Missing 'edgedriver' key in executable_path"

def test_edge_config_headers():
    """Checks the structure of 'headers' within the edge.json."""
    config_path = Path("bin/webdrivers/edge/edge.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load edge.json config"
    
    assert "headers" in config, "Missing headers key"
    assert "User-Agent" in config["headers"], "Missing 'User-Agent' key in headers"
    assert "Accept" in config["headers"], "Missing 'Accept' key in headers"


# Test cases for Playwright Crawler configurations
def test_playwright_config_valid():
    """Checks if playwrid.json loads successfully and has the expected keys."""
    config_path = Path("bin/webdrivers/playwrid.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    
    config = load_json_config(config_path)
    assert config is not None, "Failed to load playwrid.json config"

    expected_keys = ["max_requests", "headless", "browser_type", "options", "user_agent",
                     "proxy", "viewport", "timeout", "ignore_https_errors"]
    for key in expected_keys:
        assert key in config, f"Missing key: {key} in playwright config"


def test_playwright_config_proxy():
    """Checks the structure of 'proxy' within the playwrid.json."""
    config_path = Path("bin/webdrivers/playwrid.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load playwrid.json config"

    assert "proxy" in config, "Missing proxy key"
    assert "enabled" in config["proxy"], "Missing 'enabled' key in proxy"
    assert "server" in config["proxy"], "Missing 'server' key in proxy"
    assert "username" in config["proxy"], "Missing 'username' key in proxy"
    assert "password" in config["proxy"], "Missing 'password' key in proxy"


def test_playwright_config_viewport():
      """Checks the structure of 'viewport' within the playwrid.json."""
      config_path = Path("bin/webdrivers/playwrid.json")
      if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"
      config = load_json_config(config_path)
      assert config is not None, "Failed to load playwrid.json config"
      
      assert "viewport" in config, "Missing viewport key"
      assert "width" in config["viewport"], "Missing 'width' key in viewport"
      assert "height" in config["viewport"], "Missing 'height' key in viewport"


# Test cases for BeautifulSoup and XPath Parser configurations
def test_bs_config_valid():
    """Checks if bs.json loads successfully and has the expected keys."""
    config_path = Path("bin/webdrivers/bs.json")
    if not os.path.exists(config_path):
        assert False, f"Config file not found at path: {config_path}"

    config = load_json_config(config_path)
    assert config is not None, "Failed to load bs.json config"

    expected_keys = ["default_url", "default_file_path", "default_locator",
                     "logging", "proxy", "timeout", "encoding"]
    for key in expected_keys:
        assert key in config, f"Missing key: {key} in bs config"


def test_bs_config_default_locator():
    """Checks the structure of 'default_locator' within the bs.json."""
    config_path = Path("bin/webdrivers/bs.json")
    if not os.path.exists(config_path):
       assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load bs.json config"

    assert "default_locator" in config, "Missing default_locator key"
    assert "by" in config["default_locator"], "Missing 'by' key in default_locator"
    assert "attribute" in config["default_locator"], "Missing 'attribute' key in default_locator"
    assert "selector" in config["default_locator"], "Missing 'selector' key in default_locator"


def test_bs_config_logging():
    """Checks the structure of 'logging' within the bs.json."""
    config_path = Path("bin/webdrivers/bs.json")
    if not os.path.exists(config_path):
      assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load bs.json config"

    assert "logging" in config, "Missing logging key"
    assert "level" in config["logging"], "Missing 'level' key in logging"
    assert "file" in config["logging"], "Missing 'file' key in logging"


def test_bs_config_proxy():
    """Checks the structure of 'proxy' within the bs.json."""
    config_path = Path("bin/webdrivers/bs.json")
    if not os.path.exists(config_path):
      assert False, f"Config file not found at path: {config_path}"
    config = load_json_config(config_path)
    assert config is not None, "Failed to load bs.json config"
    
    assert "proxy" in config, "Missing proxy key"
    assert "enabled" in config["proxy"], "Missing 'enabled' key in proxy"
    assert "server" in config["proxy"], "Missing 'server' key in proxy"
    assert "username" in config["proxy"], "Missing 'username' key in proxy"
    assert "password" in config["proxy"], "Missing 'password' key in proxy"
```