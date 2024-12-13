```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def elecrow_data():
    """Provides the elecrow JSON data as a dictionary."""
    json_data = """
    {
      "supplier": "elecrow",
      "supplier_prefix": "elecrow",
      "start_url": "https://www.elecrow.com/",
      "price_rule": "+0",
      "if_login": false,
      "collect_products_from_categorypage": false,
      "root_category": 3,
      "scenario_files": [
        ".json",
        "ksp_categories_wathces_apple.json"
      ],
      "excluded": [
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
      ],
      "last_runned_scenario": ""
    }
    """
    return json.loads(json_data)

def test_supplier_name(elecrow_data):
    """Checks if the supplier name is correct."""
    assert elecrow_data["supplier"] == "elecrow"

def test_supplier_prefix(elecrow_data):
    """Checks if the supplier prefix is correct."""
    assert elecrow_data["supplier_prefix"] == "elecrow"

def test_start_url(elecrow_data):
    """Checks if the start URL is correct."""
    assert elecrow_data["start_url"] == "https://www.elecrow.com/"

def test_price_rule(elecrow_data):
    """Checks if the price rule is correct."""
    assert elecrow_data["price_rule"] == "+0"

def test_if_login_is_false(elecrow_data):
    """Checks if the if_login is set to false."""
    assert elecrow_data["if_login"] == False

def test_collect_products_from_categorypage_is_false(elecrow_data):
    """Checks if collect_products_from_categorypage is set to false."""
    assert elecrow_data["collect_products_from_categorypage"] == False
    
def test_root_category_is_integer(elecrow_data):
    """Checks if the root_category is an integer."""
    assert isinstance(elecrow_data["root_category"], int)
    
def test_root_category_value(elecrow_data):
    """Checks if the root category is correct."""
    assert elecrow_data["root_category"] == 3
    
def test_scenario_files_is_list(elecrow_data):
    """Checks if scenario_files is a list."""
    assert isinstance(elecrow_data["scenario_files"], list)
    
def test_scenario_files_not_empty(elecrow_data):
    """Checks if scenario_files is not empty."""
    assert len(elecrow_data["scenario_files"]) > 0

def test_scenario_files_has_json_extension(elecrow_data):
    """Checks if the scenario files are strings with .json or are .json."""
    for file in elecrow_data["scenario_files"]:
         assert isinstance(file, str)
         if file != ".json":
            assert file.endswith(".json")
    
def test_excluded_is_list(elecrow_data):
    """Checks if the excluded is a list."""
    assert isinstance(elecrow_data["excluded"], list)

def test_excluded_contains_strings(elecrow_data):
    """Checks if all elements in excluded list are strings."""
    for item in elecrow_data["excluded"]:
        assert isinstance(item, str)

def test_excluded_contains_json_extension(elecrow_data):
    """Checks if all elements in excluded are strings with json extensions."""
    for item in elecrow_data["excluded"]:
        assert item.endswith(".json")
        
def test_last_runned_scenario_is_string(elecrow_data):
    """Checks if last_runned_scenario is a string."""
    assert isinstance(elecrow_data["last_runned_scenario"], str)

def test_last_runned_scenario_is_empty(elecrow_data):
    """Checks if last_runned_scenario is empty."""
    assert elecrow_data["last_runned_scenario"] == ""
```