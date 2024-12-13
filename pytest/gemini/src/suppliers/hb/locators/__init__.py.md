```python
import pytest
from packaging.version import Version
from hypotez.src.suppliers.hb.locators.version import __version__, __doc__, __details__
from hypotez.src.suppliers.hb.locators import MODE  # Import MODE from the init file


# Test for the MODE variable
def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    assert MODE == 'dev', "The MODE variable should be set to 'dev'."

# Test for the __version__ variable
def test_version_is_valid():
    """Checks if the __version__ variable is a valid version string."""
    try:
        Version(__version__)
    except Exception:
         pytest.fail("The __version__ variable is not a valid version string.")

# Test for the __doc__ variable
def test_doc_not_empty():
    """Checks if the __doc__ variable is not empty."""
    assert __doc__, "The __doc__ variable should not be empty."
    assert isinstance(__doc__, str), "The __doc__ variable should be a string."


# Test for the __details__ variable
def test_details_not_empty():
    """Checks if the __details__ variable is not empty."""
    assert __details__, "The __details__ variable should not be empty."
    assert isinstance(__details__, str), "The __details__ variable should be a string."
```