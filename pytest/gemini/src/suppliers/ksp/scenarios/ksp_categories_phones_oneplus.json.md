```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_data():
    """Loads the JSON data from the provided string."""
    json_data = """
    {
      "scenarios": {
        "ONEPLUS NORD 2": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..27278",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS NORD 2"
            }
          }
        },
        "ONEPLUS NORD CE": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..26037",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS NORD CE"
            }
          }
        },
        "ONEPLUS 8 PRO": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..13340",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS 8 PRO"
            }
          }
        },
        "ONEPLUS 8T": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..19689",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS 8T"
            }
          }
        },
        "ONEPLUS 9": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..24484",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS 9"
            }
          }
        },
        "ONEPLUS 9 PRO": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..26171",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS 9 PRO"
            }
          }
        },
        "ONEPLUS NORD N20 SE": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..42032",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS NORD N20 SE"
            }
          }
        },
        "ONEPLUS NORD CE 2 5G": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..36632",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS NORD CE 2 5G"
            }
          }
        },
        "ONEPLUS NORD CE 2 LITE 5G": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..38693",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS NORD CE 2 5G"
            }
          }
        },
        "ONEPLUS NORD 2T 5G": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..38706",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS NORD 2T 5G"
            }
          }
        },
         "ONEPLUS 9 Pro 5G": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..26171",
          "checkbox": false,
          "active": true,
          "condition": "new",
           "presta_categories": {
              "template": {
                "oneplus": "ONEPLUS NORD 2T 5G"
             }
          }
        },
        "ONEPLUS 10 PRO 5G": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..36978",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS 10 PRO 5G"
            }
          }
        },
        "ONEPLUS 10T": {
          "brand": "ONEPLUS",
          "url": "https://ksp.co.il/web/cat/272..573..2190..43056",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "oneplus": "ONEPLUS 10T"
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)


def test_ksp_data_load(ksp_data):
    """
    Test that the fixture loads the JSON data successfully.
    """
    assert isinstance(ksp_data, dict), "Data should be a dictionary"
    assert "scenarios" in ksp_data, "Data should contain 'scenarios' key"
    assert isinstance(ksp_data["scenarios"], dict), "'scenarios' should be a dictionary"


def test_scenario_keys_exist(ksp_data):
    """
    Test that all scenarios have the expected keys.
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key"
        assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key"
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key"
        assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key"
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key"
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key"


def test_scenario_values_types(ksp_data):
    """
    Test that values in scenarios have the expected type.
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' should be a string"
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' should be a string"
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' should be a boolean"
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' should be a boolean"
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' should be a string"
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' should be a dict"


def test_presta_categories_structure(ksp_data):
    """
     Test that 'presta_categories' has the correct nested structure
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
       presta_categories = scenario_data.get("presta_categories", {})
       assert isinstance(presta_categories, dict), f"Scenario '{scenario_name}': presta_categories should be a dictionary"

       template = presta_categories.get("template", {})
       assert isinstance(template, dict), f"Scenario '{scenario_name}': 'template' in 'presta_categories' should be a dictionary"

       assert len(template) > 0, f"Scenario '{scenario_name}': 'template' in 'presta_categories' should not be empty"

       for key, value in template.items():
           assert isinstance(key, str), f"Scenario '{scenario_name}': Key in 'template' should be a string"
           assert isinstance(value, str), f"Scenario '{scenario_name}': Value in 'template' should be a string"

def test_url_format(ksp_data):
     """
     Test that the 'url' values follow the expected format
     """
     for scenario_name, scenario_data in ksp_data["scenarios"].items():
         url = scenario_data.get("url")
         assert url.startswith("https://ksp.co.il/web/cat/"), f"Scenario '{scenario_name}': 'url' should start with 'https://ksp.co.il/web/cat/'"
         assert ".." in url , f"Scenario '{scenario_name}': 'url' should contain '..'"


def test_all_brands_are_oneplus(ksp_data):
    """
    Test that all brands are 'ONEPLUS'.
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert scenario_data["brand"] == "ONEPLUS", f"Scenario '{scenario_name}' brand is not 'ONEPLUS'"


def test_all_conditions_are_new(ksp_data):
     """
     Test that all conditions are 'new'
     """
     for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario '{scenario_name} condition is not 'new' "


def test_active_is_true(ksp_data):
    """
    Test that all 'active' fields are True
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
       assert scenario_data["active"] == True, f"Scenario '{scenario_name} 'active' is not true"


def test_checkbox_is_false(ksp_data):
    """
    Test that all checkbox fields are False
    """
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name} 'checkbox' is not false"


```