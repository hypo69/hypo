rst
How to use the `tinytroupe.utils` functions
=========================================================================================

Description
-------------------------
This code defines unit tests for three utility functions within the `tinytroupe.utils` module: `name_or_empty`, `extract_json`, and `repeat_on_error`.  These functions are used for various tasks, including handling potentially failing operations, extracting JSON from strings, and safely obtaining names from objects.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `pytest` framework, `MagicMock` from `unittest.mock`, and the `name_or_empty`, `extract_json`, and `repeat_on_error` functions from the `tinytroupe.utils` module.  Import statements also include necessary paths for module imports.
2. **Define test cases for `extract_json`:** These cases test extracting JSON from strings containing valid and invalid JSON, as well as cases with no JSON.  They utilize assertions to verify the correct extraction.
3. **Define test cases for `name_or_empty`:**  The tests check the function's ability to retrieve a name from an object and handle cases where the object is `None`.
4. **Define test cases for `repeat_on_error`:** These test cases verify the retry functionality in the `repeat_on_error` decorator. The tests include cases where an exception is raised (and handled) and cases where no exception is encountered, also checking for exceptions that aren't handled.  They utilize `MagicMock` to mock the behavior of a function and `pytest.raises` to check for expected exceptions.
5. **Test assertions:** Assertions in the tests validate that the functions are behaving as expected.
6. **Import necessary testing modules:**  This part imports necessary utilities like `testing_utils` (which is assumed to contain custom testing helpers).

Usage example
-------------------------
.. code-block:: python

    import pytest
    from unittest.mock import MagicMock
    from tinytroupe.utils import extract_json, repeat_on_error


    # Example usage of extract_json
    text = 'Some text before {"key": "value"} some text after'
    extracted_json = extract_json(text)
    print(extracted_json)  # Output: {'key': 'value'}


    # Example usage of repeat_on_error
    class MyException(Exception):
        pass

    @repeat_on_error(retries=3, exceptions=[MyException])
    def my_function():
        try:
            # Simulate a function that might raise an exception
            raise MyException()
        except Exception as e:
            print(f"Caught an exception: {e}")
            return "Failed"
    result = my_function()
    print(result)  #Output will vary based on internal implementation of retry logic