```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Provides the JSON data as a dictionary."""
    json_data = """
    {
      "scenarios": {
        "iPhone SE 2022": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..36192",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone SE 2022" }
          }
        },
        "iPhone 11": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..9580",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 12 MINI" }
          }
        },
        "iPhone 12 MINI": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/272..573..245..19218",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 12 MINI" }
          }
        },
        "iPhone 12": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..19213",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 12" }
          }
        },
        "iPhone 13": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..28963",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 MINI" }
          }
        },
        "iPhone 13 MINI": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..28917",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 MINI" }
          }
        },
        "iPhone 13 PRO": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..28976",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 PRO" }
          }
        },
        "iPhone 13 PRO MAX": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..29011",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 PRO MAX" }
          }
        },
        "iPhone 14": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..41141",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 14" }
          }
        },
        "iPhone 14 PLUS": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..42640",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 14 PLUS" }
          }
        },
        "iPhone 14 PRO": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..41142",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 14 PRO" }
          }
        },
        "iPhone 14 PRO MAX": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/573..245..41143",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": "iPhone 14 PRO MAX" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_ksp_categories_data_structure(ksp_categories_data):
    """
    Test if the loaded JSON data has the expected structure.
    """
    assert "scenarios" in ksp_categories_data
    assert isinstance(ksp_categories_data["scenarios"], dict)

def test_ksp_categories_each_scenario_has_required_keys(ksp_categories_data):
    """
    Test if each scenario within the data contains the expected keys.
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data
        assert isinstance(scenario_data["presta_categories"], dict)
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)

def test_ksp_categories_data_brand_is_apple(ksp_categories_data):
     """
     Test if the brand of each scenario is "APPLE"
     """
     for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
          assert scenario_data["brand"] == "APPLE"

def test_ksp_categories_checkbox_is_false(ksp_categories_data):
    """
    Test if checkbox is false for all scenarios
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] is False


def test_ksp_categories_active_is_true(ksp_categories_data):
    """
    Test if active is True for all scenarios
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
         assert scenario_data["active"] is True

def test_ksp_categories_condition_is_new(ksp_categories_data):
    """
    Test if condition is new for all scenarios
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

def test_ksp_categories_presta_categories_template_not_empty(ksp_categories_data):
     """
     Test if the template in presta_categories is not empty
     """
     for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert scenario_data["presta_categories"]["template"]
        assert isinstance(scenario_data["presta_categories"]["template"],dict)
        assert len(scenario_data["presta_categories"]["template"].keys()) > 0
        for template_key in scenario_data["presta_categories"]["template"].keys():
            assert template_key == "apple"

def test_ksp_categories_url_is_valid(ksp_categories_data):
      """
      Test if each url is a valid ksp url
      """
      for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
           url = scenario_data["url"]
           assert url.startswith("https://ksp.co.il/web/cat/")
```