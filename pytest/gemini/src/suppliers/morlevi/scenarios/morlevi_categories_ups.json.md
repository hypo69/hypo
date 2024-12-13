```python
import pytest
import json

# Assuming the json data is loaded into a variable called `data`
# For the purpose of this test, let's simulate loading the json data:
TEST_JSON_DATA = """
{
  "scenarios": {
    "ups APC": {
      "brand": "APC",
      "url": "https://www.morlevi.co.il/Cat/332?p_315=86&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "158,247"
    },
    "ups EATON": {
      "brand": "EATON",
      "url": "https://www.morlevi.co.il/Cat/332?p_315=59&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "158,247"
    }
  }
}
"""

@pytest.fixture
def load_test_data():
    """Loads the test data from the JSON string."""
    return json.loads(TEST_JSON_DATA)


def test_scenario_keys_exist(load_test_data):
    """Test if the top level 'scenarios' key exists."""
    assert "scenarios" in load_test_data, "The 'scenarios' key is missing."


def test_scenario_is_dict(load_test_data):
    """Test if the 'scenarios' value is a dictionary."""
    assert isinstance(load_test_data["scenarios"], dict), "The 'scenarios' value is not a dictionary."


def test_scenario_contains_expected_keys(load_test_data):
    """Test that specific scenario keys exist in the 'scenarios' dictionary."""
    expected_scenarios = ["ups APC", "ups EATON"]
    for scenario_name in expected_scenarios:
        assert scenario_name in load_test_data["scenarios"], f"The '{scenario_name}' scenario is missing."


def test_scenario_values_are_dict(load_test_data):
     """Test if scenario values are dictionaries"""
     for scenario_name, scenario_data in load_test_data["scenarios"].items():
         assert isinstance(scenario_data, dict), f"The value for '{scenario_name}' is not a dictionary"



def test_scenario_has_required_fields(load_test_data):
    """Test that each scenario has the required fields."""
    required_fields = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in load_test_data["scenarios"].items():
        for field in required_fields:
            assert field in scenario_data, f"The '{field}' field is missing in the '{scenario_name}' scenario."


def test_scenario_field_types(load_test_data):
    """Test the types of specific fields in each scenario."""
    for scenario_name, scenario_data in load_test_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"The 'brand' field in '{scenario_name}' is not a string."
        assert isinstance(scenario_data["url"], str), f"The 'url' field in '{scenario_name}' is not a string."
        assert isinstance(scenario_data["checkbox"], bool), f"The 'checkbox' field in '{scenario_name}' is not a boolean."
        assert isinstance(scenario_data["active"], bool), f"The 'active' field in '{scenario_name}' is not a boolean."
        assert isinstance(scenario_data["condition"], str), f"The 'condition' field in '{scenario_name}' is not a string."
        assert isinstance(scenario_data["presta_categories"], str), f"The 'presta_categories' field in '{scenario_name}' is not a string."


def test_scenario_checkbox_is_false(load_test_data):
    """Test if 'checkbox' field is always set to false for every scenario."""
    for scenario_name, scenario_data in load_test_data["scenarios"].items():
         assert scenario_data["checkbox"] is False, f"The 'checkbox' field in '{scenario_name}' is not False"


def test_scenario_active_is_true(load_test_data):
    """Test if 'active' field is always set to true for every scenario."""
    for scenario_name, scenario_data in load_test_data["scenarios"].items():
         assert scenario_data["active"] is True, f"The 'active' field in '{scenario_name}' is not True"


def test_scenario_condition_is_new(load_test_data):
    """Test if 'condition' field is always set to 'new' for every scenario."""
    for scenario_name, scenario_data in load_test_data["scenarios"].items():
         assert scenario_data["condition"] == "new", f"The 'condition' field in '{scenario_name}' is not 'new'"


def test_presta_categories_is_string_of_numbers(load_test_data):
    """Test if 'presta_categories' contains comma separated numbers"""
    for scenario_name, scenario_data in load_test_data["scenarios"].items():
        categories = scenario_data["presta_categories"]
        categories_list = categories.split(',')
        for category in categories_list:
            assert category.isdigit(), f"The presta_categories value '{categories}' in '{scenario_name}' is not a comma separated string of numbers."


def test_empty_scenarios(load_test_data):
    """Tests handling of empty 'scenarios' case."""
    empty_data = json.loads('{"scenarios": {}}')
    assert isinstance(empty_data["scenarios"], dict)
    assert not empty_data["scenarios"]
    with pytest.raises(KeyError):
        # Tests KeyError if we try to access  a scenario that doesn't exist.
         empty_data["scenarios"]["non_existing_scenario"]



def test_invalid_json_format():
    """Tests handling of invalid JSON format."""
    invalid_json_string = '{"scenarios": "not a dict"}'
    with pytest.raises(json.JSONDecodeError):
        json.loads(invalid_json_string)


def test_invalid_field_type(load_test_data):
    """Test handling of invalid field type."""
    modified_data = json.loads(TEST_JSON_DATA)
    modified_data["scenarios"]["ups APC"]["active"] = "not a boolean"
    with pytest.raises(AssertionError):
        for scenario_name, scenario_data in modified_data["scenarios"].items():
            assert isinstance(scenario_data["active"], bool), f"The 'active' field in '{scenario_name}' is not a boolean."


def test_missing_required_field(load_test_data):
    """Test handling of missing required field."""
    modified_data = json.loads(TEST_JSON_DATA)
    del modified_data["scenarios"]["ups APC"]["brand"]
    with pytest.raises(AssertionError):
        for scenario_name, scenario_data in modified_data["scenarios"].items():
            required_fields = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
            for field in required_fields:
                assert field in scenario_data, f"The '{field}' field is missing in the '{scenario_name}' scenario."

```