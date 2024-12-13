```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_nokia_data():
    """Loads the Nokia KSP categories JSON data."""
    file_path = 'hypotez/src/suppliers/ksp/scenarios/ksp_categories_phones_nokia.json'
    with open(file_path, 'r') as file:
        return json.load(file)

# Test cases for the structure of the data
def test_ksp_nokia_data_structure(ksp_nokia_data):
    """
    Test that the loaded JSON data has the 'scenarios' key
    and that it is a dictionary.
    """
    assert "scenarios" in ksp_nokia_data
    assert isinstance(ksp_nokia_data["scenarios"], dict)

def test_ksp_nokia_scenario_structure(ksp_nokia_data):
  """
    Test that each scenario in the 'scenarios' dictionary has the
    expected keys and value types.
  """
  for scenario_name, scenario_data in ksp_nokia_data["scenarios"].items():
    assert isinstance(scenario_name, str)
    assert isinstance(scenario_data, dict)
    assert "brand" in scenario_data
    assert isinstance(scenario_data["brand"], str)
    assert "url" in scenario_data
    assert isinstance(scenario_data["url"], str)
    assert "checkbox" in scenario_data
    assert isinstance(scenario_data["checkbox"], bool)
    assert "active" in scenario_data
    assert isinstance(scenario_data["active"], bool)
    assert "condition" in scenario_data
    assert isinstance(scenario_data["condition"], str)
    assert "presta_categories" in scenario_data
    assert isinstance(scenario_data["presta_categories"], dict)
    assert "template" in scenario_data["presta_categories"]
    assert isinstance(scenario_data["presta_categories"]["template"], dict)
    assert "nokia" in scenario_data["presta_categories"]["template"]
    assert isinstance(scenario_data["presta_categories"]["template"]["nokia"], str)

# Test cases for specific data values
def test_ksp_nokia_brand_values(ksp_nokia_data):
    """
    Test that all brands are "NOKIA"
    """
    for scenario_data in ksp_nokia_data["scenarios"].values():
       assert scenario_data["brand"] == "NOKIA"

def test_ksp_nokia_active_values(ksp_nokia_data):
  """
    Test that all active values are True.
  """
  for scenario_data in ksp_nokia_data["scenarios"].values():
    assert scenario_data["active"] == True

def test_ksp_nokia_condition_values(ksp_nokia_data):
  """
    Test that all conditions are 'new'.
  """
  for scenario_data in ksp_nokia_data["scenarios"].values():
    assert scenario_data["condition"] == "new"

def test_ksp_nokia_checkbox_values(ksp_nokia_data):
  """
    Test that all checkbox values are False.
  """
  for scenario_data in ksp_nokia_data["scenarios"].values():
      assert scenario_data["checkbox"] == False

def test_ksp_nokia_url_format(ksp_nokia_data):
    """
    Test that all URLs start with "https://ksp.co.il/web/cat/"
    """
    for scenario_data in ksp_nokia_data["scenarios"].values():
        assert scenario_data["url"].startswith("https://ksp.co.il/web/cat/")
    
def test_ksp_nokia_presta_category_not_empty(ksp_nokia_data):
    """
    Test that the 'nokia' presta categories are not empty
    """
    for scenario_data in ksp_nokia_data["scenarios"].values():
        assert len(scenario_data["presta_categories"]["template"]["nokia"]) > 0

def test_ksp_nokia_scenario_names_unique(ksp_nokia_data):
    """
    Test that scenario names are unique to avoid issues.
    """
    scenario_names = list(ksp_nokia_data['scenarios'].keys())
    assert len(scenario_names) == len(set(scenario_names))
```