```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_psu_antec.json"
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        pytest.fail(f"File not found: {file_path}")
    except json.JSONDecodeError:
         pytest.fail(f"Invalid JSON format in: {file_path}")



def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test if the loaded data has the expected structure.
    Verifies the root key 'scenarios' exists and contains at least one item.
    """
    assert "scenarios" in morlevi_categories_data, "The root key 'scenarios' is missing"
    assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' value must be a dictionary."
    assert len(morlevi_categories_data["scenarios"]) > 0, "The 'scenarios' dictionary is empty."

def test_morlevi_categories_each_item_has_expected_keys(morlevi_categories_data):
    """
    Test if each item in the 'scenarios' dictionary has the expected keys:
    'brand', 'name', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         expected_keys = ['brand', 'name', 'url', 'checkbox', 'active', 'condition', 'presta_categories']
         assert all(key in scenario_data for key in expected_keys), f"Scenario '{scenario_name}' is missing one or more of the required keys: {expected_keys}"

def test_morlevi_categories_data_types(morlevi_categories_data):
    """
    Test the data types of the values for each key in every scenario.
    Validates the types for 'brand' (str), 'name' (str), 'url' (str), 'checkbox' (bool),
    'active' (bool), 'condition'(str) and 'presta_categories'(str).
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
       assert isinstance(scenario_data['brand'], str), f"The 'brand' of scenario '{scenario_name}' should be a string."
       assert isinstance(scenario_data['name'], str), f"The 'name' of scenario '{scenario_name}' should be a string."
       assert isinstance(scenario_data['url'], str), f"The 'url' of scenario '{scenario_name}' should be a string."
       assert isinstance(scenario_data['checkbox'], bool), f"The 'checkbox' of scenario '{scenario_name}' should be a boolean."
       assert isinstance(scenario_data['active'], bool), f"The 'active' of scenario '{scenario_name}' should be a boolean."
       assert isinstance(scenario_data['condition'], str), f"The 'condition' of scenario '{scenario_name}' should be a string."
       assert isinstance(scenario_data['presta_categories'], str), f"The 'presta_categories' of scenario '{scenario_name}' should be a string."

def test_morlevi_categories_brand_is_antec(morlevi_categories_data):
    """
    Test if the 'brand' value in each scenario is equal to "ANTEC".
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert scenario_data['brand'] == "ANTEC", f"The 'brand' of scenario '{scenario_name}' is not 'ANTEC'."

def test_morlevi_categories_url_valid_format(morlevi_categories_data):
    """
     Test if the 'url' value in each scenario starts with "https://www.morlevi.co.il/Cat/".
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert scenario_data['url'].startswith("https://www.morlevi.co.il/Cat/"), f"The 'url' of scenario '{scenario_name}' does not start with 'https://www.morlevi.co.il/Cat/'."

def test_morlevi_categories_active_is_true(morlevi_categories_data):
    """
    Test if the 'active' value in each scenario is equal to True.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert scenario_data['active'] == True, f"The 'active' of scenario '{scenario_name}' is not True."

def test_morlevi_categories_condition_is_new(morlevi_categories_data):
      """
      Test if the 'condition' value in each scenario is equal to "new".
      """
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data['condition'] == "new", f"The 'condition' of scenario '{scenario_name}' is not 'new'."

def test_morlevi_categories_presta_categories_not_empty(morlevi_categories_data):
      """
      Test if the 'presta_categories' value in each scenario is not an empty string.
      """
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data['presta_categories'] != "", f"The 'presta_categories' of scenario '{scenario_name}' is empty."

def test_morlevi_categories_presta_categories_comma_separated_numbers(morlevi_categories_data):
    """
    Test if the 'presta_categories' value in each scenario is a string of comma-separated numbers.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        presta_categories = scenario_data['presta_categories']
        categories_list = presta_categories.split(',')
        
        for category in categories_list:
            assert category.isdigit(), f"The category '{category}' in 'presta_categories' of scenario '{scenario_name}' is not a valid number."

def test_morlevi_categories_checkbox_is_false(morlevi_categories_data):
     """
     Test if the 'checkbox' value in each scenario is equal to False.
     """
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data['checkbox'] == False, f"The 'checkbox' of scenario '{scenario_name}' is not False."
```