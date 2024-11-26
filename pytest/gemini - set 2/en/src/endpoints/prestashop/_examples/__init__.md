```python
import pytest
from packaging.version import Version
from .version import __version__, __doc__, __details__

# Tests for __version__
def test_version_format():
    """Checks if __version__ is in the correct format (e.g., X.Y.Z)."""
    assert isinstance(__version__, str)
    try:
        Version(__version__)
    except Exception as e:
        pytest.fail(f"Invalid version format: {e}")


def test_version_is_not_empty():
  """Checks if __version__ is not empty string."""
  assert __version__ != ""


# Tests for __doc__ (assuming __doc__ contains documentation)
def test_docstring_is_not_empty():
    """Checks if the docstring is not empty."""
    assert __doc__ != ""


def test_docstring_is_string():
    """Checks if the docstring is a string."""
    assert isinstance(__doc__, str)


#Tests for __details__ (assuming __details__ is a dictionary)
def test_details_is_not_empty():
    """Checks if details are not empty."""
    assert __details__ != {}


def test_details_is_dictionary():
    """Checks if details is a dictionary."""
    assert isinstance(__details__, dict)
```