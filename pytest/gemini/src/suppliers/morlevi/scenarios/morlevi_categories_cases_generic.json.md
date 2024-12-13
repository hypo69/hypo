```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_cases_generic.json data."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_cases_generic.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test cases for the structure of the loaded JSON data

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test that the loaded data has the top-level 'scenarios' key, and that 'scenarios' is a dictionary
    """
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key is missing from the data"
    assert isinstance(morlevi_categories_data["scenarios"], dict), "'scenarios' should be a dictionary"


def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test that each scenario within the loaded data has the expected keys
    """
    expected_keys = ["brand", "template", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' should be a dictionary"
        for key in expected_keys:
             assert key in scenario_data, f"Scenario '{scenario_name}' is missing the key '{key}'"


def test_morlevi_categories_presta_categories_structure(morlevi_categories_data):
    """
    Test that each scenario within the loaded data has 'presta_categories' correctly nested
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
       
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories'"
        assert isinstance(scenario_data["presta_categories"], dict), f"'presta_categories' in '{scenario_name}' should be a dictionary"
        
        
        assert "template" in scenario_data["presta_categories"], f" 'template' key is missing from 'presta_categories' in scenario '{scenario_name}'"
        assert isinstance(scenario_data["presta_categories"]["template"], dict), f"'template' in 'presta_categories' in scenario '{scenario_name}' should be a dictionary"
        
        # Additional check for the nested dictionary and its values - assuming 'computer cases' is the key and it has string value
        for cat_key, cat_value in scenario_data["presta_categories"]["template"].items():
            assert isinstance(cat_key, str), f"Key within 'template' in 'presta_categories' in scenario '{scenario_name}' should be a string"
            assert isinstance(cat_value, str), f"Value within 'template' in 'presta_categories' in scenario '{scenario_name}' should be a string"



# Test cases for specific scenarios' values

def test_morlevi_categories_generic_mid_tower(morlevi_categories_data):
    """
    Test specific values for the "GENERIC MID TOWER" scenario
    """
    scenario = morlevi_categories_data["scenarios"].get("GENERIC MID TOWER")
    assert scenario is not None, "Scenario 'GENERIC MID TOWER' not found"
    assert scenario["brand"] == "GENERIC"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/97"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["computer cases"] == "MID TOWER"


def test_morlevi_categories_generic_full_tower(morlevi_categories_data):
    """
    Test specific values for the "GENERIC full tower" scenario
    """
    scenario = morlevi_categories_data["scenarios"].get("GENERIC full tower")
    assert scenario is not None, "Scenario 'GENERIC full tower' not found"
    assert scenario["brand"] == "GENERIC"
    assert scenario["url"] == "----------------------------GENERIC FULL TOWER--------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["computer cases"] == "FULL TOWER"

def test_morlevi_categories_generic_mini_tower(morlevi_categories_data):
    """
    Test specific values for the "GENERIC mini tower" scenario
    """
    scenario = morlevi_categories_data["scenarios"].get("GENERIC mini tower")
    assert scenario is not None, "Scenario 'GENERIC mini tower' not found"
    assert scenario["brand"] == "GENERIC"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/97"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["computer cases"] == "MINI TOWER"

def test_morlevi_categories_generic_gaming_mid_tower(morlevi_categories_data):
    """
    Test specific values for the "GENERIC gaming MID TOWER" scenario
    """
    scenario = morlevi_categories_data["scenarios"].get("GENERIC gaming MID TOWER")
    assert scenario is not None, "Scenario 'GENERIC gaming MID TOWER' not found"
    assert scenario["brand"] == "GENERIC"
    assert scenario["url"] == "----------------------------GENERIC gaming mid--------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["computer cases"] == "MID TOWER"

def test_morlevi_categories_generic_gaming_full_tower(morlevi_categories_data):
    """
    Test specific values for the "GENERIC gaming full tower" scenario
    """
    scenario = morlevi_categories_data["scenarios"].get("GENERIC gaming full tower")
    assert scenario is not None, "Scenario 'GENERIC gaming full tower' not found"
    assert scenario["brand"] == "GENERIC"
    assert scenario["url"] == "----------------------------GENERIC gaming full TOWER--------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["computer cases"] == "FULL TOWER"

def test_morlevi_categories_generic_mini_itx(morlevi_categories_data):
    """
    Test specific values for the "GENERIC mini itx" scenario
    """
    scenario = morlevi_categories_data["scenarios"].get("GENERIC mini itx")
    assert scenario is not None, "Scenario 'GENERIC mini itx' not found"
    assert scenario["brand"] == "GENERIC"
    assert scenario["url"] == "----------------------------GENERIC mini itxR--------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["computer cases"] == "MINI ITX"
```