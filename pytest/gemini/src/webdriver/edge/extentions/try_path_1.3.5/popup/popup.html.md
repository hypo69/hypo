```python
import pytest
from bs4 import BeautifulSoup

# Since the provided code is HTML, we'll use BeautifulSoup to parse it for testing purposes.
# The tests will focus on checking the structure and expected elements.
# This isn't a typical test suite as it's not testing Python code, but rather HTML structure.
# The HTML elements are what the JavaScript code would interact with, so it's still valuable for testing.

@pytest.fixture
def html_content():
    """Provides the HTML content for testing."""
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="popup.css"/>
<script src="../scripts/try_xpath_functions.js"></script>
<script src="popup.js"></script>
</head>
<body>
<div><button id="execute">Execute</button></div>
<div id="help-body"><input type="checkbox" id="help-switch"><label for="help-switch">Help</label></div>
<div>
  <h1>Main</h1>
  <div id="main-body">
    <dl>
      <dt><label for="main-way">Way</label></dt>
      <dd>
        <select id="main-way">
          <option data-method="evaluate" data-type="ANY_TYPE">xpath ANY_TYPE</option>
          <option data-method="evaluate" data-type="NUMBER_TYPE">xpath NUMBER_TYPE</option>
          <option data-method="evaluate" data-type="STRING_TYPE">xpath STRING_TYPE</option>
          <option data-method="evaluate" data-type="BOOLEAN_TYPE">xpath BOOLEAN_TYPE</option>
          <option data-method="evaluate" data-type="UNORDERED_NODE_ITERATOR_TYPE">xpath UNORDERED_NODE_ITERATOR_TYPE</option>
          <option data-method="evaluate" data-type="ORDERED_NODE_ITERATOR_TYPE">xpath ORDERED_NODE_ITERATOR_TYPE</option>
          <option data-method="evaluate" data-type="UNORDERED_NODE_SNAPSHOT_TYPE">xpath UNORDERED_NODE_SNAPSHOT_TYPE</option>
          <option data-method="evaluate" data-type="ORDERED_NODE_SNAPSHOT_TYPE">xpath ORDERED_NODE_SNAPSHOT_TYPE</option>
          <option data-method="evaluate" data-type="ANY_UNORDERED_NODE_TYPE">xpath ANY_UNORDERED_NODE_TYPE</option>
          <option data-method="evaluate" data-type="FIRST_ORDERED_NODE_TYPE">xpath FIRST_ORDERED_NODE_TYPE</option>
          <option data-method="querySelector" data-type="">querySelector</option>
          <option data-method="querySelectorAll" data-type="">querySelectorAll</option>
        </select>
      </dd>
      <dt><label for="main-expression">Expression</label></dt>
      <dd><textarea id="main-expression"></textarea></dd>
    </dl>
    <div class="help">If you want to enter a new line, please enter the Shift-Enter.</div>
  </div>
</div>
<div>
  <h1 id="context-header"><input type="checkbox" id="context-switch"><label for="context-switch">Context</label></h1>
  <div id="context-body">
    <div class="help">You can specify a context. The first node of the results is used as the CONTEXT. (document.evaluate(expr, CONTEXT, ...), CONTEXT.querySelector(...), CONTEXT.querySelectorAll(...))</div>
    <dl>
      <dt><label for="context-way">Way</label></dt>
      <dd>
        <select id="context-way">
          <option data-method="evaluate" data-type="ANY_TYPE">xpath ANY_TYPE</option>
          <option data-method="evaluate" data-type="UNORDERED_NODE_ITERATOR_TYPE">xpath UNORDERED_NODE_ITERATOR_TYPE</option>
          <option data-method="evaluate" data-type="ORDERED_NODE_ITERATOR_TYPE">xpath ORDERED_NODE_ITERATOR_TYPE</option>
          <option data-method="evaluate" data-type="UNORDERED_NODE_SNAPSHOT_TYPE">xpath UNORDERED_NODE_SNAPSHOT_TYPE</option>
          <option data-method="evaluate" data-type="ORDERED_NODE_SNAPSHOT_TYPE">xpath ORDERED_NODE_SNAPSHOT_TYPE</option>
          <option data-method="evaluate" data-type="ANY_UNORDERED_NODE_TYPE">xpath ANY_UNORDERED_NODE_TYPE</option>
          <option data-method="evaluate" data-type="FIRST_ORDERED_NODE_TYPE">xpath FIRST_ORDERED_NODE_TYPE</option>
          <option data-method="querySelector" data-type="">querySelector</option>
          <option data-method="querySelectorAll" data-type="">querySelectorAll</option>
        </select>
      </dd>
      <dt><label for="context-expression">Expression</label></dt>
      <dd><textarea id="context-expression"></textarea></dd>
    </dl>
  </div>
</div>
<div>
  <h1 id="resolver-header"><input type="checkbox" id="resolver-switch"><label for="resolver-switch">namespaceResolver</label></h1>
  <div id="resolver-body">
    <div class="help">You can specify the behavior of the namespaceResolver function. If you want to get the P elements which are in the "http://www.w3.org/1999/xhtml" namespace, please do as follows.
      <ol>
        <li>Enter {"x":"http://www.w3.org/1999/xhtml"} in the resolver input field.</li>
        <li>Enter //x:p in the expression input field.</li>
        <li>Click the Execute button.</li>
      </ol>
    </div>
    <dl>
      <dt><label for="resolver-expression">Resolver</label></dt>
      <dd><input type="text" id="resolver-expression"></dd>
    </dl>
  </div>
</div>
<div class="none">
  <h1 id="frame-designation-header"><input type="checkbox" id="frame-designation-switch"><label for="frame-designation-switch">Frame without id</label></h1>
  <div id="frame-designation-body">
    <div class="help">You can specify the frame which does not have frameId. If you want to specify window.frames[1].frames[0] enter [1, 0] in the frame input field. This specification starts with the frame specified by frameId.</div>
    <dl>
      <dt><label for="frame-designation-expression">Frame</label></dt>
      <dd><input type="text" id="frame-designation-expression"></dd>
    </dl>
    <div><button id="focus-designated-frame">Focus frame</button></div>
  </div>
</div>
<div>
  <h1 id="frame-id-header"><input type="checkbox" id="frame-id-switch"><label for="frame-id-switch">frameId</label></h1>
  <div id="frame-id-body">
    <div class="help">You can specify the frame where the expression is executed. If you want to specify a frame, please do as follows.
      <ol>
        <li>Click the Get-all-frameId button.</li>
        <li>Select a frameId.</li>
        <li>Click the Focus-frame button.</li>
        <li>Execute a expression.</li>
      </ol>
    </div>
    <div>
      <button id="get-all-frame-id">Get all frameId</button><select id="frame-id-list"><option data-frame-id="manual">Manual</option></select>
    </div>
    <dl>
      <dt><label for="frame-id-expression">frameId</label></dt>
      <dd><input type="text" id="frame-id-expression"></dd>
    </dl>
    <div><button id="focus-frame">Focus frame</button><button id="show-previous-results">Show previous results</button></div>
  </div>
</div>
<div>
  <h1>Results</h1>
  <div>Message: <span id="results-message"></span></div>
  <div>Count: <span id="results-count"></span></div>
  <div>frameId: <span id="results-frame-id"></span></div>
  <div><button id="show-all-results">Show all results</button><button id="open-options">Open options</button><button id="set-style">Set style</button><button id="reset-style">Reset style</button><button id="set-all-style">Set style(all frames)</button><button id="reset-all-style">Reset style(all frame)</button></div>
  <h2>Context detail</h2>
  <table id="context-detail">
    <tbody></tbody>
  </table>
  <h2>Details</h2>
  <div><button id="previous-details-page">&lt;</button><button id="move-details-page">Move</button><input type="text" id="details-page-count"><button id="next-details-page">&gt;</button></div>
  <table id="results-details">
    <tbody></tbody>
  </table>
</div>
</body>
</html>
    """


def test_popup_html_structure(html_content):
    """Test that the basic structure of the popup.html is correct."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Check for required elements
    assert soup.find('button', id='execute') is not None, "Execute button not found"
    assert soup.find('div', id='help-body') is not None, "Help body div not found"
    assert soup.find('select', id='main-way') is not None, "Main way select not found"
    assert soup.find('textarea', id='main-expression') is not None, "Main expression textarea not found"
    assert soup.find('div', id='context-body') is not None, "Context body div not found"
    assert soup.find('select', id='context-way') is not None, "Context way select not found"
    assert soup.find('textarea', id='context-expression') is not None, "Context expression textarea not found"
    assert soup.find('div', id='resolver-body') is not None, "Resolver body div not found"
    assert soup.find('input', id='resolver-expression') is not None, "Resolver expression input not found"
    assert soup.find('div', id='frame-designation-body') is not None, "Frame designation body div not found"
    assert soup.find('input', id='frame-designation-expression') is not None, "Frame designation expression input not found"
    assert soup.find('div', id='frame-id-body') is not None, "Frame ID body div not found"
    assert soup.find('select', id='frame-id-list') is not None, "Frame ID list select not found"
    assert soup.find('input', id='frame-id-expression') is not None, "Frame ID expression input not found"
    assert soup.find('div', id='results-message') is not None, "Results message span not found"
    assert soup.find('div', id='results-count') is not None, "Results count span not found"
    assert soup.find('div', id='results-frame-id') is not None, "Results frame ID span not found"
    assert soup.find('table', id='context-detail') is not None, "Context detail table not found"
    assert soup.find('table', id='results-details') is not None, "Results details table not found"


def test_main_way_select_options(html_content):
    """Test the options within the main-way select element."""
    soup = BeautifulSoup(html_content, 'html.parser')
    select = soup.find('select', id='main-way')
    assert select is not None, "Main way select not found"

    expected_options = [
        ("xpath ANY_TYPE", "evaluate", "ANY_TYPE"),
        ("xpath NUMBER_TYPE", "evaluate", "NUMBER_TYPE"),
        ("xpath STRING_TYPE", "evaluate", "STRING_TYPE"),
        ("xpath BOOLEAN_TYPE", "evaluate", "BOOLEAN_TYPE"),
        ("xpath UNORDERED_NODE_ITERATOR_TYPE", "evaluate", "UNORDERED_NODE_ITERATOR_TYPE"),
        ("xpath ORDERED_NODE_ITERATOR_TYPE", "evaluate", "ORDERED_NODE_ITERATOR_TYPE"),
        ("xpath UNORDERED_NODE_SNAPSHOT_TYPE", "evaluate", "UNORDERED_NODE_SNAPSHOT_TYPE"),
        ("xpath ORDERED_NODE_SNAPSHOT_TYPE", "evaluate", "ORDERED_NODE_SNAPSHOT_TYPE"),
        ("xpath ANY_UNORDERED_NODE_TYPE", "evaluate", "ANY_UNORDERED_NODE_TYPE"),
        ("xpath FIRST_ORDERED_NODE_TYPE", "evaluate", "FIRST_ORDERED_NODE_TYPE"),
        ("querySelector", "querySelector", ""),
        ("querySelectorAll", "querySelectorAll", ""),
    ]

    options = select.find_all('option')
    assert len(options) == len(expected_options), "Number of main-way select options is incorrect"

    for option, expected in zip(options, expected_options):
        assert option.text == expected[0], f"Incorrect option text: Expected '{expected[0]}', got '{option.text}'"
        assert option.get('data-method') == expected[1], f"Incorrect data-method: Expected '{expected[1]}', got '{option.get('data-method')}'"
        assert option.get('data-type') == expected[2], f"Incorrect data-type: Expected '{expected[2]}', got '{option.get('data-type')}'"


def test_context_way_select_options(html_content):
    """Test the options within the context-way select element."""
    soup = BeautifulSoup(html_content, 'html.parser')
    select = soup.find('select', id='context-way')
    assert select is not None, "Context way select not found"

    expected_options = [
        ("xpath ANY_TYPE", "evaluate", "ANY_TYPE"),
        ("xpath UNORDERED_NODE_ITERATOR_TYPE", "evaluate", "UNORDERED_NODE_ITERATOR_TYPE"),
        ("xpath ORDERED_NODE_ITERATOR_TYPE", "evaluate", "ORDERED_NODE_ITERATOR_TYPE"),
        ("xpath UNORDERED_NODE_SNAPSHOT_TYPE", "evaluate", "UNORDERED_NODE_SNAPSHOT_TYPE"),
        ("xpath ORDERED_NODE_SNAPSHOT_TYPE", "evaluate", "ORDERED_NODE_SNAPSHOT_TYPE"),
        ("xpath ANY_UNORDERED_NODE_TYPE", "evaluate", "ANY_UNORDERED_NODE_TYPE"),
        ("xpath FIRST_ORDERED_NODE_TYPE", "evaluate", "FIRST_ORDERED_NODE_TYPE"),
        ("querySelector", "querySelector", ""),
        ("querySelectorAll", "querySelectorAll", ""),
    ]

    options = select.find_all('option')
    assert len(options) == len(expected_options), "Number of context-way select options is incorrect"

    for option, expected in zip(options, expected_options):
       assert option.text == expected[0], f"Incorrect option text: Expected '{expected[0]}', got '{option.text}'"
       assert option.get('data-method') == expected[1], f"Incorrect data-method: Expected '{expected[1]}', got '{option.get('data-method')}'"
       assert option.get('data-type') == expected[2], f"Incorrect data-type: Expected '{expected[2]}', got '{option.get('data-type')}'"


def test_frame_id_list_select_options(html_content):
    """Test the options within the frame-id-list select element."""
    soup = BeautifulSoup(html_content, 'html.parser')
    select = soup.find('select', id='frame-id-list')
    assert select is not None, "Frame ID list select not found"
    
    options = select.find_all('option')
    assert len(options) == 1, "Number of frame-id-list select options is incorrect"
    
    first_option = options[0]
    assert first_option.text == "Manual", f"Incorrect option text: Expected 'Manual', got '{first_option.text}'"
    assert first_option.get('data-frame-id') == "manual", f"Incorrect data-frame-id: Expected 'manual', got '{first_option.get('data-frame-id')}'"


def test_help_switch_element(html_content):
    """Test the presence of the help switch checkbox and label."""
    soup = BeautifulSoup(html_content, 'html.parser')
    help_switch_checkbox = soup.find('input', id='help-switch')
    help_switch_label = soup.find('label', attrs={'for': 'help-switch'})

    assert help_switch_checkbox is not None, "Help switch checkbox not found"
    assert help_switch_checkbox.get('type') == 'checkbox', "Help switch should be a checkbox"
    assert help_switch_label is not None, "Help switch label not found"
    assert help_switch_label.text == 'Help', f"Help switch label text is incorrect: {help_switch_label.text}"


def test_context_switch_element(html_content):
     """Test the presence of the context switch checkbox and label."""
     soup = BeautifulSoup(html_content, 'html.parser')
     context_switch_checkbox = soup.find('input', id='context-switch')
     context_switch_label = soup.find('label', attrs={'for': 'context-switch'})

     assert context_switch_checkbox is not None, "Context switch checkbox not found"
     assert context_switch_checkbox.get('type') == 'checkbox', "Context switch should be a checkbox"
     assert context_switch_label is not None, "Context switch label not found"
     assert context_switch_label.text == 'Context', f"Context switch label text is incorrect: {context_switch_label.text}"

def test_resolver_switch_element(html_content):
     """Test the presence of the resolver switch checkbox and label."""
     soup = BeautifulSoup(html_content, 'html.parser')
     resolver_switch_checkbox = soup.find('input', id='resolver-switch')
     resolver_switch_label = soup.find('label', attrs={'for': 'resolver-switch'})

     assert resolver_switch_checkbox is not None, "resolver switch checkbox not found"
     assert resolver_switch_checkbox.get('type') == 'checkbox', "resolver switch should be a checkbox"
     assert resolver_switch_label is not None, "resolver switch label not found"
     assert resolver_switch_label.text == 'namespaceResolver', f"resolver switch label text is incorrect: {resolver_switch_label.text}"


def test_frame_designation_switch_element(html_content):
    """Test the presence of the frame designation switch checkbox and label."""
    soup = BeautifulSoup(html_content, 'html.parser')
    frame_designation_switch_checkbox = soup.find('input', id='frame-designation-switch')
    frame_designation_switch_label = soup.find('label', attrs={'for': 'frame-designation-switch'})

    assert frame_designation_switch_checkbox is not None, "frame designation switch checkbox not found"
    assert frame_designation_switch_checkbox.get('type') == 'checkbox', "frame designation switch should be a checkbox"
    assert frame_designation_switch_label is not None, "frame designation switch label not found"
    assert frame_designation_switch_label.text == 'Frame without id', f"frame designation switch label text is incorrect: {frame_designation_switch_label.text}"


def test_frame_id_switch_element(html_content):
    """Test the presence of the frame ID switch checkbox and label."""
    soup = BeautifulSoup(html_content, 'html.parser')
    frame_id_switch_checkbox = soup.find('input', id='frame-id-switch')
    frame_id_switch_label = soup.find('label', attrs={'for': 'frame-id-switch'})

    assert frame_id_switch_checkbox is not None, "frame ID switch checkbox not found"
    assert frame_id_switch_checkbox.get('type') == 'checkbox', "frame ID switch should be a checkbox"
    assert frame_id_switch_label is not None, "frame ID switch label not found"
    assert frame_id_switch_label.text == 'frameId', f"frame ID switch label text is incorrect: {frame_id_switch_label.text}"
```