```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_data():
    """Provides the JSON data for testing."""
    json_data = """
    {
      "store": {
        "store_id": "",
        "supplier_id": "",
        "get store banners": true,
        "description": "Macbook",
        "about": "Macbook ref",
        "brand": "APPLE",
        "url": "https://www.amazon.com/s?i=electronics&srs=12653393011&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AApple%2Cp_n_is_free_shipping%3A10236242011&dc&pf_rd_i=12653393011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=b8a4c9d3-e3d7-411d-a419-b400f6bb46e9&pf_rd_r=MZPGZ034JG9B0AX9YQF5&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1671327805&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_1&ds=v1%3AF7lIrJ0HgTBi42gOmuuro8RDqAov9wpPBhEYXkDVaDo",
        "shop categories page": "",
        "shop categories json file": ""
      },
    
      "scenarios": {
        "Macbook 13 I5": {
          "brand": "APPLE",
          "url": "https://www.amazon.com/s?i=electronics&srs=12653393011&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AApple%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_feature_four_browse-bin%3A2289793011%2Cp_n_size_browse-bin%3A3545275011&dc&pf_rd_i=12653393011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=b8a4c9d3-e3d7-411d-a419-b400f6bb46e9&pf_rd_r=MZPGZ034JG9B0AX9YQF5&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1671327860&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_1&ds=v1%3Ao8GTzhDT5NvBCv4bAgAny0KIaO1aWnu%2F4Hv7PV2JWeE",
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "apple": [ "MACBOOK 13 I5", "13" ] }
          },
          "checkbox": false,
    
          "price_rule": 1
        },
        "Macbook 13 I7": {
          "brand": "APPLE",
          "url": "https://www.amazon.com/s?i=electronics&srs=12653393011&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AApple%2Cp_n_is_free_shipping%3A10236242011%2Cp_n_feature_four_browse-bin%3A2289793011%2Cp_n_size_browse-bin%3A3545275011&dc&pf_rd_i=12653393011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=b8a4c9d3-e3d7-411d-a419-b400f6bb46e9&pf_rd_r=MZPGZ034JG9B0AX9YQF5&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1671327860&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_1&ds=v1%3Ao8GTzhDT5NvBCv4bAgAny0KIaO1aWnu%2F4Hv7PV2JWeE",
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": {
              "apple": ["MACBOOK 13 I7",
              "13" ]
            }
          },
          "checkbox": false,
          "price_rule": 1
        }
    
      }
    }
    """
    return json.loads(json_data)

def test_store_data_present(amazon_data):
    """Verify if store data is present and has the expected keys."""
    assert "store" in amazon_data
    assert "store_id" in amazon_data["store"]
    assert "supplier_id" in amazon_data["store"]
    assert "get store banners" in amazon_data["store"]
    assert "description" in amazon_data["store"]
    assert "about" in amazon_data["store"]
    assert "brand" in amazon_data["store"]
    assert "url" in amazon_data["store"]
    assert "shop categories page" in amazon_data["store"]
    assert "shop categories json file" in amazon_data["store"]

def test_store_data_types(amazon_data):
    """Verify the data types of the store data values."""
    assert isinstance(amazon_data["store"]["store_id"], str)
    assert isinstance(amazon_data["store"]["supplier_id"], str)
    assert isinstance(amazon_data["store"]["get store banners"], bool)
    assert isinstance(amazon_data["store"]["description"], str)
    assert isinstance(amazon_data["store"]["about"], str)
    assert isinstance(amazon_data["store"]["brand"], str)
    assert isinstance(amazon_data["store"]["url"], str)
    assert isinstance(amazon_data["store"]["shop categories page"], str)
    assert isinstance(amazon_data["store"]["shop categories json file"], str)

def test_scenarios_data_present(amazon_data):
    """Verify if scenarios data is present and has the expected keys."""
    assert "scenarios" in amazon_data
    assert "Macbook 13 I5" in amazon_data["scenarios"]
    assert "Macbook 13 I7" in amazon_data["scenarios"]

def test_scenario_macbook_13_i5_data(amazon_data):
    """Verify the data within the 'Macbook 13 I5' scenario."""
    macbook_i5_data = amazon_data["scenarios"]["Macbook 13 I5"]
    assert "brand" in macbook_i5_data
    assert "url" in macbook_i5_data
    assert "active" in macbook_i5_data
    assert "condition" in macbook_i5_data
    assert "presta_categories" in macbook_i5_data
    assert "checkbox" in macbook_i5_data
    assert "price_rule" in macbook_i5_data

def test_scenario_macbook_13_i5_data_types(amazon_data):
    """Verify the data types of the values in 'Macbook 13 I5' scenario."""
    macbook_i5_data = amazon_data["scenarios"]["Macbook 13 I5"]
    assert isinstance(macbook_i5_data["brand"], str)
    assert isinstance(macbook_i5_data["url"], str)
    assert isinstance(macbook_i5_data["active"], bool)
    assert isinstance(macbook_i5_data["condition"], str)
    assert isinstance(macbook_i5_data["presta_categories"], dict)
    assert isinstance(macbook_i5_data["checkbox"], bool)
    assert isinstance(macbook_i5_data["price_rule"], int)

def test_scenario_macbook_13_i7_data(amazon_data):
     """Verify the data within the 'Macbook 13 I7' scenario."""
     macbook_i7_data = amazon_data["scenarios"]["Macbook 13 I7"]
     assert "brand" in macbook_i7_data
     assert "url" in macbook_i7_data
     assert "active" in macbook_i7_data
     assert "condition" in macbook_i7_data
     assert "presta_categories" in macbook_i7_data
     assert "checkbox" in macbook_i7_data
     assert "price_rule" in macbook_i7_data

def test_scenario_macbook_13_i7_data_types(amazon_data):
    """Verify the data types of the values in 'Macbook 13 I7' scenario."""
    macbook_i7_data = amazon_data["scenarios"]["Macbook 13 I7"]
    assert isinstance(macbook_i7_data["brand"], str)
    assert isinstance(macbook_i7_data["url"], str)
    assert isinstance(macbook_i7_data["active"], bool)
    assert isinstance(macbook_i7_data["condition"], str)
    assert isinstance(macbook_i7_data["presta_categories"], dict)
    assert isinstance(macbook_i7_data["checkbox"], bool)
    assert isinstance(macbook_i7_data["price_rule"], int)
    
def test_presta_categories_template_i5(amazon_data):
    """Verify the structure of the 'presta_categories' in the 'Macbook 13 I5' scenario."""
    presta_categories_i5 = amazon_data["scenarios"]["Macbook 13 I5"]["presta_categories"]
    assert "template" in presta_categories_i5
    assert "apple" in presta_categories_i5["template"]
    assert isinstance(presta_categories_i5["template"]["apple"], list)
    assert len(presta_categories_i5["template"]["apple"]) == 2
    assert presta_categories_i5["template"]["apple"][0] == "MACBOOK 13 I5"
    assert presta_categories_i5["template"]["apple"][1] == "13"

def test_presta_categories_template_i7(amazon_data):
    """Verify the structure of the 'presta_categories' in the 'Macbook 13 I7' scenario."""
    presta_categories_i7 = amazon_data["scenarios"]["Macbook 13 I7"]["presta_categories"]
    assert "template" in presta_categories_i7
    assert "apple" in presta_categories_i7["template"]
    assert isinstance(presta_categories_i7["template"]["apple"], list)
    assert len(presta_categories_i7["template"]["apple"]) == 2
    assert presta_categories_i7["template"]["apple"][0] == "MACBOOK 13 I7"
    assert presta_categories_i7["template"]["apple"][1] == "13"
```