```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the JSON data from the provided string."""
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
          "asus": [ "LAPTOPS INTEL I7", "14" ]
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
          "asus": [ "LAPTOPS AMD RYZEN 7", "15" ]
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


def test_morlevi_data_load(morlevi_data):
    """Verify that the fixture loads the data correctly."""
    assert isinstance(morlevi_data, dict), "Data should be a dictionary"
    assert "Asus laptops" in morlevi_data, "Top level key 'Asus laptops' is missing"
    assert "scenarios" in morlevi_data, "Top level key 'scenarios' is missing"

def test_asus_laptops_url(morlevi_data):
     """Verify that the base URL for Asus laptops is correct."""
     assert morlevi_data["Asus laptops"]["url"] == "https://www.morlevi.co.il/Cat/1?p_315=5&sort=datafloat2%2Cprice&keyword=", "URL for 'Asus laptops' is incorrect"


def test_scenario_asus_11_6_i3(morlevi_data):
    """Tests the 'ASUS 11.6 I3' scenario."""
    scenario = morlevi_data["scenarios"]["ASUS 11.6 I3"]
    assert scenario["brand"] == "ASUS", "Brand is incorrect"
    assert scenario["url"] is None, "URL should be None"
    assert scenario["checkbox"] is False, "Checkbox should be False"
    assert scenario["active"] is True, "Active should be True"
    assert scenario["condition"] == "new", "Condition should be 'new'"
    assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I3", "11"], "Presta categories are incorrect"

def test_scenario_asus_11_6_celeron(morlevi_data):
    """Tests the 'ASUS 11.6 Celeron' scenario with a valid URL."""
    scenario = morlevi_data["scenarios"]["ASUS 11.6 Celeron"]
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1142&p_387=3416&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
    assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL CELERON", "11"], "Presta categories are incorrect"

def test_scenario_asus_13_4_13_3_i5(morlevi_data):
     """Tests the 'ASUS 13.4 - 13.3 I5' scenario."""
     scenario = morlevi_data["scenarios"]["ASUS 13.4 - 13.3 I5"]
     assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1143&p_387=3414&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
     assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I5", "13"], "Presta categories are incorrect"


def test_scenario_asus_14_i3(morlevi_data):
    """Tests the 'ASUS 14 I3' scenario."""
    scenario = morlevi_data["scenarios"]["ASUS 14 I3"]
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3413&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
    assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I3", "14"], "Presta categories are incorrect"


def test_scenario_asus_14_amd_ryzen_7(morlevi_data):
     """Tests the 'ASUS 14 AMD RYZEN 7' scenario."""
     scenario = morlevi_data["scenarios"]["ASUS 14 AMD RYZEN 7"]
     assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3415&p_387=3742&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
     assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I7", "14"], "Presta categories are incorrect"


def test_scenario_asus_15_i7(morlevi_data):
    """Tests the 'ASUS 15 I7' scenario."""
    scenario = morlevi_data["scenarios"]["ASUS 15 I7"]
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1145&p_387=3415&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
    assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I7", "15"], "Presta categories are incorrect"

def test_scenario_asus_15_amd_ryzen_7(morlevi_data):
    """Tests the 'ASUS 15 AMD RYZEN 7' scenario."""
    scenario = morlevi_data["scenarios"]["ASUS 15 AMD RYZEN 7"]
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1145&p_387=3742&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
    assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS AMD RYZEN 7", "15"], "Presta categories are incorrect"

def test_scenario_asus_17_3_i7(morlevi_data):
    """Tests the 'ASUS 17.3 I7' scenario."""
    scenario = morlevi_data["scenarios"]["ASUS 17.3 I7"]
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/69?p_238=1146&p_387=3415&sort=datafloat2%2Cprice&keyword=", "URL is incorrect"
    assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I7", "17"], "Presta categories are incorrect"

def test_scenario_asus_17_3_i9_url_none(morlevi_data):
     """Tests the 'ASUS 17.3 I9' scenario where the URL should be None."""
     scenario = morlevi_data["scenarios"]["ASUS 17.3 I9"]
     assert scenario["url"] is None, "URL should be None"
     assert scenario["presta_categories"]["template"]["asus"] == ["LAPTOPS INTEL I9", "17"], "Presta categories are incorrect"

def test_all_scenarios_have_expected_keys(morlevi_data):
     """Test if each scenario has the expected keys."""
     expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
     for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert all(key in scenario_data for key in expected_keys), f"Scenario '{scenario_name}' is missing one of the following keys: {expected_keys}"

def test_all_presta_categories_have_template_and_asus(morlevi_data):
    """Test if each presta_categories has a template and an asus key"""
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' is missing 'template' key in 'presta_categories'"
        assert "asus" in scenario_data["presta_categories"]["template"], f"Scenario '{scenario_name}' is missing 'asus' key in 'template'"

def test_all_asus_presta_categories_are_lists(morlevi_data):
     """Test that all the 'asus' values in 'presta_categories' are lists."""
     for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"]["template"]["asus"], list), f"The 'asus' value in scenario '{scenario_name}' is not a list"


def test_all_scenario_urls_are_strings_or_none(morlevi_data):
    """Tests that all scenario URLs are strings or None."""
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        url = scenario_data["url"]
        assert url is None or isinstance(url, str), f"URL in scenario '{scenario_name}' is not a string or None"


def test_all_scenario_conditions_are_new(morlevi_data):
     """Tests that all scenario conditions are 'new'."""
     for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert scenario_data["condition"] == "new", f"Condition in scenario '{scenario_name}' is not 'new'"
```