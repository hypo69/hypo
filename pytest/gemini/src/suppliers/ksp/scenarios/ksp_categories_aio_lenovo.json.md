```python
import pytest
import json

# Assuming the JSON data is loaded into a variable named 'data'
# For testing, we'll load it from a string, in reality, it would be loaded from the file
TEST_JSON_DATA = """
{
  "scenarios": {
    "IdeaCentre AIO 3-24ITL": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..28794",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "IdeaCentre 24" }
      }
    },
    "IdeaCentre AIO 3-24IAP7": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..38022",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "IdeaCentre 24" }
      }
    },
    "IdeaCentre AIO 5-24IOB": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..29670",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "IdeaCentre 24" }
      }
    },
    "IdeaCentre AIO 3-27ITL": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..30015",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "IdeaCentre 27" }
      }
    },
    "IdeaCentre AIO 3-27IAP7": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..38311",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "IdeaCentre 27" }
      }
    },
    "IdeaCentre AIO 5-27IOB": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..31370",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "IdeaCentre 27" }
      }
    },
    "Yoga AIO 7 27ACH6": {
      "brand": "LENOVO",
      "url": "https://ksp.co.il/web/cat/1513..159..34238",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": { "lenovo": "YOGA 27" }
      }
    }
  }
}
"""

@pytest.fixture
def ksp_lenovo_data():
    """Provides test data loaded from the JSON string."""
    return json.loads(TEST_JSON_DATA)


def test_ksp_lenovo_data_load(ksp_lenovo_data):
    """Checks if the fixture loads the JSON data correctly and is not empty."""
    assert ksp_lenovo_data is not None
    assert isinstance(ksp_lenovo_data, dict)
    assert "scenarios" in ksp_lenovo_data
    assert len(ksp_lenovo_data["scenarios"]) > 0


def test_ksp_lenovo_scenario_keys(ksp_lenovo_data):
    """Checks if all scenarios have the expected keys."""
    for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
         assert "brand" in scenario_data
         assert "url" in scenario_data
         assert "checkbox" in scenario_data
         assert "active" in scenario_data
         assert "condition" in scenario_data
         assert "presta_categories" in scenario_data
         assert "template" in scenario_data["presta_categories"]


def test_ksp_lenovo_scenario_values_types(ksp_lenovo_data):
     """Checks if the data types of the values are as expected."""
     for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str)
         assert isinstance(scenario_data["url"], str)
         assert isinstance(scenario_data["checkbox"], bool)
         assert isinstance(scenario_data["active"], bool)
         assert isinstance(scenario_data["condition"], str)
         assert isinstance(scenario_data["presta_categories"], dict)
         assert isinstance(scenario_data["presta_categories"]["template"], dict)


def test_ksp_lenovo_brand_value(ksp_lenovo_data):
    """Checks if the brand is always 'LENOVO'."""
    for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
        assert scenario_data["brand"] == "LENOVO"

def test_ksp_lenovo_url_valid(ksp_lenovo_data):
    """Checks if the URLs are valid strings and not empty"""
    for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
         assert isinstance(scenario_data["url"],str)
         assert len(scenario_data["url"]) > 0

def test_ksp_lenovo_presta_categories_template_not_empty(ksp_lenovo_data):
      """Checks that the template is not empty"""
      for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
          assert len(scenario_data["presta_categories"]["template"]) > 0

def test_ksp_lenovo_condition_value(ksp_lenovo_data):
      """Checks that the condition is always 'new'"""
      for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
           assert scenario_data["condition"] == "new"


def test_ksp_lenovo_checkbox_value(ksp_lenovo_data):
     """Checks that the checkbox is always False"""
     for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
         assert scenario_data["checkbox"] == False


def test_ksp_lenovo_active_value(ksp_lenovo_data):
    """Checks that the active is always True"""
    for scenario_name, scenario_data in ksp_lenovo_data["scenarios"].items():
        assert scenario_data["active"] == True
```