```python
import pytest
import os
import csv
import json
from pathlib import Path
from src.utils.csv import save_csv_file, read_csv_file, read_csv_as_json, read_csv_as_dict, read_csv_as_ns

# Fixture for creating a test CSV file
@pytest.fixture
def temp_csv_file(tmp_path):
    """Creates a temporary CSV file for testing."""
    file_path = tmp_path / "test.csv"
    data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
    ]
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return file_path

# Fixture for creating a test CSV file with numeric data
@pytest.fixture
def temp_numeric_csv_file(tmp_path):
    """Creates a temporary CSV file with numeric data for testing."""
    file_path = tmp_path / "numeric_test.csv"
    data = [
        {"col1": 1, "col2": 2, "col3": 3},
        {"col1": 4, "col2": 5, "col3": 6},
    ]
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return file_path


# Fixture for creating a test CSV file with missing data
@pytest.fixture
def temp_missing_csv_file(tmp_path):
    """Creates a temporary CSV file with missing data for testing."""
    file_path = tmp_path / "missing_test.csv"
    data = [
        {"name": "Alice", "age": "30"},
        {"name": "Bob", "city": "Los Angeles"},
    ]
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= ["name", "age", "city"])
        writer.writeheader()
        writer.writerows(data)
    return file_path

# Tests for save_csv_file function
def test_save_csv_file_valid_input(tmp_path):
    """Checks saving a CSV file with valid input."""
    file_path = tmp_path / "output.csv"
    data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
    assert save_csv_file(data, file_path) is True
    assert file_path.exists()

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert rows == data

def test_save_csv_file_invalid_data_type(tmp_path):
    """Checks TypeError is raised when input data is not a list."""
    file_path = tmp_path / "output.csv"
    data = "invalid"
    with pytest.raises(TypeError) as excinfo:
        save_csv_file(data, file_path)
    assert "Input data must be a list of dictionaries." in str(excinfo.value)

def test_save_csv_file_empty_data(tmp_path):
    """Checks ValueError is raised when input data is empty."""
    file_path = tmp_path / "output.csv"
    data = []
    with pytest.raises(ValueError) as excinfo:
        save_csv_file(data, file_path)
    assert "Input data cannot be empty." in str(excinfo.value)

def test_save_csv_file_append_mode(tmp_path):
    """Checks CSV file is appended correctly in append mode."""
    file_path = tmp_path / "append.csv"
    data1 = [{"name": "Alice", "age": "30"}]
    data2 = [{"name": "Bob", "age": "25"}]
    save_csv_file(data1, file_path, mode='w')  # Create initial file with write mode
    save_csv_file(data2, file_path, mode='a')  # Append to existing file in append mode
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert rows == data1 + data2

def test_save_csv_file_overwrite_mode(tmp_path):
    """Checks CSV file is overwritten correctly in write mode."""
    file_path = tmp_path / "overwrite.csv"
    data1 = [{"name": "Alice", "age": "30"}]
    data2 = [{"name": "Bob", "age": "25"}]
    save_csv_file(data1, file_path, mode='w')  # Create initial file
    save_csv_file(data2, file_path, mode='w') # Overwrite the file
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert rows == data2

def test_save_csv_file_invalid_file_path(tmp_path, caplog):
    """Checks that saving the CSV to an invalid file path returns False and logs an error"""
    invalid_file_path = tmp_path / 'non_existent_dir' / "test.csv"
    data = [{"name": "Alice", "age": "30"}]
    assert save_csv_file(data, invalid_file_path) is False
    assert f"Failed to save CSV to {invalid_file_path}" in caplog.text

# Tests for read_csv_file function
def test_read_csv_file_valid_input(temp_csv_file):
    """Checks reading a CSV file with valid input."""
    expected_data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
    ]
    result = read_csv_file(temp_csv_file)
    assert result == expected_data

def test_read_csv_file_file_not_found(tmp_path, caplog):
    """Checks that reading a non-existent CSV file returns None and logs an error."""
    file_path = tmp_path / "non_existent.csv"
    result = read_csv_file(file_path)
    assert result is None
    assert f"File not found: {file_path}" in caplog.text

def test_read_csv_file_invalid_file_path(tmp_path, caplog):
   """Checks that reading from an invalid file path returns None and logs an error."""
   file_path = tmp_path / "invalid_dir" / "test.csv"
   result = read_csv_file(file_path)
   assert result is None
   assert f"Failed to read CSV from {file_path}" in caplog.text

def test_read_csv_file_empty_file(tmp_path):
    """Checks that reading an empty CSV file returns an empty list."""
    file_path = tmp_path / "empty.csv"
    file_path.touch()
    result = read_csv_file(file_path)
    assert result == []

def test_read_csv_file_missing_data(temp_missing_csv_file):
     """Checks reading a CSV file with missing fields."""
     expected_data = [
        {'name': 'Alice', 'age': '30', 'city': None},
        {'name': 'Bob', 'age': None, 'city': 'Los Angeles'},
    ]
     result = read_csv_file(temp_missing_csv_file)
     assert result == expected_data

# Tests for read_csv_as_json function
def test_read_csv_as_json_valid_input(temp_csv_file, tmp_path):
    """Checks converting a valid CSV file to JSON."""
    json_file_path = tmp_path / "output.json"
    assert read_csv_as_json(temp_csv_file, json_file_path) is True
    assert json_file_path.exists()
    with open(json_file_path, 'r', encoding='utf-8') as file:
        result = json.load(file)
    expected_data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
    ]
    assert result == expected_data

def test_read_csv_as_json_csv_not_found(tmp_path, caplog):
    """Checks that attempting to convert non-existent CSV file returns False and logs an error."""
    csv_file_path = tmp_path / "non_existent.csv"
    json_file_path = tmp_path / "output.json"
    assert read_csv_as_json(csv_file_path, json_file_path) is False
    assert f"File not found: {csv_file_path}" in caplog.text

def test_read_csv_as_json_invalid_csv(tmp_path, caplog):
    """Checks that reading from an invalid CSV file path returns False and logs an error."""
    csv_file_path = tmp_path / "invalid_dir" / "test.csv"
    json_file_path = tmp_path / "output.json"
    assert read_csv_as_json(csv_file_path, json_file_path) is False
    assert f"Failed to convert CSV to JSON at {json_file_path}" in caplog.text

def test_read_csv_as_json_invalid_json_path(temp_csv_file, tmp_path, caplog):
    """Checks that saving to an invalid JSON file path returns False and logs an error."""
    json_file_path = tmp_path / "invalid_dir" / "output.json"
    assert read_csv_as_json(temp_csv_file, json_file_path) is False
    assert f"Failed to convert CSV to JSON at {json_file_path}" in caplog.text

def test_read_csv_as_json_empty_csv(tmp_path):
    """Checks that converting an empty CSV file to JSON results in an empty JSON array."""
    csv_file_path = tmp_path / "empty.csv"
    csv_file_path.touch()
    json_file_path = tmp_path / "output.json"
    assert read_csv_as_json(csv_file_path, json_file_path) is True

    with open(json_file_path, 'r', encoding='utf-8') as f:
        result = json.load(f)
    assert result == []

# Tests for read_csv_as_dict function
def test_read_csv_as_dict_valid_input(temp_csv_file):
    """Checks reading a valid CSV file and converting it to a dictionary."""
    expected_data = {
        "data": [
            {"name": "Alice", "age": "30", "city": "New York"},
            {"name": "Bob", "age": "25", "city": "Los Angeles"},
        ]
    }
    result = read_csv_as_dict(temp_csv_file)
    assert result == expected_data

def test_read_csv_as_dict_file_not_found(tmp_path, caplog):
    """Checks reading a non-existent CSV file returns None and logs an error."""
    csv_file_path = tmp_path / "non_existent.csv"
    result = read_csv_as_dict(csv_file_path)
    assert result is None
    assert "Failed to read CSV as dictionary" in caplog.text

def test_read_csv_as_dict_invalid_file_path(tmp_path, caplog):
    """Checks reading from an invalid CSV file path returns None and logs an error."""
    csv_file_path = tmp_path / "invalid_dir" / "test.csv"
    result = read_csv_as_dict(csv_file_path)
    assert result is None
    assert "Failed to read CSV as dictionary" in caplog.text

def test_read_csv_as_dict_empty_csv(tmp_path):
    """Checks that reading an empty CSV file returns an empty dictionary."""
    csv_file_path = tmp_path / "empty.csv"
    csv_file_path.touch()
    result = read_csv_as_dict(csv_file_path)
    assert result == {"data": []}

def test_read_csv_as_dict_missing_data(temp_missing_csv_file):
    """Checks reading a CSV file with missing fields."""
    expected_data = {
        "data": [
            {'name': 'Alice', 'age': '30', 'city': None},
            {'name': 'Bob', 'age': None, 'city': 'Los Angeles'},
        ]
    }
    result = read_csv_as_dict(temp_missing_csv_file)
    assert result == expected_data

# Tests for read_csv_as_ns function
def test_read_csv_as_ns_valid_input(temp_csv_file):
    """Checks reading a valid CSV file and converting it to a list of dictionaries."""
    expected_data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
    ]
    result = read_csv_as_ns(temp_csv_file)
    assert result == expected_data

def test_read_csv_as_ns_file_not_found(tmp_path, caplog):
    """Checks reading a non-existent CSV file returns an empty list and logs an error."""
    csv_file_path = tmp_path / "non_existent.csv"
    result = read_csv_as_ns(csv_file_path)
    assert result == []
    assert f"File not found: {csv_file_path}" in caplog.text

def test_read_csv_as_ns_invalid_file_path(tmp_path, caplog):
     """Checks reading from an invalid file path returns empty list and logs an error."""
     csv_file_path = tmp_path / "invalid_dir" / "test.csv"
     result = read_csv_as_ns(csv_file_path)
     assert result == []
     assert f"Failed to load CSV as dictionaries from {csv_file_path}" in caplog.text

def test_read_csv_as_ns_empty_csv(tmp_path):
    """Checks that reading an empty CSV file returns an empty list."""
    csv_file_path = tmp_path / "empty.csv"
    csv_file_path.touch()
    result = read_csv_as_ns(csv_file_path)
    assert result == []

def test_read_csv_as_ns_numeric_data(temp_numeric_csv_file):
    """Checks reading a CSV file with numeric fields."""
    expected_data = [
        {"col1": 1, "col2": 2, "col3": 3},
        {"col1": 4, "col2": 5, "col3": 6},
    ]
    result = read_csv_as_ns(temp_numeric_csv_file)
    assert result == expected_data

def test_read_csv_as_ns_missing_data(temp_missing_csv_file):
     """Checks reading a CSV file with missing fields."""
     expected_data = [
        {'name': 'Alice', 'age': '30', 'city': None},
        {'name': 'Bob', 'age': None, 'city': 'Los Angeles'},
     ]
     result = read_csv_as_ns(temp_missing_csv_file)
     assert result == expected_data
```