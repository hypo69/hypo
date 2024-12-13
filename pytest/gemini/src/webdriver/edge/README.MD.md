```python
import pytest
import json
from unittest.mock import patch, mock_open
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

# Assume that the Edge class is defined in src/webdriver/edge.py
# You might need to adjust the import path based on your project structure
from src.webdriver.edge import Edge
from src.logger import logger  # Assuming you have a logger setup

@pytest.fixture
def mock_edge_json_config():
    """Provides mock data for the edge.json configuration."""
    return {
      "options": [
        "--disable-dev-shm-usage",
        "--remote-debugging-port=0"
      ],
      "profiles": {
        "os": "%LOCALAPPDATA%\\\\Microsoft\\\\Edge\\\\User Data\\\\Default",
        "internal": "webdriver\\\\edge\\\\profiles\\\\default"
      },
      "executable_path": {
        "default": "webdrivers\\\\edge\\\\123.0.2420.97\\\\msedgedriver.exe"
      },
      "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive"
      }
    }

@pytest.fixture
def mock_edge_json_file(mock_edge_json_config):
    """Mocks the opening and reading of the edge.json file."""
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_edge_json_config))) as mock_file:
        yield mock_file

@pytest.fixture
def mock_webdriver_edge():
     """Mocks the webdriver.Edge constructor"""
     with patch("src.webdriver.edge.webdriver.Edge") as mock_edge:
         yield mock_edge

def test_edge_initialization_with_default_config(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if Edge WebDriver is initialized with correct options from config
    file when no user-provided options or user-agent are given
    """
    edge_driver = Edge()
    
    # Verify that webdriver.Edge was called with the correct options based on config
    mock_webdriver_edge.assert_called_once()
    args, kwargs = mock_webdriver_edge.call_args
    assert isinstance(kwargs['options'], EdgeOptions)
    assert kwargs['options'].arguments == mock_edge_json_config["options"]
    assert kwargs['executable_path'] == mock_edge_json_config["executable_path"]["default"]

    #Verify the headers are set as expected
    assert edge_driver.headers == mock_edge_json_config["headers"]
    
def test_edge_initialization_with_custom_options(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if Edge WebDriver is initialized with custom options provided by the user
    """
    custom_options = ["--headless", "--disable-gpu"]
    edge_driver = Edge(options=custom_options)
    
    # Verify that webdriver.Edge was called with the correct options
    mock_webdriver_edge.assert_called_once()
    args, kwargs = mock_webdriver_edge.call_args
    assert isinstance(kwargs['options'], EdgeOptions)
    assert set(kwargs['options'].arguments) == set(mock_edge_json_config["options"] + custom_options)
    
    #Verify headers are set from the config file
    assert edge_driver.headers == mock_edge_json_config["headers"]

def test_edge_initialization_with_custom_user_agent(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if Edge WebDriver is initialized with a custom user agent provided by the user
    """
    custom_user_agent = "Test User Agent"
    edge_driver = Edge(user_agent=custom_user_agent)

    # Verify that webdriver.Edge was called with the correct options
    mock_webdriver_edge.assert_called_once()
    args, kwargs = mock_webdriver_edge.call_args
    assert isinstance(kwargs['options'], EdgeOptions)
    assert kwargs['options'].arguments == mock_edge_json_config["options"]

    # Verify the user agent is updated
    assert edge_driver.headers['User-Agent'] == custom_user_agent

def test_edge_initialization_with_nonexistent_config(mock_webdriver_edge, caplog):
    """
    Checks if error is logged when edge.json does not exist and defaults are used.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        edge_driver = Edge()

    # Assert that webdriver is still called but with no specific options
    mock_webdriver_edge.assert_called_once()
    args, kwargs = mock_webdriver_edge.call_args
    assert isinstance(kwargs['options'], EdgeOptions)
    assert kwargs['options'].arguments == []

    # Verify an error log was added
    assert "Error loading edge.json configuration: [Errno 2] No such file or directory" in caplog.text

def test_edge_initialization_with_invalid_config(mock_webdriver_edge, caplog):
    """
    Checks if error is logged when edge.json has invalid json and defaults are used.
    """
    with patch("builtins.open", mock_open(read_data="invalid json")):
         edge_driver = Edge()
    
    # Assert that webdriver is still called but with no specific options
    mock_webdriver_edge.assert_called_once()
    args, kwargs = mock_webdriver_edge.call_args
    assert isinstance(kwargs['options'], EdgeOptions)
    assert kwargs['options'].arguments == []

    # Verify an error log was added
    assert "Error parsing edge.json configuration: Expecting value: line 1 column 1 (char 0)" in caplog.text

def test_edge_singleton_pattern(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if the Edge class follows the Singleton pattern.
    """
    edge1 = Edge()
    edge2 = Edge()
    
    #Check that it was only called one time with the browser driver
    mock_webdriver_edge.assert_called_once()
    
    # Assert that the two instances are the same
    assert edge1 is edge2

def test_edge_get(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if the get method of the webdriver is called when get() is called on Edge
    """
    mock_instance = mock_webdriver_edge.return_value
    edge_driver = Edge()
    url = "https://www.example.com"
    edge_driver.get(url)

    mock_instance.get.assert_called_once_with(url)

def test_edge_quit(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if the quit method of the webdriver is called when quit() is called on Edge
    """
    mock_instance = mock_webdriver_edge.return_value
    edge_driver = Edge()
    edge_driver.quit()

    mock_instance.quit.assert_called_once()

def test_edge_get_with_singleton_instance(mock_edge_json_file, mock_edge_json_config, mock_webdriver_edge):
    """
    Checks if a new window is opened when get() is called on an existing Edge instance.
    """
    mock_instance = mock_webdriver_edge.return_value
    edge_driver1 = Edge()
    url = "https://www.example.com"
    edge_driver1.get(url)
    
    edge_driver2 = Edge()
    url2 = "https://www.test.com"
    edge_driver2.get(url2)

    # Ensure that get method was called twice and with different URLS
    assert mock_instance.get.call_count == 2
    mock_instance.get.assert_any_call(url)
    mock_instance.get.assert_any_call(url2)

    # Ensure that the browser driver was only called one time to create a new instance
    mock_webdriver_edge.assert_called_once()
```