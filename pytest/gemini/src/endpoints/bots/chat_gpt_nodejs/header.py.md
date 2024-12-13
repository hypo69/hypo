```python
import pytest
from pathlib import Path
import sys
import json
from packaging.version import Version
from unittest.mock import mock_open, patch
from hypotez.src.endpoints.bots.chat_gpt_nodejs.header import set_project_root, __root__, settings, doc_str, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__
from hypotez.src import gs

# Fixture for creating dummy files and directories
@pytest.fixture
def dummy_project(tmp_path):
    """Creates a dummy project structure for testing."""
    # Create dummy files
    (tmp_path / "pyproject.toml").touch()
    (tmp_path / "requirements.txt").touch()
    (tmp_path / ".git").mkdir()
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "settings.json").write_text('{"project_name": "test_project", "version": "1.0.0", "author": "Test Author", "copyrihgnt": "Test Copyright"}')
    (tmp_path / "src" / "README.MD").write_text("Test project documentation.")
    
    return tmp_path

def test_set_project_root_with_marker_files(dummy_project):
    """Test that set_project_root correctly identifies the project root when marker files exist."""
    project_root = set_project_root()
    assert project_root == dummy_project
    assert str(dummy_project) in sys.path

def test_set_project_root_no_marker_files():
    """Test that set_project_root returns current script's parent when no marker files are found."""
    current_file_path = Path(__file__).resolve()
    project_root = set_project_root(marker_files=['nonexistent_marker'])
    assert project_root == current_file_path.parent
    assert str(current_file_path.parent) in sys.path

def test_set_project_root_empty_marker_files():
    """Test that set_project_root returns current script's parent when empty marker files."""
    current_file_path = Path(__file__).resolve()
    project_root = set_project_root(marker_files=[])
    assert project_root == current_file_path.parent
    assert str(current_file_path.parent) in sys.path

def test_global_root_variable_populated(dummy_project):
     """Tests if the global __root__ variable is populated correctly after calling the function."""
     
     assert __root__ == dummy_project

def test_settings_loaded_correctly(dummy_project):
    """Tests if the global settings variable is loaded correctly from the settings.json file."""
    assert settings == {"project_name": "test_project", "version": "1.0.0", "author": "Test Author", "copyrihgnt": "Test Copyright"}

def test_doc_str_loaded_correctly(dummy_project):
    """Tests if the global doc_str variable is loaded correctly from the README.MD file."""
    assert doc_str == "Test project documentation."

def test_settings_file_not_found():
    """Tests that settings remains None when settings.json is not found."""
    with patch("hypotez.src.endpoints.bots.chat_gpt_nodejs.header.gs.path.root", new=Path("/tmp/nonexistent")):
      
        assert set_project_root()  != Path("/tmp/nonexistent")
        assert settings is None

def test_readme_file_not_found():
    """Tests that doc_str remains None when README.MD is not found."""
    with patch("hypotez.src.endpoints.bots.chat_gpt_nodejs.header.gs.path.root", new=Path("/tmp/nonexistent")):
        assert set_project_root() != Path("/tmp/nonexistent")
        assert doc_str is None

def test_settings_json_decode_error(dummy_project):
    """Tests settings loading when settings.json contains invalid json."""
    (dummy_project / "src" / "settings.json").write_text('invalid json')
    with patch("hypotez.src.endpoints.bots.chat_gpt_nodejs.header.gs.path.root", new=dummy_project):
        assert set_project_root() == dummy_project
        assert settings is None

def test_readme_json_decode_error(dummy_project):
      """Tests doc_str loading when README.MD is not readable."""
      (dummy_project / "src" / "README.MD").write_text('\xff\xff\xff')
      with patch("hypotez.src.endpoints.bots.chat_gpt_nodejs.header.gs.path.root", new=dummy_project):
         assert set_project_root() == dummy_project
         assert doc_str is None

def test_global_project_name(dummy_project):
    """Tests that the global project_name variable is loaded correctly."""
    assert __project_name__ == "test_project"

def test_global_version(dummy_project):
    """Tests that the global version variable is loaded correctly."""
    assert __version__ == "1.0.0"

def test_global_doc(dummy_project):
    """Tests that the global doc variable is loaded correctly."""
    assert __doc__ == "Test project documentation."
    
def test_global_details(dummy_project):
      """Tests that the global details variable is empty by default."""
      assert __details__ == ""

def test_global_author(dummy_project):
    """Tests that the global author variable is loaded correctly."""
    assert __author__ == "Test Author"

def test_global_copyright(dummy_project):
    """Tests that the global copyright variable is loaded correctly."""
    assert __copyright__ == "Test Copyright"

def test_global_cofee(dummy_project):
    """Tests that the global cofee variable is loaded correctly."""
    assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def test_global_cofee_no_settings(dummy_project):
     """Test that default value is assigned for cofee variable if no settings file is present."""
     with patch("hypotez.src.endpoints.bots.chat_gpt_nodejs.header.gs.path.root", new=Path("/tmp/nonexistent")):
        assert set_project_root() != Path("/tmp/nonexistent")
        assert __cofee__ == "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```