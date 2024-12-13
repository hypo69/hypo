```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def gigabyte_laptop_data():
    """Provides the test data loaded from the JSON file."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_laptops_gigabyte.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['scenarios']

# Test cases for valid data
def test_gigabyte_laptop_i3_11_valid(gigabyte_laptop_data):
    """Check if the categories for GIGABYTE 11.6 I3 are correct."""
    scenario = gigabyte_laptop_data.get("GIGABYTE 11.6 I3")
    assert scenario is not None
    assert scenario["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS INTEL I3", "11"]
    assert scenario["brand"] == "GIGABYTE"
    assert scenario["condition"] == "new"
    assert scenario["active"] is True

def test_gigabyte_laptop_i5_15_valid(gigabyte_laptop_data):
    """Check if the categories for GIGABYTE 15 I5 are correct."""
    scenario = gigabyte_laptop_data.get("GIGABYTE 15 I5")
    assert scenario is not None
    assert scenario["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS INTEL I5", "15"]
    assert scenario["brand"] == "GIGABYTE"
    assert scenario["condition"] == "new"
    assert scenario["active"] is True
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/358?p_315=2&p_238=1145&p_387=3414&sort=datafloat2%2Cprice&keyword="

def test_gigabyte_laptop_amd_17_valid(gigabyte_laptop_data):
    """Check if the categories for GIGABYTE 17.3 AMD are correct."""
    scenario = gigabyte_laptop_data.get("GIGABYTE 17.3 AMD")
    assert scenario is not None
    assert scenario["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS AMD", "17"]
    assert scenario["brand"] == "GIGABYTE"
    assert scenario["condition"] == "new"
    assert scenario["active"] is True


def test_gigabyte_laptop_celeron_14_valid(gigabyte_laptop_data):
    """Check if the categories for GIGABYTE 14 Celeron are correct."""
    scenario = gigabyte_laptop_data.get("GIGABYTE 14 Celeron")
    assert scenario is not None
    assert scenario["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS INTEL CELERON", "14"]
    assert scenario["brand"] == "GIGABYTE"
    assert scenario["condition"] == "new"
    assert scenario["active"] is True

def test_gigabyte_laptop_ryzen_5_15_valid(gigabyte_laptop_data):
    """Check if the categories for GIGABYTE 15 AMD RYZEN 5 are correct."""
    scenario = gigabyte_laptop_data.get("GIGABYTE 15 AMD RYZEN 5")
    assert scenario is not None
    assert scenario["presta_categories"]["template"]["gigabyte"] == ["LAPTOPS AMD RYZEN 5", "15"]
    assert scenario["brand"] == "GIGABYTE"
    assert scenario["condition"] == "new"
    assert scenario["active"] is True
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/358?p_315=2&p_238=1145&p_387=3743&sort=datafloat2%2Cprice&keyword="

def test_gigabyte_laptop_all_keys_present(gigabyte_laptop_data):
    """Check if all scenarios have the required keys."""
    for scenario_name, scenario in gigabyte_laptop_data.items():
      assert "brand" in scenario
      assert "url" in scenario
      assert "checkbox" in scenario
      assert "active" in scenario
      assert "condition" in scenario
      assert "presta_categories" in scenario
      assert "template" in scenario["presta_categories"]
      assert "gigabyte" in scenario["presta_categories"]["template"]


# Test cases for edge cases
def test_gigabyte_laptop_url_is_null(gigabyte_laptop_data):
    """Check scenarios with null URLs."""
    for scenario_name, scenario in gigabyte_laptop_data.items():
        if scenario_name not in ["GIGABYTE 15 I5", "GIGABYTE 15 I7","GIGABYTE 15 AMD RYZEN 5","GIGABYTE 14 I5"]:
           assert scenario["url"] is None



def test_gigabyte_laptop_checkbox_false_for_all(gigabyte_laptop_data):
    """Check if all scenarios have checkbox set to false."""
    for scenario_name, scenario in gigabyte_laptop_data.items():
        assert scenario["checkbox"] is False
        
def test_gigabyte_laptop_active_true_for_all(gigabyte_laptop_data):
    """Check if all scenarios have active set to true."""
    for scenario_name, scenario in gigabyte_laptop_data.items():
        assert scenario["active"] is True
        
def test_gigabyte_laptop_condition_new_for_all(gigabyte_laptop_data):
    """Check if all scenarios have condition set to new."""
    for scenario_name, scenario in gigabyte_laptop_data.items():
        assert scenario["condition"] == "new"

# Test for invalid or missing data (None scenarios)
def test_gigabyte_laptop_invalid_scenario(gigabyte_laptop_data):
    """Check if accessing a non-existent scenario returns None."""
    scenario = gigabyte_laptop_data.get("NonExistentScenario")
    assert scenario is None

def test_gigabyte_laptop_missing_category_data():
    """Check error handling when category data is missing or incomplete."""
    # Create a mock data dictionary with missing category data
    mock_data = {
    "scenarios": {
      "TEST_MISSING": {
        "brand": "GIGABYTE",
        "url": null,
        "checkbox": false,
        "active": true,
        "condition": "new"

      }}
    }

    # Check that key errors are handled
    with pytest.raises(KeyError):
      scenario = mock_data["scenarios"].get("TEST_MISSING")
      assert scenario is not None
      assert scenario["presta_categories"]["template"]["gigabyte"] # This would fail



def test_gigabyte_laptop_empty_categories():
   """Check handling of empty category data."""
   mock_data = {
    "scenarios": {
      "TEST_EMPTY": {
        "brand": "GIGABYTE",
        "url": None,
        "checkbox": False,
        "active": True,
        "condition": "new",
        "presta_categories": {
          "template": {
            "gigabyte": []
          }
        }
      }
     }
    }
   # Test that an empty list is handled without errors
   scenario = mock_data["scenarios"].get("TEST_EMPTY")
   assert scenario is not None
   assert scenario["presta_categories"]["template"]["gigabyte"] == []



```