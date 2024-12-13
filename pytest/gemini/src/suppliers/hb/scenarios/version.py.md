```python
import pytest

# Fixture definitions, if needed
@pytest.fixture
def module_version_data():
    """Provides version data for the module."""
    return {
        "__name__": "__main__",
        "__version__": "3.12.0.0.0.4",
        "__doc__": "Module documentation string",
        "__details__": "Details about version for module or class",
        "__author__" : "hypotez"
    }
# Tests for module variables
def test_version_name_is_str(module_version_data):
    """Checks if __name__ is a string."""
    assert isinstance(module_version_data["__name__"], str)

def test_version_is_str(module_version_data):
    """Checks if __version__ is a string."""
    assert isinstance(module_version_data["__version__"], str)

def test_version_doc_is_str(module_version_data):
    """Checks if __doc__ is a string."""
    assert isinstance(module_version_data["__doc__"], str)

def test_version_details_is_str(module_version_data):
    """Checks if __details__ is a string."""
    assert isinstance(module_version_data["__details__"], str)

def test_version_author_is_str(module_version_data):
    """Checks if __author__ is a string."""
    assert isinstance(module_version_data["__author__"], str)

def test_version_name_not_empty(module_version_data):
    """Checks if __name__ is not an empty string."""
    assert module_version_data["__name__"] != ""

def test_version_not_empty(module_version_data):
    """Checks if __version__ is not an empty string."""
    assert module_version_data["__version__"] != ""

def test_version_doc_not_empty(module_version_data):
    """Checks if __doc__ is not an empty string."""
    assert module_version_data["__doc__"] != ""

def test_version_details_not_empty(module_version_data):
    """Checks if __details__ is not an empty string."""
    assert module_version_data["__details__"] != ""
    
def test_version_author_not_empty(module_version_data):
    """Checks if __author__ is not an empty string."""
    assert module_version_data["__author__"] != ""

def test_version_format(module_version_data):
    """Checks if __version__ follows the expected format (x.x.x.x.x.x)."""
    version = module_version_data["__version__"]
    parts = version.split('.')
    assert len(parts) == 6, "Version should have 6 parts separated by dots"
    for part in parts:
        assert part.isdigit(), "All version parts should be digits"
```