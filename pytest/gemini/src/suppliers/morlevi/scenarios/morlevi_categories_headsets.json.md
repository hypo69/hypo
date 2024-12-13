```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_headsets_data():
    """Loads the JSON data from the specified file."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_headsets.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test case for checking if the 'scenarios' key exists
def test_scenarios_key_exists(morlevi_categories_headsets_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert "scenarios" in morlevi_categories_headsets_data, "The 'scenarios' key is missing from the JSON data."

# Test case for verifying the structure of each scenario
def test_scenario_structure(morlevi_categories_headsets_data):
    """Verifies the structure of each scenario within the 'scenarios' dictionary."""
    scenarios = morlevi_categories_headsets_data.get("scenarios")
    assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
    
    for scenario_key, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_key}' is not a dictionary."
        assert "brand" in scenario_data, f"Scenario '{scenario_key}' is missing the 'brand' key."
        assert "template" in scenario_data, f"Scenario '{scenario_key}' is missing the 'template' key."
        assert "url" in scenario_data, f"Scenario '{scenario_key}' is missing the 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_key}' is missing the 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_key}' is missing the 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_key}' is missing the 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_key}' is missing the 'presta_categories' key."
        
        presta_categories = scenario_data.get("presta_categories")
        assert isinstance(presta_categories, dict), f"The 'presta_categories' for scenario '{scenario_key}' is not a dictionary."
        assert "template" in presta_categories, f"The 'template' key is missing from 'presta_categories' for scenario '{scenario_key}'."
        
        template_data = presta_categories.get("template")
        assert isinstance(template_data, dict), f"The 'template' in 'presta_categories' for scenario '{scenario_key}' is not a dictionary."
        assert len(template_data) > 0, f"The 'template' dictionary in 'presta_categories' for scenario '{scenario_key}' is empty."

# Test case for validating the data types in each scenario
def test_scenario_data_types(morlevi_categories_headsets_data):
    """Validates the data types for each key in the scenarios."""
    scenarios = morlevi_categories_headsets_data.get("scenarios")
    assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
    
    for scenario_key, scenario_data in scenarios.items():
        assert isinstance(scenario_data.get("brand"), str), f"The 'brand' for scenario '{scenario_key}' is not a string."
        assert isinstance(scenario_data.get("template"), str), f"The 'template' for scenario '{scenario_key}' is not a string."
        assert isinstance(scenario_data.get("url"), str), f"The 'url' for scenario '{scenario_key}' is not a string."
        assert isinstance(scenario_data.get("checkbox"), bool), f"The 'checkbox' for scenario '{scenario_key}' is not a boolean."
        assert isinstance(scenario_data.get("active"), bool), f"The 'active' for scenario '{scenario_key}' is not a boolean."
        assert isinstance(scenario_data.get("condition"), str), f"The 'condition' for scenario '{scenario_key}' is not a string."
        
        presta_categories = scenario_data.get("presta_categories")
        template_data = presta_categories.get("template")
        for template_key, template_value in template_data.items():
            assert isinstance(template_key, str), f"The 'template' key in 'presta_categories' for scenario '{scenario_key}' is not a string."
            assert isinstance(template_value, str), f"The 'template' value in 'presta_categories' for scenario '{scenario_key}' is not a string."


# Test case to check if all URLs are strings and are not empty
def test_url_validity(morlevi_categories_headsets_data):
      """Checks that all URLs are strings and are not empty."""
      scenarios = morlevi_categories_headsets_data.get("scenarios")
      assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
      for scenario_key, scenario_data in scenarios.items():
        url = scenario_data.get("url")
        assert isinstance(url, str), f"URL for scenario '{scenario_key}' is not a string."
        assert url, f"URL for scenario '{scenario_key}' is empty."

# Test case to check if all brand names are strings and are not empty
def test_brand_validity(morlevi_categories_headsets_data):
      """Checks that all brand names are strings and are not empty."""
      scenarios = morlevi_categories_headsets_data.get("scenarios")
      assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
      for scenario_key, scenario_data in scenarios.items():
        brand = scenario_data.get("brand")
        assert isinstance(brand, str), f"Brand for scenario '{scenario_key}' is not a string."
        assert brand, f"Brand for scenario '{scenario_key}' is empty."

# Test case to check if all template names are strings and are not empty
def test_template_validity(morlevi_categories_headsets_data):
      """Checks that all template names are strings and are not empty."""
      scenarios = morlevi_categories_headsets_data.get("scenarios")
      assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
      for scenario_key, scenario_data in scenarios.items():
        template = scenario_data.get("template")
        assert isinstance(template, str), f"Template for scenario '{scenario_key}' is not a string."
        assert template, f"Template for scenario '{scenario_key}' is empty."

# Test case to check if all condition values are strings and are not empty
def test_condition_validity(morlevi_categories_headsets_data):
      """Checks that all condition values are strings and are not empty."""
      scenarios = morlevi_categories_headsets_data.get("scenarios")
      assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
      for scenario_key, scenario_data in scenarios.items():
        condition = scenario_data.get("condition")
        assert isinstance(condition, str), f"Condition for scenario '{scenario_key}' is not a string."
        assert condition, f"Condition for scenario '{scenario_key}' is empty."

# Test case to check if all Prestashop category template values are strings and not empty
def test_presta_template_validity(morlevi_categories_headsets_data):
    """Checks that all Prestashop category template values are strings and not empty."""
    scenarios = morlevi_categories_headsets_data.get("scenarios")
    assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
    for scenario_key, scenario_data in scenarios.items():
        presta_categories = scenario_data.get("presta_categories")
        template_data = presta_categories.get("template")
        for template_key, template_value in template_data.items():
             assert isinstance(template_value, str), f"Prestashop category template value for scenario '{scenario_key}' is not a string."
             assert template_value, f"Prestashop category template value for scenario '{scenario_key}' is empty."

# Test case to check if all Prestashop category template keys are strings and not empty
def test_presta_template_keys_validity(morlevi_categories_headsets_data):
    """Checks that all Prestashop category template keys are strings and not empty."""
    scenarios = morlevi_categories_headsets_data.get("scenarios")
    assert scenarios is not None, "The 'scenarios' key is missing from the JSON data."
    for scenario_key, scenario_data in scenarios.items():
        presta_categories = scenario_data.get("presta_categories")
        template_data = presta_categories.get("template")
        for template_key, template_value in template_data.items():
             assert isinstance(template_key, str), f"Prestashop category template key for scenario '{scenario_key}' is not a string."
             assert template_key, f"Prestashop category template key for scenario '{scenario_key}' is empty."
```