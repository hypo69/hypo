```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_storage_crucial.json data."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_storage_crucial.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test to check if the loaded data is a dictionary
def test_data_is_dict(morlevi_categories_data):
    """Checks if the loaded JSON data is a dictionary."""
    assert isinstance(morlevi_categories_data, dict), "Loaded data should be a dictionary."

# Test to check if the "scenarios" key exists
def test_scenarios_key_exists(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the loaded JSON data."""
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key should exist in the data."

# Test to check if the "scenarios" value is a dictionary
def test_scenarios_value_is_dict(morlevi_categories_data):
    """Checks if the value of the 'scenarios' key is a dictionary."""
    assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."

# Test for a valid scenario, checking several fields.
def test_valid_scenario_internal_ssd_sata_3_256(morlevi_categories_data):
    """Checks a valid scenario with several fields."""
    scenario = morlevi_categories_data["scenarios"].get("internal_ssd_sata_3 240-256GB")
    assert scenario is not None, "Scenario 'internal_ssd_sata_3 240-256GB' should exist."
    assert scenario.get("brand") == "CRUCIAL", "Brand should be 'CRUCIAL'."
    assert scenario.get("name") == "internal_ssd_sata_3_256", "Name should be 'internal_ssd_sata_3_256'."
    assert scenario.get("active") is True, "Active should be True."
    assert scenario.get("condition") == "new", "Condition should be 'new'."
    assert scenario.get("presta_categories") == "117,118,135", "Presta categories should be '117,118,135'."

# Test to check for the presence of a specific URL
def test_url_internal_ssd_nvmi_256(morlevi_categories_data):
    """Checks the presence of a specific URL for a scenario."""
    scenario = morlevi_categories_data["scenarios"].get("internal_ssd_nvmi 240-256GB")
    assert scenario is not None, "Scenario 'internal_ssd_nvmi 240-256GB' should exist."
    assert scenario.get("url") == "https://www.morlevi.co.il/Cat/51?p_315=19&p_175=823&sort=datafloat2%2Cprice&keyword=", "URL should match."

# Test to check for 'checkbox' field
def test_checkbox_false_value(morlevi_categories_data):
     """Checks the value of the 'checkbox' field is False for all scenarios."""
     scenarios = morlevi_categories_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
         assert scenario_data.get("checkbox") is False, f"Checkbox value should be False for {scenario_name}"

# Test to check if all scenarios have a "brand" field.
def test_all_scenarios_have_brand(morlevi_categories_data):
    """Checks if all scenarios have the 'brand' field."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' should have a 'brand' field."

# Test to check for the absence of a scenario with wrong name
def test_invalid_scenario_name(morlevi_categories_data):
    """Checks for the absence of a scenario with a wrong name."""
    scenario = morlevi_categories_data["scenarios"].get("non_existent_scenario")
    assert scenario is None, "Scenario 'non_existent_scenario' should not exist."

# Test to check if all scenarios have an "active" field
def test_all_scenarios_have_active(morlevi_categories_data):
    """Checks if all scenarios have an 'active' field set to True."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert "active" in scenario_data, f"Scenario '{scenario_name}' should have an 'active' field."
         assert scenario_data.get("active") is True, f"Scenario '{scenario_name}' active field should be True"

#Test to check if all scenarios have 'condition' field
def test_all_scenarios_have_condition(morlevi_categories_data):
    """Checks if all scenarios have the 'condition' field with value 'new'."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' should have a 'condition' field."
        assert scenario_data.get("condition") == "new", f"Scenario '{scenario_name}' condition should be 'new'."

# Test to check for the presence of "presta_categories" field
def test_all_scenarios_have_presta_categories(morlevi_categories_data):
    """Checks if all scenarios have a 'presta_categories' field."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' should have a 'presta_categories' field."

#Test to check if the presta_categories is a string
def test_presta_categories_is_string(morlevi_categories_data):
    """Checks if the 'presta_categories' field is a string for all scenarios."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data.get("presta_categories")
        assert isinstance(presta_categories, str), f"'presta_categories' for {scenario_name} should be a string."

# Test to check if all the scenarios have the "name" field
def test_all_scenarios_have_name(morlevi_categories_data):
    """Checks if all scenarios have a 'name' field."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert "name" in scenario_data, f"Scenario '{scenario_name}' should have a 'name' field."
```