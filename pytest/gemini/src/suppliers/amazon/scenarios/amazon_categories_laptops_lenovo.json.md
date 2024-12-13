```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_data():
    """Loads the amazon_categories_laptops_lenovo.json data."""
    json_data = """
    {
      "store": {
        "store_id": "",
        "supplier_id": "",
        "get store banners": true,
        "description": "Lenovo laptops",
        "about": "Lenovo laptops",
        "brand": "LENOVO",
        "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ALenovo&dc&qid=1671858970&rnid=23716050011&ref=sr_nr_p_n_feature_thirty-one_browse-bin_1&ds=v1%3AEaENIiWwifDcRT6qTB%2FxEy6WSOBD%2FsskOooUf%2FcAiGU",
        "shop categories page": "",
        "shop categories json file": ""
      },
      "scenarios": {
        "LAPTOP LENOVO AMD ATHLON 13": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_feature_thirty-one_browse-bin%3A23716057011%2Cp_89%3ALenovo%2Cp_n_feature_four_browse-bin%3A1264728011%2Cp_n_size_browse-bin%3A3545275011&dc&qid=1674228094&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_2&ds=v1%3AM9nKGPOL2sEa75Wq%2BN5ibb4AA3CUqLERK%2Fewcx2E9G4",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": [ "LAPTOPS AMD ATHLON", "13" ] }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO AMD RYZEN 3": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_feature_thirty-one_browse-bin%3A23716057011%2Cp_89%3ALenovo%2Cp_n_feature_four_browse-bin%3A18107800011&dc&qid=1671868229&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_5&ds=v1%3APd9r%2Fmu4LFPmQbVNx4r38WEVf4oLyDiRsUPRsmJcD2c",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS AMD RYZEN 3" }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO AMD RYZEN 5": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_feature_thirty-one_browse-bin%3A23716057011%2Cp_89%3ALenovo%2Cp_n_feature_four_browse-bin%3A18107801011&dc&qid=1671868297&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_4&ds=v1%3AlnkmPjF9iXbEQyTFM60xjpdQyxVlPXztK%2Ba8hC1mcIc",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS AMD RYZEN 5" }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO AMD RYZEN 7": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_feature_thirty-one_browse-bin%3A23716057011%2Cp_89%3ALenovo%2Cp_n_feature_four_browse-bin%3A18107802011&dc&qid=1671868349&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_2&ds=v1%3AhRAIfmofpDxVwkRtHe9ZtUjE9xlCWsDuviZiGkvZQjU",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS AMD RYZEN 7" }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO INTEL CELERON": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ALenovo%2Cp_n_feature_thirty-one_browse-bin%3A23716064011%2Cp_n_feature_four_browse-bin%3A1264420011%7C1264444011&dc&qid=1671868462&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_5&ds=v1%3A%2FLFFAD%2BLJLPifEWn4EG%2BXh0xcKkn1anXkeKvpTccRy0",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS INTEL CELERON" }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO INTEL I3": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AMSI%2Cp_n_feature_thirty-one_browse-bin%3A23716057011&dc&qid=1671862901&rnid=23716050011&ref=sr_nr_p_n_feature_thirty-one_browse-bin_1&ds=v1%3AmNxTrMVph6qi00BPhcatDzt6qglhtOwAfrSEzdNZFx8",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS INTEL I3" }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO INTEL I5": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ALenovo%2Cp_n_feature_thirty-one_browse-bin%3A23716064011%2Cp_n_feature_four_browse-bin%3A2289793011&dc&qid=1671868668&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_3&ds=v1%3AkuiODIZhNBStringFormatterpVEO8vCPV2tbjwZH7cAchGSYomaTf6Q",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS INTEL I5" }
          },
          "checkbox": false,
          "price_rule": 1
        },
        "LAPTOP LENOVO INTEL I7": {
          "brand": "LENOVO",
          "url": "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ALenovo%2Cp_n_feature_thirty-one_browse-bin%3A23716064011%2Cp_n_feature_four_browse-bin%3A2289792011&dc&qid=1671868737&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_1&ds=v1%3ADRHV6fhy%2BTHCiVwGbO%2B5iq0cQ8DJY3BFdJt1YASEDqE",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "lenovo": "LAPTOPS INTEL I7" }
          },
          "checkbox": false,
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the 'store' section
def test_store_data_exists(amazon_data):
    """Verify the 'store' section exists in the data."""
    assert "store" in amazon_data, "The 'store' section should exist in the data"

def test_store_fields_not_empty(amazon_data):
  """Verify that store fields are not empty except store_id and supplier_id."""
  store_data = amazon_data.get("store")
  assert store_data.get("get store banners") == True
  assert store_data.get("description") == "Lenovo laptops"
  assert store_data.get("about") == "Lenovo laptops"
  assert store_data.get("brand") == "LENOVO"
  assert store_data.get("url") == "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3ALenovo&dc&qid=1671858970&rnid=23716050011&ref=sr_nr_p_n_feature_thirty-one_browse-bin_1&ds=v1%3AEaENIiWwifDcRT6qTB%2FxEy6WSOBD%2FsskOooUf%2FcAiGU"
  assert store_data.get("shop categories page") == ""
  assert store_data.get("shop categories json file") == ""

def test_store_id_and_supplier_id_empty(amazon_data):
  """Verify the store_id and supplier_id are empty."""
  store_data = amazon_data.get("store")
  assert store_data.get("store_id") == ""
  assert store_data.get("supplier_id") == ""

# Test cases for the 'scenarios' section
def test_scenarios_data_exists(amazon_data):
    """Verify the 'scenarios' section exists in the data."""
    assert "scenarios" in amazon_data, "The 'scenarios' section should exist in the data"

def test_scenarios_not_empty(amazon_data):
    """Verify that the 'scenarios' section is not empty."""
    assert amazon_data["scenarios"], "The 'scenarios' section should not be empty"

def test_scenario_keys_exist(amazon_data):
    """Verify that each scenario has the required keys."""
    for scenario_name, scenario_data in amazon_data["scenarios"].items():
      assert "brand" in scenario_data
      assert "url" in scenario_data
      assert "active" in scenario_data
      assert "condition" in scenario_data
      assert "presta_categories" in scenario_data
      assert "checkbox" in scenario_data
      assert "price_rule" in scenario_data
      

def test_scenario_brand_is_lenovo(amazon_data):
    """Verify that the brand is 'LENOVO' in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
        assert scenario_data["brand"] == "LENOVO"

def test_scenario_url_is_valid(amazon_data):
    """Verify that the URL is a string and not empty in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
      assert isinstance(scenario_data["url"], str)
      assert scenario_data["url"] != ""

def test_scenario_active_is_boolean(amazon_data):
    """Verify that the active field is a boolean in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
        assert isinstance(scenario_data["active"], bool)

def test_scenario_condition_is_new(amazon_data):
    """Verify that the condition field is 'new' in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
        assert scenario_data["condition"] == "new"

def test_scenario_presta_categories_is_dict(amazon_data):
    """Verify that the presta_categories field is a dict in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
        assert isinstance(scenario_data["presta_categories"], dict)
        assert "template" in scenario_data["presta_categories"]

def test_scenario_checkbox_is_false(amazon_data):
    """Verify that the checkbox field is false in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
        assert scenario_data["checkbox"] == False

def test_scenario_price_rule_is_1(amazon_data):
    """Verify that the price_rule field is 1 in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
        assert scenario_data["price_rule"] == 1

def test_scenario_presta_categories_template_is_not_empty(amazon_data):
    """Verify the 'template' field in 'presta_categories' is not empty in all scenarios."""
    for scenario_data in amazon_data["scenarios"].values():
      assert scenario_data["presta_categories"]["template"], "The 'template' field should not be empty"
```