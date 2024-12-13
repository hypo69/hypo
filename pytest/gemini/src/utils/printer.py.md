```python
import pytest
from hypotez.src.utils.printer import _color_text, pprint, TEXT_COLORS, BG_COLORS, FONT_STYLES
from pathlib import Path
import json

# Fixture for valid colors and styles
@pytest.fixture
def valid_styles():
    return {
        "text_color": "green",
        "bg_color": "bg_blue",
        "font_style": "bold",
    }

# Fixture for invalid colors and styles
@pytest.fixture
def invalid_styles():
    return {
        "text_color": "invalid_color",
        "bg_color": "invalid_bg",
        "font_style": "invalid_style",
    }
# Tests for _color_text function
def test_color_text_valid_styles(valid_styles):
    """
    Test _color_text with valid color, background, and font style.
    Verify if the function returns the text with the applied styles.
    """
    text = "Test text"
    styled_text = _color_text(
        text,
        text_color=TEXT_COLORS[valid_styles["text_color"]],
        bg_color=BG_COLORS[valid_styles["bg_color"]],
        font_style=FONT_STYLES[valid_styles["font_style"]],
    )
    assert (
        f'{FONT_STYLES[valid_styles["font_style"]]}'
        f'{TEXT_COLORS[valid_styles["text_color"]]}'
        f'{BG_COLORS[valid_styles["bg_color"]]}'
        f'{text}{"\\033[0m"}'
    ) == styled_text


def test_color_text_no_styles():
    """
    Test _color_text with no specified style.
    Verify if the function returns the text without any style applied.
    """
    text = "Test text"
    styled_text = _color_text(text)
    assert text + "\\033[0m" == styled_text


def test_color_text_with_empty_styles():
    """
    Test _color_text with empty strings as styles.
    Verify if the function returns the text without any style applied.
    """
    text = "Test text"
    styled_text = _color_text(text, text_color="", bg_color="", font_style="")
    assert text + "\\033[0m" == styled_text
    
def test_color_text_invalid_styles(invalid_styles):
    """
    Test _color_text with invalid color, background, and font style.
    Verify that function still works, but uses default values when applicable.
    """
    text = "Test text"
    styled_text = _color_text(
        text,
        text_color=invalid_styles["text_color"],
        bg_color=invalid_styles["bg_color"],
        font_style=invalid_styles["font_style"],
    )
    assert (
       f'{invalid_styles["font_style"]}{invalid_styles["text_color"]}{invalid_styles["bg_color"]}{text}{"\\033[0m"}' == styled_text
    )
    
# Tests for pprint function
def test_pprint_dict_valid_styles(valid_styles, capsys):
    """Test pprint with a dictionary and valid style parameters.
    Verifies that the output is correctly formatted and styled.
    """
    data = {"key1": "value1", "key2": 2}
    pprint(data, **valid_styles)
    captured = capsys.readouterr()
    expected_output = _color_text(json.dumps(data, indent=4), text_color=TEXT_COLORS[valid_styles["text_color"]])
    assert captured.out.strip() == expected_output.strip()

def test_pprint_list_valid_styles(valid_styles, capsys):
    """Test pprint with a list and valid style parameters.
    Verifies that the output is correctly formatted and styled.
    """
    data = ["item1", "item2"]
    pprint(data, **valid_styles)
    captured = capsys.readouterr()
    expected_output = ""
    for item in data:
        expected_output += f'{_color_text(str(item), text_color=TEXT_COLORS[valid_styles["text_color"]])}\n'
    assert captured.out.strip() == expected_output.strip()

def test_pprint_string_valid_styles(valid_styles, capsys):
    """Test pprint with a string and valid style parameters.
    Verifies that the output is correctly formatted and styled.
    """
    data = "test string"
    pprint(data, **valid_styles)
    captured = capsys.readouterr()
    expected_output = _color_text(data, text_color=TEXT_COLORS[valid_styles["text_color"]])
    assert captured.out.strip() == expected_output.strip()

def test_pprint_none_data(capsys):
    """Test pprint with None data.
    Verifies that the function prints a "No data to print!" message with red color.
    """
    pprint(None)
    captured = capsys.readouterr()
    expected_output = _color_text("No data to print!", text_color=TEXT_COLORS["red"])
    assert captured.out.strip() == expected_output.strip()


def test_pprint_path_unsupported_file(capsys, tmp_path):
    """Test pprint with Path object to unsupported file type.
    Verifies the "Unsupported file type" message is printed.
    """
    file_path = tmp_path / "test.txt"
    file_path.touch()
    pprint(file_path)
    captured = capsys.readouterr()
    expected_output = _color_text("Unsupported file type.", text_color=TEXT_COLORS["white"])
    assert captured.out.strip() == expected_output.strip()


def test_pprint_path_supported_file_reading_message(capsys, tmp_path):
    """Test pprint with Path object to supported file type.
    Verifies the supported file message is printed.
    """
    file_path = tmp_path / "test.csv"
    file_path.touch()
    pprint(file_path)
    captured = capsys.readouterr()
    expected_output = _color_text("File reading supported for .csv, .xls only.", text_color=TEXT_COLORS["white"])
    assert captured.out.strip() == expected_output.strip()


def test_pprint_exception(capsys):
    """
    Test pprint with an object that will cause an exception during printing.
    Verify that function prints a red message with the error
    """
    class BadObject:
        def __str__(self):
            raise Exception("Test exception")
    pprint(BadObject())
    captured = capsys.readouterr()
    expected_output = _color_text("Error: Test exception", text_color=TEXT_COLORS["red"])
    assert captured.out.strip() == expected_output.strip()


def test_pprint_invalid_text_color(invalid_styles, capsys):
    """Test pprint with invalid text color.
    Verifies if the default white color is used.
    """
    data = "Test"
    pprint(data, text_color=invalid_styles["text_color"])
    captured = capsys.readouterr()
    expected_output = _color_text(data, text_color=TEXT_COLORS["white"])
    assert captured.out.strip() == expected_output.strip()

def test_pprint_invalid_bg_color(invalid_styles, capsys):
    """Test pprint with invalid background color.
    Verifies if no background color is applied.
    """
    data = "Test"
    pprint(data, bg_color=invalid_styles["bg_color"])
    captured = capsys.readouterr()
    expected_output = _color_text(data, text_color=TEXT_COLORS["white"])
    assert captured.out.strip() == expected_output.strip()
    
def test_pprint_invalid_font_style(invalid_styles, capsys):
    """Test pprint with invalid font style.
    Verifies if no font style is applied.
    """
    data = "Test"
    pprint(data, font_style=invalid_styles["font_style"])
    captured = capsys.readouterr()
    expected_output = _color_text(data, text_color=TEXT_COLORS["white"])
    assert captured.out.strip() == expected_output.strip()
```