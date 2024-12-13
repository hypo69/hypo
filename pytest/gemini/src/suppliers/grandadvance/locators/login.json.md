```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def login_data():
    """Loads the login locators data from the JSON file."""
    with open('hypotez/src/suppliers/grandadvance/locators/login.json', 'r') as f:
        return json.load(f)

# Test for the 'open_login_inputs' locator
def test_open_login_inputs_locator_valid(login_data):
    """Checks if the 'open_login_inputs' locator data is correctly loaded."""
    locator = login_data['login']['open_login_inputs']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//span[@id='nav-link-accountList-nav-line-1']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] == False
    assert locator['mandatory'] == True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


def test_open_login_inputs_locator_invalid_type(login_data):
    """Checks behavior if there's a change in a data type in 'open_login_inputs' locator."""
    locator = login_data['login']['open_login_inputs']
    with pytest.raises(AssertionError):
      assert locator['timeout'] == "0"

def test_open_login_inputs_locator_invalid_value(login_data):
    """Checks behavior if there's a change in a value in 'open_login_inputs' locator."""
    locator = login_data['login']['open_login_inputs']
    with pytest.raises(AssertionError):
      assert locator['selector'] == "//span[@id='invalid_id']"

# Test for the 'email_input' locator
def test_email_input_locator_valid(login_data):
    """Checks if the 'email_input' locator data is correctly loaded."""
    locator = login_data['login']['email_input']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='ap_email']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] == False
    assert locator['mandatory'] == True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys('972547519449')"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_email_input_locator_invalid_value(login_data):
    """Checks behavior if there's a change in a value in 'email_input' locator."""
    locator = login_data['login']['email_input']
    with pytest.raises(AssertionError):
        assert locator['selector'] == "//input[@id='invalid_email']"
    

# Test for the 'continue_button' locator
def test_continue_button_locator_valid(login_data):
    """Checks if the 'continue_button' locator data is correctly loaded."""
    locator = login_data['login']['continue_button']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='continue']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] == False
    assert locator['mandatory'] == True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


def test_continue_button_locator_invalid_value(login_data):
    """Checks behavior if there's a change in a value in 'continue_button' locator."""
    locator = login_data['login']['continue_button']
    with pytest.raises(AssertionError):
        assert locator['selector'] == "//input[@id='invalid_continue_id']"


# Test for the 'password_input' locator
def test_password_input_locator_valid(login_data):
    """Checks if the 'password_input' locator data is correctly loaded."""
    locator = login_data['login']['password_input']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='ap_password']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] == False
    assert locator['mandatory'] == True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys('52UldxjzWGpdEQxWaNMY')"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None
    
def test_password_input_locator_invalid_value(login_data):
    """Checks behavior if there's a change in a value in 'password_input' locator."""
    locator = login_data['login']['password_input']
    with pytest.raises(AssertionError):
        assert locator['selector'] == "//input[@id='invalid_password']"


# Test for the 'keep_signed_in_checkbox' locator
def test_keep_signed_in_checkbox_locator_valid(login_data):
    """Checks if the 'keep_signed_in_checkbox' locator data is correctly loaded."""
    locator = login_data['login']['keep_signed_in_checkbox']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@name='rememberMe']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] == False
    assert locator['mandatory'] == True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_keep_signed_in_checkbox_locator_invalid_value(login_data):
    """Checks behavior if there's a change in a value in 'keep_signed_in_checkbox' locator."""
    locator = login_data['login']['keep_signed_in_checkbox']
    with pytest.raises(AssertionError):
        assert locator['selector'] == "//input[@name='invalid_rememberMe']"


# Test for the 'success_login_button' locator
def test_success_login_button_locator_valid(login_data):
    """Checks if the 'success_login_button' locator data is correctly loaded."""
    locator = login_data['login']['success_login_button']
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id='signInSubmit']"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] == False
    assert locator['mandatory'] == True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_success_login_button_locator_invalid_value(login_data):
    """Checks behavior if there's a change in a value in 'success_login_button' locator."""
    locator = login_data['login']['success_login_button']
    with pytest.raises(AssertionError):
        assert locator['selector'] == "//input[@id='invalid_signInSubmit']"
```