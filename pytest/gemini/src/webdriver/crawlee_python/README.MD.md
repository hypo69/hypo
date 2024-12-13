```python
import pytest
import json
import os
from unittest.mock import patch, mock_open
from playwright.async_api import async_playwright
from crawlee import PlaywrightCrawler

# Assuming the CrawleePython class is defined in src/webdriver/crawlee_python.py
# You might need to adjust this import based on your actual file structure
from src.webdriver.crawlee_python import CrawleePython 

# Mock the logger to avoid actual logging during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.webdriver.crawlee_python.logger') as mock_logger:
        yield mock_logger


@pytest.fixture
def default_config():
    """Provides a default configuration dictionary for testing."""
    return {
        "max_requests": 10,
        "headless": True,
        "browser_type": "chromium",
        "options": ["--disable-dev-shm-usage", "--no-sandbox", "--disable-gpu"],
        "user_agent": "Test User Agent",
        "proxy": {
            "enabled": False,
            "server": "http://proxy.example.com:8080",
            "username": "user",
            "password": "password",
        },
        "viewport": {"width": 1280, "height": 720},
        "timeout": 30000,
        "ignore_https_errors": False,
    }


@pytest.fixture
def mock_json_file(default_config):
    """Mocks reading from the crawlee_python.json file."""
    def _mock_json_file(config_override=None):
        config = default_config.copy()
        if config_override:
            config.update(config_override)
        
        mock_file = mock_open(read_data=json.dumps(config))
        with patch("builtins.open", mock_file):
            yield config
    
    return _mock_json_file


@pytest.mark.asyncio
async def test_crawleepython_default_config(mock_json_file, mock_logger):
    """Test initialization with default configuration from json file."""
    config = await mock_json_file()
    crawler = CrawleePython()
    
    # Assert that the crawler is initialized with the default config
    assert crawler.max_requests == config['max_requests']
    assert crawler.headless == config['headless']
    assert crawler.browser_type == config['browser_type']
    assert crawler.options == config['options']
    assert crawler.user_agent == config['user_agent']
    assert crawler.proxy == config['proxy']
    assert crawler.viewport == config['viewport']
    assert crawler.timeout == config['timeout']
    assert crawler.ignore_https_errors == config['ignore_https_errors']
    
    assert not mock_logger.error.called

@pytest.mark.asyncio
async def test_crawleepython_custom_config(mock_json_file, mock_logger):
    """Test initialization with a combination of default and custom parameters."""
    custom_config = {"max_requests": 20, "headless": False, "user_agent": "Custom Agent", "proxy": {"enabled": True, "server": "http://custom.proxy:8000", "username": "customuser", "password": "custompassword"}}
    config = await mock_json_file(custom_config)
    crawler = CrawleePython(max_requests=custom_config["max_requests"], headless=custom_config["headless"], user_agent=custom_config["user_agent"], proxy=custom_config["proxy"])
    
    assert crawler.max_requests == custom_config["max_requests"]
    assert crawler.headless == custom_config["headless"]
    assert crawler.user_agent == custom_config["user_agent"]
    assert crawler.proxy == custom_config["proxy"]
    
    # check other config remains default from json
    assert crawler.browser_type == config['browser_type']
    assert crawler.options == config['options']
    assert crawler.viewport == config['viewport']
    assert crawler.timeout == config['timeout']
    assert crawler.ignore_https_errors == config['ignore_https_errors']
    assert not mock_logger.error.called

@pytest.mark.asyncio
async def test_crawleepython_invalid_config_missing_keys(mock_json_file, mock_logger):
     """Test that missing keys in config throw an error and log it"""
     
     invalid_config = {"max_requests": 20, "headless": False, "user_agent": "Custom Agent", "proxy": {"enabled": True}}
     await mock_json_file(invalid_config)
     with pytest.raises(KeyError):
        CrawleePython(max_requests=20, headless=False, user_agent="Custom Agent", proxy={"enabled": True})
     mock_logger.error.assert_called()

@pytest.mark.asyncio
async def test_crawleepython_run_invalid_browser_type(mock_json_file, mock_logger):
    """Test that an invalid browser type will raise an error."""
    
    await mock_json_file({"browser_type": "invalid_browser"})
    crawler = CrawleePython(browser_type="invalid_browser")
    
    with pytest.raises(ValueError):
         await crawler.run(["http://example.com"])
         
    mock_logger.error.assert_called()

@pytest.mark.asyncio
async def test_crawleepython_run_valid_urls(mock_json_file, mock_logger):
    """Test that crawler runs correctly with valid URLs."""
    await mock_json_file()
    crawler = CrawleePython()

    urls = ["http://example.com", "http://example.net"]
    
    with patch.object(PlaywrightCrawler, 'run', return_value=None) as mock_run:
        await crawler.run(urls)
    
    mock_run.assert_called_once_with(urls)
    assert not mock_logger.error.called
    
@pytest.mark.asyncio
async def test_crawleepython_run_empty_urls(mock_json_file, mock_logger):
     """Test crawler when no urls are given"""
     await mock_json_file()
     crawler = CrawleePython()
     
     with patch.object(PlaywrightCrawler, 'run', return_value=None) as mock_run:
        await crawler.run([])
        
     mock_run.assert_called_once_with([])
     assert not mock_logger.error.called
```