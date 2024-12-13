```python
import pytest
from pathlib import Path
from unittest.mock import patch
from src.utils.convertors.xls import xls2dict

# Mock the read_xls_as_dict function to control its behavior during tests
@pytest.fixture
def mock_read_xls_as_dict():
    with patch("src.utils.convertors.xls.read_xls_as_dict") as mock:
        yield mock

def test_xls2dict_valid_file_path(mock_read_xls_as_dict):
    """
    Test xls2dict with a valid file path (string)
    Checks if the function correctly calls read_xls_as_dict and returns its result
    """
    test_path = "test.xls"
    expected_data = {"sheet1": [{"header1": "value1"}, {"header1": "value2"}]}
    mock_read_xls_as_dict.return_value = expected_data
    
    result = xls2dict(test_path)
    
    mock_read_xls_as_dict.assert_called_once_with(xls_file=test_path)
    assert result == expected_data

def test_xls2dict_valid_pathlib_path(mock_read_xls_as_dict):
    """
    Test xls2dict with a valid pathlib.Path object
    Checks if the function correctly calls read_xls_as_dict with the Path object
    """
    test_path = Path("test.xls")
    expected_data = {"sheet1": [{"header1": "value1"}, {"header1": "value2"}]}
    mock_read_xls_as_dict.return_value = expected_data
    
    result = xls2dict(test_path)

    mock_read_xls_as_dict.assert_called_once_with(xls_file=test_path)
    assert result == expected_data

def test_xls2dict_read_xls_as_dict_returns_none(mock_read_xls_as_dict):
    """
    Test xls2dict when read_xls_as_dict returns None
    Ensures that xls2dict returns None as well
    """
    test_path = "test.xls"
    mock_read_xls_as_dict.return_value = None
    
    result = xls2dict(test_path)
    
    mock_read_xls_as_dict.assert_called_once_with(xls_file=test_path)
    assert result is None
```