```python
import pytest
import markdown


def test_markdown_to_html_valid_input():
    """Checks converting valid markdown to HTML."""
    markdown_text = "# This is a header\n\nThis is a paragraph."
    expected_html = "<h1>This is a header</h1>\n<p>This is a paragraph.</p>"
    html_output = markdown.markdown(markdown_text)
    assert html_output == expected_html


def test_markdown_to_html_empty_input():
    """Checks handling of empty markdown input."""
    markdown_text = ""
    expected_html = ""
    html_output = markdown.markdown(markdown_text)
    assert html_output == expected_html


def test_markdown_to_html_invalid_markdown():
    """Checks handling of invalid markdown syntax."""
    markdown_text = "This is invalid markdown {incorrect syntax}"
    with pytest.raises(Exception) as excinfo:
        markdown.markdown(markdown_text)
    # Assert an exception is raised, no need for specific exception type in this case
    assert str(excinfo.value).startswith("invalid syntax")


def test_markdown_to_html_list_elements():
    """Checks proper rendering of list elements in markdown."""
    markdown_text = "* Item 1\n* Item 2\n* Item 3"
    expected_html = "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n<li>Item 3</li>\n</ul>"
    html_output = markdown.markdown(markdown_text)
    assert html_output == expected_html


def test_markdown_to_html_code_block():
    """Checks correct rendering of code blocks."""
    markdown_text = "```python\nprint('Hello, world!')\n```"
    expected_html = "<pre><code class=\"language-python\">print('Hello, world!')\n</code></pre>"
    html_output = markdown.markdown(markdown_text)
    assert html_output == expected_html



def test_markdown_to_html_fenced_code_block():
    """Checks that a fenced code block is rendered correctly."""
    markdown_text = "```python\nprint('Hello')\n```"
    expected_html = "<pre><code class=\"language-python\">print('Hello')\n</code></pre>"
    html_output = markdown.markdown(markdown_text)
    assert html_output == expected_html


def test_markdown_to_html_invalid_fenced_code_block():
    """Checks handling of invalid fenced code blocks."""
    markdown_text = "```invalid\nnot a valid language\n```"
    expected_html = "<pre><code>invalid\nnot a valid language\n</code></pre>"
    html_output = markdown.markdown(markdown_text)
    assert html_output == expected_html  
```