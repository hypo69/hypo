```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data for testing."""
    return {
        "supplier": "ksp",
        "supplier_prefix": "ksp",
        "start_url": "https://www.ksp.co.il/",
        "price_rule": "+100",
        "num_items_4_flush": 300,
        "if_login": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "collect_products_from_categorypage": False,
        "scenario_files": [
            "ksp_categories_consoles_microsoft.json",
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

def test_supplier_is_correct(json_data):
    """Checks if the supplier is 'ksp'."""
    assert json_data["supplier"] == "ksp"

def test_supplier_prefix_is_correct(json_data):
    """Checks if the supplier prefix is 'ksp'."""
    assert json_data["supplier_prefix"] == "ksp"

def test_start_url_is_correct(json_data):
    """Checks if the start URL is correct."""
    assert json_data["start_url"] == "https://www.ksp.co.il/"

def test_price_rule_is_correct(json_data):
    """Checks if the price rule is '+100'."""
    assert json_data["price_rule"] == "+100"

def test_num_items_4_flush_is_correct(json_data):
    """Checks if the number of items for flush is 300."""
    assert json_data["num_items_4_flush"] == 300

def test_if_login_is_false(json_data):
    """Checks if login is set to False."""
    assert json_data["if_login"] is False

def test_parsing_method_is_web(json_data):
    """Checks if the parsing method is 'web'."""
    assert json_data["parcing method [webdriver|api]"] == "web"

def test_about_method_web_scrapping_is_correct(json_data):
     """Checks the 'about method web scrapping' message."""
     assert json_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"

def test_collect_products_from_categorypage_is_false(json_data):
    """Checks if collecting products from category page is set to False."""
    assert json_data["collect_products_from_categorypage"] is False

def test_scenario_files_is_not_empty(json_data):
    """Checks if scenario_files list is not empty."""
    assert len(json_data["scenario_files"]) > 0

def test_scenario_files_contains_expected_files(json_data):
    """Checks if scenario_files list contains expected files."""
    expected_files = [
            "ksp_categories_consoles_microsoft.json",
            "ksp_categories_wathces_apple.json"
        ]
    assert all(file in json_data["scenario_files"] for file in expected_files)

def test_excluded_is_not_empty(json_data):
     """Checks if excluded list is not empty."""
     assert len(json_data["excluded"]) > 0

def test_excluded_contains_expected_files(json_data):
    """Checks if excluded list contains a specific file."""
    assert "ksp_categories_speakers_google.json" in json_data["excluded"]

def test_last_runned_scenario_is_empty(json_data):
    """Checks if last_runned_scenario is empty."""
    assert json_data["last_runned_scenario"] == ""

def test_data_types(json_data):
    """Checks the data types of the values in the JSON data."""
    assert isinstance(json_data["supplier"], str)
    assert isinstance(json_data["supplier_prefix"], str)
    assert isinstance(json_data["start_url"], str)
    assert isinstance(json_data["price_rule"], str)
    assert isinstance(json_data["num_items_4_flush"], int)
    assert isinstance(json_data["if_login"], bool)
    assert isinstance(json_data["parcing method [webdriver|api]"], str)
    assert isinstance(json_data["about method web scrapping [webdriver|api]"], str)
    assert isinstance(json_data["collect_products_from_categorypage"], bool)
    assert isinstance(json_data["scenario_files"], list)
    assert isinstance(json_data["excluded"], list)
    assert isinstance(json_data["last_runned_scenario"], str)
```