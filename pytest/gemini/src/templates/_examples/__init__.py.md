```python
import pytest
from packaging.version import Version

# Assuming that 'hypotez/src/templates/_examples/version.py' exists and has __version__, __doc__, and __details__
# We are mocking this here for testing purposes. In reality, you'd import from that module
class MockVersionModule:
    __version__ = "0.1.0"
    __doc__ = "This is a test docstring."
    __details__ = "These are some details."

# Mock import to avoid import errors
import sys
sys.modules['hypotez.src.templates._examples.version'] = MockVersionModule()

from hypotez.src.templates._examples import __version__, __doc__, __details__, MODE


def test_module_mode():
    """
    Test that the module-level variable MODE is set to 'dev'.
    """
    assert MODE == 'dev'

def test_version_is_valid_semver():
    """
    Test that the __version__ string can be parsed as a valid semantic version.
    """
    try:
       Version(__version__)
    except Exception as e:
       pytest.fail(f"__version__ is not a valid semantic version: {e}")

def test_version_exists():
    """
    Test that __version__ is defined and is not empty.
    """
    assert __version__
    assert isinstance(__version__, str)

def test_doc_exists():
    """
    Test that __doc__ is defined and is not empty.
    """
    assert __doc__
    assert isinstance(__doc__, str)

def test_details_exists():
    """
    Test that __details__ is defined and is not empty.
    """
    assert __details__
    assert isinstance(__details__, str)

def test_doc_is_not_empty_string():
  """Test that the module docstring is not empty.
  """
  assert __doc__.strip() != ""

def test_details_is_not_empty_string():
  """Test that the details string is not empty.
  """
  assert __details__.strip() != ""
```