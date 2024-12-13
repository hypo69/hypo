```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_locators():
    """Loads the login locators from the JSON file."""
    with open('hypotez/src/suppliers/ivory/locators/login.json', 'r') as f:
        return json.load(f)

def test_login_locators_structure(login_locators):
    """
    Tests the basic structure of the login locators JSON file.
    Verifies that the root element is named 'login' and contains the expected keys.
    """
    assert "login" in login_locators, "Root element 'login' is missing."
    assert isinstance(login_locators["login"], dict), "The 'login' element should be a dictionary."
    expected_keys = ["open_login_inputs", "email_input", "continue_button", 
                     "password_input", "keep_signed_in_checkbox", "success_login_button"]
    for key in expected_keys:
         assert key in login_locators["login"], f"Missing key '{key}' in 'login' dictionary."

def test_login_locator_attributes(login_locators):
     """
     Tests each locator's attributes.
     Checks that each locator has the expected keys: 'by', 'selector', 'if_list', 'use_mouse', 'mandatory',
     'timeout', 'timeout_for_event', 'event', and 'logic for action[AND|OR|XOR|VALUE|null]'.
     It also verifies that the 'by' key value is a string and not an empty string, the selector key value is a string and not empty string.
     And if_list key value is a string and not empty string, use_mouse and mandatory key values are bool.
     timeout key value is int. timeout_for_event key value is a string and not an empty string, event key value is string and not an empty string.
     logic for action[AND|OR|XOR|VALUE|null] is None.
    """

     for locator_key, locator_data in login_locators["login"].items():
            assert "by" in locator_data, f"Missing 'by' key in '{locator_key}'."
            assert isinstance(locator_data["by"], str), f"The 'by' value of '{locator_key}' must be a string."
            assert locator_data["by"] != "", f"The 'by' value of '{locator_key}' cannot be an empty string."
            
            assert "selector" in locator_data, f"Missing 'selector' key in '{locator_key}'."
            assert isinstance(locator_data["selector"], str), f"The 'selector' value of '{locator_key}' must be a string."
            assert locator_data["selector"] != "", f"The 'selector' value of '{locator_key}' cannot be an empty string."

            assert "if_list" in locator_data, f"Missing 'if_list' key in '{locator_key}'."
            assert isinstance(locator_data["if_list"], str), f"The 'if_list' value of '{locator_key}' must be a string."
            assert locator_data["if_list"] != "", f"The 'if_list' value of '{locator_key}' cannot be an empty string."

            assert "use_mouse" in locator_data, f"Missing 'use_mouse' key in '{locator_key}'."
            assert isinstance(locator_data["use_mouse"], bool), f"The 'use_mouse' value of '{locator_key}' must be a boolean."
           
            assert "mandatory" in locator_data, f"Missing 'mandatory' key in '{locator_key}'."
            assert isinstance(locator_data["mandatory"], bool), f"The 'mandatory' value of '{locator_key}' must be a boolean."
           
            assert "timeout" in locator_data, f"Missing 'timeout' key in '{locator_key}'."
            assert isinstance(locator_data["timeout"], int), f"The 'timeout' value of '{locator_key}' must be an int."
           
            assert "timeout_for_event" in locator_data, f"Missing 'timeout_for_event' key in '{locator_key}'."
            assert isinstance(locator_data["timeout_for_event"], str), f"The 'timeout_for_event' value of '{locator_key}' must be a string."
            assert locator_data["timeout_for_event"] != "", f"The 'timeout_for_event' value of '{locator_key}' cannot be an empty string."
          
            assert "event" in locator_data, f"Missing 'event' key in '{locator_key}'."
            assert isinstance(locator_data["event"], str), f"The 'event' value of '{locator_key}' must be a string."
            assert locator_data["event"] != "", f"The 'event' value of '{locator_key}' cannot be an empty string."

            assert "logic for action[AND|OR|XOR|VALUE|null]" in locator_data, f"Missing 'logic for action[AND|OR|XOR|VALUE|null]' key in '{locator_key}'."
            assert locator_data["logic for action[AND|OR|XOR|VALUE|null]" ] is None, f"The 'logic for action[AND|OR|XOR|VALUE|null]' value of '{locator_key}' must be None."
         
def test_login_locator_selector_valid_xpath(login_locators):
    """
    Tests if the selectors are valid XPATH expressions (basic check for format).
    This is a very basic check and does not guarantee the validity of XPATH but helps catch common mistakes.
    """
    for locator_key, locator_data in login_locators["login"].items():
            selector = locator_data["selector"]
            assert selector.startswith("//"), f"Selector for '{locator_key}' does not start with '//', which is a common pattern for XPATH."

def test_login_locator_event_valid_format(login_locators):
    """
    Test if the event strings have a valid format.
    Check for valid events like click() or send_keys(<string>).
    """
    for locator_key, locator_data in login_locators["login"].items():
        event = locator_data["event"]
        if 'click()' in event:
           assert event == "click()", f"The click() event for {locator_key} does not match 'click()'."
        elif 'send_keys' in event:
             assert event.startswith("send_keys(") and event.endswith(")") ,f"The send_keys() event for {locator_key} is not in the correct format 'send_keys(..)'."
        else:
           pytest.fail(f"Invalid event format for {locator_key}: {event}")
```