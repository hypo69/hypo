```python
import pytest
from pathlib import Path
from unittest.mock import patch
from src.utils.path import get_relative_path  # Assuming get_relative_path is in path.py


def test_get_relative_path_valid_input():
    """Checks correct relative path is returned with valid input."""
    # Mocking the Path object to create an artificial scenario
    with patch('src.utils.path.Path.resolve') as mock_resolve:
        mock_resolve.return_value = Path("/user/project/src/file.py")
        
        relative_path = get_relative_path(Path("mock_path"), 'project')
        assert relative_path == Path("src/file.py"), f"Expected 'src/file.py', got '{relative_path}'"


def test_get_relative_path_target_not_in_path():
    """Checks when the target folder does not appear in the path.
    Expected behavior: The function returns an empty Path.
    """
    with patch('src.utils.path.Path.resolve') as mock_resolve:
        mock_resolve.return_value = Path("/user/test/file.py")
        
        relative_path = get_relative_path(Path("mock_path"), 'project')
        assert relative_path == Path(""), f"Expected an empty Path, got '{relative_path}'"

def test_get_relative_path_target_is_root():
    """Checks when target is the root of the provided path."""
    with patch('src.utils.path.Path.resolve') as mock_resolve:
        mock_resolve.return_value = Path("/user/project/file.py")
        
        relative_path = get_relative_path(Path("mock_path"), 'user')
        assert relative_path == Path("project/file.py"), f"Expected 'project/file.py', got '{relative_path}'"

def test_get_relative_path_empty_target():
        """Checks when target is an empty string.
        Expected behavior: The function returns an empty Path.
        """
        with patch('src.utils.path.Path.resolve') as mock_resolve:
            mock_resolve.return_value = Path("/user/project/src/file.py")
            
            relative_path = get_relative_path(Path("mock_path"), "")
            assert relative_path == Path(""), f"Expected an empty Path, got '{relative_path}'"

def test_get_relative_path_empty_path():
    """Checks when an empty Path object is provided as input.
        Expected behavior: The function returns an empty Path.
    """
    with patch('src.utils.path.Path.resolve') as mock_resolve:
         mock_resolve.return_value = Path("")
        
         relative_path = get_relative_path(Path(""), "target")
         assert relative_path == Path(""), f"Expected an empty Path, got '{relative_path}'"
```