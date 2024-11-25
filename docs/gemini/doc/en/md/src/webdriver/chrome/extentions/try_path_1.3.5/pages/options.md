# try_path_1.3.5/pages/options.js

## Overview

This JavaScript file (`options.js`) handles the options page for the `tryxpath` extension. It allows users to customize attributes, CSS styles, and popup body dimensions for the extension's functionality.  The page interacts with browser storage and APIs to save and apply user preferences.  It also provides a feature to restore default settings.


## Variables

### `defaultAttributes`

**Description**: An object containing default attribute values for the extension.  These are used when restoring to default values.

**Values**:

```javascript
{
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}
```

### `defaultPopupBodyStyles`

**Description**: An object containing default CSS styles for the extension's popup body.


**Values**:

```javascript
{
    "width": "367px",
    "height": "auto"
}
```


### `elementAttr`, `contextAttr`, `focusedAttr`, `ancestorAttr`, `frameAttr`, `frameAncestorAttr`, `style`, `popupBodyWidth`, `popupBodyHeight`, `message`, `testElement`

**Description**:  Variables representing DOM elements on the options page.  Used for accessing and modifying user input and displaying messages.


## Functions

### `isValidAttrName(name)`

**Description**:  Checks if a given attribute name is valid.

**Parameters**:

- `name` (str): The attribute name to validate.

**Returns**:

- bool: `true` if the attribute name is valid, `false` otherwise.


**Raises**:

- (No Exceptions documented in the code)


### `isValidAttrNames(names)`

**Description**: Checks if all attribute names in a given object are valid.

**Parameters**:

- `names` (object): An object containing attribute names.

**Returns**:

- bool: `true` if all attribute names are valid, `false` otherwise.


**Raises**:

- (No Exceptions documented in the code)



### `isValidStyleLength(len)`

**Description**: Validates the length property of a CSS style, checking if it's valid CSS dimension (e.g., "367px").

**Parameters**:

- `len` (str): The CSS length value to validate.

**Returns**:

- bool: `true` if the length is a valid CSS dimension, `false` otherwise.


**Raises**:

- (No Exceptions documented in the code)



### `loadDefaultCss()`

**Description**: Loads the default CSS for the extension.

**Returns**:

- Promise<string>: A Promise resolving to the retrieved CSS text.


**Raises**:


- `fu.onError`:  In case of an error during the HTTP request.



### `extractBodyStyles(css)`

**Description**: Extracts width and height styles from a CSS string.

**Parameters**:

- `css` (str): The CSS string to extract styles from.

**Returns**:

- object: An object containing extracted `width` and `height` styles.  Returns empty object if no styles are found.


**Raises**:

- (No Exceptions documented in the code)


### `createPopupCss(bodyStyles)`

**Description**: Creates a CSS string for the popup body styles.

**Parameters**:

- `bodyStyles` (object): An object containing width and height styles.

**Returns**:

- str: A CSS string defining the popup body styles.


**Raises**:

- (No Exceptions documented in the code)



## Event Handling

### Event Listener: `load`

**Description**: This event listener runs once the page is fully loaded.  It initializes variables, retrieves user options, and sets up event listeners for saving changes and restoring defaults.


### Event Listener: "click" on save button

**Description**: This listener handles the "save" button click. It collects user input, validates attributes and styles, saves the configuration to browser storage, and displays confirmation or error messages.


### Event Listener: "click" on show-default button

**Description**: This listener restores the default attribute and style values from `defaultAttributes` and `defaultPopupBodyStyles` to the corresponding input fields on the page.


## Other Notes

The code uses asynchronous operations (Promises) for fetching and saving data, handling potential errors using `catch` blocks, and using  the `browser` API for interacting with the browser.  It employs regular expressions for extracting CSS styles. The functions (`isValidAttrName`, `isValidAttrNames`, `isValidStyleLength`) are used to validate user input and prevent errors.