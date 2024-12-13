```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup
from unittest.mock import mock_open, patch
from hypotez.src.suppliers.chat_gpt.converstions_parser import extract_conversations_from_html

@pytest.fixture
def sample_html_content():
    """Provides sample HTML content for testing."""
    return """
    <html>
        <body>
            <div class="conversation">
                <p>Conversation 1</p>
            </div>
            <div class="conversation">
                <p>Conversation 2</p>
            </div>
            <div>
                <p>Not a conversation</p>
            </div>
            <div class="conversation">
                <p>Conversation 3</p>
            </div>
        </body>
    </html>
    """


@pytest.fixture
def mock_file_path(tmp_path, sample_html_content):
    """Creates a mock file for testing."""
    file_path = tmp_path / "test.html"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(sample_html_content)
    return file_path

def test_extract_conversations_from_html_valid_file(mock_file_path):
    """Test with a valid html file, checks if the correct number of conversations are found and yielded"""
    conversations = list(extract_conversations_from_html(mock_file_path))
    assert len(conversations) == 3
    # check that it's beautiful soup object
    assert isinstance(conversations[0], BeautifulSoup)
    assert "<p>Conversation 1</p>" in str(conversations[0])


def test_extract_conversations_from_html_no_conversation(tmp_path):
    """Test with html file with no conversation div, checks if an empty generator is yielded."""
    file_path = tmp_path / "no_conversation.html"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("<html><body><div><p>No conversation</p></div></body></html>")

    conversations = list(extract_conversations_from_html(file_path))
    assert len(conversations) == 0


def test_extract_conversations_from_html_empty_file(tmp_path):
    """Test with an empty html file, checks if an empty generator is yielded."""
    file_path = tmp_path / "empty.html"
    file_path.touch()
    conversations = list(extract_conversations_from_html(file_path))
    assert len(conversations) == 0


def test_extract_conversations_from_html_file_not_found():
    """Test with a file path that does not exist, checks if FileNotFoundError is raised."""
    non_existent_file = Path("non_existent.html")
    with pytest.raises(FileNotFoundError):
         list(extract_conversations_from_html(non_existent_file))


def test_extract_conversations_from_html_invalid_file_type(tmp_path):
    """Test with a non-html file, checks for a suitable exception (for example, UnicodeDecodeError if it can't be opened as HTML)."""
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("This is not an html file")
    with pytest.raises((UnicodeDecodeError, Exception)):
        list(extract_conversations_from_html(file_path))


def test_extract_conversations_from_html_malformed_html(tmp_path):
    """Test with a malformed HTML file. This checks if BS can parse a malformed file. We do not expect exceptions here, just that it might return empty result."""
    file_path = tmp_path / "malformed.html"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("<html><body><div class='conversation'>Unclosed tag")
    
    conversations = list(extract_conversations_from_html(file_path))
    # BeautifulSoup might be able to parse and return 1 or 0 conversations
    # we will check that it does not fail

```