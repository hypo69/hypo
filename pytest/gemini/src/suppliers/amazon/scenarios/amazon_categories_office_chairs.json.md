```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def amazon_categories_office_chairs_data():
    """Provides the test data loaded from the JSON file."""
    json_data = """
    {
      "scenarios": {
        "office chairs": {
          "url": "https://amzn.to/3K2tABL",
          "condition": "new",
          "presta_categories": {
            "default_category": { "11236": "office chairs" },
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)


def test_amazon_categories_office_chairs_data_structure(amazon_categories_office_chairs_data):
    """
    Test that the basic structure of the JSON data is correct.
    Specifically, it checks if 'scenarios' key exists and is a dictionary.
    """
    assert isinstance(amazon_categories_office_chairs_data, dict), "The root is not a dictionary"
    assert "scenarios" in amazon_categories_office_chairs_data, "Missing 'scenarios' key"
    assert isinstance(amazon_categories_office_chairs_data["scenarios"], dict), "The 'scenarios' key is not a dictionary"


def test_amazon_categories_office_chairs_scenario_keys(amazon_categories_office_chairs_data):
    """
    Test that each scenario has the correct keys.
    This function assumes that there is a scenario named 'office chairs'.
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    assert "office chairs" in scenarios, "Missing 'office chairs' scenario"
    office_chairs_scenario = scenarios.get("office chairs", {})

    expected_keys = ["url", "condition", "presta_categories", "price_rule"]
    for key in expected_keys:
        assert key in office_chairs_scenario, f"Missing key: {key} in 'office chairs' scenario"


def test_amazon_categories_office_chairs_url_value(amazon_categories_office_chairs_data):
    """
    Test that the URL field of the scenario contains a string starting with "https://"
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    url = office_chairs_scenario.get("url")
    assert isinstance(url, str), "The URL must be a string"
    assert url.startswith("https://"), "The URL should start with https://"


def test_amazon_categories_office_chairs_condition_value(amazon_categories_office_chairs_data):
    """
    Test that the condition field of the scenario is equal to "new"
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    condition = office_chairs_scenario.get("condition")
    assert condition == "new", "The condition should be 'new'"


def test_amazon_categories_office_chairs_presta_categories_structure(amazon_categories_office_chairs_data):
    """
    Test the structure of the 'presta_categories' field
    It verifies that it contains default and additional categories keys
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    presta_categories = office_chairs_scenario.get("presta_categories")

    assert isinstance(presta_categories, dict), "The 'presta_categories' is not a dictionary"
    assert "default_category" in presta_categories, "Missing 'default_category' key in 'presta_categories'"
    assert "additional_categories" in presta_categories, "Missing 'additional_categories' key in 'presta_categories'"


def test_amazon_categories_office_chairs_default_category_structure(amazon_categories_office_chairs_data):
    """
    Test the structure of the 'default_category' field
    It verifies that it contains a dictionary mapping ID to category name
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    presta_categories = office_chairs_scenario.get("presta_categories")
    default_category = presta_categories.get("default_category")

    assert isinstance(default_category, dict), "The 'default_category' is not a dictionary"
    assert len(default_category) == 1, "The 'default_category' should have one entry"
    for category_id, category_name in default_category.items():
        assert isinstance(category_id, str), "The category ID should be a string"
        assert isinstance(category_name, str), "The category name should be a string"
    assert '11236' in default_category, "The 'default_category' does not contain key '11236'"


def test_amazon_categories_office_chairs_additional_categories_structure(amazon_categories_office_chairs_data):
    """
    Test the structure of the 'additional_categories' field
    It verifies that it contains a list
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    presta_categories = office_chairs_scenario.get("presta_categories")
    additional_categories = presta_categories.get("additional_categories")

    assert isinstance(additional_categories, list), "The 'additional_categories' is not a list"
    assert len(additional_categories) >= 0, "The 'additional_categories' should be a non-negative list"
    if additional_categories:
        for item in additional_categories:
            assert isinstance(item, str), "The 'additional_categories' items must be a string"


def test_amazon_categories_office_chairs_price_rule_type(amazon_categories_office_chairs_data):
    """
    Test that the price_rule field of the scenario is an integer
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    price_rule = office_chairs_scenario.get("price_rule")
    assert isinstance(price_rule, int), "The price_rule should be an integer"

def test_amazon_categories_office_chairs_price_rule_value(amazon_categories_office_chairs_data):
    """
    Test that the price_rule field of the scenario is equal to 1
    """
    scenarios = amazon_categories_office_chairs_data.get("scenarios", {})
    office_chairs_scenario = scenarios.get("office chairs", {})
    price_rule = office_chairs_scenario.get("price_rule")
    assert price_rule == 1, "The price_rule should be equal to 1"
```