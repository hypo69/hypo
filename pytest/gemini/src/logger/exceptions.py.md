```python
import pytest
from src.logger.exceptions import (
    CustomException,
    FileNotFoundError,
    ProductFieldException,
    KeePassException,
    DefaultSettingsException,
    WebDriverException,
    ExecuteLocatorException,
    PrestaShopException,
    PrestaShopAuthenticationError,
    MODE
)
from unittest.mock import patch
from pykeepass.exceptions import (CredentialsError, BinaryError,
                                   HeaderChecksumError, PayloadChecksumError, 
                                   UnableToSendToRecycleBin)
from selenium.common.exceptions import WebDriverException as WDriverException

# Fixture definitions, if needed
@pytest.fixture
def mock_logger():
    """Mocks the logger object."""
    with patch('src.logger.exceptions.logger') as mock_logger:
        yield mock_logger

# Tests for CustomException
def test_custom_exception_message(mock_logger):
    """Checks if CustomException stores and displays the correct message."""
    message = "Test custom exception message"
    exc = CustomException(message)
    assert str(exc) == message
    mock_logger.error.assert_called_with(f"Exception occurred: {exc}")

def test_custom_exception_with_original_exception(mock_logger):
    """Checks if CustomException stores and displays the original exception."""
    message = "Test custom exception with original"
    original_exception = ValueError("Original error")
    exc = CustomException(message, e=original_exception)
    assert str(exc) == message
    mock_logger.error.assert_called_with(f"Exception occurred: {exc}")
    mock_logger.debug.assert_called_with(f"Original exception: {original_exception}")


def test_custom_exception_no_exception_info(mock_logger):
    """Checks if CustomException correctly handles exc_info when set to False."""
    message = "Test custom exception with no exception info"
    exc = CustomException(message, exc_info=False)
    assert str(exc) == message
    mock_logger.error.assert_called_with(f"Exception occurred: {exc}")
    mock_logger.debug.assert_not_called()

def test_custom_exception_no_original_exception(mock_logger):
    """Checks if CustomException correctly handles no original exception passed."""
    message = "Test custom exception with no original"
    exc = CustomException(message)
    assert str(exc) == message
    mock_logger.error.assert_called_with(f"Exception occurred: {exc}")
    mock_logger.debug.assert_not_called()


# Tests for FileNotFoundError
def test_file_not_found_error():
    """Checks if FileNotFoundError is a subclass of CustomException and IOError."""
    assert issubclass(FileNotFoundError, CustomException)
    assert issubclass(FileNotFoundError, IOError)
    with pytest.raises(FileNotFoundError, match=""):
        raise FileNotFoundError("File not found")


# Tests for ProductFieldException
def test_product_field_exception():
    """Checks if ProductFieldException is a subclass of CustomException."""
    assert issubclass(ProductFieldException, CustomException)
    with pytest.raises(ProductFieldException, match=""):
        raise ProductFieldException("Product field error")

# Tests for KeePassException
def test_keepass_exception():
    """Checks if KeePassException inherits from correct Keepass exceptions."""
    assert issubclass(KeePassException, CredentialsError)
    assert issubclass(KeePassException, BinaryError)
    assert issubclass(KeePassException, HeaderChecksumError)
    assert issubclass(KeePassException, PayloadChecksumError)
    assert issubclass(KeePassException, UnableToSendToRecycleBin)

# Tests for DefaultSettingsException
def test_default_settings_exception():
    """Checks if DefaultSettingsException is a subclass of CustomException."""
    assert issubclass(DefaultSettingsException, CustomException)
    with pytest.raises(DefaultSettingsException, match=""):
        raise DefaultSettingsException("Default settings error")

# Tests for WebDriverException
def test_web_driver_exception():
    """Checks if WebDriverException is a subclass of selenium WebDriverException"""
    assert issubclass(WebDriverException, WDriverException)
    with pytest.raises(WebDriverException, match=""):
        raise WebDriverException("Webdriver error")


# Tests for ExecuteLocatorException
def test_execute_locator_exception():
    """Checks if ExecuteLocatorException is a subclass of CustomException."""
    assert issubclass(ExecuteLocatorException, CustomException)
    with pytest.raises(ExecuteLocatorException, match=""):
        raise ExecuteLocatorException("Locator execution error")


# Tests for PrestaShopException
def test_prestashop_exception_message():
    """Checks if PrestaShopException stores and displays the correct message."""
    message = "Test PrestaShop exception"
    exc = PrestaShopException(message)
    assert str(exc) == repr(message)
    assert exc.msg == message
    assert exc.ps_error_msg == ''
    assert exc.error_code is None
    assert exc.ps_error_code is None

def test_prestashop_exception_with_ps_error_message():
    """Checks if PrestaShopException stores and displays the correct error message from Prestashop."""
    message = "Test PrestaShop exception"
    ps_error_msg = "Prestashop error message"
    exc = PrestaShopException(message, ps_error_msg=ps_error_msg)
    assert str(exc) == repr(ps_error_msg)
    assert exc.msg == message
    assert exc.ps_error_msg == ps_error_msg
    assert exc.error_code is None
    assert exc.ps_error_code is None

def test_prestashop_exception_with_error_code():
    """Checks if PrestaShopException stores and displays the correct error codes."""
    message = "Test PrestaShop exception"
    error_code = 101
    ps_error_code = 202
    exc = PrestaShopException(message, error_code=error_code, ps_error_code=ps_error_code)
    assert str(exc) == repr(message)
    assert exc.msg == message
    assert exc.ps_error_msg == ''
    assert exc.error_code == error_code
    assert exc.ps_error_code == ps_error_code

def test_prestashop_exception_all_params():
    """Checks if PrestaShopException stores and displays the correct data when all params passed."""
    message = "Test PrestaShop exception"
    error_code = 101
    ps_error_code = 202
    ps_error_msg = "Prestashop error message"
    exc = PrestaShopException(message, error_code=error_code, ps_error_msg=ps_error_msg, ps_error_code=ps_error_code)
    assert str(exc) == repr(ps_error_msg)
    assert exc.msg == message
    assert exc.ps_error_msg == ps_error_msg
    assert exc.error_code == error_code
    assert exc.ps_error_code == ps_error_code


# Tests for PrestaShopAuthenticationError
def test_prestashop_authentication_error():
    """Checks if PrestaShopAuthenticationError is a subclass of PrestaShopException."""
    assert issubclass(PrestaShopAuthenticationError, PrestaShopException)
    with pytest.raises(PrestaShopAuthenticationError, match=""):
        raise PrestaShopAuthenticationError("PrestaShop authentication error")
```