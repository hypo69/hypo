```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def kualastyle_data():
    """Loads the kualastyle.json data from the given file path."""
    file_path = "hypotez/src/scenario/json/kualastyle.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def test_supplier_exists(kualastyle_data):
    """Checks if the 'supplier' key exists and has a value."""
    assert "supplier" in kualastyle_data
    assert kualastyle_data["supplier"] == "kualastyle"


def test_supplier_id_exists_and_is_correct(kualastyle_data):
    """Checks if the 'supplier_id' key exists and has correct value."""
    assert "supplier_id" in kualastyle_data
    assert kualastyle_data["supplier_id"] == "11028"

def test_supplier_prefix_exists_and_is_correct(kualastyle_data):
    """Checks if the 'supplier_prefix' key exists and has correct value."""
    assert "supplier_prefix" in kualastyle_data
    assert kualastyle_data["supplier_prefix"] == "kualastyle"

def test_start_url_exists(kualastyle_data):
    """Checks if the 'start_url' key exists and has a valid value."""
    assert "start_url" in kualastyle_data
    assert kualastyle_data["start_url"] == "https://kualastyle.com"

def test_login_url_exists(kualastyle_data):
    """Checks if the 'login_url' key exists and has a valid value."""
    assert "login_url" in kualastyle_data
    assert kualastyle_data["login_url"] == "https://kualastyle.com"

def test_check_categories_on_site_exists_and_is_boolean(kualastyle_data):
    """Checks if 'check categories on site' exists and is a boolean."""
    assert "check categories on site" in kualastyle_data
    assert isinstance(kualastyle_data["check categories on site"], bool)
    assert kualastyle_data["check categories on site"] == True

def test_if_login_exists_and_is_boolean(kualastyle_data):
    """Checks if 'if_login' exists and is a boolean."""
    assert "if_login" in kualastyle_data
    assert isinstance(kualastyle_data["if_login"], bool)
    assert kualastyle_data["if_login"] == True

def test_price_rule_exists(kualastyle_data):
    """Checks if 'price_rule' key exists and is a string."""
    assert "price_rule" in kualastyle_data
    assert isinstance(kualastyle_data["price_rule"], str)
    assert kualastyle_data["price_rule"] == "*1"

def test_if_list_exists_and_is_string(kualastyle_data):
    """Checks if 'if_list' exists and has string value"""
    assert "if_list" in kualastyle_data
    assert isinstance(kualastyle_data["if_list"], str)
    assert kualastyle_data["if_list"] == "first"


def test_use_mouse_exists_and_is_boolean(kualastyle_data):
        """Checks if 'use_mouse' exists and is a boolean"""
        assert "use_mouse" in kualastyle_data
        assert isinstance(kualastyle_data["use_mouse"], bool)
        assert kualastyle_data["use_mouse"] == False

def test_mandatory_exists_and_is_boolean(kualastyle_data):
        """Checks if 'mandatory' exists and is a boolean"""
        assert "mandatory" in kualastyle_data
        assert isinstance(kualastyle_data["mandatory"], bool)
        assert kualastyle_data["mandatory"] == True


def test_parcing_method_exists(kualastyle_data):
    """Checks if 'parcing method [webdriver|api]' key exists and has correct value"""
    assert "parcing method [webdriver|api]" in kualastyle_data
    assert kualastyle_data["parcing method [webdriver|api]"] == "web"

def test_about_method_exists(kualastyle_data):
    """Checks if 'about method web scrapping [webdriver|api]' exists and has a string value"""
    assert "about method web scrapping [webdriver|api]" in kualastyle_data
    assert isinstance(kualastyle_data["about method web scrapping [webdriver|api]"], str)

def test_collect_products_from_categorypage_exists_and_is_boolean(kualastyle_data):
    """Checks if 'collect_products_from_categorypage' exists and is a boolean."""
    assert "collect_products_from_categorypage" in kualastyle_data
    assert isinstance(kualastyle_data["collect_products_from_categorypage"], bool)
    assert kualastyle_data["collect_products_from_categorypage"] == False

def test_num_items_4_flush_exists(kualastyle_data):
    """Checks if the 'num_items_4_flush' key exists and has correct value."""
    assert "num_items_4_flush" in kualastyle_data
    assert isinstance(kualastyle_data["num_items_4_flush"], int)
    assert kualastyle_data["num_items_4_flush"] == 500

def test_scenario_files_exists_and_is_list(kualastyle_data):
    """Checks if 'scenario_files' key exists and is a list."""
    assert "scenario_files" in kualastyle_data
    assert isinstance(kualastyle_data["scenario_files"], list)
    assert len(kualastyle_data["scenario_files"]) == 10


def test_last_runned_scenario_exists_and_is_string(kualastyle_data):
        """Checks if 'last_runned_scenario' exists and is a string."""
        assert "last_runned_scenario" in kualastyle_data
        assert isinstance(kualastyle_data["last_runned_scenario"], str)
        

def test_excluded_exists_and_is_list(kualastyle_data):
    """Checks if 'excluded' key exists and is a list (can be empty)."""
    assert "excluded" in kualastyle_data
    assert isinstance(kualastyle_data["excluded"], list)

def test_all_keys_present(kualastyle_data):
    """Checks that all expected keys are present in the data."""
    expected_keys = [
        "supplier", "supplier_id", "supplier_prefix", "start_url", "login_url",
        "check categories on site", "if_login", "price_rule", "if_list", "use_mouse", "mandatory",
        "parcing method [webdriver|api]", "about method web scrapping [webdriver|api]",
        "collect_products_from_categorypage", "num_items_4_flush", "scenario_files",
        "last_runned_scenario","excluded"
    ]
    assert all(key in kualastyle_data for key in expected_keys)


def test_scenario_files_content(kualastyle_data):
    """Checks if scenario files values are correct."""
    expected_files = [
        "kualastyle_categories_accessories.json",
        "kualastyle_categories_appliances.json",
        "kualastyle_categories_carpets.json",
        "kualastyle_categories_children_and_youth.json",
        "kualastyle_categories_furniture.json",
        "kualastyle_categories_lighting.json",
        "kualastyle_categories_mattresses.json",
        "kualastyle_categories_mirrors.json",
        "kualastyle_categories_photos.json",
        "kualastyle_categories_textile.json"
    ]
    assert kualastyle_data["scenario_files"] == expected_files
```