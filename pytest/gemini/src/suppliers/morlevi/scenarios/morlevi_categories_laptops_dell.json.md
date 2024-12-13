```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi categories JSON data."""
    json_data = """
    {
      "scenarios": {
        "DELL 11.6 I3": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I3", "11" ]
            }
          }
        },
        "DELL 11.6 I5": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I5", "11" ]
            }
          }
        },
        "DELL 11.6 I7": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I7", "11" ]
            }
          }
        },
        "DELL 11.6 I9": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I9", "11" ]
            }
          }
        },
        "DELL 11.6 AMD": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS AMD", "11" ]
            }
          }
        },
        "DELL 11.6 Celeron": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "11" ]
            }
          }
        },
        "DELL 11.6 Pentium": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "11" ]
            }
          }
        },
        "DELL 13.4 - 13.3 I3": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I3", "13" ]
            }
          }
        },
        "DELL 13.4 - 13.3 I5": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I5", "13" ]
            }
          }
        },
        "DELL 13.4 - 13.3 I7": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I7", "13" ]
            }
          }
        },
        "DELL 13.4 - 13.3 I9": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I9", "13" ]
            }
          }
        },
        "DELL 13.4 - 13.3 AMD": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS AMD", "13" ]
            }
          }
        },
        "DELL 13.4 - 13.3 Celeron": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELRON", "13" ]
            }
          }
        },
        "DELL 13.4 - 13.3 Pentium": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "13" ]
            }
          }
        },
        "DELL 14 I3": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I3", "14" ]
            }
          }
        },
        "DELL 14 I5": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I5", "14" ]
            }
          }
        },
        "DELL 14 I7": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
        "DELL 14 I9": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I9", "14" ]
            }
          }
        },
        "DELL 14 AMD": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS AMD", "14" ]
            }
          }
        },
        "DELL 14 Celeron": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "14" ]
            }
          }
        },
        "DELL 14 Pentium": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "14" ]
            }
          }
        },
        "DELL 15 I3": {
          "brand": "DELL",
          "url": "https://www.morlevi.co.il/Cat/1?p_315=7&p_238=1145&p_387=3413&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I3", "15" ]
            }
          }
    
        },
        "DELL 15 I5": {
          "brand": "DELL",
          "url": "https://www.morlevi.co.il/Cat/1?p_315=7&p_238=1145&p_387=3414&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I5", "15" ]
            }
          }
        },
        "DELL 15 I7": {
          "brand": "DELL",
          "url": "https://www.morlevi.co.il/Cat/1?p_315=7&p_238=1145&p_387=3415&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I7", "15" ]
            }
          }
        },
        "DELL 15 I9": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I9", "15" ]
            }
          }
        },
        "DELL 15 AMD": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS AMD", "15" ]
            }
          }
        },
        "DELL 15 Celeron": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "15" ]
            }
          }
        },
        "DELL 15 Pentium": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "15" ]
            }
          }
        },
        "DELL 17.3 I3": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I3", "17" ]
            }
          }
        },
        "DELL 17.3 I5": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I5", "17" ]
            }
          }
        },
        "DELL 17.3 I7": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I7", "17" ]
            }
          }
        },
        "DELL 17.3 I9": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL I9", "17" ]
            }
          }
        },
        "DELL 17.3 AMD": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS AMD", "17" ]
            }
          }
        },
        "DELL 17.3 Celeron": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "17" ]
            }
          }
        },
        "DELL 17.3 Pentium": {
          "brand": "DELL",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "dell": [ "LAPTOPS INTEL CELERON", "17" ]
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_data_loads(morlevi_data):
    """Checks that the fixture loads data correctly."""
    assert morlevi_data is not None
    assert isinstance(morlevi_data, dict)
    assert "scenarios" in morlevi_data

def test_scenario_structure(morlevi_data):
    """Checks that the scenarios have the correct structure."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict)
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data
        assert isinstance(scenario_data["presta_categories"], dict)
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)
        assert "dell" in scenario_data["presta_categories"]["template"]
        assert isinstance(scenario_data["presta_categories"]["template"]["dell"], list)
        assert len(scenario_data["presta_categories"]["template"]["dell"]) == 2


def test_scenario_brand(morlevi_data):
  """Checks that all scenario brands are 'DELL'."""
  scenarios = morlevi_data['scenarios']
  for scenario_name, scenario_data in scenarios.items():
      assert scenario_data['brand'] == 'DELL'

def test_scenario_active_is_true(morlevi_data):
    """Checks if all scenarios are active."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["active"] == True

def test_scenario_condition_is_new(morlevi_data):
    """Checks if all scenarios are new."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["condition"] == "new"

def test_scenario_checkbox_is_false(morlevi_data):
    """Checks if all checkboxes are false."""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["checkbox"] == False

def test_scenario_url_is_null_or_string(morlevi_data):
  """Checks if the URLs are either null or a string."""
  scenarios = morlevi_data['scenarios']
  for scenario_name, scenario_data in scenarios.items():
    assert scenario_data['url'] is None or isinstance(scenario_data['url'], str)

def test_presta_categories_template_dell_values(morlevi_data):
    """Checks if the presta_categories template dell values are strings"""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        dell_categories = scenario_data["presta_categories"]["template"]["dell"]
        assert isinstance(dell_categories[0], str)
        assert isinstance(dell_categories[1], str)

def test_presta_categories_template_dell_first_value_contains_laptop(morlevi_data):
    """Checks that the first element of the dell category list starts with LAPTOPS"""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        dell_categories = scenario_data["presta_categories"]["template"]["dell"]
        assert dell_categories[0].startswith("LAPTOPS")

def test_presta_categories_template_dell_second_value_is_screen_size(morlevi_data):
    """Checks that the second element of the dell category list is a valid screen size, which is convertible to an int"""
    scenarios = morlevi_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
      dell_categories = scenario_data["presta_categories"]["template"]["dell"]
      try:
        int(dell_categories[1])
      except ValueError:
          pytest.fail(f"The second value in dell categories '{dell_categories[1]}' is not convertible to an integer and thus not a valid screen size.")

def test_presta_categories_template_dell_second_value_is_valid_screen_size(morlevi_data):
    """Checks that the second element of the dell category list is one of a valid screen size"""
    scenarios = morlevi_data["scenarios"]
    valid_screen_sizes = ["11", "13", "14", "15", "17"]
    for scenario_name, scenario_data in scenarios.items():
      dell_categories = scenario_data["presta_categories"]["template"]["dell"]
      assert dell_categories[1] in valid_screen_sizes
```