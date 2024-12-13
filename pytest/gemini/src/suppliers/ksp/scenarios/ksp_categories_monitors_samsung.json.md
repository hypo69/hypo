```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Provides the ksp categories data from the json file."""
    with open('hypotez/src/suppliers/ksp/scenarios/ksp_categories_monitors_samsung.json', 'r') as f:
        return json.load(f)

# Test to check if the data is loaded correctly and is a dict
def test_ksp_categories_data_is_dict(ksp_categories_data):
    """Checks that the loaded data is a dictionary."""
    assert isinstance(ksp_categories_data, dict)

# Test to check if 'scenarios' key exists
def test_ksp_categories_scenarios_key_exists(ksp_categories_data):
    """Checks that the 'scenarios' key exists in the data."""
    assert 'scenarios' in ksp_categories_data

# Test to check if 'scenarios' value is a dict
def test_ksp_categories_scenarios_is_dict(ksp_categories_data):
    """Checks that the 'scenarios' value is a dictionary."""
    assert isinstance(ksp_categories_data['scenarios'], dict)


# Test to check a specific scenario's properties
def test_ksp_categories_scenario_22_properties(ksp_categories_data):
    """Checks properties of the '22' scenario."""
    scenario_22 = ksp_categories_data['scenarios']['22']
    assert scenario_22['brand'] == "SAMSUNG"
    assert scenario_22['url'] == "https://ksp.co.il/web/cat/230..137..195"
    assert scenario_22['checkbox'] == False
    assert scenario_22['active'] == True
    assert scenario_22['condition'] == "new"
    assert scenario_22['presta_categories']['template']['samsung'] == "PC MONITORS 21 - 22"

# Test to check another specific scenario's properties
def test_ksp_categories_scenario_23_24_properties(ksp_categories_data):
    """Checks properties of the '23 - 24' scenario."""
    scenario_23_24 = ksp_categories_data['scenarios']['23 - 24']
    assert scenario_23_24['brand'] == "SAMSUNG"
    assert scenario_23_24['url'] == "https://ksp.co.il/web/cat/230..137..2238..1649..198"
    assert scenario_23_24['checkbox'] == False
    assert scenario_23_24['active'] == True
    assert scenario_23_24['condition'] == "new"
    assert scenario_23_24['presta_categories']['template']['samsung'] == "PC MONITORS 23 - 24"

# Test to check a scenario with more nested urls
def test_ksp_categories_scenario_26_28_properties(ksp_categories_data):
    """Checks properties of the '26 - 28' scenario."""
    scenario_26_28 = ksp_categories_data['scenarios']['26 - 28']
    assert scenario_26_28['brand'] == "SAMSUNG"
    assert scenario_26_28['url'] == "https://ksp.co.il/web/cat/230..137..4831..199..4784..2037"
    assert scenario_26_28['checkbox'] == False
    assert scenario_26_28['active'] == True
    assert scenario_26_28['condition'] == "new"
    assert scenario_26_28['presta_categories']['template']['samsung'] == "PC MONITORS 26 - 28"

# Test to check if all scenarios have the required keys
def test_ksp_categories_all_scenarios_have_required_keys(ksp_categories_data):
    """Checks if all scenarios contain the required keys."""
    required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_key, scenario_data in ksp_categories_data['scenarios'].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_key}' is missing key: {key}"

# Test to check 'presta_categories' template exists
def test_ksp_categories_presta_categories_template_exists(ksp_categories_data):
    """Checks if 'presta_categories' and 'template' exist for all scenarios."""
    for scenario_key, scenario_data in ksp_categories_data['scenarios'].items():
        assert 'presta_categories' in scenario_data, f"Scenario '{scenario_key}' is missing 'presta_categories'"
        assert 'template' in scenario_data['presta_categories'], f"Scenario '{scenario_key}' is missing 'template' in 'presta_categories'"

# Test to check 'presta_categories' template has 'samsung' key
def test_ksp_categories_presta_categories_template_samsung_exists(ksp_categories_data):
    """Checks if 'samsung' key exists in 'presta_categories.template' for all scenarios."""
    for scenario_key, scenario_data in ksp_categories_data['scenarios'].items():
        assert 'samsung' in scenario_data['presta_categories']['template'], f"Scenario '{scenario_key}' is missing 'samsung' in 'presta_categories.template'"

# Test to ensure all urls are valid strings
def test_ksp_categories_url_is_string(ksp_categories_data):
    """Checks if all the urls are strings"""
    for scenario_key, scenario_data in ksp_categories_data['scenarios'].items():
      assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_key}' url is not a string"

#Test to ensure all brands are "SAMSUNG"
def test_ksp_categories_brand_is_samsung(ksp_categories_data):
    """Checks if all brands are 'SAMSUNG'"""
    for scenario_key, scenario_data in ksp_categories_data['scenarios'].items():
        assert scenario_data['brand'] == "SAMSUNG", f"Scenario '{scenario_key}' brand is not SAMSUNG"
```