```python
import pytest
import json
import os
from unittest.mock import patch, mock_open
from playwright.async_api import Browser, Page
from src.webdriver.crawlee_python import CrawleePython
from src.logger import logger  # Assuming logger is set up appropriately


@pytest.fixture
def mock_json_config():
    """Provides a mock crawlee_python.json config for testing."""
    config = {
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
    return config


@pytest.fixture
def mock_browser():
    """Mocks a Playwright browser for testing."""
    class MockBrowser:
        async def new_page(self):
            return MockPage()
        async def close(self):
            pass
    return MockBrowser()


@pytest.fixture
def mock_page():
    """Mocks a Playwright Page for testing."""
    class MockPage:
        async def goto(self, url):
            pass
        async def content(self):
             return "<html><body><h1>Test</h1></body></html>"
        async def close(self):
            pass

    return MockPage()

@pytest.fixture
def mock_playwright_launch(mock_browser):
    """Mocks playwright.launch to return our mock browser."""
    with patch("playwright.async_api.async_playwright") as mock_playwright:
        mock_playwright.return_value.__aenter__.return_value.chromium.launch.return_value = mock_browser
        yield mock_playwright

@pytest.fixture
def mock_logger():
    """Mocks the logger for testing."""
    class MockLogger:
        def info(self, msg):
            pass
        def error(self, msg):
            pass
        def debug(self, msg):
            pass
    return MockLogger()

def test_load_config_from_file(mock_json_config, mock_logger):
    """Test loading configuration from a JSON file."""
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_json_config))):
        crawler = CrawleePython(logger=mock_logger)
        assert crawler.config == mock_json_config
        
def test_load_config_from_file_missing_file(mock_logger):
    """Test handling missing configuration file."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            CrawleePython(logger=mock_logger)

def test_load_config_from_file_invalid_json(mock_logger):
    """Test handling invalid JSON in the config file."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with pytest.raises(json.JSONDecodeError):
            CrawleePython(logger=mock_logger)

def test_constructor_with_overrides(mock_json_config, mock_logger):
    """Test the constructor with override options."""
    crawler = CrawleePython(
        max_requests=5,
        headless=False,
        user_agent="Test User Agent",
        logger = mock_logger,
        config=mock_json_config,
        
    )
    assert crawler.config["max_requests"] == 5
    assert crawler.config["headless"] is False
    assert crawler.config["user_agent"] == "Test User Agent"

def test_constructor_with_no_config(mock_logger):
     """Test the constructor with default configuration if no config is passed."""
     crawler = CrawleePython(logger=mock_logger)
     assert crawler.config["max_requests"] == 10
     assert crawler.config["headless"] == True


@pytest.mark.asyncio
async def test_run_with_valid_urls(mock_playwright_launch,mock_page,mock_logger):
    """Test running the crawler with valid URLs."""
    crawler = CrawleePython(logger=mock_logger)
    urls = ["http://example.com", "http://test.com"]
    with patch.object(crawler, '_process_page', return_value=None) as mock_process_page:
        await crawler.run(urls)
        assert mock_process_page.call_count == len(urls)

@pytest.mark.asyncio
async def test_run_with_empty_urls(mock_playwright_launch,mock_page,mock_logger):
    """Test running the crawler with no URLs."""
    crawler = CrawleePython(logger=mock_logger)
    await crawler.run([])
    # Assert that the crawler didn't try to launch the browser when empty URLs are given
    mock_playwright_launch.assert_not_called()

@pytest.mark.asyncio
async def test_process_page(mock_playwright_launch, mock_page,mock_logger):
    """Test _process_page with valid page and url."""
    crawler = CrawleePython(logger=mock_logger)
    url = "http://example.com"
    browser_mock = mock_playwright_launch.return_value.__aenter__.return_value.chromium.launch.return_value

    with patch.object(browser_mock, 'new_page', return_value=mock_page):
        result = await crawler._process_page(url)
        assert result ==  "<html><body><h1>Test</h1></body></html>"

@pytest.mark.asyncio
async def test_process_page_with_error(mock_playwright_launch, mock_logger):
    """Test handling exceptions in _process_page."""
    crawler = CrawleePython(logger=mock_logger)
    url = "http://example.com"
    browser_mock = mock_playwright_launch.return_value.__aenter__.return_value.chromium.launch.return_value
    with patch.object(browser_mock, 'new_page', side_effect=Exception("Simulated browser error")):
       with pytest.raises(Exception, match="Simulated browser error"):
            await crawler._process_page(url)

@pytest.mark.asyncio
async def test_browser_context_manager_valid(mock_playwright_launch,mock_logger):
    """Test the context manager for playwright browser."""
    crawler = CrawleePython(logger=mock_logger)
    async with crawler._get_browser() as browser:
       assert browser is not None

@pytest.mark.asyncio
async def test_browser_context_manager_error(mock_playwright_launch,mock_logger):
    """Test the context manager for playwright browser handling errors."""
    crawler = CrawleePython(logger=mock_logger)
    mock_playwright_launch.return_value.__aenter__.return_value.chromium.launch.side_effect = Exception("Simulated launch error")
    with pytest.raises(Exception, match="Simulated launch error"):
       async with crawler._get_browser() as browser:
           pass
```