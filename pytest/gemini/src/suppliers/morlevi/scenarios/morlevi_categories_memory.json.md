```python
import pytest
import json

# Define a fixture to load the JSON data
@pytest.fixture
def memory_scenarios():
    """Loads the memory scenarios from the JSON file."""
    file_location = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_memory.json'
    with open(file_location, 'r') as f:
        return json.load(f)

# Test for the structure of the loaded data
def test_memory_scenarios_structure(memory_scenarios):
    """
    Test that the loaded data is a dictionary with a 'scenarios' key,
    and that 'scenarios' value is also a dictionary.
    """
    assert isinstance(memory_scenarios, dict)
    assert 'scenarios' in memory_scenarios
    assert isinstance(memory_scenarios['scenarios'], dict)

# Test for the presence of specific keys in each scenario
def test_memory_scenario_keys(memory_scenarios):
    """
    Test that each scenario within 'scenarios' contains the expected keys:
    'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        assert 'brand' in scenario_data, f"Missing 'brand' in {scenario_name}"
        assert 'url' in scenario_data, f"Missing 'url' in {scenario_name}"
        assert 'checkbox' in scenario_data, f"Missing 'checkbox' in {scenario_name}"
        assert 'active' in scenario_data, f"Missing 'active' in {scenario_name}"
        assert 'condition' in scenario_data, f"Missing 'condition' in {scenario_name}"
        assert 'presta_categories' in scenario_data, f"Missing 'presta_categories' in {scenario_name}"

# Test for the correct types of values in each scenario
def test_memory_scenario_value_types(memory_scenarios):
    """
    Test that the values associated with specific keys in each scenario have the correct data types:
    'brand' should be a string, 'url' should be a string, 'checkbox' should be a boolean,
    'active' should be a boolean, 'condition' should be a string,
    and 'presta_categories' should be a dictionary.
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        assert isinstance(scenario_data['brand'], str), f"'brand' is not a string in {scenario_name}"
        assert isinstance(scenario_data['url'], str), f"'url' is not a string in {scenario_name}"
        assert isinstance(scenario_data['checkbox'], bool), f"'checkbox' is not a boolean in {scenario_name}"
        assert isinstance(scenario_data['active'], bool), f"'active' is not a boolean in {scenario_name}"
        assert isinstance(scenario_data['condition'], str), f"'condition' is not a string in {scenario_name}"
        assert isinstance(scenario_data['presta_categories'], dict), f"'presta_categories' is not a dict in {scenario_name}"


def test_presta_categories_structure(memory_scenarios):
    """
    Test that 'presta_categories' always contains a 'template' key and that template is a dict
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        assert 'template' in scenario_data['presta_categories'],f"Missing 'template' in {scenario_name} presta_categories"
        assert isinstance(scenario_data['presta_categories']['template'], dict), f"'template' is not a dict in {scenario_name}"

def test_presta_categories_template_content(memory_scenarios):
    """
    Test that each template inside 'presta_categories' has exactly one key value pair
     where the key is brand and the value is a string.
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
       template = scenario_data['presta_categories']['template']
       assert len(template) == 1, f"Template should have exactly one key in {scenario_name}"
       for k,v in template.items():
            assert isinstance(k,str), f"key should be string in {scenario_name} "
            assert isinstance(v,str), f"value should be string in {scenario_name} "


def test_memory_scenario_url_starts_with_https(memory_scenarios):
    """
        Test that each url starts with https
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        url = scenario_data['url']
        assert url.startswith("https://"), f"URL does not start with https in {scenario_name}"

def test_memory_scenario_condition_new(memory_scenarios):
    """
        Test that each condition is new
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        condition = scenario_data['condition']
        assert condition == "new", f"Condition is not new in {scenario_name}"


def test_memory_scenario_checkbox_false(memory_scenarios):
    """
        Test that each checkbox is false
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        checkbox = scenario_data['checkbox']
        assert checkbox == False, f"checkbox is not false in {scenario_name}"


def test_memory_scenario_active_true(memory_scenarios):
    """
        Test that each active is True
    """
    for scenario_name, scenario_data in memory_scenarios['scenarios'].items():
        active = scenario_data['active']
        assert active == True, f"checkbox is not True in {scenario_name}"

# Additional tests can be added to cover more specific aspects of the data
```