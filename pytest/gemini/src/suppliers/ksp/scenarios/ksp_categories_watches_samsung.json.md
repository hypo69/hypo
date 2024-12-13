```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_watches_samsung_data():
    """Loads the JSON data for testing."""
    file_path = 'hypotez/src/suppliers/ksp/scenarios/ksp_categories_watches_samsung.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test to check if the JSON file loads correctly and has the 'scenarios' key
def test_json_file_loads_correctly(ksp_categories_watches_samsung_data):
    """Checks if the JSON file is loaded and contains the 'scenarios' key."""
    assert "scenarios" in ksp_categories_watches_samsung_data
    assert isinstance(ksp_categories_watches_samsung_data["scenarios"], dict)


# Test to verify structure of a single scenario, especially properties
def test_scenario_structure(ksp_categories_watches_samsung_data):
    """Checks that each scenario has the required keys and valid types."""
    scenarios = ksp_categories_watches_samsung_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' is not a dictionary."
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand'."
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' is not a string."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url'."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' is not a string."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox'."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active'."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' is not a boolean."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition'."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' is not a string."

        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories'."
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' is not a dict."

# Test to check the 'brand' values. 
def test_scenario_brand_value(ksp_categories_watches_samsung_data):
    """Checks if brand is correct"""
    scenarios = ksp_categories_watches_samsung_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["brand"] == "SAMSUNG", f"Scenario '{scenario_name}' brand is not SAMSUNG."


# Test to check that URLs are strings and non-empty.
def test_scenario_url_valid(ksp_categories_watches_samsung_data):
    """Checks if URL is a string and non-empty"""
    scenarios = ksp_categories_watches_samsung_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url is not string."
        assert scenario_data["url"], f"Scenario '{scenario_name}' url is empty."


# Test to check if 'checkbox' field is always false
def test_checkbox_always_false(ksp_categories_watches_samsung_data):
    """Checks if the checkbox field is always false."""
    scenarios = ksp_categories_watches_samsung_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' checkbox is not False."

# Test to check if 'active' field is always true
def test_active_always_true(ksp_categories_watches_samsung_data):
    """Checks if the active field is always true."""
    scenarios = ksp_categories_watches_samsung_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["active"] == True, f"Scenario '{scenario_name}' active is not True."

# Test to check 'condition' value is always 'new'
def test_condition_always_new(ksp_categories_watches_samsung_data):
      """Checks if condition field is always set to new."""
      scenarios = ksp_categories_watches_samsung_data["scenarios"]
      for scenario_name, scenario_data in scenarios.items():
            assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' condition is not new."

# Test to verify structure of presta_categories
def test_presta_categories_structure(ksp_categories_watches_samsung_data):
      """Checks if presta_categories is a dict and contains specific key-value pairs."""
      scenarios = ksp_categories_watches_samsung_data["scenarios"]
      for scenario_name, scenario_data in scenarios.items():
          presta_categories = scenario_data["presta_categories"]
          assert isinstance(presta_categories, dict), f"Scenario '{scenario_name}' presta_categories is not a dict."
          assert "3405" in presta_categories , f"Scenario '{scenario_name}' presta_categories is missing key 3405."
          assert "3198" in presta_categories, f"Scenario '{scenario_name}' presta_categories is missing key 3198."
          assert "3202" in presta_categories, f"Scenario '{scenario_name}' presta_categories is missing key 3202."
          assert "6471" in presta_categories, f"Scenario '{scenario_name}' presta_categories is missing key 6471."
          assert "3403" in presta_categories, f"Scenario '{scenario_name}' presta_categories is missing key 3403."

          assert presta_categories["3405"] == "GOOGLE PIXEL PRO", f"Scenario '{scenario_name}' presta_categories key 3405 has wrong value"
          assert presta_categories["3198"] == "CONSUMER ELECTRONICS", f"Scenario '{scenario_name}' presta_categories key 3198 has wrong value"
          assert presta_categories["3202"] == "computer,smartphone,gaming console,smart device", f"Scenario '{scenario_name}' presta_categories key 3202 has wrong value"
          assert presta_categories["6471"] == "Smartphones", f"Scenario '{scenario_name}' presta_categories key 6471 has wrong value"
          assert presta_categories["3403"] == "GOOGLE", f"Scenario '{scenario_name}' presta_categories key 3403 has wrong value"
```