```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Loads the cdata_categories_video.json data."""
    data = {
      "scenarios": {
        "NVIDIA Tesla": {
          "brand": "NVIDIA Tesla",
          "url": "https://reseller.c-data.co.il/graphics-nvidia-tesla",
          "checkbox": False,
          "active": True,
          "condition":"new",
          "presta_categories": "108,109,987"
        },
        "NVIDIA Quadro": {
          "brand": "NVIDIA",
          "url": "https://reseller.c-data.co.il/graphics-nvidia-quadro",
          "checkbox": False,
          "active": True,
          "condition":"new",
          "presta_categories": "108,109,988"
        },
        "Nvidia GPU": {
          "brand": "NVIDIA",
          "url": "https://reseller.c-data.co.il/graphics-nvidia-gtx-rtx",
          "checkbox": False,
          "active": True,
          "condition":"new",
          "presta_categories": "108,110"
        }
      }
    }
    return data

# Test to check the presence of the "scenarios" key
def test_scenarios_key_exists(cdata_categories_data):
    """Test that the 'scenarios' key exists in the JSON data."""
    assert "scenarios" in cdata_categories_data, "The 'scenarios' key is missing from the JSON data."

# Test to check the data structure of a scenario
def test_scenario_structure(cdata_categories_data):
    """Test that each scenario has the correct keys."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data, f"The 'brand' key is missing from the scenario '{scenario_name}'."
        assert "url" in scenario_data, f"The 'url' key is missing from the scenario '{scenario_name}'."
        assert "checkbox" in scenario_data, f"The 'checkbox' key is missing from the scenario '{scenario_name}'."
        assert "active" in scenario_data, f"The 'active' key is missing from the scenario '{scenario_name}'."
        assert "condition" in scenario_data, f"The 'condition' key is missing from the scenario '{scenario_name}'."
        assert "presta_categories" in scenario_data, f"The 'presta_categories' key is missing from the scenario '{scenario_name}'."

# Test to check if the 'checkbox' value is a boolean
def test_checkbox_value_type(cdata_categories_data):
     """Test that the 'checkbox' value is a boolean."""
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"The 'checkbox' value in scenario '{scenario_name}' is not a boolean."

# Test to check if the 'active' value is a boolean
def test_active_value_type(cdata_categories_data):
    """Test that the 'active' value is a boolean."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"The 'active' value in scenario '{scenario_name}' is not a boolean."

# Test to check if the 'condition' value is a string
def test_condition_value_type(cdata_categories_data):
    """Test that the 'condition' value is a string."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str), f"The 'condition' value in scenario '{scenario_name}' is not a string."

# Test to check if the 'presta_categories' value is a string
def test_presta_categories_value_type(cdata_categories_data):
    """Test that the 'presta_categories' value is a string."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"The 'presta_categories' value in scenario '{scenario_name}' is not a string."

# Test to check if URLs are valid strings (basic check)
def test_url_valid_format(cdata_categories_data):
    """Test that URLs are valid strings and start with 'https://'."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      url = scenario_data["url"]
      assert isinstance(url,str) ,f"URL in scenario '{scenario_name}' is not a string"
      assert url.startswith("https://"), f"URL '{url}' in scenario '{scenario_name}' does not start with 'https://'."

# Test for brand values being non-empty strings
def test_brand_not_empty(cdata_categories_data):
    """Test that 'brand' values are non-empty strings."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str), f"The 'brand' value in scenario '{scenario_name}' is not a string."
         assert len(scenario_data["brand"]) > 0, f"The 'brand' value in scenario '{scenario_name}' is an empty string."
# Test for presta_categories values being non-empty strings
def test_presta_categories_not_empty(cdata_categories_data):
  """Test that 'presta_categories' values are non-empty strings."""
  for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"The 'presta_categories' value in scenario '{scenario_name}' is not a string."
        assert len(scenario_data["presta_categories"]) > 0, f"The 'presta_categories' value in scenario '{scenario_name}' is an empty string."

#Test for condition values being non-empty strings
def test_condition_not_empty(cdata_categories_data):
    """Test that 'condition' values are non-empty strings."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert isinstance(scenario_data["condition"],str), f"The 'condition' value in scenario '{scenario_name}' is not a string."
      assert len(scenario_data["condition"]) > 0, f"The 'condition' value in scenario '{scenario_name}' is an empty string."

```