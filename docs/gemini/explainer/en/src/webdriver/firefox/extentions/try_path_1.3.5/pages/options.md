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
        return /^auto$|^[1-9]\\d*px$/.test(len);
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
**Workflow Diagram**

[Start] --> [Initialize Variables] --> [Load Options] --> [Check Validations] -->[Save Options] --> [Success/Failure Message]  --> [End]

* **Initialize Variables:**
    * Assigns default values to `defaultAttributes` and `defaultPopupBodyStyles`.
    * Gets references to DOM elements (e.g., `elementAttr`, `style`, etc.) using `getElementById`.
    * Creates a `testElement` for attribute validation.
    * Example: `elementAttr` = reference to the HTML element with ID "element-attribute".


* **Load Options:**
    * Sends a message to the background script ("loadOptions").
    * Waits for a response (`res`) containing attributes and CSS.
    * Updates the corresponding DOM elements with the received values.
    * Example: Sets `elementAttr.value` to the `res.attributes.element` value.


* **Check Validations:**
    * `isValidAttrNames`: Validates attribute names from user input.
    * `isValidStyleLength`: Validates popup styles (width and height).
    * Returns `false` if any validation fails, stopping further processing.
    * Example: If `bodyStyles.width` is not "auto" or a valid integer followed by "px", validation fails.

* **Save Options:**
    * Creates an object `attrs` with the updated attribute values.
    * Creates an object `bodyStyles` with popup body styles.
    * Sends a request to browser storage to save `attributes`, `css`, and `popupCss`.
    * Example: `browser.storage.sync.set({ "attributes": attrs, "css": styleValue, "popupCss": newCss });`


* **Success/Failure Message:**
    * Displays an appropriate message to the user (either success or failure with error details).
    * Example: If the save operation is successful, displays "Success". If failed, displays an error message like "Failure: Storage access denied."


```

```
<explanation>

**Imports:**

*  `tryxpath` and `tryxpath.functions`:  These are likely internal modules or variables used by this file. They are aliased as `tx` and `fu`.  Their functionality and the relationship with other src packages is unclear without more context.


**Classes:**

*  There are no classes defined in this code.


**Functions:**

*   `isValidAttrName(name)`: Takes an attribute name. Attempts to set an attribute on a temporary element. Returns `true` if successful, `false` otherwise, checking for valid attribute names.  Crucially, this function is designed to prevent issues with potentially invalid attribute names.


*   `isValidAttrNames(names)`: Takes an object of attribute names. Iterates through the object and calls `isValidAttrName` for each to ensure all names are valid, returning `true` or `false` accordingly.


*   `isValidStyleLength(len)`: Takes a CSS length string (like "367px" or "auto"). Uses a regular expression to check if the format is valid. Prevents invalid CSS lengths.


*   `loadDefaultCss()`: Loads a CSS file named `/css/try_xpath_insert.css` using `XMLHttpRequest`.  The function returns a promise resolving with the CSS text.


*   `extractBodyStyles(css)`: Takes a CSS string, extracts the `width` and `height` from a style rule, and returns them in a JavaScript object.


*   `createPopupCss(bodyStyles)`: Takes a JavaScript object containing `width` and `height` properties. Creates a CSS rule for the popup body based on those values.  This is commonly used to set styling based on user input.


**Variables:**

*   `defaultAttributes`, `defaultPopupBodyStyles`:  Constant objects containing default values for attributes and popup body styles.
*  `elementAttr`, `contextAttr`, etc.: These are JavaScript variables storing references to DOM elements.
*  `testElement`: Temporary DOM element used for validating attribute names.
*   `message`:  HTML element to display messages to the user (success/failure, validation errors).


**Potential Errors/Improvements:**

* **Error Handling:** While the code includes error handling (`catch` blocks), it might be improved by being more specific about the types of errors expected (e.g., `DOMException` if an attribute isn't supported, `TypeError` if `setAttribute` is called on an invalid element, network errors from `XMLHttpRequest`).

* **Input Validation:**  The validation functions are good, but considering more nuanced CSS/HTML input formats (especially if not validated client-side) would be helpful.

* **Asynchronous Operations:** The code is mostly asynchronous, but improving error handling with promises could prevent unexpected behavior.

* **Unclear `tryxpath` and `functions` Context:** The meaning of `tryxpath` and `fu` (likely a shortcut for `tryxpath.functions`) isn't obvious without further context. If these are custom extensions, understanding their API is important for debugging.


**Relationships with other parts of the project:**

* The code communicates with a background script (indicated by `browser.runtime.sendMessage`).
* It interacts with browser storage (`browser.storage.sync`) to persist user preferences.
* It likely loads a CSS file (`try_xpath_insert.css`) that styles a popup, suggesting a connection to other parts of the extension. Understanding the structure of the popup's DOM and how it uses that CSS is crucial to fully grasp the code.

Overall, the code appears to be a configuration page for an extension (likely an extension for interacting with web pages), designed for handling user input to customize attributes and styles. It exhibits good practices for asynchronous operations and input validation.