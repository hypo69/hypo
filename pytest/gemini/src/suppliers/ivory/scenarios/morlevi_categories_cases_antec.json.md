```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def category_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
        "store": {
            "description": "Antec Computer Cases",
            "about": " ",
            "category ID on site": "",
            "category ID in PRESTAHOP db": "",
            "brand": [ "ANTEC" ],
            "url": "https://www.morlevi.co.il/Cat/95?p_315=12&sort=datafloat2%2Cprice&keyword=",
            "get store banners": true
        },
        "scenarios": {
            "ANTEC MID TOWER": {
              "brand": "ANTEC",
              "template": "",
              "url": "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=540&sort=datafloat2%2Cprice&keyword=",
              "checkbox": false,
              "active": true,
              "condition": "new",
              "presta_categories": {
                  "template": {
                      "antec": "MID TOWER"
                  }
              }
          },
          "ANTEC FULL TOWER": {
              "brand": "ANTEC",
              "url": "----------------------------ANTEC FULL TOWER--------------------------------",
              "checkbox": false,
              "active": true,
              "condition": "new",
              "presta_categories": {
                  "template": { "antec": "FULL TOWER" }
              }
          },
          "ANTEC MINI TOWER": {
            "brand": "ANTEC",
            "template": "",
            "url": "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=542&sort=datafloat2%2Cprice&keyword=",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": {
              "template": { "antec": "MINI TOWER" }
            }
          },
          "ANTEC gaming MID TOWER": {
              "brand": "ANTEC",
              "template": "",
              "url": "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=545&sort=datafloat2%2Cprice&keyword=",
              "checkbox": false,
              "active": true,
              "condition": "new",
              "presta_categories": {
                  "template": { "antec": "MINI TOWER" }
              }
          },
          "ANTEC gaming full tower": {
              "brand": "ANTEC",
              "template": "",
              "url": "----------------------------ANTEC gaming full TOWER--------------------------------",
              "checkbox": false,
              "active": true,
              "condition": "new",
              "presta_categories": {
                  "template": { "antec": "MINI TOWER" }
              }
          },
          "ANTEC mini itx": {
              "brand": "ANTEC",
              "template": "",
              "url": "----------------------------ANTEC mini itxR--------------------------------",
              "checkbox": false,
              "active": true,
              "condition": "new",
              "presta_categories": {
                  "template": { "antec": "MINI ITX" }
              }
          }
        }
    }
    """
    return json.loads(json_data)


# Tests for 'store' section
def test_store_description(category_data):
    """Checks the store description is correct."""
    assert category_data['store']['description'] == "Antec Computer Cases"

def test_store_brand(category_data):
    """Checks the store brand is correct."""
    assert category_data['store']['brand'] == ["ANTEC"]

def test_store_url(category_data):
     """Checks the store url is correct."""
     assert category_data['store']['url'] == "https://www.morlevi.co.il/Cat/95?p_315=12&sort=datafloat2%2Cprice&keyword="

def test_store_get_banners(category_data):
    """Checks the 'get store banners' flag is true."""
    assert category_data['store']['get store banners'] == True

# Tests for 'scenarios' section
def test_scenarios_count(category_data):
    """Checks the number of scenarios loaded."""
    assert len(category_data['scenarios']) == 6

def test_scenario_mid_tower(category_data):
     """Checks data of 'ANTEC MID TOWER' scenario"""
     mid_tower = category_data['scenarios']['ANTEC MID TOWER']
     assert mid_tower['brand'] == "ANTEC"
     assert mid_tower['url'] == "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=540&sort=datafloat2%2Cprice&keyword="
     assert mid_tower['checkbox'] == False
     assert mid_tower['active'] == True
     assert mid_tower['condition'] == 'new'
     assert mid_tower['presta_categories']['template']['antec'] == 'MID TOWER'


def test_scenario_full_tower(category_data):
     """Checks data of 'ANTEC FULL TOWER' scenario"""
     full_tower = category_data['scenarios']['ANTEC FULL TOWER']
     assert full_tower['brand'] == "ANTEC"
     assert full_tower['url'] == "----------------------------ANTEC FULL TOWER--------------------------------"
     assert full_tower['checkbox'] == False
     assert full_tower['active'] == True
     assert full_tower['condition'] == 'new'
     assert full_tower['presta_categories']['template']['antec'] == 'FULL TOWER'

def test_scenario_mini_tower(category_data):
     """Checks data of 'ANTEC MINI TOWER' scenario"""
     mini_tower = category_data['scenarios']['ANTEC MINI TOWER']
     assert mini_tower['brand'] == "ANTEC"
     assert mini_tower['url'] == "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=542&sort=datafloat2%2Cprice&keyword="
     assert mini_tower['checkbox'] == False
     assert mini_tower['active'] == True
     assert mini_tower['condition'] == 'new'
     assert mini_tower['presta_categories']['template']['antec'] == 'MINI TOWER'

def test_scenario_gaming_mid_tower(category_data):
    """Checks data of 'ANTEC gaming MID TOWER' scenario"""
    gaming_mid_tower = category_data['scenarios']['ANTEC gaming MID TOWER']
    assert gaming_mid_tower['brand'] == "ANTEC"
    assert gaming_mid_tower['url'] == "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=545&sort=datafloat2%2Cprice&keyword="
    assert gaming_mid_tower['checkbox'] == False
    assert gaming_mid_tower['active'] == True
    assert gaming_mid_tower['condition'] == 'new'
    assert gaming_mid_tower['presta_categories']['template']['antec'] == 'MINI TOWER'

def test_scenario_gaming_full_tower(category_data):
    """Checks data of 'ANTEC gaming full tower' scenario"""
    gaming_full_tower = category_data['scenarios']['ANTEC gaming full tower']
    assert gaming_full_tower['brand'] == "ANTEC"
    assert gaming_full_tower['url'] == "----------------------------ANTEC gaming full TOWER--------------------------------"
    assert gaming_full_tower['checkbox'] == False
    assert gaming_full_tower['active'] == True
    assert gaming_full_tower['condition'] == 'new'
    assert gaming_full_tower['presta_categories']['template']['antec'] == 'MINI TOWER'

def test_scenario_mini_itx(category_data):
    """Checks data of 'ANTEC mini itx' scenario"""
    mini_itx = category_data['scenarios']['ANTEC mini itx']
    assert mini_itx['brand'] == "ANTEC"
    assert mini_itx['url'] == "----------------------------ANTEC mini itxR--------------------------------"
    assert mini_itx['checkbox'] == False
    assert mini_itx['active'] == True
    assert mini_itx['condition'] == 'new'
    assert mini_itx['presta_categories']['template']['antec'] == 'MINI ITX'
```