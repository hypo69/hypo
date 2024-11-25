# try_xpath_content.js

## Overview

This JavaScript file, `try_xpath_content.js`, handles the Try XPath content script logic.  It manages the interaction with the browser extension (Try XPath popup), dynamically inserting and updating style elements, focusing elements based on XPath expressions, and handling various messages between the content script and the popup.


## Variables

### `tx`

**Description**: An alias for `tryxpath` likely referencing a global object or namespace.

### `fu`

**Description**: An alias for `tryxpath.functions`, likely containing utility functions for handling XPath results and DOM elements.


### `tx.isContentLoaded`

**Description**: A flag to prevent multiple executions of the content script.

### `dummyItem`, `dummyItems`, `invalidExecutionId`


**Description**:  These are placeholder/default values used for various data structures; e.g., representing empty or unavailable item data.


### `styleElementHeader`

**Description**: This string is prepended to the dynamically inserted style element. It serves as a comment for debugging or browser add-on identification.



### `attributes`

**Description**: A JavaScript object that stores the attributes used for adding custom attributes to elements.


### `prevMsg`, `executionCount`


**Description**:  Variables tracking the previous message sent and the execution count, likely used for managing multiple requests.


### `inBlankWindow`, `currentDocument`, `contextItem`, `currentItems`, `focusedItem`, `focusedAncestorItems`



**Description**:  These variables store state related to the current document, selected context, focused elements, and other critical information during the XPath evaluation process.

### `currentCss`, `insertedStyleElements`, `expiredCssSet`, `originalAttributes`

**Description**: These variables collectively manage the styling and temporary attribute preservation related to dynamic CSS insertion and handling potential CSS changes.


## Functions

### `setAttr(attr, value, item)`

**Description**: Sets a custom attribute to an element.


**Parameters**:

- `attr` (string): The name of the custom attribute.
- `value` (string): The value of the custom attribute.
- `item` (object): The DOM element to which the attribute should be applied.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions


### `setIndex(attr, items)`

**Description**: Sets custom attributes to a collection of elements.

**Parameters**:

- `attr` (string): The name of the custom attribute.
- `items` (array): An array of DOM elements.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.

### `isFocusable(item)`

**Description**: Checks if an item is focusable (usually an element or an attribute).


**Parameters**:

- `item` (object): The item to check.


**Returns**:

- `boolean`: True if the item is focusable, False otherwise.


### `focusItem(item)`

**Description**:  Focuses a specific item in the DOM and updates relevant variables.


**Parameters**:

- `item` (object): The DOM element to focus.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.

### `setMainAttrs()`

**Description**: Sets attributes related to the main context item in the execution.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.

### `restoreAttrs()`

**Description**: Resets custom attributes to their original values.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.


### `resetPrev()`

**Description**: Resets the previous message and various state variables.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.


### `makeTypeStr(resultType)`

**Description**: Creates a string representation of a result type.  Handles numbers, potentially for formatting or type identification.

**Parameters**:

- `resultType` (number or string): The result type.


**Returns**:

- `string`: The formatted string representation.


### `updateCss()`


**Description**: Sends a message to the browser extension to update the style element.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.


### `getFrames(spec)`

**Description**: Parses and returns an array of frame indices.

**Parameters**:

- `spec` (string): The string representation of the frame indices.


**Returns**:

- array: Array of frame indices, or throws an `Error` for invalid input.


**Raises**:

- `Error`: If the input `spec` is not a valid number array.


### `parseFrameDesignation(frameDesi)`

**Description**: Parses a frame designation string into an array of frame indices.

**Parameters**:

- `frameDesi` (string): The frame designation string.

**Returns**:

- `array`: Array of frame indices, or throws an `Error` for invalid input.


**Raises**:

- `Error`: If the input `frameDesi` is not a valid frame designation.


### `traceBlankWindows(desi, win)`

**Description**: Traces blank windows based on a given frame designation.


**Parameters**:

- `desi` (array): Array of frame indices.
- `win` (object): The current window object.


**Returns**:

- Object: An object containing either success or failure information about the tracing and the failed window object.


### `handleCssChange(newCss)`

**Description**: Manages changes to the CSS.


**Parameters**:

- `newCss` (string): The new CSS.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.


### `findFrameByMessage(event, win)`


**Description**: Locates a specific frame element based on a message.


**Parameters**:

- `event` (object): The message event.
- `win` (object): The current window.


**Returns**:

- Object: The frame element, or null if not found.

### `setFocusFrameListener(win, isBlankWindow)`


**Description**: Sets a message listener for focusing frames.


**Parameters**:

- `win` (object): The window object.
- `isBlankWindow` (boolean): Flag indicating if it's a blank window.


**Raises**:

- None explicitly, but underlying functions in `fu` may raise exceptions.


### `initBlankWindow(win)`

**Description**: Initializes the content script for a blank window.

**Parameters**:

- `win` (object): The blank window.



### `findStyleParent(doc)`

**Description**: Finds the suitable parent node for inserting a style element.

**Parameters**:

- `doc` (object): The HTML document object.



**Returns**:

- object: The appropriate parent node (head or body).


### `updateStyleElement(doc)`

**Description**: Updates the dynamically inserted style element with the current CSS.

**Parameters**:

- `doc` (object): The HTML document object.



### `updateAllStyleElements()`


**Description**: Updates all dynamically inserted style elements with the current CSS.


### `removeStyleElement(doc)`

**Description**: Removes the dynamically inserted style element.

**Parameters**:

- `doc` (object): The HTML document object.


### `removeAllStyleElements()`

**Description**: Removes all dynamically inserted style elements.


### `createResultMessage()`

**Description**: Creates a default result message object.

**Returns**:

- object: The result message object.


### `genericListener(message, sender, sendResponse)`

**Description**: A generic message listener that calls appropriate handlers based on the message type.


**Parameters**:

- `message` (object): The message received.
- `sender` (object): The sender object.
- `sendResponse` (function): The function to send a response.


### `genericListener.listeners`

**Description**: An object to store event handlers for the `genericListener`.


###  `genericListener.listeners.setContentInfo`,
`genericListener.listeners.execute`,
`genericListener.listeners.focusItem`,
`genericListener.listeners.focusContextItem`,
`genericListener.listeners.focusFrame`,
`genericListener.listeners.requestShowResultsInPopup`,
`genericListener.listeners.requestShowAllResults`,
`genericListener.listeners.resetStyle`,
`genericListener.listeners.setStyle`,
`genericListener.listeners.finishInsertCss`,
`genericListener.listeners.finishRemoveCss`

**Description**: These are event handlers within the `genericListener` object, each handling a specific type of message from the extension.


## Event Handling

- The script listens for messages from the browser extension and handles various requests like executing XPath expressions, focusing elements, updating CSS, etc.



## Browser Storage Handling

- The script listens for changes in browser storage, specifically for the `attributes` and `css` storage, updating variables accordingly.