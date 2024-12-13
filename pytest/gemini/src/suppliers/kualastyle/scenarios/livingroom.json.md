```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def livingroom_data():
    """Loads the livingroom.json data for testing."""
    file_path = "hypotez/src/suppliers/kualastyle/scenarios/livingroom.json"
    with open(file_path, 'r') as f:
        return json.load(f)

def test_livingroom_data_structure(livingroom_data):
    """
    Test that the loaded JSON data has the correct top-level structure.
    Verifies the presence of 'scenarios' and 'excluded' keys.
    """
    assert "scenarios" in livingroom_data
    assert "excluded" in livingroom_data

def test_scenarios_section(livingroom_data):
    """
    Test that the 'scenarios' section is present and contains valid data.
     Verifies that the 'scenarios' key exists and is a dictionary.
     Checks that each item in the 'scenarios' dictionary has 'url', 'condition', 'presta_categories', and 'price_rule' keys.
    """
    assert "scenarios" in livingroom_data
    assert isinstance(livingroom_data["scenarios"], dict)
    for key, value in livingroom_data["scenarios"].items():
        assert "url" in value
        assert "condition" in value
        assert "presta_categories" in value
        assert "price_rule" in value
        assert isinstance(value["presta_categories"], dict)
        assert "default_category" in value["presta_categories"]
        assert isinstance(value["presta_categories"]["default_category"], dict)
        
def test_excluded_section(livingroom_data):
    """
    Test the 'excluded' section is present and contains valid data.
    Verifies that the 'excluded' key exists and is a dictionary.
    Checks that each item in the 'excluded' dictionary has 'url', 'condition', 'presta_categories', and 'price_rule' keys.
    Also checks for optional 'active' and 'checkbox' keys.
    """
    assert "excluded" in livingroom_data
    assert isinstance(livingroom_data["excluded"], dict)
    for key, value in livingroom_data["excluded"].items():
        assert "url" in value
        assert "condition" in value
        assert "presta_categories" in value
        assert "price_rule" in value
        assert isinstance(value["presta_categories"], dict)
        assert "default_category" in value["presta_categories"]
        assert isinstance(value["presta_categories"]["default_category"], dict)
        
        # Check for optional keys
        if "active" in value:
           assert isinstance(value["active"], str)
        if "checkbox" in value:
           assert isinstance(value["checkbox"], str)

def test_scenarios_url_format(livingroom_data):
    """
    Test that the URLs in the 'scenarios' section have the correct format (start with 'https://').
    Checks that each URL value starts with "https://".
    """
    for key, value in livingroom_data["scenarios"].items():
        assert value["url"].startswith("https://")

def test_excluded_url_format(livingroom_data):
    """
     Test that the URLs in the 'excluded' section have the correct format (start with 'https://').
     Checks that each URL value starts with "https://".
    """
    for key, value in livingroom_data["excluded"].items():
        assert value["url"].startswith("https://")
        
def test_price_rule_value(livingroom_data):
    """
    Test that the price_rule in both 'scenarios' and 'excluded' sections are valid integers.
     Checks that the value of 'price_rule' is an integer.
    """
    for key, value in livingroom_data["scenarios"].items():
      assert isinstance(value["price_rule"], int)
    for key, value in livingroom_data["excluded"].items():
      assert isinstance(value["price_rule"], int)
```