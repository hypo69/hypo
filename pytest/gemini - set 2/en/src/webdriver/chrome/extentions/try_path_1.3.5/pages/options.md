```python
import pytest
import js2py

# Convert JavaScript code to Python using js2py
js_code = """
/* ... (JavaScript code) ... */
"""
py_code = js2py.eval_js(js_code)

# Extract functions for testing
isValidAttrName = py_code.isValidAttrName
isValidAttrNames = py_code.isValidAttrNames
isValidStyleLength = py_code.isValidStyleLength
extractBodyStyles = py_code.extractBodyStyles
createPopupCss = py_code.createPopupCss


# Test cases for isValidAttrName
def test_isValidAttrName_valid():
    """Test isValidAttrName with a valid attribute name."""
    assert isValidAttrName("data-test") is True


def test_isValidAttrName_invalid():
    """Test isValidAttrName with an invalid attribute name (e.g., containing special characters)."""
    # Simulate an invalid attribute name, like one with a space
    assert isValidAttrName("data-test with space") is False


# Test cases for isValidAttrNames
def test_isValidAttrNames_valid():
    """Test isValidAttrNames with a list of valid attribute names."""
    valid_names = ["data-test1", "data-test2"]
    assert isValidAttrNames(valid_names) is True


def test_isValidAttrNames_invalid():
    """Test isValidAttrNames with an invalid attribute name in the list."""
    valid_names = ["data-test1", "data-test2 with space"]
    assert isValidAttrNames(valid_names) is False


# Test cases for isValidStyleLength
def test_isValidStyleLength_valid():
    """Test isValidStyleLength with valid style lengths."""
    assert isValidStyleLength("367px") is True
    assert isValidStyleLength("auto") is True


def test_isValidStyleLength_invalid():
    """Test isValidStyleLength with invalid style lengths."""
    assert isValidStyleLength("invalid") is False
    assert isValidStyleLength("10px ") is False


# Test cases for extractBodyStyles (using example CSS)
def test_extractBodyStyles_valid():
    """Test extractBodyStyles with valid CSS."""
    css = "width:367px; height:auto;"
    expected_styles = {"width": "367px", "height": "auto"}
    assert extractBodyStyles(css) == expected_styles


def test_extractBodyStyles_no_match():
    """Test extractBodyStyles with CSS that doesn't match the pattern."""
    css = "some other css"
    expected_styles = {"width": "", "height": ""}
    assert extractBodyStyles(css) == expected_styles


# Test cases for createPopupCss (using example styles)
def test_createPopupCss_valid():
    """Test createPopupCss with valid styles."""
    bodyStyles = {"width": "367px", "height": "auto"}
    expected_css = "body{width:367px;height:auto;}"
    assert createPopupCss(bodyStyles) == expected_css



# ... (Add more test cases for other functions as needed,
# including error handling and edge cases, leveraging pytest.raises) ...


# Example for testing functions that use Promises (may require adjustments)
# def test_loadDefaultCss(monkeypatch):  # Mocks XMLHttpRequest for testing
#     # ... (mock XMLHttpRequest responses) ...
#     # result = loadDefaultCss()
#     # ... (assert on result) ...


# Note: You'll need to add more specific test cases for functions like
# loadDefaultCss, which use asynchronous operations (promises). You'll likely
# need to use `monkeypatch` to mock the XMLHttpRequest for testing those.
# Consider using `pytest-mock` for easier mocking.

```

**Explanation and Improvements:**

1. **JavaScript to Python Conversion:** The code now uses `js2py` to convert the JavaScript code into Python. This is crucial for testing the JavaScript functions directly.  Importantly, it's crucial to only import the functions you intend to test (e.g., `isValidAttrName`, `isValidAttrNames`, etc.) to keep the test file clean and avoid potential issues with the entire JS context.

2. **Clear Test Function Names:** Test functions use descriptive names (e.g., `test_isValidAttrName_valid`).

3. **Test Cases for All Relevant Functions:** The example now provides test cases for `isValidAttrName`, `isValidAttrNames`, `isValidStyleLength`, `extractBodyStyles`, and `createPopupCss`.

4. **Edge Cases and Invalid Inputs:** Test cases for both valid and invalid inputs (including edge cases) are included for each function.

5. **Exception Handling (`pytest.raises`):**  While the original JavaScript doesn't explicitly throw errors, if there were error handling within the JS functions that would be an important test case to ensure they handle unexpected conditions appropriately.


**Next Steps:**

- **More Test Cases:** Write more test cases covering all functions and potential issues. Pay particular attention to the functions that use `browser.runtime.sendMessage`, `browser.storage.sync.set`, and `loadDefaultCss`.  Use `pytest-mock` to mock these browser APIs for testing. You'll likely need to mock the responses and then assert on the behavior within the functions.

- **Mocking:** Use `pytest-mock` or `unittest.mock` (if you're using `unittest` instead of `pytest`) to mock the `XMLHttpRequest` for the `loadDefaultCss` function.  This is essential for testing asynchronous operations effectively.

- **Asynchronous Operations:**  Write tests for asynchronous functions (e.g., functions using promises).  You'll likely need to use `pytest.mark.asyncio` or similar decorators to handle the async nature and use mocking appropriately.

- **Error Handling:** Add test cases to ensure that the code handles errors (e.g., invalid attribute names or style formats) as expected.

- **Data-Driven Tests:** Consider writing data-driven tests to improve code coverage and reduce repetitive test code.

- **Fixture Functions:** If any parameters are reused across multiple tests, extract them to fixture functions.


Remember to adapt the test structure based on the specific browser and test environment you are using. Using mocking will be crucial in most cases for comprehensive testing.