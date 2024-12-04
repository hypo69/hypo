```python
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
import sys

# Ensure correct package import paths
sys.path.insert(0, '../../tinytroupe/')
sys.path.insert(0, '../../')
sys.path.insert(0, '..')

# Set the folder containing the notebooks (replace with actual path)
NOTEBOOK_FOLDER = "../examples/"
TIMEOUT = 600
KERNEL_NAME = "python3"


def get_notebooks(folder):
    """Retrieve all Jupyter notebook files from the specified folder."""
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path):
    """Execute a Jupyter notebook and assert that no exceptions occur."""
    # Check if the notebook file exists
    if not os.path.exists(notebook_path):
        pytest.skip(f"Notebook {notebook_path} not found. Skipping test.")


    with open(notebook_path, "r", encoding="utf-8") as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)
        print(f"Executing notebook: {notebook_path} with kernel: {KERNEL_NAME}")
        ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)

        try:
            # Capture standard output and errors
            captured_output = io.StringIO()
            sys.stdout = captured_output
            ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})
            sys.stdout = sys.__stdout__  # Restore stdout
            
            # Check if there are any warnings or errors in the output
            captured_output_string = captured_output.getvalue()

            if any(warning in captured_output_string for warning in ["WARNING", "error"]):
                pytest.fail(f"Notebook {notebook_path} produced warnings or errors: {captured_output_string}")


            print(f"Notebook {notebook_path} executed successfully.")

        except Exception as e:
            pytest.fail(f"Notebook {notebook_path} raised an exception: {e} \n Output: {captured_output.getvalue()}")  # Include output in failure message
        finally:
            # Save a copy of the executed notebook
            output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
            with open(output_path, "w", encoding="utf-8") as out_file:
                nbformat.write(notebook, out_file)

            print(f"Executed notebook saved as: {output_path}")


import io # Needed for capturing output


```

**Improvements and explanations:**

* **Error Handling and Output Capture:** The crucial addition is capturing standard output (`sys.stdout`) using `io.StringIO`.  This allows you to check if any warnings or errors were printed during the notebook execution.  The `pytest.fail` message now includes the output, making debugging much easier.

* **File Existence Check:** Added a check `if not os.path.exists(notebook_path):` to skip the test if the notebook file doesn't exist. This prevents `FileNotFoundError` and makes the tests more robust.

* **Robust Exception Handling:** The `try...except...finally` block is now more complete.  The `finally` block remains to save the executed notebook.

* **Clearer Error Messages:** The `pytest.fail` messages now contain more information to help you pinpoint the issue if a notebook fails. This also includes the output of the notebook in the failure message which can be invaluable in debugging.

* **Import `io`:** The `io` module is now imported to use `io.StringIO` for capturing output.

* **pytest.skip():**  The `pytest.skip` function is used gracefully handles the case where a notebook file might not exist.  This makes the test more robust.


This improved solution is significantly more robust and helpful in debugging failing notebooks by providing the detailed output from the notebook execution when a failure occurs.  Remember to replace `"../examples/"` with the actual path to your example notebook directory. Remember to install the `nbformat` and `nbconvert` libraries if you don't have them.  You can do this using pip:

```bash
pip install nbformat nbconvert
```