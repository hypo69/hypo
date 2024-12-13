```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides test data loaded from the JSON file."""
    file_location = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_keyboards_microsoft.json"
    with open(file_location, 'r') as f:
        return json.load(f)

# Test case for checking if the 'scenarios' key exists
def test_scenarios_key_exists(json_data):
    """Checks if the 'scenarios' key exists in the loaded JSON data."""
    assert "scenarios" in json_data, "The 'scenarios' key is missing from the JSON data."

# Test case for checking if there are scenarios in the JSON
def test_scenarios_not_empty(json_data):
    """Checks if the 'scenarios' dictionary is not empty."""
    assert json_data["scenarios"], "The 'scenarios' dictionary is empty."

# Test case for checking specific fields in the first scenario
def test_first_scenario_fields(json_data):
    """Checks if the fields in the first scenario are correct."""
    first_scenario = list(json_data["scenarios"].values())[0]
    assert "brand" in first_scenario, "The 'brand' key is missing from the scenario."
    assert "url" in first_scenario, "The 'url' key is missing from the scenario."
    assert "checkbox" in first_scenario, "The 'checkbox' key is missing from the scenario."
    assert "active" in first_scenario, "The 'active' key is missing from the scenario."
    assert "condition" in first_scenario, "The 'condition' key is missing from the scenario."
    assert "presta_categories" in first_scenario, "The 'presta_categories' key is missing from the scenario."
    
    assert first_scenario["brand"] == "MICROSOFT", "The 'brand' value is incorrect."
    assert first_scenario["checkbox"] == False, "The 'checkbox' value is incorrect."
    assert first_scenario["active"] == True, "The 'active' value is incorrect."
    assert first_scenario["condition"] == "new", "The 'condition' value is incorrect."


# Test case for checking specific fields in the last scenario
def test_last_scenario_fields(json_data):
    """Checks if the fields in the last scenario are correct."""
    last_scenario = list(json_data["scenarios"].values())[-1]
    assert "brand" in last_scenario, "The 'brand' key is missing from the scenario."
    assert "url" in last_scenario, "The 'url' key is missing from the scenario."
    assert "checkbox" in last_scenario, "The 'checkbox' key is missing from the scenario."
    assert "active" in last_scenario, "The 'active' key is missing from the scenario."
    assert "condition" in last_scenario, "The 'condition' key is missing from the scenario."
    assert "presta_categories" in last_scenario, "The 'presta_categories' key is missing from the scenario."

    assert last_scenario["brand"] == "MICROSOFT", "The 'brand' value is incorrect."
    assert last_scenario["checkbox"] == False, "The 'checkbox' value is incorrect."
    assert last_scenario["active"] == True, "The 'active' value is incorrect."
    assert last_scenario["condition"] == "new", "The 'condition' value is incorrect."

# Test case for checking the type of 'presta_categories' field
def test_presta_categories_type(json_data):
    """Checks if the 'presta_categories' is a string."""
    for scenario in json_data["scenarios"].values():
        assert isinstance(scenario["presta_categories"], str), "The 'presta_categories' is not a string."

# Test case for checking the type of 'active' field
def test_active_field_type(json_data):
    """Checks if the 'active' field is a boolean."""
    for scenario in json_data["scenarios"].values():
        assert isinstance(scenario["active"], bool), "The 'active' field is not a boolean."

# Test case for checking the type of 'checkbox' field
def test_checkbox_field_type(json_data):
    """Checks if the 'checkbox' field is a boolean."""
    for scenario in json_data["scenarios"].values():
          assert isinstance(scenario["checkbox"], bool), "The 'checkbox' field is not a boolean."

# Test case for checking that all urls are strings
def test_url_field_type(json_data):
    """Checks if the 'url' field is a string."""
    for scenario in json_data["scenarios"].values():
        assert isinstance(scenario["url"], str), "The 'url' field is not a string."

# Test case for checking that all brands are strings
def test_brand_field_type(json_data):
    """Checks if the 'brand' field is a string."""
    for scenario in json_data["scenarios"].values():
        assert isinstance(scenario["brand"], str), "The 'brand' field is not a string."

# Test case for checking that all conditions are strings
def test_condition_field_type(json_data):
    """Checks if the 'condition' field is a string."""
    for scenario in json_data["scenarios"].values():
        assert isinstance(scenario["condition"], str), "The 'condition' field is not a string."
```