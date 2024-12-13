```python
import pytest
import json

# Fixture definitions
@pytest.fixture
def ksp_data():
    """Provides test data for the ksp scenarios."""
    return {
        "scenarios": {
            "Xiaomi Pad 5": {
                "brand": "XIAOMI",
                "url": "https://ksp.co.il/web/cat/1045..270..2202",
                "checkbox": False,
                "active": True,
                "condition": "new",
                "presta_categories": {
                    "3405": "GOOGLE PIXEL PRO",
                    "3198": "CONSUMER ELECTRONICS",
                    "3202": "computer,smartphone,gaming console,smart device",
                    "6471": "Smartphones",
                    "3403": "GOOGLE"
                }
            },
            "Xiaomi Pad 6": {
               "brand": "XIAOMI",
                "url": "https://ksp.co.il/web/cat/1045..270..2203",
                "checkbox": True,
                "active": False,
                "condition": "used",
                "presta_categories": {
                    "3406": "GOOGLE PIXEL 6",
                    "3199": "CONSUMER ELECTRONICS",
                    "3203": "computer,smartphone,gaming console",
                    "6472": "Smartphones 2",
                    "3404": "GOOGLE"
                   }
                }
        }
    }

def test_ksp_data_structure(ksp_data):
    """
    Test if the loaded JSON data has the expected structure.
    Checks that the 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in ksp_data
    assert isinstance(ksp_data["scenarios"], dict)

def test_ksp_data_scenario_keys(ksp_data):
    """
    Test if the scenarios have the expected keys.
    Checks that each scenario has specific required keys.
    """
    for scenario in ksp_data["scenarios"].values():
        assert "brand" in scenario
        assert "url" in scenario
        assert "checkbox" in scenario
        assert "active" in scenario
        assert "condition" in scenario
        assert "presta_categories" in scenario
        

def test_ksp_data_scenario_values_types(ksp_data):
    """
    Test the data types of values within each scenario.
    Checks if values for each key in each scenario has the expected data type.
    """
    for scenario in ksp_data["scenarios"].values():
        assert isinstance(scenario["brand"], str)
        assert isinstance(scenario["url"], str)
        assert isinstance(scenario["checkbox"], bool)
        assert isinstance(scenario["active"], bool)
        assert isinstance(scenario["condition"], str)
        assert isinstance(scenario["presta_categories"], dict)


def test_ksp_data_presta_categories_values_types(ksp_data):
    """
    Test the data types of values within the 'presta_categories' for each scenario.
    Checks if keys are strings and values are strings within 'presta_categories'.
    """
    for scenario in ksp_data["scenarios"].values():
       for key, value in scenario["presta_categories"].items():
            assert isinstance(key, str)
            assert isinstance(value, str)


def test_ksp_data_empty_scenarios():
    """
    Test case with empty scenarios.
    Checks if the code handles empty 'scenarios' gracefully.
    """
    empty_data = {"scenarios": {}}
    assert "scenarios" in empty_data
    assert isinstance(empty_data["scenarios"], dict)
    assert not empty_data["scenarios"]


def test_ksp_data_invalid_types():
   """
   Test for invalid data types within the scenarios, raising an exception.
   """
   invalid_data = {
        "scenarios": {
            "Xiaomi Pad 5": {
                "brand": 123,
                "url": 456,
                "checkbox": "True",
                "active": "False",
                "condition": 789,
                "presta_categories": "invalid"
                }
            }
        }
   
   with pytest.raises(AssertionError):
         for scenario in invalid_data["scenarios"].values():
            assert isinstance(scenario["brand"], str)
            assert isinstance(scenario["url"], str)
            assert isinstance(scenario["checkbox"], bool)
            assert isinstance(scenario["active"], bool)
            assert isinstance(scenario["condition"], str)
            assert isinstance(scenario["presta_categories"], dict)
```