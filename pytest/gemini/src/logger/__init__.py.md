```python
import pytest
from hypotez.src.logger import logger  # Assuming logger is in logger.py
from hypotez.src.logger.exceptions import (
    ExecuteLocatorException,
    DefaultSettingsException,
    CredentialsError,
    PrestaShopException,
    PayloadChecksumError,
)


def test_logger_exists():
    """Checks that the logger object is accessible."""
    assert logger is not None, "Logger object should exist"

def test_execute_locator_exception():
    """Checks if ExecuteLocatorException can be raised and is of the correct type."""
    with pytest.raises(ExecuteLocatorException):
        raise ExecuteLocatorException("Test ExecuteLocatorException")


def test_default_settings_exception():
    """Checks if DefaultSettingsException can be raised and is of the correct type."""
    with pytest.raises(DefaultSettingsException):
        raise DefaultSettingsException("Test DefaultSettingsException")


def test_credentials_error():
    """Checks if CredentialsError can be raised and is of the correct type."""
    with pytest.raises(CredentialsError):
        raise CredentialsError("Test CredentialsError")

def test_prestashop_exception():
     """Checks if PrestaShopException can be raised and is of the correct type."""
     with pytest.raises(PrestaShopException):
         raise PrestaShopException("Test PrestaShopException")


def test_payload_checksum_error():
    """Checks if PayloadChecksumError can be raised and is of the correct type."""
    with pytest.raises(PayloadChecksumError):
        raise PayloadChecksumError("Test PayloadChecksumError")

def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    from hypotez.src.logger import MODE
    assert MODE == 'dev', "MODE should be set to 'dev'"
```