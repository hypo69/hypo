```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException
from types import SimpleNamespace

from src.webdriver.chrome.chrome import Chrome
from src.utils.jjson import j_loads_ns
from src import gs

# Fixture to mock UserAgent for consistent test behavior
@pytest.fixture
def mock_user_agent():
    with patch('src.webdriver.chrome.chrome.UserAgent') as mock:
        mock_instance = mock.return_value
        mock_instance.random = 'test_user_agent'
        yield mock

# Fixture to mock j_loads_ns for consistent test config
@pytest.fixture
def mock_j_loads_ns():
    with patch('src.webdriver.chrome.chrome.j_loads_ns') as mock:
        mock.return_value = SimpleNamespace(
            options=['--test-option'],
            headers=SimpleNamespace(test_header='test_value'),
            profile_directory=SimpleNamespace(testing='%LOCALAPPDATA%/test_profile'),
            binary_location=SimpleNamespace(binary='%LOCALAPPDATA%/test_binary')
        )
        yield mock
    
# Fixture to create a mock ChromeOptions object
@pytest.fixture
def mock_chrome_options():
    with patch('src.webdriver.chrome.chrome.ChromeOptions') as mock:
        mock_instance = mock.return_value
        mock_instance.add_argument = MagicMock()
        yield mock_instance

# Fixture to mock ChromeService
@pytest.fixture
def mock_chrome_service():
    with patch('src.webdriver.chrome.chrome.ChromeService') as mock:
        mock_instance = mock.return_value
        yield mock_instance
        

# Fixture to mock webdriver.Chrome for testing initialization 
@pytest.fixture
def mock_webdriver_chrome():
    with patch('src.webdriver.chrome.chrome.webdriver.Chrome') as mock:
        mock_instance = mock.return_value
        mock_instance.window_open = MagicMock()
        yield mock_instance

# Fixture to mock ExecuteLocator and JavaScript
@pytest.fixture
def mock_executors():
    with patch('src.webdriver.chrome.chrome.JavaScript') as mock_js, \
         patch('src.webdriver.chrome.chrome.ExecuteLocator') as mock_locator:
        
        mock_js_instance = mock_js.return_value
        mock_js_instance.get_page_lang = MagicMock()
        mock_js_instance.ready_state = MagicMock()
        mock_js_instance.get_referrer = MagicMock()
        mock_js_instance.unhide_DOM_element = MagicMock()
        mock_js_instance.window_focus = MagicMock()

        mock_locator_instance = mock_locator.return_value
        mock_locator_instance.execute_locator = MagicMock()
        mock_locator_instance.get_webelement_as_screenshot = MagicMock()
        mock_locator_instance.get_webelement_by_locator = MagicMock()
        mock_locator_instance.get_attribute_by_locator = MagicMock()
        mock_locator_instance.send_message = MagicMock()

        yield mock_js_instance, mock_locator_instance

def test_chrome_singleton(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks that the Chrome class is a singleton."""
    instance1 = Chrome()
    instance2 = Chrome()
    assert instance1 is instance2
    instance2.window_open.assert_called_once()

def test_chrome_init_with_defaults(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks correct initialization with default parameters."""
    chrome = Chrome()

    mock_user_agent.assert_called_once()
    mock_j_loads_ns.assert_called_once()
    
    # verify that options were passed through correctly
    mock_chrome_options.add_argument.assert_any_call('--test-option')
    mock_chrome_options.add_argument.assert_any_call('--test_header=test_value')
    mock_chrome_options.add_argument.assert_any_call(f'user-data-dir={Path(Path.home() / "AppData" / "Local" / "test_profile")}')
    assert mock_chrome_options.binary_location == str(Path(Path.home() / "AppData" / "Local" / "test_binary"))
    
    # Verify that the service was initialized with the correct path
    mock_chrome_service.assert_called_once()

    mock_webdriver_chrome.assert_called_once()
    
def test_chrome_init_with_custom_user_agent_and_options(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks correct initialization with custom user-agent and options."""
    custom_user_agent = 'custom_user_agent'
    custom_options = ['--custom-option']
    chrome = Chrome(user_agent=custom_user_agent, options=custom_options)

    mock_j_loads_ns.assert_called_once()
    mock_user_agent.assert_not_called()
    
    # verify that custom user agent was not overwritten
    assert mock_j_loads_ns.return_value.user_agent == None

    mock_chrome_options.add_argument.assert_any_call('--test-option')
    mock_chrome_options.add_argument.assert_any_call('--test_header=test_value')
    mock_chrome_options.add_argument.assert_any_call('--custom-option')    
    mock_chrome_options.add_argument.assert_any_call(f'user-data-dir={Path(Path.home() / "AppData" / "Local" / "test_profile")}')
    assert mock_chrome_options.binary_location == str(Path(Path.home() / "AppData" / "Local" / "test_binary"))
    
    # Verify that the service was initialized with the correct path
    mock_chrome_service.assert_called_once()

    mock_webdriver_chrome.assert_called_once()
    

def test_chrome_init_config_load_error(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks behavior when config loading fails."""
    mock_j_loads_ns.return_value = None
    chrome = Chrome()
    assert chrome.config is None
    mock_webdriver_chrome.assert_not_called()

def test_chrome_init_webdriver_exception(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks exception handling during WebDriver initialization."""
    mock_webdriver_chrome.side_effect = WebDriverException("WebDriver failed")
    chrome = Chrome()
    assert not hasattr(chrome, 'get_page_lang') 
    assert not hasattr(chrome, 'execute_locator')
    
def test_chrome_init_general_exception(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks general exception handling during initialization."""
    mock_webdriver_chrome.side_effect = Exception("General error")
    chrome = Chrome()
    assert not hasattr(chrome, 'get_page_lang') 
    assert not hasattr(chrome, 'execute_locator')

def test_chrome_payload_execution(mock_user_agent, mock_j_loads_ns, mock_chrome_options, mock_chrome_service, mock_webdriver_chrome, mock_executors):
    """Checks if payload methods get executed."""
    chrome = Chrome()
    js_executor, locator_executor = mock_executors

    assert hasattr(chrome, 'get_page_lang')
    assert hasattr(chrome, 'ready_state')
    assert hasattr(chrome, 'get_referrer')
    assert hasattr(chrome, 'unhide_DOM_element')
    assert hasattr(chrome, 'window_focus')
    
    assert hasattr(chrome, 'execute_locator')
    assert hasattr(chrome, 'get_webelement_as_screenshot')
    assert hasattr(chrome, 'get_webelement_by_locator')
    assert hasattr(chrome, 'get_attribute_by_locator')
    assert hasattr(chrome, 'send_message')
    assert hasattr(chrome, 'send_key_to_webelement')

    js_executor.get_page_lang.assert_called_once()
    js_executor.ready_state.assert_called_once()
    js_executor.get_referrer.assert_called_once()
    js_executor.unhide_DOM_element.assert_called_once()
    js_executor.window_focus.assert_called_once()
    
    locator_executor.execute_locator.assert_called_once()
    locator_executor.get_webelement_as_screenshot.assert_called_once()
    locator_executor.get_webelement_by_locator.assert_called_once()
    locator_executor.get_attribute_by_locator.assert_called_once()
    locator_executor.send_message.assert_called_once()
```