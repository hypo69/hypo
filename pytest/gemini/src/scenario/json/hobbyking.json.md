```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data as a dictionary for testing."""
    return {
    "supplier": "ksp",
    "supplier_prefix": "ksp",
    "start_url": "https://www.ksp.co.il/",
    "price_rule": "+100",
    "num_items_4_flush": 300,
    "if_login": False,
    "collect_products_from_categorypage": False,
    "scenarios": [
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

def test_json_data_is_loaded(json_data):
    """Checks if the fixture loads the JSON data correctly."""
    assert json_data is not None
    assert isinstance(json_data, dict)

def test_supplier_key_exists(json_data):
    """Checks if the 'supplier' key exists and has a valid value."""
    assert "supplier" in json_data
    assert json_data["supplier"] == "ksp"

def test_supplier_prefix_key_exists(json_data):
    """Checks if the 'supplier_prefix' key exists and has a valid value."""
    assert "supplier_prefix" in json_data
    assert json_data["supplier_prefix"] == "ksp"

def test_start_url_key_exists(json_data):
    """Checks if the 'start_url' key exists and has a valid value."""
    assert "start_url" in json_data
    assert json_data["start_url"] == "https://www.ksp.co.il/"

def test_price_rule_key_exists(json_data):
    """Checks if the 'price_rule' key exists and has a valid value."""
    assert "price_rule" in json_data
    assert json_data["price_rule"] == "+100"

def test_num_items_4_flush_key_exists(json_data):
    """Checks if the 'num_items_4_flush' key exists and has a valid value."""
    assert "num_items_4_flush" in json_data
    assert json_data["num_items_4_flush"] == 300

def test_if_login_key_exists(json_data):
    """Checks if the 'if_login' key exists and has a valid value."""
    assert "if_login" in json_data
    assert json_data["if_login"] is False

def test_collect_products_from_categorypage_key_exists(json_data):
    """Checks if the 'collect_products_from_categorypage' key exists and has a valid value."""
    assert "collect_products_from_categorypage" in json_data
    assert json_data["collect_products_from_categorypage"] is False

def test_scenarios_key_exists_and_is_list(json_data):
    """Checks if the 'scenarios' key exists and is a list."""
    assert "scenarios" in json_data
    assert isinstance(json_data["scenarios"], list)

def test_scenarios_list_not_empty(json_data):
    """Checks if the 'scenarios' list is not empty."""
    assert len(json_data["scenarios"]) > 0

def test_excluded_key_exists_and_is_list(json_data):
    """Checks if the 'excluded' key exists and is a list."""
    assert "excluded" in json_data
    assert isinstance(json_data["excluded"], list)

def test_excluded_list_not_empty(json_data):
    """Checks if the 'excluded' list is not empty."""
    assert len(json_data["excluded"]) > 0


def test_last_runned_scenario_key_exists(json_data):
    """Checks if the 'last_runned_scenario' key exists."""
    assert "last_runned_scenario" in json_data


def test_last_runned_scenario_is_string(json_data):
     """Checks if the 'last_runned_scenario' key  is a string."""
     assert isinstance(json_data["last_runned_scenario"], str)


def test_last_runned_scenario_initial_value(json_data):
    """Checks if the initial value of 'last_runned_scenario' is an empty string."""
    assert json_data["last_runned_scenario"] == ""
```