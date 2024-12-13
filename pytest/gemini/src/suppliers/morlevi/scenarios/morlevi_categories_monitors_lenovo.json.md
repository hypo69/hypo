```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Provides the JSON data from the file."""
    file_location = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_monitors_lenovo.json'
    with open(file_location, 'r') as f:
        return json.load(f)

def test_morlevi_data_structure(morlevi_data):
    """Checks that the loaded data has the correct structure."""
    assert "scenarios" in morlevi_data, "The root should contain a 'scenarios' key"
    assert isinstance(morlevi_data["scenarios"], dict), "'scenarios' should be a dictionary"
    
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_name, str), "Scenario names should be strings"
        assert isinstance(scenario_data, dict), f"Data for scenario '{scenario_name}' should be a dictionary"
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key"
        assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key"
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key"
        assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key"
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key"
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key"

def test_morlevi_data_values(morlevi_data):
    """Checks the validity of specific values in the loaded data."""
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert scenario_data["brand"] == "LENOVO", f"Scenario '{scenario_name}' brand is not LENOVO"
         assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' URL is not a string"
         assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' checkbox is not a boolean"
         assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' active is not a boolean"
         assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' condition is not 'new'"
         assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' missing template in 'presta_categories'"
         assert isinstance(scenario_data["presta_categories"]["template"], dict), f"Scenario '{scenario_name}' template in 'presta_categories' should be a dict"

def test_morlevi_url_format(morlevi_data):
      """Tests the format of the URL in the loaded data"""
      for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        url = scenario_data["url"]
        assert url.startswith("https://www.morlevi.co.il/Cat/"), f"URL for scenario {scenario_name} does not start with the correct prefix"
        assert "sort=datafloat2%2Cprice" in url, f"URL for scenario {scenario_name} does not contain sorting parameter"
        assert "keyword=" in url, f"URL for scenario {scenario_name} does not contain keyword parameter"

def test_morlevi_presta_categories_template_values(morlevi_data):
    """Test specific values in the presta_categories.template dictionary"""
    expected_categories = {
        "LENOVO 21 - 22": "PC MONITORS 21 - 22",
        "LENOVO 23 - 24": "PC MONITORS 23 - 24",
        "LENOVO 26 - 28": "PC MONITORS 26 - 28",
        "LENOVO 27 - 29": "PC MONITORS 27 - 29",
    }
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert "lenovo" in scenario_data["presta_categories"]["template"]
        expected_category = expected_categories.get(scenario_name)
        assert scenario_data["presta_categories"]["template"]["lenovo"] == expected_category, f"Incorrect category mapping for {scenario_name}. Expected '{expected_category}'"

def test_morlevi_active_checkbox_type(morlevi_data):
    """Test that 'active' and 'checkbox' are always booleans"""
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"'active' field in {scenario_name} is not a boolean"
        assert isinstance(scenario_data["checkbox"], bool), f"'checkbox' field in {scenario_name} is not a boolean"


def test_morlevi_condition_value(morlevi_data):
    """Test that the 'condition' field is always 'new'"""
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert scenario_data["condition"] == "new", f"Condition for scenario '{scenario_name}' is not 'new'"
```