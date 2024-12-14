```python
import pytest

# Since the provided code is HTML, there's no Python code to directly test with pytest.
# However, we can simulate testing by checking if the HTML structure is as expected
# or by checking if the HTML file exists and can be read.
# In a real application, this HTML would likely be rendered by a browser,
# and more comprehensive tests would be done using browser automation tools like Selenium.


def test_popup_html_file_exists(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks if the popup.html file exists."""
    import os
    assert os.path.exists(File_location), f"File not found: {File_location}"


def test_popup_html_content(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks basic structure and content of popup.html."""
    try:
        with open(File_location, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
         pytest.fail(f"File not found: {File_location}")

    assert "<!DOCTYPE html>" in html_content
    assert "<html" in html_content
    assert "<head>" in html_content
    assert "<title>hypotez</title>" in html_content
    assert "<body" in html_content
    assert "<h1>hypotez</h1>" in html_content
    assert "<p>Click the extension icon to collect data from the current webpage.</p>" in html_content
    assert "</html>" in html_content
    assert "width: 200px;" in html_content
    assert "padding: 10px;" in html_content
    
def test_popup_html_no_scripts(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks that popup.html doesn't contain scripts."""
    try:
        with open(File_location, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
         pytest.fail(f"File not found: {File_location}")
    
    assert "<script" not in html_content, "popup.html should not contain <script> tags for security reasons."
    

def test_popup_html_proper_encoding(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks if HTML is encoded in UTF-8."""
    try:
        with open(File_location, 'r', encoding='utf-8') as f:
            # Attempt to read and decode as UTF-8. If it fails, it will raise an error, failing the test.
            f.read()
    except UnicodeDecodeError:
        pytest.fail("The file is not encoded in UTF-8.")
    except FileNotFoundError:
        pytest.fail(f"File not found: {File_location}")
        

def test_popup_html_contains_hypotez_title(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks if the HTML contains the title hypotez."""
    try:
        with open(File_location, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
         pytest.fail(f"File not found: {File_location}")

    assert "<title>hypotez</title>" in html_content

def test_popup_html_has_paragraph(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks if the HTML has the paragraph about clicking the extension icon."""
    try:
        with open(File_location, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
         pytest.fail(f"File not found: {File_location}")
    assert "<p>Click the extension icon to collect data from the current webpage.</p>" in html_content
    
def test_popup_html_has_h1_hypotez(File_location='hypotez/src/webdriver/edge/extentions/test_extention/html/popup.html'):
    """Checks if the HTML has the H1 hypotez."""
    try:
        with open(File_location, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
         pytest.fail(f"File not found: {File_location}")
    assert "<h1>hypotez</h1>" in html_content
```