```python
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
import sys

# Add the necessary paths to ensure that the package is imported correctly
sys.path.insert(0, '../../tinytroupe/')
sys.path.insert(0, '../../')
sys.path.insert(0, '../')

# Set the folder containing the notebooks
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

@pytest.fixture(scope="session")
def all_notebooks():
    """Fixture that returns a list of all notebook paths to test."""
    return get_notebooks(NOTEBOOK_FOLDER)


def test_get_notebooks():
    """Test that the `get_notebooks` function returns a list of .ipynb files."""
    notebooks = get_notebooks(NOTEBOOK_FOLDER)
    assert isinstance(notebooks, list), "get_notebooks should return a list"
    for notebook in notebooks:
        assert notebook.endswith(".ipynb"), "Returned files should be .ipynb files"
        assert ".executed." not in notebook, "Returned files should not contain '.executed.'"
        assert ".local." not in notebook, "Returned files should not contain '.local.'"
    
    # Test case when folder is not a valid directory
    with pytest.raises(FileNotFoundError):
      get_notebooks("invalid_folder_path")


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path):
    """Test execution of Jupyter notebooks, ensuring no exceptions are raised."""
    with open(notebook_path, "r", encoding="utf-8") as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)
        print(f"Executing notebook: {notebook_path} with kernel: {KERNEL_NAME}")
        ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)

        try:
            ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})
            print(f"Notebook {notebook_path} executed successfully.")

        except Exception as e:
            pytest.fail(f"Notebook {notebook_path} raised an exception: {e}")

        finally:
            # save a copy of the executed notebook
            output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
            with open(output_path, "w", encoding="utf-8") as out_file:
                nbformat.write(notebook, out_file)
            
            print(f"Executed notebook saved as: {output_path}")
            # Check if the executed notebook file has been created and it exists
            assert os.path.exists(output_path), f"Executed notebook file {output_path} was not created"


def test_notebook_execution_timeout():
    """Test that a notebook that exceeds timeout will fail."""
    # Create a dummy notebook file for testing a timeout
    dummy_notebook_path = os.path.join(NOTEBOOK_FOLDER, "timeout_test_notebook.ipynb")
    
    if not os.path.exists(NOTEBOOK_FOLDER):
      os.makedirs(NOTEBOOK_FOLDER)

    with open(dummy_notebook_path, "w", encoding="utf-8") as f:
        nb = nbformat.v4.new_notebook()
        nb.cells.append(nbformat.v4.new_code_cell("import time; time.sleep(1200)")) # sleep for 20 minutes
        nbformat.write(nb, f)

    with pytest.raises(pytest.fail.Exception) as excinfo:
        with open(dummy_notebook_path, "r", encoding="utf-8") as nb_file:
            notebook = nbformat.read(nb_file, as_version=4)
            ep = ExecutePreprocessor(timeout=1, kernel_name=KERNEL_NAME) # timeout of 1 second
            ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})

    assert "Notebook" in str(excinfo.value), "The error message should mention 'Notebook'"
    assert "raised an exception" in str(excinfo.value), "The error message should indicate an exception was raised."

    # clean up the dummy file
    os.remove(dummy_notebook_path)
    
    
def test_no_notebooks():
    """Test when the notebook folder is empty"""
    empty_folder = os.path.join(NOTEBOOK_FOLDER, "empty_folder")
    if not os.path.exists(empty_folder):
        os.makedirs(empty_folder)
        
    notebooks = get_notebooks(empty_folder)
    
    assert len(notebooks) == 0, "There should be no notebooks"
    
    # clean up the dummy file
    os.rmdir(empty_folder)
```