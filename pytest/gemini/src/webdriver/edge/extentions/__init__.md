```python
import pytest
from packaging.version import Version
from hypotez.src.webdriver.edge.extentions import __version__, __doc__, __details__


def test_version_is_a_version_object():
    """Checks if __version__ is a Version object."""
    assert isinstance(__version__, Version)


def test_version_string_format():
    """Checks if __version__ is in the expected format."""
    assert isinstance(__version__, Version)
    assert str(__version__) == __version__


def test_docstring_is_a_string():
    """Checks if __doc__ is a string."""
    assert isinstance(__doc__, str)


def test_details_is_a_dictionary():
    """Checks if __details__ is a dictionary."""
    assert isinstance(__details__, dict)


def test_details_has_keys():
  """Checks if __details__ has at least one key."""
  assert len(__details) > 0

@pytest.mark.parametrize("key", ["name", "version", "author"])  
def test_details_keys_are_strings(key):
  """Checks if all keys in __details__ are strings."""
  if key in __details:
    assert isinstance(__details[key], str)
  else:
    pytest.skip(f"Key '{key}' not found in __details__")
  


#Example of testing for an invalid version string. This would need to be 
#customized depending on how the module handles bad inputs and if it 
#raises exceptions


def test_version_invalid_format_raises_exception():
    """Checks if invalid version format raises an exception"""
    invalid_version_string = "bad-version"

    with pytest.raises(Exception):
        Version(invalid_version_string)
```