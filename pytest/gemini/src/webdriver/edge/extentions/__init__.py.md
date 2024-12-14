```python
import pytest
from hypotez.src.webdriver.edge.extentions import __version__, __doc__, __details__
from packaging.version import Version


def test_version_is_valid():
    """
    Tests if the __version__ variable is a valid version string that can be parsed by packaging.version.Version
    """
    try:
        Version(__version__)
    except Exception as e:
        pytest.fail(f"__version__ is not a valid version string: {e}")

def test_version_is_not_empty():
    """
    Tests if the __version__ string is not empty.
    """
    assert __version__ != "", "__version__ should not be empty"

def test_doc_is_not_empty():
    """
    Tests if the __doc__ string is not empty.
    """
    assert __doc__ != "", "__doc__ should not be empty"

def test_details_is_not_empty():
    """
    Tests if the __details__ string is not empty.
    """
    assert __details__ != "", "__details__ should not be empty"

def test_details_is_a_string():
    """
    Tests if the __details__ is a string.
    """
    assert isinstance(__details__, str), "__details__ should be a string"
```