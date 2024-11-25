# try_xpath_background.js

## Overview

This JavaScript file handles background logic for the Try XPath extension. It manages communication with the popup, stores state, and interacts with browser APIs for injecting CSS, retrieving and sending results, and handling storage changes.  It uses `browser` API for interactions with the browser context.


## Variables

### `tx`

**Description**: Alias for `tryxpath`.

### `fu`

**Description**: Alias for `tryxpath.functions`.

### `popupState`

**Description**: Stores the current state of the popup, potentially for persistence.

### `popupCss`

**Description**: String containing CSS styles for the popup.

### `results`

**Description**: Object containing results data.

### `css`

**Description**: String containing CSS styles to be injected.

### `attributes`

**Description**: Object containing custom attributes used in selectors.


## Functions

### `loadDefaultCss`

**Description**: Fetches default CSS from a file located at `/css/try_xpath_insert.css` and resolves the response.

**Returns**:
- `Promise<string>`: The response text of the CSS file.

**Raises**:
- `Error`: Any error during the XMLHttpRequest.


### `genericListener`

**Description**:  A generic listener function that handles incoming messages from different parts of the extension.

**Parameters**:
- `message` (Object): The message object.
- `sender` (Object):  The sender of the message.
- `sendResponse` (function): A function to send a response to the sender.

**Returns**:
- `boolean`: Usually `undefined`, but `true` is returned to indicate that the `loadResults` function is listening for asynchronous response.

**Raises**:
- `Error`: if listener is not found.


### `genericListener.listeners.storePopupState`

**Description**: Stores the provided popup state.

**Parameters**:
- `message` (Object): Message containing the `state` property.


### `genericListener.listeners.requestRestorePopupState`

**Description**: Sends the current popup state to the requesting part of the extension.


### `genericListener.listeners.requestInsertStyleToPopup`

**Description**: Sends the `popupCss` to the popup.


### `genericListener.listeners.showAllResults`

**Description**: Handles showing all results in a new tab.

**Parameters**:
- `message` (Object): The message object.
- `sender` (Object): The sender of the message.


### `genericListener.listeners.loadResults`

**Description**: Sends the results data to the caller.

**Parameters**:
- `message` (Object): The message object.
- `sender` (Object): The sender of the message.
- `sendResponse` (function): A function to send a response.

**Returns**:
- `boolean`: `true` to indicate asynchronous response.


### `genericListener.listeners.updateCss`

**Description**: Handles updating CSS in the active tab(s).

**Parameters**:
- `message` (Object): Contains information about the CSS to be updated (including expired CSS).
- `sender` (Object): Sender information.


### `genericListener.listeners.loadOptions`

**Description**: Sends necessary options (attributes, CSS, popup CSS) to the caller.

**Parameters**:
- `message` (Object): The message object.
- `sender` (Object): The sender of the message.
- `sendResponse` (function): A function to send a response.

**Returns**:
- `boolean`: `true` to indicate asynchronous response.


### `genericListener.listeners.requestSetContentInfo`

**Description**: Sends the content information to the requesting tab.

**Parameters**:
- `message` (Object): Message to retrieve content info.
- `sender` (Object): Sender information.



## Event Listeners

### `browser.storage.onChanged`

**Description**: Listens for changes to storage items. Updates global variables based on the changes.



## Initialization

### `browser.storage.sync.get`

**Description**: Retrieves the values of `attributes`, `css`, and `popupCss` from browser storage. If `css` is `null`, it fetches the default CSS using `loadDefaultCss`.

**Parameters**:
- `options` (Object): An object containing the keys to retrieve from storage.

**Returns**:
- `Promise<Object>`: A promise that resolves to an object containing the retrieved values.


## Error Handling

The code uses `fu.onError` for handling errors.