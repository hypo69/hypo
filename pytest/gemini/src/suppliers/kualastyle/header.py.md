```python
import pytest
import sys
from pathlib import Path
import json
from unittest.mock import mock_open, patch
from packaging.version import Version
from hypotez.src.suppliers.kualastyle.header import set_project_root, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__
from hypotez.src import gs

# Fixture to create dummy files for testing
@pytest.fixture
def dummy_files(tmp_path):
    """Creates dummy files for testing."""
    (tmp_path / "pyproject.toml").touch()
    (tmp_path / "requirements.txt").touch()
    (tmp_path / ".git").mkdir()
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "settings.json").write_text('{"project_name": "test_project", "version": "1.0.0", "author": "Test Author", "copyrihgnt": "Test Copyright", "cofee": "Test Coffee"}')
    (tmp_path / "src" / "README.MD").write_text('Test Documentation')
    return tmp_path

@pytest.fixture
def dummy_files_no_settings(tmp_path):
    """Creates dummy files without settings.json for testing."""
    (tmp_path / "pyproject.toml").touch()
    (tmp_path / "requirements.txt").touch()
    (tmp_path / ".git").mkdir()
    (tmp_path / "src").mkdir()
    return tmp_path


def test_set_project_root_with_marker_files(dummy_files):
    """Checks if set_project_root returns the correct root path when marker files are present."""
    root_path = set_project_root(marker_files=("pyproject.toml", "requirements.txt", ".git"))
    assert root_path == dummy_files
    assert str(root_path) in sys.path
    
def test_set_project_root_with_custom_marker_files(dummy_files):
    """Checks if set_project_root returns the correct root path when custom marker files are passed."""
    
    (dummy_files / "custom.marker").touch()
    root_path = set_project_root(marker_files=("custom.marker",))
    assert root_path == dummy_files
    assert str(root_path) in sys.path

def test_set_project_root_no_marker_files(tmp_path):
    """Checks if set_project_root returns the current directory when no marker files are found."""
    
    test_file = tmp_path / "test.py"
    test_file.touch()
    
    # Ensure the test file's directory is included as the starting point
    current_dir = test_file.resolve().parent
    
    with patch("hypotez.src.suppliers.kualastyle.header.__file__", str(test_file)):
        root_path = set_project_root(marker_files=("nonexistent_file",))
    assert root_path == current_dir
    assert str(root_path) in sys.path

def test_set_project_root_no_marker_files_in_parents(tmp_path):
    """Checks if set_project_root returns the current directory when no marker files are found in the current or parent directories."""
    test_file = tmp_path / "subdir" / "test.py"
    test_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.touch()
    
    with patch("hypotez.src.suppliers.kualastyle.header.__file__", str(test_file)):
        root_path = set_project_root(marker_files=("nonexistent_file",))
    
    assert root_path == test_file.resolve().parent
    assert str(root_path) in sys.path

def test_global_variables_with_settings(dummy_files):
    """Checks if global variables are correctly loaded from settings.json."""
    assert __project_name__ == "test_project"
    assert __version__ == "1.0.0"
    assert __doc__ == "Test Documentation"
    assert __author__ == "Test Author"
    assert __copyright__ == "Test Copyright"
    assert __cofee__ == "Test Coffee"


def test_global_variables_no_settings(dummy_files_no_settings):
     """Checks if default values are assigned when settings.json is not found."""
     assert __project_name__ == "hypotez"
     assert __version__ == ""
     assert __doc__ == ""
     assert __author__ == ""
     assert __copyright__ == ""
     assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


def test_global_variables_with_invalid_json(tmp_path):
    """Checks if default values are assigned when settings.json contains invalid JSON."""
    (tmp_path / "pyproject.toml").touch()
    (tmp_path / "requirements.txt").touch()
    (tmp_path / ".git").mkdir()
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "settings.json").write_text('invalid json')
    (tmp_path / "src" / "README.MD").write_text('Test Documentation')
    
    with patch("hypotez.src.suppliers.kualastyle.header.__file__", str(tmp_path / 'test.py')):
        set_project_root(marker_files=("pyproject.toml", "requirements.txt", ".git"))
    
    assert __project_name__ == "hypotez"
    assert __version__ == ""
    assert __doc__ == "Test Documentation"
    assert __author__ == ""
    assert __copyright__ == ""
    assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


def test_global_variables_no_readme(tmp_path):
    """Checks if default values are assigned when README.MD is not found."""
    (tmp_path / "pyproject.toml").touch()
    (tmp_path / "requirements.txt").touch()
    (tmp_path / ".git").mkdir()
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "settings.json").write_text('{"project_name": "test_project", "version": "1.0.0", "author": "Test Author", "copyrihgnt": "Test Copyright", "cofee": "Test Coffee"}')
    
    with patch("hypotez.src.suppliers.kualastyle.header.__file__", str(tmp_path / 'test.py')):
        set_project_root(marker_files=("pyproject.toml", "requirements.txt", ".git"))
        
    assert __project_name__ == "test_project"
    assert __version__ == "1.0.0"
    assert __doc__ == ""
    assert __author__ == "Test Author"
    assert __copyright__ == "Test Copyright"
    assert __cofee__ == "Test Coffee"
```