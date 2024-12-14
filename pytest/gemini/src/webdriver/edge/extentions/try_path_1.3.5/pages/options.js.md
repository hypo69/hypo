```python
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
import json

# Assuming the javascript code is saved as options.js
# Read the javascript file content
file_path = Path(__file__).parent / "options.js"
js_code = file_path.read_text()

# Mock browser object and its methods
@pytest.fixture
def mock_browser():
    mock = MagicMock()
    mock.runtime.getURL.return_value = "/css/try_xpath_insert.css"
    mock.runtime.sendMessage.return_value = MagicMock(
        then=lambda callback: callback({
            "attributes": {
                "element": "data-tryxpath-element-test",
                "context": "data-tryxpath-context-test",
                "focused": "data-tryxpath-focused-test",
                "focusedAncestor": "data-tryxpath-focused-ancestor-test",
                "frame": "data-tryxpath-frame-test",
                "frameAncestor": "data-tryxpath-frame-ancestor-test"
            },
            "css": "body { color: red; }",
            "popupCss": "body{width:367px;height:auto;}"
        })
    )
    mock.storage.sync.set.return_value = MagicMock(
        then = lambda callback: callback()
    )
    return mock


@pytest.fixture
def mock_document():
    mock = MagicMock()
    mock.getElementById.side_effect = lambda id: MagicMock(value=f"test-{id}")
    mock.createElement.return_value = MagicMock()
    mock.addEventListener.return_value = None
    return mock

@pytest.fixture
def mock_xml_http_request():
    mock = MagicMock()
    mock_instance = MagicMock()
    mock.return_value = mock_instance
    mock_instance.readyState = 4
    mock_instance.responseText = "body{width:100px;height:200px;}"
    mock_instance.send.return_value = None
    return mock, mock_instance


def execute_js(js_code, mock_browser, mock_document, mock_xml_http_request):
    """Executes the javascript code in a mocked environment."""
    global browser, document, XMLHttpRequest
    browser = mock_browser
    document = mock_document
    XMLHttpRequest = mock_xml_http_request[0]
    
    # Execute the javascript code
    exec(js_code)

    # Simulate the "load" event listener
    for args, _ in document.addEventListener.call_args_list:
      if args[0] == 'load':
        args[1]()

# Tests for isValidAttrName
def test_isValidAttrName_valid(mock_document):
    """Checks if a valid attribute name returns True."""
    execute_js(js_code, MagicMock(), mock_document, MagicMock())
    assert isValidAttrName("data-test") == True
    
def test_isValidAttrName_invalid(mock_document):
    """Checks if an invalid attribute name returns False."""
    mock_document.createElement.return_value.setAttribute.side_effect = Exception("Invalid")
    execute_js(js_code, MagicMock(), mock_document, MagicMock())
    assert isValidAttrName("invalid-attr") == False

# Tests for isValidAttrNames
def test_isValidAttrNames_valid(mock_document):
    """Checks if a set of valid attribute names returns True."""
    execute_js(js_code, MagicMock(), mock_document, MagicMock())
    assert isValidAttrNames({"attr1": "data-test1", "attr2": "data-test2"}) == True

def test_isValidAttrNames_invalid(mock_document):
    """Checks if a set with an invalid attribute name returns False."""
    mock_document.createElement.return_value.setAttribute.side_effect = Exception("Invalid")
    execute_js(js_code, MagicMock(), mock_document, MagicMock())
    assert isValidAttrNames({"attr1": "data-test1", "attr2": "invalid-attr"}) == False

def test_isValidAttrNames_empty(mock_document):
    """Checks if an empty set returns True."""
    execute_js(js_code, MagicMock(), mock_document, MagicMock())
    assert isValidAttrNames({}) == True

# Tests for isValidStyleLength
def test_isValidStyleLength_valid_auto():
    """Checks if 'auto' is a valid style length."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    assert isValidStyleLength("auto") == True

def test_isValidStyleLength_valid_px():
    """Checks if a valid 'px' value is a valid style length."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    assert isValidStyleLength("100px") == True
    assert isValidStyleLength("1px") == True
    assert isValidStyleLength("999px") == True

def test_isValidStyleLength_invalid():
    """Checks if an invalid value is not a valid style length."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    assert isValidStyleLength("100") == False
    assert isValidStyleLength("100p") == False
    assert isValidStyleLength("0px") == False
    assert isValidStyleLength("-1px") == False

# Tests for loadDefaultCss
@patch('__main__.XMLHttpRequest')
def test_loadDefaultCss(mock_xml_http_request, mock_browser):
    """Checks if loadDefaultCss returns a Promise"""
    mock, mock_instance = mock_xml_http_request
    mock_instance.readyState = 4
    mock_instance.responseText = "test css"
    execute_js(js_code, mock_browser, MagicMock(), (mock, mock_instance))
    promise = loadDefaultCss()
    assert isinstance(promise, type(MagicMock()))

# Tests for extractBodyStyles
def test_extractBodyStyles_valid():
    """Checks extraction of valid body styles."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    css = "body { width: 100px; height: 200px; }"
    styles = extractBodyStyles(css)
    assert styles["width"] == " 100px"
    assert styles["height"] == " 200px"

def test_extractBodyStyles_missing_width():
    """Checks extraction when width is missing."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    css = "body { height: 200px; }"
    styles = extractBodyStyles(css)
    assert styles["width"] == ""
    assert styles["height"] == ""

def test_extractBodyStyles_missing_height():
    """Checks extraction when height is missing."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    css = "body { width: 100px; }"
    styles = extractBodyStyles(css)
    assert styles["width"] == ""
    assert styles["height"] == ""


def test_extractBodyStyles_empty():
    """Checks extraction with empty CSS."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    css = ""
    styles = extractBodyStyles(css)
    assert styles["width"] == ""
    assert styles["height"] == ""
    
def test_extractBodyStyles_no_match():
    """Checks extraction with css not containing width and height"""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    css = "body { color:red; }"
    styles = extractBodyStyles(css)
    assert styles["width"] == ""
    assert styles["height"] == ""

# Tests for createPopupCss
def test_createPopupCss():
    """Checks creation of CSS with body styles."""
    execute_js(js_code, MagicMock(), MagicMock(), MagicMock())
    bodyStyles = {"width": "100px", "height": "200px"}
    css = createPopupCss(bodyStyles)
    assert css == "body{width:100px;height:200px;}"

# Tests for window.onload event
def test_window_onload_initialization(mock_browser, mock_document, mock_xml_http_request):
    """Checks if initial values are set correctly on window load."""
    execute_js(js_code, mock_browser, mock_document, mock_xml_http_request)
    
    mock_document.getElementById.assert_any_call("element-attribute")
    mock_document.getElementById.assert_any_call("context-attribute")
    mock_document.getElementById.assert_any_call("focused-attribute")
    mock_document.getElementById.assert_any_call("ancestor-attribute")
    mock_document.getElementById.assert_any_call("frame-attribute")
    mock_document.getElementById.assert_any_call("frame-ancestor-attribute")
    mock_document.getElementById.assert_any_call("style")
    mock_document.getElementById.assert_any_call("popup-body-width")
    mock_document.getElementById.assert_any_call("popup-body-height")
    mock_document.getElementById.assert_any_call("message")

    assert mock_document.getElementById("element-attribute").value == "data-tryxpath-element-test"
    assert mock_document.getElementById("context-attribute").value == "data-tryxpath-context-test"
    assert mock_document.getElementById("focused-attribute").value == "data-tryxpath-focused-test"
    assert mock_document.getElementById("ancestor-attribute").value == "data-tryxpath-focused-ancestor-test"
    assert mock_document.getElementById("frame-attribute").value == "data-tryxpath-frame-test"
    assert mock_document.getElementById("frame-ancestor-attribute").value == "data-tryxpath-frame-ancestor-test"
    assert mock_document.getElementById("style").value == "body { color: red; }"
    assert mock_document.getElementById("popup-body-width").value == "367px"
    assert mock_document.getElementById("popup-body-height").value == "auto"
    
def test_save_button_click_valid(mock_browser, mock_document, mock_xml_http_request):
    """Checks the save button functionality with valid input"""
    execute_js(js_code, mock_browser, mock_document, mock_xml_http_request)
    
    #Find save button and call event listener
    for args, _ in mock_document.addEventListener.call_args_list:
        if args[0] == 'click' and hasattr(args[1], '__name__') and args[1].__name__ == "<lambda>":
            args[1]()
            break
    
    mock_browser.storage.sync.set.assert_called_once()
    message_element = mock_document.getElementById("message")
    assert message_element.textContent.startswith("Success")
    
def test_save_button_click_invalid_attr(mock_browser, mock_document, mock_xml_http_request):
    """Checks the save button functionality with invalid attribute input"""
    mock_document.getElementById.side_effect = lambda id: MagicMock(value=f"invalid-{id}")
    mock_document.createElement.return_value.setAttribute.side_effect = Exception("Invalid")
    execute_js(js_code, mock_browser, mock_document, mock_xml_http_request)
    
    #Find save button and call event listener
    for args, _ in mock_document.addEventListener.call_args_list:
        if args[0] == 'click' and hasattr(args[1], '__name__') and args[1].__name__ == "<lambda>":
            args[1]()
            break
    
    mock_browser.storage.sync.set.assert_not_called()
    message_element = mock_document.getElementById("message")
    assert message_element.textContent == "There is a invalid attribute."

def test_save_button_click_invalid_style(mock_browser, mock_document, mock_xml_http_request):
    """Checks the save button functionality with invalid style input"""
    mock_document.getElementById.side_effect = lambda id: MagicMock(value="100")
    execute_js(js_code, mock_browser, mock_document, mock_xml_http_request)
    
    #Find save button and call event listener
    for args, _ in mock_document.addEventListener.call_args_list:
        if args[0] == 'click' and hasattr(args[1], '__name__') and args[1].__name__ == "<lambda>":
            args[1]()
            break
    
    mock_browser.storage.sync.set.assert_not_called()
    message_element = mock_document.getElementById("message")
    assert message_element.textContent == "There is a invalid style."
    
def test_save_button_click_storage_error(mock_browser, mock_document, mock_xml_http_request):
    """Checks the save button functionality with storage error"""
    mock_browser.storage.sync.set.return_value = MagicMock(
        then = lambda callback: MagicMock(catch= lambda error_callback: error_callback(Exception("test error")))
    )
    execute_js(js_code, mock_browser, mock_document, mock_xml_http_request)
    
    #Find save button and call event listener
    for args, _ in mock_document.addEventListener.call_args_list:
        if args[0] == 'click' and hasattr(args[1], '__name__') and args[1].__name__ == "<lambda>":
            args[1]()
            break
    
    message_element = mock_document.getElementById("message")
    assert message_element.textContent == "Failure. test error"

def test_show_default_button_click(mock_browser, mock_document, mock_xml_http_request):
    """Checks show default button functionality."""
    execute_js(js_code, mock_browser, mock_document, mock_xml_http_request)
    
    #Find show default button and call event listener
    for args, _ in mock_document.addEventListener.call_args_list:
        if args[0] == 'click' and hasattr(args[1], '__name__') and args[1].__name__ != "<lambda>":
            args[1]()
            break

    assert mock_document.getElementById("element-attribute").value == "data-tryxpath-element"
    assert mock_document.getElementById("context-attribute").value == "data-tryxpath-context"
    assert mock_document.getElementById("focused-attribute").value == "data-tryxpath-focused"
    assert mock_document.getElementById("ancestor-attribute").value == "data-tryxpath-focused-ancestor"
    assert mock_document.getElementById("frame-attribute").value == "data-tryxpath-frame"
    assert mock_document.getElementById("frame-ancestor-attribute").value == "data-tryxpath-frame-ancestor"
    assert mock_document.getElementById("popup-body-width").value == "367px"
    assert mock_document.getElementById("popup-body-height").value == "auto"
    assert mock_document.getElementById("style").value == "body{width:100px;height:200px;}"
```