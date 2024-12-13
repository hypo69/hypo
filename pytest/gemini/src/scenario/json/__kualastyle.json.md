```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def kualastyle_data():
    """Loads the kualastyle JSON data from file."""
    with open('hypotez/src/scenario/json/__kualastyle.json', 'r') as f:
        return json.load(f)

def test_supplier_field_exists(kualastyle_data):
    """Checks if the 'supplier' field exists and is a string."""
    assert "supplier" in kualastyle_data
    assert isinstance(kualastyle_data["supplier"], str)
    assert kualastyle_data["supplier"] == "kualastyle"

def test_supplier_id_field_exists(kualastyle_data):
    """Checks if the 'supplier_id' field exists and is a string."""
    assert "supplier_id" in kualastyle_data
    assert isinstance(kualastyle_data["supplier_id"], str)
    assert kualastyle_data["supplier_id"] == "11028"

def test_supplier_prefix_field_exists(kualastyle_data):
    """Checks if the 'supplier_prefix' field exists and is a string."""
    assert "supplier_prefix" in kualastyle_data
    assert isinstance(kualastyle_data["supplier_prefix"], str)
    assert kualastyle_data["supplier_prefix"] == "kualastyle"

def test_start_url_field_exists(kualastyle_data):
    """Checks if the 'start_url' field exists and is a valid URL string."""
    assert "start_url" in kualastyle_data
    assert isinstance(kualastyle_data["start_url"], str)
    assert kualastyle_data["start_url"].startswith("https://")

def test_login_url_field_exists(kualastyle_data):
    """Checks if the 'login_url' field exists and is a valid URL string."""
    assert "login_url" in kualastyle_data
    assert isinstance(kualastyle_data["login_url"], str)
    assert kualastyle_data["login_url"].startswith("https://")

def test_check_categories_on_site_field_exists(kualastyle_data):
    """Checks if the 'check categories on site' field exists and is a boolean."""
    assert "check categories on site" in kualastyle_data
    assert isinstance(kualastyle_data["check categories on site"], bool)

def test_if_login_field_exists(kualastyle_data):
    """Checks if the 'if_login' field exists and is a boolean."""
    assert "if_login" in kualastyle_data
    assert isinstance(kualastyle_data["if_login"], bool)

def test_price_rule_field_exists(kualastyle_data):
    """Checks if the 'price_rule' field exists and is a string."""
    assert "price_rule" in kualastyle_data
    assert isinstance(kualastyle_data["price_rule"], str)

def test_if_list_field_exists(kualastyle_data):
    """Checks if the 'if_list' field exists and is a string."""
    assert "if_list" in kualastyle_data
    assert isinstance(kualastyle_data["if_list"], str)
    assert kualastyle_data["if_list"] in ("first", "all")


def test_use_mouse_field_exists(kualastyle_data):
    """Checks if the 'use_mouse' field exists and is a boolean."""
    assert "use_mouse" in kualastyle_data
    assert isinstance(kualastyle_data["use_mouse"], bool)

def test_mandatory_field_exists(kualastyle_data):
     """Checks if the 'mandatory' field exists and is a boolean."""
     assert "mandatory" in kualastyle_data
     assert isinstance(kualastyle_data["mandatory"], bool)

def test_parcing_method_field_exists(kualastyle_data):
    """Checks if the 'parcing method [webdriver|api]' field exists and is a string."""
    assert "parcing method [webdriver|api]" in kualastyle_data
    assert isinstance(kualastyle_data["parcing method [webdriver|api]"], str)
    assert kualastyle_data["parcing method [webdriver|api]"] in ("web", "api")

def test_about_method_field_exists(kualastyle_data):
     """Checks if the 'about method web scrapping [webdriver|api]' field exists and is a string."""
     assert "about method web scrapping [webdriver|api]" in kualastyle_data
     assert isinstance(kualastyle_data["about method web scrapping [webdriver|api]"], str)

def test_collect_products_from_categorypage_field_exists(kualastyle_data):
    """Checks if the 'collect_products_from_categorypage' field exists and is a boolean."""
    assert "collect_products_from_categorypage" in kualastyle_data
    assert isinstance(kualastyle_data["collect_products_from_categorypage"], bool)


def test_num_items_4_flush_field_exists(kualastyle_data):
    """Checks if the 'num_items_4_flush' field exists and is an integer."""
    assert "num_items_4_flush" in kualastyle_data
    assert isinstance(kualastyle_data["num_items_4_flush"], int)


def test_scenario_files_field_exists(kualastyle_data):
    """Checks if the 'scenario_files' field exists and is a list."""
    assert "scenario_files" in kualastyle_data
    assert isinstance(kualastyle_data["scenario_files"], list)
    for file_name in kualastyle_data["scenario_files"]:
        assert isinstance(file_name, str)
        assert file_name.endswith(".json")

def test_last_runned_scenario_field_exists(kualastyle_data):
    """Checks if the 'last_runned_scenario' field exists and is a string."""
    assert "last_runned_scenario" in kualastyle_data
    assert isinstance(kualastyle_data["last_runned_scenario"], str)

def test_excluded_field_exists(kualastyle_data):
    """Checks if the 'excluded' field exists and is a list."""
    assert "excluded" in kualastyle_data
    assert isinstance(kualastyle_data["excluded"], list)
    # Additional check if necessary: assert all elements in excluded are strings, etc.

def test_all_keys_present(kualastyle_data):
    """Check if all expected keys are present in the dictionary"""
    expected_keys = {
      "supplier",
      "supplier_id",
      "supplier_prefix",
      "start_url",
      "login_url",
      "check categories on site",
      "if_login",
      "price_rule",
      "if_list",
      "use_mouse",
      "mandatory",
      "parcing method [webdriver|api]",
      "about method web scrapping [webdriver|api]",
      "collect_products_from_categorypage",
      "num_items_4_flush",
      "scenario_files",
       "last_runned_scenario",
      "excluded"
    }

    assert set(kualastyle_data.keys()) == expected_keys
```