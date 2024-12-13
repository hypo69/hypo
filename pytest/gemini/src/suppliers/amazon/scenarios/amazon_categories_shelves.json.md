```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def amazon_categories_shelves_data():
    """Loads the test JSON data for the Amazon shelves scenario."""
    json_data = """
    {
      "scenarios": {
        "SHELVES": {
          "url": "https://amzn.to/3pObxZa",
          "condition": "new",
          "presta_categories": {
            "default_category": { "11060": "SHELVES" },
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the 'SHELVES' scenario within the JSON structure

def test_shelves_scenario_exists(amazon_categories_shelves_data):
    """Checks if the 'SHELVES' scenario exists in the JSON data."""
    assert "SHELVES" in amazon_categories_shelves_data["scenarios"]


def test_shelves_scenario_url(amazon_categories_shelves_data):
    """Checks if the 'url' for the 'SHELVES' scenario is correct."""
    assert amazon_categories_shelves_data["scenarios"]["SHELVES"]["url"] == "https://amzn.to/3pObxZa"


def test_shelves_scenario_condition(amazon_categories_shelves_data):
    """Checks if the 'condition' for the 'SHELVES' scenario is correct."""
    assert amazon_categories_shelves_data["scenarios"]["SHELVES"]["condition"] == "new"


def test_shelves_scenario_default_category(amazon_categories_shelves_data):
    """Checks if the 'default_category' for the 'SHELVES' scenario is correct."""
    assert amazon_categories_shelves_data["scenarios"]["SHELVES"]["presta_categories"]["default_category"] == { "11060": "SHELVES" }


def test_shelves_scenario_additional_categories(amazon_categories_shelves_data):
   """Checks if the 'additional_categories' for the 'SHELVES' scenario is correct."""
   assert amazon_categories_shelves_data["scenarios"]["SHELVES"]["presta_categories"]["additional_categories"] == [""]


def test_shelves_scenario_price_rule(amazon_categories_shelves_data):
    """Checks if the 'price_rule' for the 'SHELVES' scenario is correct."""
    assert amazon_categories_shelves_data["scenarios"]["SHELVES"]["price_rule"] == 1

def test_empty_scenarios(amazon_categories_shelves_data):
     """Checks if the 'scenarios' is not empty in the JSON data."""
     assert amazon_categories_shelves_data["scenarios"]

def test_scenario_structure_is_correct(amazon_categories_shelves_data):
      """Checks the structure of the "SHELVES" scenario including all expected keys"""
      expected_keys = ["url", "condition", "presta_categories", "price_rule"]
      actual_keys = amazon_categories_shelves_data["scenarios"]["SHELVES"].keys()
      assert all(key in actual_keys for key in expected_keys)


def test_presta_categories_structure_is_correct(amazon_categories_shelves_data):
     """Checks the structure of the "presta_categories" including all expected keys"""
     expected_keys = ["default_category", "additional_categories"]
     actual_keys = amazon_categories_shelves_data["scenarios"]["SHELVES"]["presta_categories"].keys()
     assert all(key in actual_keys for key in expected_keys)
```