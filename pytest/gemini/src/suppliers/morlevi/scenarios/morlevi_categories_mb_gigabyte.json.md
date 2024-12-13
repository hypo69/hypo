```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the loaded JSON data for tests."""
    json_data = """
    {
      "scenarios": {
        "GIGABYTE INTEL LGA1700 12 Gen Z690": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/378",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel Z690" }
          },
          "price_rule": 1
        },
        "GIGABYTE INTEL LGA1700 12 Gen B660": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/388",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel B660" }
          }
        },
        "GIGABYTE INTEL LGA1700 12 H610": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/389",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel H610" }
          }
        },
        "GIGABYTE INTEL LGA1200 H510": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/364",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel H610" }
          }
        },
        "GIGABYTE INTEL LGA1200 B560": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/365",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel B560" }
          }
        },
        "GIGABYTE INTEL LGA1200 Z590": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/360",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel B560" }
          }
        },
        "GIGABYTE INTEL LGA1200 H410 GEN10": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/343",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel H410" }
          }
        },
        "GIGABYTE INTEL LGA1200 H470 GEN10": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/343",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel H470" }
          }
        },
        "GIGABYTE INTEL LGA2066 X299": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/28?p_95=411",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "Intel X299" }
          }
        },
        "GIGABYTE AMD AM4+  A520": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/350",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD A520" }
          }
        },
        "GIGABYTE AMD AM4+  B450": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/311",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD B450" }
          }
        },
        "GIGABYTE AMD AM4+  B550": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/340",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD B550" }
          }
        },
        "GIGABYTE AMD AM4+  X570/X570S": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/22?p_95=4022&p_95=3225",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD X570" }
          }
        },
        "GIGABYTE AMD Threadripper   TRX40": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/349",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD TRX40" }
          }
        },
        "GIGABYTE AMD Threadripper   X399": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/353",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD X399" }
          }
        },
         "GIGABYTE AMD Threadripper   WRX80": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/366",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "gigabyte": "AMD WRX80" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test if the loaded JSON data has the expected structure.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)
    
def test_morlevi_categories_data_count(morlevi_categories_data):
     """
     Test that the correct number of scenarios are loaded
     """
     assert len(morlevi_categories_data["scenarios"]) == 17

def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test if each scenario has the expected keys.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert "brand" in scenario_data
      assert "url" in scenario_data
      assert "checkbox" in scenario_data
      assert "active" in scenario_data
      assert "condition" in scenario_data
      assert "presta_categories" in scenario_data
      
def test_morlevi_categories_scenario_values_types(morlevi_categories_data):
    """
    Test if each scenario has the expected value types.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], dict)
        
def test_morlevi_categories_presta_categories_template(morlevi_categories_data):
    """
    Test if 'presta_categories' has the 'template' key and it's a dictionary.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert "template" in scenario_data["presta_categories"]
      assert isinstance(scenario_data["presta_categories"]["template"], dict)

def test_morlevi_categories_valid_url(morlevi_categories_data):
  """
  Test if all URLs are valid strings and follow the expected format.
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    url = scenario_data["url"]
    assert isinstance(url, str)
    assert url.startswith("https://www.morlevi.co.il/Cat/")
    
def test_morlevi_categories_price_rule_key(morlevi_categories_data):
    """
    Test if a price_rule key exists only in the expected scenario and is an integer.
    """
    
    #Check that only the first item has a price_rule key
    first_scenario_key = list(morlevi_categories_data["scenarios"].keys())[0]
    assert "price_rule" in morlevi_categories_data["scenarios"][first_scenario_key]
    assert isinstance(morlevi_categories_data["scenarios"][first_scenario_key]["price_rule"], int)

    #Check that no other item has the price rule
    for key, scenario_data in list(morlevi_categories_data["scenarios"].items())[1:]:
        assert "price_rule" not in scenario_data
```