```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi_categories_cases_corsair.json data."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_cases_corsair.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test for valid scenarios loading and structure
def test_morlevi_data_structure(morlevi_data):
    """Checks if the loaded data has the expected 'scenarios' key and it is a dictionary."""
    assert "scenarios" in morlevi_data
    assert isinstance(morlevi_data["scenarios"], dict)

def test_morlevi_scenarios_keys(morlevi_data):
      """Checks if scenarios have the correct keys."""
      scenarios = morlevi_data["scenarios"]
      for scenario_name, scenario_data in scenarios.items():
            assert "brand" in scenario_data
            assert "template" in scenario_data
            assert "url" in scenario_data
            assert "checkbox" in scenario_data
            assert "active" in scenario_data
            assert "condition" in scenario_data
            assert "presta_categories" in scenario_data
            assert isinstance(scenario_data["presta_categories"], dict)
            assert "template" in scenario_data["presta_categories"]
            assert isinstance(scenario_data["presta_categories"]["template"], dict)
            
# Test for valid 'brand' values in scenarios
def test_morlevi_scenarios_brand(morlevi_data):
    """Checks if 'brand' value is 'CORSAIR' for all scenarios."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["brand"] == "CORSAIR"

# Test for valid 'checkbox' values
def test_morlevi_scenarios_checkbox(morlevi_data):
    """Checks if 'checkbox' value is False for all scenarios."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["checkbox"] == False
        
# Test for valid 'active' values
def test_morlevi_scenarios_active(morlevi_data):
    """Checks if 'active' value is True for all scenarios."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert scenario_data["active"] == True

# Test for valid 'condition' values
def test_morlevi_scenarios_condition(morlevi_data):
    """Checks if 'condition' value is new for all scenarios."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert scenario_data["condition"] == "new"

# Test for valid url
def test_morlevi_scenarios_url(morlevi_data):
      """Checks if url is str or None."""
      scenarios = morlevi_data["scenarios"]
      for scenario_name, scenario_data in scenarios.items():
          assert scenario_data["url"] is None or isinstance(scenario_data["url"], str)

# Test for prestashop template data
def test_morlevi_presta_template(morlevi_data):
      """checks if the presta template is a dict with string key and values."""
      scenarios = morlevi_data["scenarios"]
      for scenario_name, scenario_data in scenarios.items():
          template = scenario_data["presta_categories"]["template"]
          for key, value in template.items():
             assert isinstance(key, str)
             assert isinstance(value,str)

# Test for valid prestashop template values for corsair
def test_morlevi_presta_template_values(morlevi_data):
    """Checks if the corsair template values are valid."""
    scenarios = morlevi_data["scenarios"]
    valid_values = ["MINI ITX", "FULL TOWER", "MINI TOWER", "MID TOWER", "GAMING FULL TOWER"]
    for scenario_name, scenario_data in scenarios.items():
        template = scenario_data["presta_categories"]["template"]
        for key, value in template.items():
            if key == "corsair":
                assert value in valid_values

# Test for specific scenarios url is not none
def test_morlevi_specific_scenario_url(morlevi_data):
    """Checks if specific scenarios have a URL."""
    scenarios = morlevi_data["scenarios"]
    assert scenarios["CORSAIR MID TOWER"]["url"] is not None
    assert scenarios["CORSAIR gaming full tower"]["url"] is not None
```