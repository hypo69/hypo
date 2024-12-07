```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

def test_get_relative_path_valid_input():
    """Checks correct behavior with a valid input."""
    full_path = "/home/user/project/src/utils/path.py"
    relative_from = "src"
    expected_result = "utils/path.py"
    result = get_relative_path(full_path, relative_from)
    assert result == expected_result


def test_get_relative_path_valid_input_with_multiple_matches():
    """Tests when relative_from appears multiple times"""
    full_path = "/home/user/project/src/utils/src/path.py"
    relative_from = "src"
    expected_result = "utils/src/path.py"
    result = get_relative_path(full_path, relative_from)
    assert result == expected_result


def test_get_relative_path_relative_from_at_the_beginning():
    """Tests when relative_from is at the beginning of the path."""
    full_path = "/home/user/project/src/file.txt"
    relative_from = "src"
    expected_result = "file.txt"
    result = get_relative_path(full_path, relative_from)
    assert result == expected_result


def test_get_relative_path_relative_from_at_the_end():
    """Tests when relative_from is at the end of the path."""
    full_path = "/home/user/project/src/utils/path.py"
    relative_from = "path.py"
    expected_result = "path.py"
    result = get_relative_path(full_path, relative_from)
    assert result == expected_result


def test_get_relative_path_relative_from_not_found():
    """Checks handling when the relative_from segment is not found."""
    full_path = "/home/user/project/src/utils/path.py"
    relative_from = "data"
    result = get_relative_path(full_path, relative_from)
    assert result is None


def test_get_relative_path_invalid_input_full_path():
    """Checks handling of invalid full_path (not a valid path)."""
    with pytest.raises(TypeError):
        get_relative_path("invalid_path", "src")


def test_get_relative_path_invalid_input_relative_from():
    """Checks handling of invalid relative_from (not a string)."""
    full_path = "/home/user/project/src/utils/path.py"
    with pytest.raises(TypeError):
        get_relative_path(full_path, 123)  # Example invalid input


def test_get_relative_path_empty_string_input():
    """Tests with empty strings for full_path and relative_from."""
    full_path = ""
    relative_from = ""
    result = get_relative_path(full_path, relative_from)
    assert result is None


def test_get_relative_path_with_windows_path():
    """Test with a Windows path."""
    full_path = "C:\\Users\\user\\project\\src\\utils\\path.py"
    relative_from = "src"
    expected_result = "utils\\path.py"
    result = get_relative_path(full_path, relative_from)
    assert result == expected_result



```