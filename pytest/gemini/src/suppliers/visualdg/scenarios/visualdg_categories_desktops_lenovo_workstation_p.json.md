```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def scenario_data():
    """Loads the JSON data for testing."""
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_desktops_lenovo_workstation_p.json'
    with open(file_path, 'r') as file:
        return json.load(file)

# Test to ensure that the data is loaded correctly
def test_data_loaded(scenario_data):
    """Checks if the data is loaded correctly and not empty."""
    assert scenario_data is not None
    assert isinstance(scenario_data, dict)
    assert 'scenarios' in scenario_data
    assert isinstance(scenario_data['scenarios'], dict)
    assert len(scenario_data['scenarios']) > 0

# Test to check the structure of each scenario
def test_scenario_structure(scenario_data):
    """Checks if each scenario has the required keys."""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        assert isinstance(scenario, dict)
        assert 'brand' in scenario
        assert 'template' in scenario
        assert 'url' in scenario
        assert 'checkbox' in scenario
        assert 'active' in scenario
        assert 'condition' in scenario
        assert 'presta_categories' in scenario

# Test to check the data type of scenario values
def test_scenario_value_types(scenario_data):
    """Checks if scenario values have the correct data types."""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        assert isinstance(scenario['brand'], str)
        assert isinstance(scenario['template'], str)
        assert isinstance(scenario['url'], str)
        assert isinstance(scenario['checkbox'], bool)
        assert isinstance(scenario['active'], bool)
        assert isinstance(scenario['condition'], str)
        assert isinstance(scenario['presta_categories'], str)

# Test to check valid values for 'brand' and 'template'
def test_valid_brand_template_values(scenario_data):
    """Checks if 'brand' is always 'LENOVO' and 'template' is 'WORKSTATION P'."""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        assert scenario['brand'] == 'LENOVO'
        assert scenario['template'] == 'WORKSTATION P'

# Test to check that 'url' is always a string
def test_url_is_string(scenario_data):
    """Checks if url is always a string"""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        assert isinstance(scenario['url'], str)
        
# Test to check 'checkbox' values are always false
def test_checkbox_is_false(scenario_data):
    """Checks if 'checkbox' is always false."""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        assert scenario['checkbox'] == False

# Test to check 'active' values are always true
def test_active_is_true(scenario_data):
    """Checks if 'active' is always true."""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        assert scenario['active'] == True

# Test to check 'condition' is always new
def test_condition_is_new(scenario_data):
     """Checks if 'condition' is always 'new'."""
     for scenario_name, scenario in scenario_data['scenarios'].items():
        assert scenario['condition'] == 'new'

# Test to check if 'presta_categories' is always a string of comma separated integers
def test_presta_categories_format(scenario_data):
    """Checks if 'presta_categories' is a string of comma-separated integers."""
    for scenario_name, scenario in scenario_data['scenarios'].items():
        categories = scenario['presta_categories'].split(',')
        for category in categories:
            assert category.isdigit()
```