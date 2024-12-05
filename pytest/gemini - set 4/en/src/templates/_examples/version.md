```python
import pytest
import hypotez.src.templates._examples.version as version

def test_version_string():
    """Checks if __version__ is a string."""
    assert isinstance(version.__version__, str), "version is not a string"

def test_version_value():
    """Checks the value of the __version__ variable."""
    assert version.__version__ == "3.12.0.0.0.4", "Incorrect version string"

def test_author_string():
    """Checks if __author__ is a string."""
    assert isinstance(version.__author__, str), "author is not a string"
    
def test_author_value():
    """Checks the value of the __author__ variable."""
    assert version.__author__ == 'hypotez ', "Incorrect author string"

def test_details_string():
    """Checks if __details__ is a string."""
    assert isinstance(version.__details__, str), "details is not a string"


def test_details_value():
    """Checks the value of the __details__ variable."""
    assert version.__details__ == "Details about version for module or class", "Incorrect details string"



def test_mode_value():
    """Checks the value of MODE variable."""
    assert version.MODE == 'dev' , "Incorrect mode string"

```