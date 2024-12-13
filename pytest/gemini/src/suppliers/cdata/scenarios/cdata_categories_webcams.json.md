```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Provides the JSON data for testing."""
    return {
        "scenarios": {
            "Cams MICROSOFT": {
                "brand": "MICROSOFT",
                "url": "https://reseller.c-data.co.il/camwebs-and-controllers#/manFilters=1&pageSize=33&viewMode=grid&orderBy=0&pageNumber=1",
                "checkbox": False,
                "active": True,
                "condition":"new",
                "presta_categories": "520,523,984"
            },
            "Cams HP": {
                "brand": "HP",
                "url": "https://reseller.c-data.co.il/camwebs-and-controllers#/manFilters=2&pageSize=33&viewMode=grid&orderBy=0&pageNumber=1",
                "checkbox": False,
                "active": True,
                 "condition":"new",
                "presta_categories": "520,523,985"
            }
        }
    }

def test_cdata_categories_data_load(cdata_categories_data):
    """Test that the fixture loads correctly and has data."""
    assert cdata_categories_data is not None
    assert isinstance(cdata_categories_data, dict)
    assert "scenarios" in cdata_categories_data

def test_cdata_scenario_has_brand(cdata_categories_data):
    """Test that each scenario has a 'brand' key."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert "brand" in scenario_data, f"Scenario '{scenario_name}' is missing 'brand' key."
      assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' value is not a string."
def test_cdata_scenario_has_url(cdata_categories_data):
    """Test that each scenario has a 'url' key."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "url" in scenario_data, f"Scenario '{scenario_name}' is missing 'url' key."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' value is not a string."

def test_cdata_scenario_has_checkbox(cdata_categories_data):
    """Test that each scenario has a 'checkbox' key."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' value is not a boolean."

def test_cdata_scenario_has_active(cdata_categories_data):
    """Test that each scenario has an 'active' key."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' value is not a boolean."

def test_cdata_scenario_has_condition(cdata_categories_data):
    """Test that each scenario has a 'condition' key."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' value is not a string."

def test_cdata_scenario_has_presta_categories(cdata_categories_data):
    """Test that each scenario has a 'presta_categories' key."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key."
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' 'presta_categories' value is not a string."
def test_cdata_scenario_valid_values(cdata_categories_data):
    """Test the values are valid based on type."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"],str)
        assert isinstance(scenario_data["presta_categories"],str)
def test_cdata_scenario_empty_data():
    """Tests the scenario with an empty data."""
    empty_data = {"scenarios":{}}
    assert "scenarios" in empty_data
    assert len(empty_data["scenarios"]) ==0
def test_cdata_scenario_no_scenarios():
    """Tests when the scenarios key is not given."""
    no_scenarios = {}
    assert "scenarios" not in no_scenarios
```