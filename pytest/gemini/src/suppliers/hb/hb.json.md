```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def hb_data():
    """Provides the HB JSON data as a dictionary."""
    json_data = """
    {
      "supplier": "HB Dead Sea Cosmetics",
      "supplier_id": "11267",
      "supplier_prefix": "hb",
      "active_clients_list": [
        "emil-design.com",
        "e-cat.co.il"
      ],
      "start_url": "https://hbdeadsea.co.il/",
      "price_rule": "+0",
      "if_list":"first","use_mouse": false,
      "mandatory": "true",
      "if_login": false,
      "login_url": "",
      "lang": "HE",
      "id_category_default": 11246,
      "compare_categorie_dict": true,
      "collect_products_from_categorypage": false,
      "scenario_files": [
        "categories_20240503015900.json",
        "bodyspa.json",
        "soap-bar.json",
        "men-treatment.json",
        "health-products.json",
        "hair-treatment.json",
        "facial.json",
        "dead-sea-mud-products.json",
        "aromatherapy.json"
      ],
      "excluded": [],
       "last_runned_scenario": "feet-hand-treatment",
       "scenario_interrupted": "feet-hand-treatment",
       "last_runned_scenario_filename": "bodyspa.json",
       "just_runned_scenario_filename": "bodyspa.json",
       "interrupted_scenario": [
        "feet-hand-treatment"
      ]
    }
    """
    return json.loads(json_data)


def test_hb_data_supplier(hb_data):
    """Checks if the supplier name is correct."""
    assert hb_data["supplier"] == "HB Dead Sea Cosmetics"


def test_hb_data_supplier_id(hb_data):
    """Checks if the supplier ID is correct."""
    assert hb_data["supplier_id"] == "11267"


def test_hb_data_supplier_prefix(hb_data):
    """Checks if the supplier prefix is correct."""
    assert hb_data["supplier_prefix"] == "hb"


def test_hb_data_active_clients_list(hb_data):
    """Checks if the active clients list contains the correct items."""
    assert hb_data["active_clients_list"] == ["emil-design.com", "e-cat.co.il"]


def test_hb_data_start_url(hb_data):
    """Checks if the start URL is correct."""
    assert hb_data["start_url"] == "https://hbdeadsea.co.il/"


def test_hb_data_price_rule(hb_data):
    """Checks if the price rule is correct."""
    assert hb_data["price_rule"] == "+0"


def test_hb_data_if_list(hb_data):
    """Checks if the if_list value is correct"""
    assert hb_data["if_list"] == "first"


def test_hb_data_use_mouse(hb_data):
   """Checks if the use_mouse value is correct"""
   assert hb_data["use_mouse"] == False


def test_hb_data_mandatory(hb_data):
    """Checks if the mandatory value is correct."""
    assert hb_data["mandatory"] == "true"

def test_hb_data_if_login(hb_data):
    """Checks if the if_login value is correct."""
    assert hb_data["if_login"] == False

def test_hb_data_login_url(hb_data):
    """Checks if the login URL is correct."""
    assert hb_data["login_url"] == ""


def test_hb_data_lang(hb_data):
    """Checks if the language is correct."""
    assert hb_data["lang"] == "HE"


def test_hb_data_id_category_default(hb_data):
    """Checks if the default category ID is correct."""
    assert hb_data["id_category_default"] == 11246

def test_hb_data_compare_categorie_dict(hb_data):
    """Checks if the compare_categorie_dict is correct"""
    assert hb_data["compare_categorie_dict"] == True

def test_hb_data_collect_products_from_categorypage(hb_data):
    """Checks if collect products from category page is correct"""
    assert hb_data["collect_products_from_categorypage"] == False


def test_hb_data_scenario_files(hb_data):
    """Checks if the scenario files list contains the correct files."""
    expected_files = [
        "categories_20240503015900.json",
        "bodyspa.json",
        "soap-bar.json",
        "men-treatment.json",
        "health-products.json",
        "hair-treatment.json",
        "facial.json",
        "dead-sea-mud-products.json",
        "aromatherapy.json",
    ]
    assert hb_data["scenario_files"] == expected_files


def test_hb_data_excluded_empty(hb_data):
    """Checks if the excluded list is empty."""
    assert hb_data["excluded"] == []


def test_hb_data_last_runned_scenario(hb_data):
    """Checks the value of the last_runned_scenario"""
    assert hb_data["last_runned_scenario"] == "feet-hand-treatment"


def test_hb_data_scenario_interrupted(hb_data):
    """Checks the value of the scenario_interrupted"""
    assert hb_data["scenario_interrupted"] == "feet-hand-treatment"

def test_hb_data_last_runned_scenario_filename(hb_data):
    """Checks if the last runned scenario filename is correct"""
    assert hb_data["last_runned_scenario_filename"] == "bodyspa.json"


def test_hb_data_just_runned_scenario_filename(hb_data):
    """Checks if the just runned scenario filename is correct"""
    assert hb_data["just_runned_scenario_filename"] == "bodyspa.json"


def test_hb_data_interrupted_scenario(hb_data):
    """Checks if the interrupted scenario is correct"""
    assert hb_data["interrupted_scenario"] == ["feet-hand-treatment"]
```