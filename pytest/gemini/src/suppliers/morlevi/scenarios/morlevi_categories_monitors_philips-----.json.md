```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi categories JSON data."""
    file_location = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_monitors_philips-----.json'
    with open(file_location, 'r') as f:
        return json.load(f)

# Test to verify that the loaded data is a dictionary
def test_data_is_dict(morlevi_data):
    """Checks if the loaded data is a dictionary."""
    assert isinstance(morlevi_data, dict)

# Test to verify the existence of the 'scenarios' key
def test_scenarios_key_exists(morlevi_data):
    """Checks if the 'scenarios' key exists in the data."""
    assert 'scenarios' in morlevi_data

# Test to verify the 'scenarios' is a dictionary
def test_scenarios_is_dict(morlevi_data):
     """Checks if 'scenarios' is a dictionary."""
     assert isinstance(morlevi_data['scenarios'], dict)

# Test to verify the keys inside the scenarios
def test_scenarios_keys_exist(morlevi_data):
    """Checks if the specific scenarios keys exist."""
    expected_keys = ["PHILIPS 22", "PHILIPS 24-25", "PHILIPS 27-29", "PHILIPS 32", "PHILIPS 34", "PHILIPS 49"]
    assert all(key in morlevi_data['scenarios'] for key in expected_keys)

# Test to verify the structure of each scenario
def test_scenario_structure(morlevi_data):
    """Checks the structure of each scenario in the data."""
    for scenario in morlevi_data['scenarios'].values():
        assert isinstance(scenario, dict)
        assert 'brand' in scenario
        assert 'url' in scenario
        assert 'checkbox' in scenario
        assert 'active' in scenario
        assert 'condition' in scenario
        assert 'presta_categories' in scenario

# Test to verify brand in each scenario is PHILIPS
def test_scenario_brand(morlevi_data):
    """Checks the brand of each scenario is 'PHILIPS'."""
    for scenario in morlevi_data['scenarios'].values():
        assert scenario['brand'] == "PHILIPS"

# Test to verify that all urls are strings (except PHILIPS 34, PHILIPS 49)
def test_scenario_url_is_string(morlevi_data):
     """Checks that url values are strings,except for PHILIPS 34, and 49 cases """
     for key, scenario in morlevi_data['scenarios'].items():
          if key not in ["PHILIPS 34", "PHILIPS 49"]:
            assert isinstance(scenario['url'], str)

# Test to verify the checkbox value is boolean
def test_checkbox_is_boolean(morlevi_data):
    """Checks if 'checkbox' value is boolean."""
    for scenario in morlevi_data['scenarios'].values():
        assert isinstance(scenario['checkbox'], bool)

# Test to verify the active value is boolean
def test_active_is_boolean(morlevi_data):
     """Checks if 'active' value is boolean."""
     for scenario in morlevi_data['scenarios'].values():
        assert isinstance(scenario['active'], bool)

# Test to verify the condition value is string and not empty
def test_condition_is_string(morlevi_data):
    """Checks if 'condition' value is string and is not empty."""
    for scenario in morlevi_data['scenarios'].values():
         assert isinstance(scenario['condition'],str)
         assert len(scenario['condition']) > 0

# Test to verify that presta_categories value is string and not empty
def test_presta_categories_is_string(morlevi_data):
    """Checks if 'presta_categories' value is string and not empty."""
    for scenario in morlevi_data['scenarios'].values():
        assert isinstance(scenario['presta_categories'],str)
        assert len(scenario['presta_categories']) > 0

# Test to verify the urls for PHILIPS 34 and PHILIPS 49 contain specific strings
def test_philips_34_49_url_content(morlevi_data):
    """Checks if URLs for PHILIPS 34 and 49 contains expected strings."""
    assert " --------------------------  PHILIPS 34 -----------------------------------" in morlevi_data['scenarios']["PHILIPS 34"]["url"]
    assert "-----------------------------  PHILIPS 49 ---------------------------------" in morlevi_data['scenarios']["PHILIPS 49"]["url"]
```