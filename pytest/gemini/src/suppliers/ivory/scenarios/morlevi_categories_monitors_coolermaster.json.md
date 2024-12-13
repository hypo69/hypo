```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the JSON data from the specified file."""
    file_location = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_monitors_coolermaster.json'
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

# Test to ensure the data is loaded correctly
def test_data_loaded(morlevi_data):
    """Checks if the fixture correctly loads the data."""
    assert morlevi_data is not None, "Data loading failed"
    assert "scenarios" in morlevi_data, "The key 'scenarios' is missing"

# Test for valid scenario entries
def test_valid_scenario_entries(morlevi_data):
    """
    Checks if each scenario has the necessary keys and valid values for 'brand',
    'url', 'checkbox', 'active', 'condition' and 'presta_categories'.
    """
    scenarios = morlevi_data.get("scenarios", {})
    assert scenarios, "No scenarios found in data"
    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' is missing 'brand'"
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}': 'brand' must be a string"
        
        assert "url" in scenario_data, f"Scenario '{scenario_name}' is missing 'url'"
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}': 'url' must be a string"
        
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox'"
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}': 'checkbox' must be a boolean"
        
        assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active'"
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}': 'active' must be a boolean"

        assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition'"
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}': 'condition' must be a string"

        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories'"
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}': 'presta_categories' must be a string"


# Test to verify all URLs are strings
def test_url_is_string(morlevi_data):
    """Verifies that each scenario's 'url' value is a string."""
    scenarios = morlevi_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
       assert isinstance(scenario_data.get("url"), str), f"Scenario '{scenario_name}' has non-string url: {scenario_data.get('url')}"

# Test to ensure 'checkbox' is a boolean
def test_checkbox_is_boolean(morlevi_data):
    """Verifies that each scenario's 'checkbox' value is a boolean."""
    scenarios = morlevi_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("checkbox"), bool), f"Scenario '{scenario_name}' has non-boolean checkbox: {scenario_data.get('checkbox')}"

# Test to ensure 'active' is a boolean
def test_active_is_boolean(morlevi_data):
    """Verifies that each scenario's 'active' value is a boolean."""
    scenarios = morlevi_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("active"), bool), f"Scenario '{scenario_name}' has non-boolean active: {scenario_data.get('active')}"

# Test to verify 'condition' is a string
def test_condition_is_string(morlevi_data):
    """Verifies that each scenario's 'condition' value is a string."""
    scenarios = morlevi_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("condition"), str), f"Scenario '{scenario_name}' has non-string condition: {scenario_data.get('condition')}"

# Test to verify 'presta_categories' is a string
def test_presta_categories_is_string(morlevi_data):
        """Verifies that each scenario's 'presta_categories' value is a string."""
        scenarios = morlevi_data.get("scenarios", {})
        for scenario_name, scenario_data in scenarios.items():
            assert isinstance(scenario_data.get("presta_categories"), str), f"Scenario '{scenario_name}' has non-string presta_categories: {scenario_data.get('presta_categories')}"

# Test for scenarios with empty URLs
def test_empty_urls(morlevi_data):
     """Verifies that there are no scenarios with empty URLs."""
     scenarios = morlevi_data.get("scenarios", {})
     for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("url"), f"Scenario '{scenario_name}' has an empty url"

# Test for scenarios with empty brand
def test_empty_brand(morlevi_data):
     """Verifies that there are no scenarios with empty brands."""
     scenarios = morlevi_data.get("scenarios", {})
     for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("brand"), f"Scenario '{scenario_name}' has an empty brand"

# Test for scenarios with empty condition
def test_empty_condition(morlevi_data):
     """Verifies that there are no scenarios with empty condition."""
     scenarios = morlevi_data.get("scenarios", {})
     for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("condition"), f"Scenario '{scenario_name}' has an empty condition"

# Test for scenarios with empty presta_categories
def test_empty_presta_categories(morlevi_data):
     """Verifies that there are no scenarios with empty presta_categories."""
     scenarios = morlevi_data.get("scenarios", {})
     for scenario_name, scenario_data in scenarios.items():
        assert scenario_data.get("presta_categories"), f"Scenario '{scenario_name}' has an empty presta_categories"
```