```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

def test_get_relative_path_valid_input():
    """Checks correct behavior with a valid input."""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "project"
    expected_output = "data/file.txt"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output

def test_get_relative_path_valid_input_different_sep():
    """Checks correct behavior with valid input and different separators."""
    full_path = "C:\\Users\\user\\project\\data\\file.txt"
    relative_from = "project"
    expected_output = "data\\file.txt"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output


def test_get_relative_path_relative_from_not_found():
    """Checks handling when relative_from is not found in the path."""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "subdir"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output is None

def test_get_relative_path_empty_string_input():
    """Checks handling with empty string as input."""
    full_path = ""
    relative_from = "project"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output is None
    
def test_get_relative_path_relative_from_at_the_beginning():
    """Checks handling when relative_from is the first part of the path."""
    full_path = "/home/user/project/file.txt"
    relative_from = "home"
    expected_output = "user/project/file.txt"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output

def test_get_relative_path_relative_from_is_last():
    """Checks when relative_from is the last segment."""
    full_path = "/home/user/project"
    relative_from = "project"
    expected_output = ""
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == ""


def test_get_relative_path_with_slashes_in_relative_from():
    """Checks handling when relative_from contains slashes"""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "project/data"
    expected_output = "file.txt"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output


def test_get_relative_path_invalid_full_path():
    """Checks handling of invalid full_path input (not a string)."""
    with pytest.raises(TypeError):
        get_relative_path(123, "project")


def test_get_relative_path_invalid_relative_from():
    """Checks handling of invalid relative_from input (not a string)."""
    with pytest.raises(TypeError):
        get_relative_path("/path/to/file", 123)
```