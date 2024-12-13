```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def ksp_data():
    """Loads the ksp_categories_headphones_xiaomi.json data."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_headphones_xiaomi.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test case for valid scenario 'In-ear Bud'
def test_in_ear_bud_scenario_valid(ksp_data):
    """Tests the 'In-ear Bud' scenario with valid data."""
    scenario = ksp_data["scenarios"]["In-ear Bud"]
    assert scenario["brand"] == "XIAOMI"
    assert scenario["url"] == "https://ksp.co.il/web/cat/242..2202..1250"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["template"]["xiaomi"] == "HEADPHONES"

# Test case for valid scenario 'Xiaomi Mi In-ear Bud cable 3.5mm connection'
def test_xiaomi_mi_in_ear_bud_cable_scenario_valid(ksp_data):
    """Tests the 'Xiaomi Mi In-ear Bud cable 3.5mm connection' scenario with valid data."""
    scenario = ksp_data["scenarios"]["Xiaomi Mi In-ear Bud cable 3.5mm connection"]
    assert scenario["brand"] == "XIAOMI"
    assert scenario["url"] == "https://ksp.co.il/web/cat/242..2202..1250..5162"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["3459"] == "Xiaomi Mi In-ear Bud cable 3.5mm connection"
    assert scenario["presta_categories"]["template"]["xiaomi"] == "HEADPHONES"
    assert scenario["presta_categories"]["2250"] == "brand:  XIAOMI"
    assert scenario["presta_categories"]["2479"] == "BT Earbuds"
    assert scenario["presta_categories"]["3494"] == "Redmi Buds 3"

# Test case for missing 'scenarios' key
def test_missing_scenarios_key():
    """Tests for KeyError if 'scenarios' key is missing."""
    data = {}
    with pytest.raises(KeyError):
        scenarios = data["scenarios"]


# Test case for an empty 'scenarios' dictionary
def test_empty_scenarios_dictionary():
    """Tests with an empty scenarios dictionary."""
    data = {"scenarios": {}}
    assert data["scenarios"] == {}


# Test case for scenario with missing keys
def test_missing_keys_in_scenario(ksp_data):
    """Tests if a scenario is missing a key, like 'brand'."""
    scenario = ksp_data["scenarios"]["In-ear Bud"]
    with pytest.raises(KeyError):
      scenario["non_existent_key"]

# Test case for an invalid url format
def test_invalid_url_format(ksp_data):
  """Tests for incorrect url format"""
  scenario = ksp_data["scenarios"]["In-ear Bud"]
  assert isinstance(scenario["url"], str)
  assert scenario["url"].startswith("https://")


# Test case for presta_categories with wrong type
def test_presta_categories_wrong_type():
    """Test for presta_categories having a wrong type"""
    data = {
          "scenarios": {
            "In-ear Bud": {
                "brand": "XIAOMI",
              "url": "https://ksp.co.il/web/cat/242..2202..1250",
                "checkbox": False,
                "active": True,
              "condition":"new",
                "presta_categories": 123  # This is the wrong type
              }
          }
    }
    with pytest.raises(TypeError):
        data["scenarios"]["In-ear Bud"]["presta_categories"]["template"]["xiaomi"]
```