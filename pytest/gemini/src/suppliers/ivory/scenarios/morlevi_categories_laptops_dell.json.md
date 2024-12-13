```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def category_data():
    """Provides the JSON data as a dictionary."""
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


def test_category_data_structure(category_data):
    """
    Test if the loaded data is a dictionary and contains the 'scenarios' key.
    """
    assert isinstance(category_data, dict), "Data should be a dictionary."
    assert "scenarios" in category_data, "Data should contain a 'scenarios' key."


def test_scenario_keys_present(category_data):
    """
    Test if each scenario has the required keys.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' is missing 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' is missing 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key."


def test_presta_categories_structure(category_data):
    """
    Test if 'presta_categories' has the expected structure.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
         presta_categories = scenario_data.get("presta_categories")
         assert isinstance(presta_categories, dict), f"presta_categories in scenario '{scenario_name}' should be a dict."
         assert "template" in presta_categories, f"'template' key not found in presta_categories of scenario '{scenario_name}'"
         template = presta_categories.get("template")
         assert isinstance(template, dict), f"'template' in presta_categories of scenario '{scenario_name}' should be a dict."
         assert "dell" in template, f"'dell' key not found in template of scenario '{scenario_name}'"
         dell_categories = template.get("dell")
         assert isinstance(dell_categories, list), f"'dell' in template of scenario '{scenario_name}' should be a list."
         assert len(dell_categories) == 2, f"The 'dell' list in scenario '{scenario_name}' should have 2 elements."
         for item in dell_categories:
            assert isinstance(item, str), f"Each item in dell category should be a string in scenario {scenario_name}"


def test_brand_values(category_data):
  """
  Test if brand values are all "DELL".
  """
  for scenario_name, scenario_data in category_data["scenarios"].items():
    assert scenario_data["brand"] == "DELL", f"Brand in scenario '{scenario_name}' is not 'DELL'."


def test_checkbox_values(category_data):
    """
    Test if 'checkbox' values are all False.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"'checkbox' in scenario '{scenario_name}' is not False."


def test_active_values(category_data):
    """
    Test if 'active' values are all True.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert scenario_data["active"] == True, f"'active' in scenario '{scenario_name}' is not True."


def test_condition_values(category_data):
    """
    Test if 'condition' values are all "new".
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"'condition' in scenario '{scenario_name}' is not 'new'."


def test_url_type(category_data):
  """
  Test if the url is either a string or none
  """
  for scenario_name, scenario_data in category_data["scenarios"].items():
      assert scenario_data["url"] is None or isinstance(scenario_data["url"], str), f"url in scenario {scenario_name} is not None or string"
```