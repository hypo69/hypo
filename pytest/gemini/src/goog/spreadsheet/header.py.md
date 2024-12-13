```python
import pytest
from pathlib import Path
import sys
import json
from unittest.mock import patch, mock_open
from packaging.version import Version

# Assuming the code is in 'hypotez/src/goog/spreadsheet/header.py'
# We need to make sure the path is correct for importing
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from src.goog.spreadsheet.header import set_project_root, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__, settings


# Fixture definitions, if needed
@pytest.fixture
def mock_settings():
    return {
        "project_name": "test_project",
        "version": "1.2.3",
        "author": "Test Author",
        "copyrihgnt": "Test Copyright",
         "cofee": "Test Coffee"
    }

@pytest.fixture
def mock_no_settings():
    return {}

@pytest.fixture
def mock_settings_file(mock_settings):
    return json.dumps(mock_settings)


def test_set_project_root_with_marker_file():
    """Checks if project root is correctly identified using marker files."""
    # Create a dummy marker file in a parent directory
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    marker_file = parent_dir / "pyproject.toml"
    marker_file.touch()

    try:
        project_root = set_project_root()
        assert project_root == parent_dir
    finally:
         marker_file.unlink() # Clean up the dummy file
         if str(parent_dir) in sys.path:
             sys.path.remove(str(parent_dir))


def test_set_project_root_no_marker_file():
    """Checks if project root returns the current directory when no marker files are present."""
    current_dir = Path(__file__).resolve().parent
    project_root = set_project_root()
    assert project_root == current_dir
    if str(current_dir) in sys.path:
             sys.path.remove(str(current_dir))


def test_set_project_root_custom_marker_file():
    """Checks if project root correctly uses a custom marker file."""
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    custom_marker = parent_dir / "custom.marker"
    custom_marker.touch()

    try:
        project_root = set_project_root(marker_files=("custom.marker",))
        assert project_root == parent_dir
    finally:
        custom_marker.unlink() # Clean up the dummy file
        if str(parent_dir) in sys.path:
            sys.path.remove(str(parent_dir))

@patch("builtins.open", new_callable=mock_open, read_data='{"project_name": "test_project", "version": "1.2.3", "author": "Test Author", "copyrihgnt": "Test Copyright", "cofee": "Test Coffee"}')
def test_global_variables_with_settings(mock_file, mock_settings):
    """Checks if global variables are correctly initialized with settings from json file."""
    assert __project_name__ == mock_settings["project_name"]
    assert __version__ == mock_settings["version"]
    assert __author__ == mock_settings["author"]
    assert __copyright__ == mock_settings["copyrihgnt"]
    assert __cofee__ == mock_settings["cofee"]

@patch("builtins.open", new_callable=mock_open, read_data='{"version": "1.2.3"}')
def test_global_variables_missing_settings_values(mock_file, mock_no_settings):
      """Checks if global variables are correctly initialized with default values when some settings are missing from json file."""
      assert __project_name__ == "hypotez"
      assert __version__ ==  "1.2.3"
      assert __author__ == ""
      assert __copyright__ == ""
      assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


@patch("builtins.open", new_callable=mock_open, read_data="some doc string")
def test_global_doc_str_with_doc_file(mock_file):
    """Checks if the doc string from README.MD is read correctly."""
    assert __doc__ == "some doc string"


@patch("builtins.open", side_effect=FileNotFoundError)
def test_global_doc_str_no_doc_file(mock_file):
    """Checks the doc string is empty string when README.MD not exist."""
    assert __doc__ == ""


@patch("builtins.open", new_callable=mock_open, read_data='not a valid json')
def test_global_variables_invalid_settings_file(mock_file):
    """Checks if global variables are set to defaults when settings.json is invalid."""
    assert __project_name__ == "hypotez"
    assert __version__ == ""
    assert __author__ == ""
    assert __copyright__ == ""
    assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
    assert __doc__ == ""

@patch("builtins.open", side_effect=FileNotFoundError)
def test_global_variables_no_settings_file(mock_file):
    """Checks if global variables are set to default when settings.json is not found."""
    assert __project_name__ == "hypotez"
    assert __version__ == ""
    assert __author__ == ""
    assert __copyright__ == ""
    assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
    assert __doc__ == ""

def test_settings_loaded_from_json(mock_settings,mock_settings_file):
    with patch("builtins.open", mock_open(read_data=mock_settings_file)) as mock_file:
        assert settings == mock_settings

@patch("builtins.open", side_effect=FileNotFoundError)
def test_settings_not_loaded_from_json(mock_file):
    assert settings is None
```