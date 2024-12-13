```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_cpu_data():
    """Loads the morlevi_categories_cpu.json data."""
    json_data = """
    {
      "scenarios": {
        "Intel  CELERON LGA1200 Gen 10": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/337?p_134=584&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "INTEL CELERON LGA1200"
            }
          }
        },
        "Intel  CELERON LGA1200 Gen 11": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/363?p_134=584&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "INTEL CELERON LGA1200"
            }
          }
        },
        "Intel  PENTIUM LGA1200 Gen 10": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/337?p_134=585&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "INTEL PENTIUM LGA1200"
            }
          }
        },
        "I3 LGA1200": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/337?p_134=586&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I3 LGA1200"
            }
          }
        },
        "I5 LGA1200": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/399?p_134=587&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I5 LGA1200"
            }
          }
        },
        "I5 LGA1200 11": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/363?p_134=587&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I5 LGA1200"
            }
          }
        },
        "I5 LGA1700 12": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/380?p_134=587&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I5 LGA1700"
            }
          }
        },
        "I5 LGA1700 13": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/399",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I5 LGA1700"
            }
          }
        },
        "I7 LGA1200": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I7 LGA1200"
            }
          }
        },
        "I7 LGA1200 11": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/363?p_134=588&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I7 LGA1200"
            }
          }
        },
        "I7 LGA1700 12": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/380?p_134=588&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I7 LGA1700"
            }
          }
        },
        "I7 LGA1700 13": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/399",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I7 LGA1700"
            }
          }
        },
        "I9 LGA1200": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I7 LGA1200"
            }
          }
        },
        "I9 LGA1700 12": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/380",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I9 LGA1700"
            }
          }
        },
        "I9 LGA1700 13": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/399?p_134=848&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": {
              "cpu": "I9 LGA1700"
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)



def test_morlevi_categories_cpu_data_structure(morlevi_categories_cpu_data):
    """
    Test that the loaded data has the correct structure.
    Ensures the top-level is a dictionary with a 'scenarios' key,
    and that 'scenarios' is a dictionary.
    """
    assert isinstance(morlevi_categories_cpu_data, dict)
    assert "scenarios" in morlevi_categories_cpu_data
    assert isinstance(morlevi_categories_cpu_data["scenarios"], dict)


def test_scenario_keys(morlevi_categories_cpu_data):
    """
    Test that each scenario has the expected keys.
    Checks for the presence of 'brand', 'url', 'checkbox', 'active', 'presta_categories','condition' keys in each scenario.
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "presta_categories" in scenario_data
        assert "condition" in scenario_data


def test_scenario_data_types(morlevi_categories_cpu_data):
     """
    Test that each scenario has the expected data types for each key.
    Checks if 'brand' and 'url' are strings, 'checkbox' and 'active' are booleans, and 'presta_categories' is a dictionary.
    """
     for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["presta_categories"], dict)
        assert isinstance(scenario_data["condition"], str)

def test_presta_categories_structure(morlevi_categories_cpu_data):
    """
    Test the structure of the 'presta_categories' dictionary within each scenario.
    Checks if 'presta_categories' contains a 'template' key, and if 'template' is a dictionary.
    """
    for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)


def test_presta_categories_template_values(morlevi_categories_cpu_data):
     """
    Test that 'template' dictionary within 'presta_categories' has string values for cpu.
    """
     for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert "cpu" in scenario_data["presta_categories"]["template"]
        assert isinstance(scenario_data["presta_categories"]["template"]["cpu"], str)

def test_all_urls_are_strings(morlevi_categories_cpu_data):
    """
    Test that all the 'url' values in the scenarios are strings and not empty.
    """
    for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)
        assert scenario_data["url"] != ""


def test_all_brands_are_strings(morlevi_categories_cpu_data):
    """
    Test that all the 'brand' values in the scenarios are strings and not empty.
    """
    for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert scenario_data["brand"] != ""

def test_condition_values(morlevi_categories_cpu_data):
    """
    Test that all the 'condition' values in the scenarios are strings and not empty and is 'new'
    """
    for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str)
        assert scenario_data["condition"] == "new"


def test_checkbox_values_are_false(morlevi_categories_cpu_data):
    """
    Test that all 'checkbox' values are False
    """
    for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert scenario_data["checkbox"] is False


def test_active_values_are_true(morlevi_categories_cpu_data):
    """
        Test that all 'active' values are True
    """
    for _, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert scenario_data["active"] is True

def test_scenario_names_are_strings(morlevi_categories_cpu_data):
    """
    Test that the scenario names are strings and not empty.
    """
    for scenario_name in morlevi_categories_cpu_data["scenarios"].keys():
        assert isinstance(scenario_name, str)
        assert scenario_name != ""
```