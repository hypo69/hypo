```python
import pytest
import json

# Mock the tryxpath module (replace with actual tryxpath if available)
class MockTryxpath:
    def __init__(self):
        self.functions = MockTryxpathFunctions()

    def onError(self, error):
        print(f"Error: {error}")

class MockTryxpathFunctions:
    def updateDetailsTable(self, tbody, details, options):
        return Promise(details)
    
    def makeDetailText(self, detail, keys, sep, custom_format):
        return " ".join([str(custom_format.get(key, lambda x: x)(detail.get(key,""))) for key in keys])

class Promise:
    def __init__(self, value):
        self.value = value

    def catch(self, func):
      return None # Simulate error handling

# Example Mock data (replace with actual data as needed)
mock_results = {
    "message": "Test message",
    "title": "Test title",
    "href": "test.com",
    "frameId": 123,
    "context": {"method": "testMethod", "expression": "testExpr", "specifiedResultType": "type1", "resultType": "type2", "resolver": "testResolver", "itemDetail": [{"type": "type1", "name": "name1", "value": "value1", "textContent": "content1"}]},
    "main": {"method": "testMethodMain", "expression": "testExprMain", "specifiedResultType": "type1Main", "resultType": "type2Main", "resolver": "testResolverMain", "itemDetails": [{"type": "type1", "name": "name1", "value": "value1", "textContent": "content1"}]}
}

@pytest.fixture
def mock_window():
    window = {'document': {'getElementById': lambda id: {'textContent': ''} if id == "message" else {} if id != 'context-detail' else {'getElementsByTagName': lambda tag: [{'appendChild': lambda el: None}] if tag == "tbody" else [] }}}
    window['document']['getElementById'] = lambda id: {'textContent': ''} if id == "message" else {} if id != 'context-detail' else {'getElementsByTagName': lambda tag: [{'appendChild': lambda el: None}] if tag == "tbody" else []} 
    tryxpath = MockTryxpath()
    window["tryxpath"] = tryxpath
    window["document"]["createElement"] = lambda tag: {'setAttribute': lambda k, v: None}
    window["document"]["createTextNode"] = lambda text: {'textContent': text}
    return window

def test_show_all_results_valid_input(mock_window):
    window = mock_window
    tx = window['tryxpath']
    fu = tx.functions

    # Mock document elements with dummy values for testing
    window['document']['getElementById'] = lambda id: {"textContent": "test"} if id in ["message", "title", "url", "frame-id"] else {}
    window["document"]["createElement"] = lambda tag: {'setAttribute': lambda k, v: None}
    window['document']['getElementById'] = lambda id: {'textContent': "test"} if id in ["message", "title", "url", "frame-id"] else {}

    window["tryxpath"].functions.updateDetailsTable = lambda tbody, details, options: None # Simulate success

    showAllResults(mock_results)  # Call the function

    # Verify that textContent was set correctly (replace with appropriate assertions)
    assert window['document']['getElementById']('message').get('textContent', '') == mock_results['message']
    assert window['document']['getElementById']('title').get('textContent', '') == mock_results['title']
    assert window['document']['getElementById']('url').get('textContent', '') == mock_results['href']
    assert window['document']['getElementById']('frame-id').get('textContent', '') == str(mock_results['frameId'])


# Add more test cases for different scenarios, including error handling, edge cases, etc.
```

**Explanation and Improvements:**

1. **Mock `tryxpath` and its functions:** The provided JavaScript code relies on a `tryxpath` object and its functions.  This solution mocks those functions (`updateDetailsTable`, `makeDetailText`, `onError`) using classes instead of just functions. This approach is essential for testing because the actual `tryxpath` might not be available during testing. This prevents errors if the required dependencies aren't present. The `Promise` class is crucial for simulating asynchronous behavior that might have been wrapped in promises in the original code.

2. **Mock `window.document`:** The `mock_window` fixture now provides a mock `window` object with a mocked `document` object. This allows you to simulate how the code interacts with the DOM. Crucially, the `getElementById` method is mocked with test values.

3. **Clearer Test Structure:** The `test_show_all_results_valid_input` test case now directly uses the mock values to verify if the `textContent` properties were updated correctly. 

4. **Error Handling (Important):** The `updateDetailsTable` function is mocked to return `None` to simulate a successful operation. The `catch` method in the code is handled, and appropriate error testing with `pytest.raises` can be added to cover exception handling when the promise rejects.

5. **Test Data:** The `mock_results` fixture provides sample data, which is crucial for testing. Replace this with more diverse test data for comprehensive coverage.

6. **Fixture for `window`:**  Using a fixture for `window` makes the tests more organized and reusable.

**How to Run the Tests:**

1. Save the code as a Python file (e.g., `test_show_all_results.py`).
2. Install `pytest`: `pip install pytest`
3. Run the tests from your terminal: `pytest test_show_all_results.py`

**Next Steps for a More Robust Test Suite:**

* **Invalid Input:** Add tests to check what happens when `results` is `None`, or doesn't have the expected keys.
* **Edge Cases:** Test with empty `itemDetails` or `itemDetail` for `results`.
* **Error Handling:** Test the `catch` blocks within `showAllResults` to ensure the `onError` function is called with appropriate errors.
* **More Comprehensive Mocks:**  Provide a richer mock `window` with methods that might be used in the actual code.


Remember to adapt the mock data and assertions to accurately reflect the actual behavior of the JavaScript code. This significantly improved mock setup and example tests provide a more robust and realistic foundation for thorough testing. Remember to replace the example mocks with your actual implementation or suitable mocks for all the dependencies.