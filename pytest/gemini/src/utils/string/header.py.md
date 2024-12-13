```python
import pytest
import sys
from pathlib import Path
from unittest.mock import mock_open, patch
import json

# Assuming the code is in a file named header.py
from src.logger.header import set_project_root, __root__, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

# Fixture to simulate file system for testing set_project_root
@pytest.fixture
def mock_fs(tmp_path):
    """Creates a mock file system for testing."""
    def create_file(path, content=""):
       full_path = tmp_path / path
       full_path.parent.mkdir(parents=True, exist_ok=True)
       with open(full_path, 'w') as f:
           f.write(content)
       return full_path
    
    def create_dir(path):
        full_path = tmp_path / path
        full_path.mkdir(parents=True, exist_ok=True)
        return full_path
    
    return create_file, create_dir, tmp_path

def test_set_project_root_with_marker_file_in_current_dir(mock_fs):
    """Checks if root is correctly identified in the current directory."""
    create_file, _, tmp_path = mock_fs
    create_file("pyproject.toml")
    
    root = set_project_root()
    
    assert root == tmp_path
    assert str(tmp_path) in sys.path

def test_set_project_root_with_marker_file_in_parent_dir(mock_fs):
    """Checks if root is correctly identified in a parent directory."""
    create_file, _, tmp_path = mock_fs
    create_file("parent/pyproject.toml")
    current_file_path = create_file("parent/subfolder/current_file.py")

    with patch("src.logger.header.__file__", str(current_file_path)):
        root = set_project_root()

    assert root == tmp_path / "parent"
    assert str(tmp_path / "parent") in sys.path

def test_set_project_root_no_marker_files(mock_fs):
    """Checks behavior if no marker files are found."""
    _, _, tmp_path = mock_fs
    current_file_path = tmp_path / "subfolder/current_file.py"
    current_file_path.parent.mkdir(parents=True, exist_ok=True)
    with patch("src.logger.header.__file__", str(current_file_path)):
      root = set_project_root()
    assert root == current_file_path.parent
    assert str(current_file_path.parent) in sys.path


def test_set_project_root_with_custom_marker_files(mock_fs):
    """Checks if root is correctly identified with custom marker files."""
    create_file, _, tmp_path = mock_fs
    create_file("custom_marker.txt")
    
    root = set_project_root(marker_files=('custom_marker.txt',))
    
    assert root == tmp_path
    assert str(tmp_path) in sys.path

def test_set_project_root_marker_is_dir(mock_fs):
    """Checks if root is correctly identified with marker folder."""
    _, create_dir, tmp_path = mock_fs
    create_dir(".git")
    
    root = set_project_root()
    
    assert root == tmp_path
    assert str(tmp_path) in sys.path

def test_global_variables_with_settings_json(mock_fs):
    """Checks if global variables are correctly loaded from settings.json."""
    create_file, _, tmp_path = mock_fs
    settings_data = {
        "project_name": "test_project",
        "version": "1.0.0",
        "author": "Test Author",
        "copyrihgnt": "Test Copyright",
        "cofee": "Custom coffee link",
    }
    create_file("src/settings.json", json.dumps(settings_data))
    create_file("src/README.MD", "Test document")
    
    # Use __root__ as if it was already assigned
    with patch("src.logger.header.__root__", tmp_path):
      from src.logger.header import __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__
      assert __project_name__ == "test_project"
      assert __version__ == "1.0.0"
      assert __doc__ == "Test document"
      assert __author__ == "Test Author"
      assert __copyright__ == "Test Copyright"
      assert __cofee__ == "Custom coffee link"

def test_global_variables_no_settings_json(mock_fs):
    """Checks default values of global variables when settings.json doesn't exist."""
    _, _, tmp_path = mock_fs
    # Use __root__ as if it was already assigned
    with patch("src.logger.header.__root__", tmp_path):
      from src.logger.header import __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__
      assert __project_name__ == "hypotez"
      assert __version__ == ''
      assert __doc__ == ''
      assert __author__ == ''
      assert __copyright__ == ''
      assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_global_variables_settings_json_empty(mock_fs):
    """Checks handling of an empty settings.json."""
    create_file, _, tmp_path = mock_fs
    create_file("src/settings.json", "{}")
    
    # Use __root__ as if it was already assigned
    with patch("src.logger.header.__root__", tmp_path):
        from src.logger.header import __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__
        assert __project_name__ == "hypotez"
        assert __version__ == ''
        assert __doc__ == ''
        assert __author__ == ''
        assert __copyright__ == ''
        assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


def test_global_variables_settings_json_invalid(mock_fs):
    """Checks handling of invalid json in settings.json."""
    create_file, _, tmp_path = mock_fs
    create_file("src/settings.json", "{invalid json}")
    
    # Use __root__ as if it was already assigned
    with patch("src.logger.header.__root__", tmp_path):
        from src.logger.header import __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__
        assert __project_name__ == "hypotez"
        assert __version__ == ''
        assert __doc__ == ''
        assert __author__ == ''
        assert __copyright__ == ''
        assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_global_variables_no_readme(mock_fs):
    """Checks default doc value of global variable when README.MD doesn't exist."""
    create_file, _, tmp_path = mock_fs
    settings_data = {
        "project_name": "test_project",
        "version": "1.0.0",
        "author": "Test Author",
        "copyrihgnt": "Test Copyright",
        "cofee": "Custom coffee link",
    }
    create_file("src/settings.json", json.dumps(settings_data))
    
    # Use __root__ as if it was already assigned
    with patch("src.logger.header.__root__", tmp_path):
        from src.logger.header import __doc__
        assert __doc__ == ''
```