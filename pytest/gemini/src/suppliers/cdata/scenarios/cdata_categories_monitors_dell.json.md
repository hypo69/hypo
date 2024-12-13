```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_monitors_dell_data():
    """Loads the JSON data for testing."""
    file_path = "hypotez/src/suppliers/cdata/scenarios/cdata_categories_monitors_dell.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test to check if the JSON data is loaded correctly
def test_json_data_loaded(cdata_categories_monitors_dell_data):
    """
    Test that the JSON data is loaded and is a dictionary.
    """
    assert isinstance(cdata_categories_monitors_dell_data, dict)
    assert "scenarios" in cdata_categories_monitors_dell_data

# Test to verify the structure of each scenario
def test_scenario_structure(cdata_categories_monitors_dell_data):
    """
    Test each scenario in the JSON data
    to ensure they have the correct keys (brand, url, checkbox, active, condition, presta_categories).
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' data is not a dictionary."
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key."

# Test to check the 'brand' value in each scenario
def test_scenario_brand_value(cdata_categories_monitors_dell_data):
    """
    Test that the 'brand' value in all scenarios is 'DELL'.
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("brand") == "DELL", f"Scenario '{scenario_name}' has incorrect brand: {scenario_data.get('brand')}"

# Test to check that 'url' is a string for each scenario
def test_scenario_url_type(cdata_categories_monitors_dell_data):
    """
    Test that the 'url' value in all scenarios is a string.
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("url"), str), f"Scenario '{scenario_name}' has incorrect url type: {type(scenario_data.get('url'))}"

# Test to verify 'checkbox' is a boolean
def test_scenario_checkbox_type(cdata_categories_monitors_dell_data):
    """
    Test that the 'checkbox' value in all scenarios is a boolean.
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("checkbox"), bool), f"Scenario '{scenario_name}' has incorrect checkbox type: {type(scenario_data.get('checkbox'))}"

# Test to verify 'active' is a boolean
def test_scenario_active_type(cdata_categories_monitors_dell_data):
    """
    Test that the 'active' value in all scenarios is a boolean.
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("active"), bool), f"Scenario '{scenario_name}' has incorrect active type: {type(scenario_data.get('active'))}"

# Test to verify 'condition' is a string
def test_scenario_condition_type(cdata_categories_monitors_dell_data):
   """
   Test that the 'condition' value in all scenarios is a string.
   """
   scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
   for scenario_name, scenario_data in scenarios.items():
       assert isinstance(scenario_data.get("condition"), str), f"Scenario '{scenario_name}' has incorrect condition type: {type(scenario_data.get('condition'))}"

# Test to verify 'presta_categories' is a string
def test_scenario_presta_categories_type(cdata_categories_monitors_dell_data):
    """
    Test that the 'presta_categories' value in all scenarios is a string.
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("presta_categories"), str), f"Scenario '{scenario_name}' has incorrect presta_categories type: {type(scenario_data.get('presta_categories'))}"

# Test to check 'active' is always true
def test_scenario_active_true(cdata_categories_monitors_dell_data):
    """
    Test that the 'active' value in all scenarios is True
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("active") == True, f"Scenario '{scenario_name}' has incorrect active value: {scenario_data.get('active')}"

# Test to check 'checkbox' is always false
def test_scenario_checkbox_false(cdata_categories_monitors_dell_data):
    """
    Test that the 'checkbox' value in all scenarios is False
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("checkbox") == False, f"Scenario '{scenario_name}' has incorrect checkbox value: {scenario_data.get('checkbox')}"

# Test to check 'condition' is always new
def test_scenario_condition_new(cdata_categories_monitors_dell_data):
    """
    Test that the 'condition' value in all scenarios is 'new'
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("condition") == "new", f"Scenario '{scenario_name}' has incorrect condition value: {scenario_data.get('condition')}"

# Test specific scenario URL for the "DELL 49" case, as it is a string of dashes.
def test_scenario_dell_49_url(cdata_categories_monitors_dell_data):
   """
   Test that the 'url' value in the 'DELL 49' scenario is a specific string.
   """
   scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
   dell_49_scenario = scenarios.get("DELL 49")
   assert dell_49_scenario is not None, "Scenario 'DELL 49' not found."
   expected_url = "---------------------DELL 49----------------------"
   assert dell_49_scenario.get("url") == expected_url, f"Scenario 'DELL 49' has incorrect url: {dell_49_scenario.get('url')}"

# Test for all scenarios to have presta_categories as string with comma separated values
def test_scenario_presta_categories_format(cdata_categories_monitors_dell_data):
    """
    Test that the 'presta_categories' value in all scenarios
    is a string that contains at least one comma and the values are numeric.
    """
    scenarios = cdata_categories_monitors_dell_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data.get("presta_categories")
        assert isinstance(presta_categories, str), f"Scenario '{scenario_name}' has incorrect presta_categories type: {type(presta_categories)}"
        assert "," in presta_categories, f"Scenario '{scenario_name}' has incorrect format for presta_categories, missing comma: {presta_categories}"
        categories = presta_categories.split(',')
        for category in categories:
            assert category.isdigit(), f"Scenario '{scenario_name}' has non-numeric category: {category} in {presta_categories}"
```