```python
import pytest
import json

# Fixture to load the json data
@pytest.fixture
def mpdigest_data():
    """Loads the mpdigest json data from the file."""
    with open("hypotez/src/scenario/json/mpdigest.json", "r") as f:
        return json.load(f)

def test_mpdigest_supplier(mpdigest_data):
    """Checks if the supplier field is correct."""
    assert mpdigest_data["supplier"] == "mpdigest"

def test_mpdigest_supplier_prefix(mpdigest_data):
    """Checks if the supplier_prefix field is correct."""
    assert mpdigest_data["supplier_prefix"] == "mpdigest"

def test_mpdigest_start_url(mpdigest_data):
    """Checks if the start_url field is correct."""
    assert mpdigest_data["start_url"] == "https://www.mpdigest.com/category/on-the-market/"

def test_mpdigest_price_rule(mpdigest_data):
    """Checks if the price_rule field is correct."""
    assert mpdigest_data["price_rule"] == "+0"

def test_mpdigest_if_login(mpdigest_data):
    """Checks if the if_login field is correct."""
    assert mpdigest_data["if_login"] is False

def test_mpdigest_login_url(mpdigest_data):
    """Checks if the login_url field is an empty string."""
    assert mpdigest_data["login_url"] == ""

def test_mpdigest_root_category(mpdigest_data):
    """Checks if the root_category field is correct."""
    assert mpdigest_data["root_category"] == 3

def test_mpdigest_collect_products_from_categorypage(mpdigest_data):
    """Checks if the collect_products_from_categorypage field is correct."""
    assert mpdigest_data["collect_products_from_categorypage"] is False

def test_mpdigest_aliexpres_ajax_store(mpdigest_data):
    """Checks if the aliexpres_ajax_store field is correct."""
    assert mpdigest_data["aliexpres_ajax_store"] == "https://he.aliexpress.com/store/productGroupsAjax.htm?storeId="

def test_mpdigest_catalog_wholesale_products_not_empty(mpdigest_data):
    """Checks if the catalog_wholesale-products dictionary is not empty."""
    assert mpdigest_data["catalog_wholesale-products"]

def test_mpdigest_catalog_wholesale_products_keys(mpdigest_data):
    """Checks if the keys of catalog_wholesale-products are correct."""
    expected_keys = ["ALL NOT SORTED", "HE", "RU", "EN", "FR"]
    actual_keys = list(mpdigest_data["catalog_wholesale-products"].keys())
    assert set(actual_keys) == set(expected_keys)
    

def test_mpdigest_catalog_wholesale_products_url_format(mpdigest_data):
    """Checks if the URL's in catalog_wholesale-products are not empty."""
    for url in mpdigest_data["catalog_wholesale-products"].values():
         assert url, "URL must not be empty"

def test_mpdigest_scenario_files_not_empty(mpdigest_data):
    """Checks if the scenario_files list is not empty."""
    assert mpdigest_data["scenario_files"]

def test_mpdigest_scenario_files_correct_content(mpdigest_data):
    """Checks if scenario_files list has the correct names."""
    expected_files = ["aliexpress_stores_elctronic_toys.json", "aliexpress_stores_baby_clothing.json"]
    assert set(mpdigest_data["scenario_files"]) == set(expected_files)

def test_mpdigest_excluded_not_empty(mpdigest_data):
    """Checks if the excluded list is not empty."""
    assert mpdigest_data["excluded"]

def test_mpdigest_excluded_correct_content(mpdigest_data):
    """Checks if excluded list has the correct filenames."""
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
    assert set(mpdigest_data["excluded"]) == set(expected_files)

def test_mpdigest_keys_exist(mpdigest_data):
    """Checks if all expected keys are present in the dictionary."""
    expected_keys = [
        "supplier",
        "supplier_prefix",
        "start_url",
        "price_rule",
        "if_login",
        "login_url",
        "root_category",
        "collect_products_from_categorypage",
        "aliexpres_ajax_store",
        "catalog_wholesale-products",
        "scenario_files",
        "excluded"
    ]
    assert set(mpdigest_data.keys()) == set(expected_keys)
```