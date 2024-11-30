```python
import pytest
from packaging.version import Version
from hypotez.src.product._examples import __version__, __doc__, __details__


def test_version_is_a_version_object():
    """Checks if __version__ is a valid Version object."""
    assert isinstance(__version__, Version)


def test_version_string_format():
    """Checks if the version string is in a valid format."""
    assert isinstance(__version__, Version)
    assert str(__version__).count('.') == 2


def test_version_string_value():
    """Checks the version string has expected values."""
    assert isinstance(__version__, Version)


def test_docstring_is_a_string():
    """Checks if __doc__ is a string."""
    assert isinstance(__doc__, str)


def test_details_is_a_dictionary():
    """Checks if __details__ is a dictionary."""
    assert isinstance(__details__, dict)



@pytest.mark.parametrize("key", ["name", "description", "author"])
def test_details_has_expected_keys(key):
    """Checks if __details__ has expected keys."""
    assert key in __details, f"Missing key '{key}' in __details__"

```