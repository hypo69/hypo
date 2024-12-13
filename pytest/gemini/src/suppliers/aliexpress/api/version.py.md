```python
import pytest
from hypotez.src.suppliers.aliexpress.api import version

def test_version_name_is_string():
    """Checks if __name__ is a string."""
    assert isinstance(version.__name__, str)

def test_version_version_is_string():
    """Checks if __version__ is a string."""
    assert isinstance(version.__version__, str)

def test_version_doc_is_string_or_none():
    """Checks if __doc__ is a string or None.
    It can be None if not docstring is provided
    """
    assert isinstance(version.__doc__, (str, type(None)))

def test_version_details_is_string():
    """Checks if __details__ is a string."""
    assert isinstance(version.__details__, str)

def test_version_annotations_is_dict():
    """Checks if __annotations__ is a dict."""
    assert isinstance(version.__annotations__, dict)

def test_version_author_is_string():
    """Checks if __author__ is a string."""
    assert isinstance(version.__author__, str)


def test_version_version_format():
  """Checks if __version__ follows a specific format."""
  #split to check format
  parts = version.__version__.split('.')
  assert len(parts) == 6
  for part in parts:
      assert part.isdigit()
```