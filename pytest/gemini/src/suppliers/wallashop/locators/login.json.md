```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_data():
    """Loads the login data from the JSON file."""
    with open("hypotez/src/suppliers/wallashop/locators/login.json", "r") as f:
        return json.load(f)

def test_login_data_structure(login_data):
    """
    Test that the loaded JSON data has the correct structure.
    Verifies that the top-level key "login" exists and is a dictionary.
    """
    assert "login" in login_data, "The 'login' key is missing in the JSON data."
    assert isinstance(login_data["login"], dict), "The 'login' key should map to a dictionary."

def test_login_elements_presence(login_data):
    """
    Test that all expected elements are present in the login data.
    Iterates through the keys inside the 'login' dictionary and asserts each exists.
    """
    expected_elements = [
        "open_login_inputs",
        "email_input",
        "continue_button",
        "password_input",
        "keep_signed_in_checkbox",
        "success_login_button"
    ]

    for element in expected_elements:
        assert element in login_data["login"], f"Element '{element}' is missing in the login data."

def test_login_element_structure(login_data):
     """
     Test that each login element has the correct structure.
     Each element should be a dictionary and contain all expected keys such as by, selector, etc.
     """
     expected_keys = ["attribute", "by", "selector", "if_list", "use_mouse", "mandatory",
                      "timeout", "timeout_for_event", "event", "logic for action[AND|OR|XOR|VALUE|null]"]
     for element_name, element_data in login_data["login"].items():
        assert isinstance(element_data, dict), f"Element '{element_name}' should be a dictionary."
        for key in expected_keys:
            assert key in element_data, f"Key '{key}' is missing in element '{element_name}'"

def test_login_element_by_values(login_data):
    """
    Test that the 'by' key for each login element has a valid value ("XPATH").
    Checks that the 'by' key is always set to XPATH.
    """
    for element_name, element_data in login_data["login"].items():
        assert element_data["by"] == "XPATH", f"Element '{element_name}' 'by' key should be 'XPATH'"

def test_login_element_if_list_values(login_data):
    """
    Test that the 'if_list' key for each login element has a valid value ("first").
    Checks that the 'if_list' key is always set to "first".
    """
    for element_name, element_data in login_data["login"].items():
        assert element_data["if_list"] == "first", f"Element '{element_name}' 'if_list' key should be 'first'"

def test_login_element_use_mouse_values(login_data):
    """
    Test that the 'use_mouse' key for each login element has a valid value (False).
    Checks that the 'use_mouse' key is always set to False.
    """
    for element_name, element_data in login_data["login"].items():
        assert element_data["use_mouse"] is False, f"Element '{element_name}' 'use_mouse' key should be False"

def test_login_element_mandatory_values(login_data):
    """
    Test that the 'mandatory' key for each login element has a valid value (True).
    Checks that the 'mandatory' key is always set to True.
    """
    for element_name, element_data in login_data["login"].items():
        assert element_data["mandatory"] is True, f"Element '{element_name}' 'mandatory' key should be True"

def test_login_element_timeout_values(login_data):
    """
    Test that the 'timeout' key for each login element has a valid value (0).
    Checks that the 'timeout' key is always set to 0.
    """
    for element_name, element_data in login_data["login"].items():
        assert element_data["timeout"] == 0, f"Element '{element_name}' 'timeout' key should be 0"

def test_login_element_timeout_for_event_values(login_data):
      """
      Test that the 'timeout_for_event' key for each login element has a valid value ("presence_of_element_located").
      Checks that the 'timeout_for_event' key is always set to "presence_of_element_located".
      """
      for element_name, element_data in login_data["login"].items():
          assert element_data["timeout_for_event"] == "presence_of_element_located", f"Element '{element_name}' 'timeout_for_event' key should be 'presence_of_element_located'"

def test_login_element_event_values_not_empty(login_data):
    """
    Test that the 'event' key for each login element is not empty.
    Checks that the 'event' key has some value set.
    """
    for element_name, element_data in login_data["login"].items():
      assert element_data["event"] is not None, f"Element '{element_name}' 'event' key should not be None"
      assert len(element_data["event"]) > 0 , f"Element '{element_name}' 'event' key should not be empty"


def test_login_element_logic_for_action_values_null(login_data):
    """
    Test that the 'logic for action[AND|OR|XOR|VALUE|null]' key for each login element has a valid value (None).
    Checks that the 'logic for action[AND|OR|XOR|VALUE|null]' key is always set to None.
    """
    for element_name, element_data in login_data["login"].items():
        assert element_data["logic for action[AND|OR|XOR|VALUE|null]"] is None, f"Element '{element_name}' 'logic for action[AND|OR|XOR|VALUE|null]' key should be None"
```