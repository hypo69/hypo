```python
import pytest
from pathlib import Path
import sys
import json
from unittest.mock import patch, mock_open

# Assuming the code is in a file named header.py
from hypotez.src.suppliers.chat_gpt import header

@pytest.fixture
def mock_root_path(tmp_path):
    """Creates a temporary directory structure for testing."""
    
    project_root = tmp_path / "project"
    project_root.mkdir()
    (project_root / "src").mkdir()
    (project_root / "pyproject.toml").touch()
    (project_root / "src" / "settings.json").write_text('{"project_name": "test_project", "version": "0.1.0", "author": "test_author", "copyrihgnt": "test_copyright", "cofee": "test_cofee" }')
    (project_root / "src" / "README.MD").write_text("This is a test README.")
    return project_root

@pytest.fixture
def mock_empty_root_path(tmp_path):
    """Creates a temporary directory structure for testing."""
    project_root = tmp_path / "project_empty"
    project_root.mkdir()
    (project_root / "src").mkdir()

    return project_root

def test_set_project_root_with_marker(mock_root_path,monkeypatch):
    """Checks if the function correctly identifies the project root."""
    # Patch __file__ for test case
    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "test_file.py"))

    root_path = header.set_project_root()
    assert root_path == mock_root_path
    assert str(mock_root_path) in sys.path
    
def test_set_project_root_no_marker(tmp_path,monkeypatch):
    """Checks if the function returns the current directory when no marker is found."""
    current_path = tmp_path / "test_dir"
    current_path.mkdir()
    monkeypatch.setattr(header, "__file__", str(current_path / "test_file.py"))
    
    root_path = header.set_project_root()
    assert root_path == current_path
    assert str(current_path) in sys.path
   
def test_set_project_root_custom_markers(mock_root_path,monkeypatch):
        
    project_root = mock_root_path
    (project_root / "custom_marker.txt").touch()

    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "test_file.py"))
    
    root_path = header.set_project_root(marker_files=("custom_marker.txt",))

    assert root_path == mock_root_path
    assert str(mock_root_path) in sys.path

def test_set_project_root_with_parent_marker(mock_root_path,monkeypatch):
    
    project_root = mock_root_path
    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "test_file.py"))
    
    (project_root / "src" / "subdir").mkdir()
    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "subdir" / "test_file.py"))
    root_path = header.set_project_root()
    assert root_path == mock_root_path
    assert str(mock_root_path) in sys.path
    

def test_global_variables_with_settings(mock_root_path,monkeypatch):
    """Tests the global variables are loaded correctly with settings file"""
    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "test_file.py"))

    #Force the variables to reload
    header.__root__= None
    header.settings = None
    header.doc_str = None

    header.set_project_root()

    assert header.__project_name__ == "test_project"
    assert header.__version__ == "0.1.0"
    assert header.__doc__ == "This is a test README."
    assert header.__author__ == "test_author"
    assert header.__copyright__ == "test_copyright"
    assert header.__cofee__ == "test_cofee"


def test_global_variables_no_settings(mock_empty_root_path, monkeypatch):
    """Tests the global variables are loaded correctly without settings file"""
    monkeypatch.setattr(header, "__file__", str(mock_empty_root_path / "src" / "test_file.py"))
    header.__root__ = None
    header.settings = None
    header.doc_str = None
    header.set_project_root()

    assert header.__project_name__ == "hypotez"
    assert header.__version__ == ""
    assert header.__doc__ == ""
    assert header.__author__ == ""
    assert header.__copyright__ == ""
    assert header.__cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


def test_global_variables_with_invalid_json(mock_root_path, monkeypatch):
    """Tests the global variables are loaded correctly with a invalid settings file"""
    (mock_root_path / "src" / "settings.json").write_text('{"project_name": "test_project", "version": "0.1.0", "author": "test_author", "copyrihgnt": "test_copyright", "cofee": "test_cofee" ')

    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "test_file.py"))
    header.__root__= None
    header.settings = None
    header.doc_str = None
    header.set_project_root()
    
    assert header.__project_name__ == "hypotez"
    assert header.__version__ == ""
    assert header.__doc__ == ""
    assert header.__author__ == ""
    assert header.__copyright__ == ""
    assert header.__cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_global_variables_missing_readme(mock_root_path, monkeypatch):
        
    monkeypatch.setattr(header, "__file__", str(mock_root_path / "src" / "test_file.py"))

    #Force the variables to reload
    header.__root__= None
    header.settings = None
    header.doc_str = None
    
    (mock_root_path / "src" / "README.MD").unlink()

    header.set_project_root()

    assert header.__project_name__ == "test_project"
    assert header.__version__ == "0.1.0"
    assert header.__doc__ == ""
    assert header.__author__ == "test_author"
    assert header.__copyright__ == "test_copyright"
    assert header.__cofee__ == "test_cofee"

```