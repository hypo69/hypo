```python
import pytest
import os

# Dummy functions (replace with your actual functions)
def greet_user():
    return "Hi!"

def train_model(data, data_dir, positive, attachment):
    # Dummy training logic
    if data_dir:
        return f"Training with directory: {data_dir}"
    elif data:
        return f"Training with file: {data}"
    elif attachment:
        return f"Training with attachment: {attachment}"
    else:
        return "No training data provided."


def test_model(test_data):
    # Dummy model testing logic
    if isinstance(test_data, dict):
        return "Model tested with valid JSON data."
    else:
        return "Invalid test data format."
    

def archive_files(directory):
    # Dummy archiving logic
    if os.path.exists(directory):
        return f"Archived files in {directory}."
    else:
        return f"Directory {directory} does not exist."

def select_dataset(path_to_dir_positive, positive):
    # Dummy dataset selection logic
    return f"Selected dataset from {path_to_dir_positive} with positive class {positive}."

def display_instruction():
    return "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."


# Fixtures (adjust as needed)
@pytest.fixture
def valid_test_data():
    return {"input": "test_input", "output": "test_output"}


@pytest.fixture
def invalid_test_data():
    return "invalid_test_data"

@pytest.fixture
def valid_directory():
    return "dummy_directory"

@pytest.fixture
def non_existent_directory():
    return "nonexistent_directory"



# Tests for each function
def test_greet_user():
    assert greet_user() == "Hi!"

def test_train_model_with_file(valid_test_data):
    result = train_model("data.txt", None, "positive", None)
    assert "Training with file: data.txt" in result

def test_train_model_with_directory(valid_directory):
    result = train_model(None, valid_directory, "positive", None)
    assert "Training with directory: dummy_directory" in result


def test_train_model_with_invalid_input():
    result = train_model(None, None, None, None)
    assert "No training data provided." in result

def test_test_model_valid_data(valid_test_data):
    result = test_model(valid_test_data)
    assert "Model tested with valid JSON data." == result

def test_test_model_invalid_data(invalid_test_data):
    result = test_model(invalid_test_data)
    assert "Invalid test data format." in result



def test_archive_files_existing_directory(valid_directory):
    result = archive_files(valid_directory)
    assert f"Archived files in {valid_directory}." in result

def test_archive_files_nonexistent_directory(non_existent_directory):
    result = archive_files(non_existent_directory)
    assert f"Directory {non_existent_directory} does not exist." in result


def test_select_dataset(valid_directory):
    result = select_dataset(valid_directory, "positive")
    assert f"Selected dataset from {valid_directory} with positive class positive." in result

def test_instruction():
  assert display_instruction() == "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."
```