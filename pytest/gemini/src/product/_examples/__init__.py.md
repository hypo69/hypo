```python
import pytest
from packaging.version import Version
from hypotez.src.product._examples.version import __version__, __doc__, __details__
from hypotez.src.product._examples import MODE


def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    assert MODE == 'dev'

def test_version_is_valid():
    """Checks if __version__ is a valid semantic version."""
    try:
        Version(__version__)
    except Exception as e:
        pytest.fail(f"__version__ is not a valid semantic version: {e}")

def test_version_is_not_empty():
    """Checks if __version__ is not empty."""
    assert __version__ != ""

def test_doc_is_string():
    """Checks if __doc__ is a string."""
    assert isinstance(__doc__, str)

def test_doc_is_not_empty():
    """Checks if __doc__ is not empty."""
    assert __doc__ != ""

def test_details_is_string():
    """Checks if __details__ is a string."""
    assert isinstance(__details__, str)

def test_details_is_not_empty():
     """Checks if __details__ is not empty."""
     assert __details__ != ""
```