```python
import pytest
import json
from pathlib import Path
from hypotez.src.utils.printer import pprint, _color_text, TEXT_COLORS, BG_COLORS, FONT_STYLES


# Fixture definitions
@pytest.fixture
def valid_dict_data():
    return {"name": "Alice", "age": 30}


@pytest.fixture
def valid_list_data():
    return ["apple", "banana", "cherry"]


@pytest.fixture
def invalid_file_path():
    return "invalid_file.txt"


@pytest.fixture
def valid_csv_file_path(tmpdir):
    """Creates a temporary CSV file for testing."""
    csv_file_path = tmpdir.join("data.csv")
    csv_file_path.write("name,age\nAlice,30\nBob,25")
    return str(csv_file_path)

@pytest.fixture
def valid_json_file_path(tmpdir):
    """Creates a temporary JSON file for testing."""
    json_file_path = tmpdir.join("data.json")
    json_file_path.write('{"name": "Alice", "age": 30}')
    return str(json_file_path)


# Tests for _color_text
def test__color_text_valid_input(capsys):
    """Tests _color_text with valid input."""
    result = _color_text("Hello", text_color="green", font_style="bold")
    assert result == f"{FONT_STYLES.get('bold','')}{TEXT_COLORS.get('green','')}" + "Hello" + "\033[0m"
    captured = capsys.readouterr()
    assert captured.out == ""

def test__color_text_no_styling(capsys):
    result = _color_text("Hello")
    assert result == "Hello\033[0m"


# Tests for pprint
def test_pprint_valid_dict(capsys, valid_dict_data):
    """Tests pprint with a valid dictionary."""
    pprint(valid_dict_data, text_color="green")
    captured = capsys.readouterr()
    assert f"{TEXT_COLORS['green']}{json.dumps(valid_dict_data, indent=4)}\033[0m" in captured.out

def test_pprint_valid_list(capsys, valid_list_data):
    """Tests pprint with a valid list."""
    pprint(valid_list_data, text_color="blue")
    captured = capsys.readouterr()
    output = ""
    for item in valid_list_data:
        output += f"{TEXT_COLORS['blue']}{item}\033[0m\n"
    assert output[:-1] in captured.out


def test_pprint_none(capsys):
    """Tests pprint with None."""
    pprint(None)
    captured = capsys.readouterr()
    expected_output = f"{TEXT_COLORS['red']}No data to print!\033[0m\n"
    assert expected_output == captured.out


def test_pprint_invalid_file(capsys, invalid_file_path):
    """Tests pprint with an invalid file path."""
    pprint(invalid_file_path)
    captured = capsys.readouterr()
    expected_output = f"{TEXT_COLORS['white']}Unsupported file type.\033[0m\n"
    assert expected_output == captured.out


def test_pprint_valid_csv_file(capsys, valid_csv_file_path):
    """Tests pprint with a valid CSV file."""
    pprint(valid_csv_file_path, text_color="blue")
    captured = capsys.readouterr()
    assert "File reading supported for .csv, .xls only." in captured.out

def test_pprint_valid_json_file(capsys, valid_json_file_path):
    """Tests pprint with a valid JSON file."""
    pprint(valid_json_file_path, text_color="blue")
    captured = capsys.readouterr()
    assert '{"name": "Alice", "age": 30}' in captured.out



def test_pprint_unsupported_type(capsys):
    """Tests pprint with an unsupported type."""
    pprint(123)
    captured = capsys.readouterr()
    assert f"{TEXT_COLORS['white']}123\033[0m" in captured.out

# Test for error handling
def test_pprint_error(capsys):
    """Tests pprint with an error during printing."""
    with pytest.raises(Exception):
        pprint("invalid data")
    captured = capsys.readouterr()
    assert "Error:" in captured.out


```