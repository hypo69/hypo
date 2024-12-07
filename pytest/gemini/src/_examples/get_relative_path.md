```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path


def test_get_relative_path_valid_input():
    """Checks correct behavior with valid input (same directory)."""
    current_file = Path(__file__).resolve()
    relative_path = get_relative_path(current_file, str(current_file.parent))
    assert relative_path == '.'


def test_get_relative_path_valid_input_subdirectory():
    """Checks correct behavior with valid input (subdirectory)."""
    current_file = Path(__file__).resolve()
    relative_path = get_relative_path(current_file, str(current_file.parent / "hypotez"))
    #This path will be something like ".." or "./hypotez" etc.
    assert relative_path.startswith("hypotez") or relative_path.startswith("..")


def test_get_relative_path_valid_input_different_levels():
    """Checks correct behavior with valid input (different directory levels)."""
    current_file = Path(__file__).resolve()
    root_dir = current_file.parents[1]  # One level up from current file
    relative_path = get_relative_path(current_file, str(root_dir))
    assert relative_path.startswith("..")


def test_get_relative_path_invalid_input_non_existing_directory():
    """Checks handling of non-existing directory."""
    current_file = Path(__file__).resolve()
    nonexistent_dir = "nonexistent_directory"
    with pytest.raises(ValueError) as excinfo:
        get_relative_path(current_file, nonexistent_dir)
    #Check the error message.  Crucial for robust error handling.
    assert "Directory 'nonexistent_directory' does not exist." in str(excinfo.value)


def test_get_relative_path_invalid_input_invalid_path():
    """Checks handling of invalid path input."""
    current_file = Path(__file__).resolve()
    invalid_path = "invalid//path"
    with pytest.raises(ValueError) as excinfo:
        get_relative_path(current_file, invalid_path)
    assert "Invalid path: invalid//path" in str(excinfo.value)

#Important:  This test verifies the function's behavior with a None input.
def test_get_relative_path_invalid_input_none_current_path():
    with pytest.raises(TypeError):
        get_relative_path(None, "hypotez")


def test_get_relative_path_invalid_input_none_target_path():
    current_file = Path(__file__).resolve()
    with pytest.raises(TypeError):
        get_relative_path(current_file, None)


def test_get_relative_path_invalid_input_current_file_not_path():
    with pytest.raises(TypeError):
        get_relative_path("not a path", "hypotez")



```