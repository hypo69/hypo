```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_data():
    """Loads the ksp.json data for testing."""
    with open("hypotez/src/scenario/json/ksp.json", 'r') as f:
        return json.load(f)

def test_ksp_data_structure(ksp_data):
    """Checks if the basic structure of the JSON data is correct."""
    assert isinstance(ksp_data, dict), "The loaded data should be a dictionary."
    assert "supplier_id" in ksp_data, "supplier_id key is missing."
    assert "supplier" in ksp_data, "supplier key is missing."
    assert "supplier_prefix" in ksp_data, "supplier_prefix key is missing."
    assert "start_url" in ksp_data, "start_url key is missing."
    assert "price_rule" in ksp_data, "price_rule key is missing."
    assert "if_list" in ksp_data, "if_list key is missing."
    assert "use_mouse" in ksp_data, "use_mouse key is missing."
    assert "mandatory" in ksp_data, "mandatory key is missing."
    assert "num_items_4_flush" in ksp_data, "num_items_4_flush key is missing."
    assert "if_login" in ksp_data, "if_login key is missing."
    assert "parcing method [webdriver|api]" in ksp_data, "parcing method [webdriver|api] key is missing."
    assert "about method web scrapping [webdriver|api]" in ksp_data, "about method web scrapping [webdriver|api] key is missing."
    assert "collect_products_from_categorypage" in ksp_data, "collect_products_from_categorypage key is missing."
    assert "scenario_files" in ksp_data, "scenario_files key is missing."
    assert "excluded" in ksp_data, "excluded key is missing."
    assert "last_runned_scenario" in ksp_data, "last_runned_scenario key is missing."

def test_ksp_supplier_id_type(ksp_data):
    """Checks if supplier_id is a string."""
    assert isinstance(ksp_data["supplier_id"], str), "supplier_id should be a string."

def test_ksp_supplier_type(ksp_data):
    """Checks if supplier is a string."""
    assert isinstance(ksp_data["supplier"], str), "supplier should be a string."

def test_ksp_supplier_prefix_type(ksp_data):
     """Checks if supplier_prefix is a string."""
     assert isinstance(ksp_data["supplier_prefix"], str), "supplier_prefix should be a string."

def test_ksp_start_url_type(ksp_data):
    """Checks if start_url is a string."""
    assert isinstance(ksp_data["start_url"], str), "start_url should be a string."

def test_ksp_price_rule_type(ksp_data):
    """Checks if price_rule is a string."""
    assert isinstance(ksp_data["price_rule"], str), "price_rule should be a string."

def test_ksp_if_list_type(ksp_data):
    """Checks if if_list is a string."""
    assert isinstance(ksp_data["if_list"], str), "if_list should be a string."

def test_ksp_use_mouse_type(ksp_data):
    """Checks if use_mouse is a boolean."""
    assert isinstance(ksp_data["use_mouse"], bool), "use_mouse should be a boolean."

def test_ksp_mandatory_type(ksp_data):
    """Checks if mandatory is a boolean."""
    assert isinstance(ksp_data["mandatory"], bool), "mandatory should be a boolean."

def test_ksp_num_items_4_flush_type(ksp_data):
    """Checks if num_items_4_flush is an integer."""
    assert isinstance(ksp_data["num_items_4_flush"], int), "num_items_4_flush should be an integer."

def test_ksp_if_login_type(ksp_data):
    """Checks if if_login is a boolean."""
    assert isinstance(ksp_data["if_login"], bool), "if_login should be a boolean."

def test_ksp_parcing_method_type(ksp_data):
    """Checks if parcing method is a string."""
    assert isinstance(ksp_data["parcing method [webdriver|api]"], str), "parcing method should be a string."

def test_ksp_about_method_type(ksp_data):
    """Checks if about method is a string."""
    assert isinstance(ksp_data["about method web scrapping [webdriver|api]"], str), "about method should be a string."

def test_ksp_collect_products_from_categorypage_type(ksp_data):
    """Checks if collect_products_from_categorypage is a boolean."""
    assert isinstance(ksp_data["collect_products_from_categorypage"], bool), "collect_products_from_categorypage should be a boolean."

def test_ksp_scenario_files_type(ksp_data):
    """Checks if scenario_files is a list."""
    assert isinstance(ksp_data["scenario_files"], list), "scenario_files should be a list."
    for item in ksp_data["scenario_files"]:
        assert isinstance(item, str), "Each item in scenario_files should be a string."

def test_ksp_excluded_type(ksp_data):
    """Checks if excluded is a list."""
    assert isinstance(ksp_data["excluded"], list), "excluded should be a list."
    for item in ksp_data["excluded"]:
        assert isinstance(item, str), "Each item in excluded should be a string."

def test_ksp_last_runned_scenario_type(ksp_data):
    """Checks if last_runned_scenario is a string."""
    assert isinstance(ksp_data["last_runned_scenario"], str), "last_runned_scenario should be a string."

def test_ksp_num_items_4_flush_positive(ksp_data):
    """Checks if num_items_4_flush is a positive integer."""
    assert ksp_data["num_items_4_flush"] >= 0, "num_items_4_flush should be a positive integer or zero."

def test_ksp_scenario_files_not_empty(ksp_data):
    """Checks if scenario_files list is not empty."""
    assert len(ksp_data["scenario_files"]) > 0, "scenario_files list should not be empty"
```