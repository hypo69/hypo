```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def example_data():
    """Provides test data for the scenarios."""
    return {
        "scenarios": {
            "GForce": {
                "brand": "Nvidia",
                "url": "https://www.visualdg.co.il/169411-%D7%9B%D7%A8%D7%98%D7%99%D7%A1%D7%99-%D7%9E%D7%A1%D7%9A-ASUS/243216-Asus",
                "checkbox": False,
                "active": True,
                "condition":"new",
                "presta_categories": "108,524"
            }
        }
    }

def test_scenario_structure(example_data):
    """Checks the overall structure of the scenarios dictionary."""
    assert isinstance(example_data, dict)
    assert "scenarios" in example_data
    assert isinstance(example_data["scenarios"], dict)


def test_scenario_gforce_exists(example_data):
    """Checks if the 'GForce' scenario exists in the dictionary."""
    assert "GForce" in example_data["scenarios"]


def test_scenario_gforce_brand(example_data):
    """Checks the 'brand' value of the 'GForce' scenario."""
    assert example_data["scenarios"]["GForce"]["brand"] == "Nvidia"


def test_scenario_gforce_url(example_data):
    """Checks the 'url' value of the 'GForce' scenario."""
    assert example_data["scenarios"]["GForce"]["url"] == "https://www.visualdg.co.il/169411-%D7%9B%D7%A8%D7%98%D7%99%D7%A1%D7%99-%D7%9E%D7%A1%D7%9A-ASUS/243216-Asus"


def test_scenario_gforce_checkbox(example_data):
    """Checks the 'checkbox' value of the 'GForce' scenario."""
    assert example_data["scenarios"]["GForce"]["checkbox"] is False


def test_scenario_gforce_active(example_data):
    """Checks the 'active' value of the 'GForce' scenario."""
    assert example_data["scenarios"]["GForce"]["active"] is True


def test_scenario_gforce_condition(example_data):
     """Checks the 'condition' value of the 'GForce' scenario."""
     assert example_data["scenarios"]["GForce"]["condition"] == "new"

def test_scenario_gforce_presta_categories(example_data):
    """Checks the 'presta_categories' value of the 'GForce' scenario."""
    assert example_data["scenarios"]["GForce"]["presta_categories"] == "108,524"
    

def test_scenario_missing_key():
    """Checks the behavior when a key is missing from the scenario data."""
    data = {
         "scenarios": {
            "GForce": {
                "brand": "Nvidia",
                "url": "some_url",
                "checkbox": False,
                "active": True,
            }
        }
    }
    with pytest.raises(KeyError):
         _ = data["scenarios"]["GForce"]["condition"]
         
def test_scenario_empty_scenarios_dict():
    """Checks the behavior when the scenarios dictionary is empty."""
    data = {"scenarios": {}}
    assert data["scenarios"] == {}

def test_scenario_invalid_data_type():
     """Checks the behavior when one value has an invalid data type"""
     data = {
          "scenarios": {
            "GForce": {
                "brand": 123,
                "url": "https://www.visualdg.co.il/169411-%D7%9B%D7%A8%D7%98%D7%99%D7%A1%D7%99-%D7%9E%D7%A1%D7%9A-ASUS/243216-Asus",
                "checkbox": False,
                "active": True,
                "condition":"new",
                "presta_categories": "108,524"
            }
        }
     }
     assert isinstance(data["scenarios"]["GForce"]["brand"], int)

def test_scenario_multiple_scenarios():
     """Checks handling of multiple scenarios in the JSON."""
     data = {
          "scenarios": {
            "GForce": {
                "brand": "Nvidia",
                "url": "url_1",
                "checkbox": False,
                "active": True,
                "condition":"new",
                "presta_categories": "108,524"
            },
            "Radeon": {
                 "brand": "AMD",
                "url": "url_2",
                "checkbox": True,
                "active": False,
                "condition":"used",
                "presta_categories": "500,600"
            }
        }
     }
     assert len(data["scenarios"]) == 2
     assert data["scenarios"]["Radeon"]["brand"] == "AMD"
     assert data["scenarios"]["Radeon"]["checkbox"] == True
     assert data["scenarios"]["Radeon"]["active"] == False
     assert data["scenarios"]["Radeon"]["condition"] == "used"
     assert data["scenarios"]["Radeon"]["presta_categories"] == "500,600"
```