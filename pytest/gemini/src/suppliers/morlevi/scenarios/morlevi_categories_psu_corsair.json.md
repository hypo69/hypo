```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    with open('hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_psu_corsair.json', 'r') as f:
        return json.load(f)


def test_morlevi_categories_structure(morlevi_categories_data):
    """
    Test that the loaded JSON has the correct top-level structure.
    It checks if the JSON data contains a "scenarios" key.
    """
    assert "scenarios" in morlevi_categories_data, "The JSON should contain a 'scenarios' key"
    assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' should be a dictionary"


def test_morlevi_categories_keys(morlevi_categories_data):
    """
    Test if all scenario keys have the correct structure (brand, name, url, checkbox, active, condition, presta_categories).
    Iterates over each scenario in the loaded data and checks for the existence of each expected key.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' should contain a 'brand' key"
        assert "name" in scenario_data, f"Scenario '{scenario_name}' should contain a 'name' key"
        assert "url" in scenario_data, f"Scenario '{scenario_name}' should contain a 'url' key"
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' should contain a 'checkbox' key"
        assert "active" in scenario_data, f"Scenario '{scenario_name}' should contain an 'active' key"
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' should contain a 'condition' key"
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' should contain a 'presta_categories' key"


def test_morlevi_categories_data_types(morlevi_categories_data):
    """
    Test if the values in each scenario have the correct data types.
    Verifies that the 'brand' and 'name' values are strings, 'url' is a string,
    'checkbox' is a boolean, 'active' is a boolean, 'condition' is a string, and 'presta_categories' is a string.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Brand in '{scenario_name}' should be a string"
        assert isinstance(scenario_data["name"], str), f"Name in '{scenario_name}' should be a string"
        assert isinstance(scenario_data["url"], str), f"URL in '{scenario_name}' should be a string"
        assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in '{scenario_name}' should be a boolean"
        assert isinstance(scenario_data["active"], bool), f"Active in '{scenario_name}' should be a boolean"
        assert isinstance(scenario_data["condition"], str), f"Condition in '{scenario_name}' should be a string"
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' in '{scenario_name}' should be a string"

def test_morlevi_categories_checkbox_values(morlevi_categories_data):
    """
    Test if all 'checkbox' values are False.
    Iterates through each scenario and asserts that the value of 'checkbox' is always False.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"Checkbox in '{scenario_name}' should be False"


def test_morlevi_categories_active_values(morlevi_categories_data):
    """
    Test if all 'active' values are True.
    Iterates through each scenario and asserts that the value of 'active' is always True.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] == True, f"Active in '{scenario_name}' should be True"

def test_morlevi_categories_condition_values(morlevi_categories_data):
    """
    Test if all 'condition' values are 'new'.
    Iterates through each scenario and asserts that the value of 'condition' is always 'new'.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Condition in '{scenario_name}' should be 'new'"


def test_morlevi_categories_presta_categories_format(morlevi_categories_data):
    """
    Test if 'presta_categories' string consists of comma-separated numbers.
    Ensures that 'presta_categories' contains only digits and commas.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          presta_categories = scenario_data["presta_categories"]
          categories = presta_categories.split(",")
          for category in categories:
                assert category.isdigit(), f"'{category}' in 'presta_categories' should be a digit"

def test_morlevi_categories_url_format(morlevi_categories_data):
    """
    Test if 'url' values are either valid URLs or specific placeholders.
    Checks each URL. If it's a placeholder (starts with "---"), ignores it.
    Otherwise, tries to parse the URL, catching any errors.

    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        url = scenario_data["url"]
        if url.startswith("---"):
            continue
        try:
            from urllib.parse import urlparse
            result = urlparse(url)
            assert all([result.scheme, result.netloc]), f"'{url}' in '{scenario_name}' is not a valid URL"
        except:
              assert False, f"'{url}' in '{scenario_name}' is not a valid URL"
```