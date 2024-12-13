```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def load_json_data():
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_laptops_lenovo_thinkpad_p.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test to ensure the JSON data is loaded correctly
def test_json_data_loaded(load_json_data):
    """Verify that JSON data is loaded correctly and not empty."""
    data = load_json_data
    assert data is not None, "Data is None"
    assert isinstance(data, dict), "Data is not a dictionary"
    assert "scenarios" in data, "The key 'scenarios' is not in data"
    assert len(data["scenarios"]) > 0, "The 'scenarios' dictionary is empty"

# Test case for LENOVO  THINKPAD P 14 I5 scenario
def test_lenovo_thinkpad_p_14_i5_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO  THINKPAD P 14 I5' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO  THINKPAD P 14 I5")
    assert scenario is not None, "Scenario 'LENOVO  THINKPAD P 14 I5' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,104,10,5,378,838", "Incorrect presta_categories value"

# Test case for LENOVO  THINKPAD P 14 I7 scenario
def test_lenovo_thinkpad_p_14_i7_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO  THINKPAD P 14 I7' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO  THINKPAD P 14 I7")
    assert scenario is not None, "Scenario 'LENOVO  THINKPAD P 14 I7' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["url"] == "https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253274/253295", "Incorrect url"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,104,10,6,379,838", "Incorrect presta_categories value"

# Test case for LENOVO  THINKPAD P 14 I9 scenario
def test_lenovo_thinkpad_p_14_i9_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO  THINKPAD P 14 I9' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO  THINKPAD P 14 I9")
    assert scenario is not None, "Scenario 'LENOVO  THINKPAD P 14 I9' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,104,10,7,380,838", "Incorrect presta_categories value"


# Test case for LENOVO  THINKPAD P 14 AMD scenario
def test_lenovo_thinkpad_p_14_amd_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO  THINKPAD P 14 AMD' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO  THINKPAD P 14 AMD")
    assert scenario is not None, "Scenario 'LENOVO  THINKPAD P 14 AMD' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,104,10,234,381,838", "Incorrect presta_categories value"

# Test case for LENOVO   THINKPAD P 15 I5 scenario
def test_lenovo_thinkpad_p_15_i5_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO   THINKPAD P 15 I5' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO   THINKPAD P 15 I5")
    assert scenario is not None, "Scenario 'LENOVO   THINKPAD P 15 I5' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,105,11,5,385,838", "Incorrect presta_categories value"

# Test case for LENOVO   THINKPAD P 15 I7 scenario
def test_lenovo_thinkpad_p_15_i7_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO   THINKPAD P 15 I7' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO   THINKPAD P 15 I7")
    assert scenario is not None, "Scenario 'LENOVO   THINKPAD P 15 I7' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["url"] == "https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253274/253296", "Incorrect url"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,105,11,6,386,838", "Incorrect presta_categories value"

# Test case for LENOVO   THINKPAD P 15 I9 scenario
def test_lenovo_thinkpad_p_15_i9_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO   THINKPAD P 15 I9' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO   THINKPAD P 15 I9")
    assert scenario is not None, "Scenario 'LENOVO   THINKPAD P 15 I9' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["url"] == "https://www.visualdg.co.il/172327-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-P/253278/253296", "Incorrect url"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,105,11,7,387,838", "Incorrect presta_categories value"

# Test case for LENOVO   THINKPAD P 15 AMD scenario
def test_lenovo_thinkpad_p_15_amd_scenario(load_json_data):
    """Verify specific attributes for the 'LENOVO   THINKPAD P 15 AMD' scenario."""
    data = load_json_data
    scenario = data["scenarios"].get("LENOVO   THINKPAD P 15 AMD")
    assert scenario is not None, "Scenario 'LENOVO   THINKPAD P 15 AMD' not found"
    assert scenario["brand"] == "LENOVO", "Incorrect brand"
    assert scenario["template"] == "THINKPAD P", "Incorrect template"
    assert scenario["checkbox"] is False, "Incorrect checkbox value"
    assert scenario["active"] is True, "Incorrect active value"
    assert scenario["condition"] == "new", "Incorrect condition value"
    assert scenario["presta_categories"] == "3,53,105,11,234,388,838", "Incorrect presta_categories value"

# Test case for scenario with missing brand
def test_missing_brand_in_scenario(load_json_data):
    """Check behavior if a scenario is missing brand"""
    data = load_json_data
    # Create a scenario with a missing "brand" key
    data["scenarios"]["TEST_MISSING_BRAND"] = {
      "template": "TEST",
      "url": "test_url",
      "checkbox": False,
      "active": True,
      "condition":"new","presta_categories": "1,2,3"
    }
    scenario = data["scenarios"].get("TEST_MISSING_BRAND")
    assert scenario is not None, "Scenario 'TEST_MISSING_BRAND' not found"
    assert scenario.get("brand") is None, "The 'brand' key should be missing"
    assert scenario["template"] == "TEST", "Incorrect template"

# Test case for scenario with missing template
def test_missing_template_in_scenario(load_json_data):
    """Check behavior if a scenario is missing template"""
    data = load_json_data
    # Create a scenario with a missing "template" key
    data["scenarios"]["TEST_MISSING_TEMPLATE"] = {
      "brand": "TEST",
      "url": "test_url",
      "checkbox": False,
      "active": True,
      "condition":"new","presta_categories": "1,2,3"
    }
    scenario = data["scenarios"].get("TEST_MISSING_TEMPLATE")
    assert scenario is not None, "Scenario 'TEST_MISSING_TEMPLATE' not found"
    assert scenario.get("template") is None, "The 'template' key should be missing"
    assert scenario["brand"] == "TEST", "Incorrect brand"

# Test case for scenario with wrong type of checkbox
def test_wrong_type_checkbox_in_scenario(load_json_data):
    """Check behavior if a scenario has wrong type for checkbox"""
    data = load_json_data
    # Create a scenario with a wrong "checkbox" key
    data["scenarios"]["TEST_WRONG_CHECKBOX"] = {
      "brand": "TEST",
      "template": "TEST",
      "url": "test_url",
      "checkbox": "False",
      "active": True,
      "condition":"new","presta_categories": "1,2,3"
    }
    scenario = data["scenarios"].get("TEST_WRONG_CHECKBOX")
    assert scenario is not None, "Scenario 'TEST_WRONG_CHECKBOX' not found"
    assert isinstance(scenario["checkbox"], str), "The 'checkbox' should be a string"
    assert scenario["checkbox"] == "False", "Incorrect brand"
```