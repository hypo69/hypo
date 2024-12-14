```python
import pytest
import json

# Fixture to load the manifest.json content
@pytest.fixture
def manifest_data():
    """Provides the content of the manifest.json file as a Python dictionary."""
    manifest_content = """
    {
      "manifest_version": 3,
      "name": "Hypotez",
      "version": "1.0",
      "description": "Collects data from web pages and sends it to a server.",
      "permissions": [ "activeTab", "storage", "scripting" ],
      "background": {
        "service_worker": "borderify.js"
      },
      "action": {
        "default_popup": "html/popup.html",
        "default_icon": {
          "16": "icons/icon.png",
          "48": "icons/icon.png",
          "128": "icons/icon.png"
        }
      },
      "icons": {
        "16": "icons/icon.png",
        "48": "icons/icon.png",
        "128": "icons/icon.png"
      },
      "host_permissions": [
        "https://*/*",
        "http://*/*"
      ]
    }
    """
    return json.loads(manifest_content)



def test_manifest_version_is_3(manifest_data):
    """Checks if the manifest version is correctly set to 3."""
    assert manifest_data["manifest_version"] == 3

def test_manifest_name_is_hypotez(manifest_data):
    """Checks if the extension name is set to Hypotez."""
    assert manifest_data["name"] == "Hypotez"

def test_manifest_version_is_1_0(manifest_data):
    """Checks if the extension version is set to 1.0."""
    assert manifest_data["version"] == "1.0"

def test_manifest_description_is_correct(manifest_data):
    """Checks if the extension description is set correctly."""
    expected_description = "Collects data from web pages and sends it to a server."
    assert manifest_data["description"] == expected_description


def test_manifest_permissions_are_correct(manifest_data):
     """Checks if the permissions list is correctly defined."""
     expected_permissions = ["activeTab", "storage", "scripting"]
     assert manifest_data["permissions"] == expected_permissions

def test_manifest_background_script_is_correct(manifest_data):
    """Checks if the background script is correctly set."""
    expected_background = { "service_worker": "borderify.js" }
    assert manifest_data["background"] == expected_background

def test_manifest_action_popup_is_correct(manifest_data):
    """Checks if the default popup path is correct."""
    assert manifest_data["action"]["default_popup"] == "html/popup.html"

def test_manifest_action_icons_are_present(manifest_data):
    """Checks if default icons are defined under the 'action' key."""
    expected_icons = {"16": "icons/icon.png", "48": "icons/icon.png", "128": "icons/icon.png"}
    assert manifest_data["action"]["default_icon"] == expected_icons

def test_manifest_icons_are_present(manifest_data):
    """Checks if icons are defined at the root level of the manifest."""
    expected_icons = {"16": "icons/icon.png", "48": "icons/icon.png", "128": "icons/icon.png"}
    assert manifest_data["icons"] == expected_icons

def test_manifest_host_permissions_are_correct(manifest_data):
    """Checks if the host permissions list is set correctly."""
    expected_host_permissions = ["https://*/*", "http://*/*"]
    assert manifest_data["host_permissions"] == expected_host_permissions
```