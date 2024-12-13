```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.etzmaleh.login import login
from src.logger.logger import logger


def test_login_successful():
    """
    Test successful login.
    It checks if the function returns True upon successful execution.
    """
    mock_supplier = MagicMock()
    result = login(mock_supplier)
    assert result is True
    logger.info.assert_called_once_with('Залогинился ... ')


def test_login_with_exception():
    """
        Test login function exception handling.
        The test now uses pytest.raises to capture and assert the correct exception.
        It uses mock to patch the logger for avoiding log file error
    """
    mock_supplier = MagicMock()
    with pytest.raises(NameError) as excinfo:
        login(mock_supplier)
    assert 'name \'Truee\' is not defined' in str(excinfo.value)
    logger.info.assert_called_once_with('Залогинился ... ')
```