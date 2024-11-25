# popup.js Documentation

## Overview

This JavaScript file, `popup.js`, handles the user interface and communication between the popup window and the content script running in the active tab. It manages the display of results, allows users to specify XPath queries and execute them, and handles the various UI interactions for controlling the execution process.


## Variables

This section details the variables used in the `popup.js` script, along with their purposes.

### `noneClass`

A constant string, `noneClass`, representing the class used to hide elements on the UI.

### `helpClass`

A constant string, `helpClass`, representing the class used to style the help elements.

### `invalidTabId`, `invalidExecutionId`, `invalidFrameId`

Constants representing invalid values for tab IDs, execution IDs, and frame IDs, respectively.  Used to indicate when these values are not set.


### Other Variables

A large number of variables are declared to store references to DOM elements, such as `mainWay`, `mainExpression`, and elements related to context, resolver, frame designation, frame ID, results, and details.


## Functions

### `sendToActiveTab(msg, opts)`

**Description**: Sends a message (`msg`) to the active tab.

**Parameters**:

- `msg` (object): The message to send to the content script.
- `opts` (object, optional):  Options for the message, such as `frameId`. Defaults to an empty object.


**Returns**:
- `Promise`: A promise that resolves with the response from the content script or rejects with an error.


### `sendToSpecifiedFrame(msg)`

**Description**: Sends a message to the specified frame.

**Parameters**:

- `msg` (object): The message to send to the specified frame.


**Returns**:
- `Promise`: A Promise that resolves if the message was successfully sent, or rejects with an error.

**Raises**:

- `Error`: An error is raised if the `frameId` is incorrect.


### `collectPopupState()`

**Description**: Collects the current state of the popup window.

**Returns**:
- `object`: An object containing the current state of the popup UI elements.


### `changeContextVisible()`, `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`, `changeHelpVisible()`

**Description**: Functions to control the visibility of elements related to context, resolver, frame ID, frame designation and help sections based on checkbox states.


### `makeExecuteMessage()`

**Description**: Creates a message object containing the user-provided XPath query data.

**Returns**:
- `object`: An object containing the user's XPath query, method, and other details.


### `getSpecifiedFrameId()`

**Description**: Retrieves the ID of the frame to execute XPath queries against.

**Returns**:
- `integer`: The selected frame ID.
- `0`: If frame ID is not selected.

### `execContentScript()`

**Description**: Executes JavaScript content scripts in the active tab's frame.

**Returns**:
- `Promise`: A promise that resolves once the scripts are executed.


### `sendExecute()`

**Description**: Sends the XPath query and other parameters to the content script for execution.


### `handleExprEnter(event)`

**Description**: Handles the "Enter" key press event for the input field.

**Parameters**:
- `event` (Event): The event object.


### `showDetailsPage(index)`

**Description**: Displays a page of results based on the given index.

**Parameters**:
- `index` (integer): The index of the page to display.


**Raises**:

- `Error`:  An error is raised if the input `index` is not a valid integer.


### `showError(message, frameId)`

**Description**: Displays an error message to the user.

**Parameters**:
- `message` (string): The error message to display.
- `frameId` (integer): The frame ID associated with the error.


**Functionality**: Clears previous results, resets display, and updates necessary elements.


### `genericListener(message, sender, sendResponse)`

**Description**:  A listener function for handling messages from the content script.

**Parameters**:
- `message` (object): The message received.
- `sender` (object): Information about the sender (tab, frameId).
- `sendResponse` (function): A function to send a response back to the sender.

**Functionality**: This function acts as the central hub for handling various messages received from the content script.  The `genericListener.listeners` object is used to route messages to the appropriate handlers.


### (GenericListener.listeners) `showResultsInPopup`, `restorePopupState`, `insertStyleToPopup`, `addFrameId`

**Description**: Specific listeners for handling messages related to results, restoring the popup state, injecting styles, and adding frame IDs.


## Event Listeners


This section details the event listeners for UI elements, controlling functionality based on user actions.


## DOM Manipulation

This section discusses how the code manipulates the Document Object Model (DOM) for dynamically updating and displaying UI elements. This includes setting visibility of elements, populating result lists, and managing UI states.


## Conclusion

This section summarizes the JavaScript functions, handling, and their purposes.