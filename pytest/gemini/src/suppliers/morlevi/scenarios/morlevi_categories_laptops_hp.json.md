```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data for the tests."""
    json_data = """
    {
      "scenarios": {
        "HP 11.6 I3": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I3", "11" ]
            }
          }
        },
        "HP 11.6 I5": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I5", "11" ]
            }
          }
        },
        "HP 11.6 I7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I7", "11" ]
            }
          }
        },
        "HP 11.6 I9": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I9", "11" ]
            }
          }
        },
        "HP 11.6 AMD": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS AMD", "11" ]
            }
          }
        },
        "HP 11.6 Celeron": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "11" ]
            }
          }
        },
        "HP 11.6 Pentium": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "11" ]
            }
          }
        },
        "HP 13.4 - 13.3 I3": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I3", "13" ]
            }
          }
        },
        "HP 13.4 - 13.3 I5": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I5", "13" ]
            }
          }
        },
        "HP 13.4 - 13.3 I7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I7", "13" ]
            }
          }
        },
        "HP 13.4 - 13.3 I9": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I9", "13" ]
            }
          }
        },
        "HP 13.4 - 13.3 AMD": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS AMD", "13" ]
            }
          }
        },
        "HP 13.4 - 13.3 Celeron": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "13" ]
            }
          }
        },
        "HP 13.4 - 13.3 Pentium": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "13" ]
            }
          }
        },
        "HP 14 I3": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I3", "14" ]
            }
          }
        },
        "HP 14 I5": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I5", "14" ]
            }
          }
        },
        "HP 14 I7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
        "HP 14 I9": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I9", "14" ]
            }
          }
        },
        "HP 14 AMD RYZEN 7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
        "HP 14 Celeron": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "14" ]
            }
          }
        },
        "HP 14 Pentium": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "14" ]
            }
          }
        },
        "HP 15 I3": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I3", "15" ]
            }
          }
        },
        "HP 15 I5": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I5", "15" ]
            }
          }
        },
        "HP 15 I7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I7", "15" ]
            }
          }
        },
        "HP 15 I9": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I9", "15" ]
            }
          }
        },
        "HP 15 AMD RYZEN 5": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "gigabyte": [ "LAPTOPS AMD RYZEN 5", "15" ]
            }
          }
        },
        "HP 15 AMD RYZEN 7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS AMD RYZEN 7", "15" ]
            }
          }
        },
        "HP 15 Celeron": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "15" ]
            }
          }
        },
        "HP 15 Pentium": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "15" ]
            }
          }
        },
        "HP 17.3 I3": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I3", "17" ]
            }
          }
        },
        "HP 17.3 I5": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I5", "17" ]
            }
          }
        },
        "HP 17.3 I7": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I7", "17" ]
            }
          }
        },
        "HP 17.3 I9": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL I9", "17" ]
            }
          }
        },
        "HP 17.3 AMD": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS AMD", "17" ]
            }
          }
        },
        "HP 17.3 Celeron": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "17" ]
            }
          }
        },
        "HP 17.3 Pentium": {
          "brand": "HP",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "HP": [ "LAPTOPS INTEL CELERON", "17" ]
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test to verify the basic structure of the loaded JSON data.
    Checks if the 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)


def test_morlevi_scenario_keys(morlevi_categories_data):
    """
    Test to verify that each scenario has the expected keys.
    Checks for 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories' in each scenario.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data


def test_morlevi_presta_categories_structure(morlevi_categories_data):
    """
    Test to verify the structure of 'presta_categories'.
    Checks if 'presta_categories' has a 'template' key and it is a dictionary.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "presta_categories" in scenario_data
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)


def test_morlevi_template_values_are_lists(morlevi_categories_data):
    """
    Test to verify that the values inside the 'template' dictionaries are lists.
    Checks if each value in 'template' is a list.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        template = scenario_data["presta_categories"]["template"]
        for key, value in template.items():
            assert isinstance(value, list)
            assert len(value) == 2


def test_morlevi_brand_values(morlevi_categories_data):
    """
    Test to verify that the 'brand' is always "HP".
    Checks if the value of the key 'brand' is always 'HP'
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert scenario_data["brand"] == "HP"


def test_morlevi_url_values(morlevi_categories_data):
      """
    Test to verify that the 'url' is always null.
    Checks if the value of the key 'url' is always null
    """
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
            assert scenario_data["url"] == None


def test_morlevi_checkbox_values(morlevi_categories_data):
      """
    Test to verify that the 'checkbox' is always False.
    Checks if the value of the key 'checkbox' is always False
    """
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
            assert scenario_data["checkbox"] == False


def test_morlevi_active_values(morlevi_categories_data):
      """
    Test to verify that the 'active' is always True.
    Checks if the value of the key 'active' is always True
    """
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
            assert scenario_data["active"] == True


def test_morlevi_condition_values(morlevi_categories_data):
      """
    Test to verify that the 'condition' is always new.
    Checks if the value of the key 'condition' is always new
    """
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
            assert scenario_data["condition"] == "new"


def test_morlevi_amd_ryzen_5_brand(morlevi_categories_data):
    """
    Test to verify that the "HP 15 AMD RYZEN 5" scenario uses the "gigabyte" template.
    Checks the 'presta_categories' of the  "HP 15 AMD RYZEN 5" scenario.
    """
    amd_ryzen_5_scenario = morlevi_categories_data["scenarios"].get("HP 15 AMD RYZEN 5")
    assert amd_ryzen_5_scenario is not None
    assert "gigabyte" in amd_ryzen_5_scenario["presta_categories"]["template"]
    assert amd_ryzen_5_scenario["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS AMD RYZEN 5", "15"]

def test_morlevi_valid_data_types(morlevi_categories_data):
    """
    Test to verify that data types are as expected.
    Checks if the values have the expected data type
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert scenario_data["url"] is None
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], dict)

```