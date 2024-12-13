```python
import pytest
import json
from pathlib import Path

# Fixture to load the package.json content
@pytest.fixture
def package_json_content():
    """Loads the content of the package.json file."""
    file_path = Path(__file__).parent / "package.json"  # Adjust the path if needed
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        pytest.fail(f"package.json not found at {file_path}")
    except json.JSONDecodeError:
        pytest.fail(f"Invalid json content at {file_path}")

def test_package_json_name(package_json_content):
    """Checks the name field of the package.json."""
    assert package_json_content.get("name") == "chatgpt-telegram", "Name field is incorrect"

def test_package_json_version(package_json_content):
    """Checks the version field of the package.json."""
    assert package_json_content.get("version") == "1.0.0", "Version field is incorrect"

def test_package_json_main_entry_point(package_json_content):
     """Checks the main entry point of the package.json."""
     assert package_json_content.get("main") == "index.js", "Main entry point is incorrect"

def test_package_json_scripts_start(package_json_content):
    """Checks the start script command in package.json"""
    assert package_json_content["scripts"].get("start") == "cross-env NODE_ENV=production node ./src/main.js", "Start script command is incorrect"

def test_package_json_scripts_dev(package_json_content):
     """Checks the dev script command in package.json"""
     assert package_json_content["scripts"].get("dev") == "cross-env NODE_ENV=development nodemon ./src/main.js", "Dev script command is incorrect"


def test_package_json_dependencies_exist(package_json_content):
    """Checks if dependencies are defined in package.json."""
    assert "dependencies" in package_json_content, "Dependencies are not defined"

def test_package_json_dev_dependencies_exist(package_json_content):
     """Checks if dev dependencies are defined in package.json."""
     assert "devDependencies" in package_json_content, "Dev dependencies are not defined"

def test_package_json_dependencies_are_not_empty(package_json_content):
     """Checks if dependencies are not empty in package.json."""
     assert package_json_content["dependencies"], "Dependencies is empty"

def test_package_json_dev_dependencies_are_not_empty(package_json_content):
     """Checks if dev dependencies are not empty in package.json."""
     assert package_json_content["devDependencies"], "Dev dependencies is empty"

def test_package_json_dependencies_telegraf(package_json_content):
    """Checks if telegraf is included in dependencies."""
    assert "telegraf" in package_json_content["dependencies"], "telegraf is not in dependencies"

def test_package_json_dependencies_openai(package_json_content):
    """Checks if openai is included in dependencies."""
    assert "openai" in package_json_content["dependencies"], "openai is not in dependencies"

def test_package_json_dependencies_config(package_json_content):
    """Checks if config is included in dependencies."""
    assert "config" in package_json_content["dependencies"], "config is not in dependencies"
    
def test_package_json_dependencies_fluent_ffmpeg(package_json_content):
    """Checks if fluent-ffmpeg is included in dependencies."""
    assert "fluent-ffmpeg" in package_json_content["dependencies"], "fluent-ffmpeg is not in dependencies"

def test_package_json_dependencies_ffmpeg_installer(package_json_content):
    """Checks if ffmpeg-installer is included in dependencies."""
    assert "@ffmpeg-installer/ffmpeg" in package_json_content["dependencies"], "@ffmpeg-installer/ffmpeg is not in dependencies"

def test_package_json_dependencies_axios(package_json_content):
    """Checks if axios is included in dependencies."""
    assert "axios" in package_json_content["dependencies"], "axios is not in dependencies"


def test_package_json_dev_dependencies_nodemon(package_json_content):
    """Checks if nodemon is included in dev dependencies."""
    assert "nodemon" in package_json_content["devDependencies"], "nodemon is not in devDependencies"

def test_package_json_dev_dependencies_cross_env(package_json_content):
    """Checks if cross-env is included in dev dependencies."""
    assert "cross-env" in package_json_content["devDependencies"], "cross-env is not in devDependencies"

def test_package_json_type(package_json_content):
    """Checks the type field in the package.json."""
    assert package_json_content.get("type") == "module", "Type field is not 'module'"

def test_package_json_empty_description(package_json_content):
    """Checks if description field is empty."""
    assert package_json_content.get("description") == "", "Description field is not empty"

def test_package_json_empty_keywords(package_json_content):
     """Checks if keywords field is an empty array."""
     assert package_json_content.get("keywords") == [], "Keywords field is not an empty array"

def test_package_json_empty_author(package_json_content):
     """Checks if author field is empty."""
     assert package_json_content.get("author") == "", "Author field is not empty"
```