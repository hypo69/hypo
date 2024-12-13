```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def keyboard_data():
    """Loads the keyboard data from the JSON file."""
    json_data = """
{
  "scenarios": {
    "COOLER MASTER USB KEYBOARD": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER KEYBOARD",
      "url": "https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": { "template": { "computer accessories": "WIRED KB" } }
    },
    "GENIUS USB KEYBOARD": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER USB KEYBOARD",
      "url": "https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,204,315"
    },
    "COOLER MASTER USB MOUSE": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER USB MOUSE",
      "url": "https://www.morlevi.co.il/Cat/108?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,206,317"
    },
    "COOLER MASTER WIRELESS MOUSE": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER WIRELESS MOUSE",
      "url": "--------------------------------------COOLER MASTER WIRELESS MOUSE--------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,206,318"
    },
    "COOLER MASTER USB KEYBOARD-MOUSE SET": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER USB KEYBOARD-MOUSE SET",
      "url": "https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,207,208"
    },
    "COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER WIRELESS KEYBOARD-MOUSE SET",
      "url": "--------------------------------------COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET--------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,207,334"
    },
    "COOLER MASTER GAMING  KEYBOARD": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER GAMING  KEYBOARD",
      "url": "https://www.morlevi.co.il/Cat/239?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,205"
    },
    "COOLER MASTER GAMING  MOUSE": {
      "brand": "COOLER MASTER",
      "template": "COOLER MASTER GAMING  MOUSE",
      "url": "https://www.morlevi.co.il/Cat/252?p_315=74&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,206,343"
    }
  }
}
"""
    return json.loads(json_data)



def test_keyboard_data_loaded(keyboard_data):
    """Test that the fixture loads the data correctly"""
    assert keyboard_data is not None
    assert isinstance(keyboard_data, dict)
    assert "scenarios" in keyboard_data

def test_cooler_master_usb_keyboard(keyboard_data):
    """Test the properties of the 'COOLER MASTER USB KEYBOARD' entry."""
    keyboard = keyboard_data["scenarios"].get("COOLER MASTER USB KEYBOARD")
    assert keyboard is not None
    assert keyboard["brand"] == "COOLER MASTER"
    assert keyboard["template"] == "COOLER MASTER KEYBOARD"
    assert keyboard["url"] == "https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword="
    assert keyboard["checkbox"] == False
    assert keyboard["active"] == True
    assert keyboard["condition"] == "new"
    assert keyboard["presta_categories"] == { "template": { "computer accessories": "WIRED KB" } }



def test_genius_usb_keyboard(keyboard_data):
    """Test the properties of the 'GENIUS USB KEYBOARD' entry."""
    keyboard = keyboard_data["scenarios"].get("GENIUS USB KEYBOARD")
    assert keyboard is not None
    assert keyboard["brand"] == "COOLER MASTER"
    assert keyboard["template"] == "COOLER MASTER USB KEYBOARD"
    assert keyboard["url"] == "https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword="
    assert keyboard["checkbox"] == False
    assert keyboard["active"] == True
    assert keyboard["condition"] == "new"
    assert keyboard["presta_categories"] == "203,204,315"


def test_cooler_master_usb_mouse(keyboard_data):
    """Test the properties of the 'COOLER MASTER USB MOUSE' entry."""
    mouse = keyboard_data["scenarios"].get("COOLER MASTER USB MOUSE")
    assert mouse is not None
    assert mouse["brand"] == "COOLER MASTER"
    assert mouse["template"] == "COOLER MASTER USB MOUSE"
    assert mouse["url"] == "https://www.morlevi.co.il/Cat/108?p_315=74&sort=datafloat2%2Cprice&keyword="
    assert mouse["checkbox"] == False
    assert mouse["active"] == True
    assert mouse["condition"] == "new"
    assert mouse["presta_categories"] == "203,206,317"


def test_cooler_master_wireless_mouse(keyboard_data):
    """Test the properties of the 'COOLER MASTER WIRELESS MOUSE' entry, specifically the url edge case."""
    mouse = keyboard_data["scenarios"].get("COOLER MASTER WIRELESS MOUSE")
    assert mouse is not None
    assert mouse["brand"] == "COOLER MASTER"
    assert mouse["template"] == "COOLER MASTER WIRELESS MOUSE"
    assert mouse["url"] == "--------------------------------------COOLER MASTER WIRELESS MOUSE--------------------------------"
    assert mouse["checkbox"] == False
    assert mouse["active"] == True
    assert mouse["condition"] == "new"
    assert mouse["presta_categories"] == "203,206,318"


def test_cooler_master_usb_keyboard_mouse_set(keyboard_data):
    """Test the properties of the 'COOLER MASTER USB KEYBOARD-MOUSE SET' entry."""
    set_item = keyboard_data["scenarios"].get("COOLER MASTER USB KEYBOARD-MOUSE SET")
    assert set_item is not None
    assert set_item["brand"] == "COOLER MASTER"
    assert set_item["template"] == "COOLER MASTER USB KEYBOARD-MOUSE SET"
    assert set_item["url"] == "https://www.morlevi.co.il/Cat/113?p_315=74&sort=datafloat2%2Cprice&keyword="
    assert set_item["checkbox"] == False
    assert set_item["active"] == True
    assert set_item["condition"] == "new"
    assert set_item["presta_categories"] == "203,207,208"

def test_cooler_master_wireless_keyboard_mouse_set(keyboard_data):
    """Test the properties of the 'COOLER MASTER WIRELESS KEYBOARD-MOUSE SET' entry, including the url edge case."""
    set_item = keyboard_data["scenarios"].get("COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET")
    assert set_item is not None
    assert set_item["brand"] == "COOLER MASTER"
    assert set_item["template"] == "COOLER MASTER WIRELESS KEYBOARD-MOUSE SET"
    assert set_item["url"] == "--------------------------------------COOLER MASTER WIRELESS  KEYBOARD-MOUSE SET--------------------------------"
    assert set_item["checkbox"] == False
    assert set_item["active"] == True
    assert set_item["condition"] == "new"
    assert set_item["presta_categories"] == "203,207,334"


def test_cooler_master_gaming_keyboard(keyboard_data):
    """Test the properties of the 'COOLER MASTER GAMING  KEYBOARD' entry."""
    gaming_keyboard = keyboard_data["scenarios"].get("COOLER MASTER GAMING  KEYBOARD")
    assert gaming_keyboard is not None
    assert gaming_keyboard["brand"] == "COOLER MASTER"
    assert gaming_keyboard["template"] == "COOLER MASTER GAMING  KEYBOARD"
    assert gaming_keyboard["url"] == "https://www.morlevi.co.il/Cat/239?p_315=74&sort=datafloat2%2Cprice&keyword="
    assert gaming_keyboard["checkbox"] == False
    assert gaming_keyboard["active"] == True
    assert gaming_keyboard["condition"] == "new"
    assert gaming_keyboard["presta_categories"] == "203,205"


def test_cooler_master_gaming_mouse(keyboard_data):
    """Test the properties of the 'COOLER MASTER GAMING  MOUSE' entry."""
    gaming_mouse = keyboard_data["scenarios"].get("COOLER MASTER GAMING  MOUSE")
    assert gaming_mouse is not None
    assert gaming_mouse["brand"] == "COOLER MASTER"
    assert gaming_mouse["template"] == "COOLER MASTER GAMING  MOUSE"
    assert gaming_mouse["url"] == "https://www.morlevi.co.il/Cat/252?p_315=74&sort=datafloat2%2Cprice&keyword="
    assert gaming_mouse["checkbox"] == False
    assert gaming_mouse["active"] == True
    assert gaming_mouse["condition"] == "new"
    assert gaming_mouse["presta_categories"] == "203,206,343"

def test_missing_scenario(keyboard_data):
    """Test that accessing a non-existent scenario returns None."""
    missing_scenario = keyboard_data["scenarios"].get("NON EXISTENT KEYBOARD")
    assert missing_scenario is None
```