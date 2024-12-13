```python
import pytest
from pathlib import Path
import sys
import json
from unittest.mock import patch, mock_open
from packaging.version import Version

# Assuming the header.py file is in the same directory as the test file,
# if not adjust the sys.path accordingly to import the functions
from hypotez.src.suppliers.wallmart import header


# Fixture for a mock project root
@pytest.fixture
def mock_project_root(tmp_path):
    """Creates a temporary directory structure for testing and returns its path."""
    root = tmp_path / "mock_project"
    root.mkdir()
    (root / "pyproject.toml").touch()
    (root / "src").mkdir()
    (root / "src" / "settings.json").touch()
    (root / "src" / "README.MD").touch()
    
    return root

# Fixture for a mock project root without marker files
@pytest.fixture
def mock_project_root_no_markers(tmp_path):
    """Creates a temporary directory structure for testing with no marker files and returns its path."""
    root = tmp_path / "mock_project_no_markers"
    root.mkdir()
    (root / "src").mkdir()
    return root

# Fixture to mock gs.path.root
@pytest.fixture
def mock_gs_path_root(mock_project_root):
     """Mock gs.path.root for testing."""
     
     with patch("hypotez.src.suppliers.wallmart.header.gs.path") as mock_path:
          mock_path.root = mock_project_root
          yield mock_path

# Fixture for settings data
@pytest.fixture
def settings_data():
    """Provides sample settings data."""
    return {
        "project_name": "test_project",
        "version": "1.2.3",
        "author": "Test Author",
        "copyrihgnt": "Test Copyright",
        "cofee": "Test Coffee Link"
    }


# Tests for set_project_root
def test_set_project_root_with_marker_file(mock_project_root):
    """Checks if the function correctly identifies the project root with a marker file."""
    
    project_root = header.set_project_root()
    assert project_root == mock_project_root
    assert str(project_root) in sys.path


def test_set_project_root_no_marker_files(mock_project_root_no_markers):
    """Checks if the function correctly returns the script directory if no marker files found."""
    current_dir = Path(__file__).resolve().parent
    project_root = header.set_project_root()
    assert project_root == current_dir
    assert str(project_root) in sys.path

def test_set_project_root_custom_marker_files(tmp_path):
      """Checks the behavior with a custom set of marker files."""
      custom_root = tmp_path / "custom_project"
      custom_root.mkdir()
      (custom_root / "custom_marker.txt").touch()
      project_root = header.set_project_root(marker_files=("custom_marker.txt",))
      assert project_root == custom_root
      assert str(project_root) in sys.path
      

def test_set_project_root_empty_marker_files(tmp_path):
      """Checks if the function returns the script directory if no marker files are provided."""
      current_dir = Path(__file__).resolve().parent
      project_root = header.set_project_root(marker_files=())
      assert project_root == current_dir
      assert str(project_root) in sys.path



# Tests for global variables
def test_global_variables_with_settings(mock_project_root, mock_gs_path_root, settings_data):
    """Checks if the global variables are correctly set when settings are available."""

    mocked_settings_file = mock_open(read_data=json.dumps(settings_data))

    with patch("builtins.open", mocked_settings_file):
        # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header

        assert header.__project_name__ == settings_data["project_name"]
        assert header.__version__ == settings_data["version"]
        assert header.__author__ == settings_data["author"]
        assert header.__copyright__ == settings_data["copyrihgnt"]
        assert header.__cofee__ == settings_data["cofee"]


def test_global_variables_no_settings(mock_project_root, mock_gs_path_root):
    """Checks if the global variables are correctly set with default values when no settings are available."""
    mocked_settings_file = mock_open(read_data='{ "test": true }')

    with patch("builtins.open", mocked_settings_file):
         # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header
        
        assert header.__project_name__ == 'hypotez'
        assert header.__version__ == ''
        assert header.__author__ == ''
        assert header.__copyright__ == ''
        assert header.__cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


def test_global_variables_file_not_found(mock_project_root, mock_gs_path_root):
    """Checks if the global variables are correctly set with default values when settings file not found."""
    
    with patch("builtins.open", side_effect=FileNotFoundError):
        # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header

        assert header.__project_name__ == 'hypotez'
        assert header.__version__ == ''
        assert header.__author__ == ''
        assert header.__copyright__ == ''
        assert header.__cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
        
def test_global_variables_invalid_json(mock_project_root, mock_gs_path_root):
    """Checks if the global variables are correctly set with default values when settings file contains invalid json."""
    mocked_settings_file = mock_open(read_data="invalid json")
    with patch("builtins.open", mocked_settings_file):
        # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header

        assert header.__project_name__ == 'hypotez'
        assert header.__version__ == ''
        assert header.__author__ == ''
        assert header.__copyright__ == ''
        assert header.__cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_doc_string_loaded_from_readme(mock_project_root, mock_gs_path_root):
    """Checks if the doc string is loaded from the README.MD"""
    readme_content = "This is a test README file."
    mocked_readme_file = mock_open(read_data=readme_content)
    with patch("builtins.open", mocked_readme_file):
          # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header
        
        assert header.__doc__ == readme_content

def test_doc_string_default_on_readme_missing(mock_project_root, mock_gs_path_root):
    """Checks if the doc string defaults to an empty string when README.MD is missing."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header
        assert header.__doc__ == ''


def test_doc_string_default_on_readme_invalid(mock_project_root, mock_gs_path_root):
    """Checks if the doc string defaults to an empty string when README.MD is invalid."""
    mocked_readme_file = mock_open(read_data='invalid file')
    with patch("builtins.open", mocked_readme_file):
        # We need to "reload" the header after mocking the open and the paths
        # This is done by getting the modules and re-importing it
        import sys
        if "hypotez.src.suppliers.wallmart.header" in sys.modules:
             del sys.modules["hypotez.src.suppliers.wallmart.header"]
        from hypotez.src.suppliers.wallmart import header
        
        assert header.__doc__ == ''
```