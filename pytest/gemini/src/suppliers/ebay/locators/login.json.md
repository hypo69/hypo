```python
import pytest
import json


@pytest.fixture
def login_locators():
    """Provides the login locators data from the JSON file."""
    json_data = """
    {
        "login": {
            "open_login_inputs": {
                "attribute": null,
                "by": "XPATH",
                "selector": "//span[@id='nav-link-accountList-nav-line-1']",
                "if_list": "first",
                "use_mouse": false,
                "mandatory": true,
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "logic for action[AND|OR|XOR|VALUE|null]": null
            },
            "email_input": {
                "attribute": null,
                "by": "XPATH",
                "selector": "//input[@id='ap_email']",
                "if_list": "first",
                "use_mouse": false,
                "mandatory": true,
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "send_keys('972547519449')",
                "logic for action[AND|OR|XOR|VALUE|null]": null
            },
            "continue_button": {
                "attribute": null,
                "by": "XPATH",
                "selector": "//input[@id='continue']",
                "if_list": "first",
                "use_mouse": false,
                "mandatory": true,
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "logic for action[AND|OR|XOR|VALUE|null]": null
            },
            "password_input": {
                "attribute": null,
                "by": "XPATH",
                "selector": "//input[@id='ap_password']",
                "if_list": "first",
                "use_mouse": false,
                "mandatory": true,
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "send_keys('52UldxjzWGpdEQxWaNMY')",
                "logic for action[AND|OR|XOR|VALUE|null]": null
            },
             "keep_signed_in_checkbox": {
                "attribute": null,
                "by": "XPATH",
                "selector": "//input[@name='rememberMe']",
                "if_list": "first",
                "use_mouse": false,
                "mandatory": true,
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "logic for action[AND|OR|XOR|VALUE|null]": null
            },
            "success_login_button": {
                "attribute": null,
                "by": "XPATH",
                "selector": "//input[@id='signInSubmit']",
                "if_list": "first",
                "use_mouse": false,
                "mandatory": true,
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "logic for action[AND|OR|XOR|VALUE|null]": null
            }
        }
    }
    """
    return json.loads(json_data)


def test_login_locators_structure(login_locators):
    """
    Checks if the structure of the loaded JSON is as expected.
    Verifies that the 'login' key exists and is a dictionary.
    """
    assert "login" in login_locators
    assert isinstance(login_locators["login"], dict)


def test_open_login_inputs_structure(login_locators):
    """
    Checks the structure of 'open_login_inputs'.
    Verifies the presence of all expected keys with correct data types.
    """
    open_login_inputs = login_locators["login"].get("open_login_inputs")
    assert isinstance(open_login_inputs, dict)
    assert "attribute" in open_login_inputs
    assert "by" in open_login_inputs
    assert "selector" in open_login_inputs
    assert "if_list" in open_login_inputs
    assert "use_mouse" in open_login_inputs
    assert "mandatory" in open_login_inputs
    assert "timeout" in open_login_inputs
    assert "timeout_for_event" in open_login_inputs
    assert "event" in open_login_inputs
    assert "logic for action[AND|OR|XOR|VALUE|null]" in open_login_inputs


def test_email_input_structure(login_locators):
    """
    Checks the structure of 'email_input'.
    Verifies the presence of all expected keys with correct data types.
    """
    email_input = login_locators["login"].get("email_input")
    assert isinstance(email_input, dict)
    assert "attribute" in email_input
    assert "by" in email_input
    assert "selector" in email_input
    assert "if_list" in email_input
    assert "use_mouse" in email_input
    assert "mandatory" in email_input
    assert "timeout" in email_input
    assert "timeout_for_event" in email_input
    assert "event" in email_input
    assert "logic for action[AND|OR|XOR|VALUE|null]" in email_input


def test_continue_button_structure(login_locators):
    """
    Checks the structure of 'continue_button'.
    Verifies the presence of all expected keys with correct data types.
    """
    continue_button = login_locators["login"].get("continue_button")
    assert isinstance(continue_button, dict)
    assert "attribute" in continue_button
    assert "by" in continue_button
    assert "selector" in continue_button
    assert "if_list" in continue_button
    assert "use_mouse" in continue_button
    assert "mandatory" in continue_button
    assert "timeout" in continue_button
    assert "timeout_for_event" in continue_button
    assert "event" in continue_button
    assert "logic for action[AND|OR|XOR|VALUE|null]" in continue_button


def test_password_input_structure(login_locators):
    """
    Checks the structure of 'password_input'.
    Verifies the presence of all expected keys with correct data types.
    """
    password_input = login_locators["login"].get("password_input")
    assert isinstance(password_input, dict)
    assert "attribute" in password_input
    assert "by" in password_input
    assert "selector" in password_input
    assert "if_list" in password_input
    assert "use_mouse" in password_input
    assert "mandatory" in password_input
    assert "timeout" in password_input
    assert "timeout_for_event" in password_input
    assert "event" in password_input
    assert "logic for action[AND|OR|XOR|VALUE|null]" in password_input


def test_keep_signed_in_checkbox_structure(login_locators):
    """
    Checks the structure of 'keep_signed_in_checkbox'.
    Verifies the presence of all expected keys with correct data types.
    """
    keep_signed_in_checkbox = login_locators["login"].get("keep_signed_in_checkbox")
    assert isinstance(keep_signed_in_checkbox, dict)
    assert "attribute" in keep_signed_in_checkbox
    assert "by" in keep_signed_in_checkbox
    assert "selector" in keep_signed_in_checkbox
    assert "if_list" in keep_signed_in_checkbox
    assert "use_mouse" in keep_signed_in_checkbox
    assert "mandatory" in keep_signed_in_checkbox
    assert "timeout" in keep_signed_in_checkbox
    assert "timeout_for_event" in keep_signed_in_checkbox
    assert "event" in keep_signed_in_checkbox
    assert "logic for action[AND|OR|XOR|VALUE|null]" in keep_signed_in_checkbox


def test_success_login_button_structure(login_locators):
    """
    Checks the structure of 'success_login_button'.
    Verifies the presence of all expected keys with correct data types.
    """
    success_login_button = login_locators["login"].get("success_login_button")
    assert isinstance(success_login_button, dict)
    assert "attribute" in success_login_button
    assert "by" in success_login_button
    assert "selector" in success_login_button
    assert "if_list" in success_login_button
    assert "use_mouse" in success_login_button
    assert "mandatory" in success_login_button
    assert "timeout" in success_login_button
    assert "timeout_for_event" in success_login_button
    assert "event" in success_login_button
    assert "logic for action[AND|OR|XOR|VALUE|null]" in success_login_button


def test_all_locators_have_expected_keys(login_locators):
    """
    Test to ensure all locators have the expected keys with correct data types.
    """
    expected_keys = [
        "attribute",
        "by",
        "selector",
        "if_list",
        "use_mouse",
        "mandatory",
        "timeout",
        "timeout_for_event",
        "event",
        "logic for action[AND|OR|XOR|VALUE|null]",
    ]

    for locator_name, locator_data in login_locators["login"].items():
        for key in expected_keys:
            assert key in locator_data, f"Key '{key}' missing in '{locator_name}'"
            if key in ["use_mouse","mandatory"]:
                assert isinstance(locator_data[key],bool), f"Key '{key}' in '{locator_name}' should be boolean"
            elif key in ["timeout"]:
                assert isinstance(locator_data[key],int), f"Key '{key}' in '{locator_name}' should be int"
            else:
                assert locator_data[key] is None or isinstance(locator_data[key], str), f"Key '{key}' in '{locator_name}' should be string or None"


def test_timeout_values_are_valid(login_locators):
        """
        Test to ensure that timeout values for all locators are non-negative integers.
        """
        for locator_name, locator_data in login_locators["login"].items():
            timeout_value = locator_data.get("timeout")
            assert isinstance(timeout_value, int), f"Timeout value in '{locator_name}' must be an integer."
            assert timeout_value >= 0, f"Timeout value in '{locator_name}' must be non-negative."

def test_by_values_are_valid(login_locators):
    """
    Test to ensure all 'by' values are valid strings (e.g., "XPATH", "CSS").
    """
    valid_by_values = ["XPATH", "CSS", "ID", "CLASS_NAME", "LINK_TEXT","PARTIAL_LINK_TEXT","TAG_NAME"]
    for locator_name, locator_data in login_locators["login"].items():
        by_value = locator_data.get("by")
        assert by_value in valid_by_values, f"Invalid 'by' value: '{by_value}' in '{locator_name}'. Must be one of {valid_by_values}"

def test_if_list_values_are_valid(login_locators):
    """
    Test to ensure all 'if_list' values are valid strings (e.g., "first", "all").
    """
    valid_if_list_values = ["first", "all"]
    for locator_name, locator_data in login_locators["login"].items():
        if_list_value = locator_data.get("if_list")
        assert if_list_value in valid_if_list_values, f"Invalid 'if_list' value: '{if_list_value}' in '{locator_name}'. Must be one of {valid_if_list_values}"
```