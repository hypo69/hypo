```python
import pytest
import json

# Fixture to load the json data from the file
@pytest.fixture
def ksp_data():
    """Loads the json data from the file."""
    file_location = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_headphones_hyperx.json"
    with open(file_location, "r") as f:
        return json.load(f)


def test_ksp_data_structure(ksp_data):
    """
    Test the structure of the loaded data.
    Checks if the data is a dictionary with a "scenarios" key,
    and that "scenarios" is also a dictionary.
    """
    assert isinstance(ksp_data, dict), "Data should be a dictionary"
    assert "scenarios" in ksp_data, "Data should contain a 'scenarios' key"
    assert isinstance(ksp_data["scenarios"], dict), "'scenarios' should be a dictionary"


def test_ksp_scenario_keys(ksp_data):
    """
    Test the keys of the first scenario.
    Checks if the scenario is available, and then validates that all the mandatory keys
    are present in the first scenario in the "scenarios" dictionary.
    """
    scenarios = ksp_data["scenarios"]
    assert scenarios, "There should be at least one scenario."

    first_scenario_key = next(iter(scenarios))
    first_scenario = scenarios[first_scenario_key]
    
    expected_keys = {"brand", "url", "checkbox", "active", "condition", "presta_categories"}
    assert set(first_scenario.keys()) == expected_keys, f"Expected keys not found in scenario: {first_scenario}"


def test_ksp_scenario_values(ksp_data):
    """
    Test the values of the first scenario.
    Checks that specific values in the first scenario dictionary match
    the expected types and contents.
    """
    scenarios = ksp_data["scenarios"]
    first_scenario_key = next(iter(scenarios))
    first_scenario = scenarios[first_scenario_key]

    assert first_scenario["brand"] == "HYPER-X", "Brand should be HYPER-X"
    assert isinstance(first_scenario["url"], str), "URL should be a string"
    assert "ksp.co.il" in first_scenario["url"], "URL should contain 'ksp.co.il'"
    assert isinstance(first_scenario["checkbox"], bool), "Checkbox should be a boolean"
    assert isinstance(first_scenario["active"], bool), "Active should be a boolean"
    assert isinstance(first_scenario["condition"], str), "Condition should be a string"
    assert isinstance(first_scenario["presta_categories"], dict), "presta_categories should be a dictionary"


def test_ksp_presta_categories_template(ksp_data):
     """
    Test the "presta_categories" and its template subfield
    Verifies the sub-structure of the "presta_categories" including existence of the template and expected keys.
    """
     scenarios = ksp_data["scenarios"]
     first_scenario_key = next(iter(scenarios))
     first_scenario = scenarios[first_scenario_key]
    
     presta_categories = first_scenario["presta_categories"]
     assert "template" in presta_categories, "presta_categories should contain a 'template' key"
     template = presta_categories["template"]
     assert isinstance(template, dict), "template should be a dictionary"
     
     expected_template_keys = {"hyper-x"}
     assert set(template.keys()) == expected_template_keys, f"Expected keys not found in template: {template}"
     assert isinstance(template["hyper-x"], str)

def test_ksp_scenario_multiple_scenarios(ksp_data):
    """
    Test handling of multiple scenarios.
    Adds a second scenario to data and checks that it is loaded correctly.
    """
    
    ksp_data["scenarios"]["Over-ear Headphones"] = {
        "brand": "HYPER-X",
        "url": "https://ksp.co.il/web/cat/242..1250",
        "checkbox": True,
        "active": False,
        "condition": "used",
        "presta_categories": {
            "template": { "hyper-x": "HEADPHONES BT Over-ear" }
         }
    }
    
    scenarios = ksp_data["scenarios"]
    assert len(scenarios) == 2, "There should be two scenarios."

    second_scenario = scenarios["Over-ear Headphones"]
    assert second_scenario["brand"] == "HYPER-X", "Second brand should be HYPER-X"
    assert second_scenario["checkbox"] == True, "Second Checkbox should be True"
    assert second_scenario["active"] == False, "Second active should be False"
    assert second_scenario["condition"] == "used", "Second condition should be used"
    assert second_scenario["presta_categories"]["template"]["hyper-x"] == "HEADPHONES BT Over-ear", "Second category should be HEADPHONES BT Over-ear"
```