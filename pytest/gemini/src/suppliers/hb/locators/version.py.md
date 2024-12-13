```python
import pytest

from hypotez.src.suppliers.hb.locators import version

def test_version_name_is_string():
    """Checks if __name__ is a string."""
    assert isinstance(version.__name__, str)

def test_version_is_string():
    """Checks if __version__ is a string."""
    assert isinstance(version.__version__, str)


def test_version_doc_is_string():
    """Checks if __doc__ is a string or None."""
    assert isinstance(version.__doc__, str) or version.__doc__ is None
    
def test_version_details_is_string():
    """Checks if __details__ is a string."""
    assert isinstance(version.__details__, str)

def test_version_annotations_is_dict_or_none():
    """Checks if __annotations__ is a dict or None."""
    assert isinstance(version.__annotations__, dict) or version.__annotations__ is None


def test_version_author_is_string():
     """Checks if __author__ is a string."""
     assert isinstance(version.__author__, str)

def test_version_author_not_empty():
    """Checks if __author__ is not empty."""
    assert version.__author__ != ""

def test_version_string_format():
    """Checks if the version string follows the expected format."""
    version_str = version.__version__
    parts = version_str.split(".")
    assert len(parts) == 5
    for part in parts:
       assert part.isdigit(), f"Version part '{part}' is not a number"

def test_module_name_not_empty():
    """Checks if __name__ is not empty."""
    assert version.__name__ != ""
```