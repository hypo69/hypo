```python
import pytest

# No Python code to test in the provided HTML.
# Tests would need to be written against the JavaScript code in 'popup.js'
# which is not provided.
# Therefore, no functional tests can be created.

# Placeholder for hypothetical test cases (replace with actual tests)
def test_placeholder_popup_js_function():
    """
    This is a placeholder test.  No JavaScript code was provided,
    so we cannot create meaningful tests.
    Replace this with actual tests against the 'popup.js' file.
    """
    assert True  # Replace this with an actual assertion


def test_placeholder_angular_directives():
    """
    This is a placeholder test.  No AngularJS code was provided,
    so we cannot create meaningful tests.
    Replace this with actual tests against any AngularJS directives.
    """
    assert True  # Replace this with an actual assertion
```

**Explanation and Important Considerations:**

The provided code is HTML, not Python.  Therefore, there's no Python code to test.  The `popup.js` file (and likely other JavaScript files) are necessary for any meaningful test suite.

**To write actual tests:**

1. **Obtain `popup.js`:**  This JavaScript file contains the functions and logic that you need to test.

2. **Identify testable functions:** Look for JavaScript functions that manipulate data, update the UI, interact with APIs, or perform other operations.

3. **Choose a JavaScript testing framework:**  Jest, Mocha, or similar frameworks are suitable for writing JavaScript tests.

4. **Write tests in JavaScript:** Use the chosen framework to create tests.  These tests will be separate from the Python tests.

5. **Use mocking (if needed):** For testing interactions with external APIs, mock them to control the behavior and ensure your code is independent of the external system.

6. **Use assertions:**  Assert that the functions return the expected values or change the UI as expected.  Use tools to inspect variables and state inside the functions under test.

**Example Structure (JavaScript Tests):**

```javascript
// (Inside a test file, e.g., test_popup.js)
import { sendMessage, setActiveTab, isTabActive } from './popup'; // Import functions

describe('Popup functions', () => {
  it('should correctly set the active tab', () => {
    // Arrange
    let isChatActive = false;

    // Act
    setActiveTab('chat');

    // Assert
    expect(isTabActive('chat')).toBe(true);
    expect(isTabActive('model')).toBe(false);
  });

  it('should handle invalid tab names', () => {
    // Arrange

    // Act
    setActiveTab('other'); //Or other unexpected tab

    // Assert
    expect(isTabActive('chat')).toBe(false);
    expect(isTabActive('model')).toBe(false);
  });
  // ... more tests for sendMessage, etc.
});
```

**Crucial Information Missing:**

The example HTML uses AngularJS, so you should also test the AngularJS components if the application uses them extensively. You need to consider any interaction with Angular's $scope, data binding, etc.

**In summary, to create real tests for this code:** provide the `popup.js` file and any other necessary JavaScript code.  I can then give specific test examples related to the JavaScript functionality.