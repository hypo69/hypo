```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_samsung_data():
    """Loads the samsung data from the json file."""
    with open('hypotez/src/suppliers/ksp/scenarios/ksp_categories_phones_samsung.json', 'r') as f:
        return json.load(f)


def test_ksp_samsung_data_structure(ksp_samsung_data):
    """
    Test that the loaded data is a dictionary with a 'scenarios' key.
    Also checks that scenarios key contains a dictionary.
    """
    assert isinstance(ksp_samsung_data, dict)
    assert 'scenarios' in ksp_samsung_data
    assert isinstance(ksp_samsung_data['scenarios'], dict)

def test_ksp_samsung_scenario_keys(ksp_samsung_data):
    """
    Test that each scenario within 'scenarios' has the expected keys:
    'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' data is not a dictionary"
        assert 'brand' in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key"
        assert 'url' in scenario_data, f"Scenario '{scenario_name}' missing 'url' key"
        assert 'checkbox' in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key"
        assert 'active' in scenario_data, f"Scenario '{scenario_name}' missing 'active' key"
        assert 'condition' in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key"
        assert 'presta_categories' in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key"
        assert isinstance(scenario_data['presta_categories'], dict), f"Scenario '{scenario_name}' presta_categories is not a dictionary"
        assert 'template' in scenario_data['presta_categories'], f"Scenario '{scenario_name}' missing 'template' key in presta_categories"
        assert isinstance(scenario_data['presta_categories']['template'], dict), f"Scenario '{scenario_name}' template is not a dictionary"

def test_ksp_samsung_scenario_values_types(ksp_samsung_data):
    """
    Test that values within each scenario have the expected data types.
    Checks if 'brand' and 'condition' are strings, 'url' is a string,
    'checkbox' and 'active' are booleans and 'presta_categories' is a dictionary.
    """
    for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        assert isinstance(scenario_data['brand'], str), f"Scenario '{scenario_name}' 'brand' is not a string"
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' 'url' is not a string"
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean"
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' 'active' is not a boolean"
        assert isinstance(scenario_data['condition'], str), f"Scenario '{scenario_name}' 'condition' is not a string"

def test_ksp_samsung_scenario_url_format(ksp_samsung_data):
    """
    Test that the URL in each scenario is a valid string that starts with "https://ksp.co.il/web/cat/".
    """
    for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        url = scenario_data['url']
        assert url.startswith("https://ksp.co.il/web/cat/"), f"Scenario '{scenario_name}' URL '{url}' does not start with 'https://ksp.co.il/web/cat/'"

def test_ksp_samsung_presta_template(ksp_samsung_data):
    """
     Test that the presta_categories template has the correct 'samsung' key and that the value is string.
    """
    for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        template = scenario_data['presta_categories']['template']
        assert 'samsung' in template, f"Scenario '{scenario_name}' missing 'samsung' key in template"
        assert isinstance(template['samsung'], str), f"Scenario '{scenario_name}' 'samsung' value in template is not a string"
        assert template['samsung'] == scenario_name, f"Scenario '{scenario_name}' samsung value in template '{template['samsung']}' is not equal to scenario name"

def test_ksp_samsung_scenario_active_is_true(ksp_samsung_data):
    """
    Test that all scenario 'active' values are true.
    """
    for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        assert scenario_data['active'] is True, f"Scenario '{scenario_name}' 'active' is not True"
    
def test_ksp_samsung_scenario_condition_is_new(ksp_samsung_data):
     """
    Test that all scenario 'condition' values are 'new'.
    """
     for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        assert scenario_data['condition'] == 'new', f"Scenario '{scenario_name}' 'condition' is not 'new'"

def test_ksp_samsung_scenario_checkbox_is_false(ksp_samsung_data):
    """
    Test that all scenario 'checkbox' values are false.
    """
    for scenario_name, scenario_data in ksp_samsung_data['scenarios'].items():
        assert scenario_data['checkbox'] is False, f"Scenario '{scenario_name}' 'checkbox' is not False"
```