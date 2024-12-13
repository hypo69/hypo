```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def categories_data():
    """Provides the JSON data as a dictionary."""
    json_data = """
    {
      "LOGITECH WIRELESS KEYBOARD": {
        "brand": "LOGITECH",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manId=10",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "203,204,316"
      },
      "LOGITECH USB KEYBOARD": {
        "brand": "LOGITECH",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=589&manId=10",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "203,204,315"
      },
      "LOGITECH USB MOUSE": {
        "brand": "LOGITECH",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manId=10",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "203,206,317"
      },
      "LOGITECH WIRELESS MOUSE": {
        "brand": "LOGITECH",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=586&manId=10",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "203,206,318"
      },
      "LOGITECH USB KEYBOARD-MOUSE SET": {
        "brand": "LOGITECH",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=10",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "203,207,208"
      },
      "LOGITECH WIRELESS  KEYBOARD-MOUSE SET": {
        "brand": "LOGITECH",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=10",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "203,207,334"
      }
    }
    """
    return json.loads(json_data)

def test_category_count(categories_data):
    """Verify the correct number of categories are loaded."""
    assert len(categories_data) == 6, "The number of categories should be 6"

def test_logitech_wireless_keyboard_data(categories_data):
    """Verify the data for 'LOGITECH WIRELESS KEYBOARD' is correct."""
    keyboard_data = categories_data.get("LOGITECH WIRELESS KEYBOARD")
    assert keyboard_data is not None, "Data for 'LOGITECH WIRELESS KEYBOARD' should exist"
    assert keyboard_data["brand"] == "LOGITECH", "Brand should be 'LOGITECH'"
    assert keyboard_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manId=10", "URL should match"
    assert keyboard_data["checkbox"] == False, "Checkbox should be False"
    assert keyboard_data["active"] == True, "Active should be True"
    assert keyboard_data["condition"] == "new", "Condition should be new"
    assert keyboard_data["presta_categories"] == "203,204,316", "Presta categories should match"

def test_logitech_usb_keyboard_data(categories_data):
    """Verify the data for 'LOGITECH USB KEYBOARD' is correct."""
    keyboard_data = categories_data.get("LOGITECH USB KEYBOARD")
    assert keyboard_data is not None, "Data for 'LOGITECH USB KEYBOARD' should exist"
    assert keyboard_data["brand"] == "LOGITECH", "Brand should be 'LOGITECH'"
    assert keyboard_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=589&manId=10", "URL should match"
    assert keyboard_data["checkbox"] == False, "Checkbox should be False"
    assert keyboard_data["active"] == True, "Active should be True"
    assert keyboard_data["condition"] == "new", "Condition should be new"
    assert keyboard_data["presta_categories"] == "203,204,315", "Presta categories should match"


def test_logitech_usb_mouse_data(categories_data):
     """Verify the data for 'LOGITECH USB MOUSE' is correct."""
     mouse_data = categories_data.get("LOGITECH USB MOUSE")
     assert mouse_data is not None, "Data for 'LOGITECH USB MOUSE' should exist"
     assert mouse_data["brand"] == "LOGITECH", "Brand should be 'LOGITECH'"
     assert mouse_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manId=10", "URL should match"
     assert mouse_data["checkbox"] == False, "Checkbox should be False"
     assert mouse_data["active"] == True, "Active should be True"
     assert mouse_data["condition"] == "new", "Condition should be new"
     assert mouse_data["presta_categories"] == "203,206,317", "Presta categories should match"

def test_logitech_wireless_mouse_data(categories_data):
    """Verify the data for 'LOGITECH WIRELESS MOUSE' is correct."""
    mouse_data = categories_data.get("LOGITECH WIRELESS MOUSE")
    assert mouse_data is not None, "Data for 'LOGITECH WIRELESS MOUSE' should exist"
    assert mouse_data["brand"] == "LOGITECH", "Brand should be 'LOGITECH'"
    assert mouse_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=586&manId=10", "URL should match"
    assert mouse_data["checkbox"] == False, "Checkbox should be False"
    assert mouse_data["active"] == True, "Active should be True"
    assert mouse_data["condition"] == "new", "Condition should be new"
    assert mouse_data["presta_categories"] == "203,206,318", "Presta categories should match"

def test_logitech_usb_keyboard_mouse_set_data(categories_data):
    """Verify the data for 'LOGITECH USB KEYBOARD-MOUSE SET' is correct."""
    set_data = categories_data.get("LOGITECH USB KEYBOARD-MOUSE SET")
    assert set_data is not None, "Data for 'LOGITECH USB KEYBOARD-MOUSE SET' should exist"
    assert set_data["brand"] == "LOGITECH", "Brand should be 'LOGITECH'"
    assert set_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=10", "URL should match"
    assert set_data["checkbox"] == False, "Checkbox should be False"
    assert set_data["active"] == True, "Active should be True"
    assert set_data["condition"] == "new", "Condition should be new"
    assert set_data["presta_categories"] == "203,207,208", "Presta categories should match"

def test_logitech_wireless_keyboard_mouse_set_data(categories_data):
    """Verify the data for 'LOGITECH WIRELESS  KEYBOARD-MOUSE SET' is correct."""
    set_data = categories_data.get("LOGITECH WIRELESS  KEYBOARD-MOUSE SET")
    assert set_data is not None, "Data for 'LOGITECH WIRELESS  KEYBOARD-MOUSE SET' should exist"
    assert set_data["brand"] == "LOGITECH", "Brand should be 'LOGITECH'"
    assert set_data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=10", "URL should match"
    assert set_data["checkbox"] == False, "Checkbox should be False"
    assert set_data["active"] == True, "Active should be True"
    assert set_data["condition"] == "new", "Condition should be new"
    assert set_data["presta_categories"] == "203,207,334", "Presta categories should match"

def test_missing_category(categories_data):
    """Verify that accessing a non-existent category returns None"""
    missing_data = categories_data.get("NON_EXISTENT_CATEGORY")
    assert missing_data is None, "Accessing a missing category should return None"
```