```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

# Test data
TEST_DATA = [
    ("C:\\Users\\user\\Documents\\project\\data\\file.txt", "project", "data\\file.txt"),
    ("C:\\Users\\user\\Documents\\project\\data\\file.txt", "not_found", None),
    ("C:/Users/user/Documents/project/data/file.txt", "project/data", "file.txt"),
    ("/home/user/project/data/file.txt", "project", "data/file.txt"),
    ("/home/user/project/data/file.txt", "/home/user/project", "data/file.txt"),
    ("/home/user/project/data/file.txt", "not_found", None),
]

# Tests for get_relative_path
@pytest.mark.parametrize("full_path, relative_from, expected", TEST_DATA)
def test_get_relative_path(full_path, relative_from, expected):
    """
    Test various inputs for get_relative_path, including valid and invalid relative paths.
    """
    result = get_relative_path(full_path, relative_from)
    if expected is not None:
        assert result == expected
    else:
        assert result is None


# Test with empty string as input
def test_get_relative_path_empty_string():
    """Tests the function with empty strings as input, which should not raise an exception."""
    result = get_relative_path("", "project")
    assert result is None


# Test with invalid path format (not a string)
def test_get_relative_path_invalid_path():
    """Test with an invalid path input (non-string)"""
    with pytest.raises(TypeError):
        get_relative_path(Path("file.txt"), "project")


# Test with invalid relative_from (non-string)
def test_get_relative_path_invalid_relative_from():
    """Test with an invalid relative_from input (non-string)."""
    with pytest.raises(TypeError):
        get_relative_path("C:\\Users\\file.txt", Path("project"))



# Test cases for different OS path separators
def test_get_relative_path_different_os_path_separators():
    """Tests if the function handles both Windows and Unix-like path separators correctly."""
    windows_path = "C:\\folder1\\folder2\\file.txt"
    unix_path = "/home/user/folder1/folder2/file.txt"
    
    assert get_relative_path(windows_path, "folder1") == "folder2\\file.txt"
    assert get_relative_path(unix_path, "folder1") == "folder2/file.txt"


#Edge case: relative_from is the last part of the path
def test_get_relative_path_relative_from_last_part():
    """Test case where relative_from is the last part of the path."""
    full_path = "/home/user/project/file.txt"
    relative_from = "file.txt"
    expected = "file.txt"
    result = get_relative_path(full_path, relative_from)
    assert result == expected



#Edge case: empty relative_from
def test_get_relative_path_empty_relative_from():
    """Test case where relative_from is an empty string."""
    full_path = "/home/user/project/file.txt"
    relative_from = ""
    expected = "/home/user/project/file.txt"
    result = get_relative_path(full_path, relative_from)
    assert result == expected
```