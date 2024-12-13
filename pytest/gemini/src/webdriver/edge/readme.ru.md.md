```python
import pytest
import json
from unittest.mock import patch, mock_open
from pathlib import Path
from src.webdriver.edge import Edge  # Assuming the Edge class is in this location
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from fake_useragent import UserAgent
from src.logger import logger

# Fixture for a sample edge.json configuration
@pytest.fixture
def sample_config():
    return {
        "options": ["--disable-dev-shm-usage", "--remote-debugging-port=0"],
        "profiles": {
            "os": "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default",
            "internal": "webdriver\\edge\\profiles\\default"
        },
        "executable_path": {
            "default": "webdrivers\\edge\\123.0.2420.97\\msedgedriver.exe"
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


# Fixture for mocked logger
@pytest.fixture
def mock_logger():
    with patch("src.webdriver.edge.logger") as mock:
        yield mock

# Mock the UserAgent class
@pytest.fixture
def mock_user_agent():
    with patch("src.webdriver.edge.UserAgent") as mock:
        mock.return_value.random = "Fake User Agent"
        yield mock


# Test case for loading configuration from a valid file
def test_load_config_from_file(sample_config, mock_user_agent):
    """Tests that the configuration is loaded correctly from a JSON file."""
    config_file_path = "edge.json"
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
        edge = Edge()
        assert edge.config == sample_config

# Test case for handling a missing configuration file
def test_load_config_missing_file(mock_logger, mock_user_agent):
    """Tests the behavior when the configuration file is missing."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            Edge()
    mock_logger.error.assert_called_with(
        "Configuration file 'edge.json' not found."
    )

# Test case for handling an invalid configuration file
def test_load_config_invalid_json(mock_logger, mock_user_agent):
    """Tests the behavior when the configuration file is invalid JSON."""
    invalid_json = "invalid json"
    with patch("builtins.open", mock_open(read_data=invalid_json)):
         with pytest.raises(json.JSONDecodeError):
             Edge()
    mock_logger.error.assert_called_with(
         f"Error loading configuration file 'edge.json': Expecting value: line 1 column 1 (char 0)"
    )

# Test case for default user agent if not provided
def test_default_user_agent(mock_user_agent):
     """Tests that a default user agent is used if none is specified."""
     with patch("builtins.open", mock_open(read_data=json.dumps({}))):
          edge = Edge()
          assert edge.user_agent == mock_user_agent.return_value.random

# Test case for using a provided user agent
def test_custom_user_agent(sample_config, mock_user_agent):
    """Tests that a custom user agent is used if it's specified."""
    custom_user_agent = "Custom User Agent"
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
         edge = Edge(user_agent=custom_user_agent)
         assert edge.user_agent == custom_user_agent
         mock_user_agent.assert_not_called()  # Ensure fake_useragent is not called if user_agent is provided


# Test case for creating options
def test_create_options(sample_config, mock_user_agent):
    """Tests that EdgeOptions are correctly created based on the config and custom options."""
    custom_options = ["--headless", "--disable-gpu"]
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
        edge = Edge(options=custom_options)
        options = edge._create_options()
        assert isinstance(options, EdgeOptions)
        for opt in sample_config["options"]:
            assert opt in options.to_capabilities()['ms:edgeOptions']['args']
        for opt in custom_options:
             assert opt in options.to_capabilities()['ms:edgeOptions']['args']


# Test case for creating service
def test_create_service(sample_config, mock_user_agent):
    """Tests that EdgeService is correctly created from the config."""
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
        edge = Edge()
        service = edge._create_service()
        assert isinstance(service, EdgeService)
        assert service.path == sample_config['executable_path']['default']


# Test case for setting up headers
def test_setup_headers(sample_config, mock_user_agent):
    """Tests that headers are correctly set in the EdgeOptions."""
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
         edge = Edge()
         options = EdgeOptions()
         edge._setup_headers(options)
         for header, value in sample_config['headers'].items():
              assert options.to_capabilities()['goog:chromeOptions']['headers'][header] == value

# Test case for singleton pattern
def test_singleton_pattern(sample_config, mock_user_agent):
    """Tests that the singleton pattern ensures only one instance of the Edge driver."""
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
        edge1 = Edge()
        edge2 = Edge()
        assert edge1 is edge2


# Test case for get method, verifying the driver is called
def test_get_method(sample_config, mock_user_agent):
     """Tests that get method calls the driver's get method."""
     with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
         edge = Edge()
         with patch.object(edge.driver, "get") as mock_get:
              url = "https://example.com"
              edge.get(url)
              mock_get.assert_called_with(url)


# Test case for quit method, verifying driver's quit is called
def test_quit_method(sample_config, mock_user_agent):
     """Tests that quit method calls the driver's quit method."""
     with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
         edge = Edge()
         with patch.object(edge.driver, "quit") as mock_quit:
              edge.quit()
              mock_quit.assert_called()

# Test for init webdriver with error from selenium
def test_init_webdriver_error(sample_config, mock_logger, mock_user_agent):
    """Test for handling an exception during webdriver initialization."""
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
        with patch("selenium.webdriver.Edge", side_effect=Exception("Initialization failed")):
              with pytest.raises(Exception, match="Initialization failed"):
                  Edge()
        mock_logger.error.assert_called_with("Error during Edge WebDriver initialization: Initialization failed")


# Test case for handling error when creating Edge Service
def test_create_service_error(sample_config, mock_logger, mock_user_agent):
    """Tests that an exception is logged when an error occurs during service creation."""
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_config))):
        with patch("selenium.webdriver.edge.service.Service", side_effect=Exception("Service creation error")):
            with pytest.raises(Exception, match="Service creation error"):
                Edge()
        mock_logger.error.assert_called_with("Error during Edge Service initialization: Service creation error")

```