```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Loads the JSON data from the specified file."""
    file_location = "hypotez/src/suppliers/cdata/scenarios/cdata_categories_aio_asus.json"
    with open(file_location, 'r') as f:
        return json.load(f)

def test_cdata_categories_data_structure(cdata_categories_data):
    """
    Checks if the loaded JSON data has the expected structure.
    It verifies the presence of the "scenarios" key and if its value is a dictionary.
    """
    assert "scenarios" in cdata_categories_data
    assert isinstance(cdata_categories_data["scenarios"], dict)

def test_cdata_categories_scenario_keys(cdata_categories_data):
    """
    Checks if each scenario within the "scenarios" dictionary contains the required keys.
    The required keys are "brand", "url", "checkbox", "active", "condition", and "presta_categories".
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data, f"Missing 'brand' key in scenario: {scenario_name}"
        assert "url" in scenario_data, f"Missing 'url' key in scenario: {scenario_name}"
        assert "checkbox" in scenario_data, f"Missing 'checkbox' key in scenario: {scenario_name}"
        assert "active" in scenario_data, f"Missing 'active' key in scenario: {scenario_name}"
        assert "condition" in scenario_data, f"Missing 'condition' key in scenario: {scenario_name}"
        assert "presta_categories" in scenario_data, f"Missing 'presta_categories' key in scenario: {scenario_name}"

def test_cdata_categories_scenario_values_type(cdata_categories_data):
     """
     Checks if the values within each scenario have the correct data type.
     - "brand": String
     - "url": String
     - "checkbox": Boolean
     - "active": Boolean
     - "condition": String
     - "presta_categories": String
     """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
          assert isinstance(scenario_data["brand"], str), f"Incorrect type for 'brand' in scenario: {scenario_name}"
          assert isinstance(scenario_data["url"], str), f"Incorrect type for 'url' in scenario: {scenario_name}"
          assert isinstance(scenario_data["checkbox"], bool), f"Incorrect type for 'checkbox' in scenario: {scenario_name}"
          assert isinstance(scenario_data["active"], bool), f"Incorrect type for 'active' in scenario: {scenario_name}"
          assert isinstance(scenario_data["condition"], str), f"Incorrect type for 'condition' in scenario: {scenario_name}"
          assert isinstance(scenario_data["presta_categories"], str), f"Incorrect type for 'presta_categories' in scenario: {scenario_name}"

def test_cdata_categories_brand_value(cdata_categories_data):
    """
    Verifies that the 'brand' value for all scenarios is "ASUS".
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "ASUS", f"Incorrect 'brand' value in scenario: {scenario_name}"

def test_cdata_categories_checkbox_value(cdata_categories_data):
    """
    Verifies that the 'checkbox' value for all scenarios is False.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
       assert scenario_data["checkbox"] == False, f"Incorrect 'checkbox' value in scenario: {scenario_name}"

def test_cdata_categories_active_value(cdata_categories_data):
    """
    Verifies that the 'active' value for all scenarios is True.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["active"] == True, f"Incorrect 'active' value in scenario: {scenario_name}"

def test_cdata_categories_condition_value(cdata_categories_data):
    """
    Verifies that the 'condition' value for all scenarios is 'new'.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
       assert scenario_data["condition"] == "new", f"Incorrect 'condition' value in scenario: {scenario_name}"


def test_cdata_categories_presta_categories_format(cdata_categories_data):
    """
    Verifies that the 'presta_categories' value is a string containing comma separated numbers
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        categories = scenario_data["presta_categories"].split(",")
        for category in categories:
            assert category.isdigit(), f"Incorrect 'presta_categories' value format in scenario: {scenario_name}"
```