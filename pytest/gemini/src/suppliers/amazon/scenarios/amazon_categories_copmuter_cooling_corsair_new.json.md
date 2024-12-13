```python
import pytest
import json

# Assuming the json data is loaded into a variable called `data`
# For testing purposes, let's define the data directly as a fixture
@pytest.fixture
def data():
    return {
        "scenarios": {
            "NEW CORSAIR LIQUID COOLING": {
                "brand": "CORSAIR",
                "url": "https://www.amazon.com/s?k=corsair&i=computers&rh=n%3A3015422011%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ACorsair&dc&ds=v1%3A4UdJ5kFgxTrEAPAFY6KYx4O48jHaTgY%2BkKFEZHAmBy4&qid=1674395191&rnid=2528832011&ref=sr_nr_p_89_1",
                "active": True,
                "condition": "ref",
                "presta_categories": {
                    "template": {"corsair": "LIQUID CPU COOLING"}
                },
                "checkbox": False,
                "price_rule": 1,
            },
            "NEW CORSAIR AIR CHAISES COOLING": {
                "brand": "CORSAIR",
                "url": "https://www.amazon.com/s?k=corsair&i=computers&rh=n%3A172282%2Cn%3A541966%2Cn%3A193870011%2Cn%3A17923671011%2Cn%3A3012290011%2Cn%3A11036291%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ACorsair&dc&ds=v1%3A62ROR5QIpRmdvHYid8HLE4S5XJ9aeeOJV%2B9%2Fka%2FPYS8&qid=1674395269&rnid=172282&ref=sr_nr_n_2",
                "active": True,
                "condition": "ref",
                "presta_categories": {
                    "template": {"corsair": "AIR CHAISES COOLING"}
                },
                "checkbox": False,
                "price_rule": 1,
            },
        }
    }

def test_scenarios_exist(data):
    """Checks if the 'scenarios' key exists in the data."""
    assert "scenarios" in data, "The 'scenarios' key should exist in the data."

def test_scenarios_not_empty(data):
   """Checks if the 'scenarios' dictionary is not empty."""
   assert data["scenarios"], "The 'scenarios' dictionary should not be empty."


def test_scenario_keys_exist(data):
    """Checks if specific keys exist in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' should have 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' should have 'url' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' should have 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' should have 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' should have 'presta_categories' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' should have 'checkbox' key."
        assert "price_rule" in scenario_data, f"Scenario '{scenario_name}' should have 'price_rule' key."

def test_scenario_brand_type(data):
    """Checks if the 'brand' key has a string value in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}''s 'brand' should be a string."

def test_scenario_url_type(data):
    """Checks if the 'url' key has a string value in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}''s 'url' should be a string."

def test_scenario_active_type(data):
    """Checks if the 'active' key has a boolean value in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}''s 'active' should be a boolean."

def test_scenario_condition_type(data):
     """Checks if the 'condition' key has a string value in each scenario."""
     for scenario_name, scenario_data in data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}''s 'condition' should be a string."

def test_scenario_presta_categories_type(data):
    """Checks if 'presta_categories' key has a dictionary value with a template key in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}''s 'presta_categories' should be a dict."
        assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}''s 'presta_categories' should have 'template' key."
        assert isinstance(scenario_data["presta_categories"]["template"],dict), f"Scenario '{scenario_name}''s 'template' should be a dict."


def test_scenario_checkbox_type(data):
    """Checks if the 'checkbox' key has a boolean value in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}''s 'checkbox' should be a boolean."

def test_scenario_price_rule_type(data):
    """Checks if the 'price_rule' key has an integer value in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert isinstance(scenario_data["price_rule"], int), f"Scenario '{scenario_name}''s 'price_rule' should be an integer."

def test_scenario_price_rule_positive(data):
    """Checks if the 'price_rule' key has a positive integer value in each scenario."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert scenario_data["price_rule"] > 0, f"Scenario '{scenario_name}''s 'price_rule' should be positive."


def test_scenario_url_is_valid(data):
    """Checks if the 'url' key has a valid URL format."""
    import re

    url_pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')

    for scenario_name, scenario_data in data["scenarios"].items():
        url = scenario_data["url"]
        assert bool(url_pattern.match(url)), f"Scenario '{scenario_name}''s 'url' is not a valid url."

def test_scenario_brand_not_empty(data):
    """Checks if the 'brand' key has not empty string value."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert scenario_data["brand"], f"Scenario '{scenario_name}''s 'brand' should not be empty."

def test_scenario_condition_not_empty(data):
    """Checks if the 'condition' key has not empty string value."""
    for scenario_name, scenario_data in data["scenarios"].items():
        assert scenario_data["condition"], f"Scenario '{scenario_name}''s 'condition' should not be empty."

def test_scenario_presta_categories_template_not_empty(data):
     """Checks if the template dictionary is not empty."""
     for scenario_name, scenario_data in data["scenarios"].items():
        assert scenario_data["presta_categories"]["template"], f"Scenario '{scenario_name}''s 'template' should not be empty."

```