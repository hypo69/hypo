```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Loads the JSON data from the file."""
    file_location = "hypotez/src/suppliers/kualastyle/scenarios/childernsroom.json"
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data


def test_json_data_structure(json_data):
    """Checks if the top-level structure of the JSON is correct."""
    assert isinstance(json_data, dict), "The root should be a dictionary."
    assert "scenarios" in json_data, "The root should contain 'scenarios' key."
    assert isinstance(json_data["scenarios"], dict), "'scenarios' should be a dictionary."
    assert "Aronot" in json_data, "The root should contain 'Aronot' key."
    assert isinstance(json_data["Aronot"], dict), "'Aronot' should be a dictionary."


def test_scenario_noar_beds_keys(json_data):
    """Checks the keys of the 'Noar Beds' scenario."""
    noar_beds = json_data["scenarios"]["Noar Beds"]
    assert "url" in noar_beds, "Missing 'url' key in 'Noar Beds' scenario."
    assert "condition" in noar_beds, "Missing 'condition' key in 'Noar Beds' scenario."
    assert "presta_categories" in noar_beds, "Missing 'presta_categories' key in 'Noar Beds' scenario."
    assert "price_rule" in noar_beds, "Missing 'price_rule' key in 'Noar Beds' scenario."
    
def test_scenario_noar_beds_values(json_data):
        """Checks the values of the 'Noar Beds' scenario."""
        noar_beds = json_data["scenarios"]["Noar Beds"]
        assert isinstance(noar_beds["url"], str), "'url' should be a string."
        assert isinstance(noar_beds["condition"], str), "'condition' should be a string."
        assert isinstance(noar_beds["presta_categories"], dict), "'presta_categories' should be a dictionary."
        assert isinstance(noar_beds["price_rule"], int), "'price_rule' should be an integer."
        assert noar_beds["condition"] == "new", "'condition' should be equal to new."
        assert noar_beds["price_rule"] == 1, "'price_rule' should be equal to 1."

def test_scenario_noar_beds_presta_categories(json_data):
    """Checks the values of the 'Noar Beds' presta_categories."""
    noar_beds = json_data["scenarios"]["Noar Beds"]
    presta_categories = noar_beds["presta_categories"]
    assert "default_category" in presta_categories, "Missing 'default_category' in 'presta_categories'."
    default_category = presta_categories["default_category"]
    assert isinstance(default_category, dict), "'default_category' should be a dictionary."
    assert "11025" in default_category, "Missing '11025' in 'default_category'."
    assert isinstance(default_category["11025"], str), "Value of '11025' should be a string."
    assert default_category["11025"] == "home->furniture->childernroom->noarberd", "Incorrect value for category 11025."


def test_aronot_noar_beds_keys(json_data):
    """Checks the keys of the 'Aronot' -> 'Noar Beds' scenario."""
    aronot_noar_beds = json_data["Aronot"]["Noar Beds"]
    assert "url" in aronot_noar_beds, "Missing 'url' key in 'Aronot' -> 'Noar Beds' scenario."
    assert "condition" in aronot_noar_beds, "Missing 'condition' key in 'Aronot' -> 'Noar Beds' scenario."
    assert "presta_categories" in aronot_noar_beds, "Missing 'presta_categories' key in 'Aronot' -> 'Noar Beds' scenario."
    assert "price_rule" in aronot_noar_beds, "Missing 'price_rule' key in 'Aronot' -> 'Noar Beds' scenario."

def test_aronot_noar_beds_values(json_data):
        """Checks the values of the 'Aronot' -> 'Noar Beds' scenario."""
        aronot_noar_beds = json_data["Aronot"]["Noar Beds"]
        assert isinstance(aronot_noar_beds["url"], str), "'url' should be a string."
        assert isinstance(aronot_noar_beds["condition"], str), "'condition' should be a string."
        assert isinstance(aronot_noar_beds["presta_categories"], dict), "'presta_categories' should be a dictionary."
        assert isinstance(aronot_noar_beds["price_rule"], int), "'price_rule' should be an integer."
        assert aronot_noar_beds["condition"] == "new", "'condition' should be equal to new."
        assert aronot_noar_beds["price_rule"] == 1, "'price_rule' should be equal to 1."


def test_aronot_noar_beds_presta_categories(json_data):
    """Checks the values of the 'Aronot' -> 'Noar Beds' presta_categories."""
    aronot_noar_beds = json_data["Aronot"]["Noar Beds"]
    presta_categories = aronot_noar_beds["presta_categories"]
    assert "default_category" in presta_categories, "Missing 'default_category' in 'presta_categories'."
    default_category = presta_categories["default_category"]
    assert isinstance(default_category, dict), "'default_category' should be a dictionary."
    assert "11071" in default_category, "Missing '11071' in 'default_category'."
    assert isinstance(default_category["11071"], str), "Value of '11071' should be a string."
    assert default_category["11071"] == "home->furniture->childernroom->noarberd", "Incorrect value for category 11071."
```