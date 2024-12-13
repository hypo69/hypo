```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Loads the JSON data from the file."""
    file_path = 'hypotez/src/suppliers/cdata/scenarios/cdata_categories_laptops_hp.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def test_cdata_categories_data_structure(cdata_categories_data):
    """
    Test if the loaded data has the correct structure.
    It should be a dictionary with a "scenarios" key that contains another dictionary.
    """
    assert isinstance(cdata_categories_data, dict), "Data should be a dictionary."
    assert "scenarios" in cdata_categories_data, "Data should have a 'scenarios' key."
    assert isinstance(cdata_categories_data["scenarios"], dict), "'scenarios' should be a dictionary."


def test_cdata_categories_scenario_keys(cdata_categories_data):
    """
    Test if each scenario has the required keys: 'brand', 'url', 'checkbox', 'active', 'condition','presta_categories'
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key."

def test_cdata_categories_scenario_values_types(cdata_categories_data):
        """
        Test if the scenario values have the correct type
        """
        for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
          assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' should be a string."
          assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' should be a string."
          assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' should be a boolean."
          assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' should be a boolean."
          assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' should be a string."
          assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' 'presta_categories' should be a string."


def test_cdata_categories_condition_values(cdata_categories_data):
        """
        Test if the condition values are equal to "new"
        """
        for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
            assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' 'condition' should be equal to 'new'."

def test_cdata_categories_presta_categories_format(cdata_categories_data):
     """
        Test if the presta_categories values are string of comma-separated numbers
     """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        categories = presta_categories.split(',')
        for cat in categories:
           assert cat.isdigit(), f"Scenario '{scenario_name}' category '{cat}' in 'presta_categories' should be a digit."


def test_cdata_categories_url_not_empty(cdata_categories_data):
    """
    Test if url values are not empty
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert scenario_data["url"].strip() != "", f"Scenario '{scenario_name}' 'url' should not be empty."


def test_cdata_categories_brand_is_HP(cdata_categories_data):
    """
    Test if brand values are HP
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert scenario_data["brand"] == "HP", f"Scenario '{scenario_name}' 'brand' should be equal to 'HP'."


def test_cdata_categories_checkbox_is_false(cdata_categories_data):
    """
    Test if checkbox values are false
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' 'checkbox' should be equal to False."


def test_cdata_categories_active_is_true(cdata_categories_data):
    """
    Test if active values are True
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["active"] == True, f"Scenario '{scenario_name}' 'active' should be equal to True."
```