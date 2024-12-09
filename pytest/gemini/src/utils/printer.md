```python
import pytest
import json
from pathlib import Path
from hypotez.src.utils.printer import pprint, TEXT_COLORS, BG_COLORS, FONT_STYLES, _color_text


# Fixture for creating test data
@pytest.fixture
def test_data():
    return {
        "name": "Alice",
        "age": 30,
    }


@pytest.fixture
def test_list_data():
    return ["apple", "banana", "cherry"]


@pytest.fixture
def test_invalid_file():
    return Path("nonexistent_file.txt")


@pytest.fixture
def test_csv_file():
    """Creates a temporary CSV file for testing."""
    import tempfile
    import csv

    _, csv_file_path = tempfile.mkstemp(suffix=".csv")
    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Bob", "25"])
    return Path(csv_file_path)

# Tests for pprint function
def test_pprint_valid_dict(test_data):
    """Tests pprint with a valid dictionary."""
    expected_output = json.dumps(test_data, indent=4)
    formatted_output = pprint(test_data, text_color="green")
    actual_output = _color_text(expected_output, text_color='green')
    assert _color_text(expected_output, text_color='green') in str(formatted_output)
    assert "age" in str(formatted_output)



def test_pprint_valid_list(test_list_data):
    """Tests pprint with a valid list."""
    output_string = ""
    for item in test_list_data:
        output_string += _color_text(str(item), text_color="blue") + "\n"

    formatted_output = pprint(test_list_data, text_color="blue", font_style="bold")
    assert output_string.strip() in str(formatted_output)



def test_pprint_none_input():
    """Tests pprint with None input."""
    expected_output = _color_text("No data to print!", text_color=TEXT_COLORS["red"])
    formatted_output = pprint(None)
    assert expected_output in str(formatted_output)


def test_pprint_invalid_file(test_invalid_file):
    """Tests pprint with an invalid file."""
    expected_output = _color_text("Unsupported file type.", text_color="white")
    formatted_output = pprint(test_invalid_file)
    assert expected_output in str(formatted_output)


def test_pprint_valid_csv_file(test_csv_file):
    """Tests pprint with a valid CSV file."""
    expected_output = _color_text("File reading supported for .csv, .xls only.", text_color="white")
    formatted_output = pprint(test_csv_file)
    assert expected_output in str(formatted_output)



def test_pprint_invalid_data_type():
    """Tests pprint with invalid data type."""
    with pytest.raises(Exception):
        pprint(12345, bg_color="bg_red")

def test_pprint_valid_string():
    """Tests pprint with a valid string."""
    output_string = _color_text("this is a test string", text_color="green")
    formatted_output = pprint("this is a test string", text_color="green")
    assert output_string in str(formatted_output)


# Tests for _color_text (helper function)
def test__color_text_valid_input():
    result = _color_text("test", text_color="red")
    assert "\\033[31mtest\\033[0m" == result

def test__color_text_with_all_styles():
    result = _color_text("test", text_color="red", bg_color="bg_green", font_style="bold")
    assert "\\033[1m\\033[31m\\033[42mtest\\033[0m" == result



def test__color_text_missing_color():
    result = _color_text("test")
    assert "\\033[0mtest\\033[0m" == result


def test__color_text_invalid_color():
    result = _color_text("test", text_color="invalid_color")
    assert "\\033[37mtest\\033[0m" == result
```