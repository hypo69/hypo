```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

def test_get_relative_path_valid_input():
    """Checks correct behavior with a valid input."""
    full_path = "/home/user/project/src/utils/path.py"
    relative_from = "project/src/utils"
    expected_relative_path = "path.py"
    actual_relative_path = get_relative_path(full_path, relative_from)
    assert actual_relative_path == expected_relative_path

    full_path = "C:/Users/John/Documents/project/data/file.txt"
    relative_from = "project/data"
    expected_relative_path = "file.txt"
    actual_relative_path = get_relative_path(full_path, relative_from)
    assert actual_relative_path == expected_relative_path


def test_get_relative_path_relative_from_at_root():
    """Tests relative_from at root path."""
    full_path = "/home/user/project/file.txt"
    relative_from = "/"
    expected_relative_path = "home/user/project/file.txt"
    actual_relative_path = get_relative_path(full_path, relative_from)
    assert actual_relative_path == expected_relative_path


def test_get_relative_path_relative_from_not_found():
    """Checks handling when relative_from is not in the path."""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "project/src/utils"
    actual_relative_path = get_relative_path(full_path, relative_from)
    assert actual_relative_path is None


def test_get_relative_path_empty_path():
  """Checks behavior with empty full_path."""
  full_path = ""
  relative_from = "project/src"
  actual_relative_path = get_relative_path(full_path, relative_from)
  assert actual_relative_path is None

def test_get_relative_path_relative_from_empty_string():
  """Checks behavior with empty relative_from."""
  full_path = "/home/user/project/file.txt"
  relative_from = ""
  actual_relative_path = get_relative_path(full_path, relative_from)
  assert actual_relative_path is None

def test_get_relative_path_invalid_input_type():
    """Tests with invalid input types."""
    with pytest.raises(TypeError):
        get_relative_path(123, "project/src")  # Integer as full_path
    with pytest.raises(TypeError):
        get_relative_path("/path/to/file", 123) # Integer as relative_from
    with pytest.raises(TypeError):
        get_relative_path(None, "project/src") # None as full_path

def test_get_relative_path_empty_relative_from_in_path():
    """Tests relative_from existing but being empty str."""
    full_path = "/home/user/project/src/utils"
    relative_from = ""
    actual_relative_path = get_relative_path(full_path, relative_from)
    assert actual_relative_path == ""



#Example using Windows paths
def test_get_relative_path_windows_path():
    """Tests with Windows path."""
    full_path = "C:/Users/John/Documents/project/data/file.txt"
    relative_from = "C:/Users/John/Documents/project"
    expected_relative_path = "data/file.txt"
    actual_relative_path = get_relative_path(full_path, relative_from)
    assert actual_relative_path == expected_relative_path
```