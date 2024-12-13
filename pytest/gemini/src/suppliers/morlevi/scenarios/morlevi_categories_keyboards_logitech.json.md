```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides test data loaded from the JSON file."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_keyboards_logitech.json'
    with open(file_path, 'r') as f:
        return json.load(f)

def test_logitech_keyboard_wireless_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH WIRELESS KEYBOARD' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH WIRELESS KEYBOARD')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "-----------------------------------------------LOGITECH WIRELESS KEYBOARD----------------------------------------------"
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,204,316"

def test_logitech_keyboard_usb_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH USB KEYBOARD' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH USB KEYBOARD')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "-----------------------------------------------LOGITECH USB KEYBOARD----------------------------------------------"
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,204,315"


def test_logitech_mouse_usb_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH USB MOUSE' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH USB MOUSE')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/108?p_315=29&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,206,317"

def test_logitech_mouse_wireless_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH WIRELESS MOUSE' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH WIRELESS MOUSE')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/109?p_315=29&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,206,318"

def test_logitech_keyboard_mouse_set_usb_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH USB KEYBOARD-MOUSE SET' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH USB KEYBOARD-MOUSE SET')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/113?p_315=29&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,207,208"

def test_logitech_keyboard_mouse_set_wireless_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH WIRELESS  KEYBOARD-MOUSE SET' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH WIRELESS  KEYBOARD-MOUSE SET')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/114?p_315=29&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,207,334"

def test_logitech_gaming_keyboard_scenario(morlevi_categories_data):
    """Checks the 'LOGITECH GAMING  KEYBOARD' scenario."""
    scenario = morlevi_categories_data['scenarios'].get('LOGITECH GAMING  KEYBOARD')
    assert scenario is not None
    assert scenario['brand'] == 'LOGITECH'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/239?p_315=29&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "203,205"

def test_missing_scenario(morlevi_categories_data):
    """Checks the handling of a missing scenario."""
    scenario = morlevi_categories_data['scenarios'].get('NON_EXISTENT_KEYBOARD')
    assert scenario is None
```