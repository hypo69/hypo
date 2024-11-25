# background.js

## Overview

This file contains the background script for a Chrome extension. It listens for messages from content scripts and, when a message with the action `'collectData'` is received, sends collected data to a server.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`sendDataToServer`](#senddatatoserver)
* [Message Handling](#message-handling)

## Functions

### `sendDataToServer`

**Description**: This function sends collected data to a server.

**Parameters**:

- `url` (string): The URL to be included in the data.

**Returns**:
  - None

**Raises**:
  - `Error`: If the server request fails.

**Implementation Details:**

This function utilizes the `chrome.storage.local` API to retrieve stored data. If data is present, it uses the `fetch` API to send a POST request to the server. The request includes the collected data as JSON. If the request is successful, a success message is logged. If it fails, an error message is logged.


### `chrome.runtime.onMessage.addListener`

**Description**: This function listens for messages sent from other parts of the extension.

**Parameters**:

- `message` (Object): The message object containing the received data.
- `sender` (Object): Information about the sender of the message.
- `sendResponse` (Function): A function to send a response back to the sender. (Unused in this example)

**Returns**:

- `boolean`: Always returns `true` to keep the port open for future messages.

**Implementation Details**:

This listener checks if the message has the `action` property set to `'collectData'`. If it does, the `sendDataToServer()` function is called with the URL from the message.


## Message Handling

This section details how messages are handled in the background script.

**Implementation Details:**

The script listens for messages using `chrome.runtime.onMessage.addListener`. If a message containing the action 'collectData' is received, the `sendDataToServer` function is called with the URL extracted from the message.