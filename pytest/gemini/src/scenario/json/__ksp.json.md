```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "supplier_id": "2787",
      "supplier": "KSP",
      "supplier_prefix": "ksp",
      "start_url": "https://www.ksp.co.il/",
      "price_rule": "+100",
      "if_list":"first","use_mouse": false, "mandatory": true,
      "num_items_4_flush": 300,
      "if_login": false,
      "parcing method [webdriver|api]": "web",
      "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
      "collect_products_from_categorypage": false,
      "scenario_files": [
    
        "ksp_categories_aio_lenovo.json",
        "ksp_categories_headphones_jbl.json",
        "ksp_categories_headphones_msi.json",
        "ksp_categories_headphones_razer.json",
        "ksp_categories_headphones_sony.json",
        "ksp_categories_headphones_xiaomi.json",
        "ksp_categories_monitors_lenovo.json",
        "ksp_categories_monitors_lg.json",
        "ksp_categories_monitors_samsung.json",
        "ksp_categories_motherboards_msi.json",
        "ksp_categories_phones_apple.json",
        "ksp_categories_phones_asus.json",
        "ksp_categories_phones_google.json",
        "ksp_categories_phones_nokia.json",
        "ksp_categories_phones_oneplus.json",
        "ksp_categories_phones_samsung.json",
        "ksp_categories_aio_imacs.json",
    
        "ksp_categories_consoles_microsoft.json",
        "ksp_categories_consoles_nintendo.json",
        "ksp_categories_headphones_bang_olufsen.json",
        "ksp_categories_headphones_hyperx.json",
        "ksp_categories_headphones_ipods.json",
        "ksp_categories_notebooks_hp_by_model.json",
        "ksp_categories_phones_oppo.json",
        "ksp_categories_notebooks_dell_by_model.json"
    
      ],
      "excluded": [
    
        "ksp_categories_phones_xiaomi.json",
        "ksp_categories_phones_oneplus.json",
    
        "ksp_categories_phones_philips.json",
        "ksp_categories_phones_samsung.json",
        "ksp_categories_phones_xiaomi.json",
        "ksp_categories_monitors_samsung.json",
        "ksp_categories_tablets_ipads.json",
        "ksp_categories_tablets_amazon.json",
        "ksp_categories_tablets_lenovo.json",
        "ksp_categories_tablets_samsung.json",
        "ksp_categories_tablets_xiaomi.json",
        "ksp_categories_streamers_google.json",
    
    
        "ksp_categories_motherboards_msi.json",
        "ksp_categories_speakers_google.json",
        "ksp_categories_speakers_jbl.json",
    
        "ksp_categories_phones_apple.json",
        "ksp_categories_phones_asus.json",
        "ksp_categories_phones_google.json",
        "ksp_categories_phones_nokia.json",
        "ksp_categories_phones_oneplus.json",
        "ksp_categories_phones_oppo.json",
        "ksp_categories_phones_philips.json",
        "ksp_categories_phones_samsung.json",
        "ksp_categories_phones_xiaomi.json",
        "ksp_categories_watches_honor.json",
        "ksp_categories_watches_lenovo.json",
        "ksp_categories_watches_garmin.json",
        "ksp_categories_watches_samsung.json",
        "ksp_categories_watches_xiaomi.json",
        "ksp_categories_watches_amazfit.json",
        "ksp_categories_wathces_apple.json",
        "ksp_categories_notebooks_macbook.json",
        "ksp_categories_notebooks_asus_by_model.json",
        "ksp_categories_notebooks_lenovo_by_model.json",
    
    
        "ksp_categories_notebooks_huawei_by_model.json",
        "ksp_categories_monitors_lg.json",
        "ksp_categories_monitors_lenovo.json",
        "ksp_categories_monitors_samsung.json",
        "ksp_categories_tablets_ipads.json",
        "ksp_categories_tablets_amazon.json",
        "ksp_categories_tablets_lenovo.json",
        "ksp_categories_tablets_samsung.json",
        "ksp_categories_tablets_xiaomi.json",
        "ksp_categories_streamers_google.json",
        "ksp_categories_aio_imacs.json.json",
        "ksp_categories_aio_lenovo.json.json",
        "ksp_categories_motherboards_msi.json",
        "ksp_categories_speakers_google.json",
        "ksp_categories_speakers_jbl.json",
        "ksp_categories_headphones_bang_olufsen.json",
        "ksp_categories_headphones_hyperx.json",
        "ksp_categories_headphones_ipods.json",
        "ksp_categories_headphones_jbl.json",
        "ksp_categories_headphones_msi.json",
        "ksp_categories_headphones_razer.json",
        "ksp_categories_headphones_sony.json",
        "ksp_categories_headphones_xiaomi.json",
        "ksp_categories_phones_apple.json",
        "ksp_categories_phones_asus.json",
        "ksp_categories_phones_google.json",
        "ksp_categories_phones_nokia.json",
        "ksp_categories_phones_oneplus.json",
        "ksp_categories_phones_oppo.json",
        "ksp_categories_phones_philips.json",
        "ksp_categories_phones_samsung.json",
        "ksp_categories_phones_xiaomi.json",
        "ksp_categories_watches_honor.json",
        "ksp_categories_watches_lenovo.json",
        "ksp_categories_watches_garmin.json",
        "ksp_categories_watches_samsung.json",
        "ksp_categories_watches_xiaomi.json",
        "ksp_categories_watches_amazfit.json",
        "ksp_categories_wathces_apple.json",
        "ksp_categories_consoles_microsoft.json",
        "ksp_categories_consoles_nintendo.json",
        "ksp_categories_notebooks_asus_by_model.json",
        "ksp_categories_notebooks_macbook.json",
        "ksp_categories_notebooks_asus_by_model.json",
        "ksp_categories_notebooks_lenovo_by_model.json",
        "ksp_categories_notebooks_hp_by_model.json",
        "ksp_categories_notebooks_dell_by_model.json",
        "ksp_categories_notebooks_huawei_by_model.json"
      ],
      "last_runned_scenario": "ksp_categories_phones_apple.json"
    }
    """
    return json.loads(json_data)

def test_supplier_id(ksp_data):
    """Verify the supplier ID is correct."""
    assert ksp_data["supplier_id"] == "2787"

def test_supplier_name(ksp_data):
    """Verify the supplier name is correct."""
    assert ksp_data["supplier"] == "KSP"

def test_supplier_prefix(ksp_data):
    """Verify the supplier prefix is correct."""
    assert ksp_data["supplier_prefix"] == "ksp"

def test_start_url(ksp_data):
    """Verify the start URL is correct."""
    assert ksp_data["start_url"] == "https://www.ksp.co.il/"

def test_price_rule(ksp_data):
    """Verify the price rule is correct."""
    assert ksp_data["price_rule"] == "+100"

def test_if_list(ksp_data):
    """Verify the if_list setting is correct."""
    assert ksp_data["if_list"] == "first"
    
def test_use_mouse(ksp_data):
    """Verify the use_mouse setting is correct."""
    assert ksp_data["use_mouse"] == False
    
def test_mandatory(ksp_data):
    """Verify the mandatory setting is correct."""
    assert ksp_data["mandatory"] == True
    
def test_num_items_4_flush(ksp_data):
     """Verify the num_items_4_flush setting is correct."""
     assert ksp_data["num_items_4_flush"] == 300

def test_if_login(ksp_data):
    """Verify the if_login setting is correct."""
    assert ksp_data["if_login"] == False

def test_parcing_method(ksp_data):
    """Verify the parsing method is correct."""
    assert ksp_data["parcing method [webdriver|api]"] == "web"

def test_about_method_web_scrapping(ksp_data):
    """Verify the about method for web scraping is correct."""
    assert ksp_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"

def test_collect_products_from_categorypage(ksp_data):
    """Verify the collect_products_from_categorypage setting is correct."""
    assert ksp_data["collect_products_from_categorypage"] == False


def test_scenario_files_is_list(ksp_data):
    """Verify that scenario_files is a list."""
    assert isinstance(ksp_data["scenario_files"], list)


def test_scenario_files_not_empty(ksp_data):
    """Verify that the scenario_files list is not empty."""
    assert len(ksp_data["scenario_files"]) > 0
    
def test_excluded_files_is_list(ksp_data):
    """Verify that excluded is a list."""
    assert isinstance(ksp_data["excluded"], list)

def test_excluded_files_not_empty(ksp_data):
     """Verify that the excluded list is not empty."""
     assert len(ksp_data["excluded"]) > 0


def test_last_runned_scenario(ksp_data):
    """Verify the last runned scenario is correct."""
    assert ksp_data["last_runned_scenario"] == "ksp_categories_phones_apple.json"

def test_scenario_files_are_strings(ksp_data):
    """Verify that all elements in scenario_files are strings."""
    for item in ksp_data["scenario_files"]:
        assert isinstance(item, str)

def test_excluded_files_are_strings(ksp_data):
    """Verify that all elements in excluded are strings."""
    for item in ksp_data["excluded"]:
        assert isinstance(item, str)
```