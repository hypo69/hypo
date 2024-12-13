```python
import pytest
import json

# Assuming the JSON data is loaded into a dictionary called 'locators'
@pytest.fixture
def locators():
    """Fixture to load the locators from the JSON file."""
    
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
def test_login_locators_structure(locators):
    """Checks if the login locators structure is correct and contains all required keys."""
    assert "login" in locators, "The 'login' key is missing."
    assert isinstance(locators["login"], dict), "The 'login' value is not a dictionary."

    expected_keys = [
        "open_login_inputs",
        "email_input",
        "continue_button",
        "password_input",
        "keep_signed_in_checkbox",
        "success_login_button",
    ]

    for key in expected_keys:
        assert key in locators["login"], f"The '{key}' key is missing in login locators."
        assert isinstance(locators["login"][key], dict), f"The value of '{key}' is not a dictionary."

def test_locator_keys_structure(locators):
  """Checks if each locator has the required keys, values, and correct data types."""
  for locator_group in locators['login'].values():
      assert "attribute" in locator_group , f"The 'attribute' key is missing in  locator"
      assert "by" in locator_group , f"The 'by' key is missing in locator"
      assert "selector" in locator_group , f"The 'selector' key is missing in locator"
      assert "if_list" in locator_group , f"The 'if_list' key is missing in locator"
      assert "use_mouse" in locator_group , f"The 'use_mouse' key is missing in locator"
      assert "mandatory" in locator_group , f"The 'mandatory' key is missing in locator"
      assert "timeout" in locator_group , f"The 'timeout' key is missing in locator"
      assert "timeout_for_event" in locator_group , f"The 'timeout_for_event' key is missing in locator"
      assert "event" in locator_group , f"The 'event' key is missing in locator"
      assert "logic for action[AND|OR|XOR|VALUE|null]" in locator_group , f"The 'logic for action[AND|OR|XOR|VALUE|null]' key is missing in locator"
      
      assert isinstance(locator_group["attribute"], (str, type(None))), f"The 'attribute' key is of not supported type"
      assert isinstance(locator_group["by"], str), f"The 'by' key should be a string in locator"
      assert isinstance(locator_group["selector"], str), f"The 'selector' key should be a string in locator"
      assert isinstance(locator_group["if_list"], str), f"The 'if_list' key should be a string in locator"
      assert isinstance(locator_group["use_mouse"], bool), f"The 'use_mouse' key should be a bool in locator"
      assert isinstance(locator_group["mandatory"], bool), f"The 'mandatory' key should be a bool in locator"
      assert isinstance(locator_group["timeout"], int), f"The 'timeout' key should be a int in locator"
      assert isinstance(locator_group["timeout_for_event"], str), f"The 'timeout_for_event' key should be a string in locator"
      assert isinstance(locator_group["event"], str), f"The 'event' key should be a string in locator"
      assert isinstance(locator_group["logic for action[AND|OR|XOR|VALUE|null]"], (str,type(None))), f"The 'logic for action[AND|OR|XOR|VALUE|null]' key is of not supported type"


def test_locator_values(locators):
    """Checks specific values for correct locator structure."""
    assert locators["login"]["open_login_inputs"]["by"] == "XPATH"
    assert locators["login"]["open_login_inputs"]["selector"] == "//span[@id='nav-link-accountList-nav-line-1']"
    assert locators["login"]["email_input"]["by"] == "XPATH"
    assert locators["login"]["email_input"]["selector"] == "//input[@id='ap_email']"
    assert locators["login"]["continue_button"]["by"] == "XPATH"
    assert locators["login"]["continue_button"]["selector"] == "//input[@id='continue']"
    assert locators["login"]["password_input"]["by"] == "XPATH"
    assert locators["login"]["password_input"]["selector"] == "//input[@id='ap_password']"
    assert locators["login"]["keep_signed_in_checkbox"]["by"] == "XPATH"
    assert locators["login"]["keep_signed_in_checkbox"]["selector"] == "//input[@name='rememberMe']"
    assert locators["login"]["success_login_button"]["by"] == "XPATH"
    assert locators["login"]["success_login_button"]["selector"] == "//input[@id='signInSubmit']"

    # Check timeout default value
    for locator in locators["login"].values():
        assert locator["timeout"] == 0


def test_locator_event_values(locators):
    """Checks specific event values for correct locator structure."""
    assert locators["login"]["open_login_inputs"]["event"] == "click()"
    assert locators["login"]["email_input"]["event"] == "send_keys('972547519449')"
    assert locators["login"]["continue_button"]["event"] == "click()"
    assert locators["login"]["password_input"]["event"] == "send_keys('52UldxjzWGpdEQxWaNMY')"
    assert locators["login"]["keep_signed_in_checkbox"]["event"] == "click()"
    assert locators["login"]["success_login_button"]["event"] == "click()"

def test_locator_mandatory_boolean(locators):
    """Checks if all mandatory values are set to True."""
    for locator in locators["login"].values():
      assert locator["mandatory"] is True
      assert isinstance(locator["mandatory"], bool)
def test_locator_use_mouse_boolean(locators):
    """Checks if all use_mouse values are set to False."""
    for locator in locators["login"].values():
      assert locator["use_mouse"] is False
      assert isinstance(locator["use_mouse"], bool)
```