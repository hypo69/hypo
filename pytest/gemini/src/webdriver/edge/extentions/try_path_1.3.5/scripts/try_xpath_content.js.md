```python
import pytest
from unittest.mock import MagicMock, patch

# Mock browser API
class MockBrowser:
    runtime = MagicMock()
    storage = MagicMock()

browser = MockBrowser()

# Mock tryxpath API
class MockTryxpath:
    functions = MagicMock()

tryxpath = MockTryxpath()

# Patch the global browser and tryxpath objects
@pytest.fixture(autouse=True)
def mock_browser_tryxpath():
    with patch.dict('sys.modules', browser=browser, tryxpath=tryxpath):
        yield

# Load the code to test
from hypotez.src.webdriver.edge.extentions.try_path_1_3_5.scripts import try_xpath_content as txc

# --- Fixture definitions ---
@pytest.fixture
def mock_window():
    """Provides a mock window object."""
    win = MagicMock()
    win.frames = []
    win.document = MagicMock()
    win.top = win
    return win

@pytest.fixture
def mock_message():
    """Provides a mock message object."""
    return MagicMock(data={})


@pytest.fixture
def dummy_item():
    """Provides a dummy item for testing."""
    return "dummy_item"

@pytest.fixture
def dummy_items():
    """Provides a dummy item list for testing."""
    return []


# --- Test cases ---

def test_setAttr_calls_saveAttrForItem_and_setAttrToItem(dummy_item):
    """Checks if setAttr calls saveAttrForItem and setAttrToItem correctly."""
    attr = "test-attr"
    value = "test-value"
    
    txc.setAttr(attr, value, dummy_item)

    tryxpath.functions.saveAttrForItem.assert_called_once_with(dummy_item, attr, txc.originalAttributes)
    tryxpath.functions.setAttrToItem.assert_called_once_with(attr, value, dummy_item)


def test_setIndex_calls_saveAttrForItems_and_setIndexToItems(dummy_items):
    """Checks if setIndex calls saveAttrForItems and setIndexToItems correctly."""
    attr = "test-attr"
    
    txc.setIndex(attr, dummy_items)

    tryxpath.functions.saveAttrForItems.assert_called_once_with(dummy_items, attr, txc.originalAttributes)
    tryxpath.functions.setIndexToItems.assert_called_once_with(attr, dummy_items)


def test_isFocusable_returns_true_for_node_or_attr_item():
    """Checks if isFocusable returns true for node and attr items."""
    item = MagicMock()
    tryxpath.functions.isNodeItem.return_value = True
    assert txc.isFocusable(item) is True

    tryxpath.functions.isNodeItem.return_value = False
    tryxpath.functions.isAttrItem.return_value = True
    assert txc.isFocusable(item) is True


def test_isFocusable_returns_false_for_invalid_item():
    """Checks if isFocusable returns false for invalid items."""
    item = None
    assert txc.isFocusable(item) is False

    item = MagicMock()
    tryxpath.functions.isNodeItem.return_value = False
    tryxpath.functions.isAttrItem.return_value = False
    assert txc.isFocusable(item) is False


def test_focusItem_removes_attributes_and_focuses(mock_window, dummy_item):
    """Checks if focusItem removes attributes, sets focus attributes, and calls focus."""
    item = MagicMock()
    element = MagicMock()
    item.blur = MagicMock()
    item.focus = MagicMock()
    item.scrollIntoView = MagicMock()
    tryxpath.functions.isElementItem.return_value = False
    tryxpath.functions.getParentElement.return_value = element
    tryxpath.functions.getAncestorElements.return_value = [MagicMock()]

    txc.focusedItem = dummy_item
    txc.focusedAncestorItems = [dummy_item]
    txc.attributes = {"focused": "focused", "focusedAncestor": "focusedAncestor"}

    txc.focusItem(item)

    tryxpath.functions.removeAttrFromItem.assert_called_once_with("focused", dummy_item)
    tryxpath.functions.removeAttrFromItems.assert_called_once_with("focusedAncestor", [dummy_item])
    tryxpath.functions.getParentElement.assert_called_once_with(item)
    tryxpath.functions.getAncestorElements.assert_called_once_with(element)
    assert txc.focusedItem == element
    assert len(txc.focusedAncestorItems) == 1
    item.blur.assert_called_once()
    item.focus.assert_called_once()
    item.scrollIntoView.assert_called_once()


def test_focusItem_does_not_focus_if_not_focusable(mock_window):
    """Checks if focusItem does not focus if the item is not focusable."""
    item = MagicMock()
    tryxpath.functions.isNodeItem.return_value = False
    tryxpath.functions.isAttrItem.return_value = False

    txc.focusItem(item)

    tryxpath.functions.removeAttrFromItem.assert_not_called()
    tryxpath.functions.removeAttrFromItems.assert_not_called()


def test_setMainAttrs_sets_context_and_element_attributes(mock_window, dummy_item, dummy_items):
    """Checks if setMainAttrs sets context and element attributes correctly."""
    txc.contextItem = dummy_item
    txc.currentItems = dummy_items
    txc.attributes = {"context": "context", "element": "element"}
    txc.setMainAttrs()
    tryxpath.functions.setAttrToItem.assert_called_once_with("context", "true", dummy_item)
    tryxpath.functions.setIndexToItems.assert_called_once_with("element", dummy_items)


def test_restoreAttrs_restores_attributes():
    """Checks if restoreAttrs restores attributes and clears originalAttributes."""
    txc.originalAttributes = MagicMock()
    txc.restoreAttrs()
    tryxpath.functions.restoreItemAttrs.assert_called_once_with(txc.originalAttributes)
    assert txc.originalAttributes == {}


def test_resetPrev_resets_state_and_increments_executionCount(mock_window, dummy_item, dummy_items):
    """Checks if resetPrev resets state and increments executionCount."""
    txc.contextItem = "test_context_item"
    txc.currentItems = ["test_current_item"]
    txc.focusedItem = "test_focused_item"
    txc.focusedAncestorItems = ["test_ancestor_item"]
    txc.executionCount = 1
    txc.prevMsg = "prev_msg"

    txc.resetPrev()

    assert txc.contextItem == ""
    assert txc.currentItems == []
    assert txc.focusedItem == ""
    assert txc.focusedAncestorItems == []
    assert txc.executionCount == 2
    assert isinstance(txc.prevMsg, dict)


def test_makeTypeStr_returns_correct_string_for_number_type():
    """Checks if makeTypeStr returns the correct string for number type."""
    resultType = 1
    tryxpath.functions.getxpathResultStr.return_value = "NUMBER_TYPE"
    assert txc.makeTypeStr(resultType) == "NUMBER_TYPE(1)"

def test_makeTypeStr_returns_empty_string_for_invalid_type():
    """Checks if makeTypeStr returns an empty string for invalid type."""
    resultType = "invalid"
    assert txc.makeTypeStr(resultType) == ""

    resultType = float('nan')
    assert txc.makeTypeStr(resultType) == ""


def test_updateCss_sends_message_if_currentCss_is_null(mock_window):
    """Checks if updateCss sends a message if currentCss is null."""
    txc.currentCss = None
    txc.expiredCssSet = {}

    txc.updateCss()

    browser.runtime.sendMessage.assert_called_once()

def test_updateCss_sends_message_if_expiredCssSet_not_empty(mock_window):
    """Checks if updateCss sends a message if expiredCssSet is not empty."""
    txc.currentCss = "some-css"
    txc.expiredCssSet = {"old-css": True}

    txc.updateCss()

    browser.runtime.sendMessage.assert_called_once()

def test_updateCss_does_not_send_message_if_currentCss_not_null_and_expiredCssSet_empty(mock_window):
    """Checks if updateCss does not send a message if currentCss is not null and expiredCssSet is empty."""
    txc.currentCss = "some-css"
    txc.expiredCssSet = {}

    txc.updateCss()

    browser.runtime.sendMessage.assert_not_called()


def test_getFrames_returns_frame_ancestry(mock_window):
    """Checks if getFrames returns the frame ancestry."""
    spec = "[1, 2]"
    inds = [1, 2]
    mock_frames = [MagicMock(), MagicMock()]

    tryxpath.functions.isNumberArray.return_value = True
    tryxpath.functions.getFrameAncestry.return_value = mock_frames
    
    result = txc.getFrames(spec)

    tryxpath.functions.getFrameAncestry.assert_called_once_with(inds)
    assert result == mock_frames[::-1]

def test_getFrames_throws_error_for_invalid_spec():
    """Checks if getFrames throws an error for an invalid specification."""
    spec = "invalid"
    tryxpath.functions.isNumberArray.return_value = False
    with pytest.raises(Error) as e:
        txc.getFrames(spec)
    assert str(e.value) == "Invalid specification. [invalid]"

def test_parseFrameDesignation_returns_inds(mock_window):
    """Checks if parseFrameDesignation returns the frame designation indices."""
    frameDesi = "[1, 2]"
    inds = [1, 2]

    tryxpath.functions.isNumberArray.return_value = True
    
    result = txc.parseFrameDesignation(frameDesi)

    assert result == inds

def test_parseFrameDesignation_throws_error_for_invalid_frameDesi():
    """Checks if parseFrameDesignation throws an error for invalid specification."""
    frameDesi = "invalid"
    tryxpath.functions.isNumberArray.return_value = False
    with pytest.raises(Error) as e:
        txc.parseFrameDesignation(frameDesi)
    assert str(e.value) == "Invalid specification. [invalid]"


def test_traceBlankWindows_success(mock_window):
    """Checks if traceBlankWindows correctly traces through blank windows."""
    desi = [0, 0]
    mock_window.frames = [MagicMock(), MagicMock()]
    mock_window.frames[0].frames = [MagicMock()]
    tryxpath.functions.isBlankWindow.side_effect = [True, True]
    
    result = txc.traceBlankWindows(desi, mock_window)

    assert result.success is True
    assert result.windows == [mock_window.frames[0], mock_window.frames[0].frames[0]]
    
def test_traceBlankWindows_fails_if_frameInd_out_of_bounds(mock_window):
    """Checks if traceBlankWindows fails if frame index is out of bounds."""
    desi = [10, 0]
    mock_window.frames = [MagicMock()]

    result = txc.traceBlankWindows(desi, mock_window)
    
    assert result.success is False
    assert result.failedWindow is None
    
def test_traceBlankWindows_fails_if_not_blank_window(mock_window):
    """Checks if traceBlankWindows fails if a window is not blank."""
    desi = [0, 0]
    mock_window.frames = [MagicMock(), MagicMock()]
    mock_window.frames[0].frames = [MagicMock()]
    tryxpath.functions.isBlankWindow.side_effect = [True, False]

    result = txc.traceBlankWindows(desi, mock_window)
    
    assert result.success is False
    assert result.failedWindow == mock_window.frames[0].frames[0]
    
def test_handleCssChange_sets_currentCss_if_null_and_in_expiredCssSet(mock_window):
    """Checks if handleCssChange sets currentCss if it is null and the newCss is in expiredCssSet."""
    txc.currentCss = None
    txc.expiredCssSet = {"new-css": True}
    
    txc.handleCssChange("new-css")

    assert txc.currentCss == "new-css"
    assert "new-css" not in txc.expiredCssSet

def test_handleCssChange_sets_currentCss_if_not_same_and_in_expiredCssSet(mock_window):
    """Checks if handleCssChange sets currentCss if not same, and in expiredCssSet."""
    txc.currentCss = "old-css"
    txc.expiredCssSet = {"new-css": True}
    
    txc.handleCssChange("new-css")

    assert txc.currentCss == "new-css"
    assert "new-css" not in txc.expiredCssSet

def test_handleCssChange_sets_currentCss_to_null_and_add_to_expiredCssSet_if_not_same_and_not_in_expiredCssSet(mock_window):
    """Checks if handleCssChange sets currentCss to null and adds old to expiredCssSet if the newCss is not the same and not in expiredCssSet."""
    txc.currentCss = "old-css"
    txc.expiredCssSet = {}
    
    txc.handleCssChange("new-css")

    assert txc.currentCss is None
    assert txc.expiredCssSet == {"old-css": True}

def test_handleCssChange_does_nothing_if_newCss_and_currentCss_are_same(mock_window):
    """Checks if handleCssChange does nothing if newCss and currentCss are the same."""
    txc.currentCss = "same-css"
    txc.expiredCssSet = {}
    
    txc.handleCssChange("same-css")
    
    assert txc.currentCss == "same-css"
    assert not txc.expiredCssSet

def test_findFrameByMessage_returns_frame_element_from_frames(mock_window):
    """Checks if findFrameByMessage returns the frame element from frames."""
    event = MagicMock(data={"frameIndex": 1})
    mock_frame = MagicMock()
    mock_window.frames = [MagicMock(), mock_frame]
    tryxpath.functions.findFrameElement.return_value = "frame-element"
    
    result = txc.findFrameByMessage(event, mock_window)

    assert result == "frame-element"
    tryxpath.functions.findFrameElement.assert_called_once_with(mock_frame, mock_window)

def test_findFrameByMessage_returns_frame_element_from_source(mock_window):
    """Checks if findFrameByMessage returns the frame element from event source."""
    event = MagicMock(data={"frameIndex": -1}, source="event-source")
    tryxpath.functions.findFrameElement.return_value = "frame-element"
    
    result = txc.findFrameByMessage(event, mock_window)

    assert result == "frame-element"
    tryxpath.functions.findFrameElement.assert_called_once_with("event-source", mock_window)


def test_setFocusFrameListener_adds_message_listener_blank(mock_window):
    """Checks if setFocusFrameListener adds a message listener for blank window."""
    txc.updateStyleElement = MagicMock()
    txc.attributes = {"frame": "frame", "frameAncestor": "frameAncestor"}
    
    txc.setFocusFrameListener(mock_window, True)
    
    mock_window.addEventListener.assert_called_once()
    listener = mock_window.addEventListener.call_args[0][1]
    event = MagicMock(data={"message":"tryxpath-focus-frame", "index": 1, "frameIndex": 0})
    tryxpath.functions.findFrameElement.return_value = "mock-frame"
    tryxpath.functions.getAncestorElements.return_value = ["ancestor-mock-frame"]
    listener(event)
    txc.updateStyleElement.assert_called_once_with(mock_window.document)
    tryxpath.functions.setAttrToItem.assert_called_once_with("frame", 1, "mock-frame")
    tryxpath.functions.setIndexToItems.assert_called_once_with("frameAncestor", ["ancestor-mock-frame"])
    
def test_setFocusFrameListener_adds_message_listener_not_blank(mock_window):
    """Checks if setFocusFrameListener adds a message listener for not blank window."""
    txc.updateCss = MagicMock()
    txc.attributes = {"frame": "frame", "frameAncestor": "frameAncestor"}
    mock_window.parent = MagicMock()
    txc.setFocusFrameListener(mock_window, False)
    
    mock_window.addEventListener.assert_called_once()
    listener = mock_window.addEventListener.call_args[0][1]
    event = MagicMock(data={"message":"tryxpath-focus-frame", "index": 1, "frameIndex": 0})
    tryxpath.functions.findFrameElement.return_value = "mock-frame"
    tryxpath.functions.findFrameIndex.return_value = 2
    tryxpath.functions.getAncestorElements.return_value = ["ancestor-mock-frame"]
    
    listener(event)
    txc.updateCss.assert_called_once()
    tryxpath.functions.setAttrToItem.assert_called_once_with("frame", 1, "mock-frame")
    tryxpath.functions.setIndexToItems.assert_called_once_with("frameAncestor", ["ancestor-mock-frame"])
    mock_window.parent.postMessage.assert_called_once()

def test_setFocusFrameListener_does_nothing_if_frame_not_found(mock_window):
    """Checks if setFocusFrameListener doesn't call setAttr if frame is not found."""
    txc.updateCss = MagicMock()
    txc.attributes = {"frame": "frame", "frameAncestor": "frameAncestor"}
    
    txc.setFocusFrameListener(mock_window, False)
    
    mock_window.addEventListener.assert_called_once()
    listener = mock_window.addEventListener.call_args[0][1]
    event = MagicMock(data={"message":"tryxpath-focus-frame", "index": 1, "frameIndex": 0})
    tryxpath.functions.findFrameElement.return_value = None
    
    listener(event)
    txc.updateCss.assert_not_called()
    tryxpath.functions.setAttrToItem.assert_not_called()
    tryxpath.functions.setIndexToItems.assert_not_called()

def test_initBlankWindow_initializes_if_not_initialized(mock_window):
    """Checks if initBlankWindow initializes a blank window if not already initialized."""
    mock_window.tryxpath = Object.create(null)
    mock_window.tryxpath.isInitialized = False
    txc.setFocusFrameListener = MagicMock()

    txc.initBlankWindow(mock_window)

    assert mock_window.tryxpath.isInitialized is True
    txc.setFocusFrameListener.assert_called_once_with(mock_window, True)

def test_initBlankWindow_does_not_initialize_if_already_initialized(mock_window):
    """Checks if initBlankWindow does not initialize a blank window if it's already initialized."""
    mock_window.tryxpath = MagicMock(isInitialized=True)
    txc.setFocusFrameListener = MagicMock()

    txc.initBlankWindow(mock_window)

    txc.setFocusFrameListener.assert_not_called()


def test_findStyleParent_returns_head_or_body(mock_window):
    """Checks if findStyleParent returns the head or body element."""
    mock_doc = MagicMock()
    mock_doc.head = "head"
    
    result = txc.findStyleParent(mock_doc)
    assert result == "head"

    mock_doc.head = None
    mock_doc.body = "body"
    result = txc.findStyleParent(mock_doc)
    assert result == "body"

    mock_doc.body = None
    result = txc.findStyleParent(mock_doc)
    assert result == None
    

def test_updateStyleElement_creates_and_updates_style_element(mock_window):
    """Checks if updateStyleElement creates and updates a style element."""
    mock_doc = MagicMock()
    mock_parent = MagicMock()
    mock_style = MagicMock()
    mock_doc.createElement.return_value = mock_style
    mock_doc.head = mock_parent
    txc.insertedStyleElements = MagicMock()
    txc.currentCss = "test-css"
    txc.styleElementHeader = "header"
    txc.findStyleParent = MagicMock(return_value=mock_parent)
    
    txc.updateStyleElement(mock_doc)
    
    mock_doc.createElement.assert_called_once_with("style")
    mock_style.setAttribute.assert_called_once_with("type", "text/css")
    mock_style.textContent = "headertest-css"
    mock_parent.appendChild.assert_called_once_with(mock_style)
    txc.insertedStyleElements.set.assert_called_once_with(mock_doc, mock_style)


def test_updateStyleElement_updates_existing_style_element(mock_window):
    """Checks if updateStyleElement updates an existing style element."""
    mock_doc = MagicMock()
    mock_style = MagicMock()
    txc.insertedStyleElements = MagicMock()
    txc.insertedStyleElements.get.return_value = mock_style
    txc.currentCss = "test-css"
    txc.styleElementHeader = "header"

    txc.updateStyleElement(mock_doc)

    mock_style.textContent = "headertest-css"
    txc.insertedStyleElements.set.assert_not_called()
    

def test_updateAllStyleElements_updates_all_style_elements(mock_window):
    """Checks if updateAllStyleElements updates all style elements."""
    mock_doc1 = MagicMock()
    mock_doc2 = MagicMock()
    mock_style1 = MagicMock()
    mock_style2 = MagicMock()
    txc.insertedStyleElements = MagicMock()
    txc.insertedStyleElements.items.return_value = [ [mock_doc1, mock_style1], [mock_doc2, mock_style2]]
    txc.currentCss = "test-css"
    txc.styleElementHeader = "header"
    
    txc.updateAllStyleElements()
    
    mock_style1.textContent = "headertest-css"
    mock_style2.textContent = "headertest-css"


def test_removeStyleElement_removes_style_element(mock_window):
    """Checks if removeStyleElement removes a style element from the document."""
    mock_doc = MagicMock()
    mock_elem = MagicMock()
    mock_parent = MagicMock()
    mock_elem.parentNode = mock_parent
    txc.insertedStyleElements = MagicMock()
    txc.insertedStyleElements.get.return_value = mock_elem

    txc.removeStyleElement(mock_doc)
    
    mock_parent.removeChild.assert_called_once_with(mock_elem)
    txc.insertedStyleElements.delete.assert_called_once_with(mock_doc)

def test_removeStyleElement_does_nothing_if_no_element_found(mock_window):
    """Checks if removeStyleElement does nothing if style element is not found."""
    mock_doc = MagicMock()
    txc.insertedStyleElements = MagicMock()
    txc.insertedStyleElements.get.return_value = None

    txc.removeStyleElement(mock_doc)

    txc.insertedStyleElements.delete.assert_not_called()

def test_removeAllStyleElements_removes_all_style_elements(mock_window):
    """Checks if removeAllStyleElements removes all style elements."""
    mock_doc1 = MagicMock()
    mock_doc2 = MagicMock()
    mock_elem1 = MagicMock()
    mock_elem2 = MagicMock()
    mock_parent1 = MagicMock()
    mock_parent2 = MagicMock()
    mock_elem1.parentNode = mock_parent1
    mock_elem2.parentNode = mock_parent2
    txc.insertedStyleElements = MagicMock()
    txc.insertedStyleElements.items.return_value = [[mock_doc1, mock_elem1], [mock_doc2, mock_elem2]]

    txc.removeAllStyleElements()
    
    mock_parent1.removeChild.assert_called_once_with(mock_elem1)
    mock_parent2.removeChild.assert_called_once_with(mock_elem2)
    txc.insertedStyleElements.clear.assert_called_once()


def test_createResultMessage_creates_default_result_message():
    """Checks if createResultMessage creates the default result message correctly."""
    result = txc.createResultMessage()

    assert result["message"] == "There is no result."
    assert result["executionId"] is txc.invalidExecutionId
    assert result["main"]["method"] == "evaluate"
    assert result["main"]["expression"] == ""
    assert result["main"]["specifiedResultType"] == "ANY_TYPE(0)"
    assert result["main"]["resolver"] == ""
    assert result["main"]["itemDetails"] == []

def test_genericListener_calls_correct_listener(mock_window):
    """Checks if genericListener calls the correct listener function based on the event."""
    mock_listener = MagicMock()
    txc.genericListener.listeners = {"test-event": mock_listener}
    message = {"event": "test-event"}

    txc.genericListener(message, MagicMock(), MagicMock())

    mock_listener.assert_called_once_with(message, MagicMock(), MagicMock())
    
def test_genericListener_does_nothing_if_no_listener_defined(mock_window):
    """Checks if genericListener does nothing if no listener is defined for an event."""
    txc.genericListener.listeners = {}
    message = {"event": "test-event"}

    txc.genericListener(message, MagicMock(), MagicMock())


def test_setContentInfo_sets_attributes_if_defined(mock_window):
    """Checks if setContentInfo sets attributes if they are defined in the message."""
    message = {"attributes": {"test-attr": "test-value"}}
    txc.genericListener.listeners.setContentInfo(message)
    assert txc.attributes == {"test-attr": "test-value"}

def test_setContentInfo_does_nothing_if_no_message(mock_window):
    """Checks if setContentInfo does nothing if the message is not provided."""
    txc.attributes = {"old-attr": "old-value"}
    txc.genericListener.listeners.setContentInfo(None)
    assert txc.attributes == {"old-attr": "old-value"}


def test_execute_resets_state_and_sends_message(mock_window):
    """Checks if execute resets state, updates css and sends message."""
    message = {
      "main": {
        "method": "evaluate",
        "expression": "//div",
        "resultType": "ANY_TYPE"
      },
      "frameDesignation": "[0]"
    }

    mock_window.frames = [MagicMock()]
    tryxpath.functions.isNumberArray.return_value = True
    tryxpath.functions.isBlankWindow.return_value = True
    tryxpath.functions.execExpr.return_value = MagicMock(items=["item1"], resultType=0)
    tryxpath.functions.getxpathResultNum.return_value = 0
    tryxpath.functions.getItemDetails.return_value = "item_details"
    
    txc.resetPrev = MagicMock()
    txc.updateCss = MagicMock()
    txc.setMainAttrs = MagicMock()
    txc.updateStyleElement = MagicMock()
    browser.runtime.sendMessage = MagicMock()
    txc.parseFrameDesignation = MagicMock(return_value=[0])
    txc.traceBlankWindows = MagicMock(return_value=MagicMock(success=True, windows=[mock_window.frames[0]]))
    
    txc.genericListener.listeners.execute(message, MagicMock())
    
    txc.resetPrev.assert_called_once()
    txc.updateCss.assert_called_once()
    browser.runtime.sendMessage.assert_called_once()
    txc.setMainAttrs.assert_called_once()
    txc.updateStyleElement.assert_called_once()


def test_execute_sends_error_message_if_frame_not_found(mock_window):
    """Checks if execute sends error message if frame is not found."""
    message = {
      "main": {
        "method": "evaluate",
        "expression": "//div",
        "resultType": "ANY_TYPE"
      },
      "frameDesignation": "[0]"
    }
    
    tryxpath.functions.isNumberArray.return_value = True
    txc.parseFrameDesignation = MagicMock(return_value=[0])
    txc.traceBlankWindows = MagicMock(return_value=MagicMock(success=False, failedWindow=None))
    browser.runtime.sendMessage = MagicMock()
    
    txc.genericListener.listeners.execute(message, MagicMock())

    browser.runtime.sendMessage.assert_called_once()
    assert "The specified frame does not exist." in browser.runtime.sendMessage.call_args[0][0]["message"]

def test_execute_sends_error_message_if_trace_failed(mock_window):
    """Checks if execute sends error message if trace blank window failed"""
    message = {
      "main": {
        "method": "evaluate",
        "expression": "//div",
        "resultType": "ANY_TYPE"
      },
      "frameDesignation": "[0]"
    }

    mock_window.frames = [MagicMock()]
    tryxpath.functions.isNumberArray.return_value = True
    tryxpath.functions.isBlankWindow.return_value = True
    tryxpath.functions.execExpr.return_value = MagicMock(items=["item1"], resultType=0)
    tryxpath.functions.getxpathResultNum.return_value = 0
    tryxpath.functions.getItemDetails.return_value = "item_details"
    
    txc.resetPrev = MagicMock()
    txc.updateCss = MagicMock()
    txc.setMainAttrs = MagicMock()
    txc.updateStyleElement = MagicMock()
    browser.runtime.sendMessage = MagicMock()
    txc.parseFrameDesignation = MagicMock(return_value=[0])
    mock_window.frames[0].postMessage = MagicMock()
    txc.traceBlankWindows = MagicMock(return_value=MagicMock(success=False, failedWindow=mock_window.frames[0]))
    
    txc.genericListener.listeners.execute(message, MagicMock())
    
    txc.resetPrev.assert_called_once()
    txc.updateCss.assert_called_once()
    mock_window.frames[0].postMessage.assert_called_once()

def test_execute_sends_error_message_if_context_not_found(mock_window):
    """Checks if execute sends error message if context is not found."""
    message = {
      "main": {
        "method": "evaluate",
        "expression": "//div",
        "resultType": "ANY_TYPE"
      },
        "context": {
        "method": "evaluate",
        "expression": "//body",
        "resultType": "ANY_TYPE"
        }
    }
    
    tryxpath.functions.isNumberArray.return_value = True
    tryxpath.functions.execExpr.return_value = MagicMock(items=[], resultType=0)
    tryxpath.functions.getxpathResultNum.return_value = 0
    browser.runtime.sendMessage = MagicMock()
    
    txc.genericListener.listeners.execute(message, MagicMock())

    browser.runtime.sendMessage.assert_called_once()
    assert "A context is not found." in browser.runtime.sendMessage.call_args[0][0]["message"]

def test_execute_sends_error_message_if_main_execution_fails(mock_window):
    """Checks if execute sends error message if main execution fails."""
    message = {
      "main": {
        "method": "evaluate",
        "expression": "//div",
        "resultType": "ANY_TYPE"
      }
    }

    tryxpath.functions.isNumberArray.return_value = True
    tryxpath.functions.execExpr.side_effect = Exception("Test error")
    tryxpath.functions.getxpathResultNum.return_value = 0
    browser.runtime.sendMessage = MagicMock()
    
    txc.genericListener.listeners.execute(message, MagicMock())
    
    browser.runtime.sendMessage.assert_called_once()
    assert "An error occurred when getting nodes." in browser.runtime.sendMessage.call_args[0][0]["message"]

def test_execute_sends_error_message_if_context_execution_fails(mock_window):
    """Checks if execute sends error message if