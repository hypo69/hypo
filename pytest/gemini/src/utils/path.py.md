```python
import pytest
from hypotez.src.utils.path import get_relative_path


def test_get_relative_path_valid_input():
    """Checks correct behavior with valid input."""
    full_path = "/home/user/project/src/module/file.py"
    relative_from = "src"
    expected_path = "src/module/file.py"
    assert get_relative_path(full_path, relative_from) == expected_path

def test_get_relative_path_relative_from_not_found():
    """Checks behavior when relative_from segment is not in the path."""
    full_path = "/home/user/project/src/module/file.py"
    relative_from = "docs"
    assert get_relative_path(full_path, relative_from) is None


def test_get_relative_path_relative_from_at_the_begining():
    """Checks behavior when relative_from segment is the first segment."""
    full_path = "src/module/file.py"
    relative_from = "src"
    expected_path = "src/module/file.py"
    assert get_relative_path(full_path, relative_from) == expected_path

def test_get_relative_path_relative_from_at_the_end():
    """Checks behavior when relative_from segment is the last segment."""
    full_path = "/home/user/project/src"
    relative_from = "src"
    expected_path = "src"
    assert get_relative_path(full_path, relative_from) == expected_path

def test_get_relative_path_empty_path():
    """Checks behavior with an empty full path string"""
    full_path = ""
    relative_from = "src"
    assert get_relative_path(full_path, relative_from) is None


def test_get_relative_path_empty_relative_from():
     """Checks behavior with an empty relative_from string"""
     full_path = "/home/user/project/src/module/file.py"
     relative_from = ""
     assert get_relative_path(full_path, relative_from) is None

def test_get_relative_path_windows_path():
     """Checks correct behavior with Windows style path."""
     full_path = "C:\\Users\\user\\project\\src\\module\\file.py"
     relative_from = "src"
     expected_path = "src/module/file.py"
     assert get_relative_path(full_path, relative_from) == expected_path

def test_get_relative_path_relative_from_is_present_multiple_times():
    """Checks behavior when relative_from is present multiple times in path."""
    full_path = "/home/user/project/src/src/module/file.py"
    relative_from = "src"
    expected_path = "src/src/module/file.py"
    assert get_relative_path(full_path, relative_from) == expected_path
```