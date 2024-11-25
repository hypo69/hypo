# popup.js Documentation

## Overview

This JavaScript file (`popup.js`) handles the user interface and communication with the background script and content scripts for the Try XPath extension. It manages various elements in the popup, including input fields, checkboxes, and tables, to allow users to query XPath expressions on web pages and display results.  It handles sending and receiving messages to control the display and update of data.


## Variables

This section lists the important variables used in the script.

* `tx`: Alias for `tryxpath`.
* `fu`: Alias for `tryxpath.functions`.
* `noneClass`, `helpClass`: CSS classes used for visibility control.
* `invalidTabId`, `invalidExecutionId`, `invalidFrameId`: Constants for invalid IDs.
* `mainWay`, `mainExpression`, `contextCheckbox`, ...:  Variables representing elements in the popup UI for user input and selection.
* `resultedDetails`: Array holding the results of the XPath query.
* `detailsPageSize`: Number of results per page in the results table.
* `detailsPageIndex`: Current page index for displaying results.
* `relatedTabId`, `relatedFrameId`, `executionId`: Variables storing context information from the background script regarding active tab and frame.


## Functions

### `sendToActiveTab(msg, opts)`

**Description**: Sends a message (`msg`) to the active tab. Optionally includes additional options (`opts`).

**Parameters**:
- `msg` (Object): The message to be sent to the active tab.
- `opts` (Optional[Object], optional): Additional options for the message. Defaults to an empty object.


**Returns**:
- `Promise`: A promise resolving to the response from the active tab.

**Raises**:
- `Error`: An error occurs during communication with the active tab.


### `sendToSpecifiedFrame(msg)`

**Description**: Sends a message to the specified frame.

**Parameters**:
- `msg` (Object): The message to be sent.


**Returns**:
- `Promise`: A promise.

**Raises**:
- `Error`: An error related to an incorrect frame ID.


### `collectPopupState()`

**Description**: Collects the current state of the popup UI elements into an object.

**Parameters**: None.

**Returns**:
- `Object`: An object containing the state of the popup UI.

**Raises**: None


### `changeContextVisible()`

**Description**: Toggles the visibility of the context-related UI elements based on the `contextCheckbox` state.

**Parameters**: None.

**Returns**: None.

**Raises**: None.


### `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`

**Description**: Toggle the visibility of corresponding UI elements based on the related checkbox state.

**Parameters**: None.

**Returns**: None.

**Raises**: None.


### `changeHelpVisible()`

**Description**: Toggles the visibility of help content elements based on the `helpCheckbox` state.

**Parameters**: None.

**Returns**: None.

**Raises**: None.


### `makeExecuteMessage()`

**Description**: Constructs a message object to be sent to the content script, encapsulating the user's XPath query parameters and options.

**Parameters**: None.

**Returns**:
- `Object`: The message object containing query parameters.

**Raises**: None.


### `getSpecifiedFrameId()`

**Description**: Retrieves the specified frame ID from user input.

**Parameters**: None.

**Returns**:
- `number`: The integer frame ID.

**Raises**: None


### `execContentScript()`

**Description**: Executes JavaScript scripts in the content script context within the active tab/frame.

**Parameters**: None.

**Returns**:
- `Promise`: Resolves when the content script execution is complete.

**Raises**:
- `Error`: Any error during the execution of content scripts.


### `sendExecute()`

**Description**: Sends the constructed execution message to the content script for query processing.

**Parameters**: None.

**Returns**: None.

**Raises**: None


### `showDetailsPage(index)`

**Description**: Displays a portion of the results in the results table, handling pagination.

**Parameters**:
- `index` (int): Page index to display.

**Returns**: None.

**Raises**:
- `Error`: An error related to pagination.


### `showError(message, frameId)`

**Description**: Displays an error message to the user.

**Parameters**:
- `message` (str): Error message to display.
- `frameId` (str): Related frameId to include in the error.

**Returns**: None.

**Raises**: None


### `genericListener(message, sender, sendResponse)`

**Description**: General message listener for handling various events from the background script and content scripts.

**Parameters**:
- `message`: Message received from sender
- `sender`: Sender of the message
- `sendResponse`: Function to send a response.

**Returns**: `boolean` - whether or not to await response from a listener


###  `genericListener.listeners.{event_name}`

**Description**: Event handlers for different messages.  Defined as inner functions to ensure that the correct context (`genericListener.listeners`) is used for event handling.


**Example (genericListener.listeners.showResultsInPopup):** Processes the results from the background script, populating the results table, and handling pagination.


**Example (genericListener.listeners.restorePopupState):** Restores the popup state from a persisted state.


**Example (genericListener.listeners.insertStyleToPopup):** Inserts CSS styles into the popup.


**Example (genericListener.listeners.addFrameId):** Adds frame IDs to a dropdown list in the popup.

**Parameters**:  Vary according to the event handler (`message`, `sender`).

**Returns**: Vary according to the event handler.


## Event Listeners

This section describes the event listeners used to handle user interactions and messages.  They call functions to update the UI, execute queries, and manage communication with other scripts.


## Further Information


The `tryxpath` module or other related modules contain further details about the functionality and underlying logic. The complete set of available methods, parameters, and exception handling is available in those modules.