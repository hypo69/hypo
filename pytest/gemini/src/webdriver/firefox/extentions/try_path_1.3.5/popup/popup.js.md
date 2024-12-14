```python
import pytest
from unittest.mock import MagicMock, patch

# Mock browser API and tryxpath functions
@pytest.fixture
def mock_browser():
    with patch('popup.browser') as mock_browser:
        mock_browser.tabs.query.return_value = [{"id": 1}]
        mock_browser.tabs.sendMessage.return_value = PromiseMock()
        mock_browser.tabs.executeScript.return_value = PromiseMock(True)
        mock_browser.runtime.onMessage = MagicMock()
        mock_browser.runtime.sendMessage = MagicMock()
        mock_browser.runtime.openOptionsPage = MagicMock()
        yield mock_browser

@pytest.fixture
def mock_tryxpath():
    with patch('popup.tryxpath') as mock_tryxpath:
        mock_tryxpath.functions.updateDetailsTable.return_value = PromiseMock()
        mock_tryxpath.functions.emptyChildNodes = MagicMock()
        mock_tryxpath.functions.createDetailTableHeader = MagicMock(return_value=MagicMock())
        mock_tryxpath.functions.onError = MagicMock()
        yield mock_tryxpath

@pytest.fixture
def mock_document():
    with patch('popup.window.document') as mock_document:
        mock_element = MagicMock()
        mock_element.classList = MagicMock()
        mock_element.selectedOptions = [MagicMock(getAttribute=lambda x: "test")]
        mock_document.getElementById.return_value = mock_element
        mock_document.getElementsByClassName.return_value = [mock_element]
        mock_document.createElement.return_value = mock_element
        mock_document.head = MagicMock()
        yield mock_document

class PromiseMock:
    def __init__(self, resolve_value=None):
        self.resolve_value = resolve_value

    def then(self, callback):
        if self.resolve_value is not None:
           callback(self.resolve_value)
        return self

    def catch(self, callback):
        return self


def test_sendToActiveTab_success(mock_browser, mock_document):
    from popup import sendToActiveTab
    message = {"test": "message"}
    sendToActiveTab(message)
    mock_browser.tabs.query.assert_called_once_with({"active": True, "currentWindow": True})
    mock_browser.tabs.sendMessage.assert_called_once_with(1, message, {})

def test_sendToSpecifiedFrame_success(mock_browser, mock_tryxpath, mock_document):
    from popup import sendToSpecifiedFrame, getSpecifiedFrameId
    message = {"test": "message"}
    sendToSpecifiedFrame(message)
    mock_browser.tabs.executeScript.assert_called()
    mock_browser.tabs.sendMessage.assert_called()

def test_sendToSpecifiedFrame_error(mock_browser, mock_tryxpath, mock_document):
    from popup import sendToSpecifiedFrame, getSpecifiedFrameId, showError
    mock_browser.tabs.executeScript.return_value = PromiseMock(False)
    mock_browser.tabs.sendMessage.side_effect = Exception("Test Error")
    with patch('popup.showError') as mock_showError:
        message = {"test": "message"}
        sendToSpecifiedFrame(message)
        mock_showError.assert_called()

def test_collectPopupState(mock_document):
    from popup import collectPopupState
    mock_document.getElementById.return_value.checked = True
    mock_document.getElementById.return_value.selectedIndex = 1
    mock_document.getElementById.return_value.value = "test_value"
    state = collectPopupState()
    assert state["helpCheckboxChecked"] == True
    assert state["mainWayIndex"] == 1
    assert state["mainExpressionValue"] == "test_value"

def test_changeContextVisible_show(mock_document):
    from popup import changeContextVisible
    mock_document.getElementById.return_value.checked = True
    changeContextVisible()
    mock_document.getElementById.return_value.classList.remove.assert_called_once()
    
def test_changeContextVisible_hide(mock_document):
    from popup import changeContextVisible
    mock_document.getElementById.return_value.checked = False
    changeContextVisible()
    mock_document.getElementById.return_value.classList.add.assert_called_once()

def test_changeResolverVisible_show(mock_document):
    from popup import changeResolverVisible
    mock_document.getElementById.return_value.checked = True
    changeResolverVisible()
    mock_document.getElementById.return_value.classList.remove.assert_called_once()
    
def test_changeResolverVisible_hide(mock_document):
    from popup import changeResolverVisible
    mock_document.getElementById.return_value.checked = False
    changeResolverVisible()
    mock_document.getElementById.return_value.classList.add.assert_called_once()

def test_changeFrameIdVisible_show(mock_document):
    from popup import changeFrameIdVisible
    mock_document.getElementById.return_value.checked = True
    changeFrameIdVisible()
    mock_document.getElementById.return_value.classList.remove.assert_called_once()
    
def test_changeFrameIdVisible_hide(mock_document):
    from popup import changeFrameIdVisible
    mock_document.getElementById.return_value.checked = False
    changeFrameIdVisible()
    mock_document.getElementById.return_value.classList.add.assert_called_once()

def test_changeFrameDesignationVisible_show(mock_document):
    from popup import changeFrameDesignationVisible
    mock_document.getElementById.return_value.checked = True
    changeFrameDesignationVisible()
    mock_document.getElementById.return_value.classList.remove.assert_called_once()
    
def test_changeFrameDesignationVisible_hide(mock_document):
    from popup import changeFrameDesignationVisible
    mock_document.getElementById.return_value.checked = False
    changeFrameDesignationVisible()
    mock_document.getElementById.return_value.classList.add.assert_called_once()

def test_changeHelpVisible_show(mock_document):
    from popup import changeHelpVisible
    mock_document.getElementById.return_value.checked = True
    changeHelpVisible()
    mock_document.getElementsByClassName.return_value[0].classList.remove.assert_called_once()
    
def test_changeHelpVisible_hide(mock_document):
    from popup import changeHelpVisible
    mock_document.getElementById.return_value.checked = False
    changeHelpVisible()
    mock_document.getElementsByClassName.return_value[0].classList.add.assert_called_once()
    
def test_makeExecuteMessage_no_resolver(mock_document):
    from popup import makeExecuteMessage
    mock_document.getElementById.return_value.checked = False
    mock_document.getElementById.return_value.value = "test_expression"
    msg = makeExecuteMessage()
    assert msg["main"]["expression"] == "test_expression"
    assert msg["main"]["resolver"] == None

def test_makeExecuteMessage_with_resolver(mock_document):
    from popup import makeExecuteMessage
    mock_document.getElementById("resolver-switch").checked = True
    mock_document.getElementById("resolver-expression").value = "test_resolver"
    mock_document.getElementById("main-expression").value = "test_expression"

    msg = makeExecuteMessage()
    assert msg["main"]["expression"] == "test_expression"
    assert msg["main"]["resolver"] == "test_resolver"

def test_getSpecifiedFrameId_default(mock_document):
    from popup import getSpecifiedFrameId
    mock_document.getElementById.return_value.checked = False
    assert getSpecifiedFrameId() == 0

def test_getSpecifiedFrameId_manual(mock_document):
    from popup import getSpecifiedFrameId
    mock_document.getElementById("frame-id-switch").checked = True
    mock_document.getElementById("frame-id-list").selectedOptions = [MagicMock(getAttribute=lambda x: "manual")]
    mock_document.getElementById("frame-id-expression").value = "123"
    assert getSpecifiedFrameId() == 123

def test_getSpecifiedFrameId_from_list(mock_document):
    from popup import getSpecifiedFrameId
    mock_document.getElementById("frame-id-switch").checked = True
    mock_document.getElementById("frame-id-list").selectedOptions = [MagicMock(getAttribute=lambda x: "456")]
    assert getSpecifiedFrameId() == 456

def test_execContentScript(mock_browser):
    from popup import execContentScript
    execContentScript()
    assert mock_browser.tabs.executeScript.call_count == 2

def test_sendExecute(mock_browser, mock_document, mock_tryxpath):
    from popup import sendExecute, sendToSpecifiedFrame, makeExecuteMessage
    with patch('popup.sendToSpecifiedFrame') as mock_sendToSpecifiedFrame:
       with patch('popup.makeExecuteMessage') as mock_makeExecuteMessage:
            sendExecute()
            mock_sendToSpecifiedFrame.assert_called()

def test_handleExprEnter_enter_no_shift(mock_document):
    from popup import handleExprEnter
    mock_event = MagicMock()
    mock_event.key = "Enter"
    mock_event.shiftKey = False
    with patch('popup.sendExecute') as mock_sendExecute:
        handleExprEnter(mock_event)
        mock_sendExecute.assert_called_once()

def test_handleExprEnter_not_enter(mock_document):
    from popup import handleExprEnter
    mock_event = MagicMock()
    mock_event.key = "a"
    mock_event.shiftKey = False
    with patch('popup.sendExecute') as mock_sendExecute:
         handleExprEnter(mock_event)
         mock_sendExecute.assert_not_called()

def test_handleExprEnter_enter_shift(mock_document):
    from popup import handleExprEnter
    mock_event = MagicMock()
    mock_event.key = "Enter"
    mock_event.shiftKey = True
    with patch('popup.sendExecute') as mock_sendExecute:
        handleExprEnter(mock_event)
        mock_sendExecute.assert_not_called()
    
def test_showDetailsPage_valid_index(mock_tryxpath):
    from popup import showDetailsPage
    with patch('popup.resultedDetails', [1,2,3,4,5,6,7,8,9]):
        showDetailsPage(1)
        mock_tryxpath.functions.updateDetailsTable.assert_called()

def test_showDetailsPage_invalid_index(mock_tryxpath):
    from popup import showDetailsPage
    with patch('popup.resultedDetails', [1,2,3,4,5,6,7,8,9]):
       showDetailsPage("str")
       mock_tryxpath.functions.updateDetailsTable.assert_called()
       
def test_showDetailsPage_index_less_than_0(mock_tryxpath):
    from popup import showDetailsPage
    with patch('popup.resultedDetails', [1,2,3,4,5,6,7,8,9]):
        showDetailsPage(-1)
        mock_tryxpath.functions.updateDetailsTable.assert_called()

def test_showDetailsPage_index_greater_than_max(mock_tryxpath):
    from popup import showDetailsPage
    with patch('popup.resultedDetails', [1,2,3,4,5,6,7,8,9]):
        showDetailsPage(10)
        mock_tryxpath.functions.updateDetailsTable.assert_called()

def test_showError(mock_tryxpath):
    from popup import showError
    showError("test error", 123)
    mock_tryxpath.functions.updateDetailsTable.assert_called()

def test_genericListener_with_listener(mock_browser):
    from popup import genericListener
    listener_mock = MagicMock()
    genericListener.listeners["test"] = listener_mock
    message = {"event": "test"}
    genericListener(message, {}, {})
    listener_mock.assert_called()

def test_genericListener_no_listener(mock_browser):
    from popup import genericListener
    message = {"event": "test"}
    result = genericListener(message, {}, {})
    assert result is None

def test_showResultsInPopup(mock_tryxpath, mock_browser):
    from popup import genericListener
    message = {"event": "showResultsInPopup", "executionId": 1, "message": "test",
     "main": {"itemDetails": [1,2,3]}, "context": {"itemDetail": {}}}
    sender = {"tab": {"id": 1}, "frameId": 1}
    genericListener(message, sender, {})
    mock_tryxpath.functions.updateDetailsTable.assert_called()

def test_restorePopupState(mock_browser, mock_document):
    from popup import genericListener
    state = {
        "helpCheckboxChecked": True,
        "mainWayIndex": 1,
        "mainExpressionValue": "test",
        "contextCheckboxChecked": True,
        "contextWayIndex": 1,
        "contextExpressionValue": "test",
        "resolverCheckboxChecked": True,
        "resolverExpressionValue": "test",
        "frameDesignationCheckboxChecked": True,
        "frameDesignationExpressionValue": "test",
        "frameIdCheckboxChecked": True,
        "specifiedFrameId": 1,
        "detailsPageIndex": 1
    }
    message = {"event": "restorePopupState", "state": state}
    genericListener(message, {}, {})
    assert mock_document.getElementById.call_count == 10

def test_restorePopupState_no_state(mock_browser, mock_document):
    from popup import genericListener
    message = {"event": "restorePopupState", "state": None}
    genericListener(message, {}, {})

def test_insertStyleToPopup(mock_document):
    from popup import genericListener
    message = {"event": "insertStyleToPopup", "css": "test_css"}
    genericListener(message, {}, {})
    mock_document.head.appendChild.assert_called()

def test_addFrameId(mock_document):
    from popup import genericListener
    sender = {"frameId": 1}
    message = {"event": "addFrameId"}
    genericListener(message, sender, {})
    mock_document.createElement.assert_called()

def test_window_load_event(mock_browser, mock_tryxpath, mock_document):
    from popup import window
    # Simulate the 'load' event
    load_event = MagicMock()
    # Call the event listener
    window.load_event_listeners[0]()
    mock_browser.runtime.sendMessage.assert_called()
```