```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_ups_data():
    """Loads the morlevi_categories_ups.json data."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_ups.json"
    with open(file_path, 'r') as f:
        return json.load(f)

def test_morlevi_categories_ups_data_structure(morlevi_categories_ups_data):
    """
    Test that the loaded JSON data has the expected 'scenarios' key,
    and that 'scenarios' value is a dictionary.
    """
    assert "scenarios" in morlevi_categories_ups_data
    assert isinstance(morlevi_categories_ups_data["scenarios"], dict)

def test_morlevi_categories_ups_scenario_keys(morlevi_categories_ups_data):
    """
    Test that each scenario within 'scenarios' has a brand, url, checkbox, active, condition, and presta_categories.
    """
    scenarios = morlevi_categories_ups_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_morlevi_categories_ups_scenario_data_types(morlevi_categories_ups_data):
     """
     Test that values in each scenario have the correct data types
     """
     scenarios = morlevi_categories_ups_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data["brand"], str)
         assert isinstance(scenario_data["url"], str)
         assert isinstance(scenario_data["checkbox"], bool)
         assert isinstance(scenario_data["active"], bool)
         assert isinstance(scenario_data["condition"], str)
         assert isinstance(scenario_data["presta_categories"], str)

def test_morlevi_categories_ups_scenario_url_format(morlevi_categories_ups_data):
    """
    Test that each scenario URL is a valid URL format (starts with https://)
    """
    scenarios = morlevi_categories_ups_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["url"].startswith("https://")

def test_morlevi_categories_ups_scenario_condition_values(morlevi_categories_ups_data):
     """
     Test that each scenario condition value is valid ("new", "used", "refurbished")
     """
     scenarios = morlevi_categories_ups_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
         assert scenario_data["condition"] in ["new", "used", "refurbished"]


def test_morlevi_categories_ups_scenario_presta_categories_format(morlevi_categories_ups_data):
    """
    Test that presta_categories is a comma-separated string of numbers
    """
    scenarios = morlevi_categories_ups_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        categories = scenario_data["presta_categories"].split(',')
        for category in categories:
            assert category.isdigit()

def test_morlevi_categories_ups_empty_scenarios(morlevi_categories_ups_data):
    """
    Test that scenarios exist within json file. if empty it is invalid json file.
    """
    assert morlevi_categories_ups_data["scenarios"]
    assert  len(morlevi_categories_ups_data["scenarios"])> 0

def test_morlevi_categories_ups_invalid_data_format():
     """
     Test for invalid data format, like missing the key "scenarios"
     """
     with open("hypotez/src/suppliers/ivory/scenarios/morlevi_categories_ups.json", 'r') as f:
          data = json.load(f)
          del data["scenarios"]
     with pytest.raises(KeyError):
          test_morlevi_categories_ups_data_structure({"test":data})

def test_morlevi_categories_ups_missing_key():
    """
    Test missing key inside scenario in data, this test must check each key is exist.
    """
    with open("hypotez/src/suppliers/ivory/scenarios/morlevi_categories_ups.json", 'r') as f:
        data = json.load(f)
        scenarios = data["scenarios"]
        for scenario in scenarios:
            del scenarios[scenario]["url"]
            break
    with pytest.raises(KeyError):
        test_morlevi_categories_ups_scenario_keys({"scenarios":scenarios})

```