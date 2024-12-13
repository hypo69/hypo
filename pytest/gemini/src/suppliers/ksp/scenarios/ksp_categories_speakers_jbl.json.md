```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_speakers_jbl_data():
    """Loads the JSON data from the specified file."""
    file_path = 'hypotez/src/suppliers/ksp/scenarios/ksp_categories_speakers_jbl.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test cases for the structure and content of the JSON data
def test_ksp_categories_speakers_jbl_data_structure(ksp_categories_speakers_jbl_data):
    """Checks if the loaded JSON data has the expected top-level structure."""
    assert "scenarios" in ksp_categories_speakers_jbl_data
    assert isinstance(ksp_categories_speakers_jbl_data["scenarios"], dict)

def test_ksp_categories_speakers_jbl_scenario_keys(ksp_categories_speakers_jbl_data):
    """Checks if the scenarios dictionary has expected keys."""
    expected_keys = ["BoomBox 2", "Xtreme 3", "Horizon 2", "Link Portable", "FLIP 5"]
    assert all(key in ksp_categories_speakers_jbl_data["scenarios"] for key in expected_keys)

def test_ksp_categories_speakers_jbl_scenario_values_structure(ksp_categories_speakers_jbl_data):
    """Checks if each scenario has the expected structure."""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
        assert isinstance(scenario, dict)
        assert "brand" in scenario
        assert "url" in scenario
        assert "checkbox" in scenario
        assert "active" in scenario
        assert "condition" in scenario
        assert "presta_categories" in scenario
        assert isinstance(scenario["presta_categories"], dict)
        
def test_ksp_categories_speakers_jbl_scenario_values_types(ksp_categories_speakers_jbl_data):
     """Checks if each scenario has values of expected types."""
     for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
        assert isinstance(scenario["brand"], str)
        assert isinstance(scenario["url"], str)
        assert isinstance(scenario["checkbox"], bool)
        assert isinstance(scenario["active"], bool)
        assert isinstance(scenario["condition"], str)

def test_ksp_categories_speakers_jbl_scenario_brand(ksp_categories_speakers_jbl_data):
    """Checks if all brands are JBL."""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
        assert scenario["brand"] == "JBL"

def test_ksp_categories_speakers_jbl_scenario_condition(ksp_categories_speakers_jbl_data):
    """Checks if all conditions are new."""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
        assert scenario["condition"] == "new"
        
def test_ksp_categories_speakers_jbl_presta_categories_content(ksp_categories_speakers_jbl_data):
    """Checks if the presta_categories have expected values."""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
       presta_categories = scenario["presta_categories"]
       assert presta_categories.get("3496") == "BT Speakers"
       assert presta_categories.get("3198") == "CONSUMER ELECTRONICS"
       assert presta_categories.get("3202") == "computer,smartphone,gaming console,smart device"
       assert presta_categories.get("3479") == "Speakers"
       assert presta_categories.get("2264") == "JBL"
       assert presta_categories.get("2623") == "Portable Bluetooth Speakers"

def test_ksp_categories_speakers_jbl_url_format(ksp_categories_speakers_jbl_data):
    """Checks if URLs have correct format and domain"""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
       assert scenario["url"].startswith("https://ksp.co.il/web/cat/")

def test_ksp_categories_speakers_jbl_checkbox_values(ksp_categories_speakers_jbl_data):
    """Checks if all checkbox values are false"""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
        assert scenario["checkbox"] == False

def test_ksp_categories_speakers_jbl_active_values(ksp_categories_speakers_jbl_data):
    """Checks if all active values are true"""
    for scenario in ksp_categories_speakers_jbl_data["scenarios"].values():
        assert scenario["active"] == True

def test_ksp_categories_speakers_jbl_specific_scenario_content(ksp_categories_speakers_jbl_data):
    """Checks content of a specific scenario"""
    boombox_scenario = ksp_categories_speakers_jbl_data["scenarios"]["BoomBox 2"]
    assert boombox_scenario["presta_categories"].get("2624") == "BoomBox 2"
    xtreme_scenario = ksp_categories_speakers_jbl_data["scenarios"]["Xtreme 3"]
    assert xtreme_scenario["presta_categories"].get("2625") == "Xtreme 3"
    horizon_scenario = ksp_categories_speakers_jbl_data["scenarios"]["Horizon 2"]
    assert horizon_scenario["presta_categories"].get("2626") == "Horizon 2"
    link_scenario = ksp_categories_speakers_jbl_data["scenarios"]["Link Portable"]
    assert link_scenario["presta_categories"].get("2627") == "Link Portable"
    flip_scenario = ksp_categories_speakers_jbl_data["scenarios"]["FLIP 5"]
    assert flip_scenario["presta_categories"].get("2628") == "FLIP 5"
```