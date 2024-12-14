```python
import pytest
from packaging.version import Version
from hypotez.src.webdriver.edge._examples import __version__, __doc__, __details__, MODE

# Fixture definitions, if needed
@pytest.fixture
def example_version():
    """Provides a sample version string for testing."""
    return "1.2.3"

@pytest.fixture
def example_details():
    """Provides sample details string for testing."""
    return "Sample details for testing."

@pytest.fixture
def example_doc():
    """Provides a sample doc string."""
    return "Sample doc for testing."

# Tests for __version__
def test_version_is_string():
    """Checks if __version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert __version__ != ""

def test_version_is_valid_semver(example_version):
    """Checks if __version__ is a valid semantic version string."""
    
    try:
       Version(__version__)
    except ValueError:
         pytest.fail("Version string is not a valid semantic version")

def test_doc_is_string(example_doc):
    """Checks if __doc__ is a string"""
    assert isinstance(__doc__, str)

def test_doc_is_not_empty(example_doc):
    """Checks if __doc__ is not empty"""
    assert len(__doc__) > 0

def test_details_is_string(example_details):
     """Checks if __details__ is a string"""
     assert isinstance(__details__, str)

def test_details_is_not_empty(example_details):
     """Checks if __details__ is not empty"""
     assert len(__details__) > 0

def test_mode_is_dev():
    """Checks if MODE is set to 'dev'"""
    assert MODE == 'dev'
```