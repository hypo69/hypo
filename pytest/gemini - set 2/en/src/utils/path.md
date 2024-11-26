```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

# Fixtures (if needed, none in this case)


def test_get_relative_path_valid_input():
    """Tests get_relative_path with a valid input."""
    full_path = "/home/user/project/src/main.py"
    relative_from = "project"
    expected_output = "/src/main.py"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output


def test_get_relative_path_valid_input_different_separator():
    """Tests get_relative_path with a valid input and different separator."""
    full_path = "C:\\Users\\user\\project\\src\\main.py"
    relative_from = "project"
    expected_output = "\\src\\main.py"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output


def test_get_relative_path_relative_from_at_end():
    """Tests get_relative_path with relative_from at the end of the path."""
    full_path = "/home/user/project"
    relative_from = "project"
    expected_output = ""
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output


def test_get_relative_path_relative_from_not_found():
    """Tests get_relative_path with relative_from not found in the path."""
    full_path = "/home/user/project/src/main.py"
    relative_from = "data"
    expected_output = None
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output is None


def test_get_relative_path_relative_from_at_start():
    """Tests get_relative_path with relative_from at the start of the path."""
    full_path = "/home/user/project/src/main.py"
    relative_from = "/"
    expected_output = "/home/user/project/src/main.py"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output


def test_get_relative_path_empty_full_path():
  """Tests get_relative_path with an empty full path."""
  full_path = ""
  relative_from = "project"
  expected_output = None
  actual_output = get_relative_path(full_path, relative_from)
  assert actual_output is None


def test_get_relative_path_empty_relative_from():
  """Tests get_relative_path with an empty relative_from."""
  full_path = "/home/user/project/src/main.py"
  relative_from = ""
  expected_output = None
  actual_output = get_relative_path(full_path, relative_from)
  assert actual_output is None


def test_get_relative_path_relative_from_with_slashes_at_the_end():
    full_path = "/home/user/project/src/main.py"
    relative_from = "project/"
    expected_output = "/src/main.py"
    actual_output = get_relative_path(full_path, relative_from)
    assert actual_output == expected_output



def test_get_relative_path_with_invalid_full_path():
  """Test get_relative_path with invalid full path (non-string)."""
  with pytest.raises(TypeError):
      get_relative_path(123, "project")


def test_get_relative_path_with_invalid_relative_from():
  """Test get_relative_path with invalid relative_from (non-string)."""
  with pytest.raises(TypeError):
      get_relative_path("/home/user/project/src/main.py", 123)


```