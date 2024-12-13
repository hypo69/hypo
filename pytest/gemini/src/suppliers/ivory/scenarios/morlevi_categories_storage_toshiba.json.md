```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def toshiba_data():
    """Loads the Toshiba categories data from the JSON file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_toshiba.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['scenarios']

# Test case for checking the presence of all scenarios
def test_all_scenarios_present(toshiba_data):
    """Checks that all the defined scenarios are present in the data."""
    expected_scenarios = [
        "internal_ssd_sata_3 120-128GB",
        "internal_ssd_sata_3 240-256GB",
        "internal_ssd_sata_3 480-525GB",
        "internal_ssd_sata_3 960GB-1TB",
        "internal_ssd_sata_3 2TB",
        "internal_ssd_sata_3 4TB",
        "internal_ssd_sata_3 8TB",
        "internal_ssd_msata 240-256GB",
        "internal_ssd_m2sata 240-256GB",
        "internal_ssd_m2sata 480-525GB",
        "internal_ssd_nvmi 240-256GB",
        "internal_ssd_nvmi 480-525GB",
        "internal_ssd_nvmi 960GB-1TB",
        "internal_ssd_nvmi 2TB",
        "internal_ssd_nvmi_gen4 240-256GB",
        "internal_ssd_nvmi_gen4 480-525GB",
        "internal_ssd_nvmi_gen4 960GB-1TB",
        "internal_ssd_nvmi_gen4 2TB",
        "external_ssd 500GB",
        "external_ssd 1TB",
        "external_ssd 2TB",
        "internal_hdd_35 1TB",
        "internal_hdd_35 2TB",
        "internal_hdd_35 3TB",
        "internal_hdd_35 4TB",
        "internal_hdd_35 6TB",
        "internal_hdd_35 8TB",
        "TOSHIBA internal_hdd_35 10TB",
        "internal_hdd_35 18TB",
        "internal_hdd_25 500GB",
         "internal_hdd_25 1TB",
        "external_hdd_25 1TB",
        "external_hdd_25 2TB",
        "external_hdd_25 4TB",
        "external_hdd_25 5TB",
        "external_hdd_35 4TB",
         "external_hdd_35 6TB",
         "external_hdd_35 8TB",
        "external_hdd_35 10TB"
    ]
    assert set(toshiba_data.keys()) == set(expected_scenarios)

# Test case for checking the structure of a single scenario
def test_scenario_structure(toshiba_data):
    """Checks if a sample scenario has the correct keys."""
    sample_scenario = toshiba_data.get("internal_ssd_sata_3 120-128GB")
    expected_keys = {"brand", "name", "url", "checkbox", "active", "condition", "presta_categories"}
    assert set(sample_scenario.keys()) == expected_keys

# Test case to check correct brand assignment
def test_brand_assignment(toshiba_data):
    """Checks that all scenarios have the correct brand ('TOSHIBA')."""
    for scenario in toshiba_data.values():
        assert scenario["brand"] == "TOSHIBA"

# Test case to check if 'active' is always True
def test_active_status(toshiba_data):
    """Checks that the 'active' field is always True for all scenarios."""
    for scenario in toshiba_data.values():
         assert scenario["active"] is True

# Test case to check if 'checkbox' is always False
def test_checkbox_status(toshiba_data):
     """Checks that the 'checkbox' field is always False for all scenarios."""
     for scenario in toshiba_data.values():
          assert scenario["checkbox"] is False

# Test case to check if 'condition' is always new
def test_condition_status(toshiba_data):
     """Checks that the 'condition' field is always new for all scenarios."""
     for scenario in toshiba_data.values():
          assert scenario["condition"] == 'new'

# Test case for presta_categories is not empty
def test_presta_categories_not_empty(toshiba_data):
     """Checks that the 'presta_categories' field is not empty for all scenarios."""
     for scenario in toshiba_data.values():
        assert scenario["presta_categories"]

# Test case for presta_categories is string
def test_presta_categories_is_string(toshiba_data):
     """Checks that the 'presta_categories' field is string for all scenarios."""
     for scenario in toshiba_data.values():
          assert isinstance(scenario["presta_categories"], str)


# Test case for url is not empty
def test_url_not_empty(toshiba_data):
     """Checks that the 'url' field is not empty for all scenarios."""
     for scenario in toshiba_data.values():
          assert scenario["url"]

# Test case for url is string
def test_url_is_string(toshiba_data):
     """Checks that the 'url' field is string for all scenarios."""
     for scenario in toshiba_data.values():
          assert isinstance(scenario["url"], str)

# Test case for name is not empty
def test_name_not_empty(toshiba_data):
     """Checks that the 'name' field is not empty for all scenarios."""
     for scenario in toshiba_data.values():
          assert scenario["name"]
# Test case for name is string
def test_name_is_string(toshiba_data):
     """Checks that the 'name' field is string for all scenarios."""
     for scenario in toshiba_data.values():
          assert isinstance(scenario["name"], str)
```