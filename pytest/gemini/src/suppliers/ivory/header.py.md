```python
import pytest
import sys
from pathlib import Path
import json
from unittest.mock import patch, mock_open

from packaging.version import Version

from src.suppliers.ivory.header import set_project_root, __root__, settings, doc_str, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

# Fixture for creating dummy files and directories
@pytest.fixture
def create_dummy_project(tmp_path):
    """Creates a dummy project structure for testing."""
    # Create marker files in different directories
    (tmp_path / "marker1").mkdir()
    (tmp_path / "marker1" / 'pyproject.toml').touch()
    (tmp_path / "marker2").mkdir()
    (tmp_path / "marker2" / 'requirements.txt').touch()
    (tmp_path / "marker3").mkdir()
    (tmp_path / "marker3" / '.git').mkdir()

    #create a settings.json and README.md
    (tmp_path / "src").mkdir()
    with open(tmp_path / "src" / "settings.json", "w") as f:
        json.dump({"project_name": "test_project", "version": "1.0.0", "author": "test_author", "copyrihgnt":"test_copyright"}, f)
    
    with open(tmp_path / "src" / "README.MD", "w") as f:
        f.write("test_doc_str")

    
    return tmp_path

def test_set_project_root_with_marker_file_in_parent(create_dummy_project):
    """Tests that set_project_root finds the root with marker file in a parent directory."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        root_path = set_project_root()
        assert root_path == create_dummy_project / "marker1"
        assert str(root_path) in sys.path

def test_set_project_root_with_no_marker_file(create_dummy_project):
    """Tests that set_project_root returns the current directory when no marker file is found."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      root_path = set_project_root()
      assert root_path == create_dummy_project
      assert str(root_path) in sys.path

def test_set_project_root_with_multiple_marker_files_in_different_parents(create_dummy_project):
    """Tests that set_project_root stops at the first marker file found."""
    
    current_file = create_dummy_project / "marker2" / "subfolder" / "some_file.py"
    current_file.parent.mkdir()
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        root_path = set_project_root()
        assert root_path == create_dummy_project / "marker2"
        assert str(root_path) in sys.path

def test_set_project_root_with_multiple_marker_files_in_same_parents(create_dummy_project):
    """Tests that set_project_root finds root when more then one marker in same dir"""
    
    current_file = create_dummy_project / "marker3" / "some_file.py"
    current_file.touch()
    (create_dummy_project / "marker3" / "requirements.txt").touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        root_path = set_project_root()
        assert root_path == create_dummy_project / "marker3"
        assert str(root_path) in sys.path

def test_set_project_root_with_empty_marker_files_list(create_dummy_project):
    """Tests that set_project_root returns the current directory when the marker file list is empty."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      root_path = set_project_root(marker_files=())
      assert root_path == create_dummy_project
      assert str(root_path) in sys.path

def test_global_root_variable_is_set(create_dummy_project):
    """Tests that the global __root__ variable is set correctly."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      # Import to trigger the code
      from src.suppliers.ivory import header
      assert header.__root__ == create_dummy_project / "marker1"

def test_settings_loaded_correctly(create_dummy_project):
    """Tests that the settings are loaded correctly from the json file."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.settings == {
            "project_name": "test_project",
             "version": "1.0.0", 
             "author": "test_author", 
             "copyrihgnt":"test_copyright"
             }

def test_settings_not_loaded_if_json_is_invalid(create_dummy_project):
    """Tests that the settings are loaded correctly from the json file."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with open(create_dummy_project / "src" / "settings.json", "w") as f:
      f.write("invalid_json")

    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.settings == None

def test_settings_not_loaded_if_file_not_found(create_dummy_project):
      
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()

    (create_dummy_project / "src" / "settings.json").unlink()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.settings == None


def test_doc_str_loaded_correctly(create_dummy_project):
    """Tests that the doc_str is loaded correctly from the README.MD file."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.doc_str == "test_doc_str"

def test_doc_str_not_loaded_if_file_not_found(create_dummy_project):
    """Tests that the doc_str is loaded correctly from the json file."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    (create_dummy_project / "src" / "README.MD").unlink()

    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.doc_str == None

def test_project_name_from_settings(create_dummy_project):
    """Tests that the project name is loaded correctly from settings."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.__project_name__ == "test_project"

def test_project_name_default(create_dummy_project):
    """Tests that the project name is set to default when settings is None."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    
    (create_dummy_project / "src" / "settings.json").unlink()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.__project_name__ == "hypotez"

def test_version_from_settings(create_dummy_project):
    """Tests that the project version is loaded correctly from settings."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      from src.suppliers.ivory import header
      assert header.__version__ == "1.0.0"

def test_version_default(create_dummy_project):
    """Tests that the project version is set to default when settings is None."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    (create_dummy_project / "src" / "settings.json").unlink()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.__version__ == ""

def test_doc_from_doc_str(create_dummy_project):
  """Tests that the __doc__ variable is set from doc_str."""

  current_file = create_dummy_project / "marker1" / "some_file.py"
  current_file.touch()

  with patch('src.suppliers.ivory.header.__file__', str(current_file)):
    from src.suppliers.ivory import header
    assert header.__doc__ == "test_doc_str"

def test_doc_default_if_doc_str_is_None(create_dummy_project):
  """Tests that the __doc__ is set to the default empty string if doc_str is None."""

  current_file = create_dummy_project / "some_file.py"
  current_file.touch()
  (create_dummy_project / "src" / "README.MD").unlink()

  with patch('src.suppliers.ivory.header.__file__', str(current_file)):
    from src.suppliers.ivory import header
    assert header.__doc__ == ""

def test_author_from_settings(create_dummy_project):
    """Tests that the author is loaded correctly from settings."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      from src.suppliers.ivory import header
      assert header.__author__ == "test_author"

def test_author_default(create_dummy_project):
    """Tests that the author is set to default when settings is None."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    (create_dummy_project / "src" / "settings.json").unlink()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.__author__ == ""

def test_copyright_from_settings(create_dummy_project):
    """Tests that the copyright is loaded correctly from settings."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      from src.suppliers.ivory import header
      assert header.__copyright__ == "test_copyright"

def test_copyright_default(create_dummy_project):
    """Tests that the copyright is set to default when settings is None."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    (create_dummy_project / "src" / "settings.json").unlink()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.__copyright__ == ""

def test_cofee_from_settings(create_dummy_project):
    """Tests that the coffee is loaded correctly from settings."""
    
    current_file = create_dummy_project / "marker1" / "some_file.py"
    current_file.touch()
    
    with open(create_dummy_project / "src" / "settings.json", "w") as f:
        json.dump({"project_name": "test_project", "version": "1.0.0", "author": "test_author", "copyrihgnt":"test_copyright", "cofee":"test_cofee"}, f)
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
      from src.suppliers.ivory import header
      assert header.__cofee__ == "test_cofee"

def test_cofee_default(create_dummy_project):
    """Tests that the coffee is set to default when settings is None."""
    
    current_file = create_dummy_project / "some_file.py"
    current_file.touch()
    (create_dummy_project / "src" / "settings.json").unlink()
    
    with patch('src.suppliers.ivory.header.__file__', str(current_file)):
        from src.suppliers.ivory import header
        assert header.__cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```