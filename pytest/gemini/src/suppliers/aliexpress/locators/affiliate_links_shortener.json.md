```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def affiliate_links_shortener_data():
    """Loads the affiliate links shortener JSON data."""
    with open("hypotez/src/suppliers/aliexpress/locators/affiliate_links_shortener.json", "r") as f:
        return json.load(f)

def test_textarea_target_url_valid_structure(affiliate_links_shortener_data):
    """
    Checks the 'textarea_target_url' locator has the correct structure.
    Verifies the presence of required keys and correct types for the values
    """
    locator = affiliate_links_shortener_data.get("textarea_target_url")
    assert locator is not None, "textarea_target_url locator not found."
    assert isinstance(locator, dict), "textarea_target_url should be a dictionary"
    assert "attribute" in locator, "Missing key: attribute"
    assert "by" in locator, "Missing key: by"
    assert "selector" in locator, "Missing key: selector"
    assert "if_list" in locator, "Missing key: if_list"
    assert "use_mouse" in locator, "Missing key: use_mouse"
    assert "timeout" in locator, "Missing key: timeout"
    assert "timeout_for_event" in locator, "Missing key: timeout_for_event"
    assert "event" in locator, "Missing key: event"
    assert "mandatory" in locator, "Missing key: mandatory"
    assert "locator_description" in locator, "Missing key: locator_description"
    
    assert isinstance(locator["attribute"], (bool, str)), "attribute should be a boolean or a string"
    assert isinstance(locator["by"], str), "by should be a string"
    assert isinstance(locator["selector"], str), "selector should be a string"
    assert isinstance(locator["if_list"], str), "if_list should be a string"
    assert isinstance(locator["use_mouse"], bool), "use_mouse should be a boolean"
    assert isinstance(locator["timeout"], int), "timeout should be an integer"
    assert isinstance(locator["timeout_for_event"], str), "timeout_for_event should be a string"
    assert isinstance(locator["event"], (str,bool)), "event should be a string or boolean"
    assert isinstance(locator["mandatory"], bool), "mandatory should be a boolean"
    assert isinstance(locator["locator_description"], str), "locator_description should be a string"

def test_button_get_tracking_link_valid_structure(affiliate_links_shortener_data):
    """
    Checks the 'button_get_tracking_link' locator has the correct structure.
    Verifies the presence of required keys and correct types for the values
    """
    locator = affiliate_links_shortener_data.get("button_get_tracking_link")
    assert locator is not None, "button_get_tracking_link locator not found."
    assert isinstance(locator, dict), "button_get_tracking_link should be a dictionary"
    assert "attribute" in locator, "Missing key: attribute"
    assert "by" in locator, "Missing key: by"
    assert "selector" in locator, "Missing key: selector"
    assert "if_list" in locator, "Missing key: if_list"
    assert "use_mouse" in locator, "Missing key: use_mouse"
    assert "timeout" in locator, "Missing key: timeout"
    assert "timeout_for_event" in locator, "Missing key: timeout_for_event"
    assert "event" in locator, "Missing key: event"
    assert "mandatory" in locator, "Missing key: mandatory"
    assert "locator_description" in locator, "Missing key: locator_description"
    
    assert isinstance(locator["attribute"], (bool, str)), "attribute should be a boolean or a string"
    assert isinstance(locator["by"], str), "by should be a string"
    assert isinstance(locator["selector"], str), "selector should be a string"
    assert isinstance(locator["if_list"], str), "if_list should be a string"
    assert isinstance(locator["use_mouse"], bool), "use_mouse should be a boolean"
    assert isinstance(locator["timeout"], int), "timeout should be an integer"
    assert isinstance(locator["timeout_for_event"], str), "timeout_for_event should be a string"
    assert isinstance(locator["event"], (str,bool)), "event should be a string or boolean"
    assert isinstance(locator["mandatory"], bool), "mandatory should be a boolean"
    assert isinstance(locator["locator_description"], str), "locator_description should be a string"

def test_textarea_short_link_valid_structure(affiliate_links_shortener_data):
    """
    Checks the 'textarea_short_link' locator has the correct structure.
    Verifies the presence of required keys and correct types for the values
    """
    locator = affiliate_links_shortener_data.get("textarea_short_link")
    assert locator is not None, "textarea_short_link locator not found."
    assert isinstance(locator, dict), "textarea_short_link should be a dictionary"
    assert "attribute" in locator, "Missing key: attribute"
    assert "by" in locator, "Missing key: by"
    assert "selector" in locator, "Missing key: selector"
    assert "if_list" in locator, "Missing key: if_list"
    assert "use_mouse" in locator, "Missing key: use_mouse"
    assert "timeout" in locator, "Missing key: timeout"
    assert "timeout_for_event" in locator, "Missing key: timeout_for_event"
    assert "event" in locator, "Missing key: event"
    assert "mandatory" in locator, "Missing key: mandatory"
    assert "locator_description" in locator, "Missing key: locator_description"
    
    assert isinstance(locator["attribute"], (bool, str)), "attribute should be a boolean or a string"
    assert isinstance(locator["by"], str), "by should be a string"
    assert isinstance(locator["selector"], str), "selector should be a string"
    assert isinstance(locator["if_list"], str), "if_list should be a string"
    assert isinstance(locator["use_mouse"], bool), "use_mouse should be a boolean"
    assert isinstance(locator["timeout"], int), "timeout should be an integer"
    assert isinstance(locator["timeout_for_event"], str), "timeout_for_event should be a string"
    assert isinstance(locator["event"], (str,bool)), "event should be a string or boolean"
    assert isinstance(locator["mandatory"], bool), "mandatory should be a boolean"
    assert isinstance(locator["locator_description"], str), "locator_description should be a string"


def test_all_locators_exist(affiliate_links_shortener_data):
     """
    Checks that all expected locators exist in the JSON data.
    """
     assert "textarea_target_url" in affiliate_links_shortener_data, "textarea_target_url locator missing"
     assert "button_get_tracking_link" in affiliate_links_shortener_data, "button_get_tracking_link locator missing"
     assert "textarea_short_link" in affiliate_links_shortener_data, "textarea_short_link locator missing"

def test_textarea_target_url_selector_is_xpath(affiliate_links_shortener_data):
    """
    Checks if the selector type of 'textarea_target_url' is XPATH.
    """
    assert affiliate_links_shortener_data["textarea_target_url"]["by"] == "XPATH"

def test_button_get_tracking_link_selector_is_xpath(affiliate_links_shortener_data):
    """
    Checks if the selector type of 'button_get_tracking_link' is XPATH.
    """
    assert affiliate_links_shortener_data["button_get_tracking_link"]["by"] == "XPATH"

def test_textarea_short_link_selector_is_xpath(affiliate_links_shortener_data):
    """
    Checks if the selector type of 'textarea_short_link' is XPATH.
    """
    assert affiliate_links_shortener_data["textarea_short_link"]["by"] == "XPATH"

def test_textarea_short_link_attribute_is_value(affiliate_links_shortener_data):
    """
    Checks if the attribute of 'textarea_short_link' is value.
    """
    assert affiliate_links_shortener_data["textarea_short_link"]["attribute"] == "value"

def test_textarea_target_url_event_is_string_or_false(affiliate_links_shortener_data):
    """
    Checks if the event of 'textarea_target_url' is a string or boolean.
    """
    assert isinstance(affiliate_links_shortener_data["textarea_target_url"]["event"], (str,bool)), "event should be a string or boolean"

def test_button_get_tracking_link_event_is_string_or_false(affiliate_links_shortener_data):
    """
    Checks if the event of 'button_get_tracking_link' is a string or boolean.
    """
    assert isinstance(affiliate_links_shortener_data["button_get_tracking_link"]["event"], (str,bool)), "event should be a string or boolean"
    

def test_textarea_short_link_event_is_false(affiliate_links_shortener_data):
    """
    Checks if the event of 'textarea_short_link' is False.
    """
    assert affiliate_links_shortener_data["textarea_short_link"]["event"] is False
```