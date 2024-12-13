```python
import pytest
import json

# Fixture to load the manifest.json content
@pytest.fixture
def manifest_data():
    """Provides test data for the manifest file."""
    with open('hypotez/src/webdriver/chrome/extentions/openai/manifest.v3.json', 'r') as f:
      return json.load(f)


def test_manifest_valid_structure(manifest_data):
    """Checks if the manifest has the necessary keys and values are correct types"""
    assert isinstance(manifest_data, dict), "The manifest should be a dictionary"
    assert "manifest_version" in manifest_data, "manifest_version is missing"
    assert "name" in manifest_data, "name is missing"
    assert "version" in manifest_data, "version is missing"
    assert "description" in manifest_data, "description is missing"
    assert "permissions" in manifest_data, "permissions is missing"
    assert "background" in manifest_data, "background is missing"
    assert "browser_action" in manifest_data, "browser_action is missing"
    assert "icons" in manifest_data, "icons is missing"
    assert "content_security_policy" in manifest_data, "content_security_policy is missing"
    
    assert isinstance(manifest_data["manifest_version"], int), "manifest_version should be an integer"
    assert isinstance(manifest_data["name"], str), "name should be a string"
    assert isinstance(manifest_data["version"], str), "version should be a string"
    assert isinstance(manifest_data["description"], str), "description should be a string"
    assert isinstance(manifest_data["permissions"], list), "permissions should be a list"
    assert isinstance(manifest_data["background"], dict), "background should be a dictionary"
    assert isinstance(manifest_data["browser_action"], dict), "browser_action should be a dictionary"
    assert isinstance(manifest_data["icons"], dict), "icons should be a dictionary"
    assert isinstance(manifest_data["content_security_policy"], str), "content_security_policy should be a string"



def test_manifest_version_is_3(manifest_data):
    """Checks if the manifest_version is set to 3"""
    assert manifest_data["manifest_version"] == 3, "manifest_version should be 3"


def test_manifest_name_is_correct(manifest_data):
    """Checks if the name matches the expected value"""
    assert manifest_data["name"] == "OpenAI Model Interface", "name should be 'OpenAI Model Interface'"


def test_manifest_version_format(manifest_data):
    """Checks if the version string follows a valid format (e.g., x.x)"""
    version = manifest_data["version"]
    parts = version.split(".")
    assert len(parts) == 2, "version should be in the format x.x"
    for part in parts:
      assert part.isdigit(), "version parts should be numeric"
      

def test_manifest_permissions_contains_activeTab(manifest_data):
    """Checks if 'activeTab' permission is present."""
    assert "activeTab" in manifest_data["permissions"], "permissions should contain 'activeTab'"

def test_manifest_background_scripts(manifest_data):
    """Checks if background scripts are correctly defined as an array."""
    assert "scripts" in manifest_data["background"], "scripts is missing under background"
    assert isinstance(manifest_data["background"]["scripts"], list), "background scripts should be an array"
    assert len(manifest_data["background"]["scripts"]) > 0, "background scripts should not be empty"
    assert "scripts/background.js" in manifest_data["background"]["scripts"], "scripts/background.js missing in background scripts"

def test_manifest_background_persistent(manifest_data):
    """Checks that the persistent background attribute is false"""
    assert "persistent" in manifest_data["background"], "persistent is missing in background"
    assert manifest_data["background"]["persistent"] == False, "persistent should be False"
    

def test_manifest_browser_action_popup(manifest_data):
    """Checks if the default_popup is correctly set."""
    assert "default_popup" in manifest_data["browser_action"], "default_popup missing in browser_action"
    assert manifest_data["browser_action"]["default_popup"] == "index.html", "default_popup should be 'index.html'"


def test_manifest_browser_action_icons(manifest_data):
    """Checks if default_icons are correctly defined."""
    assert "default_icon" in manifest_data["browser_action"], "default_icon missing in browser_action"
    assert "16" in manifest_data["browser_action"]["default_icon"], "16px icon is missing"
    assert "48" in manifest_data["browser_action"]["default_icon"], "48px icon is missing"
    assert "128" in manifest_data["browser_action"]["default_icon"], "128px icon is missing"
    
    
def test_manifest_icons_defined(manifest_data):
    """Checks if icons are correctly defined"""
    assert "16" in manifest_data["icons"], "16px icon is missing"
    assert "48" in manifest_data["icons"], "48px icon is missing"
    assert "128" in manifest_data["icons"], "128px icon is missing"

def test_manifest_content_security_policy(manifest_data):
  """Checks if the content_security_policy is properly defined"""
  csp = manifest_data["content_security_policy"]
  assert isinstance(csp, str), "content_security_policy should be a string"
  assert "script-src 'self'" in csp, "script-src 'self' is missing from content_security_policy"
  assert "object-src 'self'" in csp, "object-src 'self' is missing from content_security_policy"
```