```python
import pytest
import hypotez.src.suppliers.aliexpress.gui.version as version

def test_version_string():
    """Tests if the __version__ attribute is a string."""
    assert isinstance(version.__version__, str), "Version should be a string."

def test_version_format():
    """Tests the format of the __version__ string."""
    version_parts = version.__version__.split(".")
    assert len(version_parts) == 6, "Version string should have 6 parts separated by dots."
    for part in version_parts:
        try:
            int(part)  # Check if each part can be converted to an integer.
        except ValueError:
            pytest.fail(f"Invalid version part: {part}. Version parts should be integers.")


def test_docstring_type():
    """Tests if the __doc__ attribute is a string."""
    assert isinstance(version.__doc__, str), "__doc__ should be a string."

def test_details_type():
    """Tests if the __details__ attribute is a string."""
    assert isinstance(version.__details__, str), "__details__ should be a string."


def test_author_type():
    """Tests if the __author__ attribute is a string."""
    assert isinstance(version.__author__, str), "__author__ should be a string."

# Test for the __name__ attribute. This assumes the file is being executed
# directly; for a module imported elsewhere, the test would be different.

def test_name_is_main_if_executed_directly():
    """Check that __name__ is "__main__" when run directly."""
    assert version.__name__ == "__main__", \
        "__name__ should be __main__ when run directly"


```