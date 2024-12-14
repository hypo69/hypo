```python
import pytest
from unittest.mock import MagicMock, patch
import json
import asyncio

# Mock browser API
class MockBrowser:
    def __init__(self):
        self.tabs = MockTabs()
        self.runtime = MockRuntime()

class MockTabs:
    def __init__(self):
         self.tab_id_counter = 0
         self.tabs = []

    def query(self, query_info):
        if query_info.get("active") and query_info.get("currentWindow"):
             return  asyncio.Future() 
        return  asyncio.Future() 

    def sendMessage(self, tab_id, message, options=None):
        return asyncio.Future()
    
    def executeScript(self, script_info):
        return asyncio.Future()
    
    def createTab(self, tab_info):
        self.tab_id_counter += 1
        self.tabs.append({"id":self.tab_id_counter})
        return asyncio.Future()

    def update(self, tab_id, tab_info):
        return asyncio.Future()

class MockRuntime:
    def __init__(self):
        self.listeners = {}

    def onMessage(self):
       return self
    
    def addListener(self, listener):
         self.listeners = listener
    
    def sendMessage(self, message):
         if isinstance(self.listeners, dict) and message.get("event"):
            if message["event"] in self.listeners:
                return self.listeners[message["event"]](message)
         return  asyncio.Future() 
    
    def openOptionsPage(self):
         return asyncio.Future()

@pytest.fixture
def mock_browser():
    with patch('popup.browser', MockBrowser()):
        yield

@pytest.fixture
def mock_dom():
    """Provides a mock DOM structure for testing."""
    
    class MockElement:
        def __init__(self, tag_name, id=None, class_name=None, selected_index=0, value="",  attributes=None, text_content = None, child_nodes = None):
            self.tagName = tag_name.upper()
            self.id = id
            self.className = class_name or ""
            self.classList = MockClassList(class_name)
            self.selectedIndex = selected_index
            self.value = value
            self.selectedOptions = [MockElement("option", attributes={"data-method":"test_method","data-type":"test_type"})] if tag_name.upper() == "SELECT" else []
            self.attributes = attributes if attributes is not None else {}
            self.textContent = text_content
            self.childNodes = child_nodes if child_nodes is not None else []
            
        def getAttribute(self, name):
                return self.attributes.get(name)

        def appendChild(self, node):
                self.childNodes.append(node)
        
        def getElementsByTagName(self, tag_name):
            return [child for child in self.childNodes if child.tagName == tag_name.upper()] if self.childNodes else []
        
        def removeChild(self, node):
           if node in self.childNodes:
              self.childNodes.remove(node)

    class MockClassList:
        def __init__(self, class_name):
            self.classes = set(class_name.split() if class_name else [])
        
        def add(self, class_name):
            self.classes.add(class_name)

        def remove(self, class_name):
            self.classes.discard(class_name)
        
        def contains(self, class_name):
           return class_name in self.classes
        
    def get_element_by_id(id):
        elements = {
            "help-body": MockElement("div", id="help-body", class_name="help none"),
            "help-switch": MockElement("input", id="help-switch",  class_name="help-switch", value=False),
            "main-way": MockElement("select", id="main-way", selected_index=0),
            "main-expression": MockElement("textarea", id="main-expression"),
            "context-header": MockElement("div", id="context-header"),
            "context-switch": MockElement("input", id="context-switch", value=False),
            "context-body": MockElement("div", id="context-body", class_name="none"),
            "context-way": MockElement("select", id="context-way"),
            "context-expression": MockElement("textarea", id="context-expression"),
            "resolver-header": MockElement("div", id="resolver-header"),
            "resolver-switch": MockElement("input", id="resolver-switch", value=False),
            "resolver-body": MockElement("div", id="resolver-body", class_name="none"),
            "resolver-expression": MockElement("textarea", id="resolver-expression"),
            "frame-designation-header": MockElement("div", id="frame-designation-header"),
            "frame-designation-switch": MockElement("input", id="frame-designation-switch", value=False),
            "frame-designation-body": MockElement("div", id="frame-designation-body", class_name="none"),
            "frame-designation-expression": MockElement("textarea", id="frame-designation-expression"),
            "frame-id-header": MockElement("div", id="frame-id-header"),
            "frame-id-switch": MockElement("input", id="frame-id-switch", value=False),
            "frame-id-body": MockElement("div", id="frame-id-body",  class_name="none"),
            "frame-id-list": MockElement("select", id="frame-id-list"),
            "frame-id-expression": MockElement("input", id="frame-id-expression"),
            "results-message": MockElement("div", id="results-message"),
            "results-count": MockElement("div", id="results-count"),
            "results-frame-id": MockElement("div", id="results-frame-id"),
            "results-details": MockElement("table", id="results-details", child_nodes=[MockElement("tbody")]),
            "context-detail": MockElement("table", id="context-detail", child_nodes=[MockElement("tbody")]),
            "details-page-count": MockElement("input", id="details-page-count"),
            "execute":  MockElement("button", id="execute"),
            "focus-designated-frame":  MockElement("button", id="focus-designated-frame"),
             "get-all-frame-id":  MockElement("button", id="get-all-frame-id"),
            "show-previous-results":  MockElement("button", id="show-previous-results"),
            "focus-frame":  MockElement("button", id="focus-frame"),
            "show-all-results":  MockElement("button", id="show-all-results"),
            "open-options":  MockElement("button", id="open-options"),
            "set-style":  MockElement("button", id="set-style"),
             "reset-style":  MockElement("button", id="reset-style"),
             "set-all-style":  MockElement("button", id="set-all-style"),
              "reset-all-style":  MockElement("button", id="reset-all-style"),
            "previous-details-page": MockElement("button", id="previous-details-page"),
             "move-details-page": MockElement("button", id="move-details-page"),
              "next-details-page": MockElement("button", id="next-details-page")
        }
        return elements.get(id)
   
    def get_elements_by_class_name(class_name):
        elements = [
             MockElement("div", class_name="help none"),
             MockElement("div", class_name="help none"),
        ]
        if class_name == "help":
            return elements
        return []

    with patch('popup.window.document.getElementById', side_effect=get_element_by_id), \
         patch('popup.window.document.getElementsByClassName', side_effect=get_elements_by_class_name), \
        patch('popup.window.document.createElement', side_effect=lambda tag: MockElement(tag)):
        yield

@pytest.fixture
def popup_module():
    """Loads the module for each test."""
    import hypotez.src.webdriver.edge.extentions.try_path_1_3_5.popup.popup as popup
    return popup

@pytest.mark.asyncio
async def test_sendToActiveTab(mock_browser, popup_module):
    """Test sending message to the active tab."""
    with patch.object(mock_browser.tabs, 'query', return_value=asyncio.Future()) as mock_query, \
          patch.object(mock_browser.tabs, 'sendMessage', return_value=asyncio.Future()) as mock_send:
           mock_query.return_value.set_result([{"id": 1}])
           mock_send.return_value.set_result(None)
           
           message = {"event": "test"}
           await popup_module.sendToActiveTab(message)
           mock_query.assert_called_once_with({"active": True, "currentWindow": True})
           mock_send.assert_called_once_with(1, message, {})

@pytest.mark.asyncio
async def test_sendToSpecifiedFrame(mock_browser, mock_dom, popup_module):
    """Test sending message to specified frame."""
    with patch.object(mock_browser.tabs, 'executeScript', return_value=asyncio.Future()) as mock_execute, \
         patch.object(mock_browser.tabs, 'sendMessage', return_value=asyncio.Future()) as mock_send:
        mock_execute.return_value.set_result([False])
        mock_send.return_value.set_result(None)

        popup_module.frameIdCheckbox.checked = True
        popup_module.frameIdList.selectedOptions = [MockElement("option", attributes={"data-frame-id":"1"})]
        message = {"event":"test"}
        await popup_module.sendToSpecifiedFrame(message)
        mock_execute.assert_called()
        mock_send.assert_called_with(1,message, {"frameId": 1})


@pytest.mark.asyncio
async def test_sendToSpecifiedFrame_error_frameId_incorrect(mock_browser, mock_dom, popup_module):
    """Test sending message to specified frame."""
    with patch.object(mock_browser.tabs, 'executeScript', return_value=asyncio.Future()) as mock_execute, \
         patch.object(mock_browser.tabs, 'sendMessage', return_value=asyncio.Future()) as mock_send:
        mock_execute.return_value.set_exception(Exception("error"))
        mock_send.return_value.set_result(None)

        popup_module.frameIdCheckbox.checked = True
        popup_module.frameIdList.selectedOptions = [MockElement("option", attributes={"data-frame-id":"1"})]
        message = {"event":"test"}
        await popup_module.sendToSpecifiedFrame(message)
        assert popup_module.resultsMessage.textContent == "An error occurred. The frameId may be incorrect."

@pytest.mark.asyncio
async def test_collectPopupState(mock_dom, popup_module):
    """Test collecting the popup's state."""
    popup_module.helpCheckbox.checked = True
    popup_module.mainWay.selectedIndex = 1
    popup_module.mainExpression.value = "main_exp"
    popup_module.contextCheckbox.checked = True
    popup_module.contextWay.selectedIndex = 2
    popup_module.contextExpression.value = "context_exp"
    popup_module.resolverCheckbox.checked = True
    popup_module.resolverExpression.value = "resolver_exp"
    popup_module.frameDesignationCheckbox.checked = True
    popup_module.frameDesignationExpression.value = "frame_designation_exp"
    popup_module.frameIdCheckbox.checked = True
    popup_module.frameIdList.selectedOptions = [MockElement("option", attributes={"data-frame-id":"2"})]
    popup_module.detailsPageIndex = 3
    
    state = popup_module.collectPopupState()
    assert state["helpCheckboxChecked"] == True
    assert state["mainWayIndex"] == 1
    assert state["mainExpressionValue"] == "main_exp"
    assert state["contextCheckboxChecked"] == True
    assert state["contextWayIndex"] == 2
    assert state["contextExpressionValue"] == "context_exp"
    assert state["resolverCheckboxChecked"] == True
    assert state["resolverExpressionValue"] == "resolver_exp"
    assert state["frameDesignationCheckboxChecked"] == True
    assert state["frameDesignationExpressionValue"] == "frame_designation_exp"
    assert state["frameIdCheckboxChecked"] == True
    assert state["specifiedFrameId"] == 2
    assert state["detailsPageIndex"] == 3

@pytest.mark.asyncio
async def test_collectPopupState_manual_frameId(mock_dom, popup_module):
    """Test collecting the popup's state with manual frame id."""
    popup_module.frameIdCheckbox.checked = True
    popup_module.frameIdList.selectedOptions = [MockElement("option", attributes={"data-frame-id":"manual"})]
    popup_module.frameIdExpression.value = "3"

    state = popup_module.collectPopupState()
    assert state["specifiedFrameId"] == 3


@pytest.mark.asyncio
async def test_changeContextVisible(mock_dom, popup_module):
    """Test visibility of context body when checkbox changes."""
    popup_module.contextCheckbox.checked = True
    popup_module.changeContextVisible()
    assert not popup_module.contextBody.classList.contains("none")

    popup_module.contextCheckbox.checked = False
    popup_module.changeContextVisible()
    assert popup_module.contextBody.classList.contains("none")


@pytest.mark.asyncio
async def test_changeResolverVisible(mock_dom, popup_module):
    """Test visibility of resolver body when checkbox changes."""
    popup_module.resolverCheckbox.checked = True
    popup_module.changeResolverVisible()
    assert not popup_module.resolverBody.classList.contains("none")
    
    popup_module.resolverCheckbox.checked = False
    popup_module.changeResolverVisible()
    assert popup_module.resolverBody.classList.contains("none")

@pytest.mark.asyncio
async def test_changeFrameIdVisible(mock_dom, popup_module):
    """Test visibility of frame id body when checkbox changes."""
    popup_module.frameIdCheckbox.checked = True
    popup_module.changeFrameIdVisible()
    assert not popup_module.frameIdBody.classList.contains("none")
    
    popup_module.frameIdCheckbox.checked = False
    popup_module.changeFrameIdVisible()
    assert popup_module.frameIdBody.classList.contains("none")

@pytest.mark.asyncio
async def test_changeFrameDesignationVisible(mock_dom, popup_module):
    """Test visibility of frame designation body when checkbox changes."""
    popup_module.frameDesignationCheckbox.checked = True
    popup_module.changeFrameDesignationVisible()
    assert not popup_module.frameDesignationBody.classList.contains("none")
    
    popup_module.frameDesignationCheckbox.checked = False
    popup_module.changeFrameDesignationVisible()
    assert popup_module.frameDesignationBody.classList.contains("none")


@pytest.mark.asyncio
async def test_changeHelpVisible(mock_dom, popup_module):
    """Test visibility of help elements when checkbox changes."""
    popup_module.helpCheckbox.checked = True
    popup_module.changeHelpVisible()
    assert not popup_module.window.document.getElementsByClassName("help")[0].classList.contains("none")
    
    popup_module.helpCheckbox.checked = False
    popup_module.changeHelpVisible()
    assert popup_module.window.document.getElementsByClassName("help")[0].classList.contains("none")

@pytest.mark.asyncio
async def test_makeExecuteMessage(mock_dom, popup_module):
    """Test creation of execute message."""
    popup_module.mainWay.selectedOptions = [MockElement("option", attributes={"data-method":"main_method","data-type":"main_type"})]
    popup_module.mainExpression.value = "main_expression_value"
    popup_module.resolverCheckbox.checked = True
    popup_module.resolverExpression.value = "resolver_expression_value"

    msg = popup_module.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "main_expression_value"
    assert msg["main"]["method"] == "main_method"
    assert msg["main"]["resultType"] == "main_type"
    assert msg["main"]["resolver"] == "resolver_expression_value"
    assert  "context" not in msg

@pytest.mark.asyncio
async def test_makeExecuteMessage_with_context(mock_dom, popup_module):
    """Test creation of execute message with context."""
    popup_module.mainWay.selectedOptions = [MockElement("option", attributes={"data-method":"main_method","data-type":"main_type"})]
    popup_module.mainExpression.value = "main_expression_value"
    popup_module.resolverCheckbox.checked = True
    popup_module.resolverExpression.value = "resolver_expression_value"
    popup_module.contextCheckbox.checked = True
    popup_module.contextWay.selectedOptions = [MockElement("option", attributes={"data-method":"context_method","data-type":"context_type"})]
    popup_module.contextExpression.value = "context_expression_value"

    msg = popup_module.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "main_expression_value"
    assert msg["main"]["method"] == "main_method"
    assert msg["main"]["resultType"] == "main_type"
    assert msg["main"]["resolver"] == "resolver_expression_value"
    assert msg["context"]["expression"] == "context_expression_value"
    assert msg["context"]["method"] == "context_method"
    assert msg["context"]["resultType"] == "context_type"
    assert msg["context"]["resolver"] == "resolver_expression_value"

@pytest.mark.asyncio
async def test_makeExecuteMessage_with_frameDesignation(mock_dom, popup_module):
    """Test creation of execute message with frame designation."""
    popup_module.mainWay.selectedOptions = [MockElement("option", attributes={"data-method":"main_method","data-type":"main_type"})]
    popup_module.mainExpression.value = "main_expression_value"
    popup_module.resolverCheckbox.checked = True
    popup_module.resolverExpression.value = "resolver_expression_value"
    popup_module.frameDesignationCheckbox.checked = True
    popup_module.frameDesignationExpression.value = "frame_designation_value"

    msg = popup_module.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "main_expression_value"
    assert msg["main"]["method"] == "main_method"
    assert msg["main"]["resultType"] == "main_type"
    assert msg["main"]["resolver"] == "resolver_expression_value"
    assert msg["frameDesignation"] == "frame_designation_value"

@pytest.mark.asyncio
async def test_makeExecuteMessage_without_resolver(mock_dom, popup_module):
    """Test creation of execute message without resolver."""
    popup_module.mainWay.selectedOptions = [MockElement("option", attributes={"data-method":"main_method","data-type":"main_type"})]
    popup_module.mainExpression.value = "main_expression_value"
    popup_module.resolverCheckbox.checked = False

    msg = popup_module.makeExecuteMessage()
    assert msg["event"] == "execute"
    assert msg["main"]["expression"] == "main_expression_value"
    assert msg["main"]["method"] == "main_method"
    assert msg["main"]["resultType"] == "main_type"
    assert msg["main"]["resolver"] is None

@pytest.mark.asyncio
async def test_getSpecifiedFrameId(mock_dom, popup_module):
    """Test getting the specified frame ID."""
    popup_module.frameIdCheckbox.checked = True
    popup_module.frameIdList.selectedOptions = [MockElement("option", attributes={"data-frame-id":"123"})]
    assert popup_module.getSpecifiedFrameId() == 123

@pytest.mark.asyncio
async def test_getSpecifiedFrameId_manual_input(mock_dom, popup_module):
    """Test getting the specified frame ID from manual input."""
    popup_module.frameIdCheckbox.checked = True
    popup_module.frameIdList.selectedOptions = [MockElement("option", attributes={"data-frame-id":"manual"})]
    popup_module.frameIdExpression.value = "456"
    assert popup_module.getSpecifiedFrameId() == 456

@pytest.mark.asyncio
async def test_getSpecifiedFrameId_checkbox_not_checked(mock_dom, popup_module):
    """Test getting the specified frame ID when checkbox is not checked."""
    popup_module.frameIdCheckbox.checked = False
    assert popup_module.getSpecifiedFrameId() == 0

@pytest.mark.asyncio
async def test_execContentScript(mock_browser, popup_module):
    """Test execution of content scripts."""
    with patch.object(mock_browser.tabs, 'executeScript', return_value=asyncio.Future()) as mock_execute:
        mock_execute.return_value.set_result(None)
        await popup_module.execContentScript()
        assert mock_execute.call_count == 2
        
@pytest.mark.asyncio
async def test_sendExecute(mock_browser, mock_dom, popup_module):
    """Test the sendExecute function."""
    with patch('popup.makeExecuteMessage', return_value={"event":"test"}) as mock_make_msg, \
         patch('popup.sendToSpecifiedFrame', return_value=asyncio.Future()) as mock_send_frame:
        mock_send_frame.return_value.set_result(None)
        await popup_module.sendExecute()
        mock_make_msg.assert_called_once()
        mock_send_frame.assert_called_once_with({"event":"test"})

@pytest.mark.asyncio
async def test_handleExprEnter(mock_dom, popup_module):
    """Test the handleExprEnter function."""
    with patch('popup.sendExecute', return_value=asyncio.Future()) as mock_send:
        mock_send.return_value.set_result(None)
        event = MagicMock(key="Enter", shiftKey=False, preventDefault=MagicMock())
        popup_module.handleExprEnter(event)
        event.preventDefault.assert_called_once()
        mock_send.assert_called_once()
        
@pytest.mark.asyncio
async def test_handleExprEnter_not_enter(mock_dom, popup_module):
    """Test the handleExprEnter function."""
    with patch('popup.sendExecute', return_value=asyncio.Future()) as mock_send:
        mock_send.return_value.set_result(None)
        event = MagicMock(key="A", shiftKey=False, preventDefault=MagicMock())
        popup_module.handleExprEnter(event)
        event.preventDefault.assert_not_called()
        mock_send.assert_not_called()

@pytest.mark.asyncio
async def test_handleExprEnter_shift_enter(mock_dom, popup_module):
    """Test the handleExprEnter function."""
    with patch('popup.sendExecute', return_value=asyncio.Future()) as mock_send:
        mock_send.return_value.set_result(None)
        event = MagicMock(key="Enter", shiftKey=True, preventDefault=MagicMock())
        popup_module.handleExprEnter(event)
        event.preventDefault.assert_not_called()
        mock_send.assert_not_called()

@pytest.mark.asyncio
async def test_showDetailsPage_valid_index(mock_dom, popup_module):
    """Test showing a details page with a valid index."""
    with patch('popup.fu.updateDetailsTable', return_value=asyncio.Future()) as mock_update, \
         patch('popup.window.scrollTo', return_value=None) as mock_scroll:
        mock_update.return_value.set_result(None)
        popup_module.resultedDetails = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        popup_module.detailsPageSize = 5
        
        await popup_module.showDetailsPage(1)
        mock_update.assert_called_once()
        assert popup_module.detailsPageIndex == 1
        mock_scroll.assert_called_once()


@pytest.mark.asyncio
async def test_showDetailsPage_invalid_index(mock_dom, popup_module):
    """Test showing a details page with invalid index."""
    with patch('popup.fu.updateDetailsTable', return_value=asyncio.Future()) as mock_update:
        mock_update.return_value.set_result(None)
        popup_module.resultedDetails = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        popup_module.detailsPageSize = 5
        await popup_module.showDetailsPage(100)
        mock_update.assert_called_once()
        assert popup_module.detailsPageIndex == 1
        
@pytest.mark.asyncio
async def test_showDetailsPage_negative_index(mock_dom, popup_module):
    """Test showing a details page with invalid index."""
    with patch('popup.fu.updateDetailsTable', return_value=asyncio.Future()) as mock_update:
        mock_update.return_value.set_result(None)
        popup_module.resultedDetails = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        popup_module.detailsPageSize = 5
        await popup_module.showDetailsPage(-1)
        mock_update.assert_called_once()
        assert popup_module.detailsPageIndex == 0


@pytest.mark.asyncio
async def test_showDetailsPage_no_index(mock_dom, popup_module):
    """Test showing a details page with no index."""
    with patch('popup.fu.updateDetailsTable', return_value=asyncio.Future()) as mock_update:
        mock_update.return_value.set_result(None)
        popup_module.resultedDetails = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        popup_module.detailsPageSize = 5
        await popup_module.showDetailsPage()
        mock_update.assert_called_once()
        assert popup_module.detailsPageIndex == 0


@pytest.mark.asyncio
async def test_showDetailsPage_error(mock_dom, popup_module):
    """Test showing a details page with error."""
    with patch('popup.fu.updateDetailsTable',  side_effect=Exception("error")) as mock_update, \
        patch('popup.fu.onError', return_value=None) as mock_error:
        popup_module.resultedDetails = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        popup_module.detailsPageSize = 5
        await popup_module.showDetailsPage(1)
        mock_update.assert_called_once()
        mock_error.assert_called_once()

@pytest.mark.asyncio
async def test_showError(mock_dom, popup_module):
    """Test the showError function."""
    popup_module.showError("test_message", 1)
    assert popup_module.relatedTabId == popup_module.invalidTabId
    assert popup_module.relatedFrameId == popup_module.invalidFrameId
    assert popup_module.executionId == popup_module.invalidExecutionId
    assert popup_module.resultsMessage.textContent == "test_message"
    assert popup_module.resultedDetails == []
    assert popup_module.resultsCount.textContent == "0"
    assert popup_module.resultsFrameId.textContent == "1"

@pytest.mark.asyncio
async def test_genericListener_existing_listener(mock_browser, mock_dom, popup_module):
    """Test genericListener with existing listener."""
    mock_listener = MagicMock()
    popup_module.genericListener.listeners["test"] = mock_listener
    message = {"event": "test"}
    sender = {"tab": {"id": 1}, "frameId": 2}
    await popup_module.genericListener(message, sender)
    mock_listener.assert_called_once_with(message, sender, None)


@pytest.mark.asyncio
async def test_genericListener_non_existing_listener(mock_browser, mock_dom, popup_module):
    """Test genericListener with non existing listener."""
    message = {"event": "test"}
    sender = {"tab": {"id": 1}, "frameId": 2}
    result = await popup_module.genericListener(message, sender)
    assert result is None


@pytest.mark.asyncio
async def test_genericListener_showResultsInPopup(mock_browser, mock_dom, popup_module):
    """Test showResultsInPopup listener."""
    with patch('popup.fu.updateDetailsTable', return_value=asyncio.Future()) as mock_update, \
         patch('popup.showDetailsPage', return_value=None) as mock_show_details:
         mock_update.return_value.set_result(None)
         message = {
            "event": "showResultsInPopup",
            "executionId": 123,
            "message": "test_message",
            "main": {"itemDetails": [1, 2, 3]},
             "context": {"itemDetail": 4}
        }
         sender = {"tab": {"id": 1}, "frameId": 2}

         await popup_module.genericListener(message, sender)

         assert popup_module.relatedTabId == 1
         assert popup_module.relatedFrameId == 2
         assert popup_module.executionId == 123
         assert popup_module.resultsMessage.textContent == "test_message"
         assert popup_module.resultedDetails == [1, 2, 3]
         assert popup_module.resultsCount.textContent == "3"
         assert popup_module.resultsFrameId.textContent == "2"
         mock_update.assert_called_once()
         mock_show_details.assert_called_once_with(0)

@pytest.mark.asyncio
async def test_genericListener_showResultsInPopup_no_context(mock_browser, mock_dom, popup_module):
    """Test showResultsInPopup listener without context."""
    with patch('popup.fu.updateDetailsTable', return_value=asyncio.Future()) as mock_update, \
         patch('popup.showDetailsPage', return_value=None) as mock_show_details:
         mock_update.return_value.set_result(None)
         message = {
            "event": "showResultsInPopup",
            "executionId": 123,
            "message": "test_message",
            "main": {"itemDetails": [1, 2, 3]}
        }
         sender = {"tab": {"id": 1}, "frameId": 2}

         await popup_module.genericListener(message, sender)

         assert popup_module.relatedTabId == 1
         assert popup_module.relatedFrameId == 2
         assert popup_module.executionId == 123
         assert popup_module.resultsMessage.textContent == "test_message"
         assert popup_module.resultedDetails == [1, 2, 3]
         assert popup_module.resultsCount.textContent == "3"
         assert popup_module.resultsFrameId.textContent == "2"
         mock_update.assert_not_called()
         mock_show_details.assert_called_once_with(0)


@pytest.mark.asyncio
async def test_genericListener_restorePopupState(mock_dom, mock_browser, popup_module):
    """Test restorePopupState listener."""
    with patch('popup.sendToSpecifiedFrame', return_value=asyncio.Future()) as mock_send_frame:
       mock_send_frame.return_value.set_result(None)
       state = {
            "helpCheckboxChecked": True,
            "mainWayIndex": 1,
            "mainExpressionValue": "main_exp",
            "contextCheckboxChecked": True,
            "contextWayIndex": 2,
            "contextExpressionValue": "context_exp",
            "resolverCheckboxChecked": True,
            "resolverExpressionValue": "resolver_exp",
            "frameDesignationCheckboxChecked": True,
            "frameDesignationExpressionValue": "frame_designation_exp",
            "frameIdCheckboxChecked": True,
            "specifiedFrameId": 2,
            "detailsPageIndex": 3,
        }
       message = {"event":"restorePopupState", "state":state}

       await popup_module.genericListener(message)
       assert popup_module.helpCheckbox.checked == True
       assert popup_module.mainWay.selectedIndex == 1
       assert popup_module.mainExpression.value == "main_exp"
       assert popup_module.contextCheckbox.checked == True
       assert popup_module.contextWay.