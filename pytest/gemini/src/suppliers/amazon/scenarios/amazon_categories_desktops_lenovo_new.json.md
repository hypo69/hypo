```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_data():
    """Loads the amazon data from the json file."""
    file_location = "hypotez/src/suppliers/amazon/scenarios/amazon_categories_desktops_lenovo_new.json"
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

# Test to check if the data is loaded correctly
def test_amazon_data_loaded(amazon_data):
    """Checks if the amazon data is loaded correctly from the json file."""
    assert isinstance(amazon_data, dict)
    assert "scenarios" in amazon_data
    assert isinstance(amazon_data["scenarios"], dict)

# Test case for NEW LENOVO DESKTOP INTEL I3 scenario
def test_new_lenovo_desktop_intel_i3(amazon_data):
    """Checks the properties of the 'NEW LENOVO DESKTOP INTEL I3' scenario."""
    scenario = amazon_data["scenarios"].get("NEW LENOVO DESKTOP INTEL I3")
    assert scenario is not None
    assert scenario["brand"] == "LENOVO"
    assert scenario["url"].startswith("https://www.amazon.com/")
    assert scenario["active"] is True
    assert scenario["condition"] == "new"
    assert "template" in scenario["presta_categories"]
    assert scenario["presta_categories"]["template"]["lenovo"] == "DESKTOPS INTEL I3"
    assert scenario["checkbox"] is False
    assert scenario["price_rule"] == 1

# Test case for NEW LENOVO DESKTOP INTEL I5 scenario
def test_new_lenovo_desktop_intel_i5(amazon_data):
    """Checks the properties of the 'NEW LENOVO DESKTOP INTEL I5' scenario."""
    scenario = amazon_data["scenarios"].get("NEW LENOVO DESKTOP INTEL I5")
    assert scenario is not None
    assert scenario["brand"] == "LENOVO"
    assert scenario["url"].startswith("https://www.amazon.com/")
    assert scenario["active"] is True
    assert scenario["condition"] == "new"
    assert "template" in scenario["presta_categories"]
    assert scenario["presta_categories"]["template"]["lenovo"] == "DESKTOPS INTEL I5"
    assert scenario["checkbox"] is False
    assert scenario["price_rule"] == 1

# Test case for NEW LENOVO DESKTOP INTEL I7 scenario
def test_new_lenovo_desktop_intel_i7(amazon_data):
    """Checks the properties of the 'NEW LENOVO DESKTOP INTEL I7' scenario."""
    scenario = amazon_data["scenarios"].get("NEW LENOVO DESKTOP INTEL I7")
    assert scenario is not None
    assert scenario["brand"] == "LENOVO"
    assert scenario["url"].startswith("https://www.amazon.com/")
    assert scenario["active"] is True
    assert scenario["condition"] == "new"
    assert "template" in scenario["presta_categories"]
    assert scenario["presta_categories"]["template"]["lenovo"] == "DESKTOPS INTEL I7"
    assert scenario["checkbox"] is False
    assert scenario["price_rule"] == 1

# Test case for NEW LENOVO DESKTOP INTEL I9 scenario
def test_new_lenovo_desktop_intel_i9(amazon_data):
    """Checks the properties of the 'NEW LENOVO DESKTOP INTEL I9' scenario."""
    scenario = amazon_data["scenarios"].get("NEW LENOVO DESKTOP INTEL I9")
    assert scenario is not None
    assert scenario["brand"] == "LENOVO"
    assert scenario["url"].startswith("https://www.amazon.com/")
    assert scenario["active"] is True
    assert scenario["condition"] == "new"
    assert "template" in scenario["presta_categories"]
    assert scenario["presta_categories"]["template"]["lenovo"] == "DESKTOPS INTEL I9"
    assert scenario["checkbox"] is False
    assert scenario["price_rule"] == 1
    
# Test case for NEW LENOVO DESKTOP AMD RYZEN 3 scenario
def test_new_lenovo_desktop_amd_ryzen_3(amazon_data):
    """Checks the properties of the 'NEW LENOVO DESKTOP AMD RYZEN 3' scenario."""
    scenario = amazon_data["scenarios"].get("NEW LENOVO DESKTOP AMD RYZEN 3")
    assert scenario is not None
    assert scenario["brand"] == "LENOVO"
    assert scenario["url"].startswith("https://www.amazon.com/")
    assert scenario["active"] is True
    assert scenario["condition"] == "new"
    assert "template" in scenario["presta_categories"]
    assert scenario["presta_categories"]["template"]["lenovo"] == "DESKTOPS AMD RYZEN 3"
    assert scenario["checkbox"] is False
    assert scenario["price_rule"] == 1

# Test case for missing scenario
def test_missing_scenario(amazon_data):
    """Checks that a missing scenario is handled correctly."""
    scenario = amazon_data["scenarios"].get("MISSING_SCENARIO")
    assert scenario is None
```