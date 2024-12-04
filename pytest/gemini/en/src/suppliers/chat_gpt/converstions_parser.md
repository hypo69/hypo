```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup
from hypotez.src.suppliers.chat_gpt.converstions_parser import extract_conversations_from_html

# Fixture to create sample HTML files
@pytest.fixture
def sample_html_file(tmp_path):
    """Creates a sample HTML file for testing."""
    html_content = """
    <html>
        <body>
            <div class="conversation">
                <p>Hello</p>
            </div>
            <div class="conversation">
                <p>World</p>
            </div>
            <div class="not-conversation">
                <p>Wrong div</p>
            </div>
        </body>
    </html>
    """
    file_path = tmp_path / "chat.html"
    file_path.write_text(html_content, encoding='utf-8')
    return file_path

# Fixture for a file with no conversations
@pytest.fixture
def empty_html_file(tmp_path):
    """Creates an HTML file with no conversation divs."""
    html_content = """
    <html>
        <body>
            <div class="not-conversation">
                <p>Wrong div</p>
            </div>
        </body>
    </html>
    """
    file_path = tmp_path / "chat_no_conv.html"
    file_path.write_text(html_content, encoding='utf-8')
    return file_path

# Test with valid input
def test_extract_conversations_from_html_valid(sample_html_file):
    """Tests with a valid HTML file containing conversation divs."""
    conversations = list(extract_conversations_from_html(sample_html_file))
    assert len(conversations) == 2
    assert conversations[0].find('p').text == "Hello"
    assert conversations[1].find('p').text == "World"


# Test with no conversation divs
def test_extract_conversations_from_html_empty(empty_html_file):
    """Tests with an HTML file containing no conversation divs."""
    conversations = list(extract_conversations_from_html(empty_html_file))
    assert len(conversations) == 0

# Test with a file that doesn't exist
def test_extract_conversations_from_html_file_not_found(tmp_path):
    """Tests with a non-existent file path."""
    nonexistent_file = tmp_path / "nonexistent.html"
    with pytest.raises(FileNotFoundError):
        list(extract_conversations_from_html(nonexistent_file))


# Test with malformed HTML (not covered in original, but good practice).
def test_extract_conversations_from_html_malformed(tmp_path):
    """Tests with malformed HTML."""
    malformed_html = """<html><body><div class="conversation"><p>Malformed</div></body></html>"""
    file_path = tmp_path / "malformed.html"
    file_path.write_text(malformed_html, encoding='utf-8')
    conversations = list(extract_conversations_from_html(file_path))
    assert len(conversations) == 0 # Or adjust as needed, depending on expected behavior

```

**Explanation and Improvements:**

* **Fixtures:** Introduced `sample_html_file` and `empty_html_file` fixtures to create sample HTML files in temporary directories, making tests more self-contained and avoiding relying on external files. This is crucial for testability.
* **Comprehensive Test Cases:** Added tests for:
    * Valid input with multiple conversation divs.
    * Empty HTML file (no conversation divs).
    * File not found (exception handling).
    * Malformed HTML (Important edge case).
* **Clearer Assertions:** Assertions are more specific, checking for the actual content within the `div` tags.
* **`pytest.raises` for Exception Handling:**  Correctly uses `pytest.raises` to test the `FileNotFoundError` when the file doesn't exist.
* **Descriptive Test Names:**  Test names now clearly indicate the scenario being tested.


This improved test suite is more robust and covers a wider range of possible scenarios, making it a more reliable test suite for the `extract_conversations_from_html` function. Remember to install `pytest` and `bs4` if you haven't already:
```bash
pip install pytest beautifulsoup4
```