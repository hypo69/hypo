```python
import pytest
import sys
import json
from pathlib import Path
from unittest.mock import mock_open, patch

from packaging.version import Version

from src.suppliers.grandadvance.header import set_project_root, __root__, settings, doc_str, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

# Fixture for creating temporary directories and files for testing purposes
@pytest.fixture
def temp_dir(tmp_path):
    """Creates a temporary directory and returns a Path object"""
    yield tmp_path

@pytest.fixture
def mock_settings_file_content():
    return {
        "project_name": "test_project",
        "version": "1.2.3",
        "author": "Test Author",
        "copyrihgnt": "Test Copyright",
         "cofee":"Test Cofee"
    }

@pytest.fixture
def mock_settings_file(temp_dir, mock_settings_file_content):
    settings_path = temp_dir / 'src' / 'settings.json'
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    with open(settings_path, 'w') as f:
      json.dump(mock_settings_file_content,f)
    return settings_path

@pytest.fixture
def mock_readme_file(temp_dir):
    readme_path = temp_dir / 'src' / 'README.MD'
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    with open(readme_path, 'w') as f:
      f.write("Test README Content")
    return readme_path

def test_set_project_root_with_marker_file_in_current_dir(temp_dir):
    """Tests that the function returns the current directory if a marker file is present"""
    (temp_dir / 'pyproject.toml').touch()
    assert set_project_root() == temp_dir
    assert str(temp_dir) in sys.path
    sys.path.remove(str(temp_dir))

def test_set_project_root_with_marker_file_in_parent_dir(temp_dir):
    """Tests that the function returns the parent directory if a marker file is present there"""
    subdir = temp_dir / 'subdir'
    subdir.mkdir()
    (temp_dir / 'requirements.txt').touch()
    assert set_project_root() == temp_dir
    assert str(temp_dir) in sys.path
    sys.path.remove(str(temp_dir))


def test_set_project_root_without_marker_files(temp_dir):
    """Tests that the function returns the current directory if no marker file is found"""
    subdir = temp_dir / 'subdir'
    subdir.mkdir()
    assert set_project_root() == Path(__file__).resolve().parent
    assert str(Path(__file__).resolve().parent) in sys.path
    sys.path.remove(str(Path(__file__).resolve().parent))

def test_set_project_root_with_custom_marker_files(temp_dir):
        """Tests that the function returns the correct directory with custom marker files"""
        subdir = temp_dir / 'subdir'
        subdir.mkdir()
        (temp_dir / "custom_marker.txt").touch()
        assert set_project_root(marker_files=("custom_marker.txt",)) == temp_dir
        assert str(temp_dir) in sys.path
        sys.path.remove(str(temp_dir))

def test_settings_loaded_successfully(mock_settings_file,mock_settings_file_content,temp_dir):
    """Tests that settings are loaded from a valid settings.json file"""
    global settings
    assert settings == mock_settings_file_content
    
    assert __project_name__ ==  mock_settings_file_content.get("project_name")
    assert __version__ ==  mock_settings_file_content.get("version")
    assert __author__ ==  mock_settings_file_content.get("author")
    assert __copyright__ ==  mock_settings_file_content.get("copyrihgnt")
    assert __cofee__ == mock_settings_file_content.get("cofee")

    
def test_settings_not_loaded_filenotfound(temp_dir):
        """Tests that settings remain None if settings.json is not found"""
        global settings
        settings=None
        global __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

        
        assert settings is None
        assert __project_name__ == 'hypotez'
        assert __version__ == ''
        assert __author__ == ''
        assert __copyright__ == ''
        assert __cofee__ ==  "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_settings_not_loaded_jsondecodeerror(temp_dir):
    """Tests that settings are none  if settings.json is invalid"""
    global settings
    settings=None
    settings_path = temp_dir / 'src' / 'settings.json'
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    with open(settings_path, 'w') as f:
      f.write("invalid json")

    global __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

    assert settings is None
    assert __project_name__ == 'hypotez'
    assert __version__ == ''
    assert __author__ == ''
    assert __copyright__ == ''
    assert __cofee__ ==  "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
    

def test_readme_loaded_successfully(mock_readme_file):
    """Tests that doc_str is loaded from a valid README.MD file"""
    global doc_str
    assert doc_str == "Test README Content"
    assert __doc__ == doc_str

def test_readme_not_loaded(temp_dir):
    """Tests that doc_str remains None if README.MD is not found"""
    global doc_str
    doc_str = None

    global __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__
    assert doc_str is None
    assert __doc__ == ''
```