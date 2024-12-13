```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Loads the JSON data from the specified file."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_aio_imacs.json"
    with open(file_path, 'r') as f:
        return json.load(f)

def test_ksp_categories_data_structure(ksp_categories_data):
    """
    Tests if the loaded JSON data has the expected top-level structure (a dictionary with a "scenarios" key).
    """
    assert isinstance(ksp_categories_data, dict), "The loaded JSON should be a dictionary."
    assert "scenarios" in ksp_categories_data, "The dictionary should have a 'scenarios' key."
    assert isinstance(ksp_categories_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."


def test_ksp_categories_scenario_keys(ksp_categories_data):
    """
    Tests that all scenarios have the expected keys.
    """
    expected_keys = {"brand", "url", "checkbox", "active", "condition", "presta_categories"}
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
       assert set(scenario_data.keys()) == expected_keys, f"Scenario '{scenario_name}' does not have all expected keys: {expected_keys}"
       assert isinstance(scenario_data["presta_categories"],dict), f"Scenario '{scenario_name}' presta_categories should be a dictionary"


def test_ksp_categories_scenario_values(ksp_categories_data):
    """
    Tests values for various scenarios including types and basic correctness.
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert isinstance(scenario_data["brand"],str), f"Scenario '{scenario_name}' brand should be a string."
      assert isinstance(scenario_data["url"],str), f"Scenario '{scenario_name}' url should be a string."
      assert isinstance(scenario_data["checkbox"],bool), f"Scenario '{scenario_name}' checkbox should be a boolean."
      assert isinstance(scenario_data["active"],bool), f"Scenario '{scenario_name}' active should be a boolean."
      assert isinstance(scenario_data["condition"],str), f"Scenario '{scenario_name}' condition should be a string."
      assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' presta_categories should have a 'template' key."
      assert isinstance(scenario_data["presta_categories"]["template"], dict), f"Scenario '{scenario_name}' template should be a dictionary"

def test_ksp_categories_apple_brand(ksp_categories_data):
    """
    Tests if brand is APPLE for all scenarios.
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert scenario_data["brand"] == "APPLE", f"Scenario '{scenario_name}' brand should be APPLE"


def test_ksp_categories_condition_new(ksp_categories_data):
    """
    Tests if condition is new for all scenarios.
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' condition should be new"

def test_ksp_categories_url_valid(ksp_categories_data):
      """
        Tests that the URLs in the data are valid URLs by checking if they start with https.
      """
      for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["url"].startswith("https://"), f"Scenario '{scenario_name}' URL should start with https://."
```