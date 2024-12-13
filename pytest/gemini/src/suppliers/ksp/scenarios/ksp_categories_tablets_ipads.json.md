```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Provides the JSON data for testing."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_tablets_ipads.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def test_ksp_categories_data_structure(ksp_categories_data):
    """
    Checks if the loaded JSON data has the correct structure.
    Validates that 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in ksp_categories_data
    assert isinstance(ksp_categories_data["scenarios"], dict)


def test_ksp_categories_scenario_keys(ksp_categories_data):
    """
    Checks if each scenario in the 'scenarios' dictionary has
    the expected keys (brand, url, checkbox, active, condition, presta_categories).
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data


def test_ksp_categories_scenario_values_types(ksp_categories_data):
    """
    Checks if the values in each scenario have the correct types.
    Validates the data types of 'brand' (string), 'url' (string),
     'checkbox' (boolean), 'active' (boolean), 'condition' (string), and 'presta_categories' (dictionary)
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], dict)


def test_ksp_categories_presta_categories_keys(ksp_categories_data):
    """
    Checks if the 'presta_categories' dictionary in each scenario
    has keys that are strings (representing category IDs).
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        for key in scenario_data["presta_categories"].keys():
           assert isinstance(key, str)


def test_ksp_categories_presta_categories_values(ksp_categories_data):
    """
    Checks if the values in 'presta_categories' dictionary in each scenario
    are strings (representing category names).
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      for value in scenario_data["presta_categories"].values():
        assert isinstance(value, str)

def test_ksp_categories_url_validity(ksp_categories_data):
    """
    Checks if the URLs in the 'url' field of each scenario start with "https://ksp.co.il/web/cat/".
    This is a basic URL format check.
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["url"].startswith("https://ksp.co.il/web/cat/")

def test_ksp_categories_condition_value(ksp_categories_data):
    """
    Checks if the 'condition' field in each scenario is equal to 'new'.
    This ensures that all the scenarios are related to new products
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"


def test_ksp_categories_brand_value(ksp_categories_data):
     """
     Checks if the 'brand' field in each scenario is equal to 'APPLE'.
     This ensures that all the scenarios are related to APPLE products
    """
     for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "APPLE"
```