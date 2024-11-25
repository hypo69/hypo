# try_xpath_background.js

## Overview

This JavaScript file (`try_xpath_background.js`) handles background logic for the Try XPath extension. It manages communication with content scripts, stores popup state, loads CSS, and interacts with browser APIs for tasks like sending messages, inserting CSS, and managing storage.


## Table of Contents

- [Overview](#overview)
- [Global Variables](#global-variables)
- [Functions](#functions)
    - [`loadDefaultCss`](#loaddefaultcss)
    - [`genericListener`](#genericlistener)
    - [`storePopupState`](#storepopupstate)
    - [`requestRestorePopupState`](#requestrestorepopupstate)
    - [`requestInsertStyleToPopup`](#requestinsertstyletopopup)
    - [`showAllResults`](#showallresults)
    - [`loadResults`](#loadresults)
    - [`updateCss`](#updatecss)
    - [`loadOptions`](#loadoptions)
    - [`requestSetContentInfo`](#requestsetcontentinfo)
- [Event Handling](#event-handling)
- [Storage Handling](#storage-handling)



## Global Variables

```javascript
var tx = tryxpath;
var fu = tryxpath.functions;
var popupState = null;
var popupCss = "body{width:367px;height:auto;}";
var results = {};
var css = "";
var attributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
};
```

**Description**: These variables store essential data for the extension, such as the alias `tx` and `fu` to the Try XPath object, the current popup state, CSS styles, results data, and attributes to be used for the selection process.


## Functions


### `loadDefaultCss`

**Description**: Loads default CSS from a file.

**Returns**:
- `Promise<string>`: Resolves with the loaded CSS content if successful.

**Error Handling**:
- Handles potential errors during the `XMLHttpRequest` request with a catch block (`fu.onError`).


### `genericListener`

**Description**:  A listener function that handles messages sent from content scripts.

**Parameters**:
- `message`: (object) The message sent by the content script.
- `sender`: (object) The sender of the message (e.g., a tab).
- `sendResponse`: (function) A function to send a response back to the content script.


**Returns**:
- (boolean | void): Depending on the specific message handler, may return a boolean to indicate whether asynchronous operations are involved.


**Error Handling**:
- Uses a `catch` block to handle any errors during asynchronous operations within the listener.



### `storePopupState`

**Description**: Stores the popup state received from a message.

**Parameters**:
- `message` (object): The message containing the popup state.


### `requestRestorePopupState`

**Description**: Sends a message to restore the popup state.

**Parameters**:
- `message` (object): The message containing information to restore the popup state.


### `requestInsertStyleToPopup`

**Description**: Sends a message to the popup to insert the `popupCss`.

**Parameters**:
- `message` (object): The message containing the `popupCss`.


### `showAllResults`

**Description**: Displays the results in a new tab.

**Parameters**:
- `message` (object): Contains the results to be displayed.
- `sender` (object): Information about the sender of the message.


### `loadResults`

**Description**: Returns the current results.

**Parameters**:
- `message` (object): Message containing information about the current results to be returned.
- `sender` (object): Information about the sender of the message.
- `sendResponse` (function): Function to send a response back to the sender.


**Returns**:
- `boolean`: True, to indicate asynchronous operation.


### `updateCss`

**Description**:  Updates the CSS in a tab.

**Parameters**:
- `message` (object): Contains the CSS data to be updated and expired CSS to remove.
- `sender` (object): Information about the sender of the message.


**Error Handling**:
- Uses a `.catch(fu.onError)` to handle potential errors during the insertion and removal of CSS.


### `loadOptions`

**Description**: Sends the attributes, CSS, and popup CSS to the content script.


**Parameters**:
- `message` (object): Message containing data to load the options.
- `sender` (object): Information about the sender of the message.
- `sendResponse` (function): Function to send a response back to the sender.


**Returns**:
- `boolean`: True, to indicate asynchronous operation.


### `requestSetContentInfo`

**Description**: Sends a message to set content info.

**Parameters**:
- `message` (object):  Contains the attributes to be set in the content script.
- `sender` (object): Information about the sender of the message.




## Event Handling

The file uses `browser.runtime.onMessage.addListener` to listen for messages from content scripts and other parts of the extension.


## Storage Handling

- The file uses `browser.storage.onChanged.addListener` to react to changes in storage.
- It uses `browser.storage.sync.get` to retrieve values from sync storage, handling cases where CSS is not present and loading the default CSS.