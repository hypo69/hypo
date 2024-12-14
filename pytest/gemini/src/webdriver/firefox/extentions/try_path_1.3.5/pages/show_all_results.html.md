```python
import pytest
from bs4 import BeautifulSoup

# Since the provided code is HTML, we'll use BeautifulSoup to parse it and then test its structure.
# This requires installing BeautifulSoup4: pip install beautifulsoup4

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


def test_html_has_head(html_content):
    """Checks if the HTML has a head element."""
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.head is not None

def test_html_has_title(html_content):
    """Checks if the HTML has a title element with correct content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.title is not None
    assert soup.title.string == "Tryxpath show all results"

def test_html_has_body(html_content):
    """Checks if the HTML has a body element."""
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.body is not None


def test_html_has_export_links(html_content):
    """Checks if the HTML has the export links section."""
    soup = BeautifulSoup(html_content, 'html.parser')
    export_links_div = soup.find('div', string="Export links")
    assert export_links_div is not None
    assert export_links_div.find_next('ul') is not None
    export_links = export_links_div.find_next('ul').find_all('li')
    assert len(export_links) == 2
    assert export_links[0].find('a', {'id':'export-text'}) is not None
    assert export_links[1].find('a', {'id':'export-partly-converted'}) is not None
    
def test_html_has_information_table(html_content):
    """Checks if the HTML has the information table."""
    soup = BeautifulSoup(html_content, 'html.parser')
    information_div = soup.find('div', string="Information")
    assert information_div is not None
    information_table = information_div.find_next('table')
    assert information_table is not None
    rows = information_table.find('tbody').find_all('tr')
    assert len(rows) == 4
    assert rows[0].find('td', {'id': 'message'}) is not None
    assert rows[1].find('td', {'id': 'title'}) is not None
    assert rows[2].find('td', {'id': 'url'}) is not None
    assert rows[3].find('td', {'id': 'frame-id'}) is not None
    

def test_html_has_context_area(html_content):
    """Checks if the HTML has the context area section."""
    soup = BeautifulSoup(html_content, 'html.parser')
    context_area_div = soup.find('div', {'id': 'context-area'})
    assert context_area_div is not None
    
    context_info_table = context_area_div.find('table')
    assert context_info_table is not None
    rows = context_info_table.find('tbody').find_all('tr')
    assert len(rows) == 5
    assert rows[0].find('td', {'id':'context-method'}) is not None
    assert rows[1].find('td', {'id':'context-expression'}) is not None
    assert rows[2].find('td', {'id':'context-specified-result-type'}) is not None
    assert rows[3].find('td', {'id':'context-result-type'}) is not None
    assert rows[4].find('td', {'id':'context-resolver'}) is not None
    
    context_detail_table = context_area_div.find('table', {'id': 'context-detail'})
    assert context_detail_table is not None


def test_html_has_main_information(html_content):
    """Checks if the HTML has the main information section."""
    soup = BeautifulSoup(html_content, 'html.parser')
    main_information_div = soup.find('div', string="Main information")
    assert main_information_div is not None
    main_info_table = main_information_div.find_next('table')
    assert main_info_table is not None
    rows = main_info_table.find('tbody').find_all('tr')
    assert len(rows) == 6
    assert rows[0].find('td', {'id': 'main-method'}) is not None
    assert rows[1].find('td', {'id': 'main-expression'}) is not None
    assert rows[2].find('td', {'id': 'main-specified-result-type'}) is not None
    assert rows[3].find('td', {'id': 'main-result-type'}) is not None
    assert rows[4].find('td', {'id': 'main-resolver'}) is not None
    assert rows[5].find('td', {'id': 'main-count'}) is not None

    main_details_table = main_information_div.find_next('table', {'id': 'main-details'})
    assert main_details_table is not None

def test_html_has_correct_scripts(html_content):
    """Check if the HTML has the correct scripts"""
    soup = BeautifulSoup(html_content, 'html.parser')
    scripts = soup.find_all('script')
    assert len(scripts) == 2
    assert any(script.get('src') == "../scripts/try_xpath_functions.js" for script in scripts)
    assert any(script.get('src') == "show_all_results.js" for script in scripts)

def test_html_has_correct_stylesheet(html_content):
  """Check if the HTML has the correct stylesheet."""
  soup = BeautifulSoup(html_content, 'html.parser')
  links = soup.find_all('link')
  assert len(links) == 1
  assert any(link.get('href') == "show_all_results.css" for link in links)
```