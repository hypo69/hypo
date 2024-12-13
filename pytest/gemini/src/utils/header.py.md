```python
import pytest
import sys
from pathlib import Path
from unittest.mock import mock_open, patch
import json
from packaging.version import Version

from hypotez.src.utils.header import set_project_root, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__


# Fixture definitions
@pytest.fixture
def mock_file_exists():
    """Mocks the exist method of the Path class."""
    with patch("pathlib.Path.exists") as mock_exists:
        yield mock_exists

@pytest.fixture
def mock_open_settings_file():
    """Mocks the open function for settings.json."""
    settings_data = {
        "project_name": "test_project",
        "version": "1.0.0",
        "author": "test_author",
        "copyrihgnt": "test_copyright",
        "cofee": "test_cofee_url"
    }
    
    with patch("builtins.open", mock_open(read_data=json.dumps(settings_data))) as mock_file:
       yield mock_file

@pytest.fixture
def mock_open_readme_file():
    """Mocks the open function for README.MD."""
    readme_data = "This is a test readme file."
    with patch("builtins.open", mock_open(read_data=readme_data)) as mock_file:
        yield mock_file

@pytest.fixture
def mock_path_is_file():
    """Mocks the is_file method of the Path class."""
    with patch("pathlib.Path.is_file", return_value=True) as mock_is_file:
        yield mock_is_file

@pytest.fixture
def mock_path_resolve():
    """Mocks the resolve method of the Path class."""
    with patch("pathlib.Path.resolve", return_value=Path("/test/project/src/header.py")) as mock_resolve:
        yield mock_resolve
    
@pytest.fixture
def mock_path_parent():
     """Mocks the parent method of the Path class."""
     with patch("pathlib.Path.parent", return_value=Path("/test/project/src")) as mock_parent:
        yield mock_parent
    


# Tests for set_project_root
def test_set_project_root_finds_root(mock_file_exists,mock_path_resolve):
    """Checks if the function correctly finds the root directory."""
    mock_file_exists.side_effect = lambda path: str(path).endswith("pyproject.toml")
    
    root_path = set_project_root()
    
    assert str(root_path) == "/test/project"
    assert str(Path("/test/project")) in sys.path



def test_set_project_root_no_marker_files(mock_file_exists,mock_path_resolve,mock_path_parent):
    """Checks if the function returns the current directory when no marker files are found."""
    mock_file_exists.return_value = False
    
    root_path = set_project_root()
    
    assert str(root_path) == "/test/project/src"
    assert str(Path("/test/project/src")) in sys.path


def test_set_project_root_custom_marker_files(mock_file_exists,mock_path_resolve):
    """Checks if the function correctly uses custom marker files."""
    mock_file_exists.side_effect = lambda path: str(path).endswith("custom.txt")
    
    root_path = set_project_root(marker_files=("custom.txt",))
    
    assert str(root_path) == "/test/project"
    assert str(Path("/test/project")) in sys.path

def test_set_project_root_empty_marker_files(mock_file_exists,mock_path_resolve,mock_path_parent):
    """Checks if the function returns the current directory when no marker files are provided."""
    mock_file_exists.return_value = False
    
    root_path = set_project_root(marker_files=())
    
    assert str(root_path) == "/test/project/src"
    assert str(Path("/test/project/src")) in sys.path

def test_project_root_already_in_path(mock_file_exists,mock_path_resolve,monkeypatch):
    """Checks if the function doesn't add the root to sys.path if it's already there."""
    mock_file_exists.side_effect = lambda path: str(path).endswith("pyproject.toml")
    
    monkeypatch.setattr(sys, 'path', ["/test/project"])
    
    root_path = set_project_root()
    assert str(root_path) == "/test/project"
    assert sys.path == ["/test/project"]

# Test for project metadata
def test_project_metadata_with_settings(mock_open_settings_file, mock_open_readme_file):
    """Checks if the metadata variables are correctly loaded from settings.json and README.MD."""
    assert __project_name__ == "test_project"
    assert __version__ == "1.0.0"
    assert __doc__ == "This is a test readme file."
    assert __author__ == "test_author"
    assert __copyright__ == "test_copyright"
    assert __cofee__ == "test_cofee_url"

def test_project_metadata_no_settings(monkeypatch, mock_open_readme_file):
    """Checks if the metadata variables have default values when settings.json is missing."""
    monkeypatch.setattr('hypotez.src.utils.header.settings',None)
    assert __project_name__ == "hypotez"
    assert __version__ == ""
    assert __doc__ == "This is a test readme file."
    assert __author__ == ""
    assert __copyright__ == ""
    assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_project_metadata_no_settings_no_readme(monkeypatch):
    """Checks if the metadata variables have default values when settings.json and README.MD are missing."""
    monkeypatch.setattr('hypotez.src.utils.header.settings',None)
    monkeypatch.setattr('hypotez.src.utils.header.doc_str',None)
    assert __project_name__ == "hypotez"
    assert __version__ == ""
    assert __doc__ == ""
    assert __author__ == ""
    assert __copyright__ == ""
    assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_project_metadata_empty_settings_values(monkeypatch, mock_open_settings_file,mock_open_readme_file):
    """Checks if the metadata variables are set to default values when settings.json keys are missing."""
    settings_data = {
        "project_name": "",
        "version": "",
        "author": "",
        "copyrihgnt": "",
        "cofee": ""
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(settings_data))) as mock_file:
        monkeypatch.setattr('hypotez.src.utils.header.settings',json.loads(mock_file.read()))
        assert __project_name__ == ""
        assert __version__ == ""
        assert __author__ == ""
        assert __copyright__ == ""
        assert __cofee__ == ""
        
def test_project_metadata_readme_not_found(monkeypatch, mock_open_settings_file):
        """Checks if the metadata variables have default values when README.MD is missing."""
        monkeypatch.setattr('hypotez.src.utils.header.doc_str',None)
        assert __project_name__ == "test_project"
        assert __version__ == "1.0.0"
        assert __doc__ == ""
        assert __author__ == "test_author"
        assert __copyright__ == "test_copyright"
        assert __cofee__ == "test_cofee_url"
```