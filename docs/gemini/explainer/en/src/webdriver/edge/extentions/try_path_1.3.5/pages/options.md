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
```

```mermaid
graph TD
    A[window.addEventListener("load")] --> B{Get element refs};
    B --> C[Load options from browser storage];
    C -- Success --> D[Set element values];
    C -- Failure --> E[Error handling];
    D --> F[Validate attribute names];
    F -- Valid --> G[Validate style length];
    G -- Valid --> H[Save options to browser storage];
    H -- Success --> I[Display success message];
    H -- Failure --> J[Display error message];
    F -- Invalid --> K[Display invalid attribute message];
    G -- Invalid --> L[Display invalid style message];
    B --> M[Attach save event listener];
    M --> F;
    B --> N[Attach show-default event listener];
    N --> O[Set default values];
    O --> P[Load default CSS];
    P -- Success --> Q[Set default styles];
    P -- Failure --> E;
    subgraph Load Options
        C --> D1;
        D1 --> D;
    end
```

```
<explanation>

**Imports:**

There are no explicit imports in the provided code. However, `tx` and `fu` are aliased to `tryxpath` and `tryxpath.functions`, indicating a dependency on a `tryxpath` object/module.  `browser` is likely an object provided by the browser extension framework, handling interactions with the browser's storage and runtime.  The presumed existence of these objects indicates a dependency on a specific framework (likely a browser extension API) and a codebase that defines the `tryxpath` and associated functions. The `browser.runtime.getURL` function suggests this code resides within a web extension environment.

**Classes:**

No classes are defined in this code.  The code functions more procedurally, using functions and variable declarations.

**Functions:**

* **`isValidAttrName(name)`**: Checks if an attribute name is valid by attempting to set it on a test element. Returns `true` if successful, `false` otherwise.
    * **Example:** `isValidAttrName("data-tryxpath-element")` likely returns `true`, while `isValidAttrName("invalid-attr")` potentially returns `false` if setting such an attribute throws an error.
* **`isValidAttrNames(names)`**: Iterates through an object of attribute names and calls `isValidAttrName` for each. Returns `true` if all attributes are valid; `false` otherwise.
    * **Example:** `isValidAttrNames({element: "valid", context: "valid"})` likely returns `true`.  `isValidAttrNames({element: "valid", context: "invalid"})` likely returns `false`.
* **`isValidStyleLength(len)`**: Validates if a style length (e.g., "367px", "auto") is in a valid format. Returns `true` if valid, `false` otherwise.
    * **Example:** `isValidStyleLength("367px")` returns `true`. `isValidStyleLength("invalid")` returns `false`.
* **`loadDefaultCss()`**: Loads default CSS from a file `/css/try_xpath_insert.css` using `XMLHttpRequest`. Returns a Promise resolving with the CSS content.
* **`extractBodyStyles(css)`**: Extracts the width and height styles from a CSS string. Returns an object containing the width and height.
    * **Example:** `extractBodyStyles("width:367px; height:auto;")` returns `{width: "367px", height: "auto"}`.
* **`createPopupCss(bodyStyles)`**: Generates CSS for the popup body based on provided styles.
    * **Example:** `createPopupCss({width: "367px", height: "auto"})` returns `body{width:367px;height:auto;}`.


**Variables:**

* `defaultAttributes`:  Object defining default attribute values for TryXpath.
* `defaultPopupBodyStyles`: An object holding default values for the popup body's width and height.
* `elementAttr`, `contextAttr`, etc.: Variables storing references to HTML elements.
* `testElement`: A temporary element used for validating attribute names.

**Potential Errors/Improvements:**

* **Error Handling:** While the code uses promises and `catch` blocks, error handling within `loadDefaultCss` could be improved.
* **Input Validation:**  The code performs some validation (e.g., attribute validity). However, more comprehensive input validation (e.g., sanitizing user-provided values) to prevent unexpected behavior or XSS vulnerabilities might be beneficial.
* **Clearer Variable Names:** Using more descriptive variable names (e.g., `popupBodyWidth` -> `popupBodyWidthStyle`) might enhance code readability.
* **CSS Parsing:** Relying on a regular expression for parsing CSS could be fragile if the CSS format changes. Using a dedicated CSS parser library would be a more robust approach.


**Relationships:**

This script interacts with:

* **`browser` (extension API):** For loading resources (CSS) and saving configuration to browser storage.
* **`tryxpath` (likely a library/module):** For functions presumably related to XPath operations.
* **HTML elements:** The script interacts with elements like `<input>`, `<button>`, and `<div>` in the extension's user interface.
* **External CSS file `/css/try_xpath_insert.css`:** Used for styling the application.


The code is designed for use within a browser extension, likely to configure options for a TryXpath library or extension.  The sequence of operations (loading options, validating input, saving configuration, and loading defaults) is crucial to the extension's configuration functionality.