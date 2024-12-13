```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def dornet_login_data():
    """Loads the dornet login JSON data for testing."""
    with open("hypotez/src/scenario/json/dornet_login.json", "r") as file:
        return json.load(file)

def test_dornet_login_data_structure(dornet_login_data):
    """
    Test if the dornet login data has the expected keys.
    This ensures the basic structure of the JSON is correct.
    """
    assert "email" in dornet_login_data
    assert "password" in dornet_login_data
    assert "open_login_dialog_locator" in dornet_login_data
    assert "email_locator" in dornet_login_data
    assert "password_locator" in dornet_login_data
    assert "loginbutton_locator" in dornet_login_data

def test_dornet_login_data_email_valid(dornet_login_data):
     """
     Test if the email field is a string and is not empty.
     """
     assert isinstance(dornet_login_data["email"], str)
     assert dornet_login_data["email"] != ""

def test_dornet_login_data_password_valid(dornet_login_data):
     """
     Test if the password field is a string and is not empty.
     """
     assert isinstance(dornet_login_data["password"], str)
     assert dornet_login_data["password"] != ""

def test_dornet_login_open_login_dialog_locator_structure(dornet_login_data):
    """
    Test the structure of the open_login_dialog_locator.
    It should have 'by' and 'selector' keys with string values.
    """
    locator = dornet_login_data["open_login_dialog_locator"]
    assert "by" in locator
    assert "selector" in locator
    assert isinstance(locator["by"], str)
    assert isinstance(locator["selector"], str)

def test_dornet_login_email_locator_structure(dornet_login_data):
    """
    Test the structure of the email_locator.
    It should have 'by' and 'selector' keys with string values.
    """
    locator = dornet_login_data["email_locator"]
    assert "by" in locator
    assert "selector" in locator
    assert isinstance(locator["by"], str)
    assert isinstance(locator["selector"], str)
    

def test_dornet_login_password_locator_structure(dornet_login_data):
    """
    Test the structure of the password_locator.
    It should have 'by' and 'selector' keys with string values.
    """
    locator = dornet_login_data["password_locator"]
    assert "by" in locator
    assert "selector" in locator
    assert isinstance(locator["by"], str)
    assert isinstance(locator["selector"], str)

def test_dornet_login_loginbutton_locator_structure(dornet_login_data):
     """
     Test the structure of the loginbutton_locator.
     It should have 'by' and 'selector' keys with string values.
     """
     locator = dornet_login_data["loginbutton_locator"]
     assert "by" in locator
     assert "selector" in locator
     assert isinstance(locator["by"], str)
     assert isinstance(locator["selector"], str)

def test_dornet_login_locator_types(dornet_login_data):
    """
    Test if the locator "by" values are all strings, and they have a valid structure.
    """
    locators = [
        dornet_login_data["open_login_dialog_locator"],
        dornet_login_data["email_locator"],
        dornet_login_data["password_locator"],
        dornet_login_data["loginbutton_locator"]
    ]
    for locator in locators:
        assert isinstance(locator["by"], str)
        assert locator["by"] in ["css selector","xpath","id","class","name","tag name"]
        
def test_dornet_login_selector_not_empty(dornet_login_data):
    """
    Test that selector fields are not empty for all locators.
    """
    locators = [
        dornet_login_data["open_login_dialog_locator"],
        dornet_login_data["email_locator"],
        dornet_login_data["password_locator"],
        dornet_login_data["loginbutton_locator"]
    ]
    for locator in locators:
         assert isinstance(locator["selector"], str)
         assert locator["selector"] != ""
```