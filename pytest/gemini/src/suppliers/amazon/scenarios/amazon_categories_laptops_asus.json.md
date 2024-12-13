```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data as a dictionary."""
    json_string = """
    {
      "store": {
        "store_id": "",
        "supplier_id": "",
        "get store banners": true,
        "description": "ASUS laptops",
        "about": "ASUS laptops",
        
        "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AAcer&dc&qid=1671859579&rnid=2528832011&ref=sr_nr_p_89_2&ds=v1%3Aug88%2Bcw6xXqu9pU7BCAPtyLlMbg8LlAfoW9fTRvciDo",
        "shop categories page": "",
        "shop categories json file": ""
      },

      "scenarios": {
        "ASUS INTEL CELERON": {
          "brand": "DELL",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ADell%2Cp_n_feature_four_browse-bin%3A1264444011&dc&qid=1671871063&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_3&ds=v1%3AKCj1uS039qeaZ2R6HdoHqgStringFormatterkBHKy61GaNmpCn%2FDs9s",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "asus": "LAPTOPS INTEL CELERON" }
          },
          "checkbox": false,
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_string)

# Test for the 'store' section
def test_store_section_exists(json_data):
    """Checks if the 'store' section exists in the JSON data."""
    assert "store" in json_data

def test_store_section_has_correct_keys(json_data):
    """Checks if all the expected keys are present in the 'store' section."""
    expected_keys = ["store_id", "supplier_id", "get store banners", "description", "about", "url", "shop categories page", "shop categories json file"]
    assert all(key in json_data["store"] for key in expected_keys)

def test_store_url_is_correct(json_data):
  """Checks if the url in the store section is a valid URL."""
  store_url = json_data["store"]["url"]
  assert store_url.startswith("https://www.amazon.com")


def test_store_description_is_correct(json_data):
  """Checks if the store description matches the expected value."""
  assert json_data["store"]["description"] == "ASUS laptops"


def test_store_about_is_correct(json_data):
  """Checks if the store 'about' matches the expected value"""
  assert json_data["store"]["about"] == "ASUS laptops"


def test_store_get_store_banners_is_boolean(json_data):
  """Checks that the 'get store banners' key is a boolean"""
  assert type(json_data["store"]["get store banners"]) is bool


# Test for the 'scenarios' section
def test_scenarios_section_exists(json_data):
    """Checks if the 'scenarios' section exists in the JSON data."""
    assert "scenarios" in json_data

def test_scenarios_contains_at_least_one_scenario(json_data):
  """Check if the scenarios section is not empty"""
  assert len(json_data["scenarios"]) > 0

def test_scenarios_asus_intel_celeron_exists(json_data):
    """Checks if the 'ASUS INTEL CELERON' scenario exists."""
    assert "ASUS INTEL CELERON" in json_data["scenarios"]

def test_scenario_asus_intel_celeron_has_correct_keys(json_data):
    """Checks if all the expected keys are present in the 'ASUS INTEL CELERON' scenario."""
    expected_keys = ["brand", "url", "active", "condition", "presta_categories", "checkbox", "price_rule"]
    assert all(key in json_data["scenarios"]["ASUS INTEL CELERON"] for key in expected_keys)

def test_scenario_asus_intel_celeron_brand_is_correct(json_data):
    """Checks if the brand is correctly set to DELL"""
    assert json_data["scenarios"]["ASUS INTEL CELERON"]["brand"] == "DELL"

def test_scenario_asus_intel_celeron_url_is_correct(json_data):
    """Checks if the url in the 'ASUS INTEL CELERON' scenario is a valid URL."""
    scenario_url = json_data["scenarios"]["ASUS INTEL CELERON"]["url"]
    assert scenario_url.startswith("https://www.amazon.com")


def test_scenario_asus_intel_celeron_active_is_boolean(json_data):
  """Checks if the 'active' value is a boolean"""
  assert type(json_data["scenarios"]["ASUS INTEL CELERON"]["active"]) is bool

def test_scenario_asus_intel_celeron_condition_is_correct(json_data):
    """Checks if the 'condition' is correctly set to 'new'."""
    assert json_data["scenarios"]["ASUS INTEL CELERON"]["condition"] == "new"


def test_scenario_asus_intel_celeron_presta_categories_is_dict(json_data):
  """Checks that presta categories is a dictionary"""
  assert isinstance(json_data["scenarios"]["ASUS INTEL CELERON"]["presta_categories"], dict)

def test_scenario_asus_intel_celeron_presta_categories_template_is_dict(json_data):
    """Checks if the 'template' inside 'presta_categories' is a dictionary."""
    assert isinstance(json_data["scenarios"]["ASUS INTEL CELERON"]["presta_categories"]["template"], dict)

def test_scenario_asus_intel_celeron_presta_categories_template_has_asus_key(json_data):
    """Checks if the 'template' has 'asus' key."""
    assert "asus" in json_data["scenarios"]["ASUS INTEL CELERON"]["presta_categories"]["template"]
    

def test_scenario_asus_intel_celeron_presta_categories_template_asus_value_is_correct(json_data):
    """Checks if the 'asus' key has the correct value in the 'template'."""
    assert json_data["scenarios"]["ASUS INTEL CELERON"]["presta_categories"]["template"]["asus"] == "LAPTOPS INTEL CELERON"

def test_scenario_asus_intel_celeron_checkbox_is_boolean(json_data):
    """Checks if the 'checkbox' value is a boolean."""
    assert isinstance(json_data["scenarios"]["ASUS INTEL CELERON"]["checkbox"], bool)
    
def test_scenario_asus_intel_celeron_price_rule_is_int(json_data):
    """Checks that the price_rule key is an integer"""
    assert isinstance(json_data["scenarios"]["ASUS INTEL CELERON"]["price_rule"], int)
```