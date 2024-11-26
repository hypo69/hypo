/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function (window, undefined) {
    "use strict";

    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    const defaultAttributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    const defaultPopupBodyStyles = {
        "width": "367px",
        "height": "auto"
    };

    var elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    function isValidAttrName(name) {
        try {
            testElement.setAttribute(name, "testValue");
        } catch (e) {
            return false;
        }
        return true;
    };

    function isValidAttrNames(names) {
        for (var p in names) {
            if (!isValidAttrName(names[p])) {
                return false;
            }
        }
        return true;
    };

    function isValidStyleLength(len) {
        return /^auto$|^[1-9]\d*px$/.test(len);
    };

    function loadDefaultCss() {
        return new Promise((resolve, reject) => {
            var req = new XMLHttpRequest();
            req.open("GET",
                     browser.runtime.getURL("/css/try_xpath_insert.css"));
            req.responseType = "text";
            req.onreadystatechange = function () {
                if (req.readyState === XMLHttpRequest.DONE) {
                    resolve(req.responseText);
                }
            };
            req.send();
        });
    };

    function extractBodyStyles(css) {
        var styles = {};

        var res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            styles.width = res[1];
            styles.height = res[2];
        } else {
            styles.width = "";
            styles.height = "";
        }

        return styles;
    };

    function createPopupCss(bodyStyles) {
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };

    window.addEventListener("load", () => {
        // ... (rest of the code)
    });

    testElement = document.createElement("div");

})(window);
```

```
<algorithm>
**Step 1: Initialization**

*   Variables like `elementAttr`, `contextAttr`, etc. are declared and initialized to null.
*   `defaultAttributes` and `defaultPopupBodyStyles` store default values for attributes and popup styles.
*   `testElement` is created to check attribute validity.


**Step 2: Validation Functions**

*   `isValidAttrName`: Attempts to set an attribute on `testElement` to check its validity.  Returns `true` if successful, `false` otherwise. Example: `isValidAttrName("data-test")` might return `true`.
*   `isValidAttrNames`: Checks if all attributes in a given set are valid. Example: `isValidAttrNames({"name": "test", "class": "another"})` might return `true` or `false` based on validation results.
*   `isValidStyleLength`: Checks if a style length string (e.g., "300px", "auto") is valid. Example: `isValidStyleLength("300px")` is `true`, `isValidStyleLength("badValue")` is `false`.

**Step 3: Loading Default CSS and Handling Options**
 * `loadDefaultCss`: Fetches default CSS (`try_xpath_insert.css`) from a specified location, returning the CSS content as a promise. Example: Calls browser function to access runtime URL, sends an XMLHttpRequest to get file contents, resolves when data is received.
 * Option Handling: This section handles loading saved options from storage, setting the input fields with the loaded data, and handling any errors while doing so.


**Step 4: Saving Options**

*   Event listener for the "save" button is registered.
*   The values from the input fields are collected, validated using `isValidAttrNames`, and `isValidStyleLength`.
*   If valid, the collected data is sent to browser storage, triggering a success message. Otherwise, appropriate error messages are shown,
*   If invalid, error messages are displayed and saving is prevented.



**Step 5: Showing Default Options**

*   Event listener for "show-default" button is registered.
*   Input fields are populated with the `defaultAttributes` values.
*   Default CSS is fetched and applied using `loadDefaultCss`.  Default popup styles are set.


**Data Flow:**

1.  User interacts with the options page.
2.  Event listeners on buttons trigger functions.
3.  Functions retrieve data from input fields, validating as needed,
4.  The data is sent to browser storage.
5.  Successfully saved data triggers success message.
6.  Failed saving triggers error message.


**Example Data Flow (Saving):**
```
User clicks "Save" ->
getDataFromInputs() -> {element:"data-test",...} ->
isValidAttrNames({element:"data-test",...}) returns true ->
browser.storage.sync.set({attributes: {...}, css: ...}) ->
Success message displayed.

```
```


<explanation>

**Imports:**

*  There are no explicit imports in the standard module sense.
*  `tx` and `fu` are aliased variables referring to `tryxpath` and `tryxpath.functions` which likely are objects (defined elsewhere in a project and likely in another file), possibly from a library or a module used for handling TryXPath operations.

**Classes:**

*  There are no classes defined in this code.

**Functions:**

*   `isValidAttrName(name)`: Takes an attribute name (`name`) as input, attempts to set an attribute with that name in a temporary element, checking for exceptions. Returns `true` if the attribute could be set; `false` otherwise.
*   `isValidAttrNames(names)`: Takes an object (`names`) of attribute names as input and checks if every attribute name is valid using `isValidAttrName`. Returns `true` if all attribute names are valid; `false` otherwise.
*   `isValidStyleLength(len)`: Takes a style length string (`len`) and checks if it's a valid style length (`"auto"` or `<number>px`).
*   `loadDefaultCss()`: Fetches default CSS file (try_xpath_insert.css) from the extension's resources. Returns a promise containing the CSS text.
*   `extractBodyStyles(css)`: Extracts width and height styles from a CSS string. Returns an object with width and height style properties.
*   `createPopupCss(bodyStyles)`: Creates a CSS string for the popup body, given the styles.


**Variables:**

*   `defaultAttributes`, `defaultPopupBodyStyles`: Constants holding default attribute and style values.
*   Many variables are used to store DOM elements, allowing the program to get values from these elements on the page and change their values.  Example variables: `elementAttr`, `contextAttr`, `style`, `popupBodyWidth`, `popupBodyHeight`, `message`.

**Potential Errors/Improvements:**

*   Error handling in `isValidAttrName` could be improved by providing more specific error messages.
*   The regular expression for `isValidStyleLength` could be more robust to handle potential variations in style length strings.
*   Consider using a more descriptive variable name for `style` (e.g., `popupStyle`).
*   Consider error handling on failed responses from `browser.runtime.sendMessage` and `browser.storage.sync.set`.

**Relationships with other parts of the project:**

*   The `tryxpath` and `tryxpath.functions` objects strongly imply that this code interacts with a TryXPath framework or library, which likely provides functions for XPath related tasks.
*   The use of `browser.runtime.getURL` and `browser.storage.sync` indicates this code is part of an extension (likely a Chrome extension) interacting with browser APIs to access resources and settings.
*   The use of promises (`loadDefaultCss`) and the event listener structure shows that this code is asynchronous, meaning it interacts with the browser's asynchronous event loop.