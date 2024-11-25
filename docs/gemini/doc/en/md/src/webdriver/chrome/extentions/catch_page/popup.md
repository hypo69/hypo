```markdown
# popup.js

## Overview

This JavaScript file handles the functionality of a Chrome extension popup. It allows users to send the URL of the active tab to a background script.

## Table of Contents

* [Functions](#functions)


## Functions

### `addEventListener`

**Description**:  Attaches an event listener to the element with the ID "sendUrlButton".  When the button is clicked, the associated function is executed.

**Parameters**:
- `event`: The event object (not used directly in this example).


**Raises**:
- No specific exceptions are raised by this method invocation.


### `alert`

**Description**: Displays an alert dialog box.

**Parameters**:
- `message`: The message to display in the alert box (string).

**Raises**:
- No specific exceptions are raised by this method invocation.


### `chrome.tabs.query`

**Description**:  Retrieves information about tabs.

**Parameters**:
- `{ active: true, currentWindow: true }`: An object specifying the criteria for selecting tabs (active and in the current window).

**Returns**:
- `tabs`: An array of tab objects that match the specified criteria.

**Raises**:
- No specific exceptions are raised by this method invocation.


### `chrome.runtime.sendMessage`

**Description**: Sends a message to the background script.

**Parameters**:
- `{ action: "sendUrl", url: activeTabUrl }`: An object containing the message data.
    - `action`: The action to perform ("sendUrl").
    - `url`: The URL of the active tab.
- `(response)`: Callback function that is executed when a response is received.  This function accepts the response object.


**Returns**:
- The value returned from the callback function (e.g., the response object from the background script).

**Raises**:
- No specific exceptions are raised by this method invocation.