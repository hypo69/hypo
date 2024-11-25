# try_xpath_content.js

## Overview

This JavaScript file, `try_xpath_content.js`, implements the content script for the "Try XPath" browser extension. It handles various interactions with the webpage, including XPath evaluation, focusing elements, and updating styles.  It communicates with the background script via browser.runtime.sendMessage.


## Variables

### `tx`

**Description**:  An alias for `tryxpath`.

### `fu`

**Description**: An alias for `tryxpath.functions`.

### `tx.isContentLoaded`

**Description**: A boolean flag to prevent multiple execution of the script.


### `dummyItem`, `dummyItems`, `invalidExecutionId`

**Description**: Dummy values used as placeholders.


### `styleElementHeader`

**Description**: String containing a comment for the inserted style element.

### `attributes`

**Description**: An object containing attribute names used to store and retrieve information about elements, contexts, focus, and frames.

### `prevMsg`

**Description**:  Stores the previous message to be sent to the popup.

### `executionCount`

**Description**: A counter for the number of execution cycles.

### `inBlankWindow`

**Description**: A boolean flag indicating whether the script is running in a blank window.

### `currentDocument`

**Description**: The current document being processed.


### `contextItem`

**Description**: The current context item.

### `currentItems`

**Description**: An array of currently selected items.

### `focusedItem`

**Description**: The currently focused item.

### `focusedAncestorItems`

**Description**: An array of ancestor elements of the focused item.

### `currentCss`

**Description**: The currently applied CSS.

### `insertedStyleElements`

**Description**: A Map to store the inserted style elements.

### `expiredCssSet`

**Description**: An object to store CSS that has expired and needs to be removed.

### `originalAttributes`

**Description**: A Map to store the original attributes of elements.


## Functions

### `setAttr`

**Description**: Sets an attribute to an item.

**Parameters**:
- `attr` (string): The attribute name to set.
- `value` (string): The value of the attribute.
- `item` (object): The item to set the attribute on.

**Returns**:
-  (void): No return value.

**Raises**:
- (None)


### `setIndex`

**Description**: Sets an attribute to a list of items.

**Parameters**:
- `attr` (string): The attribute name to set.
- `items` (array): The list of items.

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `isFocusable`

**Description**: Checks if an item is focusable.

**Parameters**:
- `item` (object): The item to check.

**Returns**:
- `boolean`: True if the item is focusable, otherwise false.

**Raises**:
- (None)

### `focusItem`

**Description**:  Focuses a specified item and its ancestors.

**Parameters**:
- `item` (object): The item to focus.

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `setMainAttrs`

**Description**: Sets attributes related to the main context.

**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `restoreAttrs`

**Description**: Restores original attribute values to elements.

**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `resetPrev`

**Description**: Resets previous message and counters.

**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `makeTypeStr`

**Description**: Creates a string representation of the result type.

**Parameters**:
- `resultType` (number): The result type.

**Returns**:
- string: The string representation of the result type.

**Raises**:
- (None)


### `updateCss`

**Description**: Sends a message to the background script to update CSS.

**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `getFrames`

**Description**: Extracts the frame indices from a specification string.

**Parameters**:
- `spec` (string): The frame specification.

**Returns**:
- array: An array of frame indices.

**Raises**:
- `Error`: If the specification is invalid.


### `parseFrameDesignation`

**Description**: Parses a frame designation string to an array of indices.


**Parameters**:
- `frameDesi` (string): The frame designation string.

**Returns**:
- array: An array of frame indices.

**Raises**:
- `Error`: If the specification is invalid.



### `traceBlankWindows`

**Description**: Checks if a sequence of frames are blank windows.

**Parameters**:
- `desi` (array): An array of frame indices.
- `win` (optional): The current window object.

**Returns**:
- object: An object containing `windows`, `failedWindow`, and `success`.

**Raises**:
- (None)


### `handleCssChange`

**Description**: Handles changes to the CSS.

**Parameters**:
- `newCss` (string): The new CSS.

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `findFrameByMessage`

**Description**: Finds the frame element corresponding to a message.


**Parameters**:
- `event` (object): The message event object.
- `win` (object): The current window object.

**Returns**:
- object: The frame element or null if not found.


**Raises**:
- (None)


### `setFocusFrameListener`

**Description**: Sets a listener for frame focusing events.

**Parameters**:
- `win` (object): The window object.
- `isBlankWindow` (boolean): A flag to specify if the window is blank.


**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `initBlankWindow`


**Description**: Initializes a blank window.

**Parameters**:
- `win` (object): The window object.

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `findStyleParent`

**Description**: Finds the parent element to insert the style element.

**Parameters**:
- `doc` (object): The document object.

**Returns**:
- object: The parent element (head or body), or null.


**Raises**:
- (None)



### `updateStyleElement`

**Description**: Updates the style element with the current CSS.

**Parameters**:
- `doc` (object): The document object.

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `updateAllStyleElements`

**Description**: Updates all style elements with the current CSS.


**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `removeStyleElement`

**Description**: Removes a style element from the document.


**Parameters**:
- `doc` (object): The document object.

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `removeAllStyleElements`


**Description**: Removes all style elements.


**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `createResultMessage`

**Description**: Creates a default result message object.

**Parameters**:
- (None)

**Returns**:
- object: The default result message.

**Raises**:
- (None)


### `genericListener`

**Description**:  A listener for messages from the background script.

**Parameters**:
- `message` (object): Message data.
- `sender` (object): Sender information.
- `sendResponse` (function): Function to send response.


**Returns**:
- (boolean): True if the message was handled.

**Raises**:
- (None)



### `genericListener.listeners`

**Description**: Object containing specific event listeners.


**Parameters**:
- (None)

**Returns**:
- Object

**Raises**:
- (None)



### `genericListener.listeners.setContentInfo`


**Description**: Handles the message to set content info.

**Parameters**:
- `message` (object): The message to handle.


**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `genericListener.listeners.execute`


**Description**: Executes the XPath expression.

**Parameters**:
- `message` (object): The message to handle.
- `sender` (object): The sender of the message.

**Returns**:
- (void): No return value.

**Raises**:
- `Error`: If an error occurs during frame/context processing.



### `genericListener.listeners.focusItem`


**Description**: Focuses the item at the specified index.


**Parameters**:
- `message` (object): Message containing execution ID and index.

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `genericListener.listeners.focusContextItem`


**Description**: Focuses the context item.

**Parameters**:
- `message` (object): Message to handle.

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `genericListener.listeners.focusFrame`


**Description**: Focuses a frame.

**Parameters**:
- `message` (object): Message containing frame designation.


**Returns**:
- (void): No return value.

**Raises**:
- `Error`: If a frame does not exist.



### `genericListener.listeners.requestShowResultsInPopup`

**Description**:  Sends the previous message object to the popup.


**Parameters**:
- (None)

**Returns**:
- (void): No return value.


**Raises**:
- (None)


### `genericListener.listeners.requestShowAllResults`

**Description**:  Sends a message to show all results.


**Parameters**:
- (None)

**Returns**:
- (void): No return value.


**Raises**:
- (None)

### `genericListener.listeners.resetStyle`

**Description**: Resets style and attributes.


**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `genericListener.listeners.setStyle`


**Description**: Sets the style.

**Parameters**:
- (None)

**Returns**:
- (void): No return value.

**Raises**:
- (None)


### `genericListener.listeners.finishInsertCss`


**Description**: Finishes inserting CSS.

**Parameters**:
- `message` (object): The message to handle.

**Returns**:
- (void): No return value.


**Raises**:
- (None)



### `genericListener.listeners.finishRemoveCss`


**Description**: Finishes removing CSS.

**Parameters**:
- `message` (object): The message to handle.


**Returns**:
- (void): No return value.

**Raises**:
- (None)

## Browser Event Listeners

### `browser.storage.onChanged`

**Description**: Listener for changes in browser storage.


**Parameters**:
- `changes` (object): Details of changes.

**Returns**:
- (void): No return value.

**Raises**:
- (None)



### `window.addEventListener`

**Description**: Listener for message events from other windows.

**Parameters**:
- `event` (object): Message event data.

**Returns**:
- (void): No return value.

**Raises**:
- (None)