rst
How to Write `pytest` Tests
========================================================================================

Description
-------------------------
This code provides instructions for generating `pytest` tests for a given Python code block. It outlines the steps to write comprehensive test cases covering various scenarios, including valid inputs, invalid inputs, edge cases, and exception handling.  The generated tests will be designed to verify the correctness and robustness of the target code.

Execution steps
-------------------------
1. **Analyze the Provided Code:** Carefully examine the Python code for which tests are to be generated.  Identify the functions, classes, and methods that need to be tested. Determine potential inputs and expected outputs for these components.
2. **Define Test Functions:** Create individual test functions for each aspect of the code that needs verification.  Use descriptive names to make the purpose of each test clear, for example, `test_function_name_valid_input`.  Test functions should be isolated to avoid unintended interactions.
3. **Implement Test Logic:** For each test function, specify the necessary input data. Execute the function being tested with the input, and compare the result with the expected output.
4. **Handle Edge Cases:** Consider edge cases, such as boundary conditions, unexpected input values, or invalid input types. Implement test cases to verify that the code handles such cases gracefully, ideally without crashing or producing incorrect results.  Use `pytest.raises` to assert that exceptions are handled correctly.
5. **Implement Fixtures (if needed):** If the functions being tested require any setup or data, define appropriate fixtures using the `@pytest.fixture` decorator.  Fixtures allow you to reuse data across multiple tests.
6. **Document Test Cases:** Include comprehensive docstrings for each test function to clearly explain the test's purpose, the input data, and the expected behavior.  Avoid vague terminology; instead use terms like "validates," "checks," or "asserts" to accurately describe the test's function.
7. **Structure the Tests:** Organize the test functions logically within the file, grouped according to the component they test.  This makes the tests easier to read and maintain.

Usage example
-------------------------
.. code-block:: python

    import pytest

    def my_function(x):
        if x > 0:
            return x * 2
        else:
            return 0

    def test_my_function_positive_input():
        """Checks correct behavior with a positive input."""
        assert my_function(5) == 10

    def test_my_function_zero_input():
        """Checks behavior with a zero input."""
        assert my_function(0) == 0

    def test_my_function_negative_input():
        """Checks behavior with a negative input."""
        assert my_function(-5) == 0

    def test_my_function_input_string():
        """Checks exception handling for non-numeric input."""
        with pytest.raises(TypeError):
            my_function("hello")