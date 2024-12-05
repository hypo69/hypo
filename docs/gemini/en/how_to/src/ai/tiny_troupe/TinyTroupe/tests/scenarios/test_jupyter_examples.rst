rst
How to execute Jupyter notebooks with pytest
========================================================================================

Description
-------------------------
This code defines a function to execute Jupyter notebooks using `nbconvert.preprocessors.ExecutePreprocessor`.  It iterates through all `.ipynb` files in a specified folder, executes them, and saves the results.  Crucially, it handles potential exceptions during execution, reporting the failure and preserving the problematic notebook for review.  It also ensures that the `tinytroupe` package is correctly imported.

Execution steps
-------------------------
1. **Import necessary libraries:** Imports `os`, `nbformat`, `ExecutePreprocessor` from `nbconvert`, `pytest`, and `sys`.  This setup is to include the package directory into Python import path.

2. **Define constants:** Sets `NOTEBOOK_FOLDER`, `TIMEOUT`, and `KERNEL_NAME` for configuration.


3. **`get_notebooks` function:** This function filters `.ipynb` files within the specified folder, excluding files containing ".executed." or ".local." in their names to prevent execution of already processed notebooks or avoid unnecessary steps.

4. **`test_notebook_execution` function:** This function uses `pytest.mark.parametrize` to execute each notebook retrieved by `get_notebooks`.
   - It reads each notebook file into a notebook object.
   - It prints a message indicating the notebook being executed.
   - It uses `ExecutePreprocessor` to execute the notebook with a specified timeout and kernel.
   - It captures any exceptions during execution. If an exception occurs, it reports it to pytest and fails the test.
   - It saves a copy of the executed notebook (with a modified filename) to persist the state. This allows for post-mortem analysis and debugging.

5. **Error Handling:** The `try...except` block ensures the script doesn't crash if a notebook fails to execute; it instead reports the failure to pytest and keeps the potentially problematic notebook saved.

6. **Save the Executed Notebook:** The `finally` block ensures the execution notebook is saved in a new location.



Usage example
-------------------------
.. code-block:: python

    import os
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    import pytest
    import sys

    # Ensure the package is imported from the correct location
    sys.path.insert(0, '../../tinytroupe/')
    sys.path.insert(0, '../../')
    sys.path.insert(0, '..')

    NOTEBOOK_FOLDER = "../examples/"  # Update this path
    TIMEOUT = 600
    KERNEL_NAME = "python3"

    # ... (The rest of the code, including get_notebooks and test_notebook_execution functions, is the same)

    # Run the tests
    pytest.main(['-v', '--disable-warnings', '--nbconvert-app=jupyter_execute', 'tests/scenarios/test_jupyter_examples.py'])