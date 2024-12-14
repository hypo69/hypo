```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup

# Fixture to load the HTML content
@pytest.fixture
def html_content():
    """Provides the HTML content from the file."""
    file_path = Path("hypotez/src/webdriver/edge/extentions/try_path_1.3.5/pages/show_all_results.html")
    with open(file_path, "r", encoding="utf-8") as f:
      return f.read()

# Fixture to parse the HTML content
@pytest.fixture
def soup(html_content):
    """Provides a BeautifulSoup object for the HTML content."""
    return BeautifulSoup(html_content, 'html.parser')

# Test for correct title
def test_title_correct(soup):
    """Checks if the title of the HTML page is correct."""
    title_tag = soup.find('title')
    assert title_tag is not None
    assert title_tag.text == "Tryxpath show all results"

# Test for export links presence
def test_export_links_presence(soup):
    """Checks if export links are present."""
    export_links = soup.find('div').find('ul').find_all('li')
    assert len(export_links) == 2
    assert export_links[0].find('a', id="export-text") is not None
    assert export_links[1].find('a', id="export-partly-converted") is not None

# Test for information table presence and structure
def test_information_table_presence_and_structure(soup):
    """Checks if information table is present and has the correct structure."""
    info_table = soup.find('div').find('table')
    assert info_table is not None
    tbody = info_table.find('tbody')
    assert tbody is not None
    rows = tbody.find_all('tr')
    assert len(rows) == 4
    assert rows[0].find('th').text == "Message"
    assert rows[0].find('td', id="message") is not None
    assert rows[1].find('th').text == "Title"
    assert rows[1].find('td', id="title") is not None
    assert rows[2].find('th').text == "URL"
    assert rows[2].find('td', id="url") is not None
    assert rows[3].find('th').text == "frameId"
    assert rows[3].find('td', id="frame-id") is not None


# Test for context information table presence and structure
def test_context_information_table_presence_and_structure(soup):
    """Checks if context information table is present and has the correct structure."""
    context_area = soup.find(id="context-area")
    assert context_area is not None
    context_table = context_area.find('table')
    assert context_table is not None
    tbody = context_table.find('tbody')
    assert tbody is not None
    rows = tbody.find_all('tr')
    assert len(rows) == 5
    assert rows[0].find('th').text == "Method"
    assert rows[0].find('td', id="context-method") is not None
    assert rows[1].find('th').text == "Expression"
    assert rows[1].find('td', id="context-expression") is not None
    assert rows[2].find('th').text == "Specified resultType"
    assert rows[2].find('td', id="context-specified-result-type") is not None
    assert rows[3].find('th').text == "resultType"
    assert rows[3].find('td', id="context-result-type") is not None
    assert rows[4].find('th').text == "Resolver"
    assert rows[4].find('td', id="context-resolver") is not None

# Test for context detail table presence
def test_context_detail_table_presence(soup):
    """Checks if the context detail table is present."""
    context_detail_table = soup.find(id="context-detail")
    assert context_detail_table is not None
    assert context_detail_table.find('tbody') is not None


# Test for main information table presence and structure
def test_main_information_table_presence_and_structure(soup):
    """Checks if main information table is present and has the correct structure."""
    main_info_div = soup.find_all('div')[4]
    assert main_info_div is not None
    main_table = main_info_div.find('table')
    assert main_table is not None
    tbody = main_table.find('tbody')
    assert tbody is not None
    rows = tbody.find_all('tr')
    assert len(rows) == 6
    assert rows[0].find('th').text == "Method"
    assert rows[0].find('td', id="main-method") is not None
    assert rows[1].find('th').text == "Expression"
    assert rows[1].find('td', id="main-expression") is not None
    assert rows[2].find('th').text == "Specified resultType"
    assert rows[2].find('td', id="main-specified-result-type") is not None
    assert rows[3].find('th').text == "resultType"
    assert rows[3].find('td', id="main-result-type") is not None
    assert rows[4].find('th').text == "Resolver"
    assert rows[4].find('td', id="main-resolver") is not None
    assert rows[5].find('th').text == "Count"
    assert rows[5].find('td', id="main-count") is not None

# Test for main detail table presence
def test_main_detail_table_presence(soup):
    """Checks if the main detail table is present."""
    main_detail_table = soup.find(id="main-details")
    assert main_detail_table is not None
    assert main_detail_table.find('tbody') is not None

# Test for charset meta tag
def test_charset_meta_tag(soup):
    """Checks if the charset meta tag is present and has the correct value."""
    charset_meta = soup.find('meta', charset="utf-8")
    assert charset_meta is not None

def test_script_tags_presence(soup):
  """Checks if the script tags are present and have the correct src attributes"""
  scripts = soup.find_all('script')
  assert len(scripts) == 2

  script_src_1 = scripts[0].get('src')
  assert script_src_1 == "../scripts/try_xpath_functions.js"

  script_src_2 = scripts[1].get('src')
  assert script_src_2 == "show_all_results.js"

def test_css_link_presence(soup):
    """Checks if the CSS link tag is present and has the correct href attribute."""
    css_link = soup.find('link', rel="stylesheet", href="show_all_results.css")
    assert css_link is not None
```