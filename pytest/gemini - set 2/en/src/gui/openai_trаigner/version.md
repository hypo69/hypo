```python
import pytest
from hypotez.src.gui.openai_trаigner.version import __version__, __doc__, __details__, __author__, __copyright__, __cofee__


def test_version_string():
    """Tests if __version__ is a string."""
    assert isinstance(__version__, str)


def test_doc_string():
    """Tests if __doc__ is a string."""
    assert isinstance(__doc__, str)


def test_details_string():
    """Tests if __details__ is a string."""
    assert isinstance(__details__, str)


def test_author_string():
    """Tests if __author__ is a string."""
    assert isinstance(__author__, str)


def test_copyright_string():
    """Tests if __copyright__ is a string."""
    assert isinstance(__copyright__, str)


def test_cofee_string():
    """Tests if __cofee__ is a string."""
    assert isinstance(__cofee__, str)

def test_version_value():
    """Tests the expected value of __version__"""
    assert __version__ == 'v1.1'


def test_doc_value():
    """Tests if __doc__ is an empty string."""
    assert __doc__ == ''


def test_details_value():
    """Tests if __details__ is an empty string."""
    assert __details__ == ''


def test_author_value():
    """Tests if __author__ contains expected value"""
    assert __author__ == 'hypo69'


def test_copyright_value():
    """Tests if __copyright__ contains a license message"""
    assert "Copyright (c) 2024 hypo69" in __copyright__
    assert "MIT License" in __copyright__
    
    
def test_cofee_value():
    """Tests if __cofee__ contains a link to support the developer."""
    assert "https://boosty.to/hypo69" in __cofee__



```