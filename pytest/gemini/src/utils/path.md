```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

# Test data
TEST_DATA = [
    ("C:\\Users\\User\\Project\\data\\file.txt", "Project", "data\\file.txt"),
    ("C:\\Users\\User\\Project\\data\\file.txt", "data", "file.txt"),
    ("C:\\Users\\User\\Project\\data\\file.txt", "not_found", None),
    ("/", "home", "home"),
    ("/home/user/documents/file.txt", "/home", "/home/user/documents/file.txt"),
    ("C:/Users/User/Project/data/file.txt", "Project", "data\\file.txt"), # Test with different separator
    ("C:/Users/User/Project", "Project", ""),
    ("/tmp/myproject/src/main.py", "/tmp/myproject/src", "main.py")

]


def test_get_relative_path_valid_input():
    """Tests with valid input, checking successful extraction."""
    for full_path, relative_from, expected_relative_path in TEST_DATA:
        if expected_relative_path is not None:
            result = get_relative_path(full_path, relative_from)
            assert result == expected_relative_path, f"Input: {full_path}, {relative_from}. Expected: {expected_relative_path}, Got: {result}"

def test_get_relative_path_invalid_input():
    """Tests with non-existent relative_from segment."""
    for full_path, relative_from, expected_relative_path in TEST_DATA:
        if expected_relative_path is None:
            result = get_relative_path(full_path, relative_from)
            assert result is None, f"Input: {full_path}, {relative_from}. Expected: None, Got: {result}"



def test_get_relative_path_empty_string():
    """Tests with empty string as input."""
    result = get_relative_path("", "root")
    assert result is None, "Empty string input should return None."
    
def test_get_relative_path_none_input():
    """Tests with None input."""
    with pytest.raises(TypeError):
        get_relative_path(None, "root")

def test_get_relative_path_non_string_input():
    """Tests with non-string input."""
    with pytest.raises(TypeError):
        get_relative_path(Path("/path/to/file"), "path")
    with pytest.raises(TypeError):
        get_relative_path("/path/to/file", 123) #non-string relative_from

def test_get_relative_path_with_relative_from_at_the_start():
    """Tests with relative_from being the first segment of the path."""
    result = get_relative_path("/home/user", "/home")
    assert result == "/home/user"
    
def test_get_relative_path_with_relative_from_at_the_end():
    """Tests with relative_from at the end of the path (which will return empty string)."""
    result = get_relative_path("C:\\Users\\User\\Project", "Project")
    assert result == ""
```