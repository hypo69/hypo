```python
import pytest
from unittest.mock import Mock, patch, mock_open
from pathlib import Path
from src.webdriver.driver import DriverBase
from selenium.common.exceptions import InvalidArgumentException
import unittest
from src.config.global_settings import gs


class TestDriverBase:
    @pytest.fixture
    def driver_base(self):
        """Fixture to create an instance of DriverBase for testing."""
        return DriverBase()

    def test_driver_payload(self, driver_base):
        """Test driver_payload method to verify correct assignment of javascript and execute locator methods."""
        with patch('src.webdriver.javascript.js.JavaScript') as mock_js, \
             patch('src.webdriver.executor.ExecuteLocator') as mock_execute_locator:
            mock_js_instance = mock_js.return_value
            mock_execute_locator_instance = mock_execute_locator.return_value

            driver_base.driver_payload()

            # Verify that methods from JavaScript are correctly assigned
            assert driver_base.get_page_lang == mock_js_instance.get_page_lang
            assert driver_base.ready_state == mock_js_instance.ready_state
            assert driver_base.get_referrer == mock_js_instance.get_referrer
            assert driver_base.unhide_DOM_element == mock_js_instance.unhide_DOM_element
            assert driver_base.window_focus == mock_js_instance.window_focus

            # Verify that methods from ExecuteLocator are correctly assigned
            assert driver_base.execute_locator == mock_execute_locator_instance.execute_locator
            assert driver_base.click == mock_execute_locator_instance.click
            assert driver_base.get_webelement_as_screenshot == mock_execute_locator_instance.get_webelement_as_screenshot
            assert driver_base.get_attribute_by_locator == mock_execute_locator_instance.get_attribute_by_locator
            assert driver_base.send_message == mock_execute_locator_instance.send_message

    def test_scroll(self, driver_base):
        """Test scroll method with different directions."""
        driver_base.execute_script = Mock()
        driver_base.wait = Mock()

        # Test scrolling forward
        assert driver_base.scroll(3, 1000, 'forward', 0.1) is True
        driver_base.execute_script.assert_called_with('window.scrollBy(0,1000)')
        
        driver_base.execute_script.reset_mock()
        # Test scrolling backward
        assert driver_base.scroll(3, 1000, 'backward', 0.1) is True
        driver_base.execute_script.assert_called_with('window.scrollBy(0,-1000)')

        driver_base.execute_script.reset_mock()
        # Test scrolling both directions
        assert driver_base.scroll(3, 1000, 'both', 0.1) is True
        driver_base.execute_script.assert_any_call('window.scrollBy(0,1000)')
        driver_base.execute_script.assert_any_call('window.scrollBy(0,-1000)')

    def test_locale(self, driver_base):
        """Test locale property, checking both cases with and without meta tag."""
        driver_base.find_element = Mock()

        # Case when meta tag is found
        meta_mock = Mock()
        meta_mock.get_attribute.return_value = 'en'
        driver_base.find_element.return_value = meta_mock
        assert driver_base.locale == 'en'

        # Case when meta tag is not found
        driver_base.find_element.side_effect = Exception
        driver_base.get_page_lang = Mock(return_value='fr')
        assert driver_base.locale == 'fr'

    def test_get_url(self, driver_base):
        """Test get_url method, ensuring correct URL loading, cookies saving and previous URL tracking."""
        driver_base.get = Mock()
        driver_base.ready_state = Mock(return_value='complete')
        driver_base.wait = Mock()
        driver_base._save_cookies_localy = Mock()

        driver_base.current_url = 'http://previous.com'
        assert driver_base.get_url('http://new.com') is True
        assert driver_base.previous_url == 'http://previous.com'
        driver_base.get.assert_called_with('http://new.com')
        driver_base._save_cookies_localy.assert_called_once()

    def test_extract_domain(self, driver_base):
        """Test extract_domain method with various URL formats."""
        assert driver_base.extract_domain('http://www.example.com/page') == 'example.com'
        assert driver_base.extract_domain('https://example.com/page') == 'example.com'
        assert driver_base.extract_domain('example.com/page') == 'example.com'

    def test_save_cookies_localy(self, driver_base):
       """Test _save_cookies_localy method with patching file operations."""
       driver_base.get_cookies = Mock(return_value={'key': 'value'})
       with patch('builtins.open', mock_open()) as mock_open_file, \
            patch('pickle.dump') as mock_pickle_dump:
           to_file = Path('/path/to/cookies')
           driver_base.extract_domain = Mock(return_value='example.com')
           gs.dir_cookies = '/cookies'
           assert driver_base._save_cookies_localy(to_file) is True
           mock_open_file.assert_called_once_with(to_file, 'wb')
           mock_pickle_dump.assert_called_once_with({'key': 'value'}, mock_open_file())

    def test_page_refresh(self, driver_base):
        """Test page_refresh method, ensuring the correct URL is reloaded."""
        driver_base.current_url = 'http://example.com'
        driver_base.get_url = Mock(return_value=True)
        assert driver_base.page_refresh() is True
        driver_base.get_url.assert_called_with('http://example.com')

    def test_wait(self, driver_base):
        """Test wait method, verifying correct sleep time."""
        with patch('time.sleep') as mock_sleep:
            driver_base.wait(1)
            mock_sleep.assert_called_with(1)

    def test_delete_driver_logs(self, driver_base):
        """Test delete_driver_logs method, ensuring logs are deleted correctly."""
        temp_dir = Path('/tmp/webdriver')
        gs.dir_logs = '/tmp'
        with patch('pathlib.Path.iterdir') as mock_iterdir, \
             patch('pathlib.Path.is_file', return_value=True), \
             patch('pathlib.Path.unlink') as mock_unlink, \
             patch('pathlib.Path.is_dir', return_value=False):
            mock_iterdir.return_value = [Path('/tmp/webdriver/file1'), Path('/tmp/webdriver/file2')]
            assert driver_base.delete_driver_logs() is True
            mock_unlink.assert_any_call()
```