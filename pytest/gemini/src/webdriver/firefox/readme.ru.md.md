```python
import pytest
from unittest.mock import patch, mock_open
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from hypotez.src.webdriver.firefox import Firefox
from hypotez.src.utils.proxy_tools import ProxyManager


@pytest.fixture
def mock_proxy_manager():
    """Mocks the ProxyManager class."""
    with patch('hypotez.src.webdriver.firefox.ProxyManager') as MockProxyManager:
        mock_instance = MockProxyManager.return_value
        mock_instance.get_working_proxy.return_value = "http://mock_proxy:8080"
        yield mock_instance


@pytest.fixture
def mock_webdriver():
    """Mocks the webdriver.Firefox class."""
    with patch('hypotez.src.webdriver.firefox.webdriver.Firefox') as MockFirefox:
        mock_instance = MockFirefox.return_value
        yield mock_instance


def test_firefox_init_default(mock_proxy_manager, mock_webdriver):
    """Test initialization with default values."""
    browser = Firefox()
    assert browser.profile_name is None
    assert browser.geckodriver_version is None
    assert browser.firefox_version is None
    assert browser.user_agent is None
    assert browser.proxy_file_path is None
    assert browser.options is None
    mock_webdriver.assert_called_once()


def test_firefox_init_with_values(mock_proxy_manager, mock_webdriver):
    """Test initialization with specific values."""
    profile_name = "test_profile"
    geckodriver_version = "v0.30.0"
    firefox_version = "80.0"
    user_agent = "test_user_agent"
    proxy_file_path = "test_proxies.txt"
    options = ["--headless"]

    browser = Firefox(profile_name=profile_name,
                      geckodriver_version=geckodriver_version,
                      firefox_version=firefox_version,
                      user_agent=user_agent,
                      proxy_file_path=proxy_file_path,
                      options=options)

    assert browser.profile_name == profile_name
    assert browser.geckodriver_version == geckodriver_version
    assert browser.firefox_version == firefox_version
    assert browser.user_agent == user_agent
    assert browser.proxy_file_path == proxy_file_path
    assert browser.options == options
    mock_webdriver.assert_called_once()


def test_set_proxy_valid_proxy(mock_proxy_manager, mock_webdriver):
    """Test setting a valid proxy from file."""
    proxy_file_path = "proxies.txt"
    browser = Firefox(proxy_file_path=proxy_file_path)
    
    options = Options()
    browser.set_proxy(options)

    mock_proxy_manager.get_working_proxy.assert_called_once()
    assert options.proxy.http == 'http://mock_proxy:8080'
    assert options.proxy.ssl == 'http://mock_proxy:8080'

def test_set_proxy_no_proxy_file(mock_proxy_manager, mock_webdriver):
    """Test set_proxy method when no proxy file is provided."""
    browser = Firefox()
    options = Options()
    browser.set_proxy(options)
    mock_proxy_manager.get_working_proxy.assert_not_called()
    assert options.proxy is None

@patch("hypotez.src.webdriver.firefox.os.path.exists", return_value=True)
@patch("hypotez.src.webdriver.firefox.shutil.copy2")
def test_payload_success(mock_copy, mock_exists):
    """Test the _payload method with success."""
    browser = Firefox()
    with patch("hypotez.src.webdriver.firefox.open", mock_open(read_data="test_data")) as mock_file:
      browser._payload()
      mock_copy.assert_called()

def test_payload_fail_file_not_exists():
  """Test the _payload method when file not exist."""
  browser = Firefox()
  with pytest.raises(FileNotFoundError):
    with patch("hypotez.src.webdriver.firefox.os.path.exists", return_value=False):
        browser._payload()

def test_payload_fail_open_file():
  """Test the _payload method when can't open file."""
  browser = Firefox()
  with pytest.raises(FileNotFoundError):
    with patch("hypotez.src.webdriver.firefox.os.path.exists", return_value=True):
        with patch("hypotez.src.webdriver.firefox.open", side_effect=FileNotFoundError):
          browser._payload()
```