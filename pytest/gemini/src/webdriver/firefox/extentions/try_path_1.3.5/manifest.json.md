```python
import pytest
import json

# Fixture to load the manifest.json content
@pytest.fixture
def manifest_data():
    """Provides test data from the manifest.json file."""
    # For testing purposes, we'll use the provided JSON as a string instead of loading from a file.
    manifest_json = """
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
    return json.loads(manifest_json)


def test_manifest_name(manifest_data):
    """Checks if the 'name' field is correct."""
    assert manifest_data["name"] == "Try xpath"

def test_manifest_description(manifest_data):
    """Checks if the 'description' field is correct."""
    assert manifest_data["description"] == "This add-on displays the result of evaluating xpath expression or CSS selector."

def test_manifest_manifest_version(manifest_data):
    """Checks if the 'manifest_version' is correct."""
    assert manifest_data["manifest_version"] == 2

def test_manifest_version(manifest_data):
    """Checks if the 'version' field is correct."""
    assert manifest_data["version"] == "1.3.5"

def test_manifest_icons(manifest_data):
    """Checks if the 'icons' field is correct."""
    assert manifest_data["icons"] == {"48": "icons/icon_48.png"}

def test_manifest_applications_gecko_id(manifest_data):
    """Checks if the gecko 'id' within applications is correct."""
    assert manifest_data["applications"]["gecko"]["id"] == "{ba6bb880-bcbe-4792-a020-fcfab8d67027}"

def test_manifest_applications_gecko_strict_min_version(manifest_data):
    """Checks if the gecko 'strict_min_version' within applications is correct."""
    assert manifest_data["applications"]["gecko"]["strict_min_version"] == "53.0"

def test_manifest_permissions(manifest_data):
    """Checks if the 'permissions' field is correct."""
    assert manifest_data["permissions"] == ["<all_urls>", "storage"]

def test_manifest_background_scripts(manifest_data):
    """Checks if the 'scripts' within 'background' is correct."""
    assert manifest_data["background"]["scripts"] == ["scripts/try_xpath_functions.js",
                                                     "background/try_xpath_background.js"]

def test_manifest_browser_action_default_icon(manifest_data):
    """Checks if the 'default_icon' within 'browser_action' is correct."""
    assert manifest_data["browser_action"]["default_icon"] == "icons/icon_48.png"

def test_manifest_browser_action_default_title(manifest_data):
    """Checks if the 'default_title' within 'browser_action' is correct."""
    assert manifest_data["browser_action"]["default_title"] == "Try xpath"

def test_manifest_browser_action_default_popup(manifest_data):
    """Checks if the 'default_popup' within 'browser_action' is correct."""
    assert manifest_data["browser_action"]["default_popup"] == "popup/popup.html"

def test_manifest_web_accessible_resources(manifest_data):
    """Checks if the 'web_accessible_resources' is correct (should be an empty list)."""
    assert manifest_data["web_accessible_resources"] == []

def test_manifest_content_scripts(manifest_data):
    """Checks if the 'content_scripts' is correct (should be an empty list)."""
    assert manifest_data["content_scripts"] == []

def test_manifest_options_ui_page(manifest_data):
    """Checks if the 'page' within 'options_ui' is correct."""
    assert manifest_data["options_ui"]["page"] == "/pages/options.html"
```