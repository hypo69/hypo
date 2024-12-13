```python
import pytest
import json

# Fixture for loading the json data
@pytest.fixture
def ksp_categories_data():
    """Provides the loaded JSON data for tests."""
    json_data = """
    {
      "scenarios": {
        "In-ear Bud": {
          "brand": "XIAOMI",
          "url": "https://ksp.co.il/web/cat/242..2202..1250",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3459": "In-ear Bud",
            "3198": "CONSUMER ELECTRONICS",
            "3433": "Smartphones smart devices",
            "3436": "Speakers & Audio",
            "3454": "Headphones in Speakers & Audio",
            "4206": "BT Connection",
            "3460": "In-ear Buds",
            "3437": "TV & Audio",
            "3997": "Headphones in TV & Audio",
            "4218": "BT in TV & Audio",
            "4018": "BT In-ear Bud in TV & Audio",
            "2250": "brand:  XIAOMI",
            "4245": "Xiaoimi BT Headphones"
          }
        },
        "Xiaomi Mi In-ear Bud cable 3.5mm connection": {
          "brand": "XIAOMI",
          "url": "https://ksp.co.il/web/cat/242..2202..1250..5162",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3459": "Xiaomi Mi In-ear Bud cable 3.5mm connection",
            "3198": "CONSUMER ELECTRONICS",
            "3433": "Smartphones smart devices",
            "3436": "Speakers & Audio",
            "3454": "Headphones in Speakers & Audio",
            "4206": "BT Connection",
            "3460": "In-ear Buds",
            "3437": "TV & Audio",
            "3997": "Headphones in TV & Audio",
            "4218": "BT in TV & Audio",
            "4018": "BT In-ear Bud in TV & Audio",
            "2250": "brand:  XIAOMI",
            "2479": "BT Earbuds",
            "3494": "Redmi Buds 3"
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_ksp_categories_data_loaded(ksp_categories_data):
    """Checks if the fixture loads data correctly and is not empty."""
    assert ksp_categories_data is not None
    assert isinstance(ksp_categories_data, dict)
    assert "scenarios" in ksp_categories_data
    assert len(ksp_categories_data["scenarios"]) > 0


def test_scenario_keys_exist(ksp_categories_data):
    """Checks if the required keys are present in each scenario."""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert "brand" in scenario_data
      assert "url" in scenario_data
      assert "checkbox" in scenario_data
      assert "active" in scenario_data
      assert "condition" in scenario_data
      assert "presta_categories" in scenario_data


def test_scenario_brand_value(ksp_categories_data):
    """Checks if brand is correct in each scenario."""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert scenario_data["brand"] == "XIAOMI"

def test_scenario_url_value(ksp_categories_data):
    """Checks if urls in each scenario are not empty strings"""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)
        assert len(scenario_data["url"]) > 0


def test_scenario_checkbox_value_is_boolean(ksp_categories_data):
    """Checks if the checkbox value is a boolean in each scenario"""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert isinstance(scenario_data["checkbox"], bool)

def test_scenario_active_value_is_boolean(ksp_categories_data):
    """Checks if the active value is a boolean in each scenario"""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
      assert isinstance(scenario_data["active"], bool)
      

def test_scenario_condition_value(ksp_categories_data):
    """Checks if condition is correct in each scenario."""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

def test_scenario_presta_categories_not_empty(ksp_categories_data):
    """Checks if 'presta_categories' is a dictionary and not empty for each scenario."""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], dict)
        assert len(scenario_data["presta_categories"]) > 0
        

def test_scenario_presta_categories_keys_are_strings(ksp_categories_data):
    """Checks if keys in 'presta_categories' are strings for each scenario."""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        for key in scenario_data["presta_categories"].keys():
            assert isinstance(key, str)
            
def test_scenario_presta_categories_values_are_strings(ksp_categories_data):
    """Checks if values in 'presta_categories' are strings for each scenario."""
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        for value in scenario_data["presta_categories"].values():
            assert isinstance(value, str)
```