```python
import pytest
import os

# Dummy functions to represent the actual code (replace with your actual code)
def greet_user():
    return "Hi!"

def train_model(data, data_dir, positive, attachment):
    # Dummy training logic
    if data:
        print(f"Training with data: {data}")
    elif data_dir:
        print(f"Training with directory: {data_dir}")
    elif attachment:
        print(f"Training with attachment: {attachment}")
    else:
        raise ValueError("No training data provided.")

def test_model(test_data):
    # Dummy testing logic
    if isinstance(test_data, dict):
        print(f"Testing with data: {test_data}")
        return "Test results"
    else:
        raise TypeError("Test data must be a JSON object.")

def archive_files(directory):
    # Dummy archiving logic
    if os.path.exists(directory):
        print(f"Archiving files in {directory}")
        return "Files archived successfully"
    else:
        raise FileNotFoundError(f"Directory {directory} not found.")

def select_dataset(path_to_dir_positive, positive):
    # Dummy selection logic
    if os.path.isdir(path_to_dir_positive):
        print(f"Selected dataset from {path_to_dir_positive} for {positive}")
        return "Dataset selected successfully"
    else:
        raise FileNotFoundError(f"Directory {path_to_dir_positive} not found.")


def test_greet_user():
    """Tests the greeting function."""
    assert greet_user() == "Hi!"

def test_train_model_data():
    """Tests training with data."""
    train_model("some_data", None, None, None)


def test_train_model_dir():
    """Tests training with directory."""
    train_model(None, "some_dir", None, None)

def test_train_model_attachment():
    """Tests training with attachment."""
    train_model(None, None, None, "some_attachment")

def test_train_model_no_data():
    """Tests training with no data."""
    with pytest.raises(ValueError, match="No training data provided."):
        train_model(None, None, None, None)

def test_test_model_valid_input():
    """Tests model testing with valid input."""
    assert test_model({"test": "data"}) == "Test results"


def test_test_model_invalid_input():
    """Tests model testing with invalid input."""
    with pytest.raises(TypeError, match="Test data must be a JSON object."):
        test_model("invalid_data")

def test_archive_files_exists():
    """Tests archiving files in an existing directory."""
    # Simulate a directory for testing
    test_dir = "test_dir"
    os.makedirs(test_dir, exist_ok=True)
    assert archive_files(test_dir) == "Files archived successfully"
    os.rmdir(test_dir)


def test_archive_files_not_exists():
    """Tests archiving files in a non-existent directory."""
    with pytest.raises(FileNotFoundError, match="Directory"):
        archive_files("nonexistent_dir")

def test_select_dataset_valid():
    """Tests selecting a dataset from a valid directory."""
    # Simulate a directory for testing
    test_dir = "test_dir"
    os.makedirs(test_dir, exist_ok=True)
    assert select_dataset(test_dir, "positive") == "Dataset selected successfully"
    os.rmdir(test_dir)


def test_select_dataset_invalid():
    """Tests selecting a dataset from an invalid directory."""
    with pytest.raises(FileNotFoundError, match="Directory"):
        select_dataset("nonexistent_dir", "positive")

```