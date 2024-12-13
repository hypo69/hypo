```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_data():
    """Loads the login data from the JSON file."""
    with open("hypotez/src/suppliers/wallmart/locators/login.json", "r") as f:
        return json.load(f)

# Test for 'open_login_inputs' locator
def test_open_login_inputs_locator(login_data):
    """
    Checks the 'open_login_inputs' locator attributes.
    Validates 'by', 'selector', 'if_list', 'use_mouse', 'mandatory', 'timeout',
    'timeout_for_event', and 'event' values.
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

# Test for 'email_input' locator
def test_email_input_locator(login_data):
    """
    Checks the 'email_input' locator attributes.
     Validates 'by', 'selector', 'if_list', 'use_mouse', 'mandatory', 'timeout',
    'timeout_for_event', and 'event' values.
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
    
# Test for 'continue_button' locator
def test_continue_button_locator(login_data):
    """
    Checks the 'continue_button' locator attributes.
     Validates 'by', 'selector', 'if_list', 'use_mouse', 'mandatory', 'timeout',
    'timeout_for_event', and 'event' values.
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

# Test for 'password_input' locator
def test_password_input_locator(login_data):
    """
    Checks the 'password_input' locator attributes.
    Validates 'by', 'selector', 'if_list', 'use_mouse', 'mandatory', 'timeout',
    'timeout_for_event', and 'event' values.
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
    
# Test for 'keep_signed_in_checkbox' locator
def test_keep_signed_in_checkbox_locator(login_data):
    """
    Checks the 'keep_signed_in_checkbox' locator attributes.
     Validates 'by', 'selector', 'if_list', 'use_mouse', 'mandatory', 'timeout',
    'timeout_for_event', and 'event' values.
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

# Test for 'success_login_button' locator
def test_success_login_button_locator(login_data):
    """
    Checks the 'success_login_button' locator attributes.
     Validates 'by', 'selector', 'if_list', 'use_mouse', 'mandatory', 'timeout',
    'timeout_for_event', and 'event' values.
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
```