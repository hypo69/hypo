```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "KINGSTON NVME GEN4 512GB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD NVME GEN4 512GB"
            }
          }
        },
        "KINGSTON NVME GEN4 1TB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=829&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD NVME GEN4 1TB"
            }
          }
        },
        "KINGSTON NVME GEN4 2TB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=831&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD NVME GEN4 2TB"
            }
          }
        },
        "KINGSTON SATA 3 256GB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=823&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD SATA 3 256GB"
            }
          }
        },
        "KINGSTON SATA 3 512GB": {
          "brand": "KINGSTON",
          "name": "internal_ssd_sata_3_2tb",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD SATA 3 512GB"
            }
          }
        },
        "KINGSTON SATA 3 1TB": {
          "brand": "KINGSTON",
          "name": "internal_ssd_sata_3_4tb",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=829&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD SATA 3 1TB"
            }
          }
        },
        "KINGSTON SATA 3 2TB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=831&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD SATA 3 2TB"
            }
          }
        },
        "KINGSTON SATA 3 4TB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=3576&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD SATA 3 4TB"
            }
          }

        },
        "KINGSTON SSD NVME PCIE 256GB": {
          "brand": "KINGSTON",
          "url": "https://www.morlevi.co.il/Cat/51?p_315=22&p_175=823&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD NVME PCIE 256GB"
            }
          }
        },
        "KINGSTON SSD NVME PCIE 512GB": {
          "brand": "KINGSTON",
          "name": "internal_ssd_m2sata_256",
          "url": "https://www.morlevi.co.il/Cat/51?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "kingston": "SSD NVME PCIE 512GB"
            }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test if the loaded data has the correct structure.
    Checks for the existence of 'scenarios' key.
    """
    assert "scenarios" in morlevi_categories_data, "The root should have a 'scenarios' key"
    assert isinstance(morlevi_categories_data["scenarios"], dict), "'scenarios' should be a dictionary."

def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test if each scenario has the required keys.
    Checks the existence of 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories' in each scenario.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' should have a 'brand' key"
        assert "url" in scenario_data, f"Scenario '{scenario_name}' should have a 'url' key"
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' should have a 'checkbox' key"
        assert "active" in scenario_data, f"Scenario '{scenario_name}' should have an 'active' key"
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' should have a 'condition' key"
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' should have a 'presta_categories' key"
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' should be a dict."


def test_morlevi_categories_scenario_values(morlevi_categories_data):
  """
    Test if the values in each scenario have the correct types
    """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' should be a string"
    assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' should be a string"
    assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' should be a boolean"
    assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' should be a boolean"
    assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' should be a string"
    assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' should be a dict."
    assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' 'presta_categories' should have a 'template' key"
    assert isinstance(scenario_data["presta_categories"]["template"], dict), f"Scenario '{scenario_name}' 'presta_categories' 'template' should be a dict."
    assert "kingston" in scenario_data["presta_categories"]["template"], f"Scenario '{scenario_name}' 'presta_categories' 'template' should have a 'kingston' key"
    assert isinstance(scenario_data["presta_categories"]["template"]["kingston"], str), f"Scenario '{scenario_name}' 'presta_categories' 'template' 'kingston' should be a string."

def test_morlevi_categories_specific_scenario(morlevi_categories_data):
    """
    Test a specific scenario for correct values.
    Checks the data for 'KINGSTON NVME GEN4 512GB' for expected values.
    """
    scenario_name = "KINGSTON NVME GEN4 512GB"
    scenario_data = morlevi_categories_data["scenarios"].get(scenario_name)
    assert scenario_data is not None, f"Scenario '{scenario_name}' not found"
    assert scenario_data["brand"] == "KINGSTON"
    assert scenario_data["url"] == "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword="
    assert scenario_data["checkbox"] == False
    assert scenario_data["active"] == True
    assert scenario_data["condition"] == "new"
    assert scenario_data["presta_categories"]["template"]["kingston"] == "SSD NVME GEN4 512GB"


def test_morlevi_categories_missing_scenario(morlevi_categories_data):
    """
    Test handling of a missing scenario.
    Attempts to access a non-existent scenario to verify correct handling.
    """
    scenario_name = "NON_EXISTENT_SCENARIO"
    scenario_data = morlevi_categories_data["scenarios"].get(scenario_name)
    assert scenario_data is None, f"Scenario '{scenario_name}' should not exist."
```