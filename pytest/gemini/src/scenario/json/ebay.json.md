```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def ebay_config():
    """Loads the eBay configuration data from the JSON file."""
    with open("hypotez/src/scenario/json/ebay.json", 'r') as file:
        return json.load(file)

def test_ebay_config_supplier(ebay_config):
    """Checks if the supplier is correctly set to 'ebay'."""
    assert ebay_config["supplier"] == "ebay", "Supplier should be 'ebay'"

def test_ebay_config_supplier_prefix(ebay_config):
    """Checks if the supplier_prefix is correctly set to 'ebay'."""
    assert ebay_config["supplier_prefix"] == "ebay", "Supplier prefix should be 'ebay'"

def test_ebay_config_start_url(ebay_config):
    """Checks if the start_url is a valid URL."""
    assert ebay_config["start_url"].startswith("https://"), "Start URL should be a valid URL starting with https://"
    assert ebay_config["start_url"] == "https://www.ebay.com/", "Start URL is incorrect"

def test_ebay_config_price_rule(ebay_config):
    """Checks if the price_rule is set to '1'."""
    assert ebay_config["price_rule"] == "1", "Price rule should be '1'"

def test_ebay_config_supplier_id(ebay_config):
    """Checks if the supplier_id is a string and is set to '2792'."""
    assert isinstance(ebay_config["supplier_id"], str), "Supplier ID should be a string"
    assert ebay_config["supplier_id"] == "2792", "Supplier ID should be '2792'"

def test_ebay_config_num_items_4_flush(ebay_config):
    """Checks if num_items_4_flush is an integer and set to 300."""
    assert isinstance(ebay_config["num_items_4_flush"], int), "num_items_4_flush should be an integer"
    assert ebay_config["num_items_4_flush"] == 300, "num_items_4_flush should be 300"


def test_ebay_config_if_login(ebay_config):
    """Checks if if_login is a boolean and set to False."""
    assert isinstance(ebay_config["if_login"], bool), "if_login should be a boolean"
    assert ebay_config["if_login"] == False, "if_login should be False"

def test_ebay_config_parcing_method(ebay_config):
     """Checks if the parcing method is a string and set to 'web'."""
     assert isinstance(ebay_config["parcing method [webdriver|api]"], str), "Parsing method should be a string"
     assert ebay_config["parcing method [webdriver|api]"] == "web", "Parsing method should be 'web'"

def test_ebay_config_about_method(ebay_config):
     """Checks if the about method description is a string and is correct"""
     assert isinstance(ebay_config["about method web scrapping [webdriver|api]"], str), "About method should be a string"
     assert ebay_config["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver", "About method description is incorrect"

def test_ebay_config_collect_products_from_categorypage(ebay_config):
    """Checks if collect_products_from_categorypage is a boolean and set to False."""
    assert isinstance(ebay_config["collect_products_from_categorypage"], bool), "collect_products_from_categorypage should be a boolean"
    assert ebay_config["collect_products_from_categorypage"] == False, "collect_products_from_categorypage should be False"

def test_ebay_config_scenario_files(ebay_config):
    """Checks if scenario_files is a list and contains the expected files."""
    assert isinstance(ebay_config["scenario_files"], list), "scenario_files should be a list"
    expected_files = ["ebay_categories_phones_apple.json",
                      "ebay_stores_mmhfcom.json",
                      "ebay_stores_pacificindustriesltd.json",
                      "ebay_stores_thegasketsman75.json",
                      "ebay_stores_himaio12.json"]
    assert ebay_config["scenario_files"] == expected_files, "scenario_files does not contain the expected file names"


def test_ebay_config_excluded(ebay_config):
     """Checks if excluded is a list and is empty."""
     assert isinstance(ebay_config["excluded"], list), "excluded should be a list"
     assert not ebay_config["excluded"], "excluded should be an empty list"

def test_ebay_config_last_runned_scenario(ebay_config):
     """Checks if last_runned_scenario is a string and is empty."""
     assert isinstance(ebay_config["last_runned_scenario"], str), "last_runned_scenario should be a string"
     assert ebay_config["last_runned_scenario"] == "", "last_runned_scenario should be empty string"

def test_ebay_config_type(ebay_config):
    """Checks if the loaded config is a dictionary"""
    assert isinstance(ebay_config,dict), "The config should be a dictionary"

def test_ebay_config_file_not_found():
    """Tests if the file not found raises an error"""
    with pytest.raises(FileNotFoundError):
      with open ("hypotez/src/scenario/json/not_exist_file.json", 'r') as file:
        json.load(file)
```