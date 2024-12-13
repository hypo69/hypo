```python
import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from pathlib import Path
from hypotez.src.webdriver.crawlee_python.crawlee_python import CrawleePython
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext

@pytest.fixture
def mock_playwright_crawler():
    """Mocks the PlaywrightCrawler class."""
    with patch("hypotez.src.webdriver.crawlee_python.crawlee_python.PlaywrightCrawler", autospec=True) as MockCrawler:
        mock_crawler_instance = MockCrawler.return_value
        mock_crawler_instance.router.default_handler = AsyncMock()
        mock_crawler_instance.run = AsyncMock()
        mock_crawler_instance.export_data = AsyncMock()
        mock_crawler_instance.get_data = AsyncMock(return_value={"mock_data": "test"})
        yield mock_crawler_instance


@pytest.fixture
def mock_playwright_crawling_context():
    """Mocks the PlaywrightCrawlingContext class."""
    mock_context = AsyncMock(spec=PlaywrightCrawlingContext)
    mock_context.request.url = "https://www.example.com"
    mock_context.page.title = AsyncMock(return_value="Example Domain")
    mock_context.page.content = AsyncMock(return_value="<html><body><h1>Example</h1></body></html>")
    mock_context.enqueue_links = AsyncMock()
    mock_context.push_data = AsyncMock()
    mock_context.log.info = AsyncMock()
    return mock_context



def test_crawleepython_initialization():
    """Checks if CrawleePython initializes correctly with default values."""
    crawler = CrawleePython()
    assert crawler.max_requests == 5
    assert crawler.headless is False
    assert crawler.browser_type == "firefox"
    assert crawler.options == []
    assert crawler.crawler is None

def test_crawleepython_initialization_custom_values():
    """Checks if CrawleePython initializes correctly with custom values."""
    crawler = CrawleePython(max_requests=10, headless=True, browser_type="chromium", options=["--disable-gpu"])
    assert crawler.max_requests == 10
    assert crawler.headless is True
    assert crawler.browser_type == "chromium"
    assert crawler.options == ["--disable-gpu"]
    assert crawler.crawler is None

@pytest.mark.asyncio
async def test_setup_crawler(mock_playwright_crawler):
    """Checks if setup_crawler correctly configures PlaywrightCrawler."""
    crawler = CrawleePython()
    await crawler.setup_crawler()
    mock_playwright_crawler.assert_called_once_with(
        max_requests_per_crawl=5, headless=False, browser_type="firefox", launch_options={"args": []}
    )
    assert crawler.crawler is not None

@pytest.mark.asyncio
async def test_setup_crawler_with_options(mock_playwright_crawler):
    """Checks if setup_crawler correctly configures PlaywrightCrawler with launch options."""
    options = ["--disable-gpu", "--no-sandbox"]
    crawler = CrawleePython(options=options)
    await crawler.setup_crawler()
    mock_playwright_crawler.assert_called_once_with(
        max_requests_per_crawl=5, headless=False, browser_type="firefox", launch_options={"args": options}
    )
    assert crawler.crawler is not None

@pytest.mark.asyncio
async def test_request_handler(mock_playwright_crawler, mock_playwright_crawling_context):
    """Checks if the request_handler processes the page correctly and enqueues links."""
    crawler = CrawleePython()
    await crawler.setup_crawler()

    request_handler = mock_playwright_crawler.router.default_handler
    await request_handler(mock_playwright_crawling_context)

    mock_playwright_crawling_context.log.info.assert_called_once()
    mock_playwright_crawling_context.enqueue_links.assert_called_once()
    mock_playwright_crawling_context.page.title.assert_called_once()
    mock_playwright_crawling_context.page.content.assert_called_once()
    mock_playwright_crawling_context.push_data.assert_called_once()

    pushed_data = mock_playwright_crawling_context.push_data.call_args[0][0]
    assert pushed_data['url'] == "https://www.example.com"
    assert pushed_data['title'] == "Example Domain"
    assert pushed_data['content'] == "<html><body><h1>Example</h1></body></html>"[:100]

@pytest.mark.asyncio
async def test_run_crawler(mock_playwright_crawler):
    """Checks if run_crawler correctly calls the crawler's run method."""
    crawler = CrawleePython()
    await crawler.setup_crawler()
    urls = ["https://www.example.com", "https://www.example.org"]
    await crawler.run_crawler(urls)
    mock_playwright_crawler.run.assert_called_once_with(urls)


@pytest.mark.asyncio
async def test_export_data(mock_playwright_crawler, tmp_path):
    """Checks if export_data correctly calls the crawler's export_data method."""
    crawler = CrawleePython()
    await crawler.setup_crawler()
    file_path = str(tmp_path / "test.json")
    await crawler.export_data(file_path)
    mock_playwright_crawler.export_data.assert_called_once_with(file_path)


@pytest.mark.asyncio
async def test_get_data(mock_playwright_crawler):
    """Checks if get_data returns the correct data from the crawler."""
    crawler = CrawleePython()
    await crawler.setup_crawler()
    data = await crawler.get_data()
    mock_playwright_crawler.get_data.assert_called_once()
    assert data == {"mock_data": "test"}


@pytest.mark.asyncio
async def test_run_integration(mock_playwright_crawler, tmp_path, caplog):
    """Checks the complete run process with setup, run, and export."""
    crawler = CrawleePython()
    urls = ["https://www.example.com"]
    await crawler.run(urls)

    mock_playwright_crawler.assert_called_once()
    mock_playwright_crawler.run.assert_called_once_with(urls)
    mock_playwright_crawler.export_data.assert_called_once()
    mock_playwright_crawler.get_data.assert_called_once()
    
    assert "Extracted data: dict_items([('mock_data', 'test')])" in caplog.text


@pytest.mark.asyncio
async def test_run_exception_handling(mock_playwright_crawler, caplog):
    """Checks if exceptions during run are correctly caught and logged."""
    mock_playwright_crawler.run.side_effect = Exception("Test Exception")
    crawler = CrawleePython()
    urls = ["https://www.example.com"]
    await crawler.run(urls)
    assert "Crawler failed with an error:" in caplog.text
    assert "Test Exception" in caplog.text


@pytest.mark.asyncio
async def test_run_with_default_output_path(mock_playwright_crawler, tmp_path):
    """Check if the export is to the default path (tmp/results.json)"""
    crawler = CrawleePython()
    urls = ["https://www.example.com"]
    await crawler.run(urls)
    expected_path = str(Path(tmp_path / 'results.json'))
    mock_playwright_crawler.export_data.assert_called_once_with(expected_path)

```