```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the json data for tests."""
    json_string = """
    {
      "supplier": "6comgiga",
      "supplier_prefix": "6comgiga",
      "start_url": "https://www.6comgiga.com/",
      "wholesale_products_url": "",
      "price_rule": "+0",
      "num_items_4_flush": 300,
      "if_login": true,
      "login_url": "",
      "root_category": 3,
      "collect_products_from_categorypage": false,
      "aliexpres_ajax_store": "https://he.aliexpress.com/store/productGroupsAjax.htm?storeId=",
      "catalog_wholesale-products": {
        "ALL NOT SORTED": "https://www.aliexpress.com/wholesale.html?spm=a2g0o.11810135.0.0.61b4IPjRIPjR75",
        "HE": "https://www.he.aliexpress.com/shop categories page.html",
        "RU": "https://www.aliexpress.com/shop categories page.html",
        "EN": "https://www.aliexpress.com/shop categories page.html",
        "FR": "https://fr.aliexpress.com/shop categories page.html"
      },
      "scenario_files": [
    
        "aliexpress_stores_elctronic_toys.json",
        "aliexpress_stores_baby_clothing.json"
    
      ],
      "excluded": [
    
        "aliexpress_stores_battery.json",
        "aliexpress_stores_brands.json",
        "aliexpress_stores_computer_components.json",
        "aliexpress_stores_computer_components_fans.json",
        "aliexpress_stores_computers.json",
        "aliexpress_stores_electronics.json",
        "aliexpress_stores_elctronic_components_audio.json",
        "aliexpress_stores_elctronic_components_leds.json",
        "aliexpress_stores_elctronic_toys.json",
        "aliexpress_stores_lighting.json",
        "aliexpress_stores_leds.json",
        "aliexpress_stores_malls.json",
        "aliexpress_stores_memory.json",
        "aliexpress_stores_phones_repair_computers.json"
      ]
    }
    """
    return json.loads(json_string)

def test_supplier_name(json_data):
    """Check if supplier name is correct"""
    assert json_data["supplier"] == "6comgiga"

def test_supplier_prefix(json_data):
     """Check if supplier prefix is correct"""
     assert json_data["supplier_prefix"] == "6comgiga"

def test_start_url(json_data):
     """Check if start_url is correct"""
     assert json_data["start_url"] == "https://www.6comgiga.com/"

def test_wholesale_products_url(json_data):
    """Check if wholesale_products_url is an empty string"""
    assert json_data["wholesale_products_url"] == ""

def test_price_rule(json_data):
     """Check if price rule is correct"""
     assert json_data["price_rule"] == "+0"

def test_num_items_4_flush(json_data):
    """Check if num_items_4_flush is correct"""
    assert json_data["num_items_4_flush"] == 300

def test_if_login(json_data):
    """Check if if_login is correct"""
    assert json_data["if_login"] == True

def test_login_url(json_data):
     """Check if login_url is an empty string"""
     assert json_data["login_url"] == ""

def test_root_category(json_data):
     """Check if root_category is correct"""
     assert json_data["root_category"] == 3

def test_collect_products_from_categorypage(json_data):
    """Check if collect_products_from_categorypage is correct"""
    assert json_data["collect_products_from_categorypage"] == False

def test_aliexpres_ajax_store(json_data):
     """Check if aliexpres_ajax_store url is correct"""
     assert json_data["aliexpres_ajax_store"] == "https://he.aliexpress.com/store/productGroupsAjax.htm?storeId="

def test_catalog_wholesale_products(json_data):
    """Check if catalog_wholesale-products contains expected keys and urls"""
    catalog = json_data["catalog_wholesale-products"]
    assert "ALL NOT SORTED" in catalog
    assert catalog["ALL NOT SORTED"] == "https://www.aliexpress.com/wholesale.html?spm=a2g0o.11810135.0.0.61b4IPjRIPjR75"
    assert "HE" in catalog
    assert catalog["HE"] == "https://www.he.aliexpress.com/shop categories page.html"
    assert "RU" in catalog
    assert catalog["RU"] == "https://www.aliexpress.com/shop categories page.html"
    assert "EN" in catalog
    assert catalog["EN"] == "https://www.aliexpress.com/shop categories page.html"
    assert "FR" in catalog
    assert catalog["FR"] == "https://fr.aliexpress.com/shop categories page.html"

def test_scenario_files(json_data):
    """Check if scenario_files contains the expected files"""
    scenario_files = json_data["scenario_files"]
    assert "aliexpress_stores_elctronic_toys.json" in scenario_files
    assert "aliexpress_stores_baby_clothing.json" in scenario_files

def test_excluded_files(json_data):
     """Check if excluded contains the expected files"""
     excluded = json_data["excluded"]
     assert "aliexpress_stores_battery.json" in excluded
     assert "aliexpress_stores_brands.json" in excluded
     assert "aliexpress_stores_computer_components.json" in excluded
     assert "aliexpress_stores_computer_components_fans.json" in excluded
     assert "aliexpress_stores_computers.json" in excluded
     assert "aliexpress_stores_electronics.json" in excluded
     assert "aliexpress_stores_elctronic_components_audio.json" in excluded
     assert "aliexpress_stores_elctronic_components_leds.json" in excluded
     assert "aliexpress_stores_elctronic_toys.json" in excluded
     assert "aliexpress_stores_lighting.json" in excluded
     assert "aliexpress_stores_leds.json" in excluded
     assert "aliexpress_stores_malls.json" in excluded
     assert "aliexpress_stores_memory.json" in excluded
     assert "aliexpress_stores_phones_repair_computers.json" in excluded
```