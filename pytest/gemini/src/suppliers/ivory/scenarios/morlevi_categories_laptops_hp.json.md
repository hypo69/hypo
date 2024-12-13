```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def category_data():
    """Provides test data loaded from the JSON file."""
    file_location = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_laptops_hp.json'
    with open(file_location, 'r') as f:
        return json.load(f)

# Test case for a scenario with valid data
def test_valid_scenario_hp_11_6_i3(category_data):
    """
    Test a valid scenario 'HP 11.6 I3' to check if the data is loaded correctly.
    Verifies if the brand and prestashop categories are properly extracted.
    """
    scenario = category_data['scenarios']['HP 11.6 I3']
    assert scenario['brand'] == 'HP'
    assert scenario['presta_categories']['template']['HP'] == ["LAPTOPS INTEL I3", "11"]

def test_valid_scenario_hp_15_amd_ryzen_5(category_data):
     """
     Test a valid scenario 'HP 15 AMD RYZEN 5' to check if the data is loaded correctly.
     Verifies if the brand and prestashop categories are properly extracted.
     Also checking if a different template key is handled correctly
     """
     scenario = category_data['scenarios']['HP 15 AMD RYZEN 5']
     assert scenario['brand'] == 'HP'
     assert scenario['presta_categories']['template']['gigabyte'] == ["LAPTOPS AMD RYZEN 5", "15"]



# Test case for checking url null for a valid scenario
def test_valid_scenario_url_null(category_data):
    """
    Test a valid scenario 'HP 11.6 I3' to check if the url is null.
    Verifies if the url is null for a valid scenario
    """
    scenario = category_data['scenarios']['HP 11.6 I3']
    assert scenario['url'] is None

# Test case for checking checkbox false for a valid scenario
def test_valid_scenario_checkbox_false(category_data):
    """
    Test a valid scenario 'HP 11.6 I3' to check if the checkbox is false.
    Verifies if the checkbox is false for a valid scenario
    """
    scenario = category_data['scenarios']['HP 11.6 I3']
    assert scenario['checkbox'] is False

# Test case for checking active true for a valid scenario
def test_valid_scenario_active_true(category_data):
    """
    Test a valid scenario 'HP 11.6 I3' to check if the active is true.
    Verifies if the active is true for a valid scenario
    """
    scenario = category_data['scenarios']['HP 11.6 I3']
    assert scenario['active'] is True

# Test case for checking condition new for a valid scenario
def test_valid_scenario_condition_new(category_data):
    """
    Test a valid scenario 'HP 11.6 I3' to check if the condition is new.
    Verifies if the condition is new for a valid scenario
    """
    scenario = category_data['scenarios']['HP 11.6 I3']
    assert scenario['condition'] == 'new'

# Test case to check if a different scenario loads correctly
def test_valid_scenario_hp_17_3_pentium(category_data):
    """
    Test a different valid scenario 'HP 17.3 Pentium' to check if the data is loaded correctly.
    Verifies if the brand and prestashop categories are properly extracted for a different entry.
    """
    scenario = category_data['scenarios']['HP 17.3 Pentium']
    assert scenario['brand'] == 'HP'
    assert scenario['presta_categories']['template']['HP'] == ["LAPTOPS INTEL CELERON", "17"]

# Test case for non existent scenario
def test_non_existent_scenario(category_data):
    """
    Test a non existent scenario to check if it returns a KeyError.
    """
    with pytest.raises(KeyError):
        _ = category_data['scenarios']['NonExistentScenario']

# Test case for an empty scenarios
def test_empty_scenarios():
     """
    Test an empty scenarios key to check if it raises a KeyError
    """
     file_location = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_laptops_hp.json'
     with open(file_location, 'r') as f:
         data = json.load(f)
     
     data['scenarios'] = {}

     with pytest.raises(KeyError):
         _ = data['scenarios']['NonExistentScenario']

# Test case for an empty json file
def test_empty_file():
    """
    Test case for an empty json file to check if it raises a json.decoder.JSONDecodeError
    """
    with pytest.raises(json.decoder.JSONDecodeError):
        with open('test_empty.json', 'w') as f:
            f.write("")
        with open('test_empty.json', 'r') as f:
            json.load(f)
```