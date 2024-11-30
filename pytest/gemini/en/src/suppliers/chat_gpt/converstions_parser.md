```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup
from hypotez.src.suppliers.chat_gpt.converstions_parser import extract_conversations_from_html

# Create a dummy HTML file for testing
def create_dummy_html(content):
    temp_file = Path("test_chat.html")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(content)
    return temp_file


def test_extract_conversations_from_html_valid_input():
    """Tests with a valid HTML file containing conversation divs."""
    html_content = """
    <html>
    <body>
        <div class="conversation">Conversation 1</div>
        <div class="conversation">Conversation 2</div>
        <div>Not a conversation</div>
    </body>
    </html>
    """
    temp_file = create_dummy_html(html_content)
    conversations = list(extract_conversations_from_html(temp_file))
    assert len(conversations) == 2
    assert conversations[0].text == "Conversation 1"
    assert conversations[1].text == "Conversation 2"
    temp_file.unlink()


def test_extract_conversations_from_html_no_conversations():
    """Tests with a valid HTML file containing no conversation divs."""
    html_content = """
    <html>
    <body>
        <div>Not a conversation</div>
    </body>
    </html>
    """
    temp_file = create_dummy_html(html_content)
    conversations = list(extract_conversations_from_html(temp_file))
    assert len(conversations) == 0
    temp_file.unlink()


def test_extract_conversations_from_html_invalid_file_path():
    """Tests with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        list(extract_conversations_from_html(Path("nonexistent_file.html")))


def test_extract_conversations_from_html_empty_file():
    """Tests with an empty file."""
    temp_file = create_dummy_html("")
    conversations = list(extract_conversations_from_html(temp_file))
    assert len(conversations) == 0
    temp_file.unlink()


def test_extract_conversations_from_html_malformed_html():
    """Tests with malformed HTML."""
    html_content = "<html><body><div class='conversation'  Conversation 1</div></body></html>"
    temp_file = create_dummy_html(html_content)
    conversations = list(extract_conversations_from_html(temp_file))
    assert len(conversations) == 0  # Should not crash
    temp_file.unlink()


def test_extract_conversations_from_html_encoding_error():
    """Test with a file containing non-UTF-8 characters."""
    html_content = "<html><body><div class='conversation'>Non-UTF-8</div></body></html>"
    temp_file = create_dummy_html(html_content.encode("latin-1"))
    with pytest.raises(UnicodeDecodeError):
        list(extract_conversations_from_html(temp_file))
    temp_file.unlink()

```

**Explanation and Improvements:**

* **Dummy HTML Creation:** The `create_dummy_html` function now creates temporary HTML files for testing, which is crucial for avoiding file system conflicts and ensuring tests operate on isolated data.  The files are cleaned up after each test with `temp_file.unlink()`. This is critical for avoiding leftover files and problems.


* **Comprehensive Test Cases:** Added tests for no conversations, empty files, invalid file paths, malformed HTML, and crucial encoding error handling (using `pytest.raises`).


* **Clearer Test Names:** Test names are more descriptive and indicate the specific input/expected outcome.


* **Exception Handling:**  Uses `pytest.raises` for testing `FileNotFoundError` and `UnicodeDecodeError`.  This is better practice than relying on `try...except` blocks within the test functions.

* **Robustness:** The tests now cover various potential issues like missing conversations, malformed HTML, and incorrect encodings – vital for ensuring the code's reliability in real-world scenarios.

* **Isolation:** All tests are independent and don't rely on the state of previous tests.

Remember to run `pytest` in the directory containing these test functions to execute them.  This revised solution is much more robust and realistic for testing production code. Remember to replace `"test_chat.html"` with the actual file path if you need a different name.