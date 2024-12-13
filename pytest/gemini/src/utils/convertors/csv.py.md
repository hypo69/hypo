```python
import pytest
from pathlib import Path
from types import SimpleNamespace
from src.utils.convertors.csv import csv2dict, csv2ns, csv_to_json
from src.utils.csv import read_csv_as_dict, read_csv_as_ns, save_csv_file
import tempfile
import json
import os

# Fixture for creating a temporary CSV file
@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_file:
        tmp_file.write("name,age,city\n")
        tmp_file.write("John,30,New York\n")
        tmp_file.write("Alice,25,Los Angeles\n")
    yield tmp_file.name
    os.remove(tmp_file.name)

# Fixture for creating a temporary CSV file with empty data
@pytest.fixture
def empty_csv_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_file:
        pass  # Empty file
    yield tmp_file.name
    os.remove(tmp_file.name)

# Fixture for creating a temporary CSV file with no header
@pytest.fixture
def no_header_csv_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_file:
        tmp_file.write("John,30,New York\n")
        tmp_file.write("Alice,25,Los Angeles\n")
    yield tmp_file.name
    os.remove(tmp_file.name)

@pytest.fixture
def temp_json_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
        pass
    yield tmp_file.name
    os.remove(tmp_file.name)

# Tests for csv2dict function
def test_csv2dict_valid_input(temp_csv_file):
    """Checks correct behavior of csv2dict with valid input."""
    result = csv2dict(temp_csv_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"name": "John", "age": "30", "city": "New York"}
    assert result[1] == {"name": "Alice", "age": "25", "city": "Los Angeles"}

def test_csv2dict_empty_file(empty_csv_file):
    """Checks behavior of csv2dict with an empty CSV file."""
    result = csv2dict(empty_csv_file)
    assert result == []  # Expecting an empty list for empty csv

def test_csv2dict_no_header(no_header_csv_file):
    """Checks behavior of csv2dict with a CSV file having no header."""
    result = csv2dict(no_header_csv_file)
    assert result == [] # should return none for no header

def test_csv2dict_invalid_file():
    """Checks behavior of csv2dict with an invalid file path."""
    result = csv2dict("invalid_file.csv")
    assert result == None

def test_csv2dict_with_encoding(temp_csv_file):
    """Checks correct behavior of csv2dict with a specific encoding."""
    result = csv2dict(temp_csv_file, encoding='utf-8')
    assert isinstance(result, list)

# Tests for csv2ns function
def test_csv2ns_valid_input(temp_csv_file):
    """Checks correct behavior of csv2ns with valid input."""
    result = csv2ns(temp_csv_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], SimpleNamespace)
    assert result[0].name == "John"
    assert result[0].age == "30"
    assert result[0].city == "New York"
    assert result[1].name == "Alice"
    assert result[1].age == "25"
    assert result[1].city == "Los Angeles"


def test_csv2ns_empty_file(empty_csv_file):
    """Checks behavior of csv2ns with an empty CSV file."""
    result = csv2ns(empty_csv_file)
    assert result == []


def test_csv2ns_no_header(no_header_csv_file):
    """Checks behavior of csv2ns with a CSV file having no header."""
    result = csv2ns(no_header_csv_file)
    assert result == []

def test_csv2ns_invalid_file():
    """Checks behavior of csv2ns with an invalid file path."""
    result = csv2ns("invalid_file.csv")
    assert result == None

def test_csv2ns_with_encoding(temp_csv_file):
    """Checks correct behavior of csv2ns with a specific encoding."""
    result = csv2ns(temp_csv_file, encoding='utf-8')
    assert isinstance(result, list)

# Tests for csv_to_json function
def test_csv_to_json_valid_input(temp_csv_file, temp_json_file):
    """Checks correct behavior of csv_to_json with valid input."""
    result = csv_to_json(temp_csv_file, temp_json_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"name": "John", "age": "30", "city": "New York"}
    assert result[1] == {"name": "Alice", "age": "25", "city": "Los Angeles"}

    # Verify that the JSON file was created and has content
    with open(temp_json_file, 'r', encoding='utf-8') as f:
      json_content = json.load(f)
      assert json_content == result

def test_csv_to_json_empty_file(empty_csv_file, temp_json_file):
    """Checks behavior of csv_to_json with an empty CSV file."""
    result = csv_to_json(empty_csv_file, temp_json_file)
    assert result == []

    with open(temp_json_file, 'r', encoding='utf-8') as f:
        json_content = json.load(f)
        assert json_content == []

def test_csv_to_json_no_header(no_header_csv_file, temp_json_file):
    """Checks behavior of csv_to_json with a CSV file having no header."""
    result = csv_to_json(no_header_csv_file, temp_json_file)
    assert result == None

    with open(temp_json_file, 'r', encoding='utf-8') as f:
      # Expect to fail
      with pytest.raises(json.JSONDecodeError):
        json.load(f)


def test_csv_to_json_invalid_csv_file(temp_json_file):
    """Checks behavior of csv_to_json with an invalid CSV file."""
    result = csv_to_json("invalid_file.csv", temp_json_file)
    assert result == None

    with open(temp_json_file, 'r', encoding='utf-8') as f:
      # Expect to fail
      with pytest.raises(json.JSONDecodeError):
        json.load(f)

def test_csv_to_json_invalid_json_file(temp_csv_file):
    """Checks behavior of csv_to_json with an invalid JSON file."""
    result = csv_to_json(temp_csv_file, "/invalid/path/file.json")
    assert result is None

def test_csv_to_json_with_encoding(temp_csv_file, temp_json_file):
    """Checks correct behavior of csv_to_json with a specific encoding."""
    result = csv_to_json(temp_csv_file, temp_json_file)
    assert isinstance(result, list)


def test_csv_to_json_exc_info_false(temp_csv_file, temp_json_file):
        """Checks correct behavior of csv_to_json with exc_info = False."""
        result = csv_to_json(temp_csv_file, temp_json_file, exc_info=False)
        assert result is not None
```