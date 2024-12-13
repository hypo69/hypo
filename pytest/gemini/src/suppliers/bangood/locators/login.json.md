```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_locators():
    """Loads the login locators from the JSON file."""
    file_path = "hypotez/src/suppliers/bangood/locators/login.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test for the 'open_login_inputs' locator
def test_open_login_inputs_valid_data(login_locators):
    """Checks if the 'open_login_inputs' locator has the expected structure and values."""
    locator = login_locators["login"]["open_login_inputs"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[@id='nav-link-accountList-nav-line-1']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

# Test for the 'email_input' locator
def test_email_input_valid_data(login_locators):
    """Checks if the 'email_input' locator has the expected structure and values."""
    locator = login_locators["login"]["email_input"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='ap_email']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "send_keys('972547519449')"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None
    
# Test for the 'continue_button' locator
def test_continue_button_valid_data(login_locators):
    """Checks if the 'continue_button' locator has the expected structure and values."""
    locator = login_locators["login"]["continue_button"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='continue']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

# Test for the 'password_input' locator
def test_password_input_valid_data(login_locators):
    """Checks if the 'password_input' locator has the expected structure and values."""
    locator = login_locators["login"]["password_input"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='ap_password']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "send_keys('52UldxjzWGpdEQxWaNMY')"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

# Test for the 'keep_signed_in_checkbox' locator
def test_keep_signed_in_checkbox_valid_data(login_locators):
    """Checks if the 'keep_signed_in_checkbox' locator has the expected structure and values."""
    locator = login_locators["login"]["keep_signed_in_checkbox"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@name='rememberMe']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

# Test for the 'success_login_button' locator
def test_success_login_button_valid_data(login_locators):
    """Checks if the 'success_login_button' locator has the expected structure and values."""
    locator = login_locators["login"]["success_login_button"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//input[@id='signInSubmit']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_login_locator_structure(login_locators):
    """Checks if the main login key and its inner keys exist in JSON"""
    assert "login" in login_locators
    assert "open_login_inputs" in login_locators["login"]
    assert "email_input" in login_locators["login"]
    assert "continue_button" in login_locators["login"]
    assert "password_input" in login_locators["login"]
    assert "keep_signed_in_checkbox" in login_locators["login"]
    assert "success_login_button" in login_locators["login"]

# Test for invalid data type for timeout 
def test_timeout_invalid_data_type(login_locators):
    """Checks if the timeout value is an integer"""
    for key,value in login_locators["login"].items():
        assert isinstance(value["timeout"],int)

# Test for invalid data type for mandatory
def test_mandatory_invalid_data_type(login_locators):
    """Checks if the mandatory value is a boolean"""
    for key,value in login_locators["login"].items():
        assert isinstance(value["mandatory"],bool)

# Test for invalid data type for if_list
def test_if_list_invalid_data_type(login_locators):
    """Checks if the if_list value is a string"""
    for key,value in login_locators["login"].items():
      assert isinstance(value["if_list"],str)

# Test for invalid data type for use_mouse
def test_use_mouse_invalid_data_type(login_locators):
    """Checks if the use_mouse value is a boolean"""
    for key,value in login_locators["login"].items():
       assert isinstance(value["use_mouse"],bool)

# Test for invalid data type for event
def test_event_invalid_data_type(login_locators):
    """Checks if the event value is a string"""
    for key,value in login_locators["login"].items():
      assert isinstance(value["event"],str)
```