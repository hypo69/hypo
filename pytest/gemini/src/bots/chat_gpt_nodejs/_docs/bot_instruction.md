```python
import pytest
import os

# Mock functions (replace with actual implementations if available)
def greet_user():
    return "Hello!"

def train_model(data, data_dir, positive, attachment):
    # Mock training logic
    if data:
        return f"Training with data: {data}"
    elif data_dir:
        return f"Training with data directory: {data_dir}"
    elif attachment:
        return f"Training with attachment: {attachment}"
    else:
        raise ValueError("No training data provided.")

def test_model(test_data):
    # Mock testing logic
    if isinstance(test_data, dict):
        return "Model tested with data: " + str(test_data)
    else:
        raise TypeError("Test data must be a JSON dictionary.")

def archive_files(directory):
    # Mock archiving logic
    if os.path.isdir(directory):
        return f"Archived files in directory: {directory}"
    else:
        raise ValueError(f"Directory '{directory}' does not exist.")


def select_dataset(path_to_dir_positive, positive):
  # Mock logic, checking for existing directory
  if os.path.isdir(path_to_dir_positive):
    return f"Selected dataset from {path_to_dir_positive} with positive: {positive}"
  else:
      raise ValueError(f"Directory '{path_to_dir_positive}' does not exist.")
  
def display_instruction():
  return "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."

# Fixture (replace with actual data if applicable)
@pytest.fixture
def valid_test_data():
  return {"input": "test", "output": "result"}

@pytest.fixture
def valid_directory():
    # Create a temporary directory for testing
    temp_dir = "temp_dir"
    os.makedirs(temp_dir, exist_ok=True)
    yield temp_dir
    # Clean up the temporary directory
    os.rmdir(temp_dir)

# Tests for each command
def test_greet_user():
    assert greet_user() == "Hello!"

def test_train_model_data(valid_test_data):
  result = train_model(valid_test_data, "", "", "")
  assert isinstance(result,str)


def test_train_model_data_dir():
  result = train_model("", "data_dir", "", "")
  assert isinstance(result, str)

def test_train_model_invalid_input():
  with pytest.raises(ValueError):
    train_model("", "", "", "")

def test_test_model_valid_input(valid_test_data):
    result = test_model(valid_test_data)
    assert isinstance(result,str)

def test_test_model_invalid_input():
    with pytest.raises(TypeError):
        test_model("invalid_data")

def test_archive_files_valid_directory(valid_directory):
    result = archive_files(valid_directory)
    assert isinstance(result, str)
    
def test_archive_files_invalid_directory():
    with pytest.raises(ValueError):
        archive_files("invalid_directory")


def test_select_dataset_valid_directory(valid_directory):
    result = select_dataset(valid_directory, "positive")
    assert isinstance(result, str)

def test_select_dataset_invalid_directory():
    with pytest.raises(ValueError):
        select_dataset("invalid_directory", "positive")
        
def test_instruction():
  assert display_instruction() == "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."
```