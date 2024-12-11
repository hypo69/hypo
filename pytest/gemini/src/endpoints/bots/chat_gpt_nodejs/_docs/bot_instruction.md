```python
import pytest
import os

# Placeholder for the actual code (replace with the provided code)
def greet_user():
    return "Hi there!"

def train_model(data, data_dir, positive, attachment):
    if data:
        # Simulate training with data
        return f"Training with data: {data}"
    elif data_dir:
        # Simulate training with directory
        return f"Training with directory: {data_dir}"
    elif attachment:
        # Simulate training with attachment
        return f"Training with attachment: {attachment}"
    else:
        return "No data provided for training."


def test_model(test_data):
    if isinstance(test_data, dict):
        # Simulate testing with JSON data
        return "Model tested with: " + str(test_data)
    else:
        return "Invalid test data format."

def archive_files(directory):
  if os.path.exists(directory):
    # Simulate archiving
    return f"Archived files in: {directory}"
  else:
    return f"Directory not found: {directory}"

def select_dataset(path_to_dir_positive, positive):
    if os.path.isdir(path_to_dir_positive):
      return f"Selected dataset: {path_to_dir_positive} with positive: {positive}"
    else:
      raise FileNotFoundError("Directory not found")

def display_instruction():
  return "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."


# Fixtures (replace with actual data if needed)
@pytest.fixture
def example_data():
    return {"key1": "value1", "key2": 123}

@pytest.fixture
def valid_directory_path():
    return "test_directory"

def test_greet_user():
  assert greet_user() == "Hi there!"

def test_train_model_with_data():
  result = train_model("some_data.txt", None, None, None)
  assert "Training with data: some_data.txt" in result

def test_train_model_with_directory():
  result = train_model(None, "data_directory", None, None)
  assert "Training with directory: data_directory" in result


def test_train_model_with_attachment():
  result = train_model(None, None, None, "attachment.pdf")
  assert "Training with attachment: attachment.pdf" in result


def test_train_model_no_data():
  result = train_model(None, None, None, None)
  assert "No data provided for training." in result

def test_test_model_valid_input(example_data):
  result = test_model(example_data)
  assert "Model tested with: " in result

def test_test_model_invalid_input():
  result = test_model("invalid_data")
  assert "Invalid test data format." in result

def test_archive_files_valid_directory(valid_directory_path):
  result = archive_files(valid_directory_path)
  assert "Archived files in: test_directory" in result


def test_archive_files_invalid_directory():
  result = archive_files("nonexistent_directory")
  assert "Directory not found: nonexistent_directory" in result

def test_select_dataset_valid_directory(valid_directory_path):
  result = select_dataset(valid_directory_path, "positive_data")
  assert "Selected dataset: test_directory" in result

def test_select_dataset_invalid_directory():
    with pytest.raises(FileNotFoundError):
        select_dataset("nonexistent_directory", "positive_data")

def test_display_instruction():
    assert display_instruction() == "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."


```