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
            self.sendMessage = MagicMock()

        class MockOnMessage:
            def __init__(self):
                self.listeners = []

            def addListener(self, listener):
                self.listeners.append(listener)

            def trigger(self, message, sender, sendResponse):
                for listener in self.listeners:
                    listener(message, sender, sendResponse)

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

browser = MockBrowser()

# Load the script to test
with open("hypotez/src/webdriver/chrome/extentions/try_path_1.3.5/scripts/try_xpath_content.js", "r") as f:
    script_content = f.read()

# Execute the script in a mock browser environment
def execute_script():
    mock_window = MagicMock()
    mock_window.frames = []
    mock_window.location = MagicMock()
    mock_window.location.href = "https://example.com"
    mock_window.document = MagicMock()
    mock_window.document.title = "Test Page"
    mock_window.document.head = MagicMock()
    mock_window.document.body = MagicMock()
    mock_window.top = mock_window
    mock_window.addEventListener = MagicMock()
    mock_window.postMessage = MagicMock()
    mock_window.removeEventListener = MagicMock()


    mock_window.browser = browser
    
    exec(script_content, {'window': mock_window})
    return mock_window

mock_window = execute_script()

# Fixture for functions
@pytest.fixture
def tryxpath_functions():
    """Provides access to tryxpath functions."""
    return mock_window.tryxpath.functions

@pytest.fixture
def reset_state():
    """Resets the state before each test."""
    mock_window.tryxpath.isContentLoaded = True # To skip the multiple execution check
    mock_window.browser.runtime.onMessage.trigger({"event": "resetStyle"}, None, None)
    mock_window.tryxpath.isContentLoaded = True
    return mock_window

@pytest.fixture
def dummy_message():
    """Provides a dummy message for testing."""
    return {
            "timeout":0,
            "timeout_for_event":"presence_of_element_located",
            "event": "showResultsInPopup",
            "executionId": 1,
            "href": "https://example.com",
            "title": "Test Page",
            "message": "Success.",
            "main": {
                "method": "evaluate",
                "expression": "//div",
                "specifiedResultType": "ANY_TYPE(0)",
                "resolver": "",
                "itemDetails": []
             }
        }


# Tests for setAttr
def test_setAttr_valid_input(tryxpath_functions, reset_state):
    """Checks correct setting of attribute with valid input."""
    item = MagicMock()
    attr = "test-attr"
    value = "test-value"
    mock_window.setAttr(attr, value, item)
    tryxpath_functions.saveAttrForItem.assert_called_with(item, attr, mock_window.originalAttributes)
    tryxpath_functions.setAttrToItem.assert_called_with(attr, value, item)


# Tests for setIndex
def test_setIndex_valid_input(tryxpath_functions, reset_state):
    """Checks correct setting of index with valid input."""
    items = [MagicMock(), MagicMock()]
    attr = "test-index"
    mock_window.setIndex(attr, items)
    tryxpath_functions.saveAttrForItems.assert_called_with(items, attr, mock_window.originalAttributes)
    tryxpath_functions.setIndexToItems.assert_called_with(attr, items)

# Tests for isFocusable
def test_isFocusable_valid_element(tryxpath_functions, reset_state):
    """Checks isFocusable returns true for a valid element item."""
    item = MagicMock()
    tryxpath_functions.isNodeItem.return_value = True
    assert mock_window.isFocusable(item) == True

def test_isFocusable_valid_attribute(tryxpath_functions, reset_state):
    """Checks isFocusable returns true for a valid attribute item."""
    item = MagicMock()
    tryxpath_functions.isNodeItem.return_value = False
    tryxpath_functions.isAttrItem.return_value = True
    assert mock_window.isFocusable(item) == True

def test_isFocusable_invalid_item(tryxpath_functions, reset_state):
    """Checks isFocusable returns false for invalid item."""
    item = MagicMock()
    tryxpath_functions.isNodeItem.return_value = False
    tryxpath_functions.isAttrItem.return_value = False
    assert mock_window.isFocusable(item) == False

def test_isFocusable_None_item(tryxpath_functions, reset_state):
    """Checks isFocusable returns false for None item."""
    assert mock_window.isFocusable(None) == False


# Tests for focusItem
def test_focusItem_valid_element(tryxpath_functions, reset_state):
    """Checks focusItem works with a valid element item."""
    item = MagicMock()
    tryxpath_functions.isElementItem.return_value = True
    tryxpath_functions.isNodeItem.return_value = True
    tryxpath_functions.getAncestorElements.return_value = [MagicMock()]
    mock_window.focusItem(item)
    tryxpath_functions.removeAttrFromItem.assert_called_with(mock_window.attributes.focused, mock_window.focusedItem)
    tryxpath_functions.removeAttrFromItems.assert_called_with(mock_window.attributes.focusedAncestor, mock_window.focusedAncestorItems)
    assert mock_window.focusedItem == item
    tryxpath_functions.getAncestorElements.assert_called_with(item)
    mock_window.browser.runtime.sendMessage.assert_not_called()
    item.blur.assert_called()
    item.focus.assert_called()
    item.scrollIntoView.assert_called()

def test_focusItem_valid_attribute(tryxpath_functions, reset_state):
    """Checks focusItem works with a valid attribute item."""
    item = MagicMock()
    parent = MagicMock()
    tryxpath_functions.isElementItem.return_value = False
    tryxpath_functions.isNodeItem.return_value = False
    tryxpath_functions.isAttrItem.return_value = True
    tryxpath_functions.getParentElement.return_value = parent
    tryxpath_functions.getAncestorElements.return_value = [MagicMock()]
    mock_window.focusItem(item)
    assert mock_window.focusedItem == parent
    tryxpath_functions.getAncestorElements.assert_called_with(parent)
    parent.blur.assert_called()
    parent.focus.assert_called()
    parent.scrollIntoView.assert_called()

def test_focusItem_invalid_item(tryxpath_functions, reset_state):
    """Checks focusItem does not throw error with invalid item."""
    item = MagicMock()
    tryxpath_functions.isNodeItem.return_value = False
    tryxpath_functions.isAttrItem.return_value = False
    mock_window.focusItem(item)
    tryxpath_functions.removeAttrFromItem.assert_not_called()
    tryxpath_functions.removeAttrFromItems.assert_not_called()
    assert mock_window.focusedItem == ""
    assert mock_window.focusedAncestorItems == []

def test_focusItem_None_item(tryxpath_functions, reset_state):
     """Checks focusItem does not throw error with None item."""
     mock_window.focusItem(None)
     tryxpath_functions.removeAttrFromItem.assert_not_called()
     tryxpath_functions.removeAttrFromItems.assert_not_called()
     assert mock_window.focusedItem == ""
     assert mock_window.focusedAncestorItems == []

# Tests for setMainAttrs
def test_setMainAttrs_with_context(tryxpath_functions, reset_state):
    """Checks setMainAttrs sets the attributes with context."""
    mock_window.contextItem = MagicMock()
    mock_window.currentItems = [MagicMock(), MagicMock()]
    mock_window.setMainAttrs()
    tryxpath_functions.saveAttrForItem.assert_called_with(mock_window.contextItem, mock_window.attributes.context, mock_window.originalAttributes)
    tryxpath_functions.setAttrToItem.assert_called_with(mock_window.attributes.context, "true", mock_window.contextItem)
    tryxpath_functions.saveAttrForItems.assert_called_with(mock_window.currentItems, mock_window.attributes.element, mock_window.originalAttributes)
    tryxpath_functions.setIndexToItems.assert_called_with(mock_window.attributes.element, mock_window.currentItems)

def test_setMainAttrs_no_context(tryxpath_functions, reset_state):
    """Checks setMainAttrs sets the attributes without context."""
    mock_window.contextItem = None
    mock_window.currentItems = [MagicMock(), MagicMock()]
    mock_window.setMainAttrs()
    tryxpath_functions.saveAttrForItem.assert_not_called()
    tryxpath_functions.setAttrToItem.assert_not_called()
    tryxpath_functions.saveAttrForItems.assert_called_with(mock_window.currentItems, mock_window.attributes.element, mock_window.originalAttributes)
    tryxpath_functions.setIndexToItems.assert_called_with(mock_window.attributes.element, mock_window.currentItems)

# Tests for restoreAttrs
def test_restoreAttrs(tryxpath_functions, reset_state):
    """Checks restoreAttrs restores the attributes."""
    mock_window.originalAttributes = MagicMock()
    mock_window.restoreAttrs()
    tryxpath_functions.restoreItemAttrs.assert_called_with(mock_window.originalAttributes)
    assert mock_window.originalAttributes.mock_calls == []

# Tests for resetPrev
def test_resetPrev(reset_state):
    """Checks resetPrev resets the variables."""
    mock_window.contextItem = "testContext"
    mock_window.currentItems = ["testItem"]
    mock_window.focusedItem = "testFocus"
    mock_window.focusedAncestorItems = ["testAncestor"]
    mock_window.prevMsg = "testPrevMsg"
    mock_window.executionCount = 1
    mock_window.resetPrev()
    assert mock_window.contextItem == ""
    assert mock_window.currentItems == []
    assert mock_window.focusedItem == ""
    assert mock_window.focusedAncestorItems == []
    assert mock_window.prevMsg["message"] == "There is no result."
    assert mock_window.executionCount == 2

# Tests for makeTypeStr
def test_makeTypeStr_valid_number(tryxpath_functions, reset_state):
    """Checks makeTypeStr returns the correct string for valid number."""
    resultType = 4
    tryxpath_functions.getxpathResultStr.return_value = "NUMBER_TYPE"
    assert mock_window.makeTypeStr(resultType) == "NUMBER_TYPE(4)"

def test_makeTypeStr_invalid_number(tryxpath_functions, reset_state):
    """Checks makeTypeStr returns empty string for invalid number."""
    resultType = float("NaN")
    assert mock_window.makeTypeStr(resultType) == ""

def test_makeTypeStr_not_number(tryxpath_functions, reset_state):
    """Checks makeTypeStr returns empty string for invalid type."""
    resultType = "test"
    assert mock_window.makeTypeStr(resultType) == ""

# Tests for updateCss
def test_updateCss_no_currentCss(reset_state):
    """Checks updateCss calls sendMessage if currentCss is None."""
    mock_window.currentCss = None
    mock_window.expiredCssSet = {}
    mock_window.updateCss()
    mock_window.browser.runtime.sendMessage.assert_called_with({"timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss", "expiredCssSet": {}})

def test_updateCss_expiredCssSet_not_empty(reset_state):
    """Checks updateCss calls sendMessage if expiredCssSet is not empty."""
    mock_window.currentCss = "testCss"
    mock_window.expiredCssSet = {"testCss": True}
    mock_window.updateCss()
    mock_window.browser.runtime.sendMessage.assert_called_with({"timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss", "expiredCssSet": {"testCss": True}})


def test_updateCss_no_update_needed(reset_state):
    """Checks updateCss does not call sendMessage if no update needed."""
    mock_window.currentCss = "testCss"
    mock_window.expiredCssSet = {}
    mock_window.updateCss()
    mock_window.browser.runtime.sendMessage.assert_not_called()


# Tests for getFrames
def test_getFrames_valid_spec(tryxpath_functions, reset_state):
    """Checks getFrames returns the correct frames for valid spec."""
    spec = '[1, 2]'
    frames = ["frame1", "frame2"]
    tryxpath_functions.isNumberArray.return_value = True
    tryxpath_functions.getFrameAncestry.return_value = frames
    assert mock_window.getFrames(spec) == frames[::-1]
    tryxpath_functions.getFrameAncestry.assert_called_with([1,2])

def test_getFrames_invalid_spec(tryxpath_functions, reset_state):
    """Checks getFrames throws an error with invalid spec."""
    spec = 'invalid'
    tryxpath_functions.isNumberArray.return_value = False
    with pytest.raises(Exception, match=r"Invalid specification. \[invalid\]"):
        mock_window.getFrames(spec)

def test_getFrames_empty_spec(tryxpath_functions, reset_state):
    """Checks getFrames throws an error with empty spec."""
    spec = '[]'
    tryxpath_functions.isNumberArray.return_value = True
    tryxpath_functions.getFrameAncestry.return_value = []
    with pytest.raises(Exception, match=r"Invalid specification. \[[]\]"):
        mock_window.getFrames(spec)


# Tests for parseFrameDesignation
def test_parseFrameDesignation_valid_frameDesi(tryxpath_functions, reset_state):
    """Checks parseFrameDesignation returns correct array for valid input."""
    frameDesi = '[1, 2, 3]'
    tryxpath_functions.isNumberArray.return_value = True
    assert mock_window.parseFrameDesignation(frameDesi) == [1,2,3]

def test_parseFrameDesignation_invalid_frameDesi(tryxpath_functions, reset_state):
    """Checks parseFrameDesignation throws error with invalid input."""
    frameDesi = 'invalid'
    tryxpath_functions.isNumberArray.return_value = False
    with pytest.raises(Exception, match=r"Invalid specification. \[invalid\]"):
        mock_window.parseFrameDesignation(frameDesi)

def test_parseFrameDesignation_empty_frameDesi(tryxpath_functions, reset_state):
    """Checks parseFrameDesignation throws error with empty input."""
    frameDesi = '[]'
    tryxpath_functions.isNumberArray.return_value = True
    with pytest.raises(Exception, match=r"Invalid specification. \[[]\]"):
        mock_window.parseFrameDesignation(frameDesi)


# Tests for traceBlankWindows
def test_traceBlankWindows_valid_desi(tryxpath_functions, reset_state):
    """Checks traceBlankWindows returns correct result for valid desi."""
    mock_window.frames = [MagicMock(), MagicMock()]
    mock_window.frames[0].frames = [MagicMock()]
    mock_window.frames[0].frames[0].frames = []
    mock_window.frames[0].frames[0].tryxpath = {}
    mock_window.frames[0].frames[0].tryxpath.isInitialized = True
    mock_window.frames[0].tryxpath = {}
    mock_window.frames[0].tryxpath.isInitialized = True

    desi = [0, 0]
    tryxpath_functions.isBlankWindow.return_value = True
    result = mock_window.traceBlankWindows(desi, mock_window)
    assert result.success == True
    assert result.windows == [mock_window.frames[0], mock_window.frames[0].frames[0]]

def test_traceBlankWindows_invalid_desi_index_out_of_range(tryxpath_functions, reset_state):
    """Checks traceBlankWindows returns correct result for invalid desi (index out of range)."""
    mock_window.frames = [MagicMock()]
    desi = [1]
    result = mock_window.traceBlankWindows(desi, mock_window)
    assert result.success == False
    assert result.failedWindow == None

def test_traceBlankWindows_invalid_desi_not_blank_window(tryxpath_functions, reset_state):
    """Checks traceBlankWindows returns correct result for invalid desi (not blank window)."""
    mock_window.frames = [MagicMock()]
    desi = [0]
    tryxpath_functions.isBlankWindow.return_value = False
    result = mock_window.traceBlankWindows(desi, mock_window)
    assert result.success == False
    assert result.failedWindow == mock_window.frames[0]


# Tests for handleCssChange
def test_handleCssChange_newCss_is_null(reset_state):
    """Checks handleCssChange works when currentCss is null and newCss is in expiredCssSet."""
    mock_window.currentCss = None
    mock_window.expiredCssSet = {"newCss": True}
    mock_window.handleCssChange("newCss")
    assert mock_window.currentCss == "newCss"
    assert "newCss" not in mock_window.expiredCssSet

def test_handleCssChange_newCss_not_null_and_not_equal(reset_state):
    """Checks handleCssChange works when newCss is not currentCss and newCss is in expiredCssSet."""
    mock_window.currentCss = "oldCss"
    mock_window.expiredCssSet = {"newCss": True}
    mock_window.handleCssChange("newCss")
    assert mock_window.currentCss == "newCss"
    assert "newCss" not in mock_window.expiredCssSet

def test_handleCssChange_newCss_not_null_and_not_equal_and_not_in_expiredCssSet(reset_state):
    """Checks handleCssChange works when newCss is not currentCss and not in expiredCssSet."""
    mock_window.currentCss = "oldCss"
    mock_window.expiredCssSet = {}
    mock_window.handleCssChange("newCss")
    assert mock_window.currentCss == None
    assert mock_window.expiredCssSet["oldCss"] == True

def test_handleCssChange_newCss_equal_to_currentCss(reset_state):
    """Checks handleCssChange does nothing when newCss is same as currentCss."""
    mock_window.currentCss = "testCss"
    mock_window.expiredCssSet = {}
    mock_window.handleCssChange("testCss")
    assert mock_window.currentCss == "testCss"
    assert mock_window.expiredCssSet == {}


# Tests for findFrameByMessage
def test_findFrameByMessage_valid_index(tryxpath_functions, reset_state):
    """Checks findFrameByMessage returns frame for valid index."""
    mock_window.frames = [MagicMock()]
    event = MagicMock()
    event.data.frameIndex = 0
    tryxpath_functions.findFrameElement.return_value = mock_window.frames[0]
    assert mock_window.findFrameByMessage(event, mock_window) == mock_window.frames[0]
    tryxpath_functions.findFrameElement.assert_called_with(mock_window.frames[0], mock_window)

def test_findFrameByMessage_invalid_index(tryxpath_functions, reset_state):
    """Checks findFrameByMessage returns frame from event source for invalid index."""
    event = MagicMock()
    event.data.frameIndex = -1
    event.source = "eventSource"
    tryxpath_functions.findFrameElement.return_value = "eventSource"
    assert mock_window.findFrameByMessage(event, mock_window) == "eventSource"
    tryxpath_functions.findFrameElement.assert_called_with("eventSource", mock_window)

# Tests for setFocusFrameListener
def test_setFocusFrameListener_blank_window(tryxpath_functions, reset_state):
    """Checks setFocusFrameListener sets up listener correctly for blank window."""
    win = MagicMock()
    win.addEventListener = MagicMock()
    mock_window.setFocusFrameListener(win, True)
    win.addEventListener.assert_called_once()
    
    event = MagicMock()
    event.data = {"message": "tryxpath-focus-frame", "index": 1, "frameIndex": 2}
    win.addEventListener.call_args[0][1](event)
    tryxpath_functions.findFrameByMessage.assert_called_with(event, win)

def test_setFocusFrameListener_not_blank_window(tryxpath_functions, reset_state):
    """Checks setFocusFrameListener sets up listener correctly for not blank window."""
    win = MagicMock()
    win.addEventListener = MagicMock()
    mock_window.setFocusFrameListener(win, False)
    win.addEventListener.assert_called_once()
    
    event = MagicMock()
    event.data = {"message": "tryxpath-focus-frame", "index": 1, "frameIndex": 2}
    win.addEventListener.call_args[0][1](event)
    tryxpath_functions.findFrameByMessage.assert_called_with(event, win)


def test_setFocusFrameListener_invalid_message(tryxpath_functions, reset_state):
    """Checks setFocusFrameListener does nothing if message is invalid."""
    win = MagicMock()
    win.addEventListener = MagicMock()
    mock_window.setFocusFrameListener(win, True)
    win.addEventListener.assert_called_once()
    
    event = MagicMock()
    event.data = {"message": "invalid-message", "index": 1, "frameIndex": 2}
    win.addEventListener.call_args[0][1](event)
    tryxpath_functions.findFrameByMessage.assert_not_called()

def test_setFocusFrameListener_invalid_index(tryxpath_functions, reset_state):
    """Checks setFocusFrameListener does nothing if index is invalid."""
    win = MagicMock()
    win.addEventListener = MagicMock()
    mock_window.setFocusFrameListener(win, True)
    win.addEventListener.assert_called_once()
    
    event = MagicMock()
    event.data = {"message": "tryxpath-focus-frame", "index": "invalid", "frameIndex": 2}
    win.addEventListener.call_args[0][1](event)
    tryxpath_functions.findFrameByMessage.assert_not_called()

def test_setFocusFrameListener_invalid_frameIndex(tryxpath_functions, reset_state):
    """Checks setFocusFrameListener does nothing if frameIndex is invalid."""
    win = MagicMock()
    win.addEventListener = MagicMock()
    mock_window.setFocusFrameListener(win, True)
    win.addEventListener.assert_called_once()
    
    event = MagicMock()
    event.data = {"message": "tryxpath-focus-frame", "index": 1, "frameIndex": "invalid"}
    win.addEventListener.call_args[0][1](event)
    tryxpath_functions.findFrameByMessage.assert_not_called()


# Tests for initBlankWindow
def test_initBlankWindow_not_initialized(reset_state):
    """Checks initBlankWindow initializes tryxpath if not already initialized."""
    win = MagicMock()
    mock_window.initBlankWindow(win)
    assert win.tryxpath.isInitialized == True
    win.addEventListener.assert_called()

def test_initBlankWindow_already_initialized(reset_state):
    """Checks initBlankWindow does nothing if already initialized."""
    win = MagicMock()
    win.tryxpath = {}
    win.tryxpath.isInitialized = True
    mock_window.initBlankWindow(win)
    win.addEventListener.assert_not_called()

# Tests for findStyleParent
def test_findStyleParent_with_head(reset_state):
    """Checks findStyleParent returns head element if available."""
    doc = MagicMock()
    doc.head = "head"
    assert mock_window.findStyleParent(doc) == "head"

def test_findStyleParent_with_body(reset_state):
    """Checks findStyleParent returns body element if head is not available."""
    doc = MagicMock()
    doc.head = None
    doc.body = "body"
    assert mock_window.findStyleParent(doc) == "body"

def test_findStyleParent_no_head_or_body(reset_state):
    """Checks findStyleParent returns null if neither head nor body is available."""
    doc = MagicMock()
    doc.head = None
    doc.body = None
    assert mock_window.findStyleParent(doc) == None


# Tests for updateStyleElement
def test_updateStyleElement_no_style(reset_state):
    """Checks updateStyleElement creates and appends a new style element when style element is not present."""
    doc = MagicMock()
    parent = MagicMock()
    doc.createElement.return_value = MagicMock()
    mock_window.findStyleParent.return_value = parent
    mock_window.currentCss = "testCss"
    mock_window.insertedStyleElements = MagicMock()
    mock_window.updateStyleElement(doc)
    mock_window.insertedStyleElements.get.assert_called_with(doc)
    doc.createElement.assert_called_with("style")
    parent.appendChild.assert_called()
    mock_window.insertedStyleElements.set.assert_called_with(doc, doc.createElement())

def test_updateStyleElement_style_exists(reset_state):
    """Checks updateStyleElement updates existing style element."""
    doc = MagicMock()
    style = MagicMock()
    mock_window.insertedStyleElements = MagicMock()
    mock_window.insertedStyleElements.get.return_value = style
    mock_window.currentCss = "testCss"
    mock_window.updateStyleElement(doc)
    mock_window.insertedStyleElements.get.assert_called_with(doc)
    style.textContent = "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\ntestCss"
    doc.createElement.assert_not_called()

def test_updateStyleElement_no_parent(reset_state):
    """Checks updateStyleElement does nothing when parent is not found."""
    doc = MagicMock()
    mock_window.findStyleParent.return_value = None
    mock_window.updateStyleElement(doc)
    mock_window.findStyleParent.assert_called_with(doc)
    doc.createElement.assert_not_called()


# Tests for updateAllStyleElements
def test_updateAllStyleElements(reset_state):
    """Checks updateAllStyleElements updates all style elements."""
    doc1 = MagicMock()
    elem1 = MagicMock()
    doc2 = MagicMock()
    elem2 = MagicMock()
    mock_window.insertedStyleElements = MagicMock()
    mock_window.insertedStyleElements.__iter__.return_value = iter([(doc1, elem1), (doc2, elem2)])
    mock_window.currentCss = "testCss"
    mock_window.updateAllStyleElements()
    elem1.textContent = "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\ntestCss"
    elem2.textContent = "/* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */\ntestCss"


# Tests for removeStyleElement
def test_removeStyleElement_style_exists(reset_state):
    """Checks removeStyleElement removes style element."""
    doc = MagicMock()
    elem = MagicMock()
    parent = MagicMock()
    elem.parentNode = parent
    mock_window.insertedStyleElements = MagicMock()
    mock_window.insertedStyleElements.get.return_value = elem
    mock_window.removeStyleElement(doc)
    parent.removeChild.assert_called_with(elem)
    mock_window.insertedStyleElements.delete.assert_called_with(doc)


def test_removeStyleElement_style_not_exists(reset_state):
     """Checks removeStyleElement does nothing if style element not found."""
     doc = MagicMock()
     mock_window.insertedStyleElements = MagicMock()
     mock_window.insertedStyleElements.get.return_value = None
     mock_window.removeStyleElement(doc)
     mock_window.insertedStyleElements.delete.assert_not_called()


# Tests for removeAllStyleElements
def test_removeAllStyleElements(reset_state):
    """Checks removeAllStyleElements removes all style elements."""
    doc1 = MagicMock()
    elem1 = MagicMock()
    parent1 = MagicMock()
    elem1.parentNode = parent1
    doc2 = MagicMock()
    elem2 = MagicMock()
    parent2 = MagicMock()
    elem2.parentNode = parent2
    mock_window.insertedStyleElements = MagicMock()
    mock_window.insertedStyleElements.__iter__.return_value = iter([(doc1, elem1), (doc2, elem2)])
    mock_window.removeAllStyleElements()
    parent1.removeChild.assert_called_with(elem1)
    parent2.removeChild.assert_called_with(elem2)
    mock_window.insertedStyleElements.clear.assert_called()

# Tests for createResultMessage
def test_createResultMessage(reset_state):
    """Checks createResultMessage returns the default result message."""
    result = mock_window.createResultMessage()
    assert result["message"] == "There is no result."
    assert result["executionId"] == float("NaN")
    assert result["main"]["specifiedResultType"] == "ANY_TYPE(0)"


# Tests for genericListener
def test_genericListener_valid_listener(reset_state):
    """Checks genericListener calls listener if it exists."""
    listener = MagicMock()
    mock_window.genericListener.listeners["testEvent"] = listener
    message = {"event": "testEvent"}
    mock_window.genericListener(message, "sender", "sendResponse")
    listener.assert_called_with(message, "sender", "sendResponse")

def test_genericListener_no_listener(reset_state):
    """Checks genericListener does nothing if listener doesn't exist."""
    message = {"event": "nonexistentEvent"}
    mock_window.genericListener(message, "sender", "sendResponse")

# Tests for genericListener.listeners.setContentInfo
def test_setContentInfo_valid_message(reset_state):
    """Checks setContentInfo updates the attributes."""
    message = {"attributes": {"test": "testValue"}}
    mock_window.genericListener.listeners.setContentInfo(message)
    assert mock_window.attributes == {"test": "testValue"}

def test_setContentInfo_no_message(reset_state):
    """Checks setContentInfo does not throw error if message is None."""
    mock_window.genericListener.listeners.setContentInfo(None)

def test_setContentInfo_no_attributes(reset_state):
    """Checks setContentInfo does not throw error if attributes is not in message."""
    message = {"test": "testValue"}
    mock_window.genericListener.listeners.setContentInfo(message)


# Tests for genericListener.listeners.execute
def test_execute_valid_message(tryxpath_functions, reset_state, dummy_message):
    """Checks execute processes valid message."""
    message = {
        "main": {
            "method": "evaluate",
            "expression": "//div",
            "resultType": "ANY_TYPE",
             "resolver": ""
        }
    }

    tryxpath_functions.execExpr.return_value = {"items": [MagicMock()], "resultType": 4}
    tryxpath_functions.getItemDetails.return_value = "test"
    mock_window.genericListener.listeners.execute(message, None)
    assert mock_window.executionCount == 1
    tryxpath_functions.execExpr.assert_called()
    assert mock_window.prevMsg["message"] == "Success."
    assert mock_window.prevMsg["executionId"] == 1

def test_execute_with_frameDesignation(tryxpath_functions, reset_state, dummy_message):
    """Checks execute processes valid message with frame designation."""
    message = {
            "main": {
                "method": "evaluate",
                "expression": "//div",
                "resultType": "ANY_TYPE",
                "resolver": ""
            },
            "frameDesignation": "[0]"
        }
    tryxpath_functions.isNumberArray.return_value = True
    mock_window.traceBlankWindows.return_value = {"success": True, "windows": [Magic