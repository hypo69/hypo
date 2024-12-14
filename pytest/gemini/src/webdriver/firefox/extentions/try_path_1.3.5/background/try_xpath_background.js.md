```python
import pytest
from unittest.mock import MagicMock, patch

# Mock the browser API
class MockBrowser:
    def __init__(self):
        self.runtime = MockRuntime()
        self.tabs = MockTabs()
        self.storage = MockStorage()
    
class MockRuntime:
    def __init__(self):
        self.onMessage = MockOnMessage()
        self.getURL = MagicMock(return_value="/css/try_xpath_insert.css")
        self.sendMessage = MagicMock()
    
class MockOnMessage:
    def __init__(self):
        self.listeners = {}
    
    def addListener(self, listener):
      self.listeners = listener
    
    def dispatch(self, message, sender, sendResponse):
        return self.listeners(message, sender, sendResponse)
    
class MockTabs:
    def __init__(self):
        self.create = MagicMock()
        self.removeCSS = MagicMock(return_value=Promise())
        self.insertCSS = MagicMock(return_value=Promise())
        self.sendMessage = MagicMock(return_value=Promise())
    
class MockStorage:
    def __init__(self):
        self.onChanged = MockOnChanged()
        self.sync = MockSync()
        
class MockOnChanged:
    def __init__(self):
        self.listeners = []
    
    def addListener(self, listener):
        self.listeners.append(listener)
    
    def dispatch(self, changes):
      for listener in self.listeners:
        listener(changes)

class MockSync:
  def __init__(self):
        self.get = MagicMock(return_value=Promise())

class Promise:
    def __init__(self, value=None):
        self.value = value
        self.then_callbacks = []
        self.catch_callbacks = []

    def then(self, callback):
        if self.value:
            self.value = callback(self.value)
        else:
            self.then_callbacks.append(callback)
        return self

    def catch(self, callback):
        self.catch_callbacks.append(callback)
        return self
        
    def resolve(self, value):
      self.value = value
      for callback in self.then_callbacks:
        self.value = callback(self.value)
      self.then_callbacks = []

    def reject(self, error):
        for callback in self.catch_callbacks:
            callback(error)
        self.catch_callbacks = []

def mock_xmlhttprequest(response_text):
  class MockXMLHttpRequest:
      DONE = 4

      def __init__(self):
          self.readyState = 0
          self.responseType = None
          self.onreadystatechange = None
          self.responseText = response_text

      def open(self, method, url):
          self.readyState = 1

      def send(self):
          self.readyState = 4
          if self.onreadystatechange:
              self.onreadystatechange()
  return MockXMLHttpRequest

@pytest.fixture
def mock_browser_api():
    mock_browser = MockBrowser()
    with patch.dict("sys.modules", {"browser": mock_browser}):
        yield mock_browser
    
@pytest.fixture
def mock_tryxpath_functions():
  return MagicMock()

@pytest.fixture
def setup_background_script(mock_browser_api, mock_tryxpath_functions):
  """Sets up the background script and returns the genericListener function."""
  
  # Set up mocks
  window = MagicMock()
  
  # Import the code with mocked browser
  with patch.dict("sys.modules", {"browser": mock_browser_api}):
      from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
      
  # Get the genericListener function from the module
  return try_xpath_background.genericListener, window
    

def test_loadDefaultCss(mock_browser_api, mock_tryxpath_functions):
    """Checks if loadDefaultCss correctly loads CSS from a file."""
    
    mock_xml = mock_xmlhttprequest("body{color: red;}")
    with patch("hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background.try_xpath_background.XMLHttpRequest", new=mock_xml):
        from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background.try_xpath_background import loadDefaultCss
        promise = loadDefaultCss()
        promise.then(lambda css: assert css == "body{color: red;}")
    

def test_storePopupState(setup_background_script):
    """Checks if storePopupState correctly stores the popup state."""
    genericListener, _ = setup_background_script
    message = {"event": "storePopupState", "state": {"key": "value"}}
    genericListener(message, None, None)
    
    # Check if the state is correctly stored
    from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
    assert try_xpath_background.popupState == {"key": "value"}


def test_requestRestorePopupState(setup_background_script, mock_browser_api):
  """Checks if requestRestorePopupState sends the stored popup state."""
  genericListener, _ = setup_background_script
  from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
  try_xpath_background.popupState = {"key": "value"}
  message = {"event": "requestRestorePopupState"}
  genericListener(message, None, None)
  
  mock_browser_api.runtime.sendMessage.assert_called_once_with(
    {"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "restorePopupState", "state": {"key": "value"}}
  )


def test_requestInsertStyleToPopup(setup_background_script, mock_browser_api):
  """Checks if requestInsertStyleToPopup sends the popup CSS."""
  genericListener, _ = setup_background_script
  message = {"event": "requestInsertStyleToPopup"}
  genericListener(message, None, None)
  
  mock_browser_api.runtime.sendMessage.assert_called_once_with({
      "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "insertStyleToPopup", "css": "body{width:367px;height:auto;}"
  })


def test_showAllResults(setup_background_script, mock_browser_api):
    """Checks if showAllResults correctly handles results and opens a new tab."""
    genericListener, _ = setup_background_script
    message = {"event": "showAllResults", "result": "test"}
    sender = {"tab": {"id": 123}, "frameId": 0}
    genericListener(message, sender, None)
    
    # Check if the results are stored correctly
    from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
    assert try_xpath_background.results == {"result": "test", "tabId": 123, "frameId": 0}
    
    # Check if a new tab is created
    mock_browser_api.tabs.create.assert_called_once_with({"url": "/pages/show_all_results.html"})


def test_loadResults(setup_background_script):
  """Checks if loadResults sends the stored results."""
  genericListener, _ = setup_background_script
  from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
  try_xpath_background.results = {"key": "value"}
  
  sendResponse_mock = MagicMock()
  message = {"event": "loadResults"}
  genericListener(message, None, sendResponse_mock)

  sendResponse_mock.assert_called_once_with({"key": "value"})


def test_updateCss(setup_background_script, mock_browser_api, mock_tryxpath_functions):
    """Checks if updateCss correctly removes and inserts CSS."""
    genericListener, _ = setup_background_script
    mock_browser_api.tabs.removeCSS.return_value.then = MagicMock(return_value=mock_browser_api.tabs.removeCSS.return_value)
    mock_browser_api.tabs.removeCSS.return_value.catch = MagicMock(return_value=mock_browser_api.tabs.removeCSS.return_value)
    mock_browser_api.tabs.insertCSS.return_value.then = MagicMock(return_value=mock_browser_api.tabs.insertCSS.return_value)
    mock_browser_api.tabs.insertCSS.return_value.catch = MagicMock(return_value=mock_browser_api.tabs.insertCSS.return_value)
    
    from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
    try_xpath_background.css = ".new-class { color: blue; }"
    
    message = {
        "event": "updateCss",
        "expiredCssSet": [".old-class { color: red; }"]
    }
    sender = {"tab": {"id": 123}, "frameId": 0}
    genericListener(message, sender, None)
    
    # Check if removeCSS and insertCSS are called
    mock_browser_api.tabs.removeCSS.assert_called_once_with(123, {
        "code": ".old-class { color: red; }",
        "matchAboutBlank": True,
        "frameId": 0
    })
    mock_browser_api.tabs.insertCSS.assert_called_once_with(123, {
        "code": ".new-class { color: blue; }",
        "cssOrigin": "author",
        "matchAboutBlank": True,
        "frameId": 0
    })
    mock_browser_api.tabs.sendMessage.assert_any_call(123, {
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "finishRemoveCss", "css": ".old-class { color: red; }"
    }, {"frameId": 0})
    mock_browser_api.tabs.sendMessage.assert_called_with(123, {
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "finishInsertCss", "css": ".new-class { color: blue; }"
    }, {"frameId": 0})


def test_loadOptions(setup_background_script):
    """Checks if loadOptions returns the correct options."""
    genericListener, _ = setup_background_script
    sendResponse_mock = MagicMock()
    from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
    try_xpath_background.attributes = {"element": "data-test-element"}
    try_xpath_background.css = ".test-class { color: green; }"
    try_xpath_background.popupCss = "body{background-color: grey;}"
    message = {"event": "loadOptions"}
    genericListener(message, None, sendResponse_mock)

    sendResponse_mock.assert_called_once_with({
        "attributes": {"element": "data-test-element"},
        "css": ".test-class { color: green; }",
        "popupCss": "body{background-color: grey;}"
    })


def test_requestSetContentInfo(setup_background_script, mock_browser_api):
    """Checks if requestSetContentInfo sends the attributes to the content script."""
    genericListener, _ = setup_background_script
    
    from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
    try_xpath_background.attributes = {"element": "data-test-element"}
    
    sender = {"tab": {"id": 123}, "frameId": 0}
    message = {"event": "requestSetContentInfo"}
    genericListener(message, sender, None)

    mock_browser_api.tabs.sendMessage.assert_called_once_with(123, {
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "setContentInfo",
        "attributes": {"element": "data-test-element"}
    }, {"frameId": 0})


def test_storage_onChanged_listener(setup_background_script, mock_browser_api):
  """Tests that storage.onChanged correctly updates the module variables"""
  _, _ = setup_background_script
  from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
  
  mock_browser_api.storage.onChanged.dispatch({"attributes": {"newValue": {"element": "new-attribute"}}})
  assert try_xpath_background.attributes == {"element": "new-attribute"}
  
  mock_browser_api.storage.onChanged.dispatch({"css": {"newValue": ".new-css{color:red;}"}})
  assert try_xpath_background.css == ".new-css{color:red;}"
  
  mock_browser_api.storage.onChanged.dispatch({"popupCss": {"newValue": "body{backgroung:blue;}"}})
  assert try_xpath_background.popupCss == "body{backgroung:blue;}"
  
def test_storage_sync_get_and_load_default_css(setup_background_script, mock_browser_api, mock_tryxpath_functions):
    """Tests that storage.sync.get loads default CSS if css is null, and handles other values"""
    _, _ = setup_background_script
    mock_xml = mock_xmlhttprequest("body{color:red;}")
    with patch("hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background.try_xpath_background.XMLHttpRequest", new=mock_xml):
        mock_browser_api.storage.sync.get.return_value.then = MagicMock(side_effect=lambda callback: callback({"attributes": {"element": "data-test-element"}, "css": None, "popupCss": "body{width:100px;}"}))
        from hypotez.src.webdriver.firefox.extentions.try_path_1_3_5.background import try_xpath_background
        assert try_xpath_background.css == "body{color:red;}"
        assert try_xpath_background.attributes == {"element": "data-test-element"}
        assert try_xpath_background.popupCss == "body{width:100px;}"
        mock_browser_api.storage.sync.get.return_value.then = MagicMock(side_effect=lambda callback: callback({"attributes": {"element": "data-test-element-2"}, "css": ".custom-css{color:black;}", "popupCss": "body{width:200px;}"}))
        assert try_xpath_background.css == ".custom-css{color:black;}"
        assert try_xpath_background.attributes == {"element": "data-test-element-2"}
        assert try_xpath_background.popupCss == "body{width:200px;}"
```