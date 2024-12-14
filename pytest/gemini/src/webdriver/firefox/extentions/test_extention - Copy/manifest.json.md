```python
import pytest
import json

# Assuming the manifest.json content is read into a variable,
# or a function is used to load it. For the sake of testing, we directly use
# the provided JSON content string.

MANIFEST_JSON_STR = """
{
  "manifest_version": 2,
  "name": "Borderify",
  "version": "1.0",

  "description": "Adds a red border to all webpages matching mozilla.org.",

  "icons": {
    "48": "icons/icon.png"
  },

  "content_scripts": [
    {
      "matches": [ "<all_urls>" ],
      "js": [ "borderify.js" ]
    }
  ]
}
"""

@pytest.fixture
def manifest_data():
    """Provides parsed JSON data of manifest.json."""
    return json.loads(MANIFEST_JSON_STR)

def test_manifest_version(manifest_data):
    """Checks if the manifest version is 2."""
    assert manifest_data["manifest_version"] == 2

def test_manifest_name(manifest_data):
    """Checks if the extension name is 'Borderify'."""
    assert manifest_data["name"] == "Borderify"

def test_manifest_version_string(manifest_data):
    """Checks if the extension version is '1.0'."""
    assert manifest_data["version"] == "1.0"

def test_manifest_description(manifest_data):
    """Checks if the description is as expected."""
    expected_description = "Adds a red border to all webpages matching mozilla.org."
    assert manifest_data["description"] == expected_description

def test_manifest_icons(manifest_data):
    """Checks if the icons field is correctly defined."""
    assert "48" in manifest_data["icons"]
    assert manifest_data["icons"]["48"] == "icons/icon.png"

def test_manifest_content_scripts_present(manifest_data):
    """Checks if content_scripts are defined and is a list."""
    assert "content_scripts" in manifest_data
    assert isinstance(manifest_data["content_scripts"], list)

def test_manifest_content_scripts_not_empty(manifest_data):
    """Checks if the content_scripts list is not empty."""
    assert len(manifest_data["content_scripts"]) > 0

def test_manifest_content_scripts_matches(manifest_data):
    """Checks if 'matches' key is correctly defined in content_scripts."""
    content_script = manifest_data["content_scripts"][0]
    assert "matches" in content_script
    assert content_script["matches"] == ["<all_urls>"]

def test_manifest_content_scripts_js(manifest_data):
    """Checks if 'js' key is correctly defined in content_scripts."""
    content_script = manifest_data["content_scripts"][0]
    assert "js" in content_script
    assert content_script["js"] == ["borderify.js"]

def test_manifest_extra_key(manifest_data):
    """Checks if adding an extra key raises no error, though we will not enforce checking for an extra key, just demonstration."""
    manifest_data["extra_field"] = "extra value"
    assert "extra_field" in manifest_data
    assert manifest_data["extra_field"] == "extra value"


def test_manifest_missing_key():
    """Tests with a manifest that has a missing key, it would not parse to json but it is good practice to test"""
    manifest_str_missing_key = """{
        "manifest_version": 2,
        "name": "Borderify",
        "version": "1.0"
    }
    """
    with pytest.raises(KeyError) :
        data = json.loads(manifest_str_missing_key)
        assert data["description"]


def test_manifest_empty_input():
    """Tests with an empty input that we handle the json error."""
    empty_str = ""
    with pytest.raises(json.JSONDecodeError):
         json.loads(empty_str)


def test_manifest_invalid_json_format():
   """Tests with an invalid JSON format to ensure it handle the JSONDecodeError."""
   invalid_json_str = "{manifest_version: 2,}"
   with pytest.raises(json.JSONDecodeError):
       json.loads(invalid_json_str)
```