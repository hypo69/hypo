# show_all_results.js

## Overview

This JavaScript file handles the display of search results from the TryXPath extension.  It populates various HTML elements with data from the results object, including message, title, URL, context information, and main search results.  It also provides functionality for downloading the results in text format and focusing on specific search items.


## Functions

### `showAllResults`

**Description**: This function populates the HTML elements with the provided `results` object. It handles both context and main results, updating the corresponding sections of the page.

**Parameters**:
- `results` (object): The object containing the search results data.  Must contain `message`, `title`, `href`, `frameId`, `context` (optional), and `main` properties.

**Raises**:
- `fu.onError`: In case any error occurs during the `updateDetailsTable` call.


### `makeTextDownloadUrl`

**Description**: Creates a download URL for a given text content.

**Parameters**:
- `text` (string): The text content to be downloaded.

**Returns**:
- `string`: The URL for the download.


### `makeInfoText`

**Description**: Generates text suitable for exporting, containing information about the results and their context.

**Parameters**:
- `results` (object): The object containing the search results.

**Returns**:
- `string`: Formatted text containing the result data.


### `makeConvertedInfoText`

**Description**: Generates text suitable for exporting, containing information about the results and their context. This version stringifies JSON values for easier reading in a text file.

**Parameters**:
- `results` (object): The object containing the search results.

**Returns**:
- `string`: Formatted text containing the result data.



## Event Handling

### Window Load Event Listener

**Description**:  This event listener is triggered when the window finishes loading. It sends a message to the browser to request search results. On receiving results it populates the UI, creates download links, and sets up event listeners for context and item clicks.

**Event Listener Details**:
- Event Type: `load`
- Action: Sends message to browser for results, and updates the UI if results are received.


### Context Detail Click Event Listener

**Description**: This event listener handles clicks on buttons within the context detail section, triggering a message to the browser to focus on the clicked context item.

**Event Listener Details**:
- Event Type: `click`
- Target: Button elements within the context detail section.
- Action: Sends a message to the browser to focus on the clicked context item.


### Main Details Click Event Listener

**Description**: This event listener handles clicks on buttons within the main details section, triggering a message to the browser to focus on the clicked main item.

**Event Listener Details**:
- Event Type: `click`
- Target: Button elements within the main details section, each associated with an item's index via `data-index`.
- Action: Sends a message to the browser to focus on the clicked item in the main result set.

## Variables

### `detailKeys` and `headerValues`

**Description**: Arrays defining the keys and their corresponding display names for the details table.


### `relatedTabId`, `relatedFrameId`, `executionId`

**Description**: Variables to store the ID of the tab, frame, and execution used for communication.

## Helper Functions (likely from `tryxpath.functions`)

### `updateDetailsTable`

**Description**: Function for rendering and populating tables. This is likely a utility function within `tryxpath.functions`.

### `onError`

**Description**: Error handler function, likely a utility function within `tryxpath.functions`.