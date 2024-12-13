```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data from the specified file."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_storage_sandisk.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def test_data_is_loaded(morlevi_categories_data):
    """Check if the fixture loads data correctly."""
    assert morlevi_categories_data is not None
    assert isinstance(morlevi_categories_data, dict)
    assert "scenarios" in morlevi_categories_data


def test_scenario_keys_exist(morlevi_categories_data):
    """Check if all expected keys exist in a scenario."""
    scenarios = morlevi_categories_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data, f"Missing 'brand' key in scenario: {scenario_name}"
        assert "name" in scenario_data, f"Missing 'name' key in scenario: {scenario_name}"
        assert "url" in scenario_data, f"Missing 'url' key in scenario: {scenario_name}"
        assert "checkbox" in scenario_data, f"Missing 'checkbox' key in scenario: {scenario_name}"
        assert "active" in scenario_data, f"Missing 'active' key in scenario: {scenario_name}"
        assert "condition" in scenario_data, f"Missing 'condition' key in scenario: {scenario_name}"
        assert "presta_categories" in scenario_data, f"Missing 'presta_categories' key in scenario: {scenario_name}"


def test_scenario_data_types(morlevi_categories_data):
    """Check if the values in the scenarios have correct data types."""
    scenarios = morlevi_categories_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data["brand"], str), f"'brand' should be a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["name"], str), f"'name' should be a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["url"], str), f"'url' should be a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["checkbox"], bool), f"'checkbox' should be a boolean in scenario: {scenario_name}"
        assert isinstance(scenario_data["active"], bool), f"'active' should be a boolean in scenario: {scenario_name}"
        assert isinstance(scenario_data["condition"], str), f"'condition' should be a string in scenario: {scenario_name}"
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' should be a string in scenario: {scenario_name}"


def test_valid_url_format_internal_ssd(morlevi_categories_data):
    """Check if url is valid for internal ssd categories."""
    scenarios = morlevi_categories_data.get("scenarios", {})
    internal_ssd_categories = [
        "internal_ssd_sata_3 120-128GB",
        "internal_ssd_sata_3 240-256GB",
        "internal_ssd_sata_3 480-525GB",
        "internal_ssd_nvmi 240-256GB",
        "internal_ssd_nvmi 480-525GB",
        "internal_ssd_nvmi 960GB-1TB"
    ]
    for category in internal_ssd_categories:
         url = scenarios[category]["url"]
         assert url.startswith("https://www.morlevi.co.il/Cat/"), f"Invalid URL format for category: {category}"


def test_url_is_not_empty(morlevi_categories_data):
    """Check if any URL is empty string"""
    scenarios = morlevi_categories_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
         url = scenario_data["url"]
         assert len(url) > 0, f"URL is empty for category: {scenario_name}"


def test_presta_categories_format(morlevi_categories_data):
    """Check if presta_categories string contains comma separated integers"""
    scenarios = morlevi_categories_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
         presta_categories = scenario_data["presta_categories"]
         categories_list = presta_categories.split(',')
         for category_id in categories_list:
             assert category_id.isdigit(), f"presta_categories contains non-integer value in scenario: {scenario_name}"


def test_all_scenarios_active(morlevi_categories_data):
    """Check if all scenarios are active."""
    scenarios = morlevi_categories_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
         assert scenario_data["active"] is True, f"Scenario {scenario_name} is not active"
```