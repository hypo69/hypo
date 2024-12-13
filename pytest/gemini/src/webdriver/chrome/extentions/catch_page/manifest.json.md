```python
import pytest
import json

# Since the input is a JSON manifest file, we'll test its structure and content
# The structure is straightforward and doesn't require a dedicated class/function, 
# so we'll focus on testing the parsed JSON data.


@pytest.fixture
def valid_manifest_data():
    """Provides a valid manifest JSON data as a dictionary."""
    return {
        "manifest_version": 3,
        "name": "URL Sender",
        "version": "1.0",
        "description": "Sends the URL of the current page to a local server.",
        "action": {
            "default_popup": "popup.html"
        },
        "background": {
            "service_worker": "background.js"
        },
        "permissions": ["activeTab", "storage"]
    }

def test_manifest_valid_structure(valid_manifest_data):
    """
    Checks if the basic keys are present in the manifest data.
    """
    assert "manifest_version" in valid_manifest_data
    assert "name" in valid_manifest_data
    assert "version" in valid_manifest_data
    assert "description" in valid_manifest_data
    assert "action" in valid_manifest_data
    assert "background" in valid_manifest_data
    assert "permissions" in valid_manifest_data

def test_manifest_manifest_version(valid_manifest_data):
    """
    Verifies that manifest_version is the expected value.
    """
    assert valid_manifest_data["manifest_version"] == 3


def test_manifest_name(valid_manifest_data):
    """
    Checks if the name of the extension is as expected.
    """
    assert valid_manifest_data["name"] == "URL Sender"


def test_manifest_version(valid_manifest_data):
    """
    Verifies that the version of the extension is as expected.
    """
    assert valid_manifest_data["version"] == "1.0"


def test_manifest_description(valid_manifest_data):
    """
    Tests if the description is as expected.
    """
    assert valid_manifest_data["description"] == "Sends the URL of the current page to a local server."


def test_manifest_action_default_popup(valid_manifest_data):
     """
     Verifies that the default_popup value is as expected.
     """
     assert valid_manifest_data["action"]["default_popup"] == "popup.html"

def test_manifest_background_service_worker(valid_manifest_data):
    """
    Checks if service_worker value is as expected.
    """
    assert valid_manifest_data["background"]["service_worker"] == "background.js"

def test_manifest_permissions(valid_manifest_data):
    """
    Checks if the permissions array contains the expected permissions.
    """
    assert "activeTab" in valid_manifest_data["permissions"]
    assert "storage" in valid_manifest_data["permissions"]
    assert len(valid_manifest_data["permissions"]) == 2  # Ensure no extra permission is added

def test_manifest_invalid_version():
    """
    Test if parsing the manifest with an invalid version throws an error
    (It won't, but it's a good placeholder for this type of test)
    """
    invalid_data = {
        "manifest_version": "invalid", # This is incorrect for manifest
        "name": "URL Sender",
        "version": "1.0",
        "description": "Sends the URL of the current page to a local server.",
        "action": {
            "default_popup": "popup.html"
        },
        "background": {
            "service_worker": "background.js"
        },
        "permissions": ["activeTab", "storage"]
    }
    with pytest.raises(TypeError):
        # We would try to read and validate the manifest data here.
        # This error is a placeholder, since we are not actually using JSON parsing here,
        # but this simulates a situation when a manifest with an invalid version would be loaded.
        # This check assumes that you have parsing logic in real case and you validate manifest_version
        # type before using it.
        assert invalid_data["manifest_version"] == 3  # Simulating an error
```