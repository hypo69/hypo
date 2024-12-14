```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def valid_manifest_data():
    """Provides a valid manifest.json data."""
    return {
        "manifest_version": 2,
        "name": "Hypotez",
        "version": "1.0",
        "description": "Adds a red border",
        "icons": {
            "48": "icons/icon.png"
        },
        "browser_action": {
            "default_icon": "icons/icon.png",
            "default_title": "Hypotez",
            "default_popup": "html/popup.html"
        },
        "content_scripts": [
            {
                "matches": [ "<all_urls>" ],
                "js": [ "borderify.js" ]
            }
        ]
    }

@pytest.fixture
def invalid_manifest_data():
    """Provides an invalid manifest.json data (missing required fields)."""
    return {
        "name": "Hypotez",
        "version": "1.0",
    }


def test_valid_manifest_structure(valid_manifest_data):
    """Checks if a valid manifest.json data is structured correctly."""
    # Attempt to load it as JSON
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)

    # Check the top-level keys
    assert "manifest_version" in data
    assert "name" in data
    assert "version" in data
    assert "description" in data
    assert "icons" in data
    assert "browser_action" in data
    assert "content_scripts" in data
    
    # Check specific fields
    assert data["name"] == "Hypotez"
    assert data["version"] == "1.0"
    assert data["description"] == "Adds a red border"

    # Check nested structure within 'icons'
    assert "48" in data["icons"]
    
    # Check nested structure within 'browser_action'
    assert "default_icon" in data["browser_action"]
    assert "default_title" in data["browser_action"]
    assert "default_popup" in data["browser_action"]
    
    # Check nested structure within 'content_scripts'
    assert isinstance(data["content_scripts"], list)
    assert len(data["content_scripts"]) == 1
    assert "matches" in data["content_scripts"][0]
    assert "js" in data["content_scripts"][0]
    

def test_invalid_manifest_missing_fields(invalid_manifest_data):
    """Checks if an invalid manifest.json data with missing fields raises KeyError during checks."""
    # Attempt to load it as JSON
    json_str = json.dumps(invalid_manifest_data)
    data = json.loads(json_str)

    # Test for missing manifest_version
    with pytest.raises(KeyError):
      assert "manifest_version" in data
      
    # Check for other present fields
    assert "name" in data
    assert "version" in data

def test_manifest_version_is_integer(valid_manifest_data):
    """Checks if the manifest_version is an integer."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["manifest_version"], int)
    
def test_manifest_name_is_string(valid_manifest_data):
    """Checks if the name is a string."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["name"], str)

def test_manifest_version_is_string(valid_manifest_data):
    """Checks if the version is a string."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["version"], str)
    
def test_manifest_description_is_string(valid_manifest_data):
    """Checks if the description is a string."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["description"], str)
    
def test_manifest_icons_is_dict(valid_manifest_data):
    """Checks if the icons is a dictionary."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["icons"], dict)
    
def test_manifest_browser_action_is_dict(valid_manifest_data):
      """Checks if the browser_action is a dictionary."""
      json_str = json.dumps(valid_manifest_data)
      data = json.loads(json_str)
      assert isinstance(data["browser_action"], dict)

def test_manifest_content_scripts_is_list(valid_manifest_data):
    """Checks if content_scripts is a list."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["content_scripts"], list)

def test_manifest_content_scripts_matches_is_list(valid_manifest_data):
    """Checks if the content_scripts matches value is a list."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["content_scripts"][0]["matches"], list)
    
def test_manifest_content_scripts_js_is_list(valid_manifest_data):
    """Checks if the content_scripts js value is a list."""
    json_str = json.dumps(valid_manifest_data)
    data = json.loads(json_str)
    assert isinstance(data["content_scripts"][0]["js"], list)
```