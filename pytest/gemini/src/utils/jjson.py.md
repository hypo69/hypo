```python
import pytest
from pathlib import Path
from types import SimpleNamespace
import json
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from unittest.mock import patch
from src.logger.logger import logger
import pandas as pd
from collections import OrderedDict
import simplejson as simplejson


# Fixture for a test JSON file
@pytest.fixture
def test_json_file(tmp_path):
    file_path = tmp_path / "test.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"key": "value", "number": 123, "list": [1, 2, 3]}, f)
    return file_path


# Fixture for a test CSV file
@pytest.fixture
def test_csv_file(tmp_path):
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    df.to_csv(file_path, index=False)
    return file_path

# Fixture for a test directory with JSON files
@pytest.fixture
def test_json_directory(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / "test1.json").write_text(json.dumps({"key1": "value1"}), encoding="utf-8")
    (dir_path / "test2.json").write_text(json.dumps({"key2": "value2"}), encoding="utf-8")
    return dir_path

# Fixture for SimpleNamespace data
@pytest.fixture
def simple_namespace_data():
    return SimpleNamespace(key="value", number=123)


# Fixture for SimpleNamespace data with nested SimpleNamespace
@pytest.fixture
def nested_simple_namespace_data():
    return SimpleNamespace(
        key="value",
        nested=SimpleNamespace(sub_key="sub_value", sub_list=[1, 2])
    )


# Fixture for mixed data (dict and SimpleNamespace in list)
@pytest.fixture
def mixed_data():
    return [
        {"key1": "value1", "list": [1, 2]},
        SimpleNamespace(key2="value2", number=123)
    ]


# Tests for j_dumps function
def test_j_dumps_valid_dict(tmp_path):
    """Test dumping a dictionary to a file."""
    file_path = tmp_path / "test.json"
    data = {"key": "value"}
    j_dumps(data, file_path)
    with open(file_path, "r") as f:
        assert json.load(f) == data


def test_j_dumps_valid_simplenamespace(tmp_path, simple_namespace_data):
    """Test dumping a SimpleNamespace object to a file."""
    file_path = tmp_path / "test.json"
    j_dumps(simple_namespace_data, file_path)
    with open(file_path, "r") as f:
        assert json.load(f) == vars(simple_namespace_data)


def test_j_dumps_valid_list_of_dicts(tmp_path):
    """Test dumping a list of dictionaries to a file."""
    file_path = tmp_path / "test.json"
    data = [{"key1": "value1"}, {"key2": "value2"}]
    j_dumps(data, file_path)
    with open(file_path, "r") as f:
        assert json.load(f) == data


def test_j_dumps_valid_list_of_simplenamespaces(tmp_path, simple_namespace_data):
    """Test dumping a list of SimpleNamespace objects to a file."""
    file_path = tmp_path / "test.json"
    data = [simple_namespace_data, simple_namespace_data]
    j_dumps(data, file_path)
    with open(file_path, "r") as f:
        assert json.load(f) == [vars(item) for item in data]


def test_j_dumps_no_file_path():
    """Test dumping to a dictionary when no file path is provided."""
    data = {"key": "value"}
    result = j_dumps(data)
    assert result == data


def test_j_dumps_invalid_mode(tmp_path):
    """Test dumping to a file with an invalid file mode."""
    file_path = tmp_path / "test.json"
    data = {"key": "value"}
    j_dumps(data, file_path, mode="x")
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) == data


def test_j_dumps_append_mode_a_plus(tmp_path):
    """Test dumping to a file in append mode ('a+') with an existing JSON list."""
    file_path = tmp_path / "test.json"
    data = [{"new_key": "new_value"}]
    initial_data = [{"key1": "value1"}, {"key2": "value2"}]
    j_dumps(initial_data, file_path)
    j_dumps(data, file_path, mode="a+")
    with open(file_path, "r", encoding="utf-8") as f:
         assert json.load(f) == data+initial_data


def test_j_dumps_append_mode_plus_a(tmp_path):
    """Test dumping to a file in append mode ('+a') with an existing JSON list."""
    file_path = tmp_path / "test.json"
    data = [{"new_key": "new_value"}]
    initial_data = [{"key1": "value1"}, {"key2": "value2"}]
    j_dumps(initial_data, file_path)
    j_dumps(data, file_path, mode="+a")
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) == initial_data+data


def test_j_dumps_append_mode_plus_a_dict_to_dict(tmp_path):
    """Test dumping to a file in append mode ('+a') with an existing JSON dict and a new dict."""
    file_path = tmp_path / "test.json"
    data = {"new_key": "new_value"}
    initial_data = {"key1": "value1", "key2": "value2"}
    j_dumps(initial_data, file_path)
    j_dumps(data, file_path, mode="+a")
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) == {**initial_data,**data}


def test_j_dumps_non_ascii_characters(tmp_path):
    """Test dumping a dict with non-ASCII characters with and without ensuring ASCII."""
    file_path = tmp_path / "test.json"
    data = {"key": "значение"}
    j_dumps(data, file_path, ensure_ascii=False)
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) == data
    
    j_dumps(data, file_path, ensure_ascii=True)
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) == {"key": "\\u0437\\u043d\\u0430\\u0447\\u0435\\u043d\\u0438\\u0435"}


def test_j_dumps_with_nested_simple_namespace(tmp_path, nested_simple_namespace_data):
    """Test dumping a SimpleNamespace object with nested SimpleNamespace."""
    file_path = tmp_path / "test.json"
    j_dumps(nested_simple_namespace_data, file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) == {
            'key': 'value',
            'nested': {'sub_key': 'sub_value', 'sub_list': [1, 2]}
        }

def test_j_dumps_with_mixed_data(tmp_path, mixed_data):
    """Test dumping mixed data list with dicts and SimpleNamespaces."""
    file_path = tmp_path / "test.json"
    j_dumps(mixed_data, file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        assert json.load(f) ==  [
            {'key1': 'value1', 'list': [1, 2]},
            {'key2': 'value2', 'number': 123}
        ]

def test_j_dumps_string_input(tmp_path):
    """Test dumping a valid json string as a dictionary."""
    file_path = tmp_path / "test.json"
    data = '{"key": "value"}'
    j_dumps(data, file_path)
    with open(file_path, "r") as f:
        assert json.load(f) == {"key": "value"}


def test_j_dumps_invalid_string_input(tmp_path):
    """Test handling of invalid json string input."""
    file_path = tmp_path / "test.json"
    data = '{"key": "value" invalid }'
    assert j_dumps(data, file_path) is None

    
def test_j_dumps_error_log(tmp_path, caplog):
     """Test that errors are logged using the logger."""
     file_path = tmp_path / "test.json"
     data = {"key": "value"}
     with patch("src.utils.jjson.logger.error") as mock_log:
         j_dumps(data, file_path, mode="x")
         mock_log.assert_called()

     with patch("src.utils.jjson.logger.error") as mock_log:
         j_dumps('{"key": "value" invalid }', file_path)
         mock_log.assert_called()

     with patch("src.utils.jjson.logger.error") as mock_log:
         j_dumps(data, Path('invalid_file_path'))
         mock_log.assert_called()

# Tests for j_loads function
def test_j_loads_valid_json_file(test_json_file):
    """Test loading from a valid JSON file."""
    data = j_loads(test_json_file)
    assert data == {"key": "value", "number": 123, "list": [1, 2, 3]}


def test_j_loads_valid_csv_file(test_csv_file):
    """Test loading from a valid CSV file."""
    data = j_loads(test_csv_file)
    assert data == [{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}]


def test_j_loads_from_string():
    """Test loading from a JSON string."""
    json_string = '{"key": "value"}'
    data = j_loads(json_string)
    assert data == {"key": "value"}


def test_j_loads_from_simple_namespace(simple_namespace_data):
    """Test loading from a SimpleNamespace object."""
    data = j_loads(simple_namespace_data)
    assert data == {"key": "value", "number": 123}


def test_j_loads_from_list():
    """Test loading from a list."""
    data = [{"key1": "value1"}, {"key2": "value2"}]
    loaded_data = j_loads(data)
    assert loaded_data == data


def test_j_loads_non_existing_file():
    """Test loading from a non-existing file."""
    file_path = Path("non_existent.json")
    assert j_loads(file_path) == {}


def test_j_loads_invalid_json_string(caplog):
    """Test loading an invalid JSON string."""
    json_string = "{invalid: json}"
    result = j_loads(json_string)
    assert result == {}


def test_j_loads_empty_string():
    """Test loading an empty string."""
    assert j_loads("") == {}

def test_j_loads_json_directory(test_json_directory):
    """Test loading from a directory containing JSON files."""
    loaded_data = j_loads(test_json_directory)
    assert isinstance(loaded_data, list)
    assert len(loaded_data) == 2
    assert {"key1": "value1"} in loaded_data
    assert {"key2": "value2"} in loaded_data


def test_j_loads_markdown_string():
    """Test loading json string from markdown format."""
    md_string = '```json\n{"key": "value"}\n```'
    data = j_loads(md_string)
    assert data == {"key": "value"}


def test_j_loads_non_json_data_in_list():
    """Test loading non-json data in list."""
    data = [1, "string", True]
    loaded_data = j_loads(data)
    assert loaded_data == data


def test_j_loads_non_json_data_dict():
    """Test loading non-json data in dict."""
    data = {1:'string', True:123}
    loaded_data = j_loads(data)
    assert loaded_data == {1:'string', True:123}
    

def test_j_loads_with_unicode_escape_chars():
    """Test loading a string with unicode escape sequences."""
    escaped_string =  '\\u0412\\u044b\\u0441\\u043e\\u043a\\u043e'
    assert j_loads(escaped_string) == 'Высоко'

def test_j_loads_with_unicode_escape_chars_in_dict():
    """Test loading dictionary with unicode escape sequences in values and keys."""
    escaped_dict =  {'\\u0412\\u044b\\u0441\\u043e\\u043a\\u043e': '\\u0412\\u044b\\u0441\\u043e\\u043a\\u043e'}
    assert j_loads(escaped_dict) == {'Высоко':'Высоко'}


def test_j_loads_with_unicode_escape_chars_in_list():
    """Test loading list with unicode escape sequences."""
    escaped_list =  ['\\u0412\\u044b\\u0441\\u043e\\u043a\\u043e','\\u0412\\u044b\\u0441\\u043e\\u043a\\u043e']
    assert j_loads(escaped_list) == ['Высоко','Высоко']


def test_j_loads_ordered_false(test_json_file):
    """Test loading from a valid JSON file and without ordered dictionary."""
    data = j_loads(test_json_file,ordered=False)
    assert data == {"key": "value", "number": 123, "list": [1, 2, 3]}


def test_j_loads_error_log(caplog):
     """Test that errors are logged using the logger."""
     with patch("src.utils.jjson.logger.error") as mock_log:
         j_loads('{"key": "value" invalid }')
         mock_log.assert_called()
     with patch("src.utils.jjson.logger.error") as mock_log:
         j_loads(Path('invalid_file_path'))
         mock_log.assert_called()


# Tests for j_loads_ns function
def test_j_loads_ns_valid_json_file(test_json_file):
    """Test loading a JSON file to SimpleNamespace."""
    ns = j_loads_ns(test_json_file)
    assert isinstance(ns, SimpleNamespace)
    assert ns.key == "value"
    assert ns.number == 123
    assert ns.list == [1, 2, 3]


def test_j_loads_ns_valid_csv_file(test_csv_file):
    """Test loading a CSV file to SimpleNamespace list."""
    ns_list = j_loads_ns(test_csv_file)
    assert isinstance(ns_list, list)
    assert len(ns_list) == 2
    assert isinstance(ns_list[0], SimpleNamespace)
    assert ns_list[0].col1 == 1
    assert ns_list[0].col2 == "a"


def test_j_loads_ns_from_string():
    """Test loading a JSON string to SimpleNamespace."""
    json_string = '{"key": "value"}'
    ns = j_loads_ns(json_string)
    assert isinstance(ns, SimpleNamespace)
    assert ns.key == "value"


def test_j_loads_ns_from_simple_namespace(simple_namespace_data):
    """Test loading a SimpleNamespace to SimpleNamespace."""
    ns = j_loads_ns(simple_namespace_data)
    assert isinstance(ns, SimpleNamespace)
    assert ns.key == "value"
    assert ns.number == 123

def test_j_loads_ns_from_list(simple_namespace_data):
    """Test loading a list of dicts and namespaces to list of SimpleNamespace."""
    data = [
         {"key1": "value1", "list": [1, 2]},
        simple_namespace_data
    ]
    ns = j_loads_ns(data)
    assert isinstance(ns, list)
    assert isinstance(ns[0], SimpleNamespace)
    assert isinstance(ns[1], SimpleNamespace)

def test_j_loads_ns_non_existing_file():
    """Test loading from a non-existent file to SimpleNamespace."""
    file_path = Path("non_existent.json")
    assert j_loads_ns(file_path) == {}


def test_j_loads_ns_invalid_json_string(caplog):
    """Test loading an invalid JSON string to SimpleNamespace."""
    json_string = "{invalid: json}"
    assert j_loads_ns(json_string) == {}

def test_j_loads_ns_empty_string():
    """Test loading an empty string to SimpleNamespace."""
    assert j_loads_ns("") == {}


def test_j_loads_ns_json_directory(test_json_directory):
    """Test loading from a directory containing JSON files to list of SimpleNamespace."""
    loaded_data = j_loads_ns(test_json_directory)
    assert isinstance(loaded_data, list)
    assert len(loaded_data) == 2
    assert isinstance(loaded_data[0], SimpleNamespace)
    assert isinstance(loaded_data[1], SimpleNamespace)


def test_j_loads_ns_error_log(caplog):
     """Test that errors are logged using the logger."""
     with patch("src.utils.jjson.logger.error") as mock_log:
         j_loads_ns('{"key": "value" invalid }')
         mock_log.assert_called()
     with patch("src.utils.jjson.logger.error") as mock_log:
         j_loads_ns(Path('invalid_file_path'))
         mock_log.assert_called()

```