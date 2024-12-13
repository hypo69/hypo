```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_monitors_samsung.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test case for SAMSUNG 21 - 22 scenario
def test_samsung_21_22_scenario(morlevi_categories_data):
    """Checks the correctness of the 'SAMSUNG 21 - 22' scenario."""
    scenario = morlevi_categories_data["scenarios"]["SAMSUNG 21 - 22"]
    assert scenario["brand"] == "SAMSUNG"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_350=1805&p_315=28&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["samsung"] == "PC MONITORS 21 - 22"

# Test case for SAMSUNG 23 - 24 scenario
def test_samsung_23_24_scenario(morlevi_categories_data):
    """Checks the correctness of the 'SAMSUNG 23 - 24' scenario."""
    scenario = morlevi_categories_data["scenarios"]["SAMSUNG 23 - 24"]
    assert scenario["brand"] == "SAMSUNG"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_350=1806&p_315=28&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["samsung"] == "PC MONITORS 23 - 24"

# Test case for SAMSUNG 26 - 28 scenario
def test_samsung_26_28_scenario(morlevi_categories_data):
    """Checks the correctness of the 'SAMSUNG 26 - 28' scenario."""
    scenario = morlevi_categories_data["scenarios"]["SAMSUNG 26 - 28"]
    assert scenario["brand"] == "SAMSUNG"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_350=1807&p_315=28&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["samsung"] == "PC MONITORS 26 - 28"

# Test case for SAMSUNG 29 - 31 scenario
def test_samsung_29_31_scenario(morlevi_categories_data):
    """Checks the correctness of the 'SAMSUNG 29 - 31' scenario."""
    scenario = morlevi_categories_data["scenarios"]["SAMSUNG 29 - 31"]
    assert scenario["brand"] == "SAMSUNG"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_350=1808&p_315=28&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["samsung"] == "PC MONITORS 29 - 31"

# Test case for SAMSUNG 32 - 34 scenario
def test_samsung_32_34_scenario(morlevi_categories_data):
    """Checks the correctness of the 'SAMSUNG 32 - 34' scenario."""
    scenario = morlevi_categories_data["scenarios"]["SAMSUNG 32 - 34"]
    assert scenario["brand"] == "SAMSUNG"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_350=1809&p_350=1810&p_315=28&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["samsung"] == "PC MONITORS 32 - 34"

# Test case for all scenarios existing
def test_all_scenarios_exist(morlevi_categories_data):
    """Checks if all expected scenarios are present."""
    scenarios = morlevi_categories_data["scenarios"]
    expected_scenarios = [
        "SAMSUNG 21 - 22",
        "SAMSUNG 23 - 24",
        "SAMSUNG 26 - 28",
        "SAMSUNG 29 - 31",
        "SAMSUNG 32 - 34"
    ]
    assert all(scenario in scenarios for scenario in expected_scenarios)

def test_scenario_keys(morlevi_categories_data):
    """Checks if all scenarios have the expected keys."""
    expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert all(key in scenario_data for key in expected_keys)

def test_presta_categories_keys(morlevi_categories_data):
    """Checks if 'presta_categories' has the expected keys."""
    for scenario_data in morlevi_categories_data["scenarios"].values():
      assert "template" in scenario_data["presta_categories"]

def test_template_keys(morlevi_categories_data):
     """Checks if 'template' has the expected keys."""
     for scenario_data in morlevi_categories_data["scenarios"].values():
         assert "samsung" in scenario_data["presta_categories"]["template"]
```