```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def load_test_data():
    """Loads the JSON data from the file."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_gigabyte.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test that the JSON file is loaded correctly
def test_json_file_loaded(load_test_data):
    """
    Test that the json file loaded successfully.
    Checks if the loaded data is not None and is a dictionary
    """
    assert load_test_data is not None
    assert isinstance(load_test_data, dict)


# Test that the 'scenarios' key exists in the loaded data
def test_scenarios_key_exists(load_test_data):
    """
    Test that the key 'scenarios' exist in the JSON file.
    Checks if the scenarios key is in the loaded data
    """
    assert 'scenarios' in load_test_data


# Test that the 'scenarios' value is a dictionary
def test_scenarios_value_is_dict(load_test_data):
    """
    Test that the value of the key 'scenarios' is dictionary.
    Checks if scenarios key is a dictionary type.
    """
    assert isinstance(load_test_data['scenarios'], dict)

# Test individual scenario data types and required keys
def test_individual_scenario_data(load_test_data):
    """
    Test the structure of each scenario in the 'scenarios' dictionary.
    Iterate through each scenario and check the data types
    of the values and presence of mandatory keys.
    """
    for scenario_name, scenario_data in load_test_data['scenarios'].items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' is not a dictionary"
        
        # Check for required keys
        required_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing key: '{key}'"
            
        # Check data types for some specific keys
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' brand is not a string"
        assert isinstance(scenario_data["name"], str), f"Scenario '{scenario_name}' name is not a string"
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url is not a string"
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' checkbox is not a boolean"
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' active is not a boolean"
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' condition is not a string"
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' presta_categories is not a string"

# Test for a specific scenario to ensure its data is correct
def test_specific_scenario_data(load_test_data):
    """
    Test specific data of one scenario.
    Check if the values of specific keys are equal to the expected.
    """
    scenario_name = "internal_ssd_sata_3 120-128GB"
    expected_data = {
        "brand": "GIGABYTE",
        "name": "internal_ssd_sata_3_128",
        "url": "https://www.morlevi.co.il/Cat/50?p_315=2&p_175=822&sort=datafloat2%2Cprice&keyword=",
        "checkbox": False,
        "active": True,
        "condition":"new",
        "presta_categories": "117,118,134"
    }
    
    assert load_test_data["scenarios"][scenario_name] == expected_data

# Test for url format
def test_url_format(load_test_data):
    """
    Test if the 'url' values in the scenarios are valid.
    Checks that if the URL doesn't start with https:// it contains the substring 'GIGABYTE'
    """
    for scenario_name, scenario_data in load_test_data['scenarios'].items():
        url = scenario_data.get("url")
        if not url.startswith("https://"):
            assert "GIGABYTE" in url, f"URL in scenario '{scenario_name}' doesn't start with https:// and doesn't contain GIGABYTE"
        

# Test the active key
def test_active_key_type(load_test_data):
    """
    Test if the 'active' key exists and if it's a boolean
    Iterates through the scenarios and checks the type of active
    """
    for scenario_name, scenario_data in load_test_data['scenarios'].items():
         assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key"
         assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' active key is not a boolean"
# Test the checkbox key
def test_checkbox_key_type(load_test_data):
    """
    Test if the 'checkbox' key exists and if it's a boolean
    Iterates through the scenarios and checks the type of checkbox
    """
    for scenario_name, scenario_data in load_test_data['scenarios'].items():
         assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key"
         assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' checkbox key is not a boolean"

# Test condition key
def test_condition_key_type(load_test_data):
     """
    Test if the 'condition' key exists and if it's a string
    Iterates through the scenarios and checks the type of condition
    """
     for scenario_name, scenario_data in load_test_data['scenarios'].items():
         assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key"
         assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' condition key is not a string"

# Test presta_categories key
def test_presta_categories_key_type(load_test_data):
     """
    Test if the 'presta_categories' key exists and if it's a string
    Iterates through the scenarios and checks the type of presta_categories
    """
     for scenario_name, scenario_data in load_test_data['scenarios'].items():
         assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key"
         assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' presta_categories key is not a string"

```