```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_asus_laptops_data():
    """Provides the JSON data for testing."""
    json_data = """
    {
      "Asus laptops": {
        "url": "https://www.morlevi.co.il/Cat/1?p_315=5&sort=datafloat2%2Cprice&keyword="
      },
      "scenarios": {
        "ASUS 11.6 I3": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "11" ]
            }
          }
        },
        "ASUS 11.6 I5": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "11" ]
            }
          }
        },
        "ASUS 11.6 I7": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "11" ]
            }
          }
        },
        "ASUS 11.6 I9": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I9", "11" ]
            }
          }
        },
        "ASUS 11.6 AMD": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS AMD", "11" ]
            }
          }
        },
        "ASUS 11.6 Celeron": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1142&p_387=3416&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "11" ]
            }
          }
        },
        "ASUS 11.6 Pentium": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "11" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 I3": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "13" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 I5": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1143&p_387=3414&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "13" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 I7": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1143&p_387=3415&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "13" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 I9": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I9", "13" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 AMD": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS AMD", "13" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 Celeron": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "13" ]
            }
          }
        },
        "ASUS 13.4 - 13.3 Pentium": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "13" ]
            }
          }
        },
        "ASUS 14 I3": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3413&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "14" ]
            }
          }
        },
        "ASUS 14 I5": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3414&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "14" ]
            }
          }
        },
        "ASUS 14 I7": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3415&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
        "ASUS 14 I9": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I9", "14" ]
            }
          }
        },
          "ASUS 14 AMD RYZEN 7": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3415&p_387=3742&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
            "presta_categories": {
                "template": {
                  "asus": ["LAPTOPS INTEL I7","14"]
                }
             }
         },
        "ASUS 14 Celeron": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "14" ]
            }
          }
        },
        "ASUS 14 Pentium": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "14" ]
            }
          }
        },
        "ASUS 15 I3": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1145&p_387=3413&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "15" ]
            }
          }
        },
        "ASUS 15 I5": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1145&p_387=3414&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "15" ]
            }
          }
        },
        "ASUS 15 I7": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1145&p_387=3415&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "15" ]
            }
          }
        },
        "ASUS 15 I9": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I9", "15" ]
            }
          }
        },
          "ASUS 15 AMD RYZEN 7": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1145&p_387=3742&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
            "presta_categories": {
                "template": {
                  "asus": ["LAPTOPS AMD RYZEN 7","15"]
                }
             }
        },
        "ASUS 15 Celeron": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "15" ]
            }
          }
        },
        "ASUS 15 Pentium": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "15" ]
            }
          }
        },
        "ASUS 17.3 I3": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "17" ]
            }
          }
        },
        "ASUS 17.3 I5": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "17" ]
            }
          }
        },
        "ASUS 17.3 I7": {
          "brand": "ASUS",
          "url": "https://www.morlevi.co.il/Cat/69?p_238=1146&p_387=3415&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "17" ]
            }
          }
        },
        "ASUS 17.3 I9": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I9", "17" ]
            }
          }
        },
        "ASUS 17.3 AMD": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS AMD", "17" ]
            }
          }
        },
        "ASUS 17.3 Celeron": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "17" ]
            }
          }
        },
        "ASUS 17.3 Pentium": {
          "brand": "ASUS",
          "url": null,
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL CELERON", "17" ]
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)


def test_asus_laptops_data_structure(morlevi_asus_laptops_data):
    """
    Test the basic structure of the loaded JSON data.
    Verifies that the top-level keys are present and have the expected types.
    """
    assert "Asus laptops" in morlevi_asus_laptops_data
    assert "scenarios" in morlevi_asus_laptops_data
    assert isinstance(morlevi_asus_laptops_data["Asus laptops"], dict)
    assert isinstance(morlevi_asus_laptops_data["scenarios"], dict)

def test_asus_laptops_url(morlevi_asus_laptops_data):
    """
    Test the 'url' value in the "Asus laptops" section.
    Verifies that it is a string and that it is not empty.
    """
    assert "url" in morlevi_asus_laptops_data["Asus laptops"]
    assert isinstance(morlevi_asus_laptops_data["Asus laptops"]["url"], str)
    assert morlevi_asus_laptops_data["Asus laptops"]["url"] != ""

def test_scenario_keys_present(morlevi_asus_laptops_data):
    """
    Test that all scenarios in 'scenarios' dictionary contain the required keys.
    """
    for scenario_name, scenario_data in morlevi_asus_laptops_data["scenarios"].items():
        assert "brand" in scenario_data, f"Missing 'brand' in scenario: {scenario_name}"
        assert "url" in scenario_data, f"Missing 'url' in scenario: {scenario_name}"
        assert "checkbox" in scenario_data, f"Missing 'checkbox' in scenario: {scenario_name}"
        assert "active" in scenario_data, f"Missing 'active' in scenario: {scenario_name}"
        assert "condition" in scenario_data, f"Missing 'condition' in scenario: {scenario_name}"
        assert "presta_categories" in scenario_data, f"Missing 'presta_categories' in scenario: {scenario_name}"

def test_scenario_data_types(morlevi_asus_laptops_data):
    """
    Test that the values in the 'scenarios' dictionary have the correct data types.
    """
    for scenario_name, scenario_data in morlevi_asus_laptops_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Incorrect 'brand' type in scenario: {scenario_name}"
        assert scenario_data["url"] is None or isinstance(scenario_data["url"], str), f"Incorrect 'url' type in scenario: {scenario_name}"
        assert isinstance(scenario_data["checkbox"], bool), f"Incorrect 'checkbox' type in scenario: {scenario_name}"
        assert isinstance(scenario_data["active"], bool), f"Incorrect 'active' type in scenario: {scenario_name}"
        assert isinstance(scenario_data["condition"], str), f"Incorrect 'condition' type in scenario: {scenario_name}"
        assert isinstance(scenario_data["presta_categories"], dict), f"Incorrect 'presta_categories' type in scenario: {scenario_name}"
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"],dict)
        assert "asus" in scenario_data["presta_categories"]["template"]
        assert isinstance(scenario_data["presta_categories"]["template"]["asus"],list)

def test_scenario_brand_values(morlevi_asus_laptops_data):
    """
    Test that all 'brand' values are 'ASUS'.
    """
    for scenario_name, scenario_data in morlevi_asus_laptops_data["scenarios"].items():
        assert scenario_data["brand"] == "ASUS", f"Incorrect 'brand' value in scenario: {scenario_name}"

def test_scenario_active_values(morlevi_asus_laptops_data):
    """
    Test that all 'active' values are True.
    """
    for scenario_name, scenario_data in morlevi_asus_laptops_data["scenarios"].items():
        assert scenario_data["active"] is True, f"Incorrect 'active' value in scenario: {scenario_name}"

def test_scenario_condition_values(morlevi_asus_laptops_data):
      """
      Test that all 'condition' values are 'new'.
      """
      for scenario_name, scenario_data in morlevi_asus_laptops_data["scenarios"].items():
          assert scenario_data["condition"] == "new", f"Incorrect 'condition' value in scenario: {scenario_name}"


def test_scenario_presta_categories_template_asus_values(morlevi_asus_laptops_data):
    """
    Test that all 'asus' list in 'presta_categories.template' is not empty and contains two strings
    """
    for scenario_name, scenario_data in morlevi_asus_laptops_data["scenarios"].items():
        asus_list = scenario_data["presta_categories"]["template"]["asus"]
        assert len(asus_list) == 2, f"Incorrect 'asus' list length in scenario: {scenario_name}"
        assert all(isinstance(item, str) for item in asus_list), f"Incorrect 'asus' list item type in scenario: {scenario_name}"
        assert asus_list[0] != "", f"Empty first value in 'asus' list: {scenario_name}"
        assert asus_list[1] != "", f"Empty second value in 'asus' list: {scenario_name}"


def test_url_is_string_or_none(morlevi_asus_laptops_data):
    """
    Test that all URLs in the scenarios are either strings or None.
    """
    for scenario_name, scenario_data in morlevi_asus_laptops_data['scenarios'].items():
      assert isinstance(scenario_data['url'], str) or scenario_data['url'] is None, f"URL for {scenario_name} is not a string or None"
```