```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_locators():
    """Loads the login locators JSON data."""
    with open("hypotez/src/endpoints/advertisement/facebook/locators/login.json", "r") as f:
        return json.load(f)

# Test cases for the email locator
def test_email_locator_valid_data(login_locators):
    """Checks if the email locator has the correct structure and values."""
    email_locator = login_locators.get("email")
    assert email_locator is not None
    assert email_locator["attribute"] is None
    assert email_locator["by"] == "XPATH"
    assert email_locator["selector"] == "//input[@name = 'email']"
    assert email_locator["if_list"] == "first"
    assert email_locator["use_mouse"] == False
    assert email_locator["timeout"] == 0
    assert email_locator["timeout_for_event"] == "presence_of_element_located"
    assert email_locator["event"] == "click()"
    assert email_locator["mandatory"] == True
    assert email_locator["locator_description"] == "user email or phone"

def test_email_locator_missing_keys(login_locators):
    """Checks behavior if keys are missing for email locator."""
    email_locator = login_locators.get("email")
    
    #Test for missing key using pop operation 
    email_locator_missing_selector = email_locator.copy()
    email_locator_missing_selector.pop("selector")
    
    email_locator_missing_by = email_locator.copy()
    email_locator_missing_by.pop("by")

    with pytest.raises(KeyError):
         email_locator_missing_selector["selector"]

    with pytest.raises(KeyError):
         email_locator_missing_by["by"]


# Test cases for the password locator
def test_password_locator_valid_data(login_locators):
    """Checks if the password locator has the correct structure and values."""
    password_locator = login_locators.get("password")
    assert password_locator is not None
    assert password_locator["attribute"] is None
    assert password_locator["by"] == "XPATH"
    assert password_locator["selector"] == "//input[@name = 'pass']"
    assert password_locator["if_list"] == "first"
    assert password_locator["use_mouse"] == [False, False]
    assert password_locator["timeout"] == 0
    assert password_locator["timeout_for_event"] == "presence_of_element_located"
    assert password_locator["event"] == "click()"
    assert password_locator["mandatory"] == [True, True]
    assert password_locator["locator_description"] == "user email or phone"

def test_password_locator_missing_keys(login_locators):
    """Checks behavior if keys are missing for password locator."""
    password_locator = login_locators.get("password")
    
    #Test for missing key using pop operation 
    password_locator_missing_selector = password_locator.copy()
    password_locator_missing_selector.pop("selector")
    
    password_locator_missing_by = password_locator.copy()
    password_locator_missing_by.pop("by")

    with pytest.raises(KeyError):
         password_locator_missing_selector["selector"]

    with pytest.raises(KeyError):
         password_locator_missing_by["by"]
    

# Test cases for the button locator
def test_button_locator_valid_data(login_locators):
    """Checks if the button locator has the correct structure and values."""
    button_locator = login_locators.get("button")
    assert button_locator is not None
    assert button_locator["attribute"] is None
    assert button_locator["by"] == "XPATH"
    assert button_locator["selector"] == "//button[@name = 'login']"
    assert button_locator["if_list"] == "first"
    assert button_locator["use_mouse"] == False
    assert button_locator["timeout"] == 0
    assert button_locator["timeout_for_event"] == "presence_of_element_located"
    assert button_locator["event"] == "click()"
    assert button_locator["mandatory"] == True
    assert button_locator["locator_description"] == "send button"


def test_button_locator_missing_keys(login_locators):
    """Checks behavior if keys are missing for button locator."""
    button_locator = login_locators.get("button")
    
    #Test for missing key using pop operation 
    button_locator_missing_selector = button_locator.copy()
    button_locator_missing_selector.pop("selector")
    
    button_locator_missing_by = button_locator.copy()
    button_locator_missing_by.pop("by")

    with pytest.raises(KeyError):
         button_locator_missing_selector["selector"]

    with pytest.raises(KeyError):
         button_locator_missing_by["by"]

def test_locator_missing_field(login_locators):
    """Checks the scenario when a locator is completely missing."""
    assert login_locators.get("non_existing_locator") is None
```