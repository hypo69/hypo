```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Loads the JSON data from the file."""
    with open('hypotez/src/scenario/json/controldcs.json', 'r') as f:
        return json.load(f)

def test_supplier_is_controldcs(json_data):
    """Checks if the supplier is correctly set to 'controldcs'."""
    assert json_data["supplier"] == "controldcs"

def test_supplier_prefix_is_controldcs(json_data):
    """Checks if the supplier prefix is correctly set to 'controldcs'."""
    assert json_data["supplier_prefix"] == "controldcs"

def test_start_url_is_correct(json_data):
    """Checks if the start URL is correctly set."""
    assert json_data["start_url"] == "https://www.controldcs.com/"

def test_wholesale_products_url_is_empty(json_data):
    """Checks if the wholesale products URL is empty."""
    assert json_data["wholesale_products_url"] == ""

def test_price_rule_is_plus_zero(json_data):
    """Checks if the price rule is correctly set to '+0'."""
    assert json_data["price_rule"] == "+0"

def test_num_items_4_flush_is_300(json_data):
     """Checks if the number of items for flush is correctly set to 300."""
     assert json_data["num_items_4_flush"] == 300

def test_if_login_is_true(json_data):
    """Checks if the login flag is set to True."""
    assert json_data["if_login"] is True

def test_login_url_is_empty(json_data):
    """Checks if the login URL is empty."""
    assert json_data["login_url"] == ""

def test_root_category_is_3(json_data):
    """Checks if the root category is set to 3."""
    assert json_data["root_category"] == 3

def test_collect_products_from_categorypage_is_false(json_data):
     """Checks if collect_products_from_categorypage is False."""
     assert json_data["collect_products_from_categorypage"] is False


def test_aliexpres_ajax_store_is_correct(json_data):
    """Checks if the AliExpress AJAX store URL is correct."""
    assert json_data["aliexpres_ajax_store"] == "https://he.aliexpress.com/store/productGroupsAjax.htm?storeId="

def test_catalog_wholesale_products_is_dict(json_data):
    """Checks if catalog_wholesale-products is a dictionary."""
    assert isinstance(json_data["catalog_wholesale-products"], dict)

def test_catalog_wholesale_products_has_correct_keys(json_data):
    """Checks if catalog_wholesale-products has the correct keys."""
    expected_keys = ["ALL NOT SORTED", "HE", "RU", "EN", "FR"]
    assert set(json_data["catalog_wholesale-products"].keys()) == set(expected_keys)

def test_catalog_wholesale_products_urls_not_empty(json_data):
    """Checks if URLs in catalog_wholesale-products are not empty."""
    for url in json_data["catalog_wholesale-products"].values():
        assert url != ""

def test_scenario_files_is_list(json_data):
    """Checks if scenario_files is a list."""
    assert isinstance(json_data["scenario_files"], list)

def test_scenario_files_not_empty(json_data):
    """Checks if scenario_files is not empty."""
    assert len(json_data["scenario_files"]) > 0

def test_scenario_files_contains_expected_files(json_data):
    """Checks if scenario_files contains the expected file names."""
    expected_files = [
        "aliexpress_stores_elctronic_toys.json",
        "aliexpress_stores_baby_clothing.json"
    ]
    assert set(json_data["scenario_files"]) == set(expected_files)

def test_excluded_is_list(json_data):
    """Checks if excluded is a list."""
    assert isinstance(json_data["excluded"], list)

def test_excluded_not_empty(json_data):
    """Checks if excluded is not empty."""
    assert len(json_data["excluded"]) > 0
def test_excluded_contains_expected_files(json_data):
    """Checks if excluded contains the expected file names."""
    expected_files = [
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
    assert set(json_data["excluded"]) == set(expected_files)

def test_data_types(json_data):
    """Checks the data types of the values in the JSON."""
    assert isinstance(json_data["supplier"], str)
    assert isinstance(json_data["supplier_prefix"], str)
    assert isinstance(json_data["start_url"], str)
    assert isinstance(json_data["wholesale_products_url"], str)
    assert isinstance(json_data["price_rule"], str)
    assert isinstance(json_data["num_items_4_flush"], int)
    assert isinstance(json_data["if_login"], bool)
    assert isinstance(json_data["login_url"], str)
    assert isinstance(json_data["root_category"], int)
    assert isinstance(json_data["collect_products_from_categorypage"], bool)
    assert isinstance(json_data["aliexpres_ajax_store"], str)
    assert isinstance(json_data["catalog_wholesale-products"], dict)
    assert isinstance(json_data["scenario_files"], list)
    assert isinstance(json_data["excluded"], list)
```