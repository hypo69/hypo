```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Provides the JSON data for the tests."""
    file_path = 'hypotez/src/suppliers/cdata/scenarios/cdata_categories_aio_hp.json'
    with open(file_path, 'r') as f:
        return json.load(f)


def test_cdata_categories_data_structure(cdata_categories_data):
    """
    Test that the loaded JSON data has the correct structure
    """
    assert "scenarios" in cdata_categories_data
    assert isinstance(cdata_categories_data["scenarios"], dict)

def test_scenario_keys_exist(cdata_categories_data):
    """
    Test that each scenario has the correct keys
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_scenario_values_data_types(cdata_categories_data):
    """
    Test that the values in each scenario have the correct data types
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)

def test_scenario_brand_value(cdata_categories_data):
     """
    Test that the brand is 'HP' for all scenarios
    """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "HP"

def test_scenario_condition_value(cdata_categories_data):
    """
    Test that the condition is 'new' for all scenarios
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

def test_scenario_checkbox_is_false(cdata_categories_data):
    """
    Test that the checkbox is False for all scenarios
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] == False

def test_scenario_active_is_true(cdata_categories_data):
    """
    Test that the active is True for all scenarios
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["active"] == True

def test_presta_categories_not_empty(cdata_categories_data):
    """
    Test that the presta_categories string is not empty
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["presta_categories"] != ""
def test_presta_categories_format(cdata_categories_data):
    """
    Test that the presta_categories string contains only digits and commas
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert all(c.isdigit() or c == ',' for c in scenario_data["presta_categories"])

def test_url_not_empty(cdata_categories_data):
    """
    Test that the url string is not empty
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["url"] != ""

def test_url_is_string(cdata_categories_data):
     """
     Test that the url is String
     """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)
```