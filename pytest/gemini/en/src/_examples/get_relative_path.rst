```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path


def test_get_relative_path_valid_input():
    """Checks correct behavior with valid input for a file path."""
    file_path = Path(__file__).resolve()
    relative_path = get_relative_path(file_path, "hypotez")
    assert str(relative_path) == "src/_examples/get_relative_path.py"

@pytest.mark.parametrize(
    "input_file_path, expected_relative_path",
    [
        (Path("./hypotez/src/_examples/get_relative_path.py"), "src/_examples/get_relative_path.py"),
        (Path("/home/user/hypotez/src/_examples/get_relative_path.py"), "src/_examples/get_relative_path.py"),
        (Path("C:/path/to/hypotez/src/_examples/get_relative_path.py"), "src/_examples/get_relative_path.py"),
    ]
)
def test_get_relative_path_valid_inputs_various_paths(input_file_path, expected_relative_path):
    """
    Checks correct behavior with various valid input paths.
    Uses parametrization to test multiple cases efficiently.
    """
    relative_path = get_relative_path(input_file_path, "hypotez")
    assert str(relative_path) == expected_relative_path


def test_get_relative_path_invalid_base_directory():
    """Checks the handling of an invalid base directory."""
    file_path = Path(__file__).resolve()
    with pytest.raises(ValueError) as excinfo:
        get_relative_path(file_path, "invalid_base_dir")
    assert "Base directory 'invalid_base_dir' not found in file path" in str(excinfo.value)


def test_get_relative_path_file_not_found():
    """
    Tests the case where the file path provided is invalid, 
    simulating a file that does not exist. 
    """
    file_path = Path("nonexistent_file.py")
    with pytest.raises(FileNotFoundError) as excinfo:
        get_relative_path(file_path, "hypotez")
    assert "The file 'nonexistent_file.py' does not exist" in str(excinfo.value)


def test_get_relative_path_non_string_base():
    """Tests with a non-string base directory."""
    file_path = Path(__file__).resolve()
    with pytest.raises(TypeError) as excinfo:
        get_relative_path(file_path, 123)  # Trying to pass an integer
    assert "Base directory must be a string" in str(excinfo.value)


def test_get_relative_path_missing_base_directory():
    """Checks if an exception is raised if the base directory is not found."""
    file_path = Path(__file__).resolve()
    with pytest.raises(ValueError) as excinfo:
        get_relative_path(file_path, "missing_dir")
    assert "Base directory 'missing_dir' not found in file path" in str(excinfo.value)


def test_get_relative_path_empty_base():
    """Checks if the function handles an empty base directory."""
    file_path = Path(__file__).resolve()
    with pytest.raises(ValueError) as excinfo:
        get_relative_path(file_path, "")
    assert "Base directory cannot be empty" in str(excinfo.value)



```