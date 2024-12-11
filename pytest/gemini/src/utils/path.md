```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path

def test_get_relative_path_valid_input():
    """Tests get_relative_path with valid input."""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "project"
    expected_result = "data/file.txt"
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result

def test_get_relative_path_valid_input_different_sep():
    """Tests get_relative_path with valid input and different separator."""
    full_path = "C:\\Users\\user\\project\\data\\file.txt"
    relative_from = "project"
    expected_result = "data\\file.txt"
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result


def test_get_relative_path_relative_from_not_found():
    """Tests get_relative_path when relative_from is not in the path."""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "wrong_segment"
    expected_result = None
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result

def test_get_relative_path_relative_from_is_first():
    """Tests get_relative_path when relative_from is the first part of the path."""
    full_path = "/home/user/project/data/file.txt"
    relative_from = "home"
    expected_result = "user/project/data/file.txt"
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result
  
def test_get_relative_path_empty_string_input():
    """Tests get_relative_path with empty string inputs."""
    full_path = ""
    relative_from = "project"
    expected_result = None
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result
    
    full_path = "/home/user/project/data/file.txt"
    relative_from = ""
    expected_result = None
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result


def test_get_relative_path_with_invalid_full_path():
    """Tests the function with an invalid full_path (not a valid path)."""
    with pytest.raises(ValueError):
        get_relative_path("invalid/path", "relative_from")

def test_get_relative_path_with_invalid_relative_from():
    """Tests the function with an invalid relative_from."""
    full_path = "/home/user/project/data/file.txt"
    with pytest.raises(TypeError):
        get_relative_path(full_path, 123)


# Example using a fixture (although not strictly necessary for these tests)
# (This fixture is here for illuStartion, as it isn't required for this specific function's testing.)
@pytest.fixture
def sample_paths():
    """Provides sample paths for testing."""
    return [
        ("/home/user/project/data/file.txt", "project", "data/file.txt"),
        ("/home/user/project/data2/file2.txt", "project", "data2/file2.txt"),
        ("/home/user/data/file.txt", "project", None),
        ("C:\\Users\\user\\project\\data\\file.txt", "project", "data\\file.txt"),
        ("","relative", None),
    ]


def test_get_relative_path_with_sample_paths(sample_paths):
  """Tests get_relative_path with multiple sample paths."""
  for full_path, relative_from, expected_result in sample_paths:
    actual_result = get_relative_path(full_path, relative_from)
    assert actual_result == expected_result


```