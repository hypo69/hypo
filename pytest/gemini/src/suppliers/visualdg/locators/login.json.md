```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_locators():
    """Loads the login locators from the JSON file."""
    with open("hypotez/src/suppliers/visualdg/locators/login.json", "r") as f:
        return json.load(f)

# Test for the open_login_inputs locator
def test_open_login_inputs_valid(login_locators):
    """Checks the 'open_login_inputs' locator has the correct values."""
    locator = login_locators["login"]["open_login_inputs"]
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[@id='nav-link-accountList-nav-line-1']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_open_login_inputs_invalid_key(login_locators):
    """Checks that accessing a non-existent key raises KeyError for 'open_login_inputs'."""
    locator = login_locators["login"]["open_login_inputs"]
    with pytest.raises(KeyError):
         locator["invalid_key"]


# Test for the email_input locator
def test_email_input_valid(login_locators):
    """Checks the 'email_input' locator has the correct values."""
    locator = login_locators["login"]["email_input"]
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='ap_email']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "send_keys('972547519449')"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_email_input_invalid_key(login_locators):
    """Checks that accessing a non-existent key raises KeyError for 'email_input'."""
    locator = login_locators["login"]["email_input"]
    with pytest.raises(KeyError):
         locator["invalid_key"]

# Test for the continue_button locator
def test_continue_button_valid(login_locators):
    """Checks the 'continue_button' locator has the correct values."""
    locator = login_locators["login"]["continue_button"]
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='continue']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_continue_button_invalid_key(login_locators):
    """Checks that accessing a non-existent key raises KeyError for 'continue_button'."""
    locator = login_locators["login"]["continue_button"]
    with pytest.raises(KeyError):
         locator["invalid_key"]

# Test for the password_input locator
def test_password_input_valid(login_locators):
    """Checks the 'password_input' locator has the correct values."""
    locator = login_locators["login"]["password_input"]
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='ap_password']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "send_keys('52UldxjzWGpdEQxWaNMY')"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_password_input_invalid_key(login_locators):
    """Checks that accessing a non-existent key raises KeyError for 'password_input'."""
    locator = login_locators["login"]["password_input"]
    with pytest.raises(KeyError):
         locator["invalid_key"]


# Test for the keep_signed_in_checkbox locator
def test_keep_signed_in_checkbox_valid(login_locators):
    """Checks the 'keep_signed_in_checkbox' locator has the correct values."""
    locator = login_locators["login"]["keep_signed_in_checkbox"]
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@name='rememberMe']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_keep_signed_in_checkbox_invalid_key(login_locators):
    """Checks that accessing a non-existent key raises KeyError for 'keep_signed_in_checkbox'."""
    locator = login_locators["login"]["keep_signed_in_checkbox"]
    with pytest.raises(KeyError):
         locator["invalid_key"]

# Test for the success_login_button locator
def test_success_login_button_valid(login_locators):
    """Checks the 'success_login_button' locator has the correct values."""
    locator = login_locators["login"]["success_login_button"]
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='signInSubmit']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_success_login_button_invalid_key(login_locators):
    """Checks that accessing a non-existent key raises KeyError for 'success_login_button'."""
    locator = login_locators["login"]["success_login_button"]
    with pytest.raises(KeyError):
         locator["invalid_key"]
# Test for the structure of the JSON file
def test_login_structure(login_locators):
     """Checks that the JSON file has the expected structure."""
     assert "login" in login_locators
     assert isinstance(login_locators["login"], dict)
     assert "open_login_inputs" in login_locators["login"]
     assert "email_input" in login_locators["login"]
     assert "continue_button" in login_locators["login"]
     assert "password_input" in login_locators["login"]
     assert "keep_signed_in_checkbox" in login_locators["login"]
     assert "success_login_button" in login_locators["login"]
```