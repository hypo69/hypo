```python
import pytest
import sys
from pathlib import Path
import json
from unittest.mock import mock_open, patch
from packaging.version import Version


# Fixture definitions
@pytest.fixture
def mock_file_open():
    """Mocks the built-in open function."""
    with patch("builtins.open", mock_open()) as mock_open_func:
        yield mock_open_func


@pytest.fixture
def mock_sys_path():
    """Mocks sys.path for testing."""
    original_sys_path = sys.path.copy()
    yield sys.path
    sys.path = original_sys_path


@pytest.fixture
def create_temp_files(tmp_path):
    """Creates temporary files for testing."""
    def _create_files(files):
        for filename, content in files.items():
            file_path = tmp_path / filename
            if isinstance(content, dict):
                 with open(file_path, 'w') as f:
                    json.dump(content, f)
            else:
                file_path.write_text(content)
        return tmp_path
    return _create_files



# Tests for set_project_root function
def test_set_project_root_with_marker_file_in_current_dir(mock_sys_path, create_temp_files):
    """Checks if the root is set correctly when marker file is in the current directory."""
    test_dir = create_temp_files({'pyproject.toml': ''})
    # Mock __file__ to be in the created test_dir
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / "test_header.py")):
      from hypotez.src.webdriver.firefox import header
      root = header.set_project_root()
      assert root == test_dir
      assert str(test_dir) in mock_sys_path[0]



def test_set_project_root_with_marker_file_in_parent_dir(mock_sys_path, create_temp_files):
    """Checks if the root is set correctly when marker file is in parent directory."""
    test_dir = create_temp_files({'parent': {'requirements.txt': ''}, 'child':{}})
    # Mock __file__ to be in the child folder
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / "child" / "test_header.py")):
      from hypotez.src.webdriver.firefox import header
      root = header.set_project_root()
      assert root == test_dir / "parent"
      assert str(test_dir / "parent") in mock_sys_path[0]


def test_set_project_root_no_marker_files(mock_sys_path, create_temp_files):
    """Checks if the root is set to the current dir if no marker file is found."""
    test_dir = create_temp_files({'test_dir':{}})
     # Mock __file__ to be in the test_dir
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'test_dir' /"test_header.py")):
      from hypotez.src.webdriver.firefox import header
      root = header.set_project_root()
      assert root == test_dir / 'test_dir'
      assert str(test_dir/ 'test_dir') in mock_sys_path[0]


def test_set_project_root_custom_marker_files(mock_sys_path, create_temp_files):
    """Checks if the root is set correctly with custom marker files."""
    test_dir = create_temp_files({'test_dir':{'custom.marker': ''}})
     # Mock __file__ to be in the test_dir
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'test_dir'/ "test_header.py")):
        from hypotez.src.webdriver.firefox import header
        root = header.set_project_root(marker_files=('custom.marker',))
        assert root == test_dir / 'test_dir'
        assert str(test_dir / 'test_dir') in mock_sys_path[0]



def test_set_project_root_already_in_sys_path(mock_sys_path, create_temp_files):
    """Checks if the root path is not added again if it's already in sys.path."""
    test_dir = create_temp_files({'pyproject.toml': ''})
    mock_sys_path.insert(0, str(test_dir))
      # Mock __file__ to be in the test_dir
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / "test_header.py")):
        from hypotez.src.webdriver.firefox import header
        root = header.set_project_root()
        assert root == test_dir
        assert mock_sys_path.count(str(test_dir)) == 1


# Tests for global variables and file loading
def test_global_settings_load_success(mock_file_open, create_temp_files):
    """Checks if settings are loaded successfully from settings.json."""
    test_dir = create_temp_files({'src/settings.json': '{"project_name": "test_project", "version": "1.0.0", "author":"test_author","copyrihgnt":"test_copyright", "cofee":"test_cofee"}'})
    # Mock __file__ to be in a subfolder
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'subfolder' / "test_header.py")):
      from hypotez.src.webdriver.firefox import header
      assert header.settings == {"project_name": "test_project", "version": "1.0.0", "author":"test_author","copyrihgnt":"test_copyright", "cofee":"test_cofee"}
      assert header.__project_name__ == "test_project"
      assert header.__version__ == "1.0.0"
      assert header.__author__ == "test_author"
      assert header.__copyright__ == "test_copyright"
      assert header.__cofee__ == "test_cofee"

def test_global_settings_load_file_not_found(mock_file_open, create_temp_files):
    """Checks if default settings are used when settings.json is not found."""
    test_dir = create_temp_files({})
    # Mock __file__ to be in a subfolder
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'subfolder' / "test_header.py")):
      from hypotez.src.webdriver.firefox import header
      assert header.settings == None
      assert header.__project_name__ == "hypotez"
      assert header.__version__ == ""
      assert header.__author__ == ""
      assert header.__copyright__ == ""
      assert header.__cofee__ ==  "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_global_settings_load_json_decode_error(mock_file_open, create_temp_files):
    """Checks if default settings are used when settings.json has decode error."""
    test_dir = create_temp_files({'src/settings.json': 'invalid json'})
    # Mock __file__ to be in a subfolder
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'subfolder' / "test_header.py")):
      from hypotez.src.webdriver.firefox import header
      assert header.settings == None
      assert header.__project_name__ == "hypotez"
      assert header.__version__ == ""
      assert header.__author__ == ""
      assert header.__copyright__ == ""
      assert header.__cofee__ ==  "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_global_doc_str_load_success(mock_file_open, create_temp_files):
     """Checks if the doc_str is loaded from README.MD successfully."""
     test_dir = create_temp_files({'src/README.MD': 'Test doc string'})
     # Mock __file__ to be in a subfolder
     with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'subfolder' / "test_header.py")):
       from hypotez.src.webdriver.firefox import header
       assert header.doc_str == "Test doc string"
       assert header.__doc__ == "Test doc string"

def test_global_doc_str_load_file_not_found(mock_file_open, create_temp_files):
    """Checks if the doc_str is empty when README.MD is not found."""
    test_dir = create_temp_files({})
     # Mock __file__ to be in a subfolder
    with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'subfolder' / "test_header.py")):
      from hypotez.src.webdriver.firefox import header
      assert header.doc_str == None
      assert header.__doc__ == ""

# def test_global_doc_str_load_decode_error(mock_file_open, create_temp_files):
#     """Checks if the doc_str is empty when README.MD has decode error."""
#     test_dir = create_temp_files({'src/README.MD': b'invalid text'})
#     # Mock __file__ to be in a subfolder
#     with patch("hypotez.src.webdriver.firefox.header.__file__", str(test_dir / 'subfolder' / "test_header.py")):
#       from hypotez.src.webdriver.firefox import header
#       assert header.doc_str == None
#       assert header.__doc__ == ""

def test_version_is_instance_of_packaging_version():
     """Test that the loaded version is instance of packaging.version.Version"""
     from hypotez.src.webdriver.firefox import header
     assert isinstance(Version(header.__version__),Version)
```