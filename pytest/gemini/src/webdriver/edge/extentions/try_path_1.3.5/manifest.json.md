```python
import pytest
import json

# Fixture for loading the manifest.json content
@pytest.fixture
def manifest_data():
    """Provides the manifest.json data as a dictionary."""
    manifest_content = """
    {
        "name": "Try xpath",
        "description": "This add-on displays the result of evaluating xpath expression or CSS selector.",
        "manifest_version": 2,
        "version": "1.3.5",
        "icons": {
            "48": "icons/icon_48.png"
        },
    
        "applications": {
            "gecko": {
                "id": "{ba6bb880-bcbe-4792-a020-fcfab8d67027}",
                "strict_min_version": "53.0"
            }
        },
    
        "permissions": [
            "<all_urls>",
            "storage"
        ],
    
        "background": {
            "scripts": ["scripts/try_xpath_functions.js",
                        "background/try_xpath_background.js"]
        },
    
        "browser_action": {
            "default_icon": "icons/icon_48.png",
            "default_title": "Try xpath",
            "default_popup": "popup/popup.html"
        },
    
        "web_accessible_resources": [
        ],
    
        "content_scripts": [
        ],
    
        "options_ui": {
            "page": "/pages/options.html"
        }
    }
    """
    return json.loads(manifest_content)

def test_manifest_name(manifest_data):
    """Checks if the name field is correct"""
    assert manifest_data["name"] == "Try xpath"

def test_manifest_description(manifest_data):
    """Checks if the description field is correct."""
    assert manifest_data["description"] == "This add-on displays the result of evaluating xpath expression or CSS selector."

def test_manifest_version(manifest_data):
    """Checks if the manifest_version field is correct."""
    assert manifest_data["manifest_version"] == 2

def test_manifest_addon_version(manifest_data):
    """Checks if the addon version field is correct."""
    assert manifest_data["version"] == "1.3.5"

def test_manifest_icons(manifest_data):
    """Checks if the icons field is correct."""
    assert manifest_data["icons"] == {"48": "icons/icon_48.png"}

def test_manifest_gecko_app_id(manifest_data):
    """Checks if gecko application id is correct."""
    assert manifest_data["applications"]["gecko"]["id"] == "{ba6bb880-bcbe-4792-a020-fcfab8d67027}"

def test_manifest_gecko_strict_min_version(manifest_data):
    """Checks if gecko strict min version is correct"""
    assert manifest_data["applications"]["gecko"]["strict_min_version"] == "53.0"

def test_manifest_permissions(manifest_data):
    """Checks if permissions list is correct."""
    assert manifest_data["permissions"] == ["<all_urls>", "storage"]

def test_manifest_background_scripts(manifest_data):
    """Checks if background scripts are correct"""
    assert manifest_data["background"]["scripts"] == ["scripts/try_xpath_functions.js", "background/try_xpath_background.js"]

def test_manifest_browser_action_icon(manifest_data):
    """Checks if browser action default icon is correct."""
    assert manifest_data["browser_action"]["default_icon"] == "icons/icon_48.png"

def test_manifest_browser_action_title(manifest_data):
     """Checks if browser action default title is correct."""
     assert manifest_data["browser_action"]["default_title"] == "Try xpath"

def test_manifest_browser_action_popup(manifest_data):
    """Checks if browser action default popup is correct."""
    assert manifest_data["browser_action"]["default_popup"] == "popup/popup.html"

def test_manifest_web_accessible_resources(manifest_data):
    """Checks if web accessible resources is an empty list"""
    assert manifest_data["web_accessible_resources"] == []

def test_manifest_content_scripts(manifest_data):
    """Checks if content scripts is an empty list"""
    assert manifest_data["content_scripts"] == []

def test_manifest_options_ui_page(manifest_data):
    """Checks if the options page path is correct."""
    assert manifest_data["options_ui"]["page"] == "/pages/options.html"
    
def test_manifest_missing_key():
    """Checks handling of missing key in manifest data"""
    manifest_content_missing_key = """
    {
        "name": "Try xpath",
        "manifest_version": 2,
        "version": "1.3.5",
        "icons": {
            "48": "icons/icon_48.png"
        }
    }
    """
    manifest_data_missing_key = json.loads(manifest_content_missing_key)
    with pytest.raises(KeyError):
        _ = manifest_data_missing_key["description"]
        
def test_manifest_invalid_json():
    """Checks handling of invalid json data"""
    manifest_content_invalid = """
    {
        "name": "Try xpath",
        "manifest_version": 2,
        "version": "1.3.5"
         "icons": {
            "48": "icons/icon_48.png"
        }
    }
    """
    with pytest.raises(json.JSONDecodeError):
        _ = json.loads(manifest_content_invalid)
```