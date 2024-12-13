```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_data():
    """Loads the login data from the JSON file."""
    with open("hypotez/src/suppliers/ksp/locators/login.json", 'r') as f:
        return json.load(f)

# Test case for the 'open_login_inputs' locator
def test_open_login_inputs_valid_data(login_data):
    """
    Checks if the 'open_login_inputs' locator has the correct data structure.
    This includes validating the by, selector, if_list, use_mouse, mandatory, timeout,
    timeout_for_event and event properties.
    """
    locator = login_data['login']['open_login_inputs']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//span[@id='nav-link-accountList-nav-line-1']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


def test_open_login_inputs_missing_keys(login_data):
    """Checks if the required key are presented."""
    locator = login_data['login']['open_login_inputs']
    assert "attribute" in locator
    assert "by" in locator
    assert "selector" in locator
    assert "if_list" in locator
    assert "use_mouse" in locator
    assert "mandatory" in locator
    assert "timeout" in locator
    assert "timeout_for_event" in locator
    assert "event" in locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in locator

# Test case for the 'email_input' locator
def test_email_input_valid_data(login_data):
    """
    Checks if the 'email_input' locator has the correct data structure,
    including by, selector, if_list, use_mouse, mandatory, timeout,
    timeout_for_event and event properties.
    """
    locator = login_data['login']['email_input']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='ap_email']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys('972547519449')"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_email_input_missing_keys(login_data):
    """Checks if the required key are presented."""
    locator = login_data['login']['email_input']
    assert "attribute" in locator
    assert "by" in locator
    assert "selector" in locator
    assert "if_list" in locator
    assert "use_mouse" in locator
    assert "mandatory" in locator
    assert "timeout" in locator
    assert "timeout_for_event" in locator
    assert "event" in locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in locator


# Test case for the 'continue_button' locator
def test_continue_button_valid_data(login_data):
    """
    Checks if the 'continue_button' locator has the correct data structure,
    including by, selector, if_list, use_mouse, mandatory, timeout,
    timeout_for_event and event properties.
    """
    locator = login_data['login']['continue_button']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='continue']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_continue_button_missing_keys(login_data):
    """Checks if the required key are presented."""
    locator = login_data['login']['continue_button']
    assert "attribute" in locator
    assert "by" in locator
    assert "selector" in locator
    assert "if_list" in locator
    assert "use_mouse" in locator
    assert "mandatory" in locator
    assert "timeout" in locator
    assert "timeout_for_event" in locator
    assert "event" in locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in locator

# Test case for the 'password_input' locator
def test_password_input_valid_data(login_data):
    """
    Checks if the 'password_input' locator has the correct data structure,
    including by, selector, if_list, use_mouse, mandatory, timeout,
    timeout_for_event and event properties.
    """
    locator = login_data['login']['password_input']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='ap_password']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys('52UldxjzWGpdEQxWaNMY')"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_password_input_missing_keys(login_data):
    """Checks if the required key are presented."""
    locator = login_data['login']['password_input']
    assert "attribute" in locator
    assert "by" in locator
    assert "selector" in locator
    assert "if_list" in locator
    assert "use_mouse" in locator
    assert "mandatory" in locator
    assert "timeout" in locator
    assert "timeout_for_event" in locator
    assert "event" in locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in locator


# Test case for the 'keep_signed_in_checkbox' locator
def test_keep_signed_in_checkbox_valid_data(login_data):
    """
    Checks if the 'keep_signed_in_checkbox' locator has the correct data structure,
    including by, selector, if_list, use_mouse, mandatory, timeout,
    timeout_for_event and event properties.
    """
    locator = login_data['login']['keep_signed_in_checkbox']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@name='rememberMe']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


def test_keep_signed_in_checkbox_missing_keys(login_data):
    """Checks if the required key are presented."""
    locator = login_data['login']['keep_signed_in_checkbox']
    assert "attribute" in locator
    assert "by" in locator
    assert "selector" in locator
    assert "if_list" in locator
    assert "use_mouse" in locator
    assert "mandatory" in locator
    assert "timeout" in locator
    assert "timeout_for_event" in locator
    assert "event" in locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in locator

# Test case for the 'success_login_button' locator
def test_success_login_button_valid_data(login_data):
    """
    Checks if the 'success_login_button' locator has the correct data structure,
    including by, selector, if_list, use_mouse, mandatory, timeout,
    timeout_for_event and event properties.
    """
    locator = login_data['login']['success_login_button']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='signInSubmit']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_success_login_button_missing_keys(login_data):
    """Checks if the required key are presented."""
    locator = login_data['login']['success_login_button']
    assert "attribute" in locator
    assert "by" in locator
    assert "selector" in locator
    assert "if_list" in locator
    assert "use_mouse" in locator
    assert "mandatory" in locator
    assert "timeout" in locator
    assert "timeout_for_event" in locator
    assert "event" in locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in locator


def test_login_structure(login_data):
    """Checks if the main structure of the json is as expecter"""
    assert "login" in login_data
    assert "open_login_inputs" in login_data['login']
    assert "email_input" in login_data['login']
    assert "continue_button" in login_data['login']
    assert "password_input" in login_data['login']
    assert "keep_signed_in_checkbox" in login_data['login']
    assert "success_login_button" in login_data['login']
```