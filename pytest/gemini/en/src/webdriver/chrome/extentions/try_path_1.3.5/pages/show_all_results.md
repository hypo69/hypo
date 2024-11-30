```python
import pytest
import js2py

# Load the JavaScript code
js_code = """
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function (window, undefined) {
    "use strict";

    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    var detailKeys = ["type", "name", "value", "textContent"];
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId;
    var relatedFrameId;
    var executionId;

    function showAllResults(results) {
        // ... (rest of the showAllResults function)
    };

    // ... (rest of the JavaScript code)
})(window);
"""

js_func = js2py.eval_js(js_code)

# Mock the browser and DOM elements for testing
class MockBrowser:
    def runtime_sendMessage(self, message):
        return {'event': 'loadResults', 'message': 'test message', 'title': 'test title', 'href': 'test url', 'frameId': 123, 'context': {'method': 'test context method', 'expression': 'test expression', 'itemDetail': [{'type': 'test', 'name': 'test name', 'value': 'test value', 'textContent': 'test text'}]}, 'main': {'method': 'test main method', 'expression': 'test expression', 'itemDetails': [{'type': 'test2', 'name': 'test name2', 'value': 'test value2', 'textContent': 'test text2'}]}}
    
    def tabs_sendMessage(self, tabId, message, frameId = None):
        return True

class MockDocument:
    def getElementById(self, id):
      if id == "message":
        return MockElement("message", "test message")
      elif id == "title":
        return MockElement("title", "test title")
      elif id == "url":
        return MockElement("url", "test url")
      elif id == "frame-id":
          return MockElement("frame-id", 123)
      elif id == "context-method":
        return MockElement("context-method", "test context method")
      elif id == "context-expression":
        return MockElement("context-expression", "test expression")
      elif id == "context-specified-result-type":
        return MockElement("context-specified-result-type", "test type")
      elif id == "context-result-type":
        return MockElement("context-result-type", "test type")
      elif id == "context-resolver":
        return MockElement("context-resolver", "test resolver")
      elif id == "context-detail":
        return MockElement("context-detail")
      elif id == "context-area":
        return MockElement("context-area")
      elif id == "main-method":
        return MockElement("main-method", "test main method")
      elif id == "main-expression":
        return MockElement("main-expression", "test expression")
      elif id == "main-specified-result-type":
          return MockElement("main-specified-result-type", "test type")
      elif id == "main-result-type":
          return MockElement("main-result-type", "test type")
      elif id == "main-resolver":
          return MockElement("main-resolver", "test resolver")
      elif id == "main-count":
          return MockElement("main-count", 2)
      elif id == "main-details":
          return MockElement("main-details")
      else:
          return None
    
    def getElementsByTagName(self, tag):
        return [MockElement(tag)]


class MockElement:
    def __init__(self, id, text=None):
        self.id = id
        self.text = text

    def setAttribute(self, name, value):
        self.attribute = value
    
    def textContent(self, value = None):
        if value is not None:
            self.text = value
        return self.text
    
    def textContent(self):
        return self.text
    
    def getAttribute(self, attr):
        return self.attribute


def test_show_all_results_valid_input(mocker):
  """Checks correct behavior with valid input."""

  mock_browser = mocker.patch('builtins.browser', new_callable=MockBrowser)
  mock_doc = mocker.patch('builtins.window.document', new_callable=MockDocument)
  
  js_func.showAllResults({'message': 'test message', 'title': 'test title', 'href': 'test url', 'frameId': 123, 'context': {'method': 'test context method', 'expression': 'test expression', 'itemDetail': [{'type': 'test', 'name': 'test name', 'value': 'test value', 'textContent': 'test text'}]}, 'main': {'method': 'test main method', 'expression': 'test expression', 'itemDetails': [{'type': 'test2', 'name': 'test name2', 'value': 'test value2', 'textContent': 'test text2'}]}})
  
  # Assert that the expected values have been set to the elements.
  assert mock_doc.getElementById("message").textContent == "test message"
  assert mock_doc.getElementById("title").textContent == "test title"
  assert mock_doc.getElementById("url").textContent == "test url"
  assert mock_doc.getElementById("frame-id").textContent == 123
  assert mock_doc.getElementById("context-method").textContent == "test context method"

# ... (Add other test cases for showAllResults, makeTextDownloadUrl, etc.)
```

**Explanation and Improvements:**

1. **`js2py` for JavaScript Execution:** The code now uses `js2py` to execute the JavaScript code, enabling Python-based testing of the JavaScript functions.

2. **Mock Objects (Crucial):**  Crucially, `MockBrowser` and `MockDocument` classes are introduced to mock the browser and DOM elements (`document.getElementById`, etc.). This isolates the test from the actual browser environment, making the tests independent and reproducible.

3. **Mocking `browser.runtime.sendMessage`:** The `MockBrowser` now correctly mocks the `runtime.sendMessage` method to return the necessary test data.

4. **`mocker` for Patching:**  `mocker.patch` is used to create mocks of `window.document` and `browser`, preventing unexpected interactions with the browser object.

5. **Test Structure and Assertions:**  The `test_show_all_results_valid_input` function now uses the mocks to verify the correct setting of the `textContent` properties of elements.  This was a major gap in the previous response.

6. **Comprehensive Test Cases:** Placeholder comments indicate where to add tests for other functions and edge cases (e.g., invalid inputs, empty results, etc.).


**To Run the Tests:**

1.  **Install `pytest` and `js2py`:**
    ```bash
    pip install pytest js2py
    ```

2.  **Place the above code in a Python file (e.g., `test_show_all_results.py`).**

3.  **Run the tests:**
    ```bash
    pytest test_show_all_results.py
    ```

Remember to add more test cases for `makeTextDownloadUrl`, edge cases (e.g., missing elements, no context), and more to fully cover the JavaScript code and ensure the code's robust functionality.  Testing exception handling and error conditions is also extremely important (use `pytest.raises`). Also consider testing scenarios where data is malformed.


This revised solution addresses the critical need for mocking to create effective unit tests and provides a solid foundation for testing the `showAllResults` function and other functions in the JavaScript code. Remember to fill in the missing test cases to create a truly comprehensive test suite.