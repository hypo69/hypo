```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Loads the JSON data from the file."""
    file_location = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_psu_cooler_maser.json"
    with open(file_location, 'r') as f:
        return json.load(f)

# Test case for valid data structure
def test_valid_data_structure(json_data):
    """Checks that the JSON data has the expected structure: a dictionary with 'scenarios' key."""
    assert isinstance(json_data, dict), "The loaded data is not a dictionary."
    assert 'scenarios' in json_data, "The 'scenarios' key is missing from the data."
    assert isinstance(json_data['scenarios'], dict), "The 'scenarios' value is not a dictionary."

# Test case for individual scenario data validity
def test_valid_scenario_data(json_data):
    """Checks each scenario to ensure it has all the expected keys and correct data types."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' data is not a dictionary."
        assert 'brand' in scenario_data, f"Scenario '{scenario_name}' is missing 'brand' key."
        assert isinstance(scenario_data['brand'], str), f"Scenario '{scenario_name}' 'brand' value is not a string."
        assert 'name' in scenario_data, f"Scenario '{scenario_name}' is missing 'name' key."
        assert isinstance(scenario_data['name'], str), f"Scenario '{scenario_name}' 'name' value is not a string."
        assert 'url' in scenario_data, f"Scenario '{scenario_name}' is missing 'url' key."
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' 'url' value is not a string."
        assert 'checkbox' in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key."
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' 'checkbox' value is not a boolean."
        assert 'active' in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key."
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' 'active' value is not a boolean."
        assert 'condition' in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key."
        assert isinstance(scenario_data['condition'], str), f"Scenario '{scenario_name}' 'condition' value is not a string."
        assert 'presta_categories' in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key."
        assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' 'presta_categories' value is not a string."

# Test case for url format validation
def test_url_format_validation(json_data):
    """Checks if 'url' is a valid URL or a specific string as in the example."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
      url = scenario_data['url']
      if url.startswith("http"):
        assert url.startswith("https://www.morlevi.co.il/"), f"URL '{url}' in scenario '{scenario_name}' is not a valid Morlevi URL."
      else:
        assert "COOLER MASTER" in url, f"URL '{url}' in scenario '{scenario_name}' should contain 'COOLER MASTER' if not a URL"

# Test case for 'checkbox' values being boolean
def test_checkbox_type(json_data):
    """Checks that 'checkbox' values are always boolean."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data['checkbox'], bool), f"The 'checkbox' value for scenario '{scenario_name}' is not a boolean."

# Test case for 'active' values being boolean
def test_active_type(json_data):
    """Checks that 'active' values are always boolean."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data['active'], bool), f"The 'active' value for scenario '{scenario_name}' is not a boolean."

# Test case for 'presta_categories' being comma-separated strings
def test_presta_categories_format(json_data):
    """Checks if 'presta_categories' is a comma-separated string of numbers."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data['presta_categories']
        assert isinstance(presta_categories, str), f"The 'presta_categories' value for scenario '{scenario_name}' is not a string."
        categories = presta_categories.split(',')
        for cat in categories:
            assert cat.strip().isdigit(), f"'{cat}' in 'presta_categories' of scenario '{scenario_name}' is not a digit."

# Test case for 'condition' being a non-empty string
def test_condition_not_empty(json_data):
    """Checks if 'condition' is not an empty string."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
      condition = scenario_data['condition']
      assert isinstance(condition,str), f"The 'condition' value for scenario '{scenario_name}' is not a string."
      assert len(condition) > 0, f"The 'condition' value for scenario '{scenario_name}' is an empty string."

def test_scenario_names_are_strings(json_data):
    """Checks if all scenario names are strings"""
    scenarios = json_data["scenarios"]
    for scenario_name in scenarios.keys():
        assert isinstance(scenario_name, str), f"Scenario name {scenario_name} is not a string."

# Test case to ensure each scenario has at least one category
def test_each_scenario_has_at_least_one_category(json_data):
    """Checks that each scenario has at least one prestashop category associated with it."""
    scenarios = json_data['scenarios']
    for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data['presta_categories']
        categories = presta_categories.split(',')
        assert len(categories) >= 1, f"Scenario '{scenario_name}' has no categories."
```