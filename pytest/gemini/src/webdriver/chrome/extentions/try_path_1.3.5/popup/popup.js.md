```python
import pytest
from unittest.mock import MagicMock, patch
import json


# Mock browser API
class MockBrowser:
    def __init__(self):
        self.tabs = MockTabs()
        self.runtime = MockRuntime()

class MockTabs:
    def __init__(self):
        self.tab_id = 1
        self.frame_id = 0
        self.messages = []
        self.scripts = []
        self.active_tab_id = 1

    def query(self, query_info):
        if query_info.get("active") and query_info.get("currentWindow"):
          return Promise.resolve([{"id": self.active_tab_id}])
        return Promise.resolve([])

    def sendMessage(self, tab_id, message, options=None):
      self.messages.append((tab_id, message, options))
      return Promise.resolve()

    def executeScript(self, script_info):
      self.scripts.append(script_info)
      if script_info.get("frameId") == 1000:
        return Promise.resolve([False])
      return Promise.resolve([True])

class MockRuntime:
    def __init__(self):
        self.listeners = {}
        self.messages = []
        self.options_opened = False

    def onMessage(self):
        return self

    def addListener(self, listener):
        self.listeners['onMessage'] = listener

    def sendMessage(self, message):
        self.messages.append(message)

    def openOptionsPage(self):
      self.options_opened = True


class Promise:
    def __init__(self, value=None):
      self.value = value
      self.then_callback = None
      self.catch_callback = None
      self.is_resolved = False

    def then(self, callback):
        if not self.is_resolved:
          self.then_callback = callback
          return self
        else:
          if self.value:
            result = callback(self.value)
            return Promise(result)
          return self

    def catch(self, callback):
        if not self.is_resolved:
          self.catch_callback = callback
          return self
        else:
          return self

    @staticmethod
    def resolve(value):
      promise = Promise(value)
      promise.is_resolved = True
      if promise.then_callback:
        result = promise.then_callback(value)
        return Promise(result)
      return promise

    def __repr__(self):
      return f"<Promise resolved={self.is_resolved}, value={self.value}>"
    

# Mock window object and document
class MockElement:
    def __init__(self, tag_name, id=None, class_name=None):
      self.tag_name = tag_name
      self.id = id
      self.classList = MockClassList()
      self.value = ""
      self.selectedOptions = [MockElement("option")]
      self.children = []
      self.textContent = ""
      self.attributes = {}
      if class_name:
        self.classList.add(class_name)

    def getAttribute(self, name):
      return self.attributes.get(name)

    def setAttribute(self, name, value):
      self.attributes[name] = value
    
    def appendChild(self, child):
      self.children.append(child)

    def getElementsByTagName(self, tag_name):
      return [child for child in self.children if child.tag_name == tag_name]
    
    def getElementsByClassName(self, class_name):
        return [child for child in self.children if class_name in child.classList.classes]

    
    def __repr__(self):
      return f"<MockElement tag_name={self.tag_name} id={self.id} class_names={self.classList.classes}>"
    
class MockClassList:
  def __init__(self):
    self.classes = []

  def add(self, class_name):
    if class_name not in self.classes:
      self.classes.append(class_name)

  def remove(self, class_name):
    if class_name in self.classes:
      self.classes.remove(class_name)

  def contains(self, class_name):
    return class_name in self.classes

class MockDocument:
    def __init__(self):
        self.head = MockElement("head")
        self.body = MockElement("body")

    def createElement(self, tag_name):
        return MockElement(tag_name)
    
    def getElementById(self, id):
        elements =  self.body.children + self.head.children
        for element in elements:
          if element.id == id:
            return element
        return None

    def getElementsByClassName(self, class_name):
      all_elements = self.body.children + self.head.children
      result = []
      for element in all_elements:
         if class_name in element.classList.classes:
              result.append(element)
      return result
    
    def __repr__(self):
      return f"<MockDocument>"

class MockWindow:
    def __init__(self):
        self.document = MockDocument()
        self.scrollY = 0
        self.scrollX = 0
    
    def addEventListener(self, event_name, callback):
        pass  # For simplicity, we ignore event listeners
    
    def scrollTo(self, x, y):
        self.scrollX = x
        self.scrollY = y


# Create mock instances
mock_browser = MockBrowser()
mock_window = MockWindow()
mock_document = mock_window.document

# Set up global mocks
def setup_module(module):
  module.browser = mock_browser
  module.window = mock_window
  module.document = mock_document


def create_popup_elements():
  mock_document.body.appendChild(MockElement("div", id="help-body"))
  mock_document.body.appendChild(MockElement("input", id="help-switch", tag_name="input"))
  mock_document.body.appendChild(MockElement("select", id="main-way"))
  mock_document.body.appendChild(MockElement("textarea", id="main-expression", tag_name="textarea"))
  mock_document.body.appendChild(MockElement("div", id="context-header"))
  mock_document.body.appendChild(MockElement("input", id="context-switch", tag_name="input"))
  mock_document.body.appendChild(MockElement("div", id="context-body", class_name="none"))
  mock_document.body.appendChild(MockElement("select", id="context-way"))
  mock_document.body.appendChild(MockElement("textarea", id="context-expression", tag_name="textarea"))
  mock_document.body.appendChild(MockElement("div", id="resolver-header"))
  mock_document.body.appendChild(MockElement("input", id="resolver-switch", tag_name="input"))
  mock_document.body.appendChild(MockElement("div", id="resolver-body", class_name="none"))
  mock_document.body.appendChild(MockElement("textarea", id="resolver-expression", tag_name="textarea"))
  mock_document.body.appendChild(MockElement("div", id="frame-designation-header"))
  mock_document.body.appendChild(MockElement("input", id="frame-designation-switch", tag_name="input"))
  mock_document.body.appendChild(MockElement("div", id="frame-designation-body", class_name="none"))
  mock_document.body.appendChild(MockElement("textarea", id="frame-designation-expression", tag_name="textarea"))
  mock_document.body.appendChild(MockElement("div", id="frame-id-header"))
  mock_document.body.appendChild(MockElement("input", id="frame-id-switch", tag_name="input"))
  mock_document.body.appendChild(MockElement("div", id="frame-id-body", class_name="none"))
  mock_document.body.appendChild(MockElement("select", id="frame-id-list"))
  mock_document.body.appendChild(MockElement("textarea", id="frame-id-expression", tag_name="textarea"))
  mock_document.body.appendChild(MockElement("div", id="results-message"))
  mock_document.body.appendChild(MockElement("div", id="results-count"))
  mock_document.body.appendChild(MockElement("div", id="results-frame-id"))
  mock_document.body.appendChild(MockElement("table", id="results-details").appendChild(MockElement("tbody")))
  mock_document.body.appendChild(MockElement("table", id="context-detail").appendChild(MockElement("tbody")))
  mock_document.body.appendChild(MockElement("input", id="details-page-count", tag_name="input"))
  mock_document.body.appendChild(MockElement("button", id="execute"))
  mock_document.body.appendChild(MockElement("button", id="focus-designated-frame"))
  mock_document.body.appendChild(MockElement("button", id="get-all-frame-id"))
  mock_document.body.appendChild(MockElement("button", id="show-previous-results"))
  mock_document.body.appendChild(MockElement("button", id="focus-frame"))
  mock_document.body.appendChild(MockElement("button", id="show-all-results"))
  mock_document.body.appendChild(MockElement("button", id="open-options"))
  mock_document.body.appendChild(MockElement("button", id="set-style"))
  mock_document.body.appendChild(MockElement("button", id="reset-style"))
  mock_document.body.appendChild(MockElement("button", id="set-all-style"))
  mock_document.body.appendChild(MockElement("button", id="reset-all-style"))
  mock_document.body.appendChild(MockElement("button", id="previous-details-page"))
  mock_document.body.appendChild(MockElement("button", id="move-details-page"))
  mock_document.body.appendChild(MockElement("button", id="next-details-page"))


@pytest.fixture(scope="function")
def popup_elements():
    create_popup_elements()
    yield
    mock_document.body.children = []
    mock_document.head.children = []
    mock_browser.tabs.messages = []
    mock_browser.tabs.scripts = []
    mock_browser.runtime.messages = []
    mock_browser.runtime.options_opened = False

@pytest.fixture
def tryxpath():
    with patch.dict('sys.modules', tryxpath=MagicMock()):
        import hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.popup.popup as popup
        yield popup

def test_sendToActiveTab(tryxpath, popup_elements):
    """Test sending a message to the active tab."""
    msg = {"event": "test_event"}
    tryxpath.sendToActiveTab(msg)
    assert len(mock_browser.tabs.messages) == 1
    tab_id, sent_msg, _ = mock_browser.tabs.messages[0]
    assert tab_id == 1
    assert sent_msg == msg

def test_sendToSpecifiedFrame_default_frame(tryxpath, popup_elements):
    """Test sending a message to the specified frame (default frameId 0)."""
    msg = {"event": "test_event"}
    tryxpath.sendToSpecifiedFrame(msg)
    assert len(mock_browser.tabs.scripts) == 2
    assert len(mock_browser.tabs.messages) == 2
    assert mock_browser.tabs.scripts[0]["frameId"] == 0
    assert mock_browser.tabs.scripts[1]["frameId"] == 0
    assert mock_browser.tabs.messages[1][2]["frameId"] == 0
    assert mock_browser.tabs.messages[1][1] == msg

def test_sendToSpecifiedFrame_with_frame_id(tryxpath, popup_elements):
    """Test sending a message to the specified frame with a specific frameId."""
    frame_id_list = mock_document.getElementById("frame-id-list")
    opt = MockElement("option")
    opt.setAttribute("data-frame-id", "5")
    frame_id_list.appendChild(opt)
    frame_id_list.selectedOptions = [opt]
    mock_document.getElementById("frame-id-switch").checked = True
    msg = {"event": "test_event"}
    tryxpath.sendToSpecifiedFrame(msg)
    assert len(mock_browser.tabs.scripts) == 2
    assert len(mock_browser.tabs.messages) == 2
    assert mock_browser.tabs.scripts[0]["frameId"] == 5
    assert mock_browser.tabs.scripts[1]["frameId"] == 5
    assert mock_browser.tabs.messages[1][2]["frameId"] == 5
    assert mock_browser.tabs.messages[1][1] == msg

def test_sendToSpecifiedFrame_with_manual_frame_id(tryxpath, popup_elements):
    """Test sending a message to the specified frame with manual frameId."""
    frame_id_list = mock_document.getElementById("frame-id-list")
    opt = MockElement("option")
    opt.setAttribute("data-frame-id", "manual")
    frame_id_list.appendChild(opt)
    frame_id_list.selectedOptions = [opt]
    mock_document.getElementById("frame-id-switch").checked = True
    mock_document.getElementById("frame-id-expression").value = "123"
    msg = {"event": "test_event"}
    tryxpath.sendToSpecifiedFrame(msg)
    assert len(mock_browser.tabs.scripts) == 2
    assert len(mock_browser.tabs.messages) == 2
    assert mock_browser.tabs.scripts[0]["frameId"] == 123
    assert mock_browser.tabs.scripts[1]["frameId"] == 123
    assert mock_browser.tabs.messages[1][2]["frameId"] == 123
    assert mock_browser.tabs.messages[1][1] == msg
    

def test_sendToSpecifiedFrame_error_handling(tryxpath, popup_elements):
    """Test error handling when executeScript fails (simulating incorrect frameId)."""
    frame_id_list = mock_document.getElementById("frame-id-list")
    opt = MockElement("option")
    opt.setAttribute("data-frame-id", "1000")
    frame_id_list.appendChild(opt)
    frame_id_list.selectedOptions = [opt]
    mock_document.getElementById("frame-id-switch").checked = True
    msg = {"event": "test_event"}
    tryxpath.sendToSpecifiedFrame(msg)
    assert len(mock_browser.tabs.scripts) == 2
    assert mock_document.getElementById("results-message").textContent == "An error occurred. The frameId may be incorrect."
    assert mock_document.getElementById("results-frame-id").textContent == "1000"

def test_collectPopupState(tryxpath, popup_elements):
    """Test collecting the state of the popup."""
    help_checkbox = mock_document.getElementById("help-switch")
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    context_checkbox = mock_document.getElementById("context-switch")
    context_way = mock_document.getElementById("context-way")
    context_expression = mock_document.getElementById("context-expression")
    resolver_checkbox = mock_document.getElementById("resolver-switch")
    resolver_expression = mock_document.getElementById("resolver-expression")
    frame_designation_checkbox = mock_document.getElementById("frame-designation-switch")
    frame_designation_expression = mock_document.getElementById("frame-designation-expression")
    frame_id_checkbox = mock_document.getElementById("frame-id-switch")
    frame_id_list = mock_document.getElementById("frame-id-list")
    frame_id_expression = mock_document.getElementById("frame-id-expression")

    help_checkbox.checked = True
    main_way.selectedIndex = 1
    main_expression.value = "main_xpath"
    context_checkbox.checked = True
    context_way.selectedIndex = 2
    context_expression.value = "context_xpath"
    resolver_checkbox.checked = True
    resolver_expression.value = "resolver_xpath"
    frame_designation_checkbox.checked = True
    frame_designation_expression.value = "frame_designation"
    frame_id_checkbox.checked = True
    opt = MockElement("option")
    opt.setAttribute("data-frame-id", "5")
    frame_id_list.appendChild(opt)
    frame_id_list.selectedOptions = [opt]
    frame_id_expression.value = "123"
    tryxpath.detailsPageIndex = 3


    state = tryxpath.collectPopupState()
    assert state["helpCheckboxChecked"] is True
    assert state["mainWayIndex"] == 1
    assert state["mainExpressionValue"] == "main_xpath"
    assert state["contextCheckboxChecked"] is True
    assert state["contextWayIndex"] == 2
    assert state["contextExpressionValue"] == "context_xpath"
    assert state["resolverCheckboxChecked"] is True
    assert state["resolverExpressionValue"] == "resolver_xpath"
    assert state["frameDesignationCheckboxChecked"] is True
    assert state["frameDesignationExpressionValue"] == "frame_designation"
    assert state["frameIdCheckboxChecked"] is True
    assert state["specifiedFrameId"] == 5
    assert state["detailsPageIndex"] == 3

def test_changeContextVisible(tryxpath, popup_elements):
    """Test toggling visibility of the context section."""
    context_body = mock_document.getElementById("context-body")
    context_checkbox = mock_document.getElementById("context-switch")
    context_checkbox.checked = True
    tryxpath.changeContextVisible()
    assert "none" not in context_body.classList.classes
    context_checkbox.checked = False
    tryxpath.changeContextVisible()
    assert "none" in context_body.classList.classes


def test_changeResolverVisible(tryxpath, popup_elements):
    """Test toggling visibility of the resolver section."""
    resolver_body = mock_document.getElementById("resolver-body")
    resolver_checkbox = mock_document.getElementById("resolver-switch")
    resolver_checkbox.checked = True
    tryxpath.changeResolverVisible()
    assert "none" not in resolver_body.classList.classes
    resolver_checkbox.checked = False
    tryxpath.changeResolverVisible()
    assert "none" in resolver_body.classList.classes


def test_changeFrameIdVisible(tryxpath, popup_elements):
    """Test toggling visibility of the frame id section."""
    frame_id_body = mock_document.getElementById("frame-id-body")
    frame_id_checkbox = mock_document.getElementById("frame-id-switch")
    frame_id_checkbox.checked = True
    tryxpath.changeFrameIdVisible()
    assert "none" not in frame_id_body.classList.classes
    frame_id_checkbox.checked = False
    tryxpath.changeFrameIdVisible()
    assert "none" in frame_id_body.classList.classes


def test_changeFrameDesignationVisible(tryxpath, popup_elements):
    """Test toggling visibility of the frame designation section."""
    frame_designation_body = mock_document.getElementById("frame-designation-body")
    frame_designation_checkbox = mock_document.getElementById("frame-designation-switch")
    frame_designation_checkbox.checked = True
    tryxpath.changeFrameDesignationVisible()
    assert "none" not in frame_designation_body.classList.classes
    frame_designation_checkbox.checked = False
    tryxpath.changeFrameDesignationVisible()
    assert "none" in frame_designation_body.classList.classes


def test_changeHelpVisible(tryxpath, popup_elements):
    """Test toggling visibility of help elements."""
    help_element1 = MockElement("div", class_name="help")
    help_element2 = MockElement("div", class_name="help")
    mock_document.body.appendChild(help_element1)
    mock_document.body.appendChild(help_element2)
    help_checkbox = mock_document.getElementById("help-switch")
    help_checkbox.checked = True
    tryxpath.changeHelpVisible()
    assert "none" not in help_element1.classList.classes
    assert "none" not in help_element2.classList.classes
    help_checkbox.checked = False
    tryxpath.changeHelpVisible()
    assert "none" in help_element1.classList.classes
    assert "none" in help_element2.classList.classes

def test_makeExecuteMessage_main_only(tryxpath, popup_elements):
    """Test creating an execute message with only main expression."""
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    opt = MockElement("option")
    opt.setAttribute("data-method", "xpath")
    opt.setAttribute("data-type", "node")
    main_way.appendChild(opt)
    main_way.selectedOptions = [opt]
    main_expression.value = "//div"
    
    msg = tryxpath.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "//div"
    assert msg["main"]["method"] == "xpath"
    assert msg["main"]["resultType"] == "node"
    assert msg["main"]["resolver"] is None
    assert "context" not in msg
    assert "frameDesignation" not in msg
    
def test_makeExecuteMessage_with_context(tryxpath, popup_elements):
    """Test creating an execute message with context expression."""
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    context_checkbox = mock_document.getElementById("context-switch")
    context_way = mock_document.getElementById("context-way")
    context_expression = mock_document.getElementById("context-expression")
    opt = MockElement("option")
    opt.setAttribute("data-method", "xpath")
    opt.setAttribute("data-type", "node")
    main_way.appendChild(opt)
    main_way.selectedOptions = [opt]
    main_expression.value = "//div"
    context_checkbox.checked = True
    opt2 = MockElement("option")
    opt2.setAttribute("data-method", "css")
    opt2.setAttribute("data-type", "string")
    context_way.appendChild(opt2)
    context_way.selectedOptions = [opt2]
    context_expression.value = ".class"
    
    msg = tryxpath.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "//div"
    assert msg["main"]["method"] == "xpath"
    assert msg["main"]["resultType"] == "node"
    assert msg["main"]["resolver"] is None
    assert msg["context"]["expression"] == ".class"
    assert msg["context"]["method"] == "css"
    assert msg["context"]["resultType"] == "string"
    assert msg["context"]["resolver"] is None
    assert "frameDesignation" not in msg

def test_makeExecuteMessage_with_resolver(tryxpath, popup_elements):
    """Test creating an execute message with resolver expression."""
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    resolver_checkbox = mock_document.getElementById("resolver-switch")
    resolver_expression = mock_document.getElementById("resolver-expression")
    opt = MockElement("option")
    opt.setAttribute("data-method", "xpath")
    opt.setAttribute("data-type", "node")
    main_way.appendChild(opt)
    main_way.selectedOptions = [opt]
    main_expression.value = "//div"
    resolver_checkbox.checked = True
    resolver_expression.value = "resolver_expression"
    
    msg = tryxpath.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "//div"
    assert msg["main"]["method"] == "xpath"
    assert msg["main"]["resultType"] == "node"
    assert msg["main"]["resolver"] == "resolver_expression"
    assert "context" not in msg
    assert "frameDesignation" not in msg
    
def test_makeExecuteMessage_with_frameDesignation(tryxpath, popup_elements):
    """Test creating an execute message with frame designation."""
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    frame_designation_checkbox = mock_document.getElementById("frame-designation-switch")
    frame_designation_expression = mock_document.getElementById("frame-designation-expression")
    opt = MockElement("option")
    opt.setAttribute("data-method", "xpath")
    opt.setAttribute("data-type", "node")
    main_way.appendChild(opt)
    main_way.selectedOptions = [opt]
    main_expression.value = "//div"
    frame_designation_checkbox.checked = True
    frame_designation_expression.value = "frame_designation"
    
    msg = tryxpath.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "//div"
    assert msg["main"]["method"] == "xpath"
    assert msg["main"]["resultType"] == "node"
    assert msg["main"]["resolver"] is None
    assert "context" not in msg
    assert msg["frameDesignation"] == "frame_designation"

def test_getSpecifiedFrameId_default_no_frameId(tryxpath, popup_elements):
    """Test getting the specified frame ID when no frame ID is selected."""
    frame_id_checkbox = mock_document.getElementById("frame-id-switch")
    frame_id_checkbox.checked = False
    frame_id = tryxpath.getSpecifiedFrameId()
    assert frame_id == 0


def test_getSpecifiedFrameId_manual_frame_id(tryxpath, popup_elements):
    """Test getting the specified frame ID from manual input."""
    frame_id_checkbox = mock_document.getElementById("frame-id-switch")
    frame_id_list = mock_document.getElementById("frame-id-list")
    frame_id_expression = mock_document.getElementById("frame-id-expression")

    opt = MockElement("option")
    opt.setAttribute("data-frame-id", "manual")
    frame_id_list.appendChild(opt)
    frame_id_list.selectedOptions = [opt]
    frame_id_expression.value = "123"
    frame_id_checkbox.checked = True
    frame_id = tryxpath.getSpecifiedFrameId()
    assert frame_id == 123


def test_getSpecifiedFrameId_selected_frame_id(tryxpath, popup_elements):
    """Test getting the specified frame ID from a selected option."""
    frame_id_checkbox = mock_document.getElementById("frame-id-switch")
    frame_id_list = mock_document.getElementById("frame-id-list")

    opt = MockElement("option")
    opt.setAttribute("data-frame-id", "5")
    frame_id_list.appendChild(opt)
    frame_id_list.selectedOptions = [opt]
    frame_id_checkbox.checked = True
    frame_id = tryxpath.getSpecifiedFrameId()
    assert frame_id == 5

def test_execContentScript(tryxpath, popup_elements):
    """Test executing content scripts."""
    tryxpath.execContentScript()
    assert len(mock_browser.tabs.scripts) == 2
    assert mock_browser.tabs.scripts[0]["file"] == "/scripts/try_xpath_functions.js"
    assert mock_browser.tabs.scripts[1]["file"] == "/scripts/try_xpath_content.js"
    assert mock_browser.tabs.scripts[0]["allFrames"] is True
    assert mock_browser.tabs.scripts[1]["allFrames"] is True


def test_sendExecute(tryxpath, popup_elements):
    """Test sending the execute message."""
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    opt = MockElement("option")
    opt.setAttribute("data-method", "xpath")
    opt.setAttribute("data-type", "node")
    main_way.appendChild(opt)
    main_way.selectedOptions = [opt]
    main_expression.value = "//div"
    tryxpath.sendExecute()
    assert len(mock_browser.tabs.scripts) == 2
    assert len(mock_browser.tabs.messages) == 2
    assert mock_browser.tabs.messages[1][1]["event"] == "execute"
    assert mock_browser.tabs.messages[1][1]["main"]["expression"] == "//div"

def test_handleExprEnter_enter_key(tryxpath, popup_elements):
    """Test handling 'Enter' key press to send execute message."""
    main_way = mock_document.getElementById("main-way")
    main_expression = mock_document.getElementById("main-expression")
    opt = MockElement("option")
    opt.setAttribute("data-method", "xpath")
    opt.setAttribute("data-type", "node")
    main_way.appendChild(opt)
    main_way.selectedOptions = [opt]
    main_expression.value = "//div"
    event = MockEvent("Enter")
    tryxpath.handleExprEnter(event)
    assert len(mock_browser.tabs.messages) == 2
    assert mock_browser.tabs.messages[1][1]["event"] == "execute"
    assert event.default_prevented is True

def test_handleExprEnter_not_enter_key(tryxpath, popup_elements):
  """Test not sending execute message when not 'Enter' key pressed."""
  event = MockEvent("A")
  tryxpath.handleExprEnter(event)
  assert len(mock_browser.tabs.messages) == 0
  assert event.default_prevented is False


def test_handleExprEnter_shift_enter_key(tryxpath, popup_elements):
    """Test not sending execute message when 'Shift + Enter' key is pressed."""
    event = MockEvent("Enter", shiftKey=True)
    tryxpath.handleExprEnter(event)
    assert len(mock_browser.tabs.messages) == 0
    assert event.default_prevented is False

def test_showDetailsPage_valid_index(tryxpath, popup_elements):
    """Test showing a specific page of details."""
    results_tbody = mock_document.getElementById("results-details").getElementsByTagName("tbody")[0]
    details_page_count = mock_document.getElementById("details-page-count")
    tryxpath.resultedDetails = [f"item {i}" for i in range(100)]
    with patch("hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.popup.popup.fu.updateDetailsTable") as mock_updateDetailsTable:
        mock_updateDetailsTable.return_value = Promise.resolve()
        tryxpath.showDetailsPage(1)
        mock_updateDetailsTable.assert_called_once()
    assert details_page_count.value == "2"
    assert tryxpath.detailsPageIndex == 1
    assert window.scrollX == 0
    assert window.scrollY == 0

def test_showDetailsPage_invalid_index(tryxpath, popup_elements):
  """Test showDetailsPage with invalid index (should default to first page)"""
  results_tbody = mock_document.getElementById("results-details").getElementsByTagName("tbody")[0]
  details_page_count = mock_document.getElementById("details-page-count")
  tryxpath.resultedDetails = [f"item {i}" for i in range(100)]
  with patch("hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.popup.popup.fu.updateDetailsTable") as mock_updateDetailsTable:
        mock_updateDetailsTable.return_value = Promise.resolve()
        tryxpath.showDetailsPage(-1)
        mock_updateDetailsTable.assert_called_once()
  assert details_page_count.value == "1"
  assert tryxpath.detailsPageIndex == 0
  

def test_showDetailsPage_index_too_large(tryxpath, popup_elements):
  """Test showDetailsPage when index is larger than max page"""
  results_tbody = mock_document.getElementById("results-details").getElementsByTagName("tbody")[0]
  details_page_count = mock_document.getElementById("details-page-count")
  tryxpath.resultedDetails = [f"item {i}" for i in range(100)]
  with patch("hypotez.src.webdriver.chrome.extentions.try_path_1_3_5.popup.popup.fu.updateDetailsTable") as mock_updateDetailsTable:
        mock_updateDetailsTable.return_value = Promise.resolve()
        tryxpath.showDetailsPage(5)
        mock_updateDetailsTable.assert_called_once()
  assert details_page_count.value == "2"
  assert tryxpath.detailsPageIndex == 1
  
def test_showDetailsPage_non_integer_index(tryxpath, popup_elements):
  """Test showDetailsPage with a non integer index"""
  results_tbody = mock_document.getElementById("results-details").getElementsByTagName("tbody")[0]
  details_page_count = mock_document.getElementById("details-page-count")
  tryxpath.resultedDetails = [f"item {i}" for i in range(100)]
  with patch("hypotez