```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Mock the browser API
class MockBrowser:
    def __init__(self):
        self.runtime = MagicMock()
        self.tabs = MagicMock()
        self.runtime.sendMessage = MagicMock(return_value=PromiseMock({"tabId": 1, "frameId": 2, "executionId": 3, "message":"Test Message", "title":"Test Title", "href":"http://example.com",
                "context": {
                    "method": "contextMethod",
                    "expression": "contextExpression",
                    "specifiedResultType": "contextSpecifiedResultType",
                    "resultType": "contextResultType",
                    "resolver": "contextResolver",
                    "itemDetail": {"type": "contextType", "name": "contextName", "value": "contextValue", "textContent": "contextTextContent"}
                },
                "main": {
                    "method": "mainMethod",
                    "expression": "mainExpression",
                    "specifiedResultType": "mainSpecifiedResultType",
                    "resultType": "mainResultType",
                    "resolver": "mainResolver",
                    "itemDetails": [
                        {"type": "mainType1", "name": "mainName1", "value": "mainValue1", "textContent": "mainTextContent1"},
                        {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
                    ]
                }
            }))

class PromiseMock:
    def __init__(self, value):
        self.value = value

    def then(self, callback):
       callback(self.value)
       return self

    def catch(self, error_callback):
        return self


@pytest.fixture
def mock_browser():
    return MockBrowser()

@pytest.fixture
def mock_document():
    class MockElement:
        def __init__(self, tag_name, parent_node=None):
          self.tag_name = tag_name
          self.text_content = None
          self.parent_node = parent_node
          self.attributes = {}
          self.children = []

        def get_elements_by_tag_name(self, tag_name):
          return [child for child in self.children if child.tag_name == tag_name]
        
        def remove_child(self, child):
          if child in self.children:
            self.children.remove(child)

        def set_attribute(self, name, value):
          self.attributes[name] = value

        def get_attribute(self, name):
          return self.attributes.get(name)

        def append_child(self, child):
            self.children.append(child)
            child.parent_node = self

        
    class MockDocument:
        def __init__(self):
            self.body = MockElement("body")
            self.elements = {}

        def get_element_by_id(self, id):
            if id not in self.elements:
                element = MockElement("div")
                self.elements[id] = element
                self.body.append_child(element)
            return self.elements[id]
        
        def create_element(self, tag_name):
            return MockElement(tag_name)
        
        
        def add_event_listener(self, event, callback):
           self.event = event
           self.callback = callback
            
           
    return MockDocument()
  

@pytest.fixture
def mock_window(mock_browser, mock_document):
    class MockWindow:
        def __init__(self, browser, document):
            self.browser = browser
            self.document = document
            self.event_listeners = []

        def add_event_listener(self, event, callback):
           self.event_listeners.append({"event":event, "callback":callback})
           
        def simulate_load_event(self):
           for item in self.event_listeners:
            if item["event"] == "load":
              item["callback"]()

    return MockWindow(mock_browser, mock_document)


def test_showAllResults_updates_elements(mock_window, mock_document):
    """Test that showAllResults correctly updates the text content of various HTML elements."""
    
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": "testFrameId",
        "context": {
            "method": "contextMethod",
            "expression": "contextExpression",
            "specifiedResultType": "contextSpecifiedResultType",
            "resultType": "contextResultType",
            "resolver": "contextResolver",
            "itemDetail": {"type": "contextType", "name": "contextName", "value": "contextValue", "textContent": "contextTextContent"}
        },
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "mainType1", "name": "mainName1", "value": "mainValue1", "textContent": "mainTextContent1"},
                {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
            ]
        }
    }

    # Simulate the 'load' event to trigger the code that calls showAllResults
    mock_window.simulate_load_event()
    
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    showAllResults(results)


    assert mock_document.get_element_by_id("message").text_content == "Test Message"
    assert mock_document.get_element_by_id("title").text_content == "Test Title"
    assert mock_document.get_element_by_id("url").text_content == "http://example.com"
    assert mock_document.get_element_by_id("frame-id").text_content == "testFrameId"
    assert mock_document.get_element_by_id("context-method").text_content == "contextMethod"
    assert mock_document.get_element_by_id("context-expression").text_content == "contextExpression"
    assert mock_document.get_element_by_id("context-specified-result-type").text_content == "contextSpecifiedResultType"
    assert mock_document.get_element_by_id("context-result-type").text_content == "contextResultType"
    assert mock_document.get_element_by_id("context-resolver").text_content == "contextResolver"
    assert mock_document.get_element_by_id("main-method").text_content == "mainMethod"
    assert mock_document.get_element_by_id("main-expression").text_content == "mainExpression"
    assert mock_document.get_element_by_id("main-specified-result-type").text_content == "mainSpecifiedResultType"
    assert mock_document.get_element_by_id("main-result-type").text_content == "mainResultType"
    assert mock_document.get_element_by_id("main-resolver").text_content == "mainResolver"
    assert mock_document.get_element_by_id("main-count").text_content == "2"

def test_showAllResults_no_context(mock_window, mock_document):
    """Test that showAllResults correctly handles the case when 'context' is not provided in results."""
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": "testFrameId",
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "mainType1", "name": "mainName1", "value": "mainValue1", "textContent": "mainTextContent1"},
                {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
            ]
        }
    }
    
    # Simulate the 'load' event to trigger the code that calls showAllResults
    mock_window.simulate_load_event()
    
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    showAllResults(results)
    
    # Verify that the context area is removed
    assert "context-area" not in mock_document.elements
    
def test_makeTextDownloadUrl(mock_window):
    """Test that makeTextDownloadUrl returns a valid URL string."""
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    text = "Test content"
    url = makeTextDownloadUrl(text)
    assert isinstance(url, str)
    assert url.startswith("blob:")
    
def test_makeInfoText_with_context(mock_window):
    """Test that makeInfoText generates the correct text with context information."""
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": "testFrameId",
        "context": {
            "method": "contextMethod",
            "expression": "contextExpression",
            "specifiedResultType": "contextSpecifiedResultType",
            "resultType": "contextResultType",
            "resolver": "contextResolver",
            "itemDetail": {"type": "contextType", "name": "contextName", "value": "contextValue", "textContent": "contextTextContent"}
        },
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "mainType1", "name": "mainName1", "value": "mainValue1", "textContent": "mainTextContent1"},
                {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
            ]
        }
    }
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    text = makeInfoText(results)
    assert "[Context information]" in text
    assert "Method:                  contextMethod" in text
    assert "Expression:              contextExpression" in text
    assert "Specified resultType:    contextSpecifiedResultType" in text
    assert "resultType:              contextResultType" in text
    assert "Resolver:                contextResolver" in text
    assert "Type, Name, Value, textContent" in text
    assert "contextType, contextName, contextValue, contextTextContent" in text
    assert "[Main information]" in text
    assert "Method:                  mainMethod" in text
    assert "Expression:              mainExpression" in text
    assert "Specified resultType:    mainSpecifiedResultType" in text
    assert "resultType:              mainResultType" in text
    assert "Resolver:                mainResolver" in text
    assert "Count:                   2" in text
    assert "[Main details]" in text
    assert "Index, Type, Name, Value, textContent" in text
    assert "0, mainType1, mainName1, mainValue1, mainTextContent1" in text
    assert "1, mainType2, mainName2, mainValue2, mainTextContent2" in text

def test_makeInfoText_no_context(mock_window):
    """Test that makeInfoText generates correct text when no context is provided."""
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": "testFrameId",
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "mainType1", "name": "mainName1", "value": "mainValue1", "textContent": "mainTextContent1"},
                {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
            ]
        }
    }
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    text = makeInfoText(results)
    assert "[Context information]" not in text
    assert "[Main information]" in text
    assert "Method:                  mainMethod" in text
    assert "Expression:              mainExpression" in text
    assert "Specified resultType:    mainSpecifiedResultType" in text
    assert "resultType:              mainResultType" in text
    assert "Resolver:                mainResolver" in text
    assert "Count:                   2" in text
    assert "[Main details]" in text
    assert "Index, Type, Name, Value, textContent" in text
    assert "0, mainType1, mainName1, mainValue1, mainTextContent1" in text
    assert "1, mainType2, mainName2, mainValue2, mainTextContent2" in text

def test_makeConvertedInfoText_with_context(mock_window):
    """Test makeConvertedInfoText with a context."""
    results = {
        "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": "testFrameId",
        "context": {
            "method": "contextMethod",
            "expression": "contextExpression",
            "specifiedResultType": "contextSpecifiedResultType",
            "resultType": "contextResultType",
            "resolver": "contextResolver",
            "itemDetail": {"type": "contextType", "name": "contextName", "value": {"key": "contextValue"}, "textContent": ["contextTextContent"]}
        },
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "mainType1", "name": "mainName1", "value": 123, "textContent": "mainTextContent1"},
                {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
            ]
        }
    }

    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    text = makeConvertedInfoText(results)
    assert "[Context information]" in text
    assert "Expression(JSON):        \"contextExpression\"" in text
    assert 'Value(JSON), textContent(JSON)' in text
    assert '{"key": "contextValue"}, ["contextTextContent"]' in text
    assert "[Main details]" in text
    assert 'Value(JSON), textContent(JSON)' in text
    assert "123, \"mainTextContent1\"" in text

def test_makeConvertedInfoText_no_context(mock_window):
    """Test makeConvertedInfoText without a context."""
    results = {
         "message": "Test Message",
        "title": "Test Title",
        "href": "http://example.com",
        "frameId": "testFrameId",
        "main": {
            "method": "mainMethod",
            "expression": "mainExpression",
            "specifiedResultType": "mainSpecifiedResultType",
            "resultType": "mainResultType",
            "resolver": "mainResolver",
            "itemDetails": [
                {"type": "mainType1", "name": "mainName1", "value": 123, "textContent": "mainTextContent1"},
                {"type": "mainType2", "name": "mainName2", "value": "mainValue2", "textContent": "mainTextContent2"}
            ]
        }
    }

    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    text = makeConvertedInfoText(results)
    assert "[Context information]" not in text
    assert "[Main details]" in text
    assert 'Value(JSON), textContent(JSON)' in text
    assert "123, \"mainTextContent1\"" in text
    

def test_load_event_listener_sets_export_attributes(mock_window, mock_document):
    """Test that the load event listener sets the correct attributes on the export elements."""
    
    # Simulate the 'load' event to trigger the code that sets attributes
    mock_window.simulate_load_event()
    
    # Create mock elements for "export-text" and "export-partly-converted"
    export_text_element = mock_document.get_element_by_id("export-text")
    export_partly_converted_element = mock_document.get_element_by_id("export-partly-converted")
    
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
      script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    # Simulate the load event listener
    mock_window.simulate_load_event()


    # Check that the attributes are correctly set
    assert export_text_element.get_attribute("download") == "tryxpath-Test Title.txt"
    assert export_text_element.get_attribute("href").startswith("blob:")
    assert export_partly_converted_element.get_attribute("download") == "tryxpath-converted-Test Title.txt"
    assert export_partly_converted_element.get_attribute("href").startswith("blob:")

def test_context_detail_click_listener(mock_window, mock_browser, mock_document):
    """Test that clicking on the context details sends a message to the correct tab."""
    # Simulate the 'load' event to trigger the code that sets attributes
    mock_window.simulate_load_event()

    cont_detail_element = mock_document.get_element_by_id("context-detail")
    
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
        script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    
    button = mock_document.create_element("button")
    button.tag_name = "button"
    cont_detail_element.append_child(button)
    
    event = MagicMock()
    event.target = button
    cont_detail_element.callback(event)

    mock_browser.tabs.sendMessage.assert_called_once_with(
        1,
        {"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "focusContextItem", "executionId": 3},
        {"frameId": 2}
    )

def test_main_details_click_listener(mock_window, mock_browser, mock_document):
    """Test that clicking on main details sends a message to the correct tab with the correct index."""
    # Simulate the 'load' event to trigger the code that sets attributes
    mock_window.simulate_load_event()
    main_details_element = mock_document.get_element_by_id("main-details")
    
    # Now, we get the generated script
    with open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/pages/show_all_results.js', 'r') as file:
      script = file.read()
    
    # We use the globals() to execute inside context of the test
    exec(script, globals())
    
    button = mock_document.create_element("button")
    button.tag_name = "button"
    button.set_attribute("data-index", "1")

    main_details_element.append_child(button)
    
    event = MagicMock()
    event.target = button
    main_details_element.callback(event)

    mock_browser.tabs.sendMessage.assert_called_once_with(
        1,
        {"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "focusItem", "executionId": 3, "index": 1},
        {"frameId": 2}
    )
```