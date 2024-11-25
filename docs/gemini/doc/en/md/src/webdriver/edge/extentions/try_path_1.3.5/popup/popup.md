# popup.js Documentation

## Overview

This JavaScript file handles the logic for the popup window of the `try_path_1.3.5` extension.  It manages user input, communication with the content scripts, display of results, and state persistence.  It utilizes the `browser` API for interacting with the browser extension's context.


## Table of Contents

* [Functions](#functions)


## Functions

### `sendToActiveTab`

**Description**: Sends a message to the active tab.

**Parameters**:
- `msg` (Object): The message to send.
- `opts` (Optional[Object], optional): Additional options for the message. Defaults to an empty object.

**Returns**:
- `Promise`: A promise that resolves with the response from the active tab.  Returns `Promise`


**Raises**:
- `TypeError`: Incorrect input type.


### `sendToSpecifiedFrame`

**Description**: Sends a message to a specified frame within the active tab.

**Parameters**:
- `msg` (Object): The message to send.

**Returns**:
- `Promise`: A promise that resolves when the message is successfully sent or an error occurs.  Returns `Promise`.


**Raises**:
- `TypeError`: Incorrect input type.


### `collectPopupState`

**Description**: Collects the current state of the popup elements.

**Parameters**: None

**Returns**:
- `Object`: An object containing the current state of popup elements.


**Raises**:
- `TypeError`: Incorrect input type.


### `changeContextVisible`

**Description**: Shows or hides the context section based on the context checkbox state.

**Parameters**: None

**Returns**: None


**Raises**: None


### `changeResolverVisible`

**Description**: Shows or hides the resolver section based on the resolver checkbox state.

**Parameters**: None

**Returns**: None


**Raises**: None


### `changeFrameIdVisible`

**Description**: Shows or hides the frame ID section based on the frame ID checkbox state.

**Parameters**: None

**Returns**: None


**Raises**: None


### `changeFrameDesignationVisible`

**Description**: Shows or hides the frame designation section based on the frame designation checkbox state.

**Parameters**: None

**Returns**: None


**Raises**: None


### `changeHelpVisible`

**Description**: Shows or hides the help sections based on the help checkbox state.

**Parameters**: None

**Returns**: None


**Raises**: None


### `makeExecuteMessage`

**Description**: Creates a message object containing the user's input for execution.

**Parameters**: None

**Returns**:
- `Object`: A message object containing the execution parameters.


**Raises**: None


### `getSpecifiedFrameId`

**Description**: Extracts and handles the selected frame ID from the UI elements.

**Parameters**: None

**Returns**:
- `Number`: The frame ID to use for execution, defaults to 0 if frame id is unchecked.


**Raises**: None


### `execContentScript`

**Description**: Executes scripts in the current tab's context.

**Parameters**: None

**Returns**:
- `Promise`: A promise that resolves after executing content scripts or if an error occurs. Returns `Promise`


**Raises**:
- `TypeError`: Incorrect input type.


### `sendExecute`

**Description**: Sends an execution request to the content script.

**Parameters**: None

**Returns**: None


**Raises**: None


### `handleExprEnter`

**Description**: Handles the 'Enter' key press on the expression input field.

**Parameters**:
- `event` (Event): The key press event.

**Returns**: None


**Raises**: None


### `showDetailsPage`

**Description**: Displays a page of results from the search.

**Parameters**:
- `index` (Integer): The page index to show.

**Returns**: None


**Raises**: None


### `showError`

**Description**: Displays an error message and resets the result display.

**Parameters**:
- `message` (String): The error message to display.
- `frameId` (String): The frame ID associated with the error.

**Returns**: None


**Raises**: None


### `genericListener`

**Description**: A message listener for handling various messages from the content script.

**Parameters**:
- `message` (Object): The message received.
- `sender` (Object): The sender of the message.
- `sendResponse` (Function): A function to send a response.

**Returns**:
- Boolean: Indicates whether the function handles a specific message type.


**Raises**: None


### `genericListener.listeners.showResultsInPopup`

**Description**: Handles messages containing the search results.

**Parameters**:
- `message` (Object): The message containing search results.
- `sender` (Object): Information about the sender.


**Returns**: None

**Raises**: None


### `genericListener.listeners.restorePopupState`

**Description**: Restores the popup state from a saved state.

**Parameters**:
- `message` (Object): The message containing the saved state.

**Returns**: None

**Raises**: None


### `genericListener.listeners.insertStyleToPopup`

**Description**: Injects custom CSS into the popup.


**Parameters**:
- `message` (Object): The message containing the CSS to inject.


**Returns**: None

**Raises**: None



### `genericListener.listeners.addFrameId`

**Description**: Adds a frame ID to the frame list in the popup.

**Parameters**:
- `message` (Object): The message containing the frame ID.
- `sender` (Object): Information about the sender.

**Returns**: None

**Raises**: None