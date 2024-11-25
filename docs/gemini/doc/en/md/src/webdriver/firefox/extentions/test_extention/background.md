# background.js

## Overview

This JavaScript file acts as the background script for a browser extension.  It listens for clicks on the browser action and injects the `contentScript.js` file into the current tab.

## Table of Contents

* [Browser Action Click Listener](#browser-action-click-listener)


## Browser Action Click Listener

### `browser.browserAction.onClicked.addListener`

**Description**: This listener function is called whenever the browser action icon is clicked.

**Parameters**:
- `tab` (Object): An object containing information about the current tab, including `tab.id`.

**Functionality**:
- Executes the `browser.scripting.executeScript` function to inject `contentScript.js` into the specified tab.

**Code Snippet**:

```javascript
browser.browserAction.onClicked.addListener((tab) => {
    browser.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["contentScript.js"],
    });
});
```

**Dependencies**:
- `browser.scripting.executeScript`: A function for injecting JavaScript code into a specific tab.