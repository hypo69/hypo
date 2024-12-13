```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_data():
    """Loads the laptop data from the provided JSON."""
    json_data = """
{
  "scenarios": {
    "LENOVO 11.6 I3": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I3", "11" ]
        }
      }
    },
    "LENOVO 11.6 I5": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I5", "11" ]
        }
      }
    },
    "LENOVO 11.6 I7": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I7", "11" ]
        }
      }
    },
    "LENOVO 11.6 I9": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I9", "11" ]
        }
      }
    },
    "LENOVO 11.6 AMD": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS AMD", "11" ]
        }
      }
    },
    "LENOVO 11.6 Celeron": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "11" ]
        }
      }
    },
    "LENOVO 11.6 Pentium": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "11" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 I3": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I3", "13" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 I5": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I5", "13" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 I7": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I7", "13" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 I9": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I9", "13" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 AMD": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS AMD", "13" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 Celeron": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "13" ]
        }
      }
    },
    "LENOVO 13.4 - 13.3 Pentium": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "13" ]
        }
      }
    },
    "LENOVO 14 I3": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1144&p_387=3413&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I3", "14" ]
        }
      }
    },
    "LENOVO 14 I5": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1144&p_387=3414&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I5", "14" ]
        }
      }
    },
    "LENOVO 14 I7": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I7", "14" ]
        }
      }
    },
    "LENOVO 14 I9": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I9", "14" ]
        }
      }
    },
    "LENOVO 14 AMD RYZEN 7": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I7", "14" ]
        }
      }
    },
    "LENOVO 14 Celeron": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1144&p_387=3416&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "14" ]
        }
      }
    },
    "LENOVO 14 Pentium": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1144&p_387=3417&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "14" ]
        }
      }
    },
    "LENOVO 15 I3": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1145&p_387=3413&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I3", "15" ]
        }
      }
    },
    "LENOVO 15 I5": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1145&p_387=3414&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I5", "15" ]
        }
      }
    },
    "LENOVO 15 I7": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1145&p_387=3415&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I7", "15" ]
        }
      }
    },
    "LENOVO 15 I9": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I9", "15" ]
        }
      }
    },
    "LENOVO 15 AMD RYZEN 5": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1145&p_387=3743&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "gigabyte": [ "LAPTOPS AMD RYZEN 5", "15" ]
        }
      }
    },
    "LENOVO 15 AMD RYZEN 7": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS AMD RYZEN 7", "15" ]
        }
      }
    },
    "LENOVO 15 Celeron": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1145&p_387=3416&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "15" ]
        }
      }
    },
    "LENOVO 15 Pentium": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1145&p_387=3417&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "15" ]
        }
      }
    },
    "LENOVO 17.3 I3": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1146&p_387=3413&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I3", "17" ]
        }
      }
    },
    "LENOVO 17.3 I5": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1146&p_387=3414&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I5", "17" ]
        }
      }
    },
    "LENOVO 17.3 I7": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1146&p_387=3415&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I7", "17" ]
        }
      }
    },
    "LENOVO 17.3 I9": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL I9", "17" ]
        }
      }
    },
    "LENOVO 17.3 AMD": {
      "brand": "LENOVO",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS AMD", "17" ]
        }
      }
    },
    "LENOVO 17.3 Celeron": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1146&p_387=3416&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "17" ]
        }
      }
    },
    "LENOVO 17.3 Pentium": {
      "brand": "LENOVO",
      "url": "https://www.morlevi.co.il/Cat/71?p_238=1146&p_387=3417&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "LENOVO": [ "LAPTOPS INTEL CELERON", "17" ]
        }
      }
    }
  }
}
    """
    return json.loads(json_data)


def test_laptop_data_loading(laptop_data):
    """Test if the data is loaded correctly from the json."""
    assert isinstance(laptop_data, dict)
    assert "scenarios" in laptop_data
    assert isinstance(laptop_data["scenarios"], dict)
    assert len(laptop_data["scenarios"]) > 0
    
def test_scenario_keys_present(laptop_data):
    """Test if all scenarios contain the expected keys."""
    for scenario in laptop_data["scenarios"].values():
        assert "brand" in scenario
        assert "url" in scenario
        assert "checkbox" in scenario
        assert "active" in scenario
        assert "condition" in scenario
        assert "presta_categories" in scenario

def test_presta_categories_structure(laptop_data):
     """Test if presta_categories are correctly structured."""
     for scenario in laptop_data["scenarios"].values():
         assert "template" in scenario["presta_categories"]
         assert isinstance(scenario["presta_categories"]["template"], dict)
         for brand_key in scenario["presta_categories"]["template"]:
            assert isinstance(scenario["presta_categories"]["template"][brand_key], list)
            assert len(scenario["presta_categories"]["template"][brand_key]) == 2 # Check for two items


def test_scenario_brand_values(laptop_data):
    """Test if brand values are as expected."""
    for scenario in laptop_data["scenarios"].values():
        assert scenario["brand"] == "LENOVO"

def test_scenario_checkbox_values(laptop_data):
    """Test if checkbox values are as expected."""
    for scenario in laptop_data["scenarios"].values():
        assert scenario["checkbox"] is False


def test_scenario_active_values(laptop_data):
    """Test if active values are as expected."""
    for scenario in laptop_data["scenarios"].values():
        assert scenario["active"] is True

def test_scenario_condition_values(laptop_data):
    """Test if condition values are as expected."""
    for scenario in laptop_data["scenarios"].values():
        assert scenario["condition"] == "new"

def test_url_presence(laptop_data):
    """Test for url presence."""
    for scenario_name, scenario in laptop_data["scenarios"].items():
        if scenario_name in ["LENOVO 14 I3", "LENOVO 14 I5", "LENOVO 14 Celeron", "LENOVO 14 Pentium", "LENOVO 15 I3", "LENOVO 15 I5", "LENOVO 15 I7","LENOVO 15 AMD RYZEN 5","LENOVO 15 Celeron", "LENOVO 15 Pentium", "LENOVO 17.3 I3", "LENOVO 17.3 I5", "LENOVO 17.3 I7", "LENOVO 17.3 Celeron", "LENOVO 17.3 Pentium"]:
              assert scenario["url"] is not None
        else:
              assert scenario["url"] is None

def test_presta_categories_values(laptop_data):
    """Test for specific category values."""
    test_cases = {
        "LENOVO 11.6 I3": ["LAPTOPS INTEL I3", "11"],
        "LENOVO 11.6 I5": ["LAPTOPS INTEL I5", "11"],
         "LENOVO 11.6 I7": ["LAPTOPS INTEL I7", "11"],
        "LENOVO 11.6 I9": ["LAPTOPS INTEL I9", "11"],
        "LENOVO 11.6 AMD": ["LAPTOPS AMD", "11"],
         "LENOVO 11.6 Celeron": ["LAPTOPS INTEL CELERON", "11"],
        "LENOVO 11.6 Pentium": ["LAPTOPS INTEL CELERON", "11"],
        "LENOVO 13.4 - 13.3 I3": ["LAPTOPS INTEL I3", "13"],
         "LENOVO 13.4 - 13.3 I5": ["LAPTOPS INTEL I5", "13"],
        "LENOVO 13.4 - 13.3 I7": ["LAPTOPS INTEL I7", "13"],
        "LENOVO 13.4 - 13.3 I9": ["LAPTOPS INTEL I9", "13"],
        "LENOVO 13.4 - 13.3 AMD": ["LAPTOPS AMD", "13"],
        "LENOVO 13.4 - 13.3 Celeron": ["LAPTOPS INTEL CELERON", "13"],
        "LENOVO 13.4 - 13.3 Pentium": ["LAPTOPS INTEL CELERON", "13"],
        "LENOVO 14 I3": ["LAPTOPS INTEL I3", "14"],
         "LENOVO 14 I5": ["LAPTOPS INTEL I5", "14"],
        "LENOVO 14 I7": ["LAPTOPS INTEL I7", "14"],
         "LENOVO 14 I9": ["LAPTOPS INTEL I9", "14"],
        "LENOVO 14 AMD RYZEN 7": ["LAPTOPS INTEL I7", "14"],
        "LENOVO 14 Celeron": ["LAPTOPS INTEL CELERON", "14"],
        "LENOVO 14 Pentium": ["LAPTOPS INTEL CELERON", "14"],
        "LENOVO 15 I3": ["LAPTOPS INTEL I3", "15"],
         "LENOVO 15 I5": ["LAPTOPS INTEL I5", "15"],
        "LENOVO 15 I7": ["LAPTOPS INTEL I7", "15"],
        "LENOVO 15 I9": ["LAPTOPS INTEL I9", "15"],
         "LENOVO 15 AMD RYZEN 5": ["LAPTOPS AMD RYZEN 5", "15"],
         "LENOVO 15 AMD RYZEN 7": ["LAPTOPS AMD RYZEN 7", "15"],
        "LENOVO 15 Celeron": ["LAPTOPS INTEL CELERON", "15"],
        "LENOVO 15 Pentium": ["LAPTOPS INTEL CELERON", "15"],
        "LENOVO 17.3 I3": ["LAPTOPS INTEL I3", "17"],
         "LENOVO 17.3 I5": ["LAPTOPS INTEL I5", "17"],
         "LENOVO 17.3 I7": ["LAPTOPS INTEL I7", "17"],
        "LENOVO 17.3 I9": ["LAPTOPS INTEL I9", "17"],
         "LENOVO 17.3 AMD": ["LAPTOPS AMD", "17"],
        "LENOVO 17.3 Celeron": ["LAPTOPS INTEL CELERON", "17"],
        "LENOVO 17.3 Pentium": ["LAPTOPS INTEL CELERON", "17"],

    }
    for scenario_name, expected_categories in test_cases.items():
        actual_categories = laptop_data["scenarios"][scenario_name]["presta_categories"]["template"]["LENOVO"]
        assert actual_categories == expected_categories, f"Category mismatch for {scenario_name}"
    assert laptop_data["scenarios"]["LENOVO 15 AMD RYZEN 5"]["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS AMD RYZEN 5", "15"]
```