```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data for testing."""
    return {
        "supplier": "crow_pi",
        "supplier_prefix": "crow_pi",
        "start_url": "https://www.crowpi.cc/",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "root_category": 3,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
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

def test_json_data_supplier(json_data):
    """Tests if the 'supplier' field is correct."""
    assert json_data["supplier"] == "crow_pi"

def test_json_data_supplier_prefix(json_data):
    """Tests if the 'supplier_prefix' field is correct."""
    assert json_data["supplier_prefix"] == "crow_pi"

def test_json_data_start_url(json_data):
    """Tests if the 'start_url' field is correct."""
    assert json_data["start_url"] == "https://www.crowpi.cc/"

def test_json_data_price_rule(json_data):
    """Tests if the 'price_rule' field is correct."""
    assert json_data["price_rule"] == "+0"

def test_json_data_if_login(json_data):
    """Tests if the 'if_login' field is correct."""
    assert json_data["if_login"] == False

def test_json_data_collect_products_from_categorypage(json_data):
    """Tests if the 'collect_products_from_categorypage' field is correct."""
    assert json_data["collect_products_from_categorypage"] == False

def test_json_data_root_category(json_data):
    """Tests if the 'root_category' field is correct."""
    assert json_data["root_category"] == 3

def test_json_data_parcing_method(json_data):
    """Tests if the 'parcing method [webdriver|api]' field is correct."""
    assert json_data["parcing method [webdriver|api]"] == "web"

def test_json_data_about_method(json_data):
    """Tests if the 'about method web scrapping [webdriver|api]' field is correct."""
    assert json_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"

def test_json_data_scenario_files(json_data):
    """Tests if the 'scenario_files' field is correct and has the correct structure."""
    assert isinstance(json_data["scenario_files"], list)
    assert ".json" in json_data["scenario_files"]
    assert "ksp_categories_wathces_apple.json" in json_data["scenario_files"]

def test_json_data_excluded_list(json_data):
    """Tests if the 'excluded' field is correct and contains specific files."""
    assert isinstance(json_data["excluded"], list)
    assert "ksp_categories_speakers_google.json" in json_data["excluded"]
    assert "ksp_categories_monitors_lg.json" in json_data["excluded"]

def test_json_data_last_runned_scenario(json_data):
    """Tests if the 'last_runned_scenario' field is correct."""
    assert json_data["last_runned_scenario"] == ""

def test_json_data_structure(json_data):
    """Tests if the JSON data has the correct keys."""
    expected_keys = [
        "supplier",
        "supplier_prefix",
        "start_url",
        "price_rule",
        "if_login",
        "collect_products_from_categorypage",
        "root_category",
        "parcing method [webdriver|api]",
        "about method web scrapping [webdriver|api]",
        "scenario_files",
        "excluded",
        "last_runned_scenario"
    ]
    assert all(key in json_data for key in expected_keys)

def test_json_data_excluded_is_a_list(json_data):
     """Tests if the 'excluded' field is a list"""
     assert isinstance(json_data["excluded"], list)

def test_json_data_scenario_files_is_a_list(json_data):
    """Tests if 'scenario_files' field is a list"""
    assert isinstance(json_data["scenario_files"], list)

def test_json_data_empty_excluded_list():
    """Test with empty 'excluded' list"""
    data = {
        "supplier": "crow_pi",
        "supplier_prefix": "crow_pi",
        "start_url": "https://www.crowpi.cc/",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "root_category": 3,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "scenario_files": [
            ".json",
            "ksp_categories_wathces_apple.json"
        ],
        "excluded": [],
        "last_runned_scenario": ""
    }
    assert isinstance(data["excluded"], list)
    assert not data["excluded"]

def test_json_data_empty_scenario_files_list():
    """Test with empty 'scenario_files' list"""
    data = {
        "supplier": "crow_pi",
        "supplier_prefix": "crow_pi",
        "start_url": "https://www.crowpi.cc/",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "root_category": 3,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "scenario_files": [],
        "excluded": [
            "ksp_categories_speakers_google.json",
            "ksp_categories_speakers_jbl.json",
        ],
        "last_runned_scenario": ""
    }
    assert isinstance(data["scenario_files"], list)
    assert not data["scenario_files"]
```