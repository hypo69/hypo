```python
import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

# Mock the browser API
class MockBrowser:
    def __init__(self):
        self.runtime = MockRuntime()
        self.tabs = MockTabs()
        self.storage = MockStorage()
        self.storage.sync = MockSyncStorage()

class MockRuntime:
    def __init__(self):
        self.onMessage = MockOnMessage()

    def getURL(self, path):
        return f"mocked_url/{path}"

class MockOnMessage:
    def __init__(self):
        self.listeners = {}

    def addListener(self, callback):
        self.listener = callback

class MockTabs:
    def __init__(self):
        self.tab_id_counter = 0
    def create(self, url):
        self.tab_id_counter += 1
        return  {"id": self.tab_id_counter,"url":url}

    def removeCSS(self, id, config):
       #  print(f'Remove CSS for tab id : {id} with config {config}')
        return PromiseMock()

    def insertCSS(self, id, config):
        #print(f'Insert CSS for tab id : {id} with config {config}')
        return PromiseMock()

    def sendMessage(self, id, message, config):
        return PromiseMock()


class MockStorage:
     def __init__(self):
         self.onChanged = MockOnChanged()
         self.sync = MockSyncStorage()

class MockOnChanged:
    def __init__(self):
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

class MockSyncStorage:
    def get(self, keys):
        return PromiseMock(
            {
                "attributes": {"element": "data-tryxpath-element",
                               "context": "data-tryxpath-context",
                               "focused": "data-tryxpath-focused",
                               "focusedAncestor": "data-tryxpath-focused-ancestor",
                               "frame": "data-tryxpath-frame",
                               "frameAncestor": "data-tryxpath-frame-ancestor"},
                "css": "mocked css",
                "popupCss": "body{width:367px;height:auto;}"
            })

class PromiseMock:
    def __init__(self, resolve_value=None):
        self.resolve_value = resolve_value
    def then(self, callback):
        if self.resolve_value:
            callback(self.resolve_value)
        return self
    def catch(self, callback):
        return self
    def get_callback_value(self):
         return self.resolve_value


# Mock XMLHttpRequest
class MockXMLHttpRequest:
    def __init__(self):
        self.readyState = 0
        self.responseText = None
        self.onreadystatechange = None
        self.responseType = None
    def open(self, method, url):
        self.url = url
    def send(self):
        self.readyState = 4
        self.responseText = "mocked css from file"
        if self.onreadystatechange:
             self.onreadystatechange()


# Fixture definitions
@pytest.fixture
def mock_window():
    window = MagicMock()
    window.tryxpath = MagicMock()
    window.tryxpath.functions = MagicMock()
    window.XMLHttpRequest = MockXMLHttpRequest
    window.browser = MockBrowser()
    return window

@pytest.fixture
def background_script(mock_window):
    # Execute the background script within the mocked window
    exec(open("hypotez/src/webdriver/edge/extentions/try_path_1.3.5/background/try_xpath_background.js", "r").read(),
         mock_window.__dict__)
    return mock_window


# Tests
def test_load_default_css(background_script):
    """Test if the default css file is loaded and saved in css var"""
    window = background_script
    assert window.browser.runtime.getURL("/css/try_xpath_insert.css") == "mocked_url//css/try_xpath_insert.css"
    assert window.css == "mocked css from file"

def test_store_popup_state(background_script):
    """Test storing popup state."""
    window = background_script
    message = {"event": "storePopupState", "state": {"key": "value"}}
    window.browser.runtime.onMessage.listener(message)
    assert window.popupState == {"key": "value"}

def test_request_restore_popup_state(background_script):
    """Test sending message to restore popup state."""
    window = background_script
    window.popupState = {"key": "value"}
    message = {"event": "requestRestorePopupState"}
    window.browser.runtime.onMessage.listener(message)
    assert  window.browser.runtime.onMessage.listener
    sent_message = window.browser.runtime.onMessage.listener.call_args.args[0]
    assert sent_message["event"] == "restorePopupState"
    assert sent_message["state"] == {"key": "value"}


def test_request_insert_style_to_popup(background_script):
    """Test sending message to insert style to popup."""
    window = background_script
    message = {"event": "requestInsertStyleToPopup"}
    window.browser.runtime.onMessage.listener(message)
    sent_message = window.browser.runtime.onMessage.listener.call_args.args[0]
    assert sent_message["event"] == "insertStyleToPopup"
    assert sent_message["css"] == "body{width:367px;height:auto;}"


def test_show_all_results(background_script):
    """Test showing all results."""
    window = background_script
    sender = {"tab": {"id": 1}, "frameId": 2}
    message = {"event": "showAllResults", "result": "test"}
    window.browser.runtime.onMessage.listener(message, sender)
    assert window.results == {"result": "test", "tabId": 1, "frameId": 2}
    assert window.browser.tabs.create.call_count == 1
    assert window.browser.tabs.create.call_args.args[0]["url"] == "/pages/show_all_results.html"

def test_load_results(background_script):
    """Test loading results."""
    window = background_script
    window.results = {"test": "value"}
    send_response = MagicMock()
    message = {"event": "loadResults"}
    result = window.browser.runtime.onMessage.listener(message, None, send_response)
    assert result == True
    send_response.assert_called_with({"test": "value"})

def test_update_css(background_script):
    """Test updating CSS."""
    window = background_script
    sender = {"tab": {"id": 1}, "frameId": 2}
    message = {"event": "updateCss", "expiredCssSet": ["expired"], }
    window.css = "new css"
    window.browser.runtime.onMessage.listener(message, sender)
    assert window.browser.tabs.removeCSS.call_count == 1
    assert window.browser.tabs.removeCSS.call_args.args[0] == 1
    assert  window.browser.tabs.removeCSS.call_args.args[1]["code"] == "expired"
    assert window.browser.tabs.insertCSS.call_count == 1
    assert window.browser.tabs.insertCSS.call_args.args[0] == 1
    assert window.browser.tabs.insertCSS.call_args.args[1]["code"] == "new css"


def test_load_options(background_script):
    """Test loading options."""
    window = background_script
    send_response = MagicMock()
    window.css = "test_css"
    window.popupCss = "test_popupCss"
    message = {"event": "loadOptions"}
    result = window.browser.runtime.onMessage.listener(message, None, send_response)
    assert result == True
    send_response.assert_called_with({
        "attributes": {"element": "data-tryxpath-element",
                       "context": "data-tryxpath-context",
                       "focused": "data-tryxpath-focused",
                       "focusedAncestor": "data-tryxpath-focused-ancestor",
                       "frame": "data-tryxpath-frame",
                       "frameAncestor": "data-tryxpath-frame-ancestor"},
        "css": "test_css",
        "popupCss": "test_popupCss"
    })

def test_request_set_content_info(background_script):
    """Test sending message to set content info."""
    window = background_script
    sender = {"tab": {"id": 1}, "frameId": 2}
    message = {"event": "requestSetContentInfo"}
    window.browser.runtime.onMessage.listener(message, sender)

    sent_message = window.browser.tabs.sendMessage.call_args.args[1]
    assert sent_message["event"] == "setContentInfo"
    assert sent_message["attributes"] == {"element": "data-tryxpath-element",
                       "context": "data-tryxpath-context",
                       "focused": "data-tryxpath-focused",
                       "focusedAncestor": "data-tryxpath-focused-ancestor",
                       "frame": "data-tryxpath-frame",
                       "frameAncestor": "data-tryxpath-frame-ancestor"}
    assert window.browser.tabs.sendMessage.call_args.args[2]["frameId"] == 2

def test_storage_on_changed_attributes(background_script):
    """Test storage on changed with attributes."""
    window = background_script
    changes = {"attributes": {"newValue": {"new_attr": "value"}}}
    window.browser.storage.onChanged.listeners[0](changes)
    assert window.attributes == {"new_attr": "value"}

def test_storage_on_changed_css(background_script):
    """Test storage on changed with css."""
    window = background_script
    changes = {"css": {"newValue": "new_css"}}
    window.browser.storage.onChanged.listeners[0](changes)
    assert window.css == "new_css"

def test_storage_on_changed_popup_css(background_script):
    """Test storage on changed with popup css."""
    window = background_script
    changes = {"popupCss": {"newValue": "new_popup_css"}}
    window.browser.storage.onChanged.listeners[0](changes)
    assert window.popupCss == "new_popup_css"

def test_storage_sync_get_with_initial_css(background_script):
     """Test storage sync get when initial css is presented"""
     window = background_script
     assert window.css == "mocked css"
def test_storage_sync_get_without_initial_css(background_script):
     """Test storage sync get when initial css is not presented, check load default css"""
     window = background_script
     window.browser.storage.sync.get = MagicMock(return_value=PromiseMock({"attributes": {"element": "data-tryxpath-element",
                               "context": "data-tryxpath-context",
                               "focused": "data-tryxpath-focused",
                               "focusedAncestor": "data-tryxpath-focused-ancestor",
                               "frame": "data-tryxpath-frame",
                               "frameAncestor": "data-tryxpath-frame-ancestor"},
                               "css": None,
                "popupCss": "body{width:367px;height:auto;}"}))
     exec(open("hypotez/src/webdriver/edge/extentions/try_path_1.3.5/background/try_xpath_background.js", "r").read(),
         window.__dict__)
     assert window.css == "mocked css from file"
```