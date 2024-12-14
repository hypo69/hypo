```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Mock the necessary browser API and tryxpath functions
@pytest.fixture(autouse=True)
def mock_browser_api(monkeypatch):
    mock_browser = MagicMock()
    mock_browser.runtime.sendMessage = MagicMock(return_value=MagicMock(then=lambda callback: callback({"message": "Test Message",
        "title":"Test Title", "href":"http://example.com", "frameId": 1,
        "context": {"method":"contextMethod", "expression": "contextExpression", "specifiedResultType": "contextSpecifiedResultType",
                    "resultType": "contextResultType", "resolver": "contextResolver",
                    "itemDetail": {"type":"type", "name": "name", "value": "value", "textContent": "textContent"}},
        "main": {"method":"mainMethod", "expression": "mainExpression", "specifiedResultType": "mainSpecifiedResultType",
                    "resultType": "mainResultType", "resolver": "mainResolver",
                    "itemDetails": [
                        {"type":"type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                        {"type":"type2", "name": "name2", "value": "value2", "textContent": "textContent2"}]
                    },
        "tabId": 2, "executionId": 3 })))
    mock_browser.tabs.sendMessage = MagicMock(return_value=None)
    monkeypatch.setattr("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser", mock_browser)
    
    mock_fu = MagicMock()
    mock_fu.updateDetailsTable = MagicMock(return_value=MagicMock(catch=lambda callback: None))
    mock_fu.onError = MagicMock()
    mock_fu.makeDetailText = MagicMock(side_effect=lambda detail, keys, sep, opts = None: ",".join([str(detail.get(key) if (opts is None or key not in opts) else opts[key](detail.get(key))) for key in keys]))
    monkeypatch.setattr("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.tryxpath.functions", mock_fu)
    
    mock_url = MagicMock()
    mock_url.createObjectURL = MagicMock(return_value="blob://test-url")
    monkeypatch.setattr("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.URL", mock_url)
    
    mock_window = MagicMock()
    mock_document = MagicMock()
    mock_document.getElementById = MagicMock(side_effect = lambda id: MagicMock(textContent = "old text", setAttribute=lambda attr, val: None, 
        getElementsByTagName = lambda tag: [MagicMock()],
        addEventListener = lambda event, callback: None))
    mock_window.document = mock_document
    monkeypatch.setattr("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window", mock_window)
    
    
# Test for showAllResults function
def test_showAllResults_valid_results():
    """Checks if showAllResults function correctly updates the document elements with valid results."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import showAllResults
    
    results = {"message": "Test Message",
        "title":"Test Title", "href":"http://example.com", "frameId": 1,
        "context": {"method":"contextMethod", "expression": "contextExpression", "specifiedResultType": "contextSpecifiedResultType",
                    "resultType": "contextResultType", "resolver": "contextResolver",
                    "itemDetail": {"type":"type", "name": "name", "value": "value", "textContent": "textContent"}},
        "main": {"method":"mainMethod", "expression": "mainExpression", "specifiedResultType": "mainSpecifiedResultType",
                    "resultType": "mainResultType", "resolver": "mainResolver",
                    "itemDetails": [
                        {"type":"type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                        {"type":"type2", "name": "name2", "value": "value2", "textContent": "textContent2"}]
                    }
    }
    
    mock_document = MagicMock()
    mock_document.getElementById = MagicMock(side_effect = lambda id: MagicMock(textContent = "old text", setAttribute=lambda attr, val: None, 
        getElementsByTagName = lambda tag: [MagicMock()],
        addEventListener = lambda event, callback: None))
    
    with patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document", mock_document):
        showAllResults(results)

        mock_document.getElementById.assert_any_call("message")
        mock_document.getElementById.assert_any_call("title")
        mock_document.getElementById.assert_any_call("url")
        mock_document.getElementById.assert_any_call("frame-id")
        
        mock_document.getElementById.assert_any_call("context-method")
        mock_document.getElementById.assert_any_call("context-expression")
        mock_document.getElementById.assert_any_call("context-specified-result-type")
        mock_document.getElementById.assert_any_call("context-result-type")
        mock_document.getElementById.assert_any_call("context-resolver")

        mock_document.getElementById.assert_any_call("main-method")
        mock_document.getElementById.assert_any_call("main-expression")
        mock_document.getElementById.assert_any_call("main-specified-result-type")
        mock_document.getElementById.assert_any_call("main-result-type")
        mock_document.getElementById.assert_any_call("main-resolver")
        mock_document.getElementById.assert_any_call("main-count")
        
        assert mock_document.getElementById("message").textContent == "Test Message"
        assert mock_document.getElementById("title").textContent == "Test Title"
        assert mock_document.getElementById("url").textContent == "http://example.com"
        assert mock_document.getElementById("frame-id").textContent == 1
        
        assert mock_document.getElementById("context-method").textContent == "contextMethod"
        assert mock_document.getElementById("context-expression").textContent == "contextExpression"
        assert mock_document.getElementById("context-specified-result-type").textContent == "contextSpecifiedResultType"
        assert mock_document.getElementById("context-result-type").textContent == "contextResultType"
        assert mock_document.getElementById("context-resolver").textContent == "contextResolver"
        
        assert mock_document.getElementById("main-method").textContent == "mainMethod"
        assert mock_document.getElementById("main-expression").textContent == "mainExpression"
        assert mock_document.getElementById("main-specified-result-type").textContent == "mainSpecifiedResultType"
        assert mock_document.getElementById("main-result-type").textContent == "mainResultType"
        assert mock_document.getElementById("main-resolver").textContent == "mainResolver"
        assert mock_document.getElementById("main-count").textContent == 2

# Test for showAllResults function when context is None
def test_showAllResults_no_context():
    """Checks if showAllResults function correctly handles results with no context."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import showAllResults
    
    results = {"message": "Test Message",
        "title":"Test Title", "href":"http://example.com", "frameId": 1,
        "context": None,
        "main": {"method":"mainMethod", "expression": "mainExpression", "specifiedResultType": "mainSpecifiedResultType",
                    "resultType": "mainResultType", "resolver": "mainResolver",
                    "itemDetails": [
                        {"type":"type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                        {"type":"type2", "name": "name2", "value": "value2", "textContent": "textContent2"}]
                    }
    }
    
    mock_document = MagicMock()
    mock_area = MagicMock()
    mock_area.parentNode = MagicMock()
    mock_document.getElementById = MagicMock(side_effect = lambda id: mock_area if id == "context-area" else MagicMock(textContent = "old text", setAttribute=lambda attr, val: None, 
        getElementsByTagName = lambda tag: [MagicMock()],
        addEventListener = lambda event, callback: None))
    
    with patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document", mock_document):
      showAllResults(results)
      mock_area.parentNode.removeChild.assert_called_once_with(mock_area)
      
      assert mock_document.getElementById("message").textContent == "Test Message"
      assert mock_document.getElementById("title").textContent == "Test Title"
      assert mock_document.getElementById("url").textContent == "http://example.com"
      assert mock_document.getElementById("frame-id").textContent == 1
      
      assert mock_document.getElementById("main-method").textContent == "mainMethod"
      assert mock_document.getElementById("main-expression").textContent == "mainExpression"
      assert mock_document.getElementById("main-specified-result-type").textContent == "mainSpecifiedResultType"
      assert mock_document.getElementById("main-result-type").textContent == "mainResultType"
      assert mock_document.getElementById("main-resolver").textContent == "mainResolver"
      assert mock_document.getElementById("main-count").textContent == 2

def test_makeTextDownloadUrl():
    """Checks if makeTextDownloadUrl function correctly creates a URL for a given text."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import makeTextDownloadUrl
    text = "Test text for download url"
    url = makeTextDownloadUrl(text)
    
    assert url == "blob://test-url"
    hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.URL.createObjectURL.assert_called_once()

def test_makeInfoText():
    """Checks if makeInfoText function correctly formats information from results into a text string."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import makeInfoText
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": 1,
        "context": {
            "method": "contextMethod",
            "expression": "contextExpression",
            "specifiedResultType": "contextSpecifiedResultType",
            "resultType": "contextResultType",
            "resolver": "contextResolver",
            "itemDetail": {"type":"type", "name": "name", "value": "value", "textContent": "textContent"},
        },
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type":"type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                {"type":"type2", "name": "name2", "value": "value2", "textContent": "textContent2"},
            ],
        },
    }
    expected_text = """[Information]
Message:     Test Message
Title:       Test Title
URL:         http://example.com
frameId:     1

[Context information]
Method:                  contextMethod
Expression:              contextExpression
Specified resultType:    contextSpecifiedResultType
resultType:              contextResultType
Resolver:                contextResolver

[Context detail]
Type, Name, Value, textContent
type,name,value,textContent

[Main information]
Method:                  mainMethod
Expression:              mainExpression
Specified resultType:    mainSpecifiedResultType
resultType:              mainResultType
Resolver:                mainResolver
Count:                   2

[Main details]
Index, Type, Name, Value, textContent
0,type1,name1,value1,textContent1
1,type2,name2,value2,textContent2
"""
    actual_text = makeInfoText(results)
    assert actual_text == expected_text


def test_makeInfoText_no_context():
    """Checks if makeInfoText function correctly formats information when context is None."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import makeInfoText
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": 1,
        "context": None,
         "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type":"type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                {"type":"type2", "name": "name2", "value": "value2", "textContent": "textContent2"},
            ],
        },
    }
    expected_text = """[Information]
Message:     Test Message
Title:       Test Title
URL:         http://example.com
frameId:     1

[Main information]
Method:                  mainMethod
Expression:              mainExpression
Specified resultType:    mainSpecifiedResultType
resultType:              mainResultType
Resolver:                mainResolver
Count:                   2

[Main details]
Index, Type, Name, Value, textContent
0,type1,name1,value1,textContent1
1,type2,name2,value2,textContent2
"""
    actual_text = makeInfoText(results)
    assert actual_text == expected_text

def test_makeConvertedInfoText():
    """Checks if makeConvertedInfoText function correctly formats information into a JSON-stringified text string."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import makeConvertedInfoText
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": 1,
        "context": {
            "method": "contextMethod",
            "expression": "contextExpression",
            "specifiedResultType": "contextSpecifiedResultType",
            "resultType": "contextResultType",
            "resolver": "contextResolver",
            "itemDetail": {"type": "type", "name": "name", "value": "value", "textContent": "textContent"},
        },
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                {"type": "type2", "name": "name2", "value": "value2", "textContent": "textContent2"},
            ],
        },
    }
    expected_text = """[Information]
Message:     Test Message
Title:       Test Title
URL:         http://example.com
frameId:     1

[Context information]
Method:                  contextMethod
Expression(JSON):        "contextExpression"
Specified resultType:    contextSpecifiedResultType
resultType:              contextResultType
Resolver:                contextResolver

[Context detail]
Type, Name, Value(JSON), textContent(JSON)
type,name,"value","textContent"

[Main information]
Method:                  mainMethod
Expression(JSON):        "mainExpression"
Specified resultType:    mainSpecifiedResultType
resultType:              mainResultType
Resolver:                mainResolver
Count:                   2

[Main details]
Index, Type, Name, Value(JSON), textContent(JSON)
0,type1,name1,"value1","textContent1"
1,type2,name2,"value2","textContent2"
"""
    actual_text = makeConvertedInfoText(results)
    assert actual_text == expected_text

def test_makeConvertedInfoText_no_context():
    """Checks if makeConvertedInfoText function correctly formats information when context is None."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import makeConvertedInfoText
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": 1,
        "context": None,
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "type1", "name": "name1", "value": "value1", "textContent": "textContent1"},
                {"type": "type2", "name": "name2", "value": "value2", "textContent": "textContent2"},
            ],
        },
    }
    expected_text = """[Information]
Message:     Test Message
Title:       Test Title
URL:         http://example.com
frameId:     1

[Main information]
Method:                  mainMethod
Expression(JSON):        "mainExpression"
Specified resultType:    mainSpecifiedResultType
resultType:              mainResultType
Resolver:                mainResolver
Count:                   2

[Main details]
Index, Type, Name, Value(JSON), textContent(JSON)
0,type1,name1,"value1","textContent1"
1,type2,name2,"value2","textContent2"
"""
    actual_text = makeConvertedInfoText(results)
    assert actual_text == expected_text
    
@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_window_load_event_listener_with_results(mock_browser):
    """Checks if the load event listener correctly calls showAllResults with valid results."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
    
    mock_event = MagicMock()
    
    window.addEventListener("load", mock_event)
    
    mock_event.call_args[0][1]()

    mock_browser.runtime.sendMessage.assert_called_once_with({"event":"loadResults"})
    assert hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document.getElementById("export-text").getAttribute("download") == "tryxpath-Test Title.txt"
    assert hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document.getElementById("export-partly-converted").getAttribute("download") == "tryxpath-converted-Test Title.txt"
    assert hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document.getElementById("export-text").href == "blob://test-url"
    assert hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document.getElementById("export-partly-converted").href == "blob://test-url"
    hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.showAllResults.assert_called_once()

@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_window_load_event_listener_no_results(mock_browser):
    """Checks if the load event listener correctly handles a case when no results returns from message."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
    
    mock_browser.runtime.sendMessage = MagicMock(return_value=MagicMock(then=lambda callback: callback(None)))
    mock_event = MagicMock()
    window.addEventListener("load", mock_event)
    
    mock_event.call_args[0][1]()
    
    mock_browser.runtime.sendMessage.assert_called_once_with({"event":"loadResults"})
    hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.showAllResults.assert_not_called()
    

@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_window_load_event_listener_error(mock_browser):
    """Checks if the load event listener correctly handles a error case."""
    from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
    
    mock_browser.runtime.sendMessage = MagicMock(return_value=MagicMock(then=lambda callback: MagicMock(catch = lambda callback: callback("Error"))))
    mock_event = MagicMock()
    window.addEventListener("load", mock_event)
    
    mock_event.call_args[0][1]()
    
    mock_browser.runtime.sendMessage.assert_called_once_with({"event":"loadResults"})
    hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.tryxpath.functions.onError.assert_called_once_with("Error")
    hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.showAllResults.assert_not_called()


@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_context_detail_click_event(mock_browser):
  """Checks if click event on the context-detail dispatches a focusContextItem event."""
  from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
  mock_event = MagicMock()
  mock_target = MagicMock()
  mock_target.tagName = "button"
  mock_target.toLowerCase = MagicMock(return_value="button")
  mock_event.target = mock_target
  
  mock_document = MagicMock()
  mock_detail = MagicMock()
  mock_detail.addEventListener = MagicMock(side_effect=lambda event, callback: callback(mock_event))
  mock_document.getElementById = MagicMock(return_value = mock_detail)
  
  with patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document", mock_document):
    mock_event = MagicMock()
    
    window.addEventListener("load", MagicMock(side_effect=lambda: None))
    window.document.getElementById("context-detail").addEventListener("click", mock_event)
    
    
    mock_event.call_args[0][1](mock_event)
    
    mock_browser.tabs.sendMessage.assert_called_once_with(2, {
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
            "executionId": 3
      }, {
          "frameId": 1
    })
    
@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_context_detail_click_event_not_button(mock_browser):
  """Checks if click event on the context-detail does not dispatch event when the target is not button."""
  from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
  mock_event = MagicMock()
  mock_target = MagicMock()
  mock_target.tagName = "div"
  mock_target.toLowerCase = MagicMock(return_value="div")
  mock_event.target = mock_target
  
  mock_document = MagicMock()
  mock_detail = MagicMock()
  mock_detail.addEventListener = MagicMock(side_effect=lambda event, callback: callback(mock_event))
  mock_document.getElementById = MagicMock(return_value = mock_detail)
  
  with patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document", mock_document):
    mock_event = MagicMock()
    
    window.addEventListener("load", MagicMock(side_effect=lambda: None))
    window.document.getElementById("context-detail").addEventListener("click", mock_event)
    
    
    mock_event.call_args[0][1](mock_event)
    
    mock_browser.tabs.sendMessage.assert_not_called()
    
@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_main_details_click_event(mock_browser):
  """Checks if click event on the main-details dispatches a focusItem event."""
  from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
  mock_event = MagicMock()
  mock_target = MagicMock()
  mock_target.tagName = "button"
  mock_target.toLowerCase = MagicMock(return_value="button")
  mock_target.getAttribute = MagicMock(return_value="1")
  mock_event.target = mock_target
  
  mock_document = MagicMock()
  mock_detail = MagicMock()
  mock_detail.addEventListener = MagicMock(side_effect=lambda event, callback: callback(mock_event))
  mock_document.getElementById = MagicMock(return_value = mock_detail)
  
  with patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document", mock_document):
    mock_event = MagicMock()
    
    window.addEventListener("load", MagicMock(side_effect=lambda: None))
    window.document.getElementById("main-details").addEventListener("click", mock_event)
    
    
    mock_event.call_args[0][1](mock_event)
    
    mock_browser.tabs.sendMessage.assert_called_once_with(2, {
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
            "executionId": 3,
            "index":1
      }, {
          "frameId": 1
    })

@patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.browser")
def test_main_details_click_event_not_button(mock_browser):
  """Checks if click event on the main-details does not dispatch event when target is not a button."""
  from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results import window
  mock_event = MagicMock()
  mock_target = MagicMock()
  mock_target.tagName = "div"
  mock_target.toLowerCase = MagicMock(return_value="div")
  mock_event.target = mock_target
  
  mock_document = MagicMock()
  mock_detail = MagicMock()
  mock_detail.addEventListener = MagicMock(side_effect=lambda event, callback: callback(mock_event))
  mock_document.getElementById = MagicMock(return_value = mock_detail)
  
  with patch("hypotez.src.webdriver.edge.extentions.try_path_1_3_5.pages.show_all_results.window.document", mock_document):
    mock_event = MagicMock()
    
    window.addEventListener("load", MagicMock(side_effect=lambda: None))
    window.document.getElementById("main-details").addEventListener("click", mock_event)
    
    
    mock_event.call_args[0][1](mock_event)
    
    mock_browser.tabs.sendMessage.assert_not_called()

```