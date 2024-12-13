```python
import pytest
import os
import shutil
import json
from unittest.mock import patch

# Since the provided code is a set of instructions for a bot, we'll mock the underlying bot functions 
# and test how it handles the commands based on the instructions provided.

# Mock the bot functions
@pytest.fixture
def mock_bot_functions():
    class MockBot:
        def __init__(self):
            self.training_data = {}
            self.selected_dataset = None
            self.archive_dir = None

        def greet(self):
            return "Hello!"

        def train(self, data, data_dir, positive, attachment=None):
            self.training_data = {
                "data": data,
                "data_dir": data_dir,
                "positive": positive,
                "attachment": attachment,
            }
            return "Training started."
            
        def test(self, test_data):
          try:
            json.loads(test_data)
            return "Testing started."
          except json.JSONDecodeError:
            return "Invalid JSON test data"

        def archive(self, directory):
            self.archive_dir = directory
            return "Archiving started."
        
        def select_dataset(self, path_to_dir_positive, positive):
            self.selected_dataset = {
                "path": path_to_dir_positive,
                "positive": positive,
            }
            return "Dataset selected."

        def instruction(self):
            return "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."
    
    return MockBot()

# Test cases for !hi command
def test_greet_command(mock_bot_functions):
    """Checks the greeting command."""
    assert mock_bot_functions.greet() == "Hello!"

# Test cases for !train command
def test_train_command_with_data(mock_bot_functions):
    """Checks the train command with file data."""
    result = mock_bot_functions.train("file_data", None, "positive_label")
    assert result == "Training started."
    assert mock_bot_functions.training_data == {
        "data": "file_data",
        "data_dir": None,
        "positive": "positive_label",
        "attachment": None,
    }

def test_train_command_with_data_dir(mock_bot_functions):
    """Checks the train command with directory data."""
    result = mock_bot_functions.train(None, "data_dir", "positive_label")
    assert result == "Training started."
    assert mock_bot_functions.training_data == {
        "data": None,
        "data_dir": "data_dir",
        "positive": "positive_label",
        "attachment": None,
    }


def test_train_command_with_attachment(mock_bot_functions):
    """Checks the train command with attachment."""
    result = mock_bot_functions.train(None, None, "positive_label", "attachment_file")
    assert result == "Training started."
    assert mock_bot_functions.training_data == {
        "data": None,
        "data_dir": None,
        "positive": "positive_label",
        "attachment": "attachment_file",
    }


# Test cases for !test command
def test_test_command_valid_json(mock_bot_functions):
    """Checks the test command with valid JSON."""
    test_json = '{"key": "value"}'
    assert mock_bot_functions.test(test_json) == "Testing started."

def test_test_command_invalid_json(mock_bot_functions):
    """Checks the test command with invalid JSON."""
    test_json = 'invalid json'
    assert mock_bot_functions.test(test_json) == "Invalid JSON test data"


# Test cases for !archive command
def test_archive_command(mock_bot_functions):
    """Checks the archive command."""
    result = mock_bot_functions.archive("archive_dir")
    assert result == "Archiving started."
    assert mock_bot_functions.archive_dir == "archive_dir"


# Test cases for !select_dataset command
def test_select_dataset_command(mock_bot_functions):
    """Checks the select dataset command."""
    result = mock_bot_functions.select_dataset("dataset_path", "positive_label")
    assert result == "Dataset selected."
    assert mock_bot_functions.selected_dataset == {
        "path": "dataset_path",
        "positive": "positive_label",
    }


# Test cases for !instruction command
def test_instruction_command(mock_bot_functions):
    """Checks the instruction command."""
    expected_instruction = "!hi: Greets the user.\n!train <data> <data_dir> <positive> <attachment>: Trains the model with the provided data. Use data for a file, data_dir for a directory, or attachment for a file attachment.\n!test <test_data>: Tests the model with provided JSON test data.\n!archive <directory>: Archives files in the specified directory.\n!select_dataset <path_to_dir_positive> <positive>: Selects a dataset for training from the specified directory.\n!instruction: Displays this instruction message."
    assert mock_bot_functions.instruction() == expected_instruction
```