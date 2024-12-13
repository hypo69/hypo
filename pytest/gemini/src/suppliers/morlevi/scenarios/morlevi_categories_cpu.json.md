```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_cpu_data():
    """Loads the JSON data for testing."""
    json_data = """
{
  "scenarios": {
    "Intel  CELERON LGA1200 Gen 10": {
      "brand": "INTEL",
      "url": "https://www.morlevi.co.il/Cat/337?p_134=584&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
      "condition":"new","presta_categories": {
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
    Tests the basic structure of the loaded JSON data.
    Checks if the data is a dictionary and contains the 'scenarios' key.
    """
    assert isinstance(morlevi_categories_cpu_data, dict)
    assert "scenarios" in morlevi_categories_cpu_data


def test_morlevi_categories_cpu_scenarios_not_empty(morlevi_categories_cpu_data):
    """
    Checks if the 'scenarios' dictionary is not empty.
    """
    assert morlevi_categories_cpu_data["scenarios"]


def test_morlevi_categories_cpu_scenario_keys(morlevi_categories_cpu_data):
    """
    Checks if each scenario has the required keys.
    """
    required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        for key in required_keys:
            assert key in scenario_data, f"Missing key '{key}' in scenario: {scenario_name}"

def test_morlevi_categories_cpu_presta_categories_template(morlevi_categories_cpu_data):
    """
    Checks if 'presta_categories' contains the required 'template' key.
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
          assert "template" in scenario_data["presta_categories"], f"Missing 'template' key in presta_categories for scenario: {scenario_name}"
          assert "cpu" in scenario_data["presta_categories"]["template"], f"Missing 'cpu' key in template for scenario: {scenario_name}"


def test_morlevi_categories_cpu_data_types(morlevi_categories_cpu_data):
    """
    Tests if the data types for various fields are correct
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
      assert isinstance(scenario_data["brand"], str)
      assert isinstance(scenario_data["url"], str)
      assert isinstance(scenario_data["checkbox"], bool)
      assert isinstance(scenario_data["active"], bool)
      assert isinstance(scenario_data["condition"], str)
      assert isinstance(scenario_data["presta_categories"], dict)
      assert isinstance(scenario_data["presta_categories"]["template"], dict)
      assert isinstance(scenario_data["presta_categories"]["template"]["cpu"], str)
      
def test_morlevi_categories_cpu_url_valid(morlevi_categories_cpu_data):
    """
    Tests if the url field is a valid URL format
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
      url = scenario_data["url"]
      assert url.startswith("https://"), f"Invalid URL format: {url} in scenario: {scenario_name}"
      
      # Optionally, add more robust URL validation if needed, e.g., using urllib.parse or regex


def test_morlevi_categories_cpu_active_values(morlevi_categories_cpu_data):
    """
    Tests if the "active" field only contains boolean values
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
      assert isinstance(scenario_data["active"],bool), f"Invalid type for 'active' in scenario: {scenario_name}"


def test_morlevi_categories_cpu_checkbox_values(morlevi_categories_cpu_data):
    """
    Tests if the "checkbox" field only contains boolean values
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
      assert isinstance(scenario_data["checkbox"],bool), f"Invalid type for 'checkbox' in scenario: {scenario_name}"

def test_morlevi_categories_cpu_condition_values(morlevi_categories_cpu_data):
    """
    Tests if the "condition" field is a string
    """
    for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str), f"Invalid type for 'condition' in scenario: {scenario_name}"
    
def test_morlevi_categories_cpu_brand_values(morlevi_categories_cpu_data):
        """
        Tests if the "brand" field is a string
        """
        for scenario_name, scenario_data in morlevi_categories_cpu_data["scenarios"].items():
          assert isinstance(scenario_data["brand"], str), f"Invalid type for 'brand' in scenario: {scenario_name}"
          assert scenario_data["brand"] == "INTEL", f"Invalid brand value in scenario: {scenario_name}"
```