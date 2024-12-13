```python
import pytest
import json

# Fixture for loading the manifest.json content
@pytest.fixture
def manifest_data():
    """Provides test data for the manifest.json file."""
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
    """Checks if manifest_version is set to 3."""
    assert manifest_data["manifest_version"] == 3, "manifest_version should be 3"


def test_manifest_name_is_hypotez(manifest_data):
    """Checks if the extension name is set to Hypotez."""
    assert manifest_data["name"] == "Hypotez", "Extension name should be Hypotez"


def test_manifest_version_is_1_0(manifest_data):
    """Checks if the extension version is set to 1.0."""
    assert manifest_data["version"] == "1.0", "Extension version should be 1.0"


def test_manifest_has_description(manifest_data):
    """Checks if a description is present."""
    assert "description" in manifest_data, "Description should be present"
    assert manifest_data["description"] == "Collects data from web pages and sends it to a server.", "Description is not as expected"


def test_manifest_permissions_are_correct(manifest_data):
    """Checks if required permissions are present."""
    expected_permissions = ["activeTab", "storage", "scripting"]
    assert "permissions" in manifest_data, "Permissions key should be present"
    assert manifest_data["permissions"] == expected_permissions, "Permissions are not correct"

def test_manifest_background_service_worker(manifest_data):
    """Checks if the background service worker is configured correctly."""
    assert "background" in manifest_data, "Background key should be present"
    assert manifest_data["background"]["service_worker"] == "borderify.js", "Service worker should be borderify.js"

def test_manifest_action_default_popup(manifest_data):
    """Checks if default popup configuration is correct"""
    assert "action" in manifest_data, "Action key should be present"
    assert manifest_data["action"]["default_popup"] == "html/popup.html", "Default popup should be html/popup.html"

def test_manifest_action_default_icons(manifest_data):
    """Checks if the default icons sizes are set"""
    assert "action" in manifest_data, "Action key should be present"
    assert "default_icon" in manifest_data["action"], "Default icon key should be present"
    assert "16" in manifest_data["action"]["default_icon"], "Icon size 16 should be present"
    assert "48" in manifest_data["action"]["default_icon"], "Icon size 48 should be present"
    assert "128" in manifest_data["action"]["default_icon"], "Icon size 128 should be present"

def test_manifest_icons_are_present(manifest_data):
    """Checks if icon sizes are set"""
    assert "icons" in manifest_data, "Icons key should be present"
    assert "16" in manifest_data["icons"], "Icon size 16 should be present"
    assert "48" in manifest_data["icons"], "Icon size 48 should be present"
    assert "128" in manifest_data["icons"], "Icon size 128 should be present"


def test_manifest_host_permissions_are_correct(manifest_data):
    """Checks if correct host permissions are set."""
    expected_host_permissions = ["https://*/*", "http://*/*"]
    assert "host_permissions" in manifest_data, "Host permissions key should be present"
    assert manifest_data["host_permissions"] == expected_host_permissions, "Host permissions are not correct"


def test_manifest_invalid_version():
    """Checks if the manifest version can be invalid"""
    manifest_content = """
        {
          "manifest_version": 2,
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
    manifest_data = json.loads(manifest_content)
    with pytest.raises(AssertionError) as excinfo:
        test_manifest_version_is_3(manifest_data)
    assert str(excinfo.value) == "manifest_version should be 3"


def test_manifest_missing_permissions():
    """Checks if the manifest without permissions is parsed correctly"""
    manifest_content = """
        {
          "manifest_version": 3,
          "name": "Hypotez",
          "version": "1.0",
          "description": "Collects data from web pages and sends it to a server.",
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
    manifest_data = json.loads(manifest_content)
    with pytest.raises(AssertionError) as excinfo:
        test_manifest_permissions_are_correct(manifest_data)
    assert str(excinfo.value) == "Permissions key should be present"
```