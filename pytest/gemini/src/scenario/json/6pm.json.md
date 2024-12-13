```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data for testing."""
    with open('hypotez/src/scenario/json/6pm.json', 'r') as f:
        return json.load(f)

def test_supplier_name(json_data):
    """Verify the supplier name is correct."""
    assert json_data["supplier"] == "6pm", "Supplier name should be '6pm'"

def test_supplier_prefix(json_data):
    """Verify the supplier prefix is correct."""
    assert json_data["supplier_prefix"] == "6pm", "Supplier prefix should be '6pm'"

def test_start_url(json_data):
    """Verify the start URL is correct."""
    assert json_data["start_url"] == "https://www.6pm.com/", "Start URL is incorrect"

def test_price_rule(json_data):
    """Verify the price rule is correct."""
    assert json_data["price_rule"] == "+0", "Price rule should be '+0'"

def test_if_login_is_boolean(json_data):
     """Verify that the if_login is a boolean value"""
     assert isinstance(json_data["if_login"], bool), "if_login should be a boolean value"


def test_collect_products_from_categorypage_is_boolean(json_data):
    """Verify that collect_products_from_categorypage is a boolean value."""
    assert isinstance(json_data["collect_products_from_categorypage"], bool), "collect_products_from_categorypage should be a boolean value"

def test_root_category_is_integer(json_data):
    """Verify that root_category is an integer."""
    assert isinstance(json_data["root_category"], int), "root_category should be an integer"

def test_scenario_files_is_list(json_data):
    """Verify that scenario_files is a list."""
    assert isinstance(json_data["scenario_files"], list), "scenario_files should be a list"

def test_scenario_files_content(json_data):
    """Verify the contents of scenario_files list."""
    assert ".json" in json_data["scenario_files"] , "'.json' should be in the scenario_files list"
    assert "ksp_categories_wathces_apple.json" in json_data["scenario_files"], "'ksp_categories_wathces_apple.json' should be in the scenario_files list"

def test_excluded_is_list(json_data):
    """Verify that excluded is a list."""
    assert isinstance(json_data["excluded"], list), "excluded should be a list"

def test_excluded_content(json_data):
     """Verify that the excluded list contains specific strings."""
     expected_exclusions = [
        "ksp_categories_speakers_google.json",
        "ksp_categories_speakers_jbl.json",
        "ksp_categories_phones_philips.json",
        "ksp_categories_phones_samsung.json",
        "ksp_categories_phones_google.json",
        "ksp_categories_phones_asus.json",
        "ksp_categories_phones_nokia.json",
        "ksp_categories_phones_oppo.json",
        "ksp_categories_phones_oneplus.json",
        "ksp_categories_phones_philips.json",
        "ksp_categories_phones_xiaomi.json",
        "ksp_categories_headphones_bang_olufsen.json",
        "ksp_categories_headphones_hyperx.json",
        "ksp_categories_headphones_jbl.json",
        "ksp_categories_headphones_razer.json",
        "ksp_categories_headphones_sony.json",
        "ksp_categories_headphones_xiaomi.json",
        "ksp_categories_tablets_amazon.json",
        "ksp_categories_tablets_lenovo.json",
        "ksp_categories_tablets_samsung.json",
        "ksp_categories_tablets_xiaomi.json",
        "ksp_categories_iphones.json",
        "ksp_categories_macbook.json",
        "ksp_categories_apple_wathces.json",
        "ksp_categories_ipods.json",
        "ksp_categories_ipads.json",
        "ksp_categories_imacs.json",
        "ksp_categories_consoles_microsoft.json",
        "ksp_categories_consoles_nintendo.json",
        "ksp_categories_notebooks_asus_by_model.json",
        "ksp_categories_notebooks_lenovo_by_model.json",
        "ksp_categories_notebooks_hp_by_model.json",
        "ksp_categories_notebooks_dell_by_model.json",
        "ksp_categories_notebooks_huawei_by_model.json",
         "ksp_categories_speakers_google.json",
        "ksp_categories_speakers_jbl.json",
        "ksp_categories_watches_honor.json",
        "ksp_categories_watches_lenovo.json",
        "ksp_categories_watches_garmin.json",
        "ksp_categories_watches_samsung.json",
        "ksp_categories_watches_xiaomi.json",
         "ksp_categories_watches_amazfit.json",
        "ksp_categories_streamers_google.json",
        "ksp_categories_monitors_samsung.json",
        "ksp_categories_monitors_lg.json"
     ]

     for item in expected_exclusions:
        assert item in json_data["excluded"], f"'{item}' should be in the excluded list"


def test_last_runned_scenario_is_string(json_data):
    """Verify that last_runned_scenario is a string."""
    assert isinstance(json_data["last_runned_scenario"], str), "last_runned_scenario should be a string"


def test_last_runned_scenario_empty_string(json_data):
     """Verify that last_runned_scenario is an empty string"""
     assert json_data["last_runned_scenario"] == "", "last_runned_scenario should be an empty string"
```