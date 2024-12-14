```python
import pytest
from unittest.mock import MagicMock, patch

# Mock the browser and window objects
@pytest.fixture
def mock_browser():
    mock = MagicMock()
    mock.runtime.sendMessage = MagicMock(return_value=PromiseMock({"tabId": 1, "frameId": 2, "executionId": "test-id", "title":"test title", "message":"test message", "href":"http://test.url",
                                                                  "context": { "method": "test method", "expression":"test expression", "specifiedResultType":"test type", "resultType":"test result type", "resolver":"test resolver",
                                                                            "itemDetail": {"type": "test type", "name": "test name", "value": "test value", "textContent":"test text content"} },
                                                                  "main": { "method": "test method", "expression":"test expression", "specifiedResultType":"test type", "resultType":"test result type", "resolver":"test resolver",
                                                                          "itemDetails": [{"type": "test type", "name": "test name", "value": "test value", "textContent":"test text content"}] }}))
    mock.tabs.sendMessage = MagicMock()
    return mock

@pytest.fixture
def mock_document():
    mock = MagicMock()
    mock.getElementById = MagicMock(side_effect=lambda id: MagicMock(textContent="", parentNode=MagicMock(removeChild=MagicMock()),
                                                                    getElementsByTagName=MagicMock(return_value=[MagicMock(innerHTML="")])))
    mock.createElement = MagicMock(return_value=MagicMock())
    return mock

@pytest.fixture
def mock_url():
  mock = MagicMock()
  mock.createObjectURL = MagicMock(return_value="test-url")
  return mock

@pytest.fixture
def mock_tryxpath():
    mock = MagicMock()
    mock.functions.updateDetailsTable = MagicMock(return_value=PromiseMock(None))
    mock.functions.onError = MagicMock()
    mock.functions.makeDetailText = MagicMock(side_effect=lambda detail, keys, sep, formatters=None: ", ".join(str(detail.get(key)) for key in keys))
    return mock


class PromiseMock:
    def __init__(self, value=None):
        self.value = value

    def then(self, callback):
        if self.value is not None:
            callback(self.value)
        return self

    def catch(self, callback):
       return self

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_showAllResults_with_context(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test showAllResults function with context data."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture
    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    show_all_results.showAllResults(mock_browser_fixture.runtime.sendMessage.return_value.value)

    # Verify that the text content of the correct elements has been updated.
    mock_document_fixture.getElementById.assert_any_call("message")
    mock_document_fixture.getElementById.return_value.textContent =="test message"
    mock_document_fixture.getElementById.assert_any_call("title")
    mock_document_fixture.getElementById.return_value.textContent =="test title"
    mock_document_fixture.getElementById.assert_any_call("url")
    mock_document_fixture.getElementById.return_value.textContent =="http://test.url"
    mock_document_fixture.getElementById.assert_any_call("frame-id")
    mock_document_fixture.getElementById.return_value.textContent =="2"

    mock_document_fixture.getElementById.assert_any_call("context-method")
    mock_document_fixture.getElementById.return_value.textContent =="test method"
    mock_document_fixture.getElementById.assert_any_call("context-expression")
    mock_document_fixture.getElementById.return_value.textContent =="test expression"
    mock_document_fixture.getElementById.assert_any_call("context-specified-result-type")
    mock_document_fixture.getElementById.return_value.textContent =="test type"
    mock_document_fixture.getElementById.assert_any_call("context-result-type")
    mock_document_fixture.getElementById.return_value.textContent =="test result type"
    mock_document_fixture.getElementById.assert_any_call("context-resolver")
    mock_document_fixture.getElementById.return_value.textContent =="test resolver"
    mock_document_fixture.getElementById.assert_any_call("context-detail")
    mock_tryxpath_fixture.functions.updateDetailsTable.assert_called()

    mock_document_fixture.getElementById.assert_any_call("main-method")
    mock_document_fixture.getElementById.return_value.textContent =="test method"
    mock_document_fixture.getElementById.assert_any_call("main-expression")
    mock_document_fixture.getElementById.return_value.textContent =="test expression"
    mock_document_fixture.getElementById.assert_any_call("main-specified-result-type")
    mock_document_fixture.getElementById.return_value.textContent =="test type"
    mock_document_fixture.getElementById.assert_any_call("main-result-type")
    mock_document_fixture.getElementById.return_value.textContent =="test result type"
    mock_document_fixture.getElementById.assert_any_call("main-resolver")
    mock_document_fixture.getElementById.return_value.textContent =="test resolver"
    mock_document_fixture.getElementById.assert_any_call("main-count")
    mock_document_fixture.getElementById.return_value.textContent =="1"
    mock_document_fixture.getElementById.assert_any_call("main-details")
    mock_tryxpath_fixture.functions.updateDetailsTable.assert_called()


@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_showAllResults_without_context(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test showAllResults function without context data."""
    mock_window.document = mock_document_fixture
    mock_browser_fixture.runtime.sendMessage = MagicMock(return_value=PromiseMock({"tabId": 1, "frameId": 2, "executionId": "test-id", "title":"test title", "message":"test message", "href":"http://test.url",
                                                                  "main": { "method": "test method", "expression":"test expression", "specifiedResultType":"test type", "resultType":"test result type", "resolver":"test resolver",
                                                                          "itemDetails": [{"type": "test type", "name": "test name", "value": "test value", "textContent":"test text content"}] }}))
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture
    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    show_all_results.showAllResults(mock_browser_fixture.runtime.sendMessage.return_value.value)

    # Verify that the context area is removed when no context is available
    mock_document_fixture.getElementById.assert_any_call("context-area")
    mock_document_fixture.getElementById.return_value.parentNode.removeChild.assert_called()

    # Verify that main results are still processed
    mock_document_fixture.getElementById.assert_any_call("main-method")
    mock_document_fixture.getElementById.return_value.textContent =="test method"
    mock_document_fixture.getElementById.assert_any_call("main-expression")
    mock_document_fixture.getElementById.return_value.textContent =="test expression"
    mock_document_fixture.getElementById.assert_any_call("main-specified-result-type")
    mock_document_fixture.getElementById.return_value.textContent =="test type"
    mock_document_fixture.getElementById.assert_any_call("main-result-type")
    mock_document_fixture.getElementById.return_value.textContent =="test result type"
    mock_document_fixture.getElementById.assert_any_call("main-resolver")
    mock_document_fixture.getElementById.return_value.textContent =="test resolver"
    mock_document_fixture.getElementById.assert_any_call("main-count")
    mock_document_fixture.getElementById.return_value.textContent =="1"
    mock_document_fixture.getElementById.assert_any_call("main-details")
    mock_tryxpath_fixture.functions.updateDetailsTable.assert_called()


@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_makeTextDownloadUrl(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test makeTextDownloadUrl function."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    text = "test text"
    url = show_all_results.makeTextDownloadUrl(text)
    mock_url_fixture.createObjectURL.assert_called()
    assert url == "test-url"

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_makeInfoText_with_context(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test makeInfoText function with context data."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    results = mock_browser_fixture.runtime.sendMessage.return_value.value
    text = show_all_results.makeInfoText(results)
    assert "[Information]" in text
    assert "[Context information]" in text
    assert "[Context detail]" in text
    assert "[Main information]" in text
    assert "[Main details]" in text
    mock_tryxpath_fixture.functions.makeDetailText.assert_called()

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_makeInfoText_without_context(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test makeInfoText function without context data."""
    mock_window.document = mock_document_fixture
    mock_browser_fixture.runtime.sendMessage = MagicMock(return_value=PromiseMock({"tabId": 1, "frameId": 2, "executionId": "test-id", "title":"test title", "message":"test message", "href":"http://test.url",
                                                                  "main": { "method": "test method", "expression":"test expression", "specifiedResultType":"test type", "resultType":"test result type", "resolver":"test resolver",
                                                                          "itemDetails": [{"type": "test type", "name": "test name", "value": "test value", "textContent":"test text content"}] }}))
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    results = mock_browser_fixture.runtime.sendMessage.return_value.value
    text = show_all_results.makeInfoText(results)
    assert "[Information]" in text
    assert "[Context information]" not in text
    assert "[Context detail]" not in text
    assert "[Main information]" in text
    assert "[Main details]" in text
    mock_tryxpath_fixture.functions.makeDetailText.assert_called()

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_makeConvertedInfoText_with_context(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test makeConvertedInfoText function with context data."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    results = mock_browser_fixture.runtime.sendMessage.return_value.value
    text = show_all_results.makeConvertedInfoText(results)
    assert "[Information]" in text
    assert "[Context information]" in text
    assert "[Context detail]" in text
    assert "[Main information]" in text
    assert "[Main details]" in text
    mock_tryxpath_fixture.functions.makeDetailText.assert_called()

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_makeConvertedInfoText_without_context(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test makeConvertedInfoText function without context data."""
    mock_window.document = mock_document_fixture
    mock_browser_fixture.runtime.sendMessage = MagicMock(return_value=PromiseMock({"tabId": 1, "frameId": 2, "executionId": "test-id", "title":"test title", "message":"test message", "href":"http://test.url",
                                                                  "main": { "method": "test method", "expression":"test expression", "specifiedResultType":"test type", "resultType":"test result type", "resolver":"test resolver",
                                                                          "itemDetails": [{"type": "test type", "name": "test name", "value": "test value", "textContent":"test text content"}] }}))
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture
    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    results = mock_browser_fixture.runtime.sendMessage.return_value.value
    text = show_all_results.makeConvertedInfoText(results)
    assert "[Information]" in text
    assert "[Context information]" not in text
    assert "[Context detail]" not in text
    assert "[Main information]" in text
    assert "[Main details]" in text
    mock_tryxpath_fixture.functions.makeDetailText.assert_called()

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_window_load_event(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test the window load event listener."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    # Trigger the 'load' event
    load_callback = mock_window.addEventListener.call_args[0][1]
    load_callback()
    # Verify that sendMessage was called with the correct arguments
    mock_browser_fixture.runtime.sendMessage.assert_called_with({"event":"loadResults"})
    # Verify that the export links were created
    mock_document_fixture.getElementById.assert_any_call("export-text")
    mock_document_fixture.getElementById.assert_any_call("export-partly-converted")

    # Verify that showAllResults was called with results
    mock_tryxpath_fixture.functions.updateDetailsTable.assert_called()

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_context_detail_click_event(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test the context detail click event listener."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    # Trigger the 'load' event
    load_callback = mock_window.addEventListener.call_args[0][1]
    load_callback()
    # Get the context detail click event listener
    contDetail_callback = mock_document_fixture.getElementById.return_value.addEventListener.call_args[0][1]
    mock_target = MagicMock(tagName="button")
    mock_event = MagicMock(target=mock_target)
    contDetail_callback(mock_event)
    mock_browser_fixture.tabs.sendMessage.assert_called_with(1, {"timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem","executionId": "test-id"}, {"frameId": 2})

    mock_target = MagicMock(tagName="DIV")
    mock_event = MagicMock(target=mock_target)
    contDetail_callback(mock_event)
    mock_browser_fixture.tabs.sendMessage.assert_called_once()

@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.window')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.browser')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.document')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.URL')
@patch('hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages.show_all_results.tryxpath', new_callable=lambda: MagicMock())
def test_main_details_click_event(mock_tryxpath, mock_url, mock_document, mock_browser, mock_window, mock_browser_fixture, mock_document_fixture, mock_url_fixture, mock_tryxpath_fixture):
    """Test the main details click event listener."""
    mock_window.document = mock_document_fixture
    mock_browser.return_value = mock_browser_fixture
    mock_url.return_value = mock_url_fixture
    mock_tryxpath.return_value = mock_tryxpath_fixture

    from hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.pages import show_all_results
    # Trigger the 'load' event
    load_callback = mock_window.addEventListener.call_args[0][1]
    load_callback()
    # Get the main detail click event listener
    mainDetails_callback = mock_document_fixture.getElementById.return_value.addEventListener.call_args[0][1]
    mock_target = MagicMock(tagName="button", getAttribute=MagicMock(return_value="0"))
    mock_event = MagicMock(target=mock_target)
    mainDetails_callback(mock_event)
    mock_browser_fixture.tabs.sendMessage.assert_called_with(1, {"timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem","executionId": "test-id","index":0}, {"frameId": 2})

    mock_target = MagicMock(tagName="DIV", getAttribute=MagicMock(return_value="0"))
    mock_event = MagicMock(target=mock_target)
    mainDetails_callback(mock_event)
    mock_browser_fixture.tabs.sendMessage.assert_called_once()
```