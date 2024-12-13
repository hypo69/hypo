```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "REF lenovo DESKTOP INTEL I5": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565098&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565098%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_condition-type%3A16907720011%2Cp_n_feature_four_browse-bin%3A2289793011%2Cp_89%3ALenovo&dc&qid=1674307084&rnid=2528832011&ref=sr_nr_p_89_1&ds=v1%3AIAdNgWGJXPCgrRpng%2BDk9gjnN0r38POCeNus%2BZFjOOA",
          "active": true,
          "condition": "ref",
          "presta_categories": {
            "template": { "lenovo": "DESKTOPS INTEL I5" }
          },
          "checkbox": false,
          "price_rule": 1
        },
    
        "REF lenovo DESKTOP INTEL I7": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565098&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565098%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ADell%7Cdell%2Cp_n_condition-type%3A16907720011%2Cp_n_feature_four_browse-bin%3A2289792011&dc&qid=1674299080&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_1&ds=v1%3A%2FdybWSJv9V7xpKMaLknN8Xo3%2FPJOC%2FdkbA0bPV8g4UU",
          "active": true,
          "condition": "ref",
          "presta_categories": {
            "template": { "lenovo": "DESKTOPS INTEL I5" }
          },
          "checkbox": false,
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the amazon_data fixture itself
def test_amazon_data_fixture_loads(amazon_data):
    """Checks if the amazon_data fixture loads correctly."""
    assert isinstance(amazon_data, dict)
    assert "scenarios" in amazon_data
    assert isinstance(amazon_data["scenarios"], dict)
    assert len(amazon_data["scenarios"]) == 2


# Tests for scenario data
def test_scenario_has_correct_keys(amazon_data):
    """Check if each scenario has the correct keys"""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data
        assert "checkbox" in scenario_data
        assert "price_rule" in scenario_data

def test_scenario_brand_is_string(amazon_data):
    """Checks if the brand value is a string."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)

def test_scenario_url_is_string(amazon_data):
    """Checks if the url value is a string."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
         assert isinstance(scenario_data["url"], str)

def test_scenario_active_is_boolean(amazon_data):
    """Checks if the active value is a boolean."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool)

def test_scenario_condition_is_string(amazon_data):
    """Checks if the condition value is a string."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str)

def test_scenario_presta_categories_is_dict(amazon_data):
    """Checks if the presta_categories value is a dict."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
         assert isinstance(scenario_data["presta_categories"], dict)

def test_scenario_presta_categories_template_is_dict(amazon_data):
    """Checks if the template value inside presta_categories  is a dict."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
         assert isinstance(scenario_data["presta_categories"]["template"], dict)

def test_scenario_checkbox_is_boolean(amazon_data):
    """Checks if the checkbox value is a boolean."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool)

def test_scenario_price_rule_is_int(amazon_data):
    """Checks if the price_rule value is an integer."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert isinstance(scenario_data["price_rule"], int)

def test_scenario_valid_price_rule_value(amazon_data):
    """Checks if the price_rule value is valid."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert scenario_data["price_rule"] >= 0

def test_scenario_data_valid_brand(amazon_data):
    """Checks if brand is not empty string"""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert scenario_data["brand"] != ""

def test_scenario_data_valid_url(amazon_data):
    """Checks if url is not empty string"""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert scenario_data["url"] != ""

def test_scenario_data_valid_condition(amazon_data):
    """Checks if condition is not empty string"""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
         assert scenario_data["condition"] != ""

def test_scenario_data_valid_presta_categories(amazon_data):
     """Checks if presta_categories is not empty dictionary"""
     for scenario_name, scenario_data in amazon_data["scenarios"].items():
        assert scenario_data["presta_categories"] != {}

def test_scenario_data_valid_presta_categories_template(amazon_data):
     """Checks if template is not empty dictionary"""
     for scenario_name, scenario_data in amazon_data["scenarios"].items():
         assert scenario_data["presta_categories"]["template"] != {}
```