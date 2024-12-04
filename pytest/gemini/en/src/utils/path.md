```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

def test_get_relative_path_valid_input():
    """Checks correct behavior with valid input."""
    full_path = "/Users/john/Documents/project/src/utils/path.py"
    relative_from = "src/utils"
    expected_output = "path.py"
    assert get_relative_path(full_path, relative_from) == expected_output

def test_get_relative_path_valid_input_different_sep():
    """Checks correct behavior with valid input and different separator."""
    full_path = "C:\\Users\\john\\Documents\\project\\src\\utils\\path.py"
    relative_from = "src\\utils"
    expected_output = "path.py"
    assert get_relative_path(full_path, relative_from) == expected_output


def test_get_relative_path_relative_from_at_end():
    """Checks behavior when relative_from is the last part of the path."""
    full_path = "/Users/john/Documents/project/src/utils"
    relative_from = "src/utils"
    expected_output = ""
    assert get_relative_path(full_path, relative_from) == expected_output


def test_get_relative_path_relative_from_not_found():
    """Checks the function's handling when relative_from is not found."""
    full_path = "/Users/john/Documents/project/src/utils/path.py"
    relative_from = "src/data"
    assert get_relative_path(full_path, relative_from) is None


def test_get_relative_path_empty_relative_from():
    """Tests the function with an empty string as relative_from."""
    full_path = "/Users/john/Documents/project/src/utils/path.py"
    relative_from = ""
    expected_output = "/Users/john/Documents/project/src/utils/path.py"
    assert get_relative_path(full_path, relative_from) == expected_output


def test_get_relative_path_invalid_full_path():
    """Checks the function's handling with an invalid full_path."""
    full_path = "invalid_path"  # Invalid path
    relative_from = "src/utils"
    with pytest.raises(TypeError):
        get_relative_path(full_path, relative_from)

def test_get_relative_path_invalid_relative_from():
  """Tests the function with an invalid relative_from."""
  full_path = "/Users/john/Documents/project/src/utils/path.py"
  relative_from = 123 #Invalid input type
  with pytest.raises(TypeError):
      get_relative_path(full_path, relative_from)


def test_get_relative_path_empty_full_path():
  """Tests handling empty full_path."""
  full_path = ""
  relative_from = "src/utils"
  assert get_relative_path(full_path, relative_from) is None

# test with different path separators - important for cross-platform compatibility
def test_get_relative_path_windows_paths():
  """Checks for handling different path separators (Windows)."""
  full_path = "C:\\Users\\john\\Documents\\project\\src\\utils\\path.py"
  relative_from = "src\\utils"
  assert get_relative_path(full_path, relative_from) == "path.py"

```