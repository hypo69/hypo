```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_categories_data():
    """Provides test data loaded from the JSON file."""
    file_path = "hypotez/src/suppliers/amazon/scenarios/amazon_categories_desktops_hp_used.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the structure of the loaded data
def test_amazon_categories_data_structure(amazon_categories_data):
    """Checks if the loaded JSON data has the expected top-level structure."""
    assert "scenarios" in amazon_categories_data, "The 'scenarios' key is missing in the JSON."
    assert isinstance(amazon_categories_data["scenarios"], dict), "The 'scenarios' value is not a dictionary."

# Test cases for individual scenarios
def test_amazon_categories_scenario_structure(amazon_categories_data):
    """Checks if individual scenario entries have the expected keys."""
    scenarios = amazon_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' is missing 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' is missing 'url' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key."
        assert "price_rule" in scenario_data, f"Scenario '{scenario_name}' is missing 'price_rule' key."

def test_amazon_categories_scenario_values(amazon_categories_data):
    """Checks if individual scenario entries have valid values."""
    scenarios = amazon_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' is not a string."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' is not a string."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' is not a boolean."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' is not a string."
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' is not a dict."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean."
        assert isinstance(scenario_data["price_rule"], int), f"Scenario '{scenario_name}' 'price_rule' is not an int."
        assert scenario_data["price_rule"] > 0, f"Scenario '{scenario_name}' 'price_rule' is not greater than 0"

def test_amazon_categories_presta_categories_structure(amazon_categories_data):
    """Checks the structure of the 'presta_categories' dictionary."""
    scenarios = amazon_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data["presta_categories"]
        assert "template" in presta_categories, f"Scenario '{scenario_name}' 'presta_categories' missing 'template' key."
        assert isinstance(presta_categories["template"], dict), f"Scenario '{scenario_name}' 'template' is not a dict"
        for key, value in presta_categories["template"].items():
            assert isinstance(key, str), f"Scenario '{scenario_name}' 'template' key '{key}' is not a string."
            assert isinstance(value, str), f"Scenario '{scenario_name}' 'template' value '{value}' is not a string."

def test_amazon_categories_url_validity(amazon_categories_data):
    """Basic check to make sure URLs are strings and not empty. More validation could be added"""
    scenarios = amazon_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        url = scenario_data["url"]
        assert isinstance(url, str), f"Scenario '{scenario_name}' url is not a string"
        assert len(url) > 0, f"Scenario '{scenario_name}' url is an empty string"
        assert url.startswith("https://"), f"Scenario '{scenario_name}' url does not start with https://"

def test_amazon_categories_condition_values(amazon_categories_data):
        """Checks if the condition key has the expected 'new' value"""
        scenarios = amazon_categories_data["scenarios"]
        for scenario_name, scenario_data in scenarios.items():
            condition = scenario_data["condition"]
            assert condition == "new", f"Scenario '{scenario_name}' condition is not 'new'"
```