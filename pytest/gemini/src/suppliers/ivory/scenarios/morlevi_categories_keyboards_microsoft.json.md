```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_keyboards_microsoft.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test case for the presence of 'scenarios' key
def test_scenarios_key_exists(morlevi_data):
    """Checks that the 'scenarios' key exists in the JSON data."""
    assert 'scenarios' in morlevi_data, "The 'scenarios' key is missing in the JSON data."

# Test cases for individual scenarios
def test_microsoft_wireless_keyboard_scenario(morlevi_data):
    """Checks the data for 'MICROSOFT WIRELESS KEYBOARD' scenario."""
    scenario = morlevi_data['scenarios'].get('MICROSOFT WIRELESS KEYBOARD')
    assert scenario is not None, "The 'MICROSOFT WIRELESS KEYBOARD' scenario is missing."
    assert scenario['brand'] == 'MICROSOFT', "Incorrect brand for 'MICROSOFT WIRELESS KEYBOARD'."
    assert scenario['url'] == "-----------------------------------------------MICROSOFT WIRELESS KEYBOARD----------------------------------------------", "Incorrect URL for 'MICROSOFT WIRELESS KEYBOARD'."
    assert scenario['checkbox'] == False, "Incorrect checkbox value for 'MICROSOFT WIRELESS KEYBOARD'."
    assert scenario['active'] == True, "Incorrect active status for 'MICROSOFT WIRELESS KEYBOARD'."
    assert scenario['condition'] == "new", "Incorrect condition for 'MICROSOFT WIRELESS KEYBOARD'."
    assert scenario['presta_categories'] == "203,204,316", "Incorrect presta_categories for 'MICROSOFT WIRELESS KEYBOARD'."

def test_microsoft_usb_keyboard_scenario(morlevi_data):
    """Checks the data for 'MICROSOFT USB KEYBOARD' scenario."""
    scenario = morlevi_data['scenarios'].get('MICROSOFT USB KEYBOARD')
    assert scenario is not None, "The 'MICROSOFT USB KEYBOARD' scenario is missing."
    assert scenario['brand'] == 'MICROSOFT', "Incorrect brand for 'MICROSOFT USB KEYBOARD'."
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/155?p_315=42&sort=datafloat2%2Cprice&keyword=", "Incorrect URL for 'MICROSOFT USB KEYBOARD'."
    assert scenario['checkbox'] == False, "Incorrect checkbox value for 'MICROSOFT USB KEYBOARD'."
    assert scenario['active'] == True, "Incorrect active status for 'MICROSOFT USB KEYBOARD'."
    assert scenario['condition'] == "new", "Incorrect condition for 'MICROSOFT USB KEYBOARD'."
    assert scenario['presta_categories'] == "203,204,315", "Incorrect presta_categories for 'MICROSOFT USB KEYBOARD'."

def test_microsoft_usb_mouse_scenario(morlevi_data):
     """Checks the data for 'MICROSOFT USB MOUSE' scenario."""
     scenario = morlevi_data['scenarios'].get('MICROSOFT USB MOUSE')
     assert scenario is not None, "The 'MICROSOFT USB MOUSE' scenario is missing."
     assert scenario['brand'] == 'MICROSOFT', "Incorrect brand for 'MICROSOFT USB MOUSE'."
     assert scenario['url'] == "------------------------------------------------------MICROSOFT USB MOUSE------------------------------------------------", "Incorrect URL for 'MICROSOFT USB MOUSE'."
     assert scenario['checkbox'] == False, "Incorrect checkbox value for 'MICROSOFT USB MOUSE'."
     assert scenario['active'] == True, "Incorrect active status for 'MICROSOFT USB MOUSE'."
     assert scenario['condition'] == "new", "Incorrect condition for 'MICROSOFT USB MOUSE'."
     assert scenario['presta_categories'] == "203,206,317", "Incorrect presta_categories for 'MICROSOFT USB MOUSE'."

def test_microsoft_wireless_mouse_scenario(morlevi_data):
    """Checks the data for 'MICROSOFT WIRELESS MOUSE' scenario."""
    scenario = morlevi_data['scenarios'].get('MICROSOFT WIRELESS MOUSE')
    assert scenario is not None, "The 'MICROSOFT WIRELESS MOUSE' scenario is missing."
    assert scenario['brand'] == 'MICROSOFT', "Incorrect brand for 'MICROSOFT WIRELESS MOUSE'."
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/109?p_315=42&sort=datafloat2%2Cprice&keyword=", "Incorrect URL for 'MICROSOFT WIRELESS MOUSE'."
    assert scenario['checkbox'] == False, "Incorrect checkbox value for 'MICROSOFT WIRELESS MOUSE'."
    assert scenario['active'] == True, "Incorrect active status for 'MICROSOFT WIRELESS MOUSE'."
    assert scenario['condition'] == "new", "Incorrect condition for 'MICROSOFT WIRELESS MOUSE'."
    assert scenario['presta_categories'] == "203,206,318", "Incorrect presta_categories for 'MICROSOFT WIRELESS MOUSE'."

def test_microsoft_usb_keyboard_mouse_set_scenario(morlevi_data):
    """Checks the data for 'MICROSOFT USB KEYBOARD-MOUSE SET' scenario."""
    scenario = morlevi_data['scenarios'].get('MICROSOFT USB KEYBOARD-MOUSE SET')
    assert scenario is not None, "The 'MICROSOFT USB KEYBOARD-MOUSE SET' scenario is missing."
    assert scenario['brand'] == 'MICROSOFT', "Incorrect brand for 'MICROSOFT USB KEYBOARD-MOUSE SET'."
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/113?p_315=42&sort=datafloat2%2Cprice&keyword=", "Incorrect URL for 'MICROSOFT USB KEYBOARD-MOUSE SET'."
    assert scenario['checkbox'] == False, "Incorrect checkbox value for 'MICROSOFT USB KEYBOARD-MOUSE SET'."
    assert scenario['active'] == True, "Incorrect active status for 'MICROSOFT USB KEYBOARD-MOUSE SET'."
    assert scenario['condition'] == "new", "Incorrect condition for 'MICROSOFT USB KEYBOARD-MOUSE SET'."
    assert scenario['presta_categories'] == "203,207,208", "Incorrect presta_categories for 'MICROSOFT USB KEYBOARD-MOUSE SET'."

def test_microsoft_wireless_keyboard_mouse_set_scenario(morlevi_data):
    """Checks the data for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET' scenario."""
    scenario = morlevi_data['scenarios'].get('MICROSOFT WIRELESS  KEYBOARD-MOUSE SET')
    assert scenario is not None, "The 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET' scenario is missing."
    assert scenario['brand'] == 'MICROSOFT', "Incorrect brand for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'."
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/114?p_315=42&sort=datafloat2%2Cprice&keyword=", "Incorrect URL for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'."
    assert scenario['checkbox'] == False, "Incorrect checkbox value for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'."
    assert scenario['active'] == True, "Incorrect active status for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'."
    assert scenario['condition'] == "new", "Incorrect condition for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'."
    assert scenario['presta_categories'] == "203,207,334", "Incorrect presta_categories for 'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'."

# Test case for checking all scenarios
def test_all_scenarios_present(morlevi_data):
     """Checks if all expected scenarios are present in the JSON data."""
     expected_scenarios = [
         'MICROSOFT WIRELESS KEYBOARD',
         'MICROSOFT USB KEYBOARD',
         'MICROSOFT USB MOUSE',
         'MICROSOFT WIRELESS MOUSE',
         'MICROSOFT USB KEYBOARD-MOUSE SET',
         'MICROSOFT WIRELESS  KEYBOARD-MOUSE SET'
     ]
     
     scenarios_keys = morlevi_data['scenarios'].keys()
     for scenario in expected_scenarios:
          assert scenario in scenarios_keys, f"The '{scenario}' scenario is missing."


#Test case for validating all keys in scenarios
def test_all_keys_in_scenarios(morlevi_data):
    """Validates all keys in each scenario of the JSON data."""
    expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    
    for scenario_name, scenario_data in morlevi_data['scenarios'].items():
        for key in expected_keys:
            assert key in scenario_data, f"Key '{key}' is missing in scenario '{scenario_name}'."
```