```rst
.. role:: python(code)
   :language: python

Prompt for Writing `pytest` Tests
=================================

This document provides instructions for writing comprehensive test cases for Python code using the `pytest` framework.  The tests should cover all major functionalities, considering valid and invalid inputs, edge cases, and exception handling.


Requirements
------------

1.  **Clear and Descriptive Test Names:**  Test function names should clearly indicate the purpose of the test.
2.  **Isolated Tests:** Each test function should be independent and not rely on the state of other tests.
3.  **Comprehensive Scenarios:** Tests should cover various scenarios, including:
    *   Valid inputs.
    *   Invalid or unexpected inputs.
    *   Edge or boundary cases.
4.  **Exception Handling:** Use `pytest.raises` to test exception handling.
5.  **Fixtures (if needed):** Define fixtures separately for data setup.
6.  **Comments:** Add comments explaining the logic of each test.


Example Structure
----------------

.. code-block:: python

   import pytest

   # Fixture definitions (if needed)
   @pytest.fixture
   def example_data():
       """Provides test data for the function."""
       return {...}

   # Tests for Function 1
   def test_function1_valid_input():
       """Checks correct behavior with valid input."""
       # ... test code ...

   def test_function1_invalid_input():
       """Checks correct handling of invalid input."""
       # ... test code ...

   # Tests for Function 2
   def test_function2_edge_case():
       """Checks behavior with edge cases."""
       # ... test code ...

.. note::
   Replace the `# ... test code ...` placeholders with actual test code.  Replace `{...}` with the appropriate fixture data.


.. toctree::
   :maxdepth: 2

   modules/module_name.rst


.. automodule:: module_name
   :members:
   :undoc-members:
   :show-inheritance:


```


**Explanation and Important Considerations**

The generated RST file is a template.  You need to replace placeholders (`# ... test code ...`, `{...}`, `module_name`) with the actual Python code and test cases.  Crucially, the `module_name` needs to be updated to reflect the actual module name.  The `.. toctree::` directive should point to a file, `modules/module_name.rst`, which will contain the specific module documentation. This approach is essential for organizing large projects.   A complete `module_name.rst` file should follow the pattern of the example, listing functions and classes in the corresponding modules.  You will need to create that file and populate it with the appropriate `automodule` directives pointing to the actual Python code files. This file structure will help you structure your documentation in a well-organized way. This is a critical step to ensuring that your documentation is complete and correctly reflects the Python code.