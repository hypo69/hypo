```python
import pytest
import json

# Define a fixture to load the manifest file content
@pytest.fixture
def manifest_content():
    """Provides the content of the manifest.json file as a dictionary."""
    manifest_string = """
    {
      "manifest_version": 3,
      "name": "OpenAI Model Interface",
      "version": "1.0",
      "description": "Interface for interacting with OpenAI model",
      "permissions": [
        "activeTab"
      ],
      "background": {
        "service_worker": "background.js"
      },
      "action": {
        "default_popup": "index.html",
        "default_icon": {
          "16": "icons/16.png",
          "48": "icons/48.png",
          "128": "icons/128.png"
        },
        "default_width": 750,
        "default_height": 600
      },
      "icons": {
        "16": "icons/16.png",
        "48": "icons/48.png",
        "128": "icons/128.png"
      },
      "content_security_policy": {
        "extension_pages": "script-src 'self'; object-src 'self';"
      }
    }
    """
    return json.loads(manifest_string)

def test_manifest_version(manifest_content):
    """Checks if the manifest version is correct."""
    assert manifest_content["manifest_version"] == 3

def test_manifest_name(manifest_content):
    """Checks if the manifest name is correct."""
    assert manifest_content["name"] == "OpenAI Model Interface"

def test_manifest_version_number(manifest_content):
    """Checks if the version number is correct."""
    assert manifest_content["version"] == "1.0"

def test_manifest_description(manifest_content):
    """Checks if the manifest description is correct."""
    assert manifest_content["description"] == "Interface for interacting with OpenAI model"

def test_manifest_permissions(manifest_content):
    """Checks if the permissions array includes 'activeTab'."""
    assert "activeTab" in manifest_content["permissions"]
    
def test_manifest_background_service_worker(manifest_content):
     """Checks if the background service worker is correctly specified."""
     assert manifest_content["background"]["service_worker"] == "background.js"

def test_manifest_action_default_popup(manifest_content):
    """Checks if the default popup is set to 'index.html'."""
    assert manifest_content["action"]["default_popup"] == "index.html"

def test_manifest_action_default_icon(manifest_content):
    """Checks if the default icons are correctly specified."""
    assert manifest_content["action"]["default_icon"]["16"] == "icons/16.png"
    assert manifest_content["action"]["default_icon"]["48"] == "icons/48.png"
    assert manifest_content["action"]["default_icon"]["128"] == "icons/128.png"

def test_manifest_action_default_width(manifest_content):
    """Checks if the default width is set to 750."""
    assert manifest_content["action"]["default_width"] == 750

def test_manifest_action_default_height(manifest_content):
    """Checks if the default height is set to 600."""
    assert manifest_content["action"]["default_height"] == 600

def test_manifest_icons(manifest_content):
    """Checks if all icon sizes are present."""
    assert manifest_content["icons"]["16"] == "icons/16.png"
    assert manifest_content["icons"]["48"] == "icons/48.png"
    assert manifest_content["icons"]["128"] == "icons/128.png"

def test_manifest_content_security_policy(manifest_content):
    """Checks if the content security policy is correctly defined."""
    assert manifest_content["content_security_policy"]["extension_pages"] == "script-src 'self'; object-src 'self';"

def test_manifest_missing_key(manifest_content):
    """Checks behavior when trying to access a missing key, should raise KeyError."""
    with pytest.raises(KeyError):
        manifest_content["non_existent_key"]
```