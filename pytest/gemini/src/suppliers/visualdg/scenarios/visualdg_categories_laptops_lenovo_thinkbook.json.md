```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_data():
    """Loads the laptop data from the JSON file."""
    json_data = """
    {
      "scenarios": {
        "LENOVO THINKBOOK 13.4 - 13.3 I3": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "-----------------THINKBOOK 13.4 - 13.3 I3-------------r ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,4,370"
        },
        "LENOVO THINKBOOK 13.4 - 13.3 I5": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253273/253294",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,5,371"
        },
        "LENOVO THINKBOOK 13.4 - 13.3 I7": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253274/253294",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,6,372"
        },
        "LENOVO THINKBOOK 13.4 - 13.3 I9": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "----------------LENOVO THINKBOOK 13.4 - 13.3 I9------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,7,373"
        },
        "LENOVO THINKBOOK 13.4 - 13.3 AMD": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "--------------LENOVO THINKBOOK 13.4 - 13.3 AMD--------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,53,306,9,234,347"
        },
        "LENOVO THINKBOOK 14 I3": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "------------------------LENOVO THINKBOOK 14 I3----------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,4,377"
        },
        "LENOVO THINKBOOK 14 I5": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253273/253295",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,5,378"
        },
        "LENOVO THINKBOOK 14 I7": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253274/253295",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,6,379"
        },
        "LENOVO THINKBOOK 14 I9": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "----------------LENOVO THINKBOOK 14 I9------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,7,380"
        },
        "LENOVO THINKBOOK 14 AMD": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "----------------LENOVO THINKBOOK 14 AMD------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,234,381"
        },

        "LENOVO THINKBOOK 15 I3": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "----------------LENOVO THINKBOOK 15 I3------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,4,384"
        },
        "LENOVO THINKBOOK 15 I5": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253273/253296",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,5,385"
        },
        "LENOVO THINKBOOK 15 I7": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "https://www.visualdg.co.il/172332-%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkBook-/253274/253296",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,6,386"
        },
        "LENOVO THINKBOOK 15 I9": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "----------------LENOVO THINKBOOK 15 I9------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,7,387"
        },
        "LENOVO THINKBOOK 15 AMD": {
          "brand": "LENOVO",
          "template": "THINKBOOK",
          "url": "----------------LENOVO THINKBOOK 15 AMD------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,234,388"
        }
      }
    }
    """
    return json.loads(json_data)

def test_laptop_data_structure(laptop_data):
    """Checks if the data is a dictionary with a 'scenarios' key."""
    assert isinstance(laptop_data, dict)
    assert 'scenarios' in laptop_data

def test_laptop_scenarios_is_dict(laptop_data):
    """Checks if 'scenarios' value is a dictionary."""
    assert isinstance(laptop_data['scenarios'], dict)

def test_laptop_scenario_keys(laptop_data):
    """Checks if each scenario has the correct keys."""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert isinstance(scenario_data, dict)
        assert 'brand' in scenario_data
        assert 'template' in scenario_data
        assert 'url' in scenario_data
        assert 'checkbox' in scenario_data
        assert 'active' in scenario_data
        assert 'condition' in scenario_data
        assert 'presta_categories' in scenario_data
    
def test_laptop_scenario_data_types(laptop_data):
    """Checks if each scenario has the correct data types."""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert isinstance(scenario_data['brand'], str)
        assert isinstance(scenario_data['template'], str)
        assert isinstance(scenario_data['url'], str)
        assert isinstance(scenario_data['checkbox'], bool)
        assert isinstance(scenario_data['active'], bool)
        assert isinstance(scenario_data['condition'], str)
        assert isinstance(scenario_data['presta_categories'], str)

def test_laptop_brand_values(laptop_data):
  """Checks if the 'brand' values are as expected"""
  for scenario_name, scenario_data in laptop_data['scenarios'].items():
    assert scenario_data['brand'] == "LENOVO"

def test_laptop_template_values(laptop_data):
    """Checks if the 'template' values are as expected"""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert scenario_data['template'] == "THINKBOOK"

def test_laptop_checkbox_values(laptop_data):
    """Checks if the 'checkbox' values are always false"""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
      assert scenario_data['checkbox'] == False

def test_laptop_active_values(laptop_data):
    """Checks if the 'active' values are always True"""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
      assert scenario_data['active'] == True

def test_laptop_condition_values(laptop_data):
    """Checks if the 'condition' values are always new"""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
      assert scenario_data['condition'] == "new"


def test_laptop_presta_categories_format(laptop_data):
    """Checks if 'presta_categories' is a comma-separated string of numbers."""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        categories = scenario_data['presta_categories'].split(',')
        for cat in categories:
            assert cat.isdigit(), f"Category '{cat}' in '{scenario_name}' is not a number."
            
def test_laptop_url_not_empty(laptop_data):
    """Checks that urls are not empty strings"""
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert len(scenario_data["url"]) > 0
```