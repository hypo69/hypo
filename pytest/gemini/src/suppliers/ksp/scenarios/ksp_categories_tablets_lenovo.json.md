```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_lenovo_tablets_data():
    """Loads the JSON data for testing."""
    file_location = 'hypotez/src/suppliers/ksp/scenarios/ksp_categories_tablets_lenovo.json'
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data


def test_ksp_lenovo_tablets_data_structure(ksp_lenovo_tablets_data):
    """
    Test that the loaded JSON data has the expected structure.
    Checks for the presence of 'scenarios' key, and that it's a dict.
    """
    assert "scenarios" in ksp_lenovo_tablets_data
    assert isinstance(ksp_lenovo_tablets_data["scenarios"], dict)

def test_ksp_lenovo_tablets_scenario_keys(ksp_lenovo_tablets_data):
    """
    Test that each scenario in the JSON has the expected keys.
    Checks for the presence of 'brand', 'url', 'checkbox', 'active','condition', and 'presta_categories' keys
    in each scenario.
    """
    for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_ksp_lenovo_tablets_brand_values(ksp_lenovo_tablets_data):
      """
      Test that the brand value is always LENOVO in all scenarios.
      """
      for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
        assert scenario_data["brand"] == "LENOVO"

def test_ksp_lenovo_tablets_checkbox_values(ksp_lenovo_tablets_data):
      """
      Test that the checkbox value is always false in all scenarios.
      """
      for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
        assert scenario_data["checkbox"] == False

def test_ksp_lenovo_tablets_active_values(ksp_lenovo_tablets_data):
        """
        Test that the active value is always True in all scenarios.
        """
        for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
          assert scenario_data["active"] == True

def test_ksp_lenovo_tablets_condition_values(ksp_lenovo_tablets_data):
        """
        Test that the condition value is always new in all scenarios.
        """
        for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
            assert scenario_data["condition"] == "new"

def test_ksp_lenovo_tablets_presta_categories_types(ksp_lenovo_tablets_data):
    """
    Test the 'presta_categories' values, they can be dict or string type.
    Checks that the 'presta_categories' are either a dictionary or a string
    """
    for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], (dict,str))

def test_ksp_lenovo_tablets_presta_categories_dict_values(ksp_lenovo_tablets_data):
     """
     Test if 'presta_categories' is a dict, check if each key is a string and value also a string
     """
     for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
        if isinstance(scenario_data["presta_categories"], dict):
            for key,value in scenario_data["presta_categories"].items():
                assert isinstance(key,str)
                assert isinstance(value,str)

def test_ksp_lenovo_tablets_presta_categories_str_values(ksp_lenovo_tablets_data):
    """
    Test if 'presta_categories' is a string, check if it has correct format
    it should be comma separated values
    """
    for scenario_name, scenario_data in ksp_lenovo_tablets_data["scenarios"].items():
        if isinstance(scenario_data["presta_categories"], str):
            assert all(item.isdigit() for item in scenario_data["presta_categories"].split(','))
```