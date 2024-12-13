```python
import pytest
import json

# Fixture to load the json data
@pytest.fixture
def amazon_config():
    """Provides the amazon configuration data as a dictionary."""
    return {
        "supplier": "amazon",
        "supplier_id": "2800",
        "supplier_prefix": "amazon",
        "start_url": "https://www.amazon.com/",
        "price_rule": "+0",
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "if_login": False,
        "login_url": "https://amazon.com",
        "lang": "EN",
        "check categories on site": False,
        "parsing via api": False,
        "collect_products_from_categorypage": False,
        "scenario_files": [
            "amazon_categories_murano_glass.json"
        ],
        "excluded": [
            "amazon_categories_lighting.json",
            "amazon_categories_shelves.json",
            "amazon_categories_consoles.json",
            "amazon_categories_office_chairs.json",
            "amazon_categories_ottomans.json",
            "amazon_categories_desktops_dell_ref.json",
            "amazon_categories_videocards.json",
            "amazon_categories_copmuter_cooling_corsair_new.json",
            "amazon_categories_desktops_dell_ref.json",
            "amazon_categories_desktops_hp_used.json",
            "amazon_categories_desktops_lenovo_new.json",
            "amazon_categories_desktops_lenovo_ref.json",
            "amazon_categories_desktops_lenovo_used.json",
            "amazon_categories_laptops_acer.json",
            "amazon_categories_laptops_asus.json",
            "amazon_stores_tech_pirate.json",
            "amazon_stores_amazon_ref.json",
            "amazon_stores_asus.json",
            "amazon_stores_feebz.json",
            "amazon_stores_lenovo.json",
             "amazon_categories_laptops_lenovo.json",
            "amazon_categories_watches_apple.json",
            "amazon_categories_laptops_macbook.json.json"
        ],
        "last_runned_scenario": "",
        "last_runned_scenario_filename": ""
    }

def test_amazon_config_supplier(amazon_config):
    """Tests if the supplier field is correct"""
    assert amazon_config["supplier"] == "amazon"

def test_amazon_config_supplier_id(amazon_config):
    """Tests if the supplier_id field is correct"""
    assert amazon_config["supplier_id"] == "2800"

def test_amazon_config_supplier_prefix(amazon_config):
     """Tests if the supplier_prefix field is correct"""
     assert amazon_config["supplier_prefix"] == "amazon"

def test_amazon_config_start_url(amazon_config):
    """Tests if the start_url is correct"""
    assert amazon_config["start_url"] == "https://www.amazon.com/"

def test_amazon_config_price_rule(amazon_config):
    """Tests if the price_rule is correct"""
    assert amazon_config["price_rule"] == "+0"

def test_amazon_config_if_list(amazon_config):
    """Tests if the if_list field is correct"""
    assert amazon_config["if_list"] == "first"

def test_amazon_config_use_mouse(amazon_config):
     """Tests if the use_mouse field is correct"""
     assert amazon_config["use_mouse"] == False

def test_amazon_config_mandatory(amazon_config):
    """Tests if the mandatory field is correct"""
    assert amazon_config["mandatory"] == True

def test_amazon_config_if_login(amazon_config):
     """Tests if the if_login field is correct"""
     assert amazon_config["if_login"] == False

def test_amazon_config_login_url(amazon_config):
    """Tests if the login_url field is correct"""
    assert amazon_config["login_url"] == "https://amazon.com"

def test_amazon_config_lang(amazon_config):
    """Tests if the lang field is correct"""
    assert amazon_config["lang"] == "EN"

def test_amazon_config_check_categories(amazon_config):
    """Tests if the check categories field is correct"""
    assert amazon_config["check categories on site"] == False

def test_amazon_config_parsing_api(amazon_config):
    """Tests if the parsing via api is correct"""
    assert amazon_config["parsing via api"] == False

def test_amazon_config_collect_products(amazon_config):
     """Tests if the collect_products_from_categorypage field is correct"""
     assert amazon_config["collect_products_from_categorypage"] == False

def test_amazon_config_scenario_files(amazon_config):
    """Tests if scenario files are correctly loaded"""
    assert isinstance(amazon_config["scenario_files"], list)
    assert "amazon_categories_murano_glass.json" in amazon_config["scenario_files"]

def test_amazon_config_excluded_files(amazon_config):
    """Tests if excluded files are correctly loaded and is a list"""
    assert isinstance(amazon_config["excluded"], list)
    assert "amazon_categories_lighting.json" in amazon_config["excluded"]

def test_amazon_config_last_runned_scenario(amazon_config):
    """Tests if last_runned_scenario is an empty string"""
    assert amazon_config["last_runned_scenario"] == ""

def test_amazon_config_last_runned_scenario_filename(amazon_config):
    """Tests if last_runned_scenario_filename is an empty string"""
    assert amazon_config["last_runned_scenario_filename"] == ""

def test_amazon_config_all_keys_present(amazon_config):
    """Tests if all keys are present"""
    expected_keys = [
        "supplier", "supplier_id", "supplier_prefix", "start_url", "price_rule", "if_list", "use_mouse", "mandatory",
        "if_login", "login_url", "lang", "check categories on site", "parsing via api",
        "collect_products_from_categorypage", "scenario_files", "excluded", "last_runned_scenario",
        "last_runned_scenario_filename"
    ]
    assert all(key in amazon_config for key in expected_keys)

def test_amazon_config_type_validation(amazon_config):
    """Validates the types of all fields in config"""
    assert isinstance(amazon_config["supplier"], str)
    assert isinstance(amazon_config["supplier_id"], str)
    assert isinstance(amazon_config["supplier_prefix"], str)
    assert isinstance(amazon_config["start_url"], str)
    assert isinstance(amazon_config["price_rule"], str)
    assert isinstance(amazon_config["if_list"], str)
    assert isinstance(amazon_config["use_mouse"], bool)
    assert isinstance(amazon_config["mandatory"], bool)
    assert isinstance(amazon_config["if_login"], bool)
    assert isinstance(amazon_config["login_url"], str)
    assert isinstance(amazon_config["lang"], str)
    assert isinstance(amazon_config["check categories on site"], bool)
    assert isinstance(amazon_config["parsing via api"], bool)
    assert isinstance(amazon_config["collect_products_from_categorypage"], bool)
    assert isinstance(amazon_config["scenario_files"], list)
    assert isinstance(amazon_config["excluded"], list)
    assert isinstance(amazon_config["last_runned_scenario"], str)
    assert isinstance(amazon_config["last_runned_scenario_filename"], str)


def test_amazon_config_excluded_list_content_type(amazon_config):
    """Test to ensure that items in the excluded list are strings."""
    for item in amazon_config["excluded"]:
        assert isinstance(item, str), "All items in 'excluded' list must be strings."

def test_amazon_config_scenario_files_list_content_type(amazon_config):
     """Test to ensure that items in the scenario_files list are strings."""
     for item in amazon_config["scenario_files"]:
        assert isinstance(item, str), "All items in 'scenario_files' list must be strings."
```