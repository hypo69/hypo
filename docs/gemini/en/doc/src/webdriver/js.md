# hypotez/src/webdriver/js.py

## Overview

This module provides JavaScript utility functions for interacting with a web page. It extends Selenium WebDriver capabilities by adding common JavaScript-based functions for handling DOM element visibility, retrieving page information, and managing browser focus.

## Table of Contents

* [Classes](#classes)
    * [JavaScript](#javascript)
* [Functions](#functions)
    * [unhide_DOM_element](#unhide-dom-element)
    * [ready_state](#ready-state)
    * [window_focus](#window-focus)
    * [get_referrer](#get-referrer)
    * [get_page_lang](#get-page-lang)


## Classes

### `JavaScript`

**Description**: Provides JavaScript utility functions for interacting with a web page.

**Methods**

#### `__init__`

**Description**: Initializes the JavaScript helper with a Selenium WebDriver instance.

**Parameters**:

- `driver` (WebDriver): Selenium WebDriver instance to execute JavaScript.

#### `unhide_DOM_element`

**Description**: Makes an invisible DOM element visible by modifying its style properties.

**Parameters**:

- `element` (WebElement): The WebElement object to make visible.

**Returns**:

- `bool`: True if the script executes successfully, False otherwise.

**Raises**:

- `Exception`: Any exception during JavaScript execution.

#### `ready_state`

**Description**: Retrieves the document loading status.

**Returns**:

- `str`: 'loading' if the document is still loading, 'complete' if loading is finished.

**Raises**:

- `Exception`: Any exception during JavaScript execution.


#### `window_focus`

**Description**: Sets focus to the browser window using JavaScript. Attempts to bring the browser window to the foreground.

**Raises**:

- `Exception`: Any exception during JavaScript execution.


#### `get_referrer`

**Description**: Retrieves the referrer URL of the current document.

**Returns**:

- `str`: The referrer URL, or an empty string if unavailable.

**Raises**:

- `Exception`: Any exception during JavaScript execution.


#### `get_page_lang`

**Description**: Retrieves the language of the current page.

**Returns**:

- `str`: The language code of the page, or an empty string if unavailable.

**Raises**:

- `Exception`: Any exception during JavaScript execution.


## Functions

(No functions defined in the module besides class methods)