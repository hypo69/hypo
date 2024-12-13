```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_samsung_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "SAMSUNG NVME GEN4 512GB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/314?p_315=28&p_175=826&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME GEN4 512GB"
            }
          }
        },
        "SAMSUNG NVME GEN4 1TB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/314?p_315=28&p_175=829&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME GEN4 1TB"
            }
          }
        },
        "SAMSUNG NVME GEN4 2TB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/314?p_315=28&p_175=831&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME GEN4 2TB"
            }
          }
        },
        "SAMSUNG SATA 3 256GB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=28&p_175=823&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SATA 3 256GB"
            }
          }
        },
        "SAMSUNG SATA 3 512GB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=28&p_175=826&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SATA 3 521GB"
            }
          }
        },
        "SAMSUNG SATA 3 1TB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=28&p_175=829&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SATA 3 1TB"
            }
          }
        },
        "SAMSUNG SATA 3 2TB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=28&p_175=831&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SATA 3 2TB"
            }
          }
        },
         "SAMSUNG SATA 3 4TB": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=28&p_175=3576&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SATA 3 4TB"
            }
          }
        },
        "SAMSUNG SSD NVME PCIE 256GB ": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=28&p_175=3576&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME PCIE 256GB"
            }
          }
        },
         "SAMSUNG SSD NVME PCIE 512GB ": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/51?p_315=28&p_175=826&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME PCIE 512GB"
            }
          }
        },
        "SAMSUNG SSD NVME PCIE 1TB ": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/51?p_315=28&p_175=829&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME PCIE 1TB"
            }
          }
        },
        "SAMSUNG SSD NVME PCIE 2TB ": {
          "brand": "SAMSUNG",
          "url": "https://www.morlevi.co.il/Cat/51?p_315=28&p_175=831&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "samsung": "SSD NVME PCIE 2TB"
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)


def test_load_data(morlevi_samsung_data):
    """Test that fixture loads data successfully"""
    assert morlevi_samsung_data is not None
    assert isinstance(morlevi_samsung_data, dict)
    assert "scenarios" in morlevi_samsung_data

def test_scenario_count(morlevi_samsung_data):
    """Test the number of scenarios loaded"""
    assert len(morlevi_samsung_data["scenarios"]) == 12

def test_scenario_structure(morlevi_samsung_data):
    """Test the structure of a single scenario"""
    first_scenario = list(morlevi_samsung_data["scenarios"].values())[0]
    assert "brand" in first_scenario
    assert "url" in first_scenario
    assert "checkbox" in first_scenario
    assert "active" in first_scenario
    assert "condition" in first_scenario
    assert "presta_categories" in first_scenario
    assert "template" in first_scenario["presta_categories"]
    assert "samsung" in first_scenario["presta_categories"]["template"]


def test_scenario_brand(morlevi_samsung_data):
    """Test all scenarios have brand samsung"""
    for scenario in morlevi_samsung_data["scenarios"].values():
      assert scenario["brand"] == "SAMSUNG"

def test_scenario_active_is_true(morlevi_samsung_data):
    """Test all scenarios have active is true"""
    for scenario in morlevi_samsung_data["scenarios"].values():
        assert scenario["active"] is True

def test_scenario_condition_is_new(morlevi_samsung_data):
    """Test all scenarios have condition is new"""
    for scenario in morlevi_samsung_data["scenarios"].values():
        assert scenario["condition"] == "new"


def test_scenario_checkbox_is_false(morlevi_samsung_data):
    """Test all scenarios have checkbox is false"""
    for scenario in morlevi_samsung_data["scenarios"].values():
        assert scenario["checkbox"] is False

def test_scenario_url_format(morlevi_samsung_data):
    """Test if all urls follow the expected format"""
    for scenario in morlevi_samsung_data["scenarios"].values():
        assert scenario["url"].startswith("https://www.morlevi.co.il/Cat/")
        assert "sort=datafloat2%2Cprice&keyword=" in scenario["url"]

def test_scenario_presta_categories_template_samsung_values(morlevi_samsung_data):
    """Test the values of 'samsung' in presta_categories.template"""
    expected_values = [
        "SSD NVME GEN4 512GB",
        "SSD NVME GEN4 1TB",
        "SSD NVME GEN4 2TB",
        "SATA 3 256GB",
        "SATA 3 521GB",
        "SATA 3 1TB",
        "SATA 3 2TB",
        "SATA 3 4TB",
        "SSD NVME PCIE 256GB",
         "SSD NVME PCIE 512GB",
        "SSD NVME PCIE 1TB",
        "SSD NVME PCIE 2TB"
    ]
    actual_values = [
        scenario["presta_categories"]["template"]["samsung"]
        for scenario in morlevi_samsung_data["scenarios"].values()
    ]
    assert sorted(actual_values) == sorted(expected_values)
```