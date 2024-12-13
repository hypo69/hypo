```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_oppo_data():
    """Loads the ksp_categories_phones_oppo.json data."""
    with open("hypotez/src/suppliers/ksp/scenarios/ksp_categories_phones_oppo.json", 'r') as f:
        return json.load(f)

def test_ksp_oppo_data_structure(ksp_oppo_data):
    """
    Test that the loaded JSON data has the expected structure:
    a dictionary with a 'scenarios' key which is another dictionary.
    """
    assert isinstance(ksp_oppo_data, dict), "The root should be a dictionary"
    assert "scenarios" in ksp_oppo_data, "The root should have a 'scenarios' key"
    assert isinstance(ksp_oppo_data["scenarios"], dict), "The 'scenarios' value should be a dictionary"


def test_ksp_oppo_scenario_keys(ksp_oppo_data):
    """
    Test that each scenario within 'scenarios' has the expected keys:
    'brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories'
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
        assert isinstance(scenario_data, dict), f"Scenario {scenario_name} should be a dictionary"
        assert "brand" in scenario_data, f"Scenario {scenario_name} is missing 'brand' key"
        assert "url" in scenario_data, f"Scenario {scenario_name} is missing 'url' key"
        assert "checkbox" in scenario_data, f"Scenario {scenario_name} is missing 'checkbox' key"
        assert "active" in scenario_data, f"Scenario {scenario_name} is missing 'active' key"
        assert "condition" in scenario_data, f"Scenario {scenario_name} is missing 'condition' key"
        assert "presta_categories" in scenario_data, f"Scenario {scenario_name} is missing 'presta_categories' key"

def test_ksp_oppo_scenario_data_types(ksp_oppo_data):
    """
    Test that the data types of the values in each scenario are correct.
     'brand' should be str, 'url' should be str, 'checkbox' should be bool, 'active' should be bool,
     'condition' should be str, and 'presta_categories' should be a dictionary
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Scenario {scenario_name} 'brand' should be a string"
        assert isinstance(scenario_data["url"], str), f"Scenario {scenario_name} 'url' should be a string"
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario {scenario_name} 'checkbox' should be a boolean"
        assert isinstance(scenario_data["active"], bool), f"Scenario {scenario_name} 'active' should be a boolean"
        assert isinstance(scenario_data["condition"], str), f"Scenario {scenario_name} 'condition' should be a string"
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario {scenario_name} 'presta_categories' should be a dictionary"

def test_ksp_oppo_scenario_presta_categories(ksp_oppo_data):
    """
    Test that 'presta_categories' has the expected structure:
    it should contain a 'template' key which is a dictionary and contain 'oppo' key
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
         presta_categories = scenario_data["presta_categories"]
         assert "template" in presta_categories, f"Scenario {scenario_name} 'presta_categories' should have a 'template' key"
         assert isinstance(presta_categories["template"], dict), f"Scenario {scenario_name} 'template' should be a dictionary"
         assert "oppo" in presta_categories["template"], f"Scenario {scenario_name} 'template' should have a 'oppo' key"
         assert isinstance(presta_categories["template"]["oppo"], str), f"Scenario {scenario_name} 'oppo' should be string"


def test_ksp_oppo_scenario_url_format(ksp_oppo_data):
    """
    Test that each 'url' starts with 'https://ksp.co.il/web/cat/'
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
          assert scenario_data["url"].startswith("https://ksp.co.il/web/cat/"), f"Scenario {scenario_name} 'url' is not in the correct format"

def test_ksp_oppo_scenario_brand_value(ksp_oppo_data):
    """
    Test that each 'brand' value is equal to 'OPPO'.
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
        assert scenario_data["brand"] == "OPPO", f"Scenario {scenario_name} 'brand' is not equal to 'OPPO'"


def test_ksp_oppo_scenario_condition_value(ksp_oppo_data):
    """
    Test that each 'condition' value is equal to 'new'.
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario {scenario_name} 'condition' is not equal to 'new'"

def test_ksp_oppo_scenario_checkbox_false(ksp_oppo_data):
    """
    Test that each 'checkbox' value is false.
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"Scenario {scenario_name} 'checkbox' is not equal to 'false'"

def test_ksp_oppo_scenario_active_true(ksp_oppo_data):
    """
    Test that each 'active' value is true.
    """
    for scenario_name, scenario_data in ksp_oppo_data["scenarios"].items():
        assert scenario_data["active"] == True, f"Scenario {scenario_name} 'active' is not equal to 'true'"

def test_ksp_oppo_data_not_empty(ksp_oppo_data):
    """
        Test that the loaded JSON data is not empty
    """
    assert ksp_oppo_data, "The loaded JSON data is empty"
    assert ksp_oppo_data["scenarios"], "The 'scenarios' dictionary is empty"

```