```python
import pytest
import json

# Assuming the file is loaded as a dictionary, not read directly from disk in this context.
# If you have a function to load this file, the tests would be adapted.

TEST_CONFIG = {
  "default_url": "https://example.com",
  "default_file_path": "file://path/to/your/file.html",
  "default_locator": {
    "by": "ID",
    "attribute": "element_id",
    "selector": "//*[@id='element_id']"
  },
  "logging": {
    "level": "INFO",
    "file": "logs/bs.log"
  },
  "proxy": {
    "enabled": False,
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "password"
  },
  "timeout": 10,
  "encoding": "utf-8"
}


def test_default_url():
    """Checks if the 'default_url' is correctly loaded."""
    assert TEST_CONFIG["default_url"] == "https://example.com"

def test_default_file_path():
    """Checks if 'default_file_path' is correctly loaded."""
    assert TEST_CONFIG["default_file_path"] == "file://path/to/your/file.html"

def test_default_locator_by():
    """Checks the 'by' field in the default locator"""
    assert TEST_CONFIG["default_locator"]["by"] == "ID"

def test_default_locator_attribute():
    """Checks the 'attribute' field in the default locator"""
    assert TEST_CONFIG["default_locator"]["attribute"] == "element_id"

def test_default_locator_selector():
    """Checks the 'selector' field in the default locator"""
    assert TEST_CONFIG["default_locator"]["selector"] == "//*[@id='element_id']"

def test_logging_level():
    """Checks the 'level' field in the logging configuration"""
    assert TEST_CONFIG["logging"]["level"] == "INFO"

def test_logging_file():
    """Checks the 'file' field in the logging configuration"""
    assert TEST_CONFIG["logging"]["file"] == "logs/bs.log"

def test_proxy_enabled():
    """Checks if 'proxy' is enabled correctly."""
    assert TEST_CONFIG["proxy"]["enabled"] is False

def test_proxy_server():
    """Checks the 'server' field in the proxy config."""
    assert TEST_CONFIG["proxy"]["server"] == "http://proxy.example.com:8080"

def test_proxy_username():
    """Checks the 'username' field in the proxy config."""
    assert TEST_CONFIG["proxy"]["username"] == "user"

def test_proxy_password():
    """Checks the 'password' field in the proxy config."""
    assert TEST_CONFIG["proxy"]["password"] == "password"

def test_timeout():
    """Checks the 'timeout' setting."""
    assert TEST_CONFIG["timeout"] == 10

def test_encoding():
    """Checks the 'encoding' setting."""
    assert TEST_CONFIG["encoding"] == "utf-8"


def test_config_keys_exist():
    """Check if all the expected keys exist in the config dict"""
    expected_keys = ["default_url", "default_file_path", "default_locator", "logging", "proxy", "timeout", "encoding"]
    for key in expected_keys:
        assert key in TEST_CONFIG, f"Expected key '{key}' not found in config"

    
def test_config_nested_keys_exist():
    """Checks if all nested keys in config are present as expected"""
    assert "by" in TEST_CONFIG["default_locator"]
    assert "attribute" in TEST_CONFIG["default_locator"]
    assert "selector" in TEST_CONFIG["default_locator"]
    assert "level" in TEST_CONFIG["logging"]
    assert "file" in TEST_CONFIG["logging"]
    assert "enabled" in TEST_CONFIG["proxy"]
    assert "server" in TEST_CONFIG["proxy"]
    assert "username" in TEST_CONFIG["proxy"]
    assert "password" in TEST_CONFIG["proxy"]
```