```python
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException

from src.webdriver.firefox.firefox import Firefox
from src.webdriver.proxy import check_proxy, get_proxies_dict
from src.logger.logger import logger
from src import gs

# Fixture for settings
@pytest.fixture
def mock_settings():
    class MockSettings:
        class executable_path:
            geckodriver = "geckodriver"
            firefox_binary = "firefox_binary"
        class profile_directory:
             default = 'os'
             os = str(Path('%LOCALAPPDATA%', 'Mozilla', 'Firefox', 'Profiles'))
             internal = "internal_profile"
        options = ["--headless"]
        headers = type('Headers', (object,), {"user_agent": "test_user_agent"})
        proxy_enabled = True

    return MockSettings()

@pytest.fixture
def mock_j_loads_ns(mock_settings):
    with patch("src.webdriver.firefox.firefox.j_loads_ns", return_value=mock_settings) as mock:
        yield mock

@pytest.fixture
def mock_service():
    with patch("src.webdriver.firefox.firefox.Service", return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def mock_options():
    with patch("src.webdriver.firefox.firefox.Options", return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def mock_firefox_profile():
    with patch("src.webdriver.firefox.firefox.FirefoxProfile", return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def mock_webdriver():
    with patch("src.webdriver.firefox.firefox.WebDriver", return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def mock_useragent():
    with patch("src.webdriver.firefox.firefox.UserAgent") as mock:
        mock_instance = MagicMock()
        mock_instance.random = 'random_user_agent'
        mock.return_value = mock_instance
        yield mock

@pytest.fixture
def mock_get_proxies_dict():
    with patch("src.webdriver.firefox.firefox.get_proxies_dict", return_value={"socks4": [{"host": "127.0.0.1", "port": "1080", "protocol": "socks4"}]}) as mock:
        yield mock

@pytest.fixture
def mock_check_proxy():
    with patch("src.webdriver.firefox.firefox.check_proxy", return_value=True) as mock:
        yield mock

# Test cases for __init__ method
def test_firefox_init_default(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks initialization with default parameters."""
    browser = Firefox()
    mock_j_loads_ns.assert_called_once()
    mock_service.assert_called_once()
    mock_options.assert_called_once()
    mock_firefox_profile.assert_called_once()
    mock_webdriver.assert_called_once()
    mock_useragent.assert_called_once()

def test_firefox_init_with_custom_params(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks initialization with custom parameters."""
    profile_name = "test_profile"
    geckodriver_version = "0.30.0"
    firefox_version = "100.0"
    user_agent = "custom_user_agent"
    proxy_file_path = "path/to/proxy.txt"
    options = ["--kiosk"]
    browser = Firefox(profile_name=profile_name, geckodriver_version=geckodriver_version,
                      firefox_version=firefox_version, user_agent=user_agent,
                      proxy_file_path=proxy_file_path, options=options)
    mock_j_loads_ns.assert_called_once()
    mock_service.assert_called_once()
    mock_options.assert_called_once()
    mock_firefox_profile.assert_called_once()
    mock_webdriver.assert_called_once()
    mock_useragent.assert_called_once()

def test_firefox_init_profile_name_os(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if profile directory is set correctly when profile name is provided and default os dir."""
    profile_name = "test_profile"
    Firefox(profile_name=profile_name)
    expected_profile_dir = str(Path(os.environ.get('LOCALAPPDATA'), 'Mozilla', 'Firefox', 'Profiles', '..', profile_name))
    mock_firefox_profile.assert_called_with(profile_directory=expected_profile_dir)


def test_firefox_init_profile_name_internal(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if profile directory is set correctly when profile name is provided and internal dir."""
    class MockSettings:
        class executable_path:
            geckodriver = "geckodriver"
            firefox_binary = "firefox_binary"
        class profile_directory:
             default = 'internal'
             os = str(Path('%LOCALAPPDATA%', 'Mozilla', 'Firefox', 'Profiles'))
             internal = "internal_profile"
        options = ["--headless"]
        headers = type('Headers', (object,), {"user_agent": "test_user_agent"})
        proxy_enabled = True
    mock_j_loads_ns.return_value = MockSettings()
    profile_name = "test_profile"
    Firefox(profile_name=profile_name)
    expected_profile_dir = str(Path(gs.path.src, "internal_profile").parent / profile_name)
    mock_firefox_profile.assert_called_with(profile_directory=expected_profile_dir)

def test_firefox_init_webdriver_exception(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks how WebDriverException is handled during initialization."""
    mock_webdriver.side_effect = WebDriverException("Test WebDriver Exception")
    browser = Firefox()
    assert browser is None
    logger.critical.assert_called()

def test_firefox_init_exception(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks how other Exceptions are handled during initialization."""
    mock_webdriver.side_effect = Exception("Test Exception")
    browser = Firefox()
    assert browser is None
    logger.critical.assert_called()

def test_firefox_init_options_from_settings(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if options are loaded from settings file."""
    browser = Firefox()
    mock_options.return_value.add_argument.assert_called_with("--headless")

def test_firefox_init_options_from_params(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if options from params are added to the browser."""
    options = ["--kiosk"]
    Firefox(options=options)
    mock_options.return_value.add_argument.assert_called_with("--kiosk")

def test_firefox_init_headers_from_settings(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if headers are loaded from settings file."""
    Firefox()
    mock_options.return_value.add_argument.assert_called_with("--user_agent=test_user_agent")

def test_firefox_init_user_agent_setting(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if user agent is set correctly."""
    Firefox()
    mock_options.return_value.set_preference.assert_called_with('general.useragent.override', 'random_user_agent')

def test_firefox_init_user_agent_custom(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if user agent is set correctly from params."""
    user_agent = 'custom_user_agent'
    Firefox(user_agent=user_agent)
    mock_options.return_value.set_preference.assert_called_with('general.useragent.override', user_agent)


# Test cases for set_proxy method
def test_set_proxy_valid_proxy(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent, mock_get_proxies_dict, mock_check_proxy):
    """Checks if a valid proxy is set."""
    browser = Firefox()
    browser.set_proxy(mock_options.return_value)
    mock_options.return_value.set_preference.assert_called()

def test_set_proxy_no_working_proxy(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent, mock_get_proxies_dict):
    """Checks the behavior when no working proxy is available."""
    with patch("src.webdriver.firefox.firefox.check_proxy", return_value=False):
         browser = Firefox()
         browser.set_proxy(mock_options.return_value)
         mock_options.return_value.set_preference.assert_not_called()
         logger.warning.assert_called_with('Нет доступных прокси в предоставленном файле.')

def test_set_proxy_unknown_protocol(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent, mock_get_proxies_dict, mock_check_proxy):
    """Checks behavior with unknown proxy protocol."""
    mock_get_proxies_dict.return_value = {"unknown": [{"host": "127.0.0.1", "port": "1080", "protocol": "unknown"}]}
    browser = Firefox()
    browser.set_proxy(mock_options.return_value)
    mock_options.return_value.set_preference.assert_not_called()
    logger.warning.assert_called_with("Неизвестный тип прокси: unknown")

def test_set_proxy_http(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent, mock_get_proxies_dict, mock_check_proxy):
    """Checks if http proxy is set correctly."""
    mock_get_proxies_dict.return_value = {"http": [{"host": "127.0.0.1", "port": "1080", "protocol": "http"}]}
    browser = Firefox()
    browser.set_proxy(mock_options.return_value)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.type', 1)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.http', '127.0.0.1')
    mock_options.return_value.set_preference.assert_any_call('network.proxy.http_port', 1080)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.ssl', '127.0.0.1')
    mock_options.return_value.set_preference.assert_any_call('network.proxy.ssl_port', 1080)
    logger.info.assert_called_with("Настройка HTTP Proxy: http://127.0.0.1:1080")

def test_set_proxy_socks4(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent, mock_get_proxies_dict, mock_check_proxy):
    """Checks if socks4 proxy is set correctly."""
    mock_get_proxies_dict.return_value = {"socks4": [{"host": "127.0.0.1", "port": "1080", "protocol": "socks4"}]}
    browser = Firefox()
    browser.set_proxy(mock_options.return_value)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.type', 1)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.socks', '127.0.0.1')
    mock_options.return_value.set_preference.assert_any_call('network.proxy.socks_port', 1080)
    logger.info.assert_called_with("Настройка SOCKS4 Proxy: 127.0.0.1:1080")


def test_set_proxy_socks5(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent, mock_get_proxies_dict, mock_check_proxy):
    """Checks if socks5 proxy is set correctly."""
    mock_get_proxies_dict.return_value = {"socks5": [{"host": "127.0.0.1", "port": "1080", "protocol": "socks5"}]}
    browser = Firefox()
    browser.set_proxy(mock_options.return_value)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.type', 1)
    mock_options.return_value.set_preference.assert_any_call('network.proxy.socks', '127.0.0.1')
    mock_options.return_value.set_preference.assert_any_call('network.proxy.socks_port', 1080)
    logger.info.assert_called_with("Настройка SOCKS5 Proxy: 127.0.0.1:1080")


# Test cases for _payload method
def test_payload_method(mock_j_loads_ns, mock_service, mock_options, mock_firefox_profile, mock_webdriver, mock_useragent):
    """Checks if the payload method correctly sets up attributes."""
    browser = Firefox()
    assert hasattr(browser, 'get_page_lang')
    assert hasattr(browser, 'ready_state')
    assert hasattr(browser, 'get_referrer')
    assert hasattr(browser, 'unhide_DOM_element')
    assert hasattr(browser, 'window_focus')
    assert hasattr(browser, 'execute_locator')
    assert hasattr(browser, 'get_webelement_as_screenshot')
    assert hasattr(browser, 'get_webelement_by_locator')
    assert hasattr(browser, 'get_attribute_by_locator')
    assert hasattr(browser, 'send_message')
    assert hasattr(browser, 'send_key_to_webelement')
```