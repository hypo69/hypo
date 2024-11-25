html
<h1>pytest Test Case Generation Instructions</h1>

<h2>Overview</h2>
<p>This document outlines the instructions for generating comprehensive pytest test cases for a given Python code snippet.  The generated tests should cover various scenarios, including valid inputs, invalid/unexpected inputs, edge/boundary cases, and exception handling.</p>

<h2>Instructions</h2>

<ol>
  <li><strong>Input Structure:</strong> The input will contain a Python code block.  This block should contain the Python code to be tested.</li>
  <li><strong>Test Structure:</strong> The generated pytest test cases should follow a structured approach, as demonstrated in the example:</li>
  <ul>
    <li><strong>Import pytest:</strong> Include <code>import pytest</code> at the beginning of the test file.</li>
    <li><strong>Fixture Definition (if needed):</strong> Define fixtures using the <code>@pytest.fixture</code> decorator to provide reusable data for tests.</li>
    <li><strong>Test Functions:</strong> Define test functions using the <code>test_</code> prefix (e.g., <code>test_function1_valid_input</code>). Function names should clearly indicate the scenario being tested.</li>
    <li><strong>Test Logic:</strong> Implement the test logic within the test functions. Utilize <code>assert</code> statements to verify expected results. Test different cases such as valid inputs, invalid inputs, edge cases, and exceptions.</li>
    <li><strong>Exception Handling:</strong> Use <code>pytest.raises</code> to test exceptions.  Ensure tests handle expected exceptions using specific assertion statements.</li>
    <li><strong>Comments:</strong> Include clear and concise comments explaining the purpose of each test function.</li>
    <li><strong>Clear Naming:</strong>  Use descriptive names for test functions (e.g., `test_calculate_average_valid_input`, `test_calculate_average_empty_list`, `test_calculate_average_invalid_input`).</li>
  </ul>
  <li><strong>Test Coverage:</strong>  The tests should aim to cover a wide range of possible inputs and scenarios within the provided Python code.</li>
</ol>

<h2>Example Structure</h2>
<pre><code class="language-python">
import pytest
import math  # if needed for import

# Fixture definitions (if applicable)
@pytest.fixture
def example_data():
    """Provides test data."""
    return [1, 2, 3, 4, 5]

# Test for a function
def test_function1_valid_input(example_data):
  """Tests a function with valid input."""
  # Add assertion statements here to validate expected behavior
  # Example:
  # result = some_function(example_data)
  # assert result == expected_result
  # ...


def test_function1_invalid_input():
  """Tests the function with invalid input."""
  # Add assertion statements to validate exception handling or invalid input results
  # Example:
  # with pytest.raises(TypeError) as excinfo:
  #     result = some_function("invalid input")
  # assert "Expected type int" in str(excinfo.value)
  # ...

#Test for another function (for exception handling)
def test_function2_exception():
    """Tests function with invalid input to catch an exception"""
    with pytest.raises(ValueError) as ex:
      #Call function with input that should raise an error
      result = some_function(invalid_data)
    assert 'Invalid input' in str(ex.value)


</code></pre>

<h2>Important Considerations</h2>
<ul>
<li>Ensure the Python code provided for testing is correctly structured.</li>
<li>Thoroughly test the provided code's handling of edge cases and unexpected input values.</li>
<li>Test any functions, methods, or classes you want to cover.</li>
</ul>

<h2>Output Format</h2>
<p>The output will be a series of pytest test functions, ready to be executed using the pytest framework.</p>

<p>Provide the Python code you wish to test, and I will generate the pytest test cases for that code.</p>