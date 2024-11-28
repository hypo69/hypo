```python
import pytest
import os

# Mock functions (replace with actual implementation for testing)
def greet_user():
    return "Hello!"

def train_model(data, data_dir, positive, attachment):
    # Mock training logic
    if data:
        print(f"Training with data: {data}")
    elif data_dir:
        print(f"Training with directory: {data_dir}")
    elif attachment:
        print(f"Training with attachment: {attachment}")
    else:
        raise ValueError("No data or directory provided for training.")
    return "Model trained."

def test_model(test_data):
    # Mock testing logic
    print(f"Testing with data: {test_data}")
    return "Model tested."

def archive_files(directory):
    # Mock archiving logic
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")
    print(f"Archiving files in directory: {directory}")
    return "Files archived."

def select_dataset(path_to_dir_positive, positive):
    # Mock dataset selection logic
    if not os.path.isdir(path_to_dir_positive):
        raise FileNotFoundError(f"Directory '{path_to_dir_positive}' not found.")
    print(f"Selected dataset: {path_to_dir_positive}, positive: {positive}")
    return "Dataset selected."

def display_instructions():
    return "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."

# Test functions for each command

def test_greet_user():
    assert greet_user() == "Hello!"


def test_train_model_data():
    assert train_model(data="some_data.txt", data_dir=None, positive=True, attachment=None) == "Model trained."

def test_train_model_directory():
    assert train_model(data=None, data_dir="data_dir", positive=False, attachment=None) == "Model trained."

def test_train_model_attachment():
    assert train_model(data=None, data_dir=None, positive=True, attachment="attachment.pdf") == "Model trained."

def test_train_model_no_input():
    with pytest.raises(ValueError):
      train_model(data=None, data_dir=None, positive=None, attachment=None)

def test_test_model():
  assert test_model(test_data='{"data": "test"}') == "Model tested."

def test_archive_files_existing_dir():
    # Mock checking directory existence
    os.path.exists = lambda x: True
    assert archive_files("test_dir") == "Files archived."

def test_archive_files_nonexistent_dir():
    # Mock checking directory existence
    os.path.exists = lambda x: False
    with pytest.raises(FileNotFoundError, match=r"Directory"):
      archive_files("nonexistent_dir")

def test_select_dataset_existing_dir():
    # Mock checking directory existence
    os.path.isdir = lambda x: True
    assert select_dataset("test_dir", "positive") == "Dataset selected."

def test_select_dataset_nonexistent_dir():
    # Mock checking directory existence
    os.path.isdir = lambda x: False
    with pytest.raises(FileNotFoundError, match=r"Directory"):
      select_dataset("nonexistent_dir", "positive")

def test_display_instructions():
  instructions = display_instructions()
  assert isinstance(instructions,str)

```