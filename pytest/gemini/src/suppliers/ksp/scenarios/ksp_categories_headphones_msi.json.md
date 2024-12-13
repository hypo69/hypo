```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_data():
    """Loads the JSON data from the specified file."""
    with open('hypotez/src/suppliers/ksp/scenarios/ksp_categories_headphones_msi.json', 'r') as f:
        return json.load(f)

def test_ksp_data_structure(ksp_data):
    """
    Test that the loaded data has the expected structure, 
    specifically checking for the 'scenarios' key and if its value is a dictionary.
    """
    assert "scenarios" in ksp_data, "The JSON data should have a 'scenarios' key."
    assert isinstance(ksp_data["scenarios"], dict), "The value of 'scenarios' should be a dictionary."

def test_ksp_scenario_keys(ksp_data):
    """
    Test that each scenario within the 'scenarios' dictionary has the expected keys.
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' is missing 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' is missing 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key."

def test_ksp_scenario_values_types(ksp_data):
    """
    Test that the values within each scenario have the expected types.
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' should be a string."
         assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' should be a string."
         assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' should be a boolean."
         assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' should be a boolean."
         assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' should be a string."
         assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' should be a dictionary."

def test_ksp_presta_categories_structure(ksp_data):
    """
    Test that 'presta_categories' within each scenario has the expected nested structure.
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert "template" in presta_categories, f"Scenario '{scenario_name}' 'presta_categories' should have a 'template' key."
        assert isinstance(presta_categories["template"], dict), f"Scenario '{scenario_name}' 'template' should be a dictionary."
        # Additional check to ensure the nested dictionary contains 'msi' key
        assert "msi" in presta_categories["template"], f"Scenario '{scenario_name}' 'template' should have a 'msi' key."
        assert isinstance(presta_categories["template"]["msi"], str), f"Scenario '{scenario_name}' 'msi' value should be a string."

def test_ksp_scenario_values_content(ksp_data):
  """
  Test the values of the keys in all scenarios have specific values
  """
  assert ksp_data["scenarios"]["In-ear Bud"]["brand"] == "MSI", "The brand for 'In-ear Bud' should be 'MSI'"
  assert ksp_data["scenarios"]["In-ear Bud"]["url"] == "https://ksp.co.il/web/cat/242..47..1250", "The url for 'In-ear Bud' should be correct"
  assert ksp_data["scenarios"]["In-ear Bud"]["checkbox"] == False, "The checkbox for 'In-ear Bud' should be false"
  assert ksp_data["scenarios"]["In-ear Bud"]["active"] == True, "The 'active' for 'In-ear Bud' should be True"
  assert ksp_data["scenarios"]["In-ear Bud"]["condition"] == "new", "The 'condition' for 'In-ear Bud' should be 'new'"
  assert ksp_data["scenarios"]["In-ear Bud"]["presta_categories"]["template"]["msi"] == "HEADPHONES BT In-ear Bud", "The msi template for 'In-ear Bud' should be correct"

  assert ksp_data["scenarios"]["Overear"]["brand"] == "MSI", "The brand for 'Overear' should be 'MSI'"
  assert ksp_data["scenarios"]["Overear"]["url"] == "https://ksp.co.il/web/cat/242..1252..47", "The url for 'Overear' should be correct"
  assert ksp_data["scenarios"]["Overear"]["checkbox"] == False, "The checkbox for 'Overear' should be false"
  assert ksp_data["scenarios"]["Overear"]["active"] == True, "The 'active' for 'Overear' should be True"
  assert ksp_data["scenarios"]["Overear"]["condition"] == "new", "The 'condition' for 'Overear' should be 'new'"
  assert ksp_data["scenarios"]["Overear"]["presta_categories"]["template"]["msi"] == "HEADPHONES Overear", "The msi template for 'Overear' should be correct"
```