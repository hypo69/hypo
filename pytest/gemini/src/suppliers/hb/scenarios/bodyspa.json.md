```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def bodyspa_data():
    """Loads the bodyspa.json data."""
    with open("hypotez/src/suppliers/hb/scenarios/bodyspa.json", 'r') as f:
        return json.load(f)

# Test to check if the 'scenarios' key exists
def test_scenarios_key_exists(bodyspa_data):
    """Checks if the 'scenarios' key exists in the data."""
    assert "scenarios" in bodyspa_data, "The 'scenarios' key is missing."

# Test to check if scenarios is a dictionary
def test_scenarios_is_dict(bodyspa_data):
    """Checks if 'scenarios' is a dictionary."""
    assert isinstance(bodyspa_data["scenarios"], dict), "The 'scenarios' value is not a dictionary."


# Test to check the structure of each scenario
def test_scenario_structure(bodyspa_data):
    """Checks the structure of each scenario within the 'scenarios' dictionary."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        assert "url" in scenario_data, f"Missing 'url' in scenario: {scenario_name}"
        assert "name" in scenario_data, f"Missing 'name' in scenario: {scenario_name}"
        assert "condition" in scenario_data, f"Missing 'condition' in scenario: {scenario_name}"
        assert "presta_categories" in scenario_data, f"Missing 'presta_categories' in scenario: {scenario_name}"

        assert isinstance(scenario_data["url"], str), f"'url' is not a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["name"], str), f"'name' is not a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["condition"], str), f"'condition' is not a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["presta_categories"], dict), f"'presta_categories' is not a dictionary in scenario: {scenario_name}"

# Test to check 'url' field is not empty
def test_scenario_url_not_empty(bodyspa_data):
    """Checks if 'url' field is not an empty string."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        assert scenario_data["url"], f"'url' is empty in scenario: {scenario_name}"

# Test to check 'name' field is not empty
def test_scenario_name_not_empty(bodyspa_data):
    """Checks if 'name' field is not an empty string."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        assert scenario_data["name"], f"'name' is empty in scenario: {scenario_name}"

# Test to check 'condition' field is not empty
def test_scenario_condition_not_empty(bodyspa_data):
    """Checks if 'condition' field is not an empty string."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
       assert scenario_data["condition"], f"'condition' is empty in scenario: {scenario_name}"

# Test to check 'presta_categories' structure
def test_presta_categories_structure(bodyspa_data):
    """Checks the structure of 'presta_categories' within each scenario."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert "default_category" in presta_categories, f"Missing 'default_category' in scenario: {scenario_name}"
        assert "additional_categories" in presta_categories, f"Missing 'additional_categories' in scenario: {scenario_name}"
        assert isinstance(presta_categories["default_category"], int), f"'default_category' is not an integer in scenario: {scenario_name}"
        assert isinstance(presta_categories["additional_categories"], list), f"'additional_categories' is not a list in scenario: {scenario_name}"


# Test to check that "default_category" is an int
def test_default_category_is_int(bodyspa_data):
    """Checks if default_category is an integer."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
         assert isinstance(scenario_data["presta_categories"]["default_category"],int), f"default_category is not an integer in {scenario_name}"

# Test to check that "additional_categories" is a list
def test_additional_categories_is_list(bodyspa_data):
    """Checks if additional_categories is a list."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"]["additional_categories"], list), f"additional_categories is not a list in {scenario_name}"

#Test if condition field has only 'new' as value
def test_condition_field_value(bodyspa_data):
    """Checks if condition field has only 'new' as value"""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"'condition' field should be 'new' in scenario: {scenario_name}"

# Test for empty additional_categories list (edge case)
def test_additional_categories_empty(bodyspa_data):
    """Checks if 'additional_categories' is an empty list, which is acceptable."""
    for scenario_name, scenario_data in bodyspa_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"]["additional_categories"], list),f"'additional_categories' must be a list: {scenario_name}"
        # Additional check: It's OK for additional_categories to be empty, as specified in the JSON structure
        # If we wanted to explicitly verify it's empty, uncomment this line:
        # assert not scenario_data["presta_categories"]["additional_categories"],f"'additional_categories' should be an empty list: {scenario_name}"
```