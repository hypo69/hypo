```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Mock browser API
class MockBrowser:
    def __init__(self):
        self.runtime = MockRuntime()
        self.storage = MockStorage()
    
    class MockRuntime:
        def __init__(self):
            self.onMessage = MockOnMessage()

        class MockOnMessage:
            def __init__(self):
                self.listeners = []

            def addListener(self, listener):
                self.listeners.append(listener)

            def trigger(self, message, sender, sendResponse):
                for listener in self.listeners:
                    listener(message, sender, sendResponse)
            
        def sendMessage(self, message):
            pass


    class MockStorage:
        def __init__(self):
          self.onChanged = MockOnChanged()

        class MockOnChanged:
            def __init__(self):
                self.listeners = []

            def addListener(self, listener):
                self.listeners.append(listener)
            
            def trigger(self, changes):
              for listener in self.listeners:
                listener(changes)


class MockWindow:
    def __init__(self, is_blank=False, top=None, parent=None, frames=[]):
        self.is_blank = is_blank
        self.top = top if top else self
        self.parent = parent
        self.frames = frames
        self.document = MockDocument()
        self.tryxpath = None
        self.event_listeners = {}

    def addEventListener(self, event_type, callback):
      if event_type not in self.event_listeners:
        self.event_listeners[event_type] = []
      self.event_listeners[event_type].append(callback)

    def removeEventListener(self, event_type, callback):
        if event_type in self.event_listeners:
          self.event_listeners[event_type].remove(callback)

    def postMessage(self, message, targetOrigin):
        if self.parent and 'message' in message:
          if message['message'] == 'tryxpath-focus-frame':
             self.parent.trigger_message_event(message, self)


    def trigger_message_event(self, message, source):
        if "message" in message and message["message"] == "tryxpath-focus-frame":
          if "message" in message and message["message"] == "tryxpath-focus-frame":
             for callback in self.event_listeners.get('message', []):
                 callback({"data": message, "source": source})

    def focus(self):
      pass
    def blur(self):
      pass
    
    def scrollIntoView(self):
        pass

class MockDocument:
  def __init__(self):
    self.head = MockElement()
    self.body = MockElement()
  def createElement(self, tag_name):
    return MockElement(tag_name)


class MockElement:
  def __init__(self, tag_name=None):
    self.attributes = {}
    self.children = []
    self.tag_name = tag_name
    self.textContent = None
    self.parentNode = None
    self.style = {}

  def setAttribute(self, name, value):
    self.attributes[name] = value
  
  def removeAttribute(self, name):
    if name in self.attributes:
        del self.attributes[name]

  def getAttribute(self, name):
      return self.attributes.get(name)

  def appendChild(self, child):
    self.children.append(child)
    child.parentNode = self
    
  def removeChild(self, child):
      if child in self.children:
          self.children.remove(child)
          child.parentNode = None

# Mock tryxpath functions
class MockTryXpathFunctions:
    def __init__(self):
        self.original_attrs = {}

    def saveAttrForItem(self, item, attr, originalAttributes):
      if item not in self.original_attrs:
          self.original_attrs[item] = {}
      if attr not in self.original_attrs[item]:
          self.original_attrs[item][attr] = item.getAttribute(attr)
      
    def saveAttrForItems(self, items, attr, originalAttributes):
      for item in items:
        self.saveAttrForItem(item, attr, originalAttributes)

    def setAttrToItem(self, attr, value, item):
        item.setAttribute(attr, value)

    def setIndexToItems(self, attr, items):
       for i, item in enumerate(items):
         self.setAttrToItem(attr, str(i), item)


    def removeAttrFromItem(self, attr, item):
       item.removeAttribute(attr)
    
    def removeAttrFromItems(self, attr, items):
      for item in items:
          self.removeAttrFromItem(attr,item)

    def isNodeItem(self, item):
        return isinstance(item, MockElement)

    def isAttrItem(self, item):
        return False

    def isElementItem(self, item):
      return isinstance(item, MockElement)
    
    def getParentElement(self, item):
        if isinstance(item, MockElement):
           return item.parentNode
        return None

    def getAncestorElements(self, item):
        ancestors = []
        current = item.parentNode
        while current:
            ancestors.append(current)
            current = current.parentNode
        return ancestors
    
    def restoreItemAttrs(self, originalAttributes):
      for item, attrs in self.original_attrs.items():
          for attr, value in attrs.items():
              if value is not None:
                  item.setAttribute(attr, value)
              else:
                  item.removeAttribute(attr)
    
    def getxpathResultStr(self, resultType):
      return f"TYPE_{resultType}"
    
    def isNumberArray(self, arr):
       return isinstance(arr, list) and all(isinstance(x, int) for x in arr)

    def getFrameAncestry(self, inds):
      frames = []
      current_window = window
      for ind in inds:
        current_window = current_window.frames[ind]
        frames.append(current_window.document.body)
      return frames

    def isBlankWindow(self, win):
      return win.is_blank
    
    def findFrameElement(self, subWin, win):
      if not subWin:
        return None
      for frame in win.frames:
        if frame == subWin:
          return frame.document.body
      return None

    def findFrameIndex(self, win, parent):
        for i, frame in enumerate(parent.frames):
            if frame == win:
                return i
        return -1
    
    def execExpr(self, expression, method, params):
        # Mock execution logic, return some mock items
      if method == "evaluate":
        if expression == "//*[@id='test']":
          if "context" in params and params["context"] == document:
              mock_element = MockElement()
              mock_element.setAttribute("id", "test")
              return {"items": [mock_element], "resultType": 7}
          elif "context" in params and params["context"] != document:
              mock_element = MockElement()
              mock_element.setAttribute("id", "test_blank")
              return {"items": [mock_element], "resultType": 7}
        elif expression == "//div":
           mock_element_1 = MockElement()
           mock_element_2 = MockElement()
           return {"items": [mock_element_1, mock_element_2], "resultType": 7}
      return {"items": [], "resultType": 0}
    
    def getItemDetail(self, item):
       return {"tagName": item.tag_name, "attributes": item.attributes}

    def getItemDetails(self, items):
        return [self.getItemDetail(item) for item in items]

# Setup mocks
browser = MockBrowser()
window = MockWindow()
document = window.document
tryxpath = {}
tryxpath['functions'] = MockTryXpathFunctions()
tryxpath['isContentLoaded'] = False

# Execute the code
with patch.dict('sys.modules', {'browser': browser}):
    exec(open('hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/scripts/try_xpath_content.js').read())

# Fixtures
@pytest.fixture
def mock_message():
  return {"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "showResultsInPopup"}

@pytest.fixture
def mock_execute_message():
    return {
        "main": {
            "method": "evaluate",
            "expression": "//*[@id='test']",
            "resultType": "ANY_TYPE(0)",
            "resolver": ""
        },
        "context": None
    }

@pytest.fixture
def mock_execute_message_with_context():
  return {
        "main": {
            "method": "evaluate",
            "expression": "//div",
            "resultType": "ANY_TYPE(0)",
            "resolver": ""
        },
        "context": {
            "method": "evaluate",
            "expression": "//*[@id='test']",
             "resultType": "ANY_TYPE(0)",
            "resolver": ""
        }
    }

@pytest.fixture
def mock_execute_message_with_frame():
  return {
        "main": {
            "method": "evaluate",
            "expression": "//*[@id='test']",
            "resultType": "ANY_TYPE(0)",
            "resolver": ""
        },
       "frameDesignation": "[0]"
    }

@pytest.fixture
def mock_execute_message_with_invalid_frame():
  return {
        "main": {
            "method": "evaluate",
            "expression": "//*[@id='test']",
            "resultType": "ANY_TYPE(0)",
            "resolver": ""
        },
       "frameDesignation": "[-1]"
    }

@pytest.fixture
def mock_focus_item_message():
    return {"executionId": 1, "index": 0, "event": "focusItem"}

@pytest.fixture
def mock_focus_context_item_message():
    return {"executionId": 1, "event": "focusContextItem"}

@pytest.fixture
def mock_focus_frame_message():
    return {"event": "focusFrame"}

@pytest.fixture
def mock_focus_frame_message_with_frame():
    return {"event": "focusFrame", "frameDesignation": "[0]"}

@pytest.fixture
def mock_focus_frame_message_with_invalid_frame():
    return {"event": "focusFrame", "frameDesignation": "[-1]"}

@pytest.fixture
def mock_set_content_info_message():
    return {"event": "setContentInfo", "attributes": {"element": "data-tryxpath-element", "context": "data-tryxpath-context", "focused": "data-tryxpath-focused", "focusedAncestor": "data-tryxpath-focused-ancestor", "frame": "data-tryxpath-frame", "frameAncestor": "data-tryxpath-frame-ancestor"}}

@pytest.fixture
def mock_set_style_message():
    return {"event": "setStyle"}

@pytest.fixture
def mock_reset_style_message():
   return {"event": "resetStyle"}

@pytest.fixture
def mock_finish_insert_css_message():
  return {"event": "finishInsertCss", "css": "test_css"}

@pytest.fixture
def mock_finish_remove_css_message():
  return {"event": "finishRemoveCss", "css": "test_css"}

@pytest.fixture
def mock_request_message_to_popup():
    return {"message": "tryxpath-request-message-to-popup", "messageId": 0}

@pytest.fixture
def mock_request_message_to_popup_1():
    return {"message": "tryxpath-request-message-to-popup", "messageId": 1}

@pytest.fixture
def mock_storage_change_message():
    return {"attributes": {"newValue": {"element": "data-tryxpath-element-2", "context": "data-tryxpath-context-2", "focused": "data-tryxpath-focused-2", "focusedAncestor": "data-tryxpath-focused-ancestor-2", "frame": "data-tryxpath-frame-2", "frameAncestor": "data-tryxpath-frame-ancestor-2"}}}

@pytest.fixture
def mock_css_storage_change_message():
  return {"css":{"newValue":"test_css"}}

# Tests
def test_setAttr():
    item = MockElement()
    tx.setAttr("test", "value", item)
    assert item.getAttribute("test") == "value"

def test_setIndex():
    items = [MockElement(), MockElement()]
    tx.setIndex("index", items)
    assert items[0].getAttribute("index") == "0"
    assert items[1].getAttribute("index") == "1"

def test_isFocusable_with_node_item():
  item = MockElement()
  assert tx.isFocusable(item) == True

def test_isFocusable_with_attr_item():
  item = "test"
  assert tx.isFocusable(item) == False

def test_isFocusable_with_invalid_item():
  assert tx.isFocusable(None) == False

def test_focusItem():
    item = MockElement()
    tx.focusItem(item)
    assert item.getAttribute("data-tryxpath-focused") == "true"

def test_focusItem_not_focusable():
    item = "test"
    tx.focusItem(item)
    
def test_setMainAttrs():
    tx.contextItem = MockElement()
    tx.currentItems = [MockElement(), MockElement()]
    tx.setMainAttrs()
    assert tx.contextItem.getAttribute("data-tryxpath-context") == "true"
    assert tx.currentItems[0].getAttribute("data-tryxpath-element") == "0"
    assert tx.currentItems[1].getAttribute("data-tryxpath-element") == "1"

def test_restoreAttrs():
    item = MockElement()
    item.setAttribute("test", "value")
    tx.originalAttributes.set(item, {"test":"value"})
    tx.restoreAttrs()
    assert item.getAttribute("test") == "value"
    assert len(tx.originalAttributes) == 0

def test_resetPrev():
    tx.contextItem = "test_context"
    tx.currentItems = ["test_item"]
    tx.focusedItem = "test_focused"
    tx.focusedAncestorItems = ["test_ancestor"]
    tx.resetPrev()
    assert tx.contextItem == ""
    assert tx.currentItems == []
    assert tx.focusedItem == ""
    assert tx.focusedAncestorItems == []
    assert tx.executionCount == 1

def test_makeTypeStr_with_number():
    assert tx.makeTypeStr(1) == "TYPE_1(1)"

def test_makeTypeStr_with_invalid_number():
    assert tx.makeTypeStr("test") == ""

def test_updateCss_no_currentCss():
    tx.currentCss = None
    tx.expiredCssSet["test_css"] = True
    browser.runtime.sendMessage = MagicMock()
    tx.updateCss()
    browser.runtime.sendMessage.assert_called_once()

def test_updateCss_expiredCss():
    tx.currentCss = "old_css"
    tx.expiredCssSet["test_css"] = True
    browser.runtime.sendMessage = MagicMock()
    tx.updateCss()
    browser.runtime.sendMessage.assert_called_once()

def test_updateCss_no_change():
    tx.currentCss = "test_css"
    tx.expiredCssSet = {}
    browser.runtime.sendMessage = MagicMock()
    tx.updateCss()
    browser.runtime.sendMessage.assert_not_called()

def test_getFrames():
    window.frames = [MockWindow(is_blank=True), MockWindow(is_blank=True)]
    frames = tx.getFrames("[0,1]")
    assert len(frames) == 2

def test_getFrames_invalid_spec():
    with pytest.raises(Exception, match="Invalid specification. \\[invalid\\]"):
        tx.getFrames("invalid")

def test_parseFrameDesignation():
  inds = tx.parseFrameDesignation("[0,1]")
  assert inds == [0, 1]

def test_parseFrameDesignation_invalid_spec():
    with pytest.raises(Exception, match="Invalid specification. \\[invalid\\]"):
        tx.parseFrameDesignation("invalid")

def test_traceBlankWindows_success():
    window.frames = [MockWindow(is_blank=True)]
    result = tx.traceBlankWindows([0])
    assert result.success == True
    assert result.windows[0] == window.frames[0]

def test_traceBlankWindows_failed_frame_index():
  window.frames = [MockWindow(is_blank=True)]
  result = tx.traceBlankWindows([1])
  assert result.success == False
  assert result.failedWindow == None

def test_traceBlankWindows_failed_not_blank():
    window.frames = [MockWindow(is_blank=False)]
    result = tx.traceBlankWindows([0])
    assert result.success == False
    assert result.failedWindow == window.frames[0]


def test_handleCssChange_new_css():
    tx.currentCss = "old_css"
    tx.expiredCssSet["new_css"] = True
    tx.handleCssChange("new_css")
    assert tx.currentCss == "new_css"
    assert "new_css" not in tx.expiredCssSet

def test_handleCssChange_same_css():
    tx.currentCss = "test_css"
    tx.expiredCssSet = {}
    tx.handleCssChange("test_css")
    assert tx.currentCss == "test_css"
    assert not tx.expiredCssSet

def test_handleCssChange_change_current_css():
  tx.currentCss = "old_css"
  tx.expiredCssSet = {}
  tx.handleCssChange("new_css")
  assert tx.currentCss == None
  assert tx.expiredCssSet["old_css"] == True

def test_handleCssChange_new_css_first_time():
  tx.currentCss = None
  tx.expiredCssSet["test_css"] = True
  tx.handleCssChange("test_css")
  assert tx.currentCss == "test_css"
  assert "test_css" not in tx.expiredCssSet


def test_findFrameByMessage_with_index():
    win = MockWindow()
    win.frames = [MockWindow()]
    event = MagicMock(data={"frameIndex":0})
    frame = tx.findFrameByMessage(event, win)
    assert frame == win.frames[0].document.body

def test_findFrameByMessage_with_source():
    win = MockWindow()
    event = MagicMock(data={"frameIndex":-1}, source=MockWindow())
    frame = tx.findFrameByMessage(event, win)
    assert frame == event.source.document.body

def test_setFocusFrameListener_blank_window():
    win = MockWindow(is_blank=True)
    tx.setFocusFrameListener(win, True)
    assert "message" in win.event_listeners

def test_setFocusFrameListener_not_blank_window():
   win = MockWindow()
   tx.setFocusFrameListener(win, False)
   assert "message" in win.event_listeners
   

def test_initBlankWindow():
    win = MockWindow(is_blank=True)
    tx.initBlankWindow(win)
    assert win.tryxpath.isInitialized == True

def test_initBlankWindow_already_initialized():
    win = MockWindow(is_blank=True)
    win.tryxpath = {"isInitialized": True}
    tx.initBlankWindow(win)
    assert win.tryxpath.isInitialized == True
    

def test_findStyleParent_with_head():
    doc = MockDocument()
    assert tx.findStyleParent(doc) == doc.head

def test_findStyleParent_with_body():
    doc = MockDocument()
    doc.head = None
    assert tx.findStyleParent(doc) == doc.body

def test_findStyleParent_without_head_and_body():
    doc = MockDocument()
    doc.head = None
    doc.body = None
    assert tx.findStyleParent(doc) == None
    

def test_updateStyleElement_new_style():
  doc = MockDocument()
  tx.currentCss = "test_css"
  tx.insertedStyleElements = {}
  tx.updateStyleElement(doc)
  assert len(doc.head.children) == 1
  assert doc.head.children[0].textContent ==  "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\\ntest_css"

def test_updateStyleElement_update_style():
  doc = MockDocument()
  style_element = MockElement("style")
  tx.insertedStyleElements.set(doc, style_element)
  tx.currentCss = "test_css_updated"
  tx.updateStyleElement(doc)
  assert style_element.textContent == "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\\ntest_css_updated"

def test_updateAllStyleElements():
    doc1 = MockDocument()
    doc2 = MockDocument()
    elem1 = MockElement("style")
    elem2 = MockElement("style")
    tx.insertedStyleElements.set(doc1, elem1)
    tx.insertedStyleElements.set(doc2, elem2)
    tx.currentCss = "test_css"
    tx.updateAllStyleElements()
    assert elem1.textContent == "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\\ntest_css"
    assert elem2.textContent == "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\\ntest_css"

def test_removeStyleElement():
  doc = MockDocument()
  elem = MockElement("style")
  doc.head.appendChild(elem)
  tx.insertedStyleElements.set(doc, elem)
  tx.removeStyleElement(doc)
  assert len(doc.head.children) == 0
  assert not tx.insertedStyleElements.get(doc)

def test_removeStyleElement_not_found():
  doc = MockDocument()
  tx.insertedStyleElements = {}
  tx.removeStyleElement(doc)

def test_removeAllStyleElements():
    doc1 = MockDocument()
    doc2 = MockDocument()
    elem1 = MockElement("style")
    elem2 = MockElement("style")
    doc1.head.appendChild(elem1)
    doc2.head.appendChild(elem2)
    tx.insertedStyleElements.set(doc1, elem1)
    tx.insertedStyleElements.set(doc2, elem2)
    tx.removeAllStyleElements()
    assert len(doc1.head.children) == 0
    assert len(doc2.head.children) == 0
    assert len(tx.insertedStyleElements) == 0

def test_createResultMessage():
    result = tx.createResultMessage()
    assert result["message"] == "There is no result."
    assert result["main"]["method"] == "evaluate"

def test_genericListener_with_listener(mock_message):
    mock_listener = MagicMock()
    tx.genericListener.listeners["showResultsInPopup"] = mock_listener
    tx.genericListener(mock_message, None, None)
    mock_listener.assert_called_once()

def test_genericListener_without_listener(mock_message):
    tx.genericListener(mock_message, None, None)

def test_setContentInfo_listener(mock_set_content_info_message):
    tx.genericListener.listeners.setContentInfo(mock_set_content_info_message)
    assert tx.attributes["element"] == "data-tryxpath-element"
    assert tx.attributes["context"] == "data-tryxpath-context"
    assert tx.attributes["focused"] == "data-tryxpath-focused"
    assert tx.attributes["focusedAncestor"] == "data-tryxpath-focused-ancestor"
    assert tx.attributes["frame"] == "data-tryxpath-frame"
    assert tx.attributes["frameAncestor"] == "data-tryxpath-frame-ancestor"

def test_setContentInfo_listener_with_none():
    tx.genericListener.listeners.setContentInfo(None)

def test_execute_listener(mock_execute_message):
    browser.runtime.sendMessage = MagicMock()
    tx.genericListener.listeners.execute(mock_execute_message, None)
    browser.runtime.sendMessage.assert_called_once()
    assert tx.executionCount == 1
    assert tx.contextItem == document
    assert len(tx.currentItems) > 0

def test_execute_listener_with_context(mock_execute_message_with_context):
  browser.runtime.sendMessage = MagicMock()
  tx.genericListener.listeners.execute(mock_execute_message_with_context, None)
  browser.runtime.sendMessage.assert_called_once()
  assert tx.executionCount == 1
  assert tx.contextItem != document
  assert len(tx.currentItems) > 0

def test_execute_listener_with_frame(mock_execute_message_with_frame):
    browser.runtime.sendMessage = MagicMock()
    window.frames = [MockWindow(is_blank=True)]
    tx.genericListener.listeners.execute(mock_execute_message_with_frame, None)
    browser.runtime.sendMessage.assert_called_once()
    assert tx.inBlankWindow == True
    assert tx.executionCount == 1
    assert tx.currentDocument == window.frames[0].document

def test_execute_listener_with_invalid_frame(mock_execute_message_with_invalid_frame):
    browser.runtime.sendMessage = MagicMock()
    tx.genericListener.listeners.execute(mock_execute_message_with_invalid_frame, None)
    browser.runtime.sendMessage.assert_called_once()

def test_execute_listener_with_not_found_context(mock_execute_message_with_context):
    mock_execute_message_with_context['context']['expression'] = "//not_found"
    browser.runtime.sendMessage = MagicMock()
    tx.genericListener.listeners.execute(mock_execute_message_with_context, None)
    browser.runtime.sendMessage.assert_called_once()
  
def test_execute_listener_with_exception_context(mock_execute_message_with_context):
    mock_execute_message_with_context['context']['expression'] = "error"
    browser.runtime.sendMessage = MagicMock()
    tx.genericListener.listeners.execute(mock_execute_message_with_context, None)
    browser.runtime.sendMessage.assert_called_once()

def test_execute_listener_with_exception_main(mock_execute_message):
    mock_execute_message['main']['expression'] = "error"
    browser.runtime.sendMessage = MagicMock()
    tx.genericListener.listeners.execute(mock_execute_message, None)
    browser.runtime.sendMessage.assert_called_once()
    
def test_focusItem_listener(mock_focus_item_message):
    tx.executionCount = 1
    tx.currentItems = [MockElement()]
    tx.genericListener.listeners.focusItem(mock_focus_item_message)
    assert tx.currentItems[0].getAttribute("data-tryxpath-focused") == "true"

def test_focusItem_listener_invalid_id(mock_focus_item_message):
  tx.executionCount = 2
  tx.currentItems = [MockElement()]
  tx.genericListener.listeners.focusItem(mock_focus_item_message)
  assert tx.currentItems[0].getAttribute("data-tryxpath-focused") != "true"
  

def test_focusContextItem_listener(mock_focus_context_item_message):
    tx.executionCount = 1
    tx.contextItem = MockElement()
    tx.genericListener.listeners.focusContextItem(mock_focus_context_item_message)
    assert tx.contextItem.getAttribute("data-tryxpath-focused") == "true"

def test_focusContextItem_listener_invalid_id(mock_focus_context_item_message):
  tx.executionCount = 2
  tx.contextItem = MockElement()
  tx.genericListener.listeners.focusContextItem(mock_focus_context_item_message)
  assert tx.contextItem.getAttribute("data-tryxpath-focused") != "true"


def test_focusFrame_listener(mock_focus_frame_message):
    window.parent = MockWindow()
    window.parent.postMessage = MagicMock()
    tx.genericListener.listeners.focusFrame(mock_focus_frame_message)
    window.parent.postMessage.assert_called_once()

def test_focusFrame_listener_top_window(mock_focus_frame_message):
    window.parent = None
    window.focus = MagicMock()
    tx.genericListener.listeners.focusFrame(mock_focus_frame_message)
    window.focus.assert_called_once()

def test_focusFrame_listener_with_frame(mock_focus_frame_message_with_frame):
    window.frames = [MockWindow(is_blank=True)]
    window.parent = MockWindow()
    tx.genericListener.listeners.focusFrame(mock_focus_frame_message_with_frame)
    assert len(window.frames[0].event_listeners["message"]) > 0
   

def test_focusFrame_listener_with_invalid_frame(mock_focus_frame_message_with_invalid_frame):
    browser.runtime.sendMessage = MagicMock()
    tx.genericListener.listeners.focusFrame(mock_focus_frame_message_with_invalid_frame)
    browser.runtime.sendMessage.assert_called_once()


def test_requestShowResultsInPopup_listener(mock_message):
    browser.runtime.sendMessage = MagicMock()
    tx.prevMsg = mock_message
    tx.genericListener.listeners.requestShowResultsInPopup()
    browser.runtime.sendMessage.assert_called_once()

def test_requestShowResultsInPopup_listener_no_prev(mock_message):
    browser.runtime.sendMessage = MagicMock()
    tx.prevMsg = None
    tx.genericListener.listeners.requestShowResultsInPopup()
    browser.runtime.sendMessage.assert_not_called()

def test_requestShowAllResults_listener(mock_message):
    browser.runtime.sendMessage = MagicMock()
    tx.prevMsg = mock_message
    tx.genericListener.listeners.requestShowAllResults()
    browser.runtime.sendMessage.assert_called_once()

def test_requestShowAllResults_listener_no_prev():
    browser.runtime.sendMessage = MagicMock()
    tx.prevMsg = None
    tx.genericListener.listeners.requestShowAllResults()
    browser.runtime.sendMessage.assert_not_called()


def test_resetStyle_listener():
    tx.originalAttributes = "test"
    tx.insertedStyleElements = {"test":"test"}
    tx.genericListener.listeners.resetStyle()
    assert tx.originalAttributes == {}
    assert len(tx.insertedStyleElements) == 0

def test_setStyle_listener(mock_set_style_message):
    browser.runtime.sendMessage = MagicMock()
    tx.currentCss = "test_css"
    tx.contextItem = MockElement()
    tx.currentItems = [MockElement()]
    tx.genericListener.listeners.setStyle(mock_set_style_message)
    browser.runtime.sendMessage.assert_called()
    assert tx.contextItem.getAttribute("data-tryxpath-context") == "true"
    assert tx.currentItems[0].getAttribute("data-tryxpath-element") == "0"


def test_finishInsertCss_listener(mock_finish_insert_css_message):
    tx.expiredCssSet = {"test_css":True}
    tx.insertedStyleElements = {}
    tx.genericListener.listeners.finishInsertCss(mock_finish_insert_css_message)
    assert tx.currentCss == "test_css"
    assert "test_css" not in tx.expiredCssSet

def test_finishRemoveCss_listener(mock_finish_remove_css_message):
    tx.currentCss = "test_css"
    tx.expiredCssSet = {"test_css":True}
    tx.genericListener.listeners.finishRemoveCss(mock_finish_remove_css_message)
    assert tx.currentCss == None
    assert "test_css" not in tx.expiredCssSet

def test_finishRemoveCss_listener_not_current_css(mock_finish_remove_css_message):
    tx.currentCss = "other_css"
    tx.expiredCssSet = {"test_css":True}
    tx.genericListener.listeners.finishRemoveCss(mock_finish_remove_css_message)
    assert tx.currentCss == "other_css"
    assert "test_css" not in tx.expiredCssSet

def test_storage_onChanged_attributes_listener(mock_storage_change_message):
    browser.storage.onChanged.trigger(mock_storage_change_message)
    assert tx.attributes["element"] == "data-tryxpath-element-2"
    assert tx.attributes["context"] == "data-tryxpath-context-2"
    assert tx.attributes["focused"] == "data-tryxpath-focused-2