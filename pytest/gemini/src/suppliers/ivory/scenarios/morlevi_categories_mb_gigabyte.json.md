```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def category_data():
    """Loads the JSON data for testing."""
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

def test_category_data_structure(category_data):
    """
    Checks if the loaded data has the correct structure
    """
    assert isinstance(category_data, dict)
    assert "scenarios" in category_data
    assert isinstance(category_data["scenarios"], dict)


def test_scenario_keys(category_data):
    """
    Checks that each scenario has the expected keys.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "presta_categories" in scenario_data
        assert "condition" in scenario_data


def test_scenario_data_types(category_data):
    """
    Checks if the data types of each key in a scenario are correct.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["presta_categories"], dict)
        assert isinstance(scenario_data["condition"],str)


def test_presta_categories_structure(category_data):
    """
    Checks the structure of the 'presta_categories' dictionary.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        presta_categories = scenario_data.get("presta_categories")
        assert isinstance(presta_categories, dict)
        assert "template" in presta_categories
        assert isinstance(presta_categories["template"], dict)


def test_template_keys_and_values(category_data):
    """
    Checks if the 'template' dictionary within 'presta_categories' has a 'gigabyte' key
    and that its value is a string.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
          template = scenario_data["presta_categories"].get("template")
          assert "gigabyte" in template
          assert isinstance(template["gigabyte"], str)


def test_price_rule_key(category_data):
  """
    Checks if the 'price_rule' key exists and if its value is an integer.
    """
  scenario_with_price_rule = category_data["scenarios"].get("GIGABYTE INTEL LGA1700 12 Gen Z690")
  assert "price_rule" in scenario_with_price_rule
  assert isinstance(scenario_with_price_rule["price_rule"], int)

def test_condition_key(category_data):
  """
    Checks if the 'condition' key exists and if its value is a string.
    """
  for scenario_name, scenario_data in category_data["scenarios"].items():
    assert "condition" in scenario_data
    assert isinstance(scenario_data["condition"], str)


def test_url_format(category_data):
    """
    Checks if the 'url' values are strings that start with 'https://'.
    """
    for scenario_name, scenario_data in category_data["scenarios"].items():
        assert scenario_data["url"].startswith("https://")
```