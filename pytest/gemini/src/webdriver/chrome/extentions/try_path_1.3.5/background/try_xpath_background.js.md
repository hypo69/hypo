```python
import pytest
from unittest.mock import MagicMock, patch

# Mock browser API
class MockBrowser:
    def __init__(self):
        self.runtime = MockRuntime()
        self.tabs = MockTabs()
        self.storage = MockStorage()
        self.storage.sync = MockStorageSync()
    
class MockRuntime:
    def __init__(self):
        self.onMessage = MockOnMessage()
        self.sendMessage = MagicMock()
        self.getURL = MagicMock(return_value="/css/try_xpath_insert.css")

class MockTabs:
    def __init__(self):
        self.create = MagicMock()
        self.removeCSS = MagicMock(return_value=Promise(resolve=lambda: None))
        self.insertCSS = MagicMock(return_value=Promise(resolve=lambda: None))
        self.sendMessage = MagicMock(return_value=Promise(resolve=lambda: None))
        
class MockStorage:
    def __init__(self):
        self.onChanged = MockOnChanged()

class MockStorageSync:
     def __init__(self):
        self.get = MagicMock(return_value=Promise(resolve=lambda: None))

class MockOnMessage:
    def __init__(self):
        self.listeners = {}
    def addListener(self, listener):
        self.listener = listener
        
class MockOnChanged:
    def __init__(self):
       self.listeners = []
    def addListener(self, listener):
        self.listeners.append(listener)
        
class Promise:
    def __init__(self, resolve=lambda x: None, reject=lambda x: None):
        self.resolve_callback = resolve
        self.reject_callback = reject
    def then(self, callback):
        self.resolve_callback = callback
        return self
    def catch(self, callback):
        self.reject_callback = callback
        return self
    
    def resolve(self, value):
        return self.resolve_callback(value)
    
    def reject(self, value):
        return self.reject_callback(value)

@pytest.fixture(autouse=True)
def mock_browser_api():
    with patch("__main__.browser", new=MockBrowser()):
         yield
         
@pytest.fixture()
def mock_xml_http_request():
    with patch("__main__.XMLHttpRequest") as MockXHR:
        mock_xhr_instance = MockXHR.return_value
        mock_xhr_instance.readyState = 4
        mock_xhr_instance.responseText = ".test { color: red;}"
        yield mock_xhr_instance
        
@pytest.fixture
def mock_message():
    return {
        "event": "test_event",
        "data": {"key": "value"}
    }

@pytest.fixture
def mock_sender():
     return  MagicMock(tab=MagicMock(id=1), frameId=2)
        

def test_store_popup_state(mock_message):
    """Tests if popup state is correctly stored."""
    browser.runtime.onMessage.listener(
        {
            "event": "storePopupState",
            "state": "test_state"
        },
        mock_sender(),
        None
    )
    assert browser.runtime.onMessage.listeners.listeners["storePopupState"](
        {"event": "storePopupState", "state": "test_state"},
        mock_sender(),
        None
    ) is None
    assert browser.runtime.onMessage.listener.listeners["storePopupState"](
        {"event": "storePopupState", "state": "test_state"},
         mock_sender(),
        None
    ) is None
    assert browser.runtime.onMessage.listener.listeners["storePopupState"](
        {"event": "storePopupState", "state": "test_state"},
         mock_sender(),
        None
    ) is None
    
def test_request_restore_popup_state():
    """Tests if the correct message is sent to restore the popup state."""
    browser.runtime.onMessage.listener(
            {"event": "storePopupState", "state": "test_state"},
            mock_sender(),
            None
        )
    browser.runtime.onMessage.listener(
       {"event": "requestRestorePopupState"},
        mock_sender(),
        None
    )
    
    browser.runtime.onMessage.listener.listeners["requestRestorePopupState"](
        {"event":"requestRestorePopupState"},
        mock_sender(),
        None
    )

    browser.runtime.sendMessage.assert_called_with(
        {
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": "restorePopupState",
            "state": "test_state"
        }
    )
    
def test_request_insert_style_to_popup():
    """Tests if the correct message is sent to insert style to the popup."""
    browser.runtime.onMessage.listener(
        {"event": "requestInsertStyleToPopup"},
        mock_sender(),
        None
    )
    
    browser.runtime.onMessage.listener.listeners["requestInsertStyleToPopup"](
        {"event":"requestInsertStyleToPopup"},
        mock_sender(),
        None
    )

    browser.runtime.sendMessage.assert_called_with(
        {
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": "insertStyleToPopup",
            "css": "body{width:367px;height:auto;}"
        }
    )


def test_show_all_results(mock_sender):
    """Tests if showAllResults function correctly create tab with results"""
    mock_message = {
        "event": "showAllResults",
        "result1": "data1",
        "result2": "data2"
    }
    browser.runtime.onMessage.listener(
        mock_message,
        mock_sender,
        None
    )
    browser.runtime.onMessage.listener.listeners["showAllResults"](
        mock_message,
        mock_sender,
        None
    )

    browser.tabs.create.assert_called_with(
        {"url": "/pages/show_all_results.html"}
    )
    
def test_load_results(mock_sender):
    """Tests if loadResults function correctly return results."""
    results = {"key":"value"}
    browser.runtime.onMessage.listener.listeners["showAllResults"](
        {
            "event": "showAllResults",
            "key": "value"
        },
        mock_sender,
        None
    )
    
    send_response_mock = MagicMock()
    browser.runtime.onMessage.listener(
         {"event":"loadResults"},
        mock_sender,
        send_response_mock
    )
    
    assert browser.runtime.onMessage.listener.listeners["loadResults"](
        {"event": "loadResults"},
        mock_sender,
        send_response_mock
    ) == True
    send_response_mock.assert_called_with(results)

def test_update_css(mock_sender):
    """Tests if updateCss function removes and inserts css correctly."""
    mock_message = {
        "event": "updateCss",
        "expiredCssSet": {
            ".old_class { color: black; }": True
            }
    }
    browser.runtime.onMessage.listener(
        mock_message,
        mock_sender,
        None
    )
    browser.runtime.onMessage.listener.listeners["updateCss"](
        mock_message,
        mock_sender,
        None
    )

    browser.tabs.removeCSS.assert_called_with(1, {
        "code": ".old_class { color: black; }",
        "matchAboutBlank": True,
        "frameId": 2
    })
    browser.tabs.insertCSS.assert_called_with(1, {
            "code":"",
            "cssOrigin": "author",
            "matchAboutBlank": True,
            "frameId": 2
    })
    
def test_load_options(mock_sender):
    """Tests if loadOptions function return options correctly."""
    send_response_mock = MagicMock()
    browser.runtime.onMessage.listener(
         {"event":"loadOptions"},
        mock_sender,
        send_response_mock
    )
    
    assert browser.runtime.onMessage.listener.listeners["loadOptions"](
        {"event": "loadOptions"},
         mock_sender,
        send_response_mock
    ) == True

    send_response_mock.assert_called_with({
        "attributes": {
            "element": "data-tryxpath-element",
            "context": "data-tryxpath-context",
            "focused": "data-tryxpath-focused",
            "focusedAncestor": "data-tryxpath-focused-ancestor",
            "frame": "data-tryxpath-frame",
            "frameAncestor": "data-tryxpath-frame-ancestor"
        },
        "css": "",
        "popupCss": "body{width:367px;height:auto;}"
        })
    
def test_request_set_content_info(mock_sender):
    """Tests if requestSetContentInfo sends content info correctly."""
    browser.runtime.onMessage.listener(
        {"event":"requestSetContentInfo"},
        mock_sender,
        None
    )
    browser.runtime.onMessage.listener.listeners["requestSetContentInfo"](
        {"event":"requestSetContentInfo"},
        mock_sender,
        None
    )
    browser.tabs.sendMessage.assert_called_with(
        1,
        {
           "timeout": 0,
            "timeout_for_event":"presence_of_element_located",
            "event": "setContentInfo",
            "attributes": {
                "element": "data-tryxpath-element",
                "context": "data-tryxpath-context",
                "focused": "data-tryxpath-focused",
                "focusedAncestor": "data-tryxpath-focused-ancestor",
                "frame": "data-tryxpath-frame",
                "frameAncestor": "data-tryxpath-frame-ancestor"
            }
        },
        {"frameId":2}
    )
    
def test_storage_on_changed_attributes():
     """Tests if storage change listener updates attributes correctly."""
     browser.storage.onChanged.listeners[0](
          {"attributes":{
               "newValue": {
                    "element": "new-data-tryxpath-element",
                    "context": "new-data-tryxpath-context",
                    "focused": "new-data-tryxpath-focused",
                    "focusedAncestor": "new-data-tryxpath-focused-ancestor",
                    "frame": "new-data-tryxpath-frame",
                    "frameAncestor": "new-data-tryxpath-frame-ancestor"
                }
           }}
     )
     assert browser.storage.onChanged.listeners[0](
          {"attributes":{
               "newValue": {
                    "element": "new-data-tryxpath-element",
                    "context": "new-data-tryxpath-context",
                    "focused": "new-data-tryxpath-focused",
                    "focusedAncestor": "new-data-tryxpath-focused-ancestor",
                    "frame": "new-data-tryxpath-frame",
                    "frameAncestor": "new-data-tryxpath-frame-ancestor"
                }
           }}
     ) is None
     assert browser.storage.onChanged.listeners[0](
          {"attributes":{
               "newValue": {
                    "element": "new-data-tryxpath-element",
                    "context": "new-data-tryxpath-context",
                    "focused": "new-data-tryxpath-focused",
                    "focusedAncestor": "new-data-tryxpath-focused-ancestor",
                    "frame": "new-data-tryxpath-frame",
                    "frameAncestor": "new-data-tryxpath-frame-ancestor"
                }
           }}
     ) is None
     assert browser.runtime.onMessage.listener.listeners["loadOptions"](
         {"event": "loadOptions"},
         mock_sender(),
          MagicMock()
     )

def test_storage_on_changed_css():
    """Tests if storage change listener updates css correctly."""
    browser.storage.onChanged.listeners[0](
        {"css": { "newValue": ".new_class { color: blue; }" } }
    )
    assert browser.storage.onChanged.listeners[0](
        {"css": { "newValue": ".new_class { color: blue; }" } }
    ) is None
    assert browser.storage.onChanged.listeners[0](
        {"css": { "newValue": ".new_class { color: blue; }" } }
    ) is None
    assert browser.runtime.onMessage.listener.listeners["loadOptions"](
        {"event": "loadOptions"},
        mock_sender(),
         MagicMock()
    )
    
def test_storage_on_changed_popup_css():
     """Tests if storage change listener updates popupCss correctly."""
     browser.storage.onChanged.listeners[0](
          {"popupCss": { "newValue": "body{width:400px;}" } }
     )
     assert browser.storage.onChanged.listeners[0](
        {"popupCss": { "newValue": "body{width:400px;}" } }
    ) is None
     assert browser.storage.onChanged.listeners[0](
          {"popupCss": { "newValue": "body{width:400px;}" } }
    ) is None
     assert browser.runtime.onMessage.listener.listeners["loadOptions"](
        {"event": "loadOptions"},
         mock_sender(),
        MagicMock()
    )

def test_storage_sync_get_with_css(mock_xml_http_request):
    """Tests if storage sync get is done correctly if css is in storage."""
    browser.storage.sync.get.return_value.resolve({
        "attributes": {
             "element": "new-data-tryxpath-element",
            "context": "new-data-tryxpath-context",
            "focused": "new-data-tryxpath-focused",
            "focusedAncestor": "new-data-tryxpath-focused-ancestor",
            "frame": "new-data-tryxpath-frame",
            "frameAncestor": "new-data-tryxpath-frame-ancestor"
        },
        "css": ".storage_class { color: green; }",
        "popupCss":"body{width:400px;}"
        })
    assert browser.storage.sync.get.return_value.resolve({
            "attributes": {
             "element": "new-data-tryxpath-element",
            "context": "new-data-tryxpath-context",
            "focused": "new-data-tryxpath-focused",
            "focusedAncestor": "new-data-tryxpath-focused-ancestor",
            "frame": "new-data-tryxpath-frame",
            "frameAncestor": "new-data-tryxpath-frame-ancestor"
        },
        "css": ".storage_class { color: green; }",
        "popupCss":"body{width:400px;}"
        }) is None
    assert browser.runtime.onMessage.listener.listeners["loadOptions"](
        {"event": "loadOptions"},
         mock_sender(),
        MagicMock()
    )

def test_storage_sync_get_without_css(mock_xml_http_request):
    """Tests if storage sync get is done correctly if css is not in storage."""
    browser.storage.sync.get.return_value.resolve({
        "attributes": {
            "element": "new-data-tryxpath-element",
            "context": "new-data-tryxpath-context",
            "focused": "new-data-tryxpath-focused",
            "focusedAncestor": "new-data-tryxpath-focused-ancestor",
            "frame": "new-data-tryxpath-frame",
            "frameAncestor": "new-data-tryxpath-frame-ancestor"
         },
        "css": None,
        "popupCss":"body{width:400px;}"
        })
    
    mock_xml_http_request.onreadystatechange()
    
    assert browser.storage.sync.get.return_value.resolve({
            "attributes": {
            "element": "new-data-tryxpath-element",
            "context": "new-data-tryxpath-context",
            "focused": "new-data-tryxpath-focused",
            "focusedAncestor": "new-data-tryxpath-focused-ancestor",
            "frame": "new-data-tryxpath-frame",
            "frameAncestor": "new-data-tryxpath-frame-ancestor"
            },
            "css": None,
            "popupCss":"body{width:400px;}"
            }) is None
    
    assert browser.runtime.onMessage.listener.listeners["loadOptions"](
        {"event": "loadOptions"},
         mock_sender(),
        MagicMock()
    )
```