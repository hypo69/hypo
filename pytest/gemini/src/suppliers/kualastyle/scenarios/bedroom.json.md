```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def bedroom_data():
    """Loads the bedroom.json data."""
    file_location = "hypotez/src/suppliers/kualastyle/scenarios/bedroom.json"
    with open(file_location, 'r') as f:
        return json.load(f)

# Test case for the 'Sliding Doors Closet' scenario
def test_sliding_doors_closet_scenario(bedroom_data):
    """
    Checks the 'Sliding Doors Closet' scenario properties
    """
    scenario = bedroom_data["scenarios"].get("Sliding Doors Closet")
    assert scenario is not None, "Sliding Doors Closet scenario not found"
    assert scenario["url"] == "https://kualastyle.com/collections/%D7%90%D7%A8%D7%95%D7%A0%D7%95%D7%AA-%D7%94%D7%96%D7%96%D7%94"
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["default_category"]["10994"] == "home->furniture->bedroom->Sliding Doors Closet"
    assert scenario["price_rule"] == 1

# Test case for the 'Beds' excluded category
def test_beds_excluded_category(bedroom_data):
    """
    Checks the 'Beds' excluded category properties
    """
    excluded = bedroom_data["excluded"].get("Beds")
    assert excluded is not None, "Beds excluded category not found"
    assert excluded["url"] == "https://kualastyle.com/collections/%D7%9E%D7%99%D7%98%D7%95%D7%AA-%D7%9C%D7%97%D7%93%D7%A8-%D7%A9%D7%99%D7%A0%D7%94"
    assert excluded["condition"] == "new"
    assert excluded["presta_categories"]["default_category"]["10985"] == "home->furniture->bedroom->beds"
    assert excluded["price_rule"] == 1

# Test case for missing scenario
def test_missing_scenario(bedroom_data):
    """
    Checks that accessing a missing scenario returns None
    """
    scenario = bedroom_data["scenarios"].get("NonExistentScenario")
    assert scenario is None, "Missing scenario should return None"

# Test case for missing excluded category
def test_missing_excluded_category(bedroom_data):
    """
    Checks that accessing a missing excluded category returns None
    """
    excluded = bedroom_data["excluded"].get("NonExistentCategory")
    assert excluded is None, "Missing excluded category should return None"

# Test case for empty scenarios
def test_empty_scenarios(bedroom_data):
    """
    Checks behavior when scenarios are empty (edge case)
    """
    bedroom_data["scenarios"] = {}
    scenario = bedroom_data["scenarios"].get("Sliding Doors Closet")
    assert scenario is None, "Should return None when scenarios are empty"

# Test case for empty excluded
def test_empty_excluded(bedroom_data):
     """
    Checks behavior when excluded are empty (edge case)
    """
    bedroom_data["excluded"] = {}
    excluded = bedroom_data["excluded"].get("Beds")
    assert excluded is None, "Should return None when excluded are empty"

# Test case for invalid JSON file path
def test_invalid_file_path():
    """
    Checks exception handling for invalid file path
    """
    invalid_file_location = "non_existent_file.json"
    with pytest.raises(FileNotFoundError):
        with open(invalid_file_location, 'r') as f:
            json.load(f)
```