```python
import pytest
from pathlib import Path
from hypotez.src.utils.path import get_relative_path


def test_get_relative_path_valid_input():
    """Tests get_relative_path with a valid input."""
    # Create example paths for testing
    file_path = Path(__file__).resolve()
    target_directory = Path("hypotez")
    
    # Create a hypotez directory if it doesn't exist to avoid errors
    target_directory.mkdir(parents=True, exist_ok=True)

    relative_path = get_relative_path(file_path, target_directory)
    
    # Assert that the relative path is correct
    assert relative_path == Path("..")


def test_get_relative_path_target_doesnt_exist():
    """Tests get_relative_path when the target directory does not exist."""
    # Create example paths for testing
    file_path = Path(__file__).resolve()
    target_directory = Path("nonexistent_directory")

    with pytest.raises(FileNotFoundError) as excinfo:
        get_relative_path(file_path, target_directory)
        
    # Assert that the correct exception is raised
    assert "Directory not found" in str(excinfo.value)



def test_get_relative_path_target_is_file():
    """Tests get_relative_path when the target is a file."""
    file_path = Path(__file__).resolve()
    target_file = Path("test_file.txt")
    target_file.touch()


    with pytest.raises(ValueError) as excinfo:
        get_relative_path(file_path, target_file)
    # Assert that the correct exception is raised
    assert "Target must be a directory" in str(excinfo.value)
    target_file.unlink()


def test_get_relative_path_file_path_is_invalid():
    """Tests get_relative_path when the file path is invalid."""
    # Use a string to mimic invalid path
    invalid_file_path = "not_a_valid_path"
    target_directory = Path("hypotez")

    with pytest.raises(TypeError) as excinfo:
        get_relative_path(invalid_file_path, target_directory)
    # Assert that the correct exception is raised
    assert "Path must be a pathlib.Path object" in str(excinfo.value)
    

def test_get_relative_path_target_is_same_as_file():
    """Tests get_relative_path when the target directory is the same as the file path"""
    file_path = Path(__file__).resolve()
    target_directory = file_path.parent


    relative_path = get_relative_path(file_path, target_directory)
    
    # Assert that the relative path is correct
    assert relative_path == Path(".")




# Important: Remove or comment out these lines, if the
# code doesn't define or use a 'header' module.
# import header  # This is not used in the provided code.
# from src.utils.path import get_relative_path #This line is commented out to avoid circular import


```