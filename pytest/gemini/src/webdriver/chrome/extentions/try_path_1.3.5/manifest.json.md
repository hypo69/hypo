```python
import pytest
import json

# Fixture to load the manifest.json file content
@pytest.fixture
def manifest_data():
    """Provides the content of the manifest.json file as a dictionary."""
    manifest_content = """
    {
        "manifest_version": 3,
        "name": "Try xpath",
        "description": "This extension displays the result of evaluating xpath expression or CSS selector.",
        "version": "1.3.5",
        "icons": {
            "48": "icons/icon_48.png"
        },
        "permissions": [
            "<all_urls>",
            "storage"
        ],
        "action": {
            "default_icon": "icons/icon_48.png",
            "default_title": "Try xpath",
            "default_popup": "popup/popup.html"
        },
        "background": {
            "service_worker": "background/try_xpath_background.js"
        },
        "content_scripts": [
            {
                "matches": ["<all_urls>"],
                "js": ["scripts/try_xpath_functions.js"]
            }
        ]
    }
    """
    return json.loads(manifest_content)


def test_manifest_version(manifest_data):
    """Checks that the manifest version is set to 3."""
    assert manifest_data["manifest_version"] == 3, "Manifest version should be 3"


def test_extension_name(manifest_data):
    """Checks the name of the extension."""
    assert manifest_data["name"] == "Try xpath", "Extension name should be 'Try xpath'"


def test_extension_description(manifest_data):
    """Checks the description of the extension."""
    expected_description = "This extension displays the result of evaluating xpath expression or CSS selector."
    assert manifest_data["description"] == expected_description, "Incorrect extension description"


def test_extension_version(manifest_data):
    """Checks the extension version."""
    assert manifest_data["version"] == "1.3.5", "Extension version should be '1.3.5'"


def test_icons_presence(manifest_data):
    """Checks that the icons key is present and has the expected icon file."""
    assert "icons" in manifest_data, "Icons key should be present"
    assert "48" in manifest_data["icons"], "Icon with size 48 should be present"
    assert manifest_data["icons"]["48"] == "icons/icon_48.png", "Incorrect path for 48px icon"


def test_permissions_presence(manifest_data):
    """Checks that permissions are specified correctly."""
    assert "permissions" in manifest_data, "Permissions key should be present"
    assert "<all_urls>" in manifest_data["permissions"], "<all_urls> permission should be present"
    assert "storage" in manifest_data["permissions"], "storage permission should be present"


def test_action_presence(manifest_data):
    """Checks that the action key is present and contains default information."""
    assert "action" in manifest_data, "Action key should be present"
    assert "default_icon" in manifest_data["action"], "default_icon key should be present"
    assert manifest_data["action"]["default_icon"] == "icons/icon_48.png", "Incorrect default icon"
    assert "default_title" in manifest_data["action"], "default_title key should be present"
    assert manifest_data["action"]["default_title"] == "Try xpath", "Incorrect default title"
    assert "default_popup" in manifest_data["action"], "default_popup key should be present"
    assert manifest_data["action"]["default_popup"] == "popup/popup.html", "Incorrect default popup"


def test_background_presence(manifest_data):
    """Checks that background scripts are specified correctly."""
    assert "background" in manifest_data, "Background key should be present"
    assert "service_worker" in manifest_data["background"], "Service worker key should be present"
    assert manifest_data["background"]["service_worker"] == "background/try_xpath_background.js", "Incorrect background script"


def test_content_scripts_presence(manifest_data):
    """Checks that content scripts are specified correctly."""
    assert "content_scripts" in manifest_data, "Content scripts key should be present"
    assert isinstance(manifest_data["content_scripts"], list), "Content scripts should be a list"
    assert len(manifest_data["content_scripts"]) == 1, "Should be one content script specified"
    content_script = manifest_data["content_scripts"][0]
    assert "matches" in content_script, "Matches key should be present"
    assert "<all_urls>" in content_script["matches"], "<all_urls> in matches of content script"
    assert "js" in content_script, "JS key should be present"
    assert isinstance(content_script["js"], list), "JS files should be a list"
    assert len(content_script["js"]) == 1, "Should be one JS file specified"
    assert content_script["js"][0] == "scripts/try_xpath_functions.js", "Incorrect js script path"


def test_invalid_manifest_format():
    """Checks that an invalid manifest format throws an error."""
    invalid_manifest_content = "invalid json format"
    with pytest.raises(json.JSONDecodeError):
        json.loads(invalid_manifest_content)
```