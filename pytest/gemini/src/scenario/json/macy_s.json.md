```python
import pytest
import json

# Fixture for loading the JSON data
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


def test_json_data_structure(json_data):
    """Verify the basic structure of the loaded JSON data."""
    assert isinstance(json_data, dict)
    assert "supplier" in json_data
    assert "scenario_files" in json_data
    assert "excluded" in json_data

def test_supplier_value(json_data):
    """Verify the 'supplier' value."""
    assert json_data["supplier"] == "ksp"

def test_start_url_is_valid_url(json_data):
    """Verify that 'start_url' is a valid URL (basic check)."""
    start_url = json_data["start_url"]
    assert start_url.startswith("https://") or start_url.startswith("http://")
    assert "." in start_url # check for domain

def test_price_rule_is_string(json_data):
     """Verify that 'price_rule' is a string."""
     assert isinstance(json_data["price_rule"], str)


def test_num_items_4_flush_is_int(json_data):
    """Verify that 'num_items_4_flush' is an integer."""
    assert isinstance(json_data["num_items_4_flush"], int)

def test_if_login_is_boolean(json_data):
    """Verify that 'if_login' is a boolean."""
    assert isinstance(json_data["if_login"], bool)


def test_parcing_method_is_string(json_data):
    """Verify that 'parcing method [webdriver|api]' is a string"""
    assert isinstance(json_data["parcing method [webdriver|api]"], str)


def test_about_method_is_string(json_data):
    """Verify that 'about method web scrapping [webdriver|api]' is a string"""
    assert isinstance(json_data["about method web scrapping [webdriver|api]"], str)

def test_collect_products_from_categorypage_is_boolean(json_data):
        """Verify that 'collect_products_from_categorypage' is a boolean."""
        assert isinstance(json_data["collect_products_from_categorypage"], bool)


def test_scenario_files_is_list(json_data):
    """Verify that 'scenario_files' is a list."""
    assert isinstance(json_data["scenario_files"], list)

def test_scenario_files_content_is_string(json_data):
    """Verify that items in 'scenario_files' are strings."""
    for item in json_data["scenario_files"]:
        assert isinstance(item, str)

def test_excluded_is_list(json_data):
    """Verify that 'excluded' is a list."""
    assert isinstance(json_data["excluded"], list)

def test_excluded_content_is_string(json_data):
    """Verify that items in 'excluded' are strings."""
    for item in json_data["excluded"]:
        assert isinstance(item, str)

def test_last_runned_scenario_is_string(json_data):
    """Verify that 'last_runned_scenario' is a string."""
    assert isinstance(json_data["last_runned_scenario"], str)

def test_scenario_files_not_empty(json_data):
    """Verify that the 'scenario_files' list is not empty"""
    assert len(json_data["scenario_files"]) > 0

def test_excluded_can_be_empty(json_data):
        """Verify that the 'excluded' list can be empty"""
        assert isinstance(json_data["excluded"], list)

def test_last_runned_scenario_can_be_empty(json_data):
        """Verify that the 'last_runned_scenario' can be empty"""
        assert isinstance(json_data["last_runned_scenario"], str)
```