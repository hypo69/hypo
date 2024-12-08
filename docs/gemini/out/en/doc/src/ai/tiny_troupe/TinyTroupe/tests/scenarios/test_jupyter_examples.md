# test_jupyter_examples.py

## Overview

This module provides a pytest test suite for executing Jupyter notebooks. It iterates through notebooks in a specified folder, executes them using `nbconvert.preprocessor.ExecutePreprocessor`, and checks for exceptions during execution.  The executed notebooks are saved with a '.executed.local.ipynb' suffix.


## Functions

### `get_notebooks`

**Description**: Retrieves all Jupyter notebook files from a specified folder.

**Parameters**:
- `folder` (str): The path to the folder containing the notebooks.

**Returns**:
- list: A list of absolute paths to the Jupyter notebook files.

**Raises**:
- `FileNotFoundError`: If the specified folder does not exist.


### `test_notebook_execution`

**Description**: Executes a Jupyter notebook and asserts that no exceptions occur.

**Parameters**:
- `notebook_path` (str): The absolute path to the Jupyter notebook file to execute.

**Returns**:
- None

**Raises**:
- `Exception`: If any exception is raised during notebook execution.  The specific exception and path are printed to the console, and the test fails.


## Constants

### `NOTEBOOK_FOLDER`

**Description**: The folder containing the Jupyter notebooks. Default is "../examples/". Should be updated if needed.


### `TIMEOUT`

**Description**: Timeout for long-running notebooks, in seconds. Default is 600 (10 minutes).


### `KERNEL_NAME`

**Description**: The kernel name to use for notebook execution.  Default is "python3".


## Usage

To use this test suite, ensure that the `nbconvert` library is installed, and the path to your notebooks folder is correctly set in the `NOTEBOOK_FOLDER` constant.  You can run the tests using `pytest`.


## Notes

- The code ensures that the `tinytroupe` package is imported from the parent directory to avoid import errors.
- It appends ".executed.local.ipynb" to the original file name when saving the executed notebook.
- Handles encoding issues (`utf-8`) when reading and writing files.
- Includes error handling (try-except) to catch and report exceptions during notebook execution.