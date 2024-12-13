```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the JSON data for tests."""
    
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_samsung.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test that the loaded JSON has the expected structure.
    It should be a dictionary with a 'scenarios' key.
    """
    assert isinstance(morlevi_categories_data, dict)
    assert 'scenarios' in morlevi_categories_data

def test_morlevi_categories_scenarios_not_empty(morlevi_categories_data):
      """
      Test that the 'scenarios' key is not empty.
      """
      assert morlevi_categories_data['scenarios']

def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test that each scenario in 'scenarios' has the expected keys.
    """
    expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
       assert all(key in scenario_data for key in expected_keys), f"Scenario '{scenario_name}' is missing one or more keys"


def test_morlevi_categories_scenario_values_type(morlevi_categories_data):
    """
    Test that the values for specific keys have the correct types.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['brand'], str), f"Brand in '{scenario_name}' is not a string."
        assert isinstance(scenario_data['url'], str), f"URL in '{scenario_name}' is not a string."
        assert isinstance(scenario_data['checkbox'], bool), f"Checkbox in '{scenario_name}' is not a boolean."
        assert isinstance(scenario_data['active'], bool), f"Active in '{scenario_name}' is not a boolean."
        assert isinstance(scenario_data['condition'], str), f"Condition in '{scenario_name}' is not a string."
        assert isinstance(scenario_data['presta_categories'], dict), f"presta_categories in '{scenario_name}' is not a dict."
        assert "template" in scenario_data["presta_categories"] ,f"template in '{scenario_name}' is not a in presta_categories."
        assert isinstance(scenario_data["presta_categories"]["template"], dict),  f"template in '{scenario_name}' is not a dict."

def test_morlevi_categories_url_valid(morlevi_categories_data):
    """
    Test that each URL in 'scenarios' is a valid URL string.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        url = scenario_data['url']
        assert url.startswith("https://"), f"URL in '{scenario_name}' does not start with 'https://'."
        assert "morlevi.co.il" in url, f"URL in '{scenario_name}' does not contain 'morlevi.co.il'."

def test_morlevi_categories_presta_categories_template_not_empty(morlevi_categories_data):
    """
    Test that 'presta_categories' -> 'template' dictionary is not empty in each scenario.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        template = scenario_data['presta_categories']['template']
        assert template, f"Template in '{scenario_name}' is empty."


def test_morlevi_categories_presta_categories_template_samsung_value_type(morlevi_categories_data):
    """
    Test that the 'samsung' value in 'presta_categories' -> 'template' is a string.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        template = scenario_data['presta_categories']['template']
        assert 'samsung' in template, f"'samsung' key not found in template of '{scenario_name}'"
        assert isinstance(template['samsung'], str), f"'samsung' value in template of '{scenario_name}' is not a string."

def test_morlevi_categories_all_scenarios_present(morlevi_categories_data):
    """
    Test that all expected scenarios are present in the data.
    """
    expected_scenarios = [
        "SAMSUNG NVME GEN4 512GB",
        "SAMSUNG NVME GEN4 1TB",
        "SAMSUNG NVME GEN4 2TB",
        "SAMSUNG SATA 3 256GB",
        "SAMSUNG SATA 3 512GB",
        "SAMSUNG SATA 3 1TB",
        "SAMSUNG SATA 3 2TB",
        "SAMSUNG SATA 3 4TB",
        "SAMSUNG SSD NVME PCIE 256GB ",
        "SAMSUNG SSD NVME PCIE 512GB ",
        "SAMSUNG SSD NVME PCIE 1TB ",
        "SAMSUNG SSD NVME PCIE 2TB "
    ]
    
    actual_scenarios = morlevi_categories_data['scenarios'].keys()
    for scenario in expected_scenarios:
      assert scenario in actual_scenarios, f"Expected scenario '{scenario}' is missing."

```