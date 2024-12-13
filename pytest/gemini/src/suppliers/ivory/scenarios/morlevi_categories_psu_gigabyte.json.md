```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data as a dictionary."""
    json_string = """
    {
      "scenarios": {
        "AOURUS BY GIGABYTE 450W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "450W",
          "url": "--------------------------------------AOURUS BY GIGABYTE 450W-------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "158,511,188"
        },
        "AOURUS BY GIGABYTE 500W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "500W",
          "url": "--------------------------------------AOURUS BY GIGABYTE 500W-------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "158,511,189"
        },
        "AOURUS BY GIGABYTE 550W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "550W",
          "url": "---------------------------------AOURUS BY GIGABYTE 550W--------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "151,158,511,190"
        },
        "AOURUS BY GIGABYTE 600W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "600W",
          "url": "--------------------------------------AOURUS BY GIGABYTE 600W-------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "151,158,511,191"
        },
        "AOURUS BY GIGABYTE 650W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "650W",
          "url": "--------------------------------------AOURUS BY GIGABYTE 650W-------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "151,158,511,192"
        },
        "AOURUS BY GIGABYTE 700W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "700W",
          "url": "--------------------------------------AOURUS BY GIGABYTE 700W-------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "151,158,511,193"
        },
        "AOURUS BY GIGABYTE 750W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "750W",
          "url": "https://www.morlevi.co.il/Cat/339?p_145=670&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "151,158,511,194"
        },
        "AOURUS BY GIGABYTE 850W": {
          "brand": "AOURUS BY GIGABYTE",
          "name": "850W",
          "url": "https://www.morlevi.co.il/Cat/339?p_145=672&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "151,158,511,571"
        }
      }
    }
    """
    return json.loads(json_string)

# Test for correct structure of loaded data
def test_json_data_structure(json_data):
    """Checks if the json data is loaded as a dictionary and has the 'scenarios' key."""
    assert isinstance(json_data, dict)
    assert 'scenarios' in json_data
    assert isinstance(json_data['scenarios'], dict)

# Test for the number of scenarios in the data
def test_number_of_scenarios(json_data):
    """Checks if the expected number of scenarios are loaded."""
    assert len(json_data['scenarios']) == 8

# Test for correct scenario data
def test_scenario_450w_data(json_data):
    """Checks if the data of the 'AOURUS BY GIGABYTE 450W' scenario is loaded correctly."""
    scenario = json_data['scenarios']['AOURUS BY GIGABYTE 450W']
    assert scenario['brand'] == "AOURUS BY GIGABYTE"
    assert scenario['name'] == "450W"
    assert scenario['url'] == "--------------------------------------AOURUS BY GIGABYTE 450W-------------------------------------------"
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "158,511,188"

# Test for different scenario data
def test_scenario_850w_data(json_data):
    """Checks if the data of the 'AOURUS BY GIGABYTE 850W' scenario is loaded correctly."""
    scenario = json_data['scenarios']['AOURUS BY GIGABYTE 850W']
    assert scenario['brand'] == "AOURUS BY GIGABYTE"
    assert scenario['name'] == "850W"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/339?p_145=672&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "151,158,511,571"


# Test for correct data type of fields
def test_data_types(json_data):
    """Checks if the data types of the fields are as expected."""
    for scenario in json_data['scenarios'].values():
        assert isinstance(scenario['brand'], str)
        assert isinstance(scenario['name'], str)
        assert isinstance(scenario['url'], str)
        assert isinstance(scenario['checkbox'], bool)
        assert isinstance(scenario['active'], bool)
        assert isinstance(scenario['condition'], str)
        assert isinstance(scenario['presta_categories'], str)

# Test for empty scenarios (edge case)
def test_empty_scenarios():
    """Checks if the code correctly handles an empty scenarios dictionary"""
    empty_data = {"scenarios":{}}
    assert isinstance(empty_data, dict)
    assert 'scenarios' in empty_data
    assert isinstance(empty_data['scenarios'], dict)
    assert len(empty_data['scenarios']) == 0

# Test for missing "scenarios" key
def test_missing_scenarios_key():
        """Checks the handling of a dictionary with missing 'scenarios' key"""
        missing_key_data = {"other_key":{}}
        assert isinstance(missing_key_data, dict)
        assert 'scenarios' not in missing_key_data
        with pytest.raises(KeyError):
           missing_key_data['scenarios']
```