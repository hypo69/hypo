```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup
from hypotez.src.suppliers.chat_gpt.converstions_parser import extract_conversations_from_html

# Create a dummy HTML file for testing purposes
def create_dummy_html(filename, conversations_content):
    html_content = f"""
    <html>
    <body>
    {conversations_content}
    </body>
    </html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

# Fixture to create and clean up temporary files
@pytest.fixture
def temp_html_file():
    temp_file_name = "temp_chat.html"
    conversations_content = "<div class=\"conversation\">Conversation 1</div>"
    create_dummy_html(temp_file_name, conversations_content)
    yield Path(temp_file_name)
    import os
    os.remove(temp_file_name)


def test_extract_conversations_from_html_valid_input(temp_html_file):
    """Checks correct behavior with a valid HTML file containing a conversation div."""
    conversations = list(extract_conversations_from_html(temp_html_file))
    assert len(conversations) == 1
    assert conversations[0].text == "Conversation 1"


def test_extract_conversations_from_html_multiple_conversations(temp_html_file):
    """Checks handling of multiple conversation divs in a valid HTML file."""
    conversations_content = """
        <div class="conversation">Conversation 1</div>
        <div class="conversation">Conversation 2</div>
    """
    create_dummy_html("temp_chat.html", conversations_content)
    file_path = Path("temp_chat.html")
    conversations = list(extract_conversations_from_html(file_path))
    assert len(conversations) == 2
    assert conversations[0].text == "Conversation 1"
    assert conversations[1].text == "Conversation 2"


def test_extract_conversations_from_html_no_conversations(temp_html_file):
    """Checks handling of an HTML file with no conversation divs."""
    conversations_content = "<html><body></body></html>"
    create_dummy_html("temp_chat.html", conversations_content)
    file_path = Path("temp_chat.html")
    conversations = list(extract_conversations_from_html(file_path))
    assert len(conversations) == 0


def test_extract_conversations_from_html_invalid_file(temp_html_file):
    """Checks handling of a file that doesn't exist."""
    invalid_file_path = Path("nonexistent_file.html")
    with pytest.raises(FileNotFoundError):
        list(extract_conversations_from_html(invalid_file_path))

def test_extract_conversations_from_html_no_class(temp_html_file):
    """Checks behavior with a div that doesn't have the specified class."""
    conversations_content = """<div>Conversation not having the class</div>"""
    create_dummy_html("temp_chat.html", conversations_content)
    file_path = Path("temp_chat.html")
    conversations = list(extract_conversations_from_html(file_path))
    assert len(conversations) == 0


```