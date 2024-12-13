```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data for testing."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_laptops_lenovo.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['scenarios']

# Test for valid data structure and keys
def test_valid_data_structure(morlevi_categories_data):
    """
    Checks if the loaded JSON data has the expected structure and keys.
    Verifies that each scenario has the expected keys
    """
    assert isinstance(morlevi_categories_data, dict)
    for scenario_name, scenario_data in morlevi_categories_data.items():
       assert isinstance(scenario_data, dict), f"Scenario {scenario_name} is not a dict"
       assert 'brand' in scenario_data, f"Scenario {scenario_name} missing 'brand' key"
       assert 'url' in scenario_data, f"Scenario {scenario_name} missing 'url' key"
       assert 'checkbox' in scenario_data, f"Scenario {scenario_name} missing 'checkbox' key"
       assert 'active' in scenario_data, f"Scenario {scenario_name} missing 'active' key"
       assert 'condition' in scenario_data, f"Scenario {scenario_name} missing 'condition' key"
       assert 'presta_categories' in scenario_data, f"Scenario {scenario_name} missing 'presta_categories' key"
       assert isinstance(scenario_data['presta_categories'], dict), f"Scenario {scenario_name}'s 'presta_categories' is not a dict"
       assert 'template' in scenario_data['presta_categories'], f"Scenario {scenario_name} missing 'template' key in 'presta_categories'"
       assert isinstance(scenario_data['presta_categories']['template'], dict), f"Scenario {scenario_name}'s 'template' is not a dict"


# Test to check if 'brand' is always "LENOVO"
def test_brand_is_lenovo(morlevi_categories_data):
    """
    Checks if the 'brand' field for all scenarios is consistently 'LENOVO'.
    """
    for scenario_name, scenario_data in morlevi_categories_data.items():
        assert scenario_data['brand'] == "LENOVO", f"Scenario {scenario_name} has a brand other than LENOVO"

# Test to check if 'condition' is always "new"
def test_condition_is_new(morlevi_categories_data):
    """
     Checks if the 'condition' field for all scenarios is consistently 'new'.
    """
    for scenario_name, scenario_data in morlevi_categories_data.items():
        assert scenario_data['condition'] == "new", f"Scenario {scenario_name} has a condition other than 'new'"

# Test to ensure 'checkbox' is always False
def test_checkbox_is_false(morlevi_categories_data):
    """
     Checks if the 'checkbox' field for all scenarios is consistently False.
    """
    for scenario_name, scenario_data in morlevi_categories_data.items():
        assert scenario_data['checkbox'] is False, f"Scenario {scenario_name} has a checkbox value other than False"

# Test to ensure 'active' is always True
def test_active_is_true(morlevi_categories_data):
    """
    Checks if the 'active' field for all scenarios is consistently True.
    """
    for scenario_name, scenario_data in morlevi_categories_data.items():
        assert scenario_data['active'] is True, f"Scenario {scenario_name} has an active value other than True"

# Test to validate 'presta_categories' template structure
def test_presta_categories_template_structure(morlevi_categories_data):
    """
    Checks if 'presta_categories' -> 'template' is structured correctly.
    Verifies that 'template' is a dict with a 'LENOVO' key and a list as its value.
    """
    for scenario_name, scenario_data in morlevi_categories_data.items():
       template = scenario_data['presta_categories']['template']
       assert isinstance(template, dict), f"Template in scenario {scenario_name} is not a dictionary"
       assert "LENOVO" in template, f"Template in scenario {scenario_name} does not have a 'LENOVO' key"
       assert isinstance(template['LENOVO'], list), f"'LENOVO' value in scenario {scenario_name} template is not a list"
       assert len(template['LENOVO']) == 2, f"'LENOVO' value in scenario {scenario_name} does not have 2 elements"


# Test to ensure URL is either None or a valid string
def test_url_valid_format(morlevi_categories_data):
    """
    Checks if the URL is either None or a valid string.
    If it is a string, it checks if it starts with "https://www.morlevi.co.il"
    """
    for scenario_name, scenario_data in morlevi_categories_data.items():
       url = scenario_data['url']
       if url is not None:
           assert isinstance(url, str), f"Scenario {scenario_name} has url that is not a string or None"
           assert url.startswith("https://www.morlevi.co.il"), f"Scenario {scenario_name} has url that does not start with the required prefix"

# Test edge case when all fields are in their default states (not applicable here)

#Test to validate edge cases with AMD RYZEN scenarios
def test_amd_ryzen_scenarios(morlevi_categories_data):
    """
    Checks specific scenarios involving AMD Ryzen processors.
    Verifies that categories are correct for specific models
    """
    amd_ryzen_5_scenario = morlevi_categories_data.get("LENOVO 15 AMD RYZEN 5")
    assert amd_ryzen_5_scenario is not None, "LENOVO 15 AMD RYZEN 5 scenario not found"
    assert amd_ryzen_5_scenario['presta_categories']['template']['gigabyte'] == ["LAPTOPS AMD RYZEN 5", "15"], "Category is incorrect for LENOVO 15 AMD RYZEN 5"

    amd_ryzen_7_scenario_1 = morlevi_categories_data.get("LENOVO 14 AMD RYZEN 7")
    assert amd_ryzen_7_scenario_1 is not None, "LENOVO 14 AMD RYZEN 7 scenario not found"
    assert amd_ryzen_7_scenario_1['presta_categories']['template']['LENOVO'] == ["LAPTOPS INTEL I7", "14"], "Category is incorrect for LENOVO 14 AMD RYZEN 7"

    amd_ryzen_7_scenario_2 = morlevi_categories_data.get("LENOVO 15 AMD RYZEN 7")
    assert amd_ryzen_7_scenario_2 is not None, "LENOVO 15 AMD RYZEN 7 scenario not found"
    assert amd_ryzen_7_scenario_2['presta_categories']['template']['LENOVO'] == ["LAPTOPS AMD RYZEN 7", "15"], "Category is incorrect for LENOVO 15 AMD RYZEN 7"
```