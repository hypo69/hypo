```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_categories_consoles_data():
    """Provides the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "Consoles Entrance chests": {
          "url": "https://amzn.to/3K1wqqD",
          "condition": "new",
          "presta_categories": {
            "default_category": { "11199": "Consoles Entrance chests" },
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)


def test_amazon_categories_consoles_data_structure(amazon_categories_consoles_data):
    """Checks if the loaded JSON data has the expected structure."""
    assert "scenarios" in amazon_categories_consoles_data
    assert isinstance(amazon_categories_consoles_data["scenarios"], dict)


def test_amazon_categories_consoles_scenario_presence(amazon_categories_consoles_data):
    """Checks if the 'Consoles Entrance chests' scenario is present."""
    assert "Consoles Entrance chests" in amazon_categories_consoles_data["scenarios"]


def test_amazon_categories_consoles_url_is_string(amazon_categories_consoles_data):
    """Checks if the URL is a string."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    assert isinstance(scenario["url"], str)


def test_amazon_categories_consoles_condition_is_string(amazon_categories_consoles_data):
    """Checks if the condition is a string."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    assert isinstance(scenario["condition"], str)


def test_amazon_categories_consoles_condition_value(amazon_categories_consoles_data):
     """Checks if the condition value is correct."""
     scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
     assert scenario["condition"] == "new"

def test_amazon_categories_consoles_presta_categories_structure(amazon_categories_consoles_data):
    """Checks if 'presta_categories' has the expected structure."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    assert "presta_categories" in scenario
    assert isinstance(scenario["presta_categories"], dict)
    assert "default_category" in scenario["presta_categories"]
    assert "additional_categories" in scenario["presta_categories"]


def test_amazon_categories_consoles_default_category_structure(amazon_categories_consoles_data):
    """Checks the structure of 'default_category'."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    default_category = scenario["presta_categories"]["default_category"]
    assert isinstance(default_category, dict)
    assert "11199" in default_category
    

def test_amazon_categories_consoles_default_category_value(amazon_categories_consoles_data):
    """Checks if the value in the default category is correct."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    default_category = scenario["presta_categories"]["default_category"]
    assert default_category["11199"] == "Consoles Entrance chests"

def test_amazon_categories_consoles_additional_categories_structure(amazon_categories_consoles_data):
    """Checks the structure of 'additional_categories'."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    additional_categories = scenario["presta_categories"]["additional_categories"]
    assert isinstance(additional_categories, list)


def test_amazon_categories_consoles_additional_categories_content(amazon_categories_consoles_data):
    """Checks if the content in 'additional_categories' is correct."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    additional_categories = scenario["presta_categories"]["additional_categories"]
    assert additional_categories == [""]

def test_amazon_categories_consoles_price_rule_is_integer(amazon_categories_consoles_data):
    """Checks if the price_rule is an integer."""
    scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
    assert isinstance(scenario["price_rule"], int)

def test_amazon_categories_consoles_price_rule_value(amazon_categories_consoles_data):
     """Checks if the price_rule value is correct."""
     scenario = amazon_categories_consoles_data["scenarios"]["Consoles Entrance chests"]
     assert scenario["price_rule"] == 1
```