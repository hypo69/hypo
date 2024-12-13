```python
import pytest
from unittest.mock import MagicMock

import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('../')

from tinytroupe.utils import name_or_empty, extract_json, repeat_on_error
#from testing_utils import * # This is not used, commenting out

def test_extract_json_valid_object():
    """Tests extract_json with a valid JSON object string."""
    text = 'Some text before {"key": "value"} some text after'
    result = extract_json(text)
    assert result == {"key": "value"}

def test_extract_json_valid_array():
    """Tests extract_json with a valid JSON array string."""
    text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
    result = extract_json(text)
    assert result == [{"key": "value"}, {"key2": "value2"}]

def test_extract_json_escaped_characters():
    """Tests extract_json with escaped characters in JSON string."""
    text = 'Some text before {"key": "\\\'value\\\'"} some text after'
    result = extract_json(text)
    assert result == {"key": "\'value\'"}

def test_extract_json_invalid_json():
    """Tests extract_json with invalid JSON string."""
    text = 'Some text before {"key": "value",} some text after'
    result = extract_json(text)
    assert result == {}

def test_extract_json_no_json():
    """Tests extract_json with no JSON string."""
    text = 'Some text with no JSON'
    result = extract_json(text)
    assert result == {}

def test_extract_json_empty_string():
    """Tests extract_json with an empty string."""
    text = ''
    result = extract_json(text)
    assert result == {}

def test_extract_json_nested_json():
    """Tests extract_json with a nested JSON object."""
    text = 'Some text before {"key": {"nested_key": "nested_value"}} some text after'
    result = extract_json(text)
    assert result == {"key": {"nested_key": "nested_value"}}

def test_name_or_empty_named_entity():
    """Tests name_or_empty with an object having a name attribute."""
    class MockEntity:
        def __init__(self, name):
            self.name = name
    entity = MockEntity("Test")
    result = name_or_empty(entity)
    assert result == "Test"

def test_name_or_empty_none_entity():
    """Tests name_or_empty with a None input."""
    result = name_or_empty(None)
    assert result == ""

def test_name_or_empty_empty_name():
    """Tests name_or_empty with a entity that has an empty name"""
    class MockEntity:
        def __init__(self, name):
            self.name = name
    entity = MockEntity("")
    result = name_or_empty(entity)
    assert result == ""

def test_name_or_empty_noname_attribute():
    """Tests name_or_empty with an entity that does not have a name attribute"""
    class MockEntity:
        def __init__(self, value):
            self.value = value

    entity = MockEntity("Test")
    result = name_or_empty(entity)
    assert result == ""

def test_repeat_on_error_exception_retries():
    """Tests repeat_on_error with an exception that retries and ultimately raises."""
    class DummyException(Exception):
        pass

    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == retries

def test_repeat_on_error_no_exception():
    """Tests repeat_on_error with no exception occurring."""
    class DummyException(Exception):
        pass
    retries = 3
    dummy_function = MagicMock()  # no exception raised
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
    assert dummy_function.call_count == 1

def test_repeat_on_error_different_exception():
    """Tests repeat_on_error with an exception not in the exceptions list."""
    class DummyException(Exception):
        pass
    retries = 3
    dummy_function = MagicMock(side_effect=RuntimeError())
    with pytest.raises(RuntimeError):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1

def test_repeat_on_error_zero_retries():
    """Tests repeat_on_error with zero retries and an exception occurring."""
    class DummyException(Exception):
        pass
    retries = 0
    dummy_function = MagicMock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1

def test_repeat_on_error_no_exceptions_list():
    """Tests repeat_on_error with no exception list and an exception occurring."""
    class DummyException(Exception):
        pass
    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries)
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1
```