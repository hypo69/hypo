```python
import pytest
from src.utils.convertors.html import html2escape, escape2html, html2dict, html2ns, html2pdf
from types import SimpleNamespace
import os

class StringFormatter:
    @staticmethod
    def escape_html_tags(input_str: str) -> str:
        """
        Convert HTML to escape sequences.
    
        Args:
            input_str (str): The HTML code.
    
        Returns:
            str: HTML converted into escape sequences.
    
        Example:
            >>> html = "<p>Hello, world!</p>"
            >>> result = StringFormatter.escape_html_tags(html)
            >>> print(result)
            &lt;p&gt;Hello, world!&lt;/p&gt;
        """
        escaped_str = input_str.replace("&", "&amp;") \
            .replace("<", "&lt;") \
            .replace(">", "&gt;") \
            .replace('"', "&quot;") \
            .replace("'", "&#39;")
        return escaped_str

    @staticmethod
    def unescape_html_tags(input_str: str) -> str:
        """
        Convert escape sequences to HTML.
    
        Args:
            input_str (str): The string with escape sequences.
    
        Returns:
            str: The escape sequences converted back into HTML.
    
        Example:
            >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
            >>> result = StringFormatter.unescape_html_tags(escaped)
            >>> print(result)
            <p>Hello, world!</p>
        """
        unescaped_str = input_str.replace("&amp;", "&") \
            .replace("&lt;", "<") \
            .replace("&gt;", ">") \
            .replace("&quot;", '"') \
            .replace("&#39;", "'")
        return unescaped_str
@pytest.fixture
def html_string():
    """Provides a sample HTML string for testing."""
    return "<p>Hello</p><a href='link'>World</a>"

@pytest.fixture
def escaped_html_string():
    """Provides a sample escaped HTML string for testing."""
    return "&lt;p&gt;Hello&lt;/p&gt;&lt;a href=&#39;link&#39;&gt;World&lt;/a&gt;"

# Tests for html2escape
def test_html2escape_valid_input(html_string):
    """Checks correct behavior of html2escape with valid HTML input."""
    expected_output = StringFormatter.escape_html_tags(html_string)
    assert html2escape(html_string) == expected_output

def test_html2escape_empty_input():
    """Checks behavior of html2escape with an empty string input."""
    assert html2escape("") == ""

def test_html2escape_no_tags():
     """Checks behavior of html2escape with no tags present"""
     text = "Simple text without any tags"
     assert html2escape(text) == StringFormatter.escape_html_tags(text)

# Tests for escape2html
def test_escape2html_valid_input(escaped_html_string):
    """Checks correct behavior of escape2html with valid escaped HTML input."""
    expected_output = StringFormatter.unescape_html_tags(escaped_html_string)
    assert escape2html(escaped_html_string) == expected_output

def test_escape2html_empty_input():
    """Checks behavior of escape2html with an empty string input."""
    assert escape2html("") == ""

def test_escape2html_no_escapes():
    """Checks behavior of escape2html with a string that doesn't have escapes"""
    text = "Simple text without any escapes"
    assert escape2html(text) == StringFormatter.unescape_html_tags(text)

# Tests for html2dict
def test_html2dict_valid_input(html_string):
    """Checks correct behavior of html2dict with valid HTML input."""
    expected_output = {'p': 'Hello', 'a': 'World'}
    assert html2dict(html_string) == expected_output

def test_html2dict_empty_input():
    """Checks behavior of html2dict with empty HTML input."""
    assert html2dict("") == {}

def test_html2dict_nested_tags():
    """Checks behavior of html2dict with nested HTML tags."""
    html = "<div><p>Nested</p></div>"
    expected_output = {'div': '', 'p': 'Nested'}
    assert html2dict(html) == expected_output


def test_html2dict_tags_with_attributes():
    """Checks behavior of html2dict with HTML tags with attributes."""
    html = "<p class='test'>Content</p><a href='link'>Link Text</a>"
    expected_output = {'p': 'Content', 'a': 'Link Text'}
    assert html2dict(html) == expected_output

def test_html2dict_multiple_same_tags():
    """Checks behavior of html2dict with multiple same HTML tags."""
    html = "<p>First</p><p>Second</p>"
    expected_output = {'p': 'Second'}
    assert html2dict(html) == {'p': 'Second'}


# Tests for html2ns
def test_html2ns_valid_input(html_string):
    """Checks correct behavior of html2ns with valid HTML input."""
    result = html2ns(html_string)
    assert isinstance(result, SimpleNamespace)
    assert result.p == 'Hello'
    assert result.a == 'World'

def test_html2ns_empty_input():
    """Checks behavior of html2ns with empty HTML input."""
    result = html2ns("")
    assert isinstance(result, SimpleNamespace)
    assert not result.__dict__

def test_html2ns_nested_tags():
    """Checks behavior of html2ns with nested HTML tags."""
    html = "<div><p>Nested</p></div>"
    result = html2ns(html)
    assert hasattr(result, 'p')
    assert hasattr(result, 'div')
    assert result.p == 'Nested'


def test_html2ns_tags_with_attributes():
    """Checks behavior of html2ns with HTML tags with attributes."""
    html = "<p class='test'>Content</p><a href='link'>Link Text</a>"
    result = html2ns(html)
    assert hasattr(result, 'p')
    assert hasattr(result, 'a')
    assert result.p == 'Content'
    assert result.a == 'Link Text'

def test_html2ns_multiple_same_tags():
    """Checks behavior of html2ns with multiple same HTML tags."""
    html = "<p>First</p><p>Second</p>"
    result = html2ns(html)
    assert hasattr(result, 'p')
    assert result.p == 'Second'

# Test for html2pdf
def test_html2pdf_valid_input(html_string, tmp_path):
    """Checks if a PDF is generated successfully with valid input."""
    pdf_file = tmp_path / "test.pdf"
    result = html2pdf(html_string, pdf_file)
    assert result is True
    assert os.path.exists(pdf_file)

def test_html2pdf_empty_input(tmp_path):
    """Checks if a PDF is generated successfully with empty input."""
    pdf_file = tmp_path / "test.pdf"
    result = html2pdf("", pdf_file)
    assert result is True
    assert os.path.exists(pdf_file)

def test_html2pdf_invalid_html(tmp_path):
     """Check how the pdf function handles invalid html input"""
     pdf_file = tmp_path / "test.pdf"
     html = "<html><head></head><body><p>Hello</p><a>This is unclosed"
     result = html2pdf(html, pdf_file)
     assert result is True
     assert os.path.exists(pdf_file)

def test_html2pdf_non_existent_path():
     """Checks how the html2pdf handles non existent paths"""
     pdf_file = "non_existent_dir/test.pdf"
     html = "<p>Hello world</p>"
     result = html2pdf(html, pdf_file)
     assert result is None
```