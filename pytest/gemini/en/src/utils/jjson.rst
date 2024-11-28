```python
import pytest
from pathlib import Path
from hypotez.src.utils.jjson import j_dumps, j_loads, j_loads_ns, replace_key_in_json, process_json_file, recursive_process_json_files, extract_json_from_string
from types import SimpleNamespace
import json
import os
from unittest.mock import patch


# Sample data for testing
SAMPLE_JSON_DATA = {"name": "John Doe", "age": 30, "city": "New York"}
SAMPLE_JSON_DATA2 = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]
SAMPLE_NESTED_JSON_DATA = {"outer": {"inner": {"name": "Inner John"}}}

# Create a temporary directory for testing
TEST_DIR = Path("./test_data")
TEST_DIR.mkdir(parents=True, exist_ok=True)

# Create sample JSON files for testing
(TEST_DIR / "test1.json").write_text(json.dumps(SAMPLE_JSON_DATA, indent=4))
(TEST_DIR / "test2.json").write_text(json.dumps(SAMPLE_JSON_DATA2, indent=4))
(TEST_DIR / "nested.json").write_text(json.dumps(SAMPLE_NESTED_JSON_DATA, indent=4))


@pytest.fixture
def sample_json_data():
    return SAMPLE_JSON_DATA


@pytest.fixture
def sample_json_data2():
    return SAMPLE_JSON_DATA2


@pytest.fixture
def sample_nested_json_data():
    return SAMPLE_NESTED_JSON_DATA

@pytest.fixture
def dummy_markdown():
    return "```json\n{ \"name\": \"John\" }\n```"


def test_j_dumps_valid_input(sample_json_data):
    """Tests j_dumps with valid dictionary input."""
    temp_file = Path("./temp_output.json")
    j_dumps(sample_json_data, file_path=temp_file)
    assert (temp_file.exists())
    temp_file.unlink()


def test_j_dumps_list_input(sample_json_data2):
    """Tests j_dumps with valid list input."""
    temp_file = Path("./temp_output.json")
    j_dumps(sample_json_data2, file_path=temp_file)
    assert (temp_file.exists())
    temp_file.unlink()


def test_j_dumps_simple_namespace_input(sample_json_data):
    """Tests j_dumps with valid SimpleNamespace input."""
    ns_data = SimpleNamespace(**sample_json_data)
    temp_file = Path("./temp_output.json")
    j_dumps(ns_data, file_path=temp_file)
    assert (temp_file.exists())
    temp_file.unlink()


def test_j_dumps_invalid_mode():
    """Tests j_dumps with invalid mode."""
    with pytest.raises(ValueError):
        j_dumps({"key": "value"}, mode="r")


def test_j_loads_valid_file_path():
    """Tests j_loads with a valid file path."""
    data = j_loads(TEST_DIR / "test1.json")
    assert data == SAMPLE_JSON_DATA


def test_j_loads_nonexistent_file():
    """Tests j_loads with a non-existent file path."""
    with pytest.raises(FileNotFoundError):
        j_loads(Path("nonexistent_file.json"))

def test_replace_key_in_json_simple_dict():
    data = {"name": "John Doe"}
    updated_data = replace_key_in_json(data, "name", "category_name")
    assert updated_data == {"category_name": "John Doe"}

def test_replace_key_in_json_nested_dict():
    data = {"person": {"name": "Alice"}}
    updated_data = replace_key_in_json(data, "name", "category_name")
    assert updated_data == {"person": {"category_name": "Alice"}}

def test_process_json_file(sample_json_data):
    """Tests processing a JSON file"""
    temp_file = TEST_DIR / "test_process.json"
    temp_file.write_text(json.dumps(sample_json_data))
    process_json_file(temp_file)
    assert temp_file.exists()
    temp_file.unlink()

def test_recursive_process_json_files():
    """Tests processing a directory of json files"""
    recursive_process_json_files(TEST_DIR)

def test_extract_json_from_string(dummy_markdown):
    json_string = extract_json_from_string(dummy_markdown)
    assert json_string == '{"name": "John"}'


def test_j_loads_markdown_string():
    md_string = "```json\n{\"name\": \"John\", \"age\": 30}\n```"
    loaded_data = j_loads(md_string)
    assert loaded_data == {"name": "John", "age": 30}


# Cleanup the temporary directory after tests
def teardown_module(module):
    import shutil
    try:
        shutil.rmtree(TEST_DIR)
    except FileNotFoundError:
        pass
```