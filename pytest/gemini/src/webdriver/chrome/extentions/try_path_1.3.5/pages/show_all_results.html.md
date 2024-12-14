```python
import pytest
from bs4 import BeautifulSoup

# Since the provided code is HTML, we'll focus on testing the structure and elements using BeautifulSoup
# We'll simulate the behavior that a browser would have when parsing the HTML.

@pytest.fixture
def html_content():
    """Provides the HTML content as a string."""
    return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Tryxpath show all results</title>
    <script src="../scripts/try_xpath_functions.js"></script>
    <script src="show_all_results.js"></script>
    <link rel="stylesheet" href="show_all_results.css"/>
  </head>

  <body>
    <div>
      <h1>Export links</h1>
      <ul>
        <li><a id="export-text">Plain text</a></li>
        <li><a id="export-partly-converted">Some values are converted by JSON.stringify.</a></li>
      </ul>
    </div>
    <div>
      <h1>Information</h1>
      <table>
        <tbody>
          <tr><th>Message</th><td id="message"></td></tr>
          <tr><th>Title</th><td id="title"></td></tr>
          <tr><th>URL</th><td id="url"></td></tr>
          <tr><th>frameId</th><td id="frame-id"</td></tr>
        </tbody>
      </table>
    </div>
    <div id="context-area">
      <h1>Context information</h1>
      <table>
        <tbody>
          <tr><th>Method</th><td id="context-method"></td></tr>
          <tr><th>Expression</th><td id="context-expression"></td></tr>
          <tr><th>Specified resultType</th><td id="context-specified-result-type"></td></tr>
          <tr><th>resultType</th><td id="context-result-type"></td></tr>
          <tr><th>Resolver</th><td id="context-resolver"></td></tr>
        </tbody>
      </table>
      <h1>Context detail</h1>
      <table id="context-detail">
        <tbody>
        </tbody>
      </table>
    </div>
    <div>
      <h1>Main information</h1>
      <table>
        <tbody>
          <tr><th>Method</th><td id="main-method"></td></tr>
          <tr><th>Expression</th><td id="main-expression"></td></tr>
          <tr><th>Specified resultType</th><td id="main-specified-result-type"></td></tr>
          <tr><th>resultType</th><td id="main-result-type"></td></tr>
          <tr><th>Resolver</th><td id="main-resolver"></td></tr>
          <tr><th>Count</th><td id="main-count"></td><tr>
        </tbody>
      </table>
      <h1>Main details</h1>
      <table id="main-details">
        <tbody>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""

@pytest.fixture
def parsed_html(html_content):
    """Parses the HTML content using BeautifulSoup."""
    return BeautifulSoup(html_content, 'html.parser')


def test_html_structure(parsed_html):
    """Checks if the basic HTML structure is present."""
    assert parsed_html.find('html') is not None, "HTML tag not found"
    assert parsed_html.find('head') is not None, "Head tag not found"
    assert parsed_html.find('body') is not None, "Body tag not found"


def test_title_content(parsed_html):
  """Checks the content of the title tag."""
  title = parsed_html.find('title')
  assert title is not None, "Title tag not found"
  assert title.text == "Tryxpath show all results", "Incorrect title content"


def test_export_links_section(parsed_html):
  """Checks for the presence and correct structure of export links."""
  export_div = parsed_html.find('div', string=lambda text: text and "Export links" in text)
  assert export_div is not None, "Export links div not found"
  
  ul_tag = export_div.find('ul')
  assert ul_tag is not None, "Unordered list for export links not found"

  list_items = ul_tag.find_all('li')
  assert len(list_items) == 2, "Incorrect number of export link items"
  
  link1 = list_items[0].find('a', {'id': 'export-text'})
  assert link1 is not None
  assert link1.text == 'Plain text'
  
  link2 = list_items[1].find('a', {'id': 'export-partly-converted'})
  assert link2 is not None
  assert link2.text == "Some values are converted by JSON.stringify."

def test_information_section(parsed_html):
    """Checks the structure of the Information section and its table."""
    info_div = parsed_html.find('div', string=lambda text: text and "Information" in text)
    assert info_div is not None, "Information div not found"

    table = info_div.find('table')
    assert table is not None, "Information table not found"

    tbody = table.find('tbody')
    assert tbody is not None, "Information table body not found"

    rows = tbody.find_all('tr')
    assert len(rows) == 4, "Incorrect number of rows in information table"

    # Check specific cells
    assert rows[0].find('th').text == "Message"
    assert rows[0].find('td', {'id': 'message'}) is not None

    assert rows[1].find('th').text == "Title"
    assert rows[1].find('td', {'id': 'title'}) is not None

    assert rows[2].find('th').text == "URL"
    assert rows[2].find('td', {'id': 'url'}) is not None
    
    assert rows[3].find('th').text == "frameId"
    assert rows[3].find('td', {'id': 'frame-id'}) is not None


def test_context_area_section(parsed_html):
    """Checks the structure of the Context information area and its tables."""
    context_div = parsed_html.find('div', {'id': 'context-area'})
    assert context_div is not None, "Context area div not found"
    
    info_h1 = context_div.find('h1', string="Context information")
    assert info_h1 is not None, "Context information h1 not found"

    table1 = context_div.find('table')
    assert table1 is not None, "Context information table not found"
    
    tbody1 = table1.find('tbody')
    assert tbody1 is not None, "Context information table body not found"

    rows1 = tbody1.find_all('tr')
    assert len(rows1) == 5, "Incorrect number of rows in context information table"

    # Check specific cells in context information table
    assert rows1[0].find('th').text == "Method"
    assert rows1[0].find('td', {'id': 'context-method'}) is not None
    assert rows1[1].find('th').text == "Expression"
    assert rows1[1].find('td', {'id': 'context-expression'}) is not None
    assert rows1[2].find('th').text == "Specified resultType"
    assert rows1[2].find('td', {'id': 'context-specified-result-type'}) is not None
    assert rows1[3].find('th').text == "resultType"
    assert rows1[3].find('td', {'id': 'context-result-type'}) is not None
    assert rows1[4].find('th').text == "Resolver"
    assert rows1[4].find('td', {'id': 'context-resolver'}) is not None
    
    detail_h1 = context_div.find('h1', string="Context detail")
    assert detail_h1 is not None, "Context detail h1 not found"
    
    table2 = context_div.find('table', {'id': 'context-detail'})
    assert table2 is not None, "Context detail table not found"
    tbody2 = table2.find('tbody')
    assert tbody2 is not None, "Context detail table body not found"
    

def test_main_information_section(parsed_html):
    """Checks the structure of the Main information section and its tables."""
    main_div = parsed_html.find('div', string=lambda text: text and "Main information" in text)
    assert main_div is not None, "Main information div not found"

    table1 = main_div.find('table')
    assert table1 is not None, "Main information table not found"

    tbody1 = table1.find('tbody')
    assert tbody1 is not None, "Main information table body not found"

    rows1 = tbody1.find_all('tr')
    assert len(rows1) == 6, "Incorrect number of rows in main information table"

    # Check specific cells in main information table
    assert rows1[0].find('th').text == "Method"
    assert rows1[0].find('td', {'id': 'main-method'}) is not None
    assert rows1[1].find('th').text == "Expression"
    assert rows1[1].find('td', {'id': 'main-expression'}) is not None
    assert rows1[2].find('th').text == "Specified resultType"
    assert rows1[2].find('td', {'id': 'main-specified-result-type'}) is not None
    assert rows1[3].find('th').text == "resultType"
    assert rows1[3].find('td', {'id': 'main-result-type'}) is not None
    assert rows1[4].find('th').text == "Resolver"
    assert rows1[4].find('td', {'id': 'main-resolver'}) is not None
    assert rows1[5].find('th').text == "Count"
    assert rows1[5].find('td', {'id': 'main-count'}) is not None

    
    details_h1 = main_div.find('h1', string="Main details")
    assert details_h1 is not None, "Main details h1 not found"
    
    table2 = main_div.find('table', {'id': 'main-details'})
    assert table2 is not None, "Main details table not found"
    tbody2 = table2.find('tbody')
    assert tbody2 is not None, "Main details table body not found"
```