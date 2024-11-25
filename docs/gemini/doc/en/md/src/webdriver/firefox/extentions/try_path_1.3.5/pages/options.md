# try_path_1.3.5/pages/options.js

## Overview

This JavaScript file manages the options page for the try_xpath extension. It handles user input for various attributes, styles, and default options, and saves these settings to browser storage.  It also provides functionality to load default settings.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`isValidAttrName`](#isvalidattrname)
    * [`isValidAttrNames`](#isvalidattrnames)
    * [`isValidStyleLength`](#isvalidstylelength)
    * [`loadDefaultCss`](#loaddefaultcss)
    * [`extractBodyStyles`](#extractbodystyles)
    * [`createPopupCss`](#createpopupcss)


## Functions

### `isValidAttrName`

**Description**: Checks if an attribute name is valid for use on an element.

**Parameters**:
- `name` (str): The attribute name to validate.

**Returns**:
- `boolean`: `true` if the attribute name is valid, `false` otherwise.


**Raises**:
-  None


### `isValidAttrNames`

**Description**: Checks if a set of attribute names are valid for use on an element.

**Parameters**:
- `names` (dict): A dictionary where keys are attribute names and values are associated values (can be anything)

**Returns**:
- `boolean`: `true` if all attribute names in the input are valid, `false` otherwise.


**Raises**:
- None


### `isValidStyleLength`

**Description**: Checks if a style length is valid (e.g., "367px" or "auto").

**Parameters**:
- `len` (str): The style length to validate.

**Returns**:
- `boolean`: `true` if the style length is valid, `false` otherwise.


**Raises**:
- None


### `loadDefaultCss`

**Description**: Loads default CSS from a file.

**Parameters**:
- None

**Returns**:
- `Promise<string>`: A promise resolving to the CSS content from the file.


**Raises**:
- `SomeError (from XMLHttpRequest or other internal browser APIs)`: An error occurred during the loading process.


### `extractBodyStyles`

**Description**: Extracts width and height styles from a CSS string.

**Parameters**:
- `css` (str): The CSS string to extract styles from.

**Returns**:
- `object`: An object containing the extracted width and height styles.


**Raises**:
- None


### `createPopupCss`

**Description**: Creates a CSS string for the popup body.

**Parameters**:
- `bodyStyles` (object): An object containing width and height styles.


**Returns**:
- `string`: The CSS string representing the popup body styles.


**Raises**:
- None


###  Event Handling

The file contains event handling for loading options, saving options, and showing default options. These actions interact with the browser's storage API.
* Loads default attributes and styles when the page loads
* Saves user-entered attributes and styles to browser storage on click of the "Save" button
* Loads default options and styles on click of "Show Default" button

**Error Handling**:
Error handling is present within the event listeners to catch issues with loading/saving to browser storage using `.catch(fu.onError)`, as well as attribute and style validation.