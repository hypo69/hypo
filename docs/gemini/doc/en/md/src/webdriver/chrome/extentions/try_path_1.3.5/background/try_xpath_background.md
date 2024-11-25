# try_xpath_background.js Documentation

## Overview

This JavaScript file (`try_xpath_background.js`) contains the background script for the Try XPath Chrome extension. It handles communication between the popup and content scripts, manages persistent data, and controls the display of results.  It utilizes the browser API for interactions with other parts of the extension.


## Table of Contents

* [Overview](#overview)
* [Global Variables](#global-variables)
* [Functions](#functions)
    * [`loadDefaultCss`](#loaddefaultcss)
    * [`genericListener`](#genericlistener)
    * [`genericListener.listeners.storePopupState`](#genericlistenerlistenersstorepopupstate)
    * [`genericListener.listeners.requestRestorePopupState`](#genericlistenerlistenersrequestrestorepopupstate)
    * [`genericListener.listeners.requestInsertStyleToPopup`](#genericlistenerlistenersrequestinsertstyletopopup)
    * [`genericListener.listeners.showAllResults`](#genericlistenerlistenersfetchallresults)
    * [`genericListener.listeners.loadResults`](#genericlistenerlistenersloadresults)
    * [`genericListener.listeners.updateCss`](#genericlistenerlistenersupdatecss)
    * [`genericListener.listeners.loadOptions`](#genericlistenerlistenersloadoptions)
    * [`genericListener.listeners.requestSetContentInfo`](#genericlistenerlistenersrequestsetcontentinfo)


## Global Variables

The following variables store persistent data and configuration.

* `tx`: An alias for `tryxpath`.
* `fu`: An alias for `tryxpath.functions`.
* `popupState`: Stores the current state of the popup.
* `popupCss`: Contains CSS rules for styling the popup.
* `results`: Holds the results of the XPath query.
* `css`: Stores the CSS code to be injected.
* `attributes`: An object containing attributes used for identifying elements.


## Functions

### `loadDefaultCss`

**Description**: Fetches the default CSS file (`try_xpath_insert.css`) from the extension's resources and resolves with the retrieved text content.

**Parameters**:
   None

**Returns**:
  - `Promise<string>`: Resolves with the text content of the default CSS file.


**Raises**:
-  `fu.onError`:  If there's an error during the XMLHttpRequest.



### `genericListener`

**Description**: A listener function for messages received by the background script.

**Parameters**:
   - `message`: The message received from the content script.
   - `sender`: The sender of the message.
   - `sendResponse`: A function to send a response to the sender.

**Returns**:
  - Can return a value based on the message's event handler.


**Raises**:
-  None (Handled through the `genericListener.listeners` object)


### `genericListener.listeners.storePopupState`

**Description**: Stores the popup state received from the popup window.

**Parameters**:
- `message`: The message containing the popup state.

**Returns**:
- None


**Raises**:
- None


### `genericListener.listeners.requestRestorePopupState`

**Description**: Sends a message to restore the previously saved popup state.

**Parameters**:
- `message`: The message triggering the action.

**Returns**:
- None

**Raises**:
- None

### `genericListener.listeners.requestInsertStyleToPopup`

**Description**: Sends a message to inject CSS to the popup.

**Parameters**:
- `message`: The message triggering the action.

**Returns**:
- None

**Raises**:
- None

### `genericListener.listeners.showAllResults`

**Description**:  Displays the results in a new tab by creating a tab pointing to the show_all_results.html page.
**Parameters**:
- `message`: message containing results from the content script.
- `sender`: Details of the sender of the message (typically the content script).

**Returns**:
- None

**Raises**:
- None


### `genericListener.listeners.loadResults`

**Description**: Sends the results data back to the requesting script.

**Parameters**:
- `message`: The message received.
- `sender`: The sender of the message.
- `sendResponse`: A function to send a response to the sender.

**Returns**:
- `boolean`: `true` to indicate successful response.


**Raises**:
- None


### `genericListener.listeners.updateCss`

**Description**: Updates the CSS styles for a specific tab/frame.

**Parameters**:
- `message`: Contains a set of CSS to remove and inject.
- `sender`: Sender details (tabID and frameID).


**Returns**:
- None

**Raises**:
- `fu.onError`: If errors occur during CSS manipulation.


### `genericListener.listeners.loadOptions`

**Description**: Sends relevant options (attributes, CSS, popup CSS) back to the requester.

**Parameters**:
- `message`: The message received.
- `sender`: The sender of the message.
- `sendResponse`: A function to send a response to the sender.


**Returns**:
- `boolean`: `true` to indicate successful response.


**Raises**:
- None


### `genericListener.listeners.requestSetContentInfo`

**Description**: Sends a message to the content script to set the required content information.

**Parameters**:
- `message`: The message containing instructions.
- `sender`: The sender of the message.


**Returns**:
- None


**Raises**:
- None



## Browser Storage Changes

The code includes a listener for `browser.storage.onChanged` to dynamically update variables (`attributes`, `css`, `popupCss`) when storage changes occur.  This ensures the extension uses the most recent configuration.
```