```python
import pytest
from hypotez.src.gui.openai_trаigner.version import (
    __version__,
    __doc__,
    __details__,
    __author__,
    __copyright__,
    __cofee__,
    MODE,
)


def test_version_string():
    """Checks if __version__ is a string."""
    assert isinstance(__version__, str)


def test_doc_string():
    """Checks if __doc__ is a string."""
    assert isinstance(__doc__, str)


def test_details_string():
    """Checks if __details__ is a string."""
    assert isinstance(__details__, str)


def test_author_string():
    """Checks if __author__ is a string."""
    assert isinstance(__author__, str)


def test_copyright_string():
    """Checks if __copyright__ is a string."""
    assert isinstance(__copyright__, str)


def test_cofee_string():
    """Checks if __cofee__ is a string."""
    assert isinstance(__cofee__, str)


def test_mode_string():
    """Checks if MODE is a string."""
    assert isinstance(MODE, str)

def test_copyright_content():
    """Checks if copyright string contains expected license information."""
    assert "MIT License" in __copyright__
    assert "Copyright (c) 2024 hypo69" in __copyright__


def test_cofee_link():
  """Checks if the coffee link is a valid URL."""
  assert "https://boosty.to/hypo69" in __cofee__

```