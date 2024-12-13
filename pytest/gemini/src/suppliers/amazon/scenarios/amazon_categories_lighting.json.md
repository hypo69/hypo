```python
import pytest
import json

# Define a fixture to load the JSON data
@pytest.fixture
def amazon_lighting_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "Murano Glass": {
          "url": "https://amzn.to/46PWVcs",
          "condition": "new",
          "presta_categories": {
            "default_category": { "11209": "MURANO GLASS" },
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)

def test_amazon_lighting_data_load(amazon_lighting_data):
    """Tests if the JSON data is loaded correctly."""
    assert isinstance(amazon_lighting_data, dict)
    assert "scenarios" in amazon_lighting_data

def test_amazon_lighting_scenario_keys(amazon_lighting_data):
    """Tests if the 'scenarios' dictionary has the expected keys."""
    assert "Murano Glass" in amazon_lighting_data["scenarios"]

def test_amazon_lighting_scenario_values(amazon_lighting_data):
    """Tests if the 'Murano Glass' scenario has the expected values."""
    murano_glass_scenario = amazon_lighting_data["scenarios"]["Murano Glass"]
    assert murano_glass_scenario["url"] == "https://amzn.to/46PWVcs"
    assert murano_glass_scenario["condition"] == "new"
    assert isinstance(murano_glass_scenario["presta_categories"], dict)
    assert murano_glass_scenario["price_rule"] == 1

def test_amazon_lighting_presta_categories(amazon_lighting_data):
    """Tests if the 'presta_categories' dictionary has the expected structure."""
    presta_categories = amazon_lighting_data["scenarios"]["Murano Glass"]["presta_categories"]
    assert "default_category" in presta_categories
    assert "additional_categories" in presta_categories

def test_amazon_lighting_default_category(amazon_lighting_data):
    """Tests if the 'default_category' dictionary has the expected structure."""
    default_category = amazon_lighting_data["scenarios"]["Murano Glass"]["presta_categories"]["default_category"]
    assert isinstance(default_category, dict)
    assert "11209" in default_category
    assert default_category["11209"] == "MURANO GLASS"

def test_amazon_lighting_additional_categories(amazon_lighting_data):
    """Tests if the 'additional_categories' list contains expected values."""
    additional_categories = amazon_lighting_data["scenarios"]["Murano Glass"]["presta_categories"]["additional_categories"]
    assert isinstance(additional_categories, list)
    assert "" in additional_categories


def test_amazon_lighting_price_rule_type(amazon_lighting_data):
    """Tests if the price_rule is an integer type."""
    price_rule = amazon_lighting_data["scenarios"]["Murano Glass"]["price_rule"]
    assert isinstance(price_rule, int)

def test_amazon_lighting_missing_scenario_key(amazon_lighting_data):
    """Tests the case where a key is missing in a scenario."""
    with pytest.raises(KeyError):
        _ = amazon_lighting_data["scenarios"]["NonExistentScenario"]

def test_amazon_lighting_empty_scenarios(amazon_lighting_data):
    """Tests the case where scenarios are empty"""
    empty_data = {"scenarios": {}}
    with pytest.raises(KeyError):
       _ = empty_data["scenarios"]["NonExistentScenario"]
       
def test_amazon_lighting_invalid_data_type():
    """Tests the case where JSON data has invalid type."""
    invalid_data = "this is not a json"
    with pytest.raises(json.JSONDecodeError):
        json.loads(invalid_data)
```