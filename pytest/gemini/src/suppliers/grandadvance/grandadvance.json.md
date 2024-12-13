```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def grandadvance_data():
    """Provides the grandadvance supplier data loaded from the JSON."""
    with open("hypotez/src/suppliers/grandadvance/grandadvance.json", 'r') as file:
        data = json.load(file)
    return data

def test_supplier_name(grandadvance_data):
    """Checks if the supplier name is correct."""
    assert grandadvance_data["supplier"] == "grandadvance", "Supplier name should be 'grandadvance'."

def test_supplier_id_is_string(grandadvance_data):
    """Checks if supplier ID is a string."""
    assert isinstance(grandadvance_data["supplier_id"], str), "Supplier ID should be a string."

def test_supplier_id_correct_value(grandadvance_data):
    """Checks if supplier ID has the correct value."""
    assert grandadvance_data["supplier_id"] == "2789", "Supplier ID should be '2789'."

def test_supplier_prefix_is_string(grandadvance_data):
      """Checks if supplier prefix is a string."""
      assert isinstance(grandadvance_data["supplier_prefix"], str), "Supplier prefix should be a string."

def test_supplier_prefix_correct_value(grandadvance_data):
    """Checks if the supplier prefix is correct."""
    assert grandadvance_data["supplier_prefix"] == "grandadvance", "Supplier prefix should be 'grandadvance'."

def test_start_url_is_string(grandadvance_data):
    """Checks if start URL is a string."""
    assert isinstance(grandadvance_data["start_url"], str), "Start URL should be a string."

def test_start_url_valid_format(grandadvance_data):
    """Checks if the start URL starts with 'https://'."""
    assert grandadvance_data["start_url"].startswith("https://"), "Start URL should start with 'https://'."

def test_price_rule_is_string(grandadvance_data):
     """Checks if price rule is a string."""
     assert isinstance(grandadvance_data["price_rule"], str), "Price rule should be a string."

def test_price_rule_correct_value(grandadvance_data):
    """Checks if the price rule is correct."""
    assert grandadvance_data["price_rule"] == "+0", "Price rule should be '+0'."

def test_if_login_is_boolean(grandadvance_data):
     """Checks if if_login is a boolean."""
     assert isinstance(grandadvance_data["if_login"], bool), "if_login should be a boolean."

def test_if_login_correct_value(grandadvance_data):
    """Checks if if_login is set to false."""
    assert grandadvance_data["if_login"] == False, "if_login should be False."

def test_login_url_is_string(grandadvance_data):
    """Checks if login URL is a string."""
    assert isinstance(grandadvance_data["login_url"], str), "Login URL should be a string."

def test_login_url_valid_format(grandadvance_data):
     """Checks if login URL starts with 'https://'."""
     assert grandadvance_data["login_url"].startswith("https://"), "Login URL should start with 'https://'."

def test_root_category_is_integer(grandadvance_data):
    """Checks if root category is an integer."""
    assert isinstance(grandadvance_data["root_category"], int), "Root category should be an integer."

def test_root_category_correct_value(grandadvance_data):
    """Checks if the root category is set to 3."""
    assert grandadvance_data["root_category"] == 3, "Root category should be 3."

def test_collect_products_from_categorypage_is_boolean(grandadvance_data):
    """Checks if collect_products_from_categorypage is a boolean."""
    assert isinstance(grandadvance_data["collect_products_from_categorypage"], bool), "collect_products_from_categorypage should be a boolean."


def test_collect_products_from_categorypage_correct_value(grandadvance_data):
    """Checks if collect_products_from_categorypage is set to True."""
    assert grandadvance_data["collect_products_from_categorypage"] == True, "collect_products_from_categorypage should be True."

def test_scenario_files_is_list(grandadvance_data):
     """Checks if scenario_files is a list."""
     assert isinstance(grandadvance_data["scenario_files"], list), "scenario_files should be a list."

def test_scenario_files_is_empty_list(grandadvance_data):
    """Checks if scenario files list is empty."""
    assert not grandadvance_data["scenario_files"], "scenario_files should be empty."

def test_out_is_list(grandadvance_data):
     """Checks if out is a list."""
     assert isinstance(grandadvance_data["out"], list), "out should be a list."

def test_out_is_empty_list(grandadvance_data):
    """Checks if out list is empty."""
    assert not grandadvance_data["out"], "out list should be empty."

def test_last_runned_scenario_is_string(grandadvance_data):
     """Checks if last_runned_scenario is a string."""
     assert isinstance(grandadvance_data["last_runned_scenario"], str), "last_runned_scenario should be a string."

def test_last_runned_scenario_empty_string(grandadvance_data):
    """Checks if last_runned_scenario is an empty string."""
    assert grandadvance_data["last_runned_scenario"] == "", "last_runned_scenario should be an empty string."

def test_locator_description_is_string(grandadvance_data):
     """Checks if locator_description is a string."""
     assert isinstance(grandadvance_data["locator_description"], str), "locator_description should be a string."

def test_locator_description_empty_string(grandadvance_data):
    """Checks if locator_description is an empty string."""
    assert grandadvance_data["locator_description"] == "", "locator_description should be an empty string."

def test_scenario_interrupted_is_string(grandadvance_data):
     """Checks if scenario_interrupted is a string."""
     assert isinstance(grandadvance_data["scenario_interrupted"], str), "scenario_interrupted should be a string."

def test_scenario_interrupted_empty_string(grandadvance_data):
    """Checks if scenario_interrupted is an empty string."""
    assert grandadvance_data["scenario_interrupted"] == "", "scenario_interrupted should be an empty string."
```